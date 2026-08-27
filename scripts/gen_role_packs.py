#!/usr/bin/env python
# DIET-CLASS: TOOLING
"""GENERATE THE PER-ROLE RULE PACKS — one self-contained document per role.

★ THE MEASUREMENT THAT FORCED THIS (W1 first pass, 2026-08-27).

`RULES_BY_ROLE.md` is ~15,600 tokens and was being read WHOLE by every dispatch that
needed a pack — because a file path handed to an agent gets read as a file. A role's
actual pack is 2–3k. So roughly **12,000 tokens per dispatch were spent delivering rules
that bind somebody else**, against a recorded fixed overhead of ~20,000 tokens for a
probe-scale dispatch: over half of it, for nothing.

This emits ONE self-contained document per role — the organigramme, the common core, that
role's own rules, its activity blocks, and the manuals INDEX — so a dispatch loads one
file instead of two large ones and reads nothing that binds another role.

★ THE FIX IS GENERATION, NOT DELETION, AND THE DIFFERENCE MATTERS. Nothing is removed and
no rule moves house: `RULES_CORE.md` and `RULES_BY_ROLE.md` remain the sources and the
authority. A pack is a VIEW. The alternative — centralising shared text behind pointers —
was considered and refused: each block is load-bearing at the point of use, and *a role
that must follow a pointer to learn its own diet bound is a role that will sometimes not
follow it*. The manuals principle is explicit that a document must be COMPLETE for its
activity.

★ THE HAZARD THIS CREATES, NAMED. A generated view that drifts from its source is a drift
pair with a build step in front of it. Two guards: every pack carries a FINGERPRINT of the
sources it was cut from, and `check_records.py` fails the bank if any pack is stale.
Regenerate at every consolidation and whenever the rules change:

    python scripts/gen_role_packs.py            # write the packs
    python scripts/gen_role_packs.py --check    # verify currency; write nothing
"""
import argparse
import hashlib
import io
import re
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

ROOT = Path(__file__).resolve().parent.parent


def apparatus_dir():
    for c in ("knowledge/prompts", "prompts"):
        if (ROOT / c).is_dir():
            return ROOT / c
    raise SystemExit("[packs] no apparatus directory found")


AP = apparatus_dir()
OUT = AP / "packs"

# role -> (section number in RULES_BY_ROLE, activity block letters, role file)
ROLES = {
    "worker":          ("1", ["B", "P", "S"], "FORMATION_CORE.md"),
    "coordinator":     ("2", ["B", "P", "X"], "coordinator_agent.md"),
    "reviewer":        ("3", ["X"],           "reviewer_agent.md"),
    "meta-observer":   ("4", ["X"],           "meta_observer.md"),
    "keeper":          ("5", ["X"],           "coherence_keeper.md"),
    "philosopher":     ("6", ["X", "P"],      "philosopher_ledger_agent.md"),
    "archivist":       ("7", ["B"],           "archivist_agent.md"),
    "auditor":         ("8", [],              "removal_auditor_agent.md"),
    "external-loop":   ("9", ["P"],           "external_review_loop.md"),
    "rederivation":    (None, ["X"],          "rederivation_agent.md"),
    "clerk":           (None, [],             "register_clerk.md"),
    "decision-reader": (None, [],             "decision_attention_reader.md"),
}

BLOCK_NAMES = {"B": "BANKING PASS", "P": "PAPER & RELEASE", "X": "ANY CHECKING ROLE",
               "S": "SIMULATOR CAMPAIGN"}

# ---------------------------------------------------------------------------
# THE ORGANIGRAMME, compact — every role carries it, so every instance can see where it
# sits and what else is watching. Text rather than a diagram: this ships in every pack,
# and the whole point of the exercise is not to spend tokens twice.
#
# ★ THE SPIRIT LINE NAMES NO AGENT AND NO CADENCE, DELIBERATELY (human coordinator,
# 2026-08-27: "the worker doesn't even know if the audit is systematic or sampled").
# Attributing the question to THE APPARATUS rather than to a named role withholds more
# than a frequency: it withholds whether an audit is a standing process or a draw. Saying
# "available, and it draws its own sample" would already have answered that. The role's
# own file states its cadence, because the instrument needs to know it; nothing an
# ordinary role reads does. Its value depends on being BELIEVED to be callable, and a
# deterrent whose rate is published is a cost an agent can price and accept.
ORGANIGRAMME = """## THE APPARATUS — where you sit

```
              EXTERNAL REVIEWER   cold; sees only the released artifact; owes us nothing
                      |           (the release goes out from the human's own surface — fence F1)
              HUMAN COORDINATOR   owns the ontology · rules · ratifies
                      |
                AI COORDINATOR    saturated with STATE; dispatches, triages, escalates
                      |           cannot tier, bank, rule freely, or edit the canon
        +-------------+--------------+
    FLUENT WORKERS            THE INNER CHECK (§8a, cross-class on AUTHORSHIP)
    formation + one brief       REVIEWER          saturated with the derivation
    derive · bank nothing       META-OBSERVER     STARVED of the derivation
                                KEEPER            saturated with the whole result set
                                RE-DERIVATION     the claim's bare statement only
        +-------------+--------------+
    PHILOSOPHER               THE APPARATUS WATCHES ITSELF
    starved of our              APPARATUS AUDITOR · DECISION-ATTENTION READER
    derivations,                ARCHIVIST · REGISTER CLERK
    saturated with RIVALS
                      |
              THE DATA BANK     bank.sh is the only way in: suites green -> records gate
                                -> re-index -> sweep-guarded commit. The record then feeds
                                formation and diet-bounded retrieval back to the workers.
```

**Read it by DIET, not by hierarchy.** Every instrument is defined by what it is *starved
of* and what it is *saturated with*. Merging two roles destroys a measurement, not merely
tidiness.

**THE APPARATUS asks whether the SPIRIT of the rules was served, not whether the letter was
followed:** a recorded, reasoned break is **compliance**, and what it hunts is a rule followed
to the letter while the thing the rule exists to produce did not happen — a sweep that touched
every site and fixed nothing, a tier tag technically defensible and misleading, a check that
passes and verifies nothing. That is the class no gate reaches and no per-claim reviewer is
looking for. It never adjudicates the research; §8a does that.
"""


def read(p):
    return io.open(p, encoding="utf-8").read()


def fingerprint(*texts):
    h = hashlib.sha1()
    for t in texts:
        h.update(t.encode("utf-8"))
    return h.hexdigest()[:12]


def section(text, heading_re, stop_re=r"(?m)^## "):
    """Extract one '## ' section, heading included, up to the next '## '."""
    m = re.search(heading_re, text)
    if not m:
        return None
    rest = text[m.start():]
    nxt = re.search(stop_re, rest[1:])
    return rest[:nxt.start() + 1] if nxt else rest


def strip_marker(text):
    return re.sub(r"^<!-- DIET-CLASS:[^>]*-->\n", "", text)


def build(role, spec, core, byrole, manuals_index):
    sec_no, blocks, role_file = spec
    parts = []
    fp = fingerprint(core, byrole)

    parts.append(f"""<!-- DIET-CLASS: RULES -->
<!-- GENERATED FILE — do not edit. Regenerate: python scripts/gen_role_packs.py
     sources: RULES_CORE.md + RULES_BY_ROLE.md · fingerprint {fp}
     check_records.py fails the bank if this pack is stale. -->
# RULE PACK — {role.upper()}

**Everything binding on you, in one document.** The core that binds every role, your own
rules, your activity blocks, and the manuals you may need to open. Generated from
`RULES_CORE.md` and `RULES_BY_ROLE.md`, which remain the sources and the authority — this
is a VIEW, and no rule moved house to make it.

**Your role's own definition — diet, powers, verdict vocabulary — is `{role_file}`.**
Read that with this.
""")

    parts.append(ORGANIGRAMME)
    parts.append("\n---\n\n# PART 1 — THE COMMON CORE (binds every role)\n")
    parts.append(strip_marker(core))

    if sec_no:
        sec = section(byrole, rf"(?m)^## {sec_no}\. ")
        if sec:
            parts.append("\n---\n\n# PART 2 — YOUR PACK\n")
            parts.append(sec)
    else:
        parts.append(f"""
---

# PART 2 — YOUR PACK

**You have no pack rows of your own**, and that is a finding of the rules split rather than
an omission: what makes you what you are is your DIET and your verdict vocabulary, which
live in `{role_file}`, not in the rule inventory.
""")

    if blocks:
        parts.append("\n---\n\n# PART 3 — YOUR ACTIVITY BLOCKS\n")
        parts.append("*You take a block when you do the activity, whatever your role.*\n")
        for b in blocks:
            sec = section(byrole, rf"(?m)^## {b}\. ")
            if sec:
                parts.append(sec)

    parts.append(f"""
---

# PART 4 — THE MANUALS

**Start knowing the NAMES; open one only when you are about to do that activity.** A manual
is COMPLETE for its activity: read it and you need nothing else to act correctly.

{manuals_index}
""")
    return "\n".join(parts), fp


def manuals_table(ap):
    idx = read(ap / "manuals" / "INDEX.md")
    rows = re.findall(r"(?m)^\|\s*`([a-z_]+\.md)`\s*\|([^|]+)\|\s*\*\*WRITTEN\*\*", idx)
    if not rows:
        return "*(no manuals written yet)*"
    out = ["| manual | read it if you are about to… |", "|---|---|"]
    for name, trig in rows:
        out.append(f"| `manuals/{name}` |{trig}|")
    owed = re.findall(r"(?m)^\|\s*`([a-z_]+\.md)`\s*\|[^|]+\|\s*owed\s*\|", idx)
    if owed:
        out.append("")
        out.append("*Owed (their rules still live in the packs above, and remain binding): "
                   + ", ".join(f"`{o}`" for o in owed) + ".*")
    return "\n".join(out)


def main():
    ap_ = argparse.ArgumentParser()
    ap_.add_argument("--check", action="store_true",
                     help="verify every pack is current; write nothing")
    a = ap_.parse_args()

    core = read(AP / "RULES_CORE.md")
    byrole = read(AP / "RULES_BY_ROLE.md")
    mans = manuals_table(AP)
    fp = fingerprint(core, byrole)

    if a.check:
        stale, missing = [], []
        for role in ROLES:
            p = OUT / f"{role}.md"
            if not p.exists():
                missing.append(role)
                continue
            m = re.search(r"fingerprint ([0-9a-f]{12})", read(p))
            if not m or m.group(1) != fp:
                stale.append(role)
        if missing or stale:
            print(f"[packs] STALE — sources fingerprint {fp}")
            if missing:
                print(f"        missing: {', '.join(missing)}")
            if stale:
                print(f"        stale:   {', '.join(stale)}")
            print("        regenerate: python scripts/gen_role_packs.py")
            return 1
        print(f"[packs] all {len(ROLES)} packs current (fingerprint {fp})")
        return 0

    OUT.mkdir(parents=True, exist_ok=True)
    tot_before = (len(core) + len(byrole)) // 4
    sizes = []
    for role, spec in ROLES.items():
        text, _ = build(role, spec, core, byrole, mans)
        io.open(OUT / f"{role}.md", "w", encoding="utf-8", newline="").write(text)
        sizes.append((role, len(text) // 4))
    print(f"[packs] wrote {len(sizes)} packs to {OUT.relative_to(ROOT).as_posix()}/ "
          f"(fingerprint {fp})")
    print(f"  a role previously loaded core + the whole role file: ~{tot_before} tokens")
    for role, n in sorted(sizes, key=lambda kv: kv[1]):
        print(f"    {role:<18}{n:>6}   saves ~{tot_before - n:>6}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
