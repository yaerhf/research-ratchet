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

MAX_DESCRIPTION = 200            # claude.ai's published limit; Claude Code states none — 200 travels


def description_too_long(meta, limit=MAX_DESCRIPTION):
    """'' when the description fits every surface this skill is published on.

    ★ Measured 2026-09-23, before the first upload: both skills were written with rich multi-sentence
    descriptions and **claude.ai caps the field at 200 characters**. A skill that cannot be uploaded
    is not a shopfront. The trigger vocabulary that does not fit belongs in the body's opening lines,
    where it still reaches the model."""
    n = len(meta.get("description", ""))
    if n <= limit:
        return ""
    return (f"{meta['name']}: description is {n} characters, over the {limit} that claude.ai "
            f"accepts — shorten it and move the rest into the body's opening lines")


def assemble(meta, body, source_stamp, home=HOME, footer=FOOTER):
    """The published SKILL.md, byte for byte. Frontmatter + body + footer, nothing improvised."""
    tools = meta.get("allowed-tools")
    front = (f"---\nname: {meta['name']}\ndescription: {meta['description']}\n"
             + (f"allowed-tools: {tools}\n" if tools else "")
             + f"license: CC BY 4.0 (docs) / MIT (code)\n---\n\n")
    return front + body.rstrip() + "\n" + footer.format(
        home=home, source=meta["source"], stamp=source_stamp)


def zip_members(meta, files):
    """What goes into the uploadable archive: the skill FOLDER as the zip's root, holding only the
    published files. `body.md` and `meta.json` are build inputs and do not travel."""
    return {f"{meta['name']}/{name}": text for name, text in files.items()}


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


def expected_files(meta, body):
    """Everything this skill publishes: the assembled SKILL.md, plus any bundled file, which is a
    COPY OF A FILE THAT LIVES IN THIS TREE — one home for the code, a generated copy in the skill,
    and the same comparison catching a hand edit of either."""
    files = {"SKILL.md": assemble(meta, body, meta.get("source_sha", "unblessed"))}
    for published, source in (meta.get("bundle") or {}).items():
        files[published] = read(ROOT / source)
    return files


def actual_files(skill_dir, names):
    out = {}
    for n in names:
        p = skill_dir / n
        out[n] = read(p) if p.is_file() else None
    return out


def every_skill():
    return sorted(p for p in SKILLS.glob("*/meta.json")) if SKILLS.is_dir() else []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="verify; write nothing")
    ap.add_argument("--bless", action="store_true",
                    help="re-record each source fingerprint (a human act, after re-reading)")
    ap.add_argument("--package", action="store_true",
                    help="write dist/<name>.zip, uploadable as-is (the folder is the zip's root)")
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

        want = expected_files(meta, body)
        too_long = description_too_long(meta)

        if a.package:
            import zipfile
            dist = ROOT / "dist"
            dist.mkdir(exist_ok=True)
            if too_long:
                print(f"[skills] REFUSED to package {meta['name']}: {too_long}")
                failures.append(too_long)
                continue
            out = dist / f"{meta['name']}.zip"
            with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
                for member, text in sorted(zip_members(meta, want).items()):
                    z.writestr(member, text)
            print(f"[skills] packaged {out.relative_to(ROOT).as_posix()} "
                  f"({', '.join(sorted(want))}) — upload this file as it is")
            continue

        if a.check:
            if drift:
                failures.append(drift)
            if too_long:
                failures.append(too_long)
            got = actual_files(d, want)
            for name in sorted(want):
                if got.get(name) != want[name]:
                    failures.append(
                        f"{meta['name']}/{name}: not what the assembler produces — it is "
                        f"generated; edit the source, then run: python scripts/gen_skills.py")
        else:
            for name, text in want.items():
                io.open(d / name, "w", encoding="utf-8", newline="").write(text)
            print(f"[skills] wrote {meta['name']}: {', '.join(sorted(want))} "
                  f"(source {meta['source']} @ {meta.get('source_sha')})")

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
    demo("limits: a description over claude.ai's 200 characters is refused before upload",
         description_too_long({**META, "description": "x" * 201}), True)
    demo("limits: CONTROL — exactly 200 characters travels",
         description_too_long({**META, "description": "x" * 200}), False)
    demo("limits: and the message says where the overflow belongs",
         "body's opening lines" in description_too_long({**META, "description": "x" * 400}), True)
    demo("package: the zip's root is the skill FOLDER, as the upload requires",
         all(k.startswith("rr-x/") for k in zip_members(META, {"SKILL.md": built})), True)
    demo("package: build inputs do not travel — only what was assembled",
         any("meta.json" in k for k in zip_members(META, {"SKILL.md": built})), False)
    demo("assembly: a pre-approved tool line reaches the frontmatter when declared",
         "allowed-tools: Bash(x *)" in assemble({**META, "allowed-tools": "Bash(x *)"},
                                                BODY, META["source_sha"]), True)
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
