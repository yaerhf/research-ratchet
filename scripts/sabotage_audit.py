#!/usr/bin/env python
# DIET-CLASS: TOOLING
"""SABOTAGE AUDIT — break the code on purpose and find out whether the checks notice.

★ WHY. *A check never shown able to fail verifies nothing.* A green suite is evidence that nothing
broke it, and evidence of nothing else. This runs the other half: plant a defect in the region a
check CLAIMS to cover, run the checks, and see whether they go red. **A check that stays green on a
planted defect has been demonstrated not to cover it** — not argued to, demonstrated.

★ SAFETY, AND IT IS THE FIRST RULE. **Everything happens in a COPY.** The tree you point this at is
never written to. (Measured, 2026-09-03: a sabotage reverted with `git checkout` in place also
discarded ~130 lines of uncommitted work. Sabotage a copy, always.)

★ THE BASELINE IS NOT OPTIONAL. The unmodified copy is run FIRST. If the checks are already red,
every later result is void — you cannot measure whether a check fired when it was firing before you
touched anything. That is the instrument-or-yardstick rule, and it is why this tool refuses instead
of reporting.

    python scripts/sabotage_audit.py --command "pytest -q" \
        --plant "src/calc.py::return a + b::return a * b" --label "addition becomes multiplication"
    python scripts/sabotage_audit.py --command "npm test" --plan sabotages.json
    python scripts/sabotage_audit.py --self-test

WHAT THIS CANNOT SEE — stated, and pinned in `--self-test`:
  * **COVERAGE.** This is a sampling test. Every CAUGHT says one defect was caught, never that the
    suite is good; every MISSED says one defect went unnoticed, never that the suite is bad.
  * **WHICH CHECK claims which region.** It runs one command and watches its exit code. Deciding
    that a check *claimed* to cover the sabotaged line is a judgment made by whoever writes the
    plan, and the report cannot make it for them.
  * **A FLAKY SUITE.** One baseline run, one patched run. A suite that fails intermittently will
    produce CAUGHT by luck, and nothing here can tell that from a real catch.
"""
import argparse
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError, ValueError):
        pass

IGNORE = (".git", "node_modules", ".venv", "venv", "__pycache__", ".mypy_cache",
          ".pytest_cache", "dist", "build", "target", ".next", ".tox")
MAX_MB = 200


# ---- pure functions, so the demonstrations need no repository ----------------------------------

def apply_patch(text, find, replace):
    """(new_text, status). A sabotage that does not land EXACTLY once is void, never approximate:
    zero matches is a stale plan, several is an ambiguous one, and both would be reported as a
    result if this returned the text anyway."""
    n = text.count(find)
    if n == 0:
        return None, "anchor not found"
    if n > 1:
        return None, f"anchor matches {n} times — make it unique"
    return text.replace(find, replace, 1), "ok"


def verdict(baseline_exit, patched_exit):
    """What one sabotage showed. VOID when the baseline was already red: a check that was failing
    before the sabotage cannot demonstrate anything about the sabotage."""
    if baseline_exit != 0:
        return "VOID"
    return "CAUGHT" if patched_exit != 0 else "MISSED"


def summarize(rows):
    """The counts, and the one sentence this tool is allowed to say."""
    caught = sum(1 for r in rows if r["verdict"] == "CAUGHT")
    missed = sum(1 for r in rows if r["verdict"] == "MISSED")
    void = sum(1 for r in rows if r["verdict"] == "VOID")
    line = (f"{len(rows)} sabotage(s): {caught} caught, {missed} UNNOTICED, {void} void. "
            f"This is a sample, never coverage: each MISSED is a demonstrated hole, each CAUGHT "
            f"covers that one defect and says nothing about the next.")
    return {"caught": caught, "missed": missed, "void": void, "line": line}


def load_plan(text):
    """A plan is a list of {label, file, find, replace}. `claims` is optional prose for the report:
    which check was expected to notice, in the plan-writer's own words."""
    plan = json.loads(text)
    if isinstance(plan, dict):
        plan = plan.get("sabotages", [])
    out = []
    for i, item in enumerate(plan):
        missing = [k for k in ("file", "find", "replace") if not item.get(k)]
        if missing:
            raise ValueError(f"sabotage {i}: missing {', '.join(missing)}")
        item.setdefault("label", f"{item['file']}: {item['find'][:40]}")
        out.append(item)
    return out


def parse_plant(spec):
    """'file::find::replace' — the one-off form, for a single sabotage from the command line."""
    parts = spec.split("::")
    if len(parts) != 3:
        raise ValueError("--plant wants file::find::replace (:: separates the three)")
    return {"file": parts[0], "find": parts[1], "replace": parts[2],
            "label": f"{parts[0]}: {parts[1][:40]}"}


# ---- the run ------------------------------------------------------------------------------------

def tree_size_mb(root):
    total = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORE]
        for f in filenames:
            try:
                total += (Path(dirpath) / f).stat().st_size
            except OSError:
                pass
    return total / 1e6


def copy_tree(src, dst, include_git=False):
    ignore = shutil.ignore_patterns(*(i for i in IGNORE if include_git is False or i != ".git"))
    shutil.copytree(src, dst, ignore=ignore, symlinks=True)


def run(command, cwd, timeout):
    try:
        p = subprocess.run(command, cwd=cwd, shell=True, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=timeout)
        return p.returncode, (p.stdout + p.stderr)[-1500:]
    except subprocess.TimeoutExpired:
        return 124, f"the check command did not finish within {timeout}s"


def main():
    ap = argparse.ArgumentParser(description="Plant defects in a COPY and see if the checks notice.")
    ap.add_argument("--command", help="the check command, e.g. 'pytest -q'")
    ap.add_argument("--repo", default=".", help="the tree to audit (never written to)")
    ap.add_argument("--plant", action="append", default=[], help="file::find::replace")
    ap.add_argument("--label", action="append", default=[], help="a label per --plant, in order")
    ap.add_argument("--plan", help="a JSON file of sabotages")
    ap.add_argument("--timeout", type=int, default=900, help="seconds per run (900)")
    ap.add_argument("--include-git", action="store_true", help="copy .git too (slower)")
    ap.add_argument("--json", action="store_true", help="machine-readable report")
    ap.add_argument("--self-test", action="store_true", help="the demonstrations; touches nothing")
    a = ap.parse_args()
    if getattr(a, "self_test"):
        return self_test()
    if not a.command:
        print("--command is required: the check whose blind spots you are measuring")
        return 2

    repo = Path(a.repo).resolve()
    try:
        plan = load_plan(io.open(a.plan, encoding="utf-8").read()) if a.plan else []
    except (OSError, ValueError) as exc:
        print(f"plan unreadable: {exc}")
        return 2
    for i, spec in enumerate(a.plant):
        item = parse_plant(spec)
        if i < len(a.label):
            item["label"] = a.label[i]
        plan.append(item)
    if not plan:
        print("nothing to plant: pass --plant file::find::replace or --plan plan.json")
        return 2

    size = tree_size_mb(repo)
    if size > MAX_MB:
        print(f"the tree is {size:.0f} MB, over the {MAX_MB} MB guard — audit a subdirectory, "
              f"or raise MAX_MB deliberately")
        return 2

    work = Path(tempfile.mkdtemp(prefix="sabotage-"))
    rows = []
    try:
        base = work / "baseline"
        copy_tree(repo, base, a.include_git)
        print(f"== baseline: running the checks on an UNMODIFIED copy of {repo.name}")
        baseline_exit, baseline_out = run(a.command, base, a.timeout)
        if baseline_exit != 0:
            print(f"   the checks are already red on the untouched copy (exit {baseline_exit}).")
            print(f"   Nothing can be concluded about a check that was failing before the "
                  f"sabotage — fix the suite first, then audit it.")
            print(f"   last output:\n{baseline_out[-600:]}")
            return 2
        print(f"   green (exit 0) — the audit can mean something\n")

        for item in plan:
            case = work / f"case{len(rows)}"
            copy_tree(repo, case, a.include_git)
            target = case / item["file"]
            if not target.is_file():
                rows.append({**item, "verdict": "VOID", "why": "no such file in the tree"})
                continue
            text = io.open(target, encoding="utf-8", errors="replace").read()
            patched, status = apply_patch(text, item["find"], item["replace"])
            if patched is None:
                rows.append({**item, "verdict": "VOID", "why": status})
                continue
            io.open(target, "w", encoding="utf-8", newline="").write(patched)
            exit_code, out = run(a.command, case, a.timeout)
            v = verdict(baseline_exit, exit_code)
            rows.append({**item, "verdict": v, "why": f"checks exited {exit_code}",
                         "tail": out[-400:] if v == "CAUGHT" else ""})
            print(f"   [{v:<7}] {item['label']}")
            if v == "MISSED":
                print(f"             the checks stayed green with this defect in place")
    finally:
        shutil.rmtree(work, ignore_errors=True)

    s = summarize(rows)
    print(f"\n== {s['line']}")
    if s["missed"]:
        print("== unnoticed:")
        for r in rows:
            if r["verdict"] == "MISSED":
                print(f"   - {r['label']}  ({r['file']})"
                      + (f"\n     expected to be caught by: {r['claims']}" if r.get("claims") else ""))
    if a.json:
        print(json.dumps({"rows": rows, "summary": s}, indent=2, ensure_ascii=False))
    return 1 if s["missed"] else 0


# ---- the demonstrations ---------------------------------------------------------------------------

def self_test():
    cases, blind = [], []

    def demo(name, got, want):
        ok = bool(got) == want
        cases.append(ok)
        if "BLIND SPOT" in name:
            blind.append(ok)
        print(f"  [{'OK ' if ok else 'FAIL'}] {name} "
              f"({'fired' if got else 'did not fire'}; expected {'fire' if want else 'no fire'})")

    print("  SABOTAGE-AUDIT SELF-TEST — planted defects for the planter and the verdict")
    print("  " + "-" * 68)

    demo("patch: a sabotage whose anchor is not there is VOID, never approximate",
         apply_patch("a = 1\n", "b = 2", "b = 3")[0] is None, True)
    demo("patch: an anchor matching twice is VOID, and the message says why",
         "2 times" in apply_patch("x\nx\n", "x", "y")[1], True)
    demo("patch: CONTROL — a unique anchor lands exactly once",
         apply_patch("a > b\n", "a > b", "a >= b") == ("a >= b\n", "ok"), True)
    demo("verdict: checks went red on the planted defect -> CAUGHT",
         verdict(0, 1) == "CAUGHT", True)
    demo("verdict: checks stayed green on the planted defect -> MISSED (the finding)",
         verdict(0, 0) == "MISSED", True)
    demo("verdict: a baseline that was ALREADY red makes every result VOID",
         verdict(1, 1) == "VOID", True)
    demo("verdict: ...including when the patched run 'passes' (the trap this closes)",
         verdict(1, 0) == "VOID", True)
    demo("report: the summary counts the unnoticed ones",
         summarize([{"verdict": "MISSED"}, {"verdict": "CAUGHT"}])["missed"] == 1, True)
    demo("report: and it refuses to claim coverage in its own sentence",
         "never coverage" in summarize([{"verdict": "CAUGHT"}])["line"], True)
    demo("plan: a sabotage missing its replacement is refused, with the field named",
         "replace" in _err(lambda: load_plan('[{"file":"a","find":"b"}]')), True)
    demo("plan: CONTROL — a complete sabotage loads and gets a label",
         load_plan('[{"file":"a.py","find":"x","replace":"y"}]')[0]["label"], True)
    demo("sabotage: BLIND SPOT (pinned) — a CAUGHT says nothing about the next defect",
         summarize([{"verdict": "CAUGHT"}])["missed"], False)

    bad = cases.count(False)
    print("  " + "-" * 70)
    if bad:
        print(f"  SABOTAGE-AUDIT SELF-TEST: {bad} of {len(cases)} demonstrations did NOT behave as "
              f"specified — the instrument that measures other checks is itself unchecked.")
        return 1
    print(f"  SABOTAGE-AUDIT SELF-TEST: {len(cases)}/{len(cases)} demonstrations behaved as "
          f"specified — {len(blind)} of them pin{'s' if len(blind) == 1 else ''} a blind spot "
          f"(this is a sample, never coverage).")
    return 0


def _err(fn):
    try:
        fn()
        return ""
    except Exception as exc:                                  # the message IS the demonstration
        return str(exc)


if __name__ == "__main__":
    try:
        _rc = main()
    except BrokenPipeError:
        _rc = 0
    try:
        sys.stdout.flush()
    except (BrokenPipeError, OSError):
        try:
            os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        except OSError:
            pass
        _rc = 0
    sys.exit(_rc)
