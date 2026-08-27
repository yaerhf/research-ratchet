#!/usr/bin/env python
"""RETRIEVAL QUERY — ask the record instead of bulk-loading it.

THE CLI CONTRACT (the apparatus's documents quote this form; keep it stable if
you swap the implementation for an embedding store):

    python rag/query.py "question in plain words" -k 8
    python rag/query.py "question" -k 8 --source paper
    python rag/query.py "question" --source code --full

SOURCE SHORTHANDS. `--source` filters by where a chunk lives:
    paper    the corpus prose — the paper and its companion
    code     BOTH engines — the main engine AND the companion engine, plus the
             harnesses (a shorthand that silently covered only the main engine
             would hide half the executable ground truth; this is pinned by
             `scripts/check_records.py` § tooling coherence)
    ledgers  the standing ledgers
    prompts  the apparatus itself (roles, rules, manuals)
    scripts  the gates and instruments
    all      no filter (default)

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
    "paper": lambda s: _in("corpus")(s) and s.endswith(".md"),
    # BOTH engines and both harnesses — see the header note.
    "code": lambda s: s.endswith(".py") and (_in("corpus")(s) or _in("simulator")(s)),
    "ledgers": _in("ledgers"),
    "prompts": _in("prompts"),
    "scripts": _in("scripts"),
    "all": lambda s: True,
}


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


def search(index, question, k, source):
    keep = SOURCE_FILTERS.get(source, SOURCE_FILTERS["all"])
    q = tok(question)
    idf, avglen = index["idf"], index["avglen"] or 1
    scored = []
    for d in index["docs"]:
        if not keep(d["source"]):
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
    return scored[:k]


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
    ap.add_argument("--full", action="store_true", help="print whole chunks, not excerpts")
    a = ap.parse_args()

    index = load()
    hits = search(index, a.question, a.k, a.source)
    if not hits:
        print(f"[rag] no match for {a.question!r}"
              f"{'' if a.source == 'all' else f' in --source {a.source}'}.")
        print("      Retrieval is lexical: try the corpus's own vocabulary, or widen "
              "--source. Remember knowledge/audit/ is never indexed.")
        return 1
    print(f"[rag] {len(hits)} hit(s) for {a.question!r}"
          f"{'' if a.source == 'all' else f'  --source {a.source}'}\n")
    for score, d in hits:
        print(f"  [{d['source']} §{d['name']}]  score {score:.2f}")
        body = d["text"] if a.full else excerpt(d["text"], a.question)
        for line in body.split("\n"):
            print(f"    {line}")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
