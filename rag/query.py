#!/usr/bin/env python
# DIET-CLASS: TOOLING
"""RETRIEVAL QUERY — ask the record instead of bulk-loading it.

THE CLI CONTRACT (the apparatus's documents quote this form; keep it stable if
you swap the implementation for an embedding store):

    python rag/query.py "question in plain words" -k 8
    python rag/query.py "question" -k 8 --source paper
    python rag/query.py "question" --source code --full

SOURCE SHORTHANDS. `--source` filters by where a chunk lives:
    canon       the root-level binding documents
    paper       the corpus prose — the paper and its companion
    code        BOTH engines — the main engine AND the companion engine, plus the
                harnesses (a shorthand that silently covered only the main engine
                would hide half the executable ground truth; this is pinned by
                `scripts/check_records.py` § tooling coherence)
    ledgers     the standing ledgers
    prompts     the apparatus itself (roles, rules, manuals)
    scripts     the gates and instruments
    candidates  the round directories — derivations under review, persisted verdicts
    all         no filter (default)

★ DIET BOUNDS — `--role <who you are>` keeps retrieval from breaching a
starvation. The bound is not a path rule: every chunk carries the DIET CLASS of
the artifact it came from (`rag/diet.py`), and the role table says which classes
that role may receive. So the meta-observer cannot retrieve a DERIVATION, a
VERDICT or the FORMATION prefix (rule 92) wherever any of them happens to live.

    python rag/query.py "question" -k 8 --role meta-observer
    python rag/diet.py --role meta-observer FILE   # may I open this at all?

The dispatching brief's `[RETRIEVAL]` line names the role; the bound and anything
WITHHELD are PRINTED with the results, so the transcript proves what was applied.
`--exclude SUBSTR` (repeatable) narrows further. `--diet` is a deprecated alias.

WHAT IT WILL NOT RETURN. `knowledge/audit/` is not in the index, by design —
governing records are reachable only by explicit pointer, and the session
handoff's sole path is the canon's pointer line. If you need one, you must
already know it exists; that starvation is an instrument, not a gap.

Output is `[source §name]` + a scored excerpt, so what you retrieve can be
cited in the form the apparatus's rules require ('cite [source §section]').
"""
import argparse
import json
import math
import re
import sys
from pathlib import Path

try:
    from diet import ROLES, ROLE_ALIASES, check as diet_check, role_denials
except ImportError:                     # pragma: no cover
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from diet import ROLES, ROLE_ALIASES, check as diet_check, role_denials

INDEX = Path(__file__).resolve().parent / "index.json"

TOKEN = re.compile(r"[a-z0-9_]{2,}")
K1, B = 1.5, 0.75

def _in(seg):
    """Layout-robust: matches `<seg>/...` at the root AND `.../<seg>/...` nested.

    An instantiated tree keeps the apparatus at `knowledge/prompts/`; the
    research-ratchet repository itself ships it at `prompts/`. A filter that
    matched only one layout would silently return nothing in the other — which
    is the failure mode a shorthand exists to prevent.
    """
    return lambda s: s.startswith(seg + "/") or ("/" + seg + "/") in s


SOURCE_FILTERS = {
    # Root-level documents: the canon (auto-loaded, binding) and its neighbours.
    "canon": lambda s: "/" not in s and s.endswith(".md"),
    "paper": lambda s: _in("corpus")(s) and s.endswith(".md"),
    # BOTH engines and both harnesses — see the header note.
    "code": lambda s: s.endswith(".py") and (_in("corpus")(s) or _in("simulator")(s)),
    "ledgers": _in("ledgers"),
    "prompts": _in("prompts"),
    "scripts": _in("scripts"),
    # Nameable BECAUSE it is the region the starved roles must not reach: the round
    # directories hold the derivations under review and the persisted verdicts.
    "candidates": _in("candidates"),
    "all": lambda s: True,
}

# ---------------------------------------------------------------------------
# ★ DIET BOUNDS — retrieval must not silently breach a role's starvation.
#
# The whole architecture rests on some roles being STARVED: the meta-observer of
# the derivation, the re-derivation agent of the derivation and ALL verdicts, the
# checkers of the formation prefix (rule 92, ABSOLUTE). Those artifacts are in the
# index — only `knowledge/audit/` is excluded — so an unbounded query is one
# keystroke from voiding the measurement the dispatch was made to take, and it
# would leave no trace: the verdict would look identical.
#
# `--role` applies the bound mechanically and PRINTS it, so the transcript shows
# what was in force. The dispatching brief's [RETRIEVAL] line names it; the
# apparatus auditor checks the line against what was actually run. A separation
# asserted and never verified is a convention, not a control.
# ---------------------------------------------------------------------------
# ★ WHY --role AND NOT A PATH BOUND — A MEASURED DEFECT (2026-08-27).
# These path-shaped bounds were the first design, and the proxy leaked: `starved`
# allowed `prompts`, and FORMATION_CORE.md lives there — so the meta-observer's own
# bound returned the one file rule 92 (ABSOLUTE) forbids passing to a checker. A
# bound that permits an absolute breach is not a bound. `--role` replaces them by
# filtering on WHAT AN ARTIFACT IS (rag/diet.py), not on where it sits. Kept as
# aliases so existing briefs keep working — each maps to the role it stood for.
DIET_ALIASES = {"open": None, "starved": "meta-observer", "bare-statement": "rederivation"}


def tok(text):
    return TOKEN.findall(text.lower())


def load():
    if not INDEX.exists():
        print("[rag] no index found. Build it first:\n      python rag/ingest.py",
              file=sys.stderr)
        sys.exit(2)
    try:
        return json.loads(INDEX.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        print(f"[rag] index unreadable ({type(e).__name__}) — rebuild with "
              f"`python rag/ingest.py`", file=sys.stderr)
        sys.exit(2)


def search(index, question, k, source, role=None, exclude=()):
    """Filter by source shorthand, then by the ROLE's diet over CONTENT CLASSES."""
    want = SOURCE_FILTERS.get(source, SOURCE_FILTERS["all"])
    withheld = {}                       # class → how many chunks it hid, for the report

    def keep(d):
        s = d["source"]
        if any(x in s for x in exclude):
            return False
        if not want(s):
            return False
        if role:
            cls = d.get("cls", "UNCLASSIFIED")
            ok, _ = diet_check(role, cls)
            if not ok:
                withheld[cls] = withheld.get(cls, 0) + 1
                return False
        return True

    q = tok(question)
    idf, avglen = index["idf"], index["avglen"] or 1
    scored = []
    for d in index["docs"]:
        if not keep(d):
            continue
        tf, dl = d["tf"], d["len"] or 1
        s = 0.0
        for t in q:
            f = tf.get(t)
            if not f:
                continue
            s += idf.get(t, 0.0) * (f * (K1 + 1)) / (f + K1 * (1 - B + B * dl / avglen))
        if s > 0:
            scored.append((s, d))
    scored.sort(key=lambda x: -x[0])
    # `withheld` counts only chunks the DIET removed — never what --source narrowed,
    # so the report distinguishes "not asked for" from "not allowed to see".
    return scored[:k], withheld


def excerpt(text, question, width=420):
    """Show the densest window, so the hit explains itself without --full."""
    q = set(tok(question))
    lines = [l for l in text.split("\n") if l.strip()]
    if not lines:
        return text[:width]
    best, best_i = -1, 0
    for i, l in enumerate(lines):
        hits = len(q & set(tok(l)))
        if hits > best:
            best, best_i = hits, i
    out, n = [], 0
    for l in lines[max(0, best_i - 1):]:
        out.append(l)
        n += len(l)
        if n >= width:
            break
    s = "\n".join(out)
    return s if n < width else s[:width].rstrip() + " …"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("question")
    ap.add_argument("-k", type=int, default=8, help="how many chunks (default 8)")
    ap.add_argument("--source", default="all", choices=sorted(SOURCE_FILTERS),
                    help="filter by where the chunk lives")
    ap.add_argument("--role", default=None,
                    help="WHO YOU ARE dispatched as — your brief's [RETRIEVAL] line names it. "
                         "Retrieval is then bounded by what each artifact IS "
                         "(rag/diet.py). Known: " + ", ".join(sorted(ROLES)))
    ap.add_argument("--diet", default=None, choices=sorted(DIET_ALIASES),
                    help="deprecated alias for --role (open|starved|bare-statement)")
    ap.add_argument("--exclude", action="append", default=[], metavar="SUBSTR",
                    help="drop any chunk whose path contains SUBSTR (repeatable)")
    ap.add_argument("--full", action="store_true", help="print whole chunks, not excerpts")
    a = ap.parse_args()

    role = a.role or (DIET_ALIASES.get(a.diet) if a.diet else None)
    if role:
        role, denials = role_denials(role)          # normalizes aliases, rejects unknowns
    else:
        denials = {}

    index = load()
    hits, withheld = search(index, a.question, a.k, a.source, role, tuple(a.exclude))
    bound = f"  --role {role}" if role else ""
    src = "" if a.source == "all" else f"  --source {a.source}"
    if not hits:
        print(f"[rag] no match for {a.question!r}{src}{bound}.")
        print("      Retrieval is lexical: try the corpus's own vocabulary, or widen "
              "--source. Remember knowledge/audit/ is never indexed.")
    else:
        print(f"[rag] {len(hits)} hit(s) for {a.question!r}{src}{bound}")
    # THE BOUND IS PRINTED WITH THE RESULTS, ALWAYS — the transcript is the proof of
    # what was in force, and the apparatus auditor checks it against the brief's
    # [RETRIEVAL] line. Withheld classes are named but never their contents: knowing
    # that something was withheld is not knowing what it said.
    if role:
        if denials:
            print(f"      diet: {role} may not receive "
                  + ", ".join(sorted(denials)) + " — starvation is the instrument")
        else:
            print(f"      diet: {role} is saturated; nothing was withheld")
        if withheld:
            print("      WITHHELD this query: "
                  + " · ".join(f"{c} ×{n}" for c, n in sorted(withheld.items()))
                  + "  (names only — the contents stay out of your context)")
    print()
    if not hits:
        return 1
    for score, d in hits:
        print(f"  [{d['source']} §{d['name']}]  score {score:.2f}")
        body = d["text"] if a.full else excerpt(d["text"], a.question)
        for line in body.split("\n"):
            print(f"    {line}")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
