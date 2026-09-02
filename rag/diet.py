#!/usr/bin/env python
# DIET-CLASS: TOOLING
"""DIET CLASSIFICATION — what an artifact IS, so a role cannot feed itself the wrong diet.

★ THE PROBLEM THIS SOLVES, AND THE DEFECT THAT PROVED IT REAL.

The apparatus's whole architecture rests on roles being STARVED of particular
material: the meta-observer of the derivation, the re-derivation agent of the
derivation and every verdict, the checkers of the formation prefix (rule 92,
ABSOLUTE), the apparatus auditor of the authoring transcript. Those starvations
were first bounded by PATH — "the round directories are out of reach". Path is
a PROXY for the property that matters, and on 2026-08-27 the proxy leaked: the
meta-observer's own bound returned `FORMATION_CORE.md`, because that file lives
under `prompts/` and `prompts/` was allowed. **A bound that permits a breach of
an absolute rule is not a bound.**

So classification is a property of the ARTIFACT, declared on the artifact:

    <!-- DIET-CLASS: DERIVATION -->        (markdown — invisible when rendered)
    # DIET-CLASS: ENGINE                   (python and other code)

and the role table below says which classes each role may receive. Path
heuristics remain as a FALLBACK for unmarked files, and the fallback is
**fail-safe, never fail-open**: an unmarked file inside a round directory is
treated as a DERIVATION, which is the most restricted thing it could be.

★ WHAT THIS CAN AND CANNOT DO — state it plainly, because overselling a control
is the failure this apparatus is built around.

It makes an ACCIDENTAL breach hard: retrieval is filtered by role, and an agent
can check any file BEFORE opening it (`--role`). It does NOT make a deliberate
breach impossible — every checker has a file-reading tool and can open anything.
That is the same honest position as the rest of the apparatus: ~85% of the rules
have no mechanical enforcement, and the answer is never to pretend otherwise but
to make the break **cheap to declare and expensive to hide**. If you breached
your diet, say so in your verdict; a contaminated finding reported honestly is
recoverable, and one reported clean is not.

RUN
    python rag/diet.py --role meta-observer FILE [FILE...]   # may I open these?
    python rag/diet.py --role rederivation --list            # what may I see at all?
    python rag/diet.py --audit knowledge/candidates          # what is unmarked?
    python rag/diet.py --classes                             # the taxonomy
"""
import argparse
import re
import os
import sys
from pathlib import Path

# THE CONSOLE THIS PRINTS INTO MAY NOT BE UTF-8, and these tools quote DOCUMENTS — whose
# headings carry stars, arrows and em-dashes. On a cp1252 console one such character raised
# UnicodeEncodeError and killed the tool at the moment it had already found the answer.
# The founding programme's measured retrieval failure is exactly this shape: a documented
# command that silently does not run on the working box, after which retrieval stays
# "available and unused". bank.sh exports PYTHONUTF8=1; a human typing the documented form
# does not, so each entry point makes itself safe.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError, ValueError):
        pass


def _closed_pipe_exit(code):
    """Return an exit code that does not treat a CLOSED READER as a failure.

    `python rag/query.py ... | head -3` closes the pipe while we are still writing.
    On POSIX that surfaces as BrokenPipeError at the print; on Windows CPython
    raises OSError EINVAL when it flushes the std streams at interpreter shutdown
    and then exits 120. Either way, under `set -euo pipefail` — which means any
    script and any CI job — a documented, correct invocation fails the run.

    Measured 2026-09-02 (exit 120 on Windows, reproduced at >64 KB of output into
    `head -1`); found by a cold external review, which hit it twice while writing
    the install dry-run. Pointing the fd at the null device is what makes the
    interpreter's own shutdown flush a no-op.
    """
    try:
        sys.stdout.flush()
    except (BrokenPipeError, OSError):
        code = 0
    try:
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
    except (OSError, ValueError):
        pass
    return code


ROOT = Path(__file__).resolve().parent.parent

MARKER = re.compile(r"DIET-CLASS:\s*([A-Z][A-Z-]*)", re.I)
MARKER_SCAN_CHARS = 4000          # markers belong at the top of a file

# ---------------------------------------------------------------------------
# THE TAXONOMY — what an artifact is, for diet purposes only. This is NOT a
# content taxonomy: two files with identical subject matter can carry different
# diet classes (a claim's BARE STATEMENT and its DERIVATION are the same physics
# and opposite diets), and that is the entire point.
# ---------------------------------------------------------------------------
CLASSES = {
    "CANON":       "the binding canon — auto-loaded, governs everything",
    "RULES":       "the rules layer: core, role packs, activity manuals",
    "ROLE":        "a role definition (what an instrument is and is starved of)",
    "FORMATION":   "the worker formation prefix — CHECKERS MUST NEVER RECEIVE IT (rule 92)",
    "BRIEF":       "a dispatch brief: the task, its steer, its forecast",
    "CORPUS":      "the paper and companion prose",
    "ENGINE":      "executable ground truth: the engines and their harnesses",
    "LEDGER":      "a standing ledger",
    "CLAIM":       "the BARE STATEMENT of a claim — the re-derivation agent's whole diet",
    "DERIVATION":  "a worker's derivation, probe, or report — the thing checkers are starved of",
    "VERDICT":     "a persisted checker verdict",
    "GOVERNING":   "an adjudication or governing record",
    "TRANSCRIPT":  "a session transcript / an author's own account of what they meant",
    "TOOLING":     "scripts, gates and instruments",
    "PUBLIC":      "release-facing artifacts a stranger receives",
    "UNCLASSIFIED": "unknown — treated as the most restricted class that could apply",
}

# ---------------------------------------------------------------------------
# THE ROLE TABLE. `deny` is written rather than `allow` because a DENIAL carries
# a reason and an allowance does not — and the reason is what makes this
# checkable by the apparatus auditor instead of merely obeyed.
# ---------------------------------------------------------------------------
ROLES = {
    "worker": {},
    "coordinator": {},
    "reviewer": {
        "FORMATION": "rule 92 (ABSOLUTE): never pass the formation prefix to a checker — "
                     "checkers keep their own diet and outsider stance; measured result, "
                     "not caution",
    },
    "meta-observer": {
        "FORMATION": "rule 92 (ABSOLUTE): never pass the formation prefix to a checker",
        "DERIVATION": "your starvation IS your instrument — you exist to ask whether the "
                      "claim is ABOUT what it says, and a derivation captures that judgment",
        "VERDICT": "you stay isolated until your own verdict lands (RUL-079): reading another "
                   "checker's verdict makes your agreement worthless as evidence",
        "TRANSCRIPT": "a session transcript carries the derivation inside it — the starvation "
                      "is on the CONTENT, not on the filename that happens to hold it",
    },
    "keeper": {
        "FORMATION": "rule 92 (ABSOLUTE): never pass the formation prefix to a checker",
    },
    "rederivation": {
        "FORMATION": "rule 92's spirit, and worse for you: you must arrive with no route",
        "DERIVATION": "FORBIDDEN — the measurement is void from the moment you read it, and "
                      "cannot be repaired by reading less afterwards",
        "VERDICT": "FORBIDDEN — you may not know what anyone else concluded",
        "BRIEF": "the dispatching brief may name the derivation's location; you get the bare "
                 "statement and nothing else",
        "CORPUS": "the paper may contain the derivation you are re-proving",
        "GOVERNING": "an adjudication records the route and the verdicts",
        "TRANSCRIPT": "a session transcript carries the derivation inside it",
    },
    "philosopher": {},            # RUL-043 carve-out: receives FORMATION deliberately
    "contra-reviewer": {},        # same carve-out (RUL-044)
    "auditor": {
        "TRANSCRIPT": "you are starved of the authoring session and the author's account of "
                      "what they meant — the standard is what the RECORD shows, because that "
                      "is all any future worker will have",
    },
    "archivist": {
        "DERIVATION": "you handle the record's SHAPE, never its content — semantic judgment "
                      "is outside your powers, and reading derivations invites it",
    },
    "clerk": {
        "CORPUS": "starved of the research corpus: a question needing it is not a clerk "
                  "question — say so and point at the retrieval layer",
        "ENGINE": "same — you are a lookup over the registers, not a judge",
        "DERIVATION": "same",
    },
    "decision-reader": {
        "LEDGER": "you model a stranger holding the RELEASE ARTIFACT and nothing else",
        "GOVERNING": "a stranger does not have the audit tree",
        "DERIVATION": "a stranger does not have the round directories",
        "VERDICT": "a stranger does not have the verdicts",
        "BRIEF": "a stranger does not have the briefs",
        "TRANSCRIPT": "a stranger does not have the transcripts",
        "RULES": "a stranger does not have the apparatus",
        "ROLE": "a stranger does not have the apparatus",
        "FORMATION": "a stranger does not have the apparatus",
    },
}
ROLE_ALIASES = {
    "meta_observer": "meta-observer", "metaobserver": "meta-observer",
    "re-derivation": "rederivation", "re_derivation": "rederivation",
    "coherence-keeper": "keeper", "removal-auditor": "auditor",
    "apparatus-auditor": "auditor", "register-clerk": "clerk",
    "decision-attention-reader": "decision-reader", "n2": "decision-reader",
    "adversarial-reviewer": "reviewer", "fluent-worker": "worker",
}


# ---------------------------------------------------------------------------
def _heuristic(rel):
    """Path/name fallback for unmarked files. FAIL-SAFE: when a file sits in a
    round directory and says nothing about itself, it is a DERIVATION."""
    p = rel.replace("\\", "/")
    name = p.rsplit("/", 1)[-1].upper()
    parts = set(p.split("/"))

    if name in ("CLAUDE.MD",):
        return "CANON"
    if "prompts" in parts:
        if name == "FORMATION_CORE.MD":
            return "FORMATION"
        if name.startswith("RULES_") or "/manuals/" in p or name == "AGENT_RULES.MD":
            return "RULES"
        if name.endswith("_AGENT.MD") or name in (
                "META_OBSERVER.MD", "COHERENCE_KEEPER.MD", "REVIEWER_AGENT.MD",
                "REGISTER_CLERK.MD", "DECISION_ATTENTION_READER.MD", "PROFILES.MD",
                "APPARATUS_MAP.MD", "EXTERNAL_REVIEW_LOOP.MD"):
            return "ROLE"
        if "BRIEF" in name:
            return "BRIEF"
        return "RULES"
    if "ledgers" in parts:
        return "LEDGER"
    if "corpus" in parts:
        return "ENGINE" if p.endswith(".py") else "CORPUS"
    if "scripts" in parts or p.startswith("rag/"):
        return "TOOLING"
    if "audit" in parts or "candidates" in parts:
        # A round directory. Order matters: the most restricted reading wins.
        if "VERDICT" in name or "CONTRA_REVIEW" in name:
            return "VERDICT"
        if "ADJUDICATION" in name or "RECORD" in name or "INDEX" in name:
            return "GOVERNING"
        if "TRANSCRIPT" in name or "SESSION" in name:
            return "TRANSCRIPT"
        if "BRIEF" in name:
            return "BRIEF"
        if "CLAIM" in name or "STATEMENT" in name:
            return "CLAIM"
        return "DERIVATION"          # ← fail-safe default
    return "UNCLASSIFIED"


def classify(path, text=None):
    """→ (class, how) where how ∈ {marker, heuristic}. Marker always wins."""
    p = Path(path)
    rel = p.as_posix()
    try:
        rel = p.resolve().relative_to(ROOT).as_posix()
    except (ValueError, OSError):
        pass
    if text is None:
        try:
            text = p.read_text(encoding="utf-8", errors="replace")[:MARKER_SCAN_CHARS]
        except OSError:
            text = ""
    m = MARKER.search(text[:MARKER_SCAN_CHARS])
    if m:
        cls = m.group(1).upper()
        return (cls if cls in CLASSES else "UNCLASSIFIED"), "marker"
    return _heuristic(rel), "heuristic"


def role_denials(role):
    role = ROLE_ALIASES.get(role.lower().strip(), role.lower().strip())
    if role not in ROLES:
        raise SystemExit(f"[diet] unknown role {role!r}. Known: "
                         f"{', '.join(sorted(ROLES))}")
    return role, ROLES[role]


def check(role, cls):
    """→ (allowed: bool, reason: str)."""
    _, denials = role_denials(role)
    if cls in denials:
        return False, denials[cls]
    if cls == "UNCLASSIFIED":
        # Fail-safe: unknown content is refused for any role carrying ANY starvation,
        # and permitted for the saturated roles. An unmarked artifact must not be able
        # to walk past a starvation just because nobody labeled it.
        if denials:
            return False, ("UNCLASSIFIED and you carry a starvation — label the artifact "
                           "(DIET-CLASS marker) or treat it as forbidden. An unmarked file "
                           "must never be able to walk past a diet by default")
    return True, ""


# ======================================================================
# PLANTED-DEFECT DEMONSTRATIONS FOR THE STARVATIONS (W11, 2026-09-02).
#
# WHY THIS EXISTS. This module is the mechanism behind rule 92 (ABSOLUTE) and
# behind every starvation the apparatus calls an instrument. Its FIRST design was
# measured to leak on 2026-08-27 — the meta-observer's own PATH-shaped bound
# returned FORMATION_CORE.md — and it was re-cut onto the artifact's declared
# CLASS. That re-cut had never been shown able to fail, which by the gate class's
# own standard made it a phantom cite: a check never demonstrated to fire
# verifies nothing.
#
# Found by a cold external review at bf302af (2026-09-02), which counted 2 of 15
# executable tools carrying a demonstrated failure mode — and one of those two is
# never run. This closes the acute half of that finding: the tool enforcing the
# ABSOLUTE rule now carries its own demonstration.
#
# THE PREDICATES ARE PURE OVER (path, text) precisely so a demonstration can
# plant a defect and watch the check fire WITHOUT MUTATING THE TREE.
#
# Its own failure mode is demonstrated rather than assumed: deleting the
# meta-observer's TRANSCRIPT denial — a plausible tidy-up — turns exactly that
# line red and exits 1.
#
#     python rag/diet.py --self-test
# ======================================================================
_ST_FAILS = []
_ST_TOTAL = 0


def _demo(name, got, want):
    global _ST_TOTAL
    _ST_TOTAL += 1
    ok = (got == want)
    verb = "fired" if got else "did not fire"
    expect = "expected fire" if want else "expected no fire"
    print(f"  [{'OK ' if ok else 'FAIL'}] {name} ({verb}; {expect})")
    if not ok:
        _ST_FAILS.append(name)


def _denied(role, path, text=None):
    """True when `role` may NOT receive this artifact. The whole predicate."""
    cls, _how = classify(path, text)
    ok, _reason = check(role, cls)
    return not ok


def self_test():
    """Planted-defect demonstrations for the starvation predicates."""
    print("  DIET SELF-TEST — planted defects for the starvation predicates")
    print("  " + "-" * 68)

    # -- rule 92 (ABSOLUTE): no checker ever receives the formation prefix -----
    for role in ("reviewer", "meta-observer", "keeper", "rederivation"):
        _demo(f"rule 92: {role} handed FORMATION_CORE.md",
              _denied(role, "knowledge/prompts/FORMATION_CORE.md"), True)
    _demo("rule 92: CONTROL — the philosopher's RUL-043 carve-out stands",
          _denied("philosopher", "knowledge/prompts/FORMATION_CORE.md"), False)

    # -- the measured leak of 2026-08-27, pinned so it cannot silently return --
    _demo("leak-2026-08-27: the meta-observer's own bound returns FORMATION_CORE",
          _denied("meta-observer", "knowledge/prompts/FORMATION_CORE.md"), True)

    # -- a marker below the scan window is not a marker ------------------------
    _late = "# Derivation\n" + ("filler prose. " * 400) + "\n<!-- DIET-CLASS: DERIVATION -->\n"
    _demo("marker: a DERIVATION whose marker sits below MARKER_SCAN_CHARS",
          _denied("meta-observer", "knowledge/candidates/R001/deriv.md", _late), True)

    # -- unmarked files must fail SAFE, never fail OPEN ------------------------
    _demo("fail-safe: an unmarked file in a round directory",
          _denied("meta-observer", "knowledge/candidates/R001/notes.md",
                  "# route\nstep 1..."), True)
    _demo("fail-safe: an unmarked file OUTSIDE any known directory",
          _denied("meta-observer", "scratch/worker_notes.md", "# my derivation\n..."), True)
    _demo("fail-safe: an unmarked file at repo root",
          _denied("rederivation", "notes_from_author.md", "# the whole route\n..."), True)

    # -- each starvation that IS an instrument, each with its control ----------
    _demo("meta-observer: starved of the DERIVATION",
          _denied("meta-observer", "x.md", "<!-- DIET-CLASS: DERIVATION -->\n"), True)
    _demo("meta-observer: starved of another checker's VERDICT (RUL-079)",
          _denied("meta-observer", "x.md", "<!-- DIET-CLASS: VERDICT -->\n"), True)
    _demo("meta-observer: starved of a TRANSCRIPT (the derivation rides inside it)",
          _denied("meta-observer", "x.md", "<!-- DIET-CLASS: TRANSCRIPT -->\n"), True)
    _demo("meta-observer: CONTROL — the CLAIM itself is its whole diet",
          _denied("meta-observer", "x.md", "<!-- DIET-CLASS: CLAIM -->\n"), False)

    _demo("rederivation: FORBIDDEN the DERIVATION",
          _denied("rederivation", "x.md", "<!-- DIET-CLASS: DERIVATION -->\n"), True)
    _demo("rederivation: FORBIDDEN the CORPUS (the paper carries the proof)",
          _denied("rederivation", "x.md", "<!-- DIET-CLASS: CORPUS -->\n"), True)
    _demo("rederivation: FORBIDDEN a GOVERNING record (it records the route)",
          _denied("rederivation", "x.md", "<!-- DIET-CLASS: GOVERNING -->\n"), True)
    _demo("rederivation: CONTROL — the bare CLAIM passes",
          _denied("rederivation", "x.md", "<!-- DIET-CLASS: CLAIM -->\n"), False)

    _demo("auditor: starved of the authoring TRANSCRIPT",
          _denied("auditor", "x.md", "<!-- DIET-CLASS: TRANSCRIPT -->\n"), True)
    _demo("archivist: starved of DERIVATION content (shape, never semantics)",
          _denied("archivist", "x.md", "<!-- DIET-CLASS: DERIVATION -->\n"), True)
    _demo("decision-reader: starved of the apparatus (it models a stranger)",
          _denied("decision-reader", "x.md", "<!-- DIET-CLASS: RULES -->\n"), True)
    _demo("decision-reader: CONTROL — the released artifact is its whole diet",
          _denied("decision-reader", "x.md", "<!-- DIET-CLASS: PUBLIC -->\n"), False)

    # -- saturated roles must not be OVER-starved: that is a defect too --------
    _demo("keeper: CONTROL — saturated by construction, sees the result set",
          _denied("keeper", "x.md", "<!-- DIET-CLASS: DERIVATION -->\n"), False)
    _demo("worker: CONTROL — carries no starvation",
          _denied("worker", "knowledge/prompts/FORMATION_CORE.md"), False)
    _demo("coordinator: CONTROL — saturated with state",
          _denied("coordinator", "x.md", "<!-- DIET-CLASS: GOVERNING -->\n"), False)

    # -- aliases are an easy place to open a hole -----------------------------
    _demo("alias: meta_observer resolves to the starved role",
          _denied("meta_observer", "x.md", "<!-- DIET-CLASS: DERIVATION -->\n"), True)
    _demo("alias: coherence-keeper resolves to keeper, still saturated",
          _denied("coherence-keeper", "x.md", "<!-- DIET-CLASS: DERIVATION -->\n"), False)

    print("  " + "-" * 68)
    if _ST_FAILS:
        print(f"  DIET SELF-TEST: {len(_ST_FAILS)} of {_ST_TOTAL} demonstrations did NOT "
              f"behave as specified — a starvation is UNENFORCED.")
        for f in _ST_FAILS:
            print(f"      - {f}")
        print("  Fix rag/diet.py (ROLES / _heuristic) before banking. A bound that permits")
        print("  a breach of an absolute rule is not a bound.")
        return 1
    print(f"  DIET SELF-TEST: {_ST_TOTAL}/{_ST_TOTAL} demonstrations behaved as specified.")
    return 0

# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("paths", nargs="*", help="files to check")
    ap.add_argument("--role", help="the role you are dispatched as")
    ap.add_argument("--list", action="store_true", help="what this role may and may not see")
    ap.add_argument("--classes", action="store_true", help="print the taxonomy")
    ap.add_argument("--audit", metavar="DIR", help="report unmarked artifacts under DIR")
    ap.add_argument("--self-test", action="store_true",
                    help="the planted-defect demonstrations (W11)")
    a = ap.parse_args()

    if a.self_test:
        return self_test()

    if a.classes:
        print("DIET CLASSES:")
        for k, v in CLASSES.items():
            print(f"  {k:<14} {v}")
        return 0

    if a.audit:
        base = Path(a.audit)
        if not base.exists():
            print(f"[diet] {a.audit} does not exist")
            return 1
        unmarked = []
        total = 0
        for p in sorted(base.rglob("*")):
            if not p.is_file() or p.suffix not in (".md", ".py", ".txt"):
                continue
            total += 1
            cls, how = classify(p)
            if how == "heuristic":
                unmarked.append((p, cls))
        print(f"[diet] {total} artifact(s) under {a.audit}; "
              f"{total - len(unmarked)} marked, {len(unmarked)} relying on the heuristic")
        for p, cls in unmarked[:40]:
            print(f"   unmarked  {p.as_posix():<58} heuristic → {cls}")
        if unmarked:
            print("\n  A heuristic is a guess. Add a marker to each — one line at the top:")
            print("     <!-- DIET-CLASS: DERIVATION -->      (markdown)")
            print("     # DIET-CLASS: ENGINE                 (code)")
        return 0

    if a.list:
        if not a.role:
            print("[diet] --list needs --role")
            return 2
        role, denials = role_denials(a.role)
        print(f"[diet] role: {role}")
        if not denials:
            print("  SATURATED — no class is withheld from this role.")
            return 0
        print("  MAY NOT RECEIVE:")
        for cls, why in denials.items():
            print(f"    {cls:<12} {why}")
        print("  MAY RECEIVE: " + ", ".join(c for c in CLASSES
                                            if c not in denials and c != "UNCLASSIFIED"))
        return 0

    if not a.role or not a.paths:
        ap.print_help()
        return 2

    role, _ = role_denials(a.role)
    bad = 0
    print(f"[diet] role: {role}")
    for path in a.paths:
        cls, how = classify(path)
        ok, why = check(role, cls)
        mark = "ALLOWED " if ok else "FORBIDDEN"
        via = "declared" if how == "marker" else "inferred"
        print(f"  {mark}  {path}")
        print(f"            class {cls} ({via})")
        if not ok:
            print(f"            {why}")
            bad += 1
    if bad:
        print(f"\n  {bad} file(s) are outside your diet. Reading one voids the measurement "
              f"you were dispatched to make — and it would leave no trace, because your "
              f"output would look identical. If you have already read it, SAY SO in your "
              f"report rather than filing a contaminated finding as clean.")
    return 1 if bad else 0


if __name__ == "__main__":
    try:
        _rc = main()
    except BrokenPipeError:      # the reader went away; that is not our error
        _rc = 0
    sys.exit(_closed_pipe_exit(_rc))
