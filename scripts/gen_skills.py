#!/usr/bin/env python
# DIET-CLASS: TOOLING
"""ASSEMBLE THE PUBLISHED SKILLS — and keep each one tied to the manual it was derived from.

★ WHY THIS EXISTS. A skill is published OUTWARD: it ends up in strangers' sessions, where nothing
reports back. **A copy in somebody else's hands is a drift pair with the worst feedback loop there
is** — the apparatus moves, the copy does not, and nobody tells you. The role packs solved this
shape for generated views; a skill is NOT a mechanical projection of its manual (it is written for
a reader who has none of this apparatus), so it needs the other half of the same idea:

  * `SKILL.md` is ASSEMBLED, never hand-edited — frontmatter + body + the standard footer. The
    check rebuilds it and compares the TEXT, so an edit to the published file is caught.
  * the body is a HAND-WRITTEN derivation of a manual, and `meta.json` records **the fingerprint of
    that manual as it stood when a human last blessed the derivation.** Move the manual and the
    check fails: not because the skill is wrong, but because **nobody has re-read it against what
    the apparatus now says.**

    python scripts/gen_skills.py            # assemble every SKILL.md
    python scripts/gen_skills.py --check    # verify; write nothing
    python scripts/gen_skills.py --bless    # re-record the source fingerprints (a human act)
    python scripts/gen_skills.py --self-test

WHAT THIS CANNOT SEE — stated, and pinned in `--self-test`:
  * **WHETHER THE DERIVATION IS FAITHFUL.** A body that contradicts its manual passes, as long as
    the manual has not moved since somebody blessed it. This check tracks PROVENANCE, not meaning;
    only a person re-reading the two can say the skill still says what the apparatus says.
  * **WHAT A PUBLISHED COPY OUT THERE CONTAINS.** Once it is installed in a stranger's session it
    is beyond every gate here. That is the reason for the footer and the version line, not a gap
    this file can close.
"""
import argparse
import hashlib
import io
import json
import os
import sys
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError, ValueError):
        pass

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"

FOOTER = """
---

*This skill is one activity from **research-ratchet**, a methodological apparatus for
AI-assisted research under a human coordinator: {home}*

*What you get here is the discipline. **The apparatus adds what a single session cannot:** roles
that are starved of information so their agreement means something, gates that refuse a commit
until its checks have been shown able to fail, and records that outlive the conversation. If this
was useful, that is where it comes from.*

*Docs CC BY 4.0, code MIT. Derived from `{source}` at {stamp}.*
"""

HOME = "https://github.com/yaerhf/research-ratchet"


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def read(path):
    return io.open(path, encoding="utf-8").read()


# ---- pure functions, so the demonstrations need no files ---------------------------------------

def assemble(meta, body, source_stamp, home=HOME, footer=FOOTER):
    """The published SKILL.md, byte for byte. Frontmatter + body + footer, nothing improvised."""
    front = (f"---\nname: {meta['name']}\ndescription: {meta['description']}\n"
             f"license: CC BY 4.0 (docs) / MIT (code)\n---\n\n")
    return front + body.rstrip() + "\n" + footer.format(
        home=home, source=meta["source"], stamp=source_stamp)


def provenance_drift(meta, source_text):
    """'' when the source manual is where the blessing left it; otherwise what moved and the fix."""
    recorded = meta.get("source_sha")
    current = sha(source_text)
    if recorded == current:
        return ""
    return (f"{meta['name']}: {meta['source']} has changed since this skill was last blessed "
            f"({recorded} -> {current}). Re-read the skill against the manual; if it still says "
            f"what the apparatus says, run: python scripts/gen_skills.py --bless")


def stale_skills(expected, actual):
    """Published files that are not exactly what the assembler produces, in either direction."""
    names = set(expected) | set(actual)
    return sorted(n for n in names if actual.get(n) != expected.get(n))


# ---- the run -----------------------------------------------------------------------------------

def load(skill_dir):
    meta = json.loads(read(skill_dir / "meta.json"))
    body = read(skill_dir / "body.md")
    source_text = read(ROOT / meta["source"])
    return meta, body, source_text


def every_skill():
    return sorted(p for p in SKILLS.glob("*/meta.json")) if SKILLS.is_dir() else []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="verify; write nothing")
    ap.add_argument("--bless", action="store_true",
                    help="re-record each source fingerprint (a human act, after re-reading)")
    ap.add_argument("--self-test", action="store_true", help="the demonstrations")
    a = ap.parse_args()
    if getattr(a, "self_test"):
        return self_test()

    metas = every_skill()
    if not metas:
        print("[skills] no skills in skills/ — nothing to assemble")
        return 0

    failures, blessed = [], []
    for meta_path in metas:
        d = meta_path.parent
        meta, body, source_text = load(d)
        drift = provenance_drift(meta, source_text)

        if a.bless:
            meta["source_sha"] = sha(source_text)
            io.open(meta_path, "w", encoding="utf-8", newline="").write(
                json.dumps(meta, indent=2, ensure_ascii=False) + "\n")
            blessed.append(meta["name"])
            drift = ""

        text = assemble(meta, body, meta.get("source_sha", "unblessed"))
        out = d / "SKILL.md"
        if a.check:
            if drift:
                failures.append(drift)
            if not out.exists() or read(out) != text:
                failures.append(f"{meta['name']}: SKILL.md is not what the assembler produces — "
                                f"it is generated; edit body.md or meta.json, then run: "
                                f"python scripts/gen_skills.py")
        else:
            io.open(out, "w", encoding="utf-8", newline="").write(text)
            print(f"[skills] wrote {out.relative_to(ROOT).as_posix()} "
                  f"({len(text.split())} words, source {meta['source']} @ "
                  f"{meta.get('source_sha')})")

    if a.bless:
        print(f"[skills] blessed: {', '.join(blessed)} — the record now says a human re-read them")
        return 0
    if a.check:
        if failures:
            print(f"[skills] NOT CURRENT — {len(failures)} finding(s):")
            for f in failures:
                print(f"        {f}")
            return 1
        print(f"[skills] all {len(metas)} skill(s) assembled as published, each tied to the manual "
              f"it was derived from (provenance, not fidelity — see --self-test)")
    return 0


# ---- the demonstrations -------------------------------------------------------------------------

def self_test():
    cases, blind = [], []

    def demo(name, got, want):
        ok = bool(got) == want
        cases.append(ok)
        if "BLIND SPOT" in name:
            blind.append(ok)
        print(f"  [{'OK ' if ok else 'FAIL'}] {name} "
              f"({'fired' if got else 'did not fire'}; expected {'fire' if want else 'no fire'})")

    print("  SKILLS SELF-TEST — planted defects for the assembler and the provenance tie")
    print("  " + "-" * 68)

    MANUAL = "# manual\nthe rule, as the apparatus states it.\n"
    META = {"name": "rr-x", "description": "d", "source": "manuals/x.md",
            "source_sha": sha(MANUAL)}
    BODY = "# skill\nthe rule, for a reader who has none of this.\n"

    demo("provenance: the manual moved after the skill was blessed",
         provenance_drift(META, MANUAL + "a new paragraph nobody carried across\n"), True)
    demo("provenance: CONTROL — the manual is where the blessing left it",
         provenance_drift(META, MANUAL), False)
    demo("provenance: the fix names the command that re-blesses it",
         "--bless" in provenance_drift(META, MANUAL + "x"), True)

    built = assemble(META, BODY, META["source_sha"])
    demo("assembly: the published file carries the trigger description",
         "description: d" in built, True)
    demo("assembly: it points home, so the output can travel alone",
         HOME in built, True)
    demo("assembly: it says what the apparatus adds that a session cannot",
         "gates that refuse" in built, True)
    demo("assembly: a hand-edited SKILL.md is not what the assembler produces",
         stale_skills({"rr-x": built}, {"rr-x": built.replace("the rule", "a rule")}), True)
    demo("assembly: a skill file with no source in skills/ is caught too",
         stale_skills({"rr-x": built}, {"rr-x": built, "rr-ghost": "# orphan\n"}), True)
    demo("assembly: CONTROL — untouched output matches",
         stale_skills({"rr-x": built}, {"rr-x": built}), False)
    demo("skills: BLIND SPOT (pinned) — a body that CONTRADICTS its manual passes",
         provenance_drift(META, MANUAL)
         or stale_skills({"rr-x": assemble(META, "# skill\nthe opposite of the rule.\n",
                                           META["source_sha"])},
                         {"rr-x": assemble(META, "# skill\nthe opposite of the rule.\n",
                                           META["source_sha"])}), False)

    bad = cases.count(False)
    print("  " + "-" * 70)
    if bad:
        print(f"  SKILLS SELF-TEST: {bad} of {len(cases)} demonstrations did NOT behave as "
              f"specified — the tie between a published skill and its manual is unreliable.")
        return 1
    print(f"  SKILLS SELF-TEST: {len(cases)}/{len(cases)} demonstrations behaved as specified — "
          f"{len(blind)} of them pin{'s' if len(blind) == 1 else ''} a blind spot (this gate "
          f"tracks PROVENANCE, never fidelity).")
    return 0


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
