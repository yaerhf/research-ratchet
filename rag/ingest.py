#!/usr/bin/env python
# DIET-CLASS: TOOLING
"""RETRIEVAL INGEST — build the query index over the programme's record.

WHAT THIS IS FOR. The apparatus asks agents to QUERY the corpus rather than
bulk-load it (RULES_BY_ROLE #171; manuals/INDEX.md's doc-tree principle), and
`bank.sh` gate [3/4] re-indexes at every bank so the record stays retrievable.
The founding programme measured what happens when this layer silently breaks:
retrieval stays "available and unused" and every read-on-demand instruction
degrades into a bulk read.

★ THIS IS A REFERENCE IMPLEMENTATION, AND IT IS DELIBERATELY DEPENDENCY-FREE.
Lexical BM25 over the tree — no embeddings, no model, no network, no install.
It works on any box with Python, which is the property that matters for an
apparatus meant to be instantiated in one paste. The founding programme ran an
embedding store on a local GPU and got better recall on paraphrase; swapping
this out for one is expected and supported — keep the CLI contract in
`query.py`'s header and nothing else in the apparatus needs to change.

★ TWO SCOPE DECISIONS ARE ARCHITECTURAL, NOT CONVENIENCE:

  1. `knowledge/audit/` IS NOT INDEXED, BY DESIGN. Governing records are
     reachable only by explicit pointer — the session handoff's sole path is
     the canon's pointer line. This is a DIET implemented at the file layer,
     the same instrument as the role diets, and removing it would let an agent
     stumble onto governing records it was deliberately not given.

  2. CODE IS CHUNKED PER PRIMITIVE (via `ast`), not per file. A primitive can
     then be *queried* at a fraction of the context of reading the engine —
     which is the whole economics of the doc-tree principle. Long docstrings
     fragment this; that is a cost of the docstring, not of the chunker.

RUN
    python rag/ingest.py                 # build the index
    python rag/ingest.py --check         # report what WOULD be indexed; write nothing
    python rag/ingest.py --root PATH     # index a tree other than the repo root

The index is written to `rag/index.json` (generated; do not hand-edit, do not
commit it if your tree gitignores generated artifacts).
"""
import argparse
import ast
import json
import math
import re
import sys
from pathlib import Path

try:                                    # diet classification travels with the index
    from diet import classify          # noqa: E402  (same directory)
except ImportError:                     # pragma: no cover - diet.py is part of the layer
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from diet import classify

ROOT = Path(__file__).resolve().parent.parent
INDEX = Path(__file__).resolve().parent / "index.json"

# ---------------------------------------------------------------------------
# SCOPE. `include` is walked; `exclude` wins over it at any depth.
# ---------------------------------------------------------------------------
# Both layouts are supported deliberately: an INSTANTIATED tree keeps the apparatus
# at `knowledge/prompts/`, while the research-ratchet repository itself ships it at
# `prompts/`. Listing both means the same ingest works before and after instantiation.
INCLUDE_DIRS = ["knowledge", "scripts", "prompts", "simulator"]
# knowledge/audit is EXCLUDED BY DESIGN — see the module docstring. The rest are
# generated artifacts, caches, and archives (archives stay reachable by pointer,
# like the audit tree: they are history, not live record).
# `packs/` is EXCLUDED for the same reason `audit/` is — but a different one worth stating:
# the per-role packs are GENERATED VIEWS of RULES_CORE + RULES_BY_ROLE, so indexing them
# would put twelve near-identical copies of every core rule in front of every query and
# bury the source under its own reflections. The sources are indexed; the views are not.
EXCLUDE_PARTS = {"audit", "packs", "__pycache__", ".git", "archive", "node_modules",
                 ".venv"}
INCLUDE_SUFFIXES = {".md", ".py", ".txt"}
MAX_CHUNK_CHARS = 6000          # a chunk larger than this is split on blank lines

TOKEN = re.compile(r"[a-z0-9_]{2,}")
# Deliberately tiny: domain terms are the signal, and an over-eager stoplist in a
# research corpus removes exactly the words a methodology query needs ("not",
# "never", "only" carry meaning in a rules corpus).
STOP = {"the", "and", "for", "that", "this", "with", "from", "are", "was", "its",
        "但", "have", "has", "had", "which", "into", "than", "then", "them",
        "they", "their", "there", "here", "what", "when", "where", "would",
        "could", "should", "been", "being", "you", "your", "out", "any", "all"}


def tok(text):
    return [t for t in TOKEN.findall(text.lower()) if t not in STOP]


# ---------------------------------------------------------------------------
def chunk_markdown(text, rel):
    """Split on headings; a heading's section is the unit an agent wants back."""
    out, cur_head, cur = [], "", []
    for line in text.split("\n"):
        if re.match(r"^#{1,6}\s+\S", line):
            if cur and any(l.strip() for l in cur):
                out.append((cur_head, "\n".join(cur)))
            cur_head, cur = line.strip("# ").strip(), [line]
        else:
            cur.append(line)
    if cur and any(l.strip() for l in cur):
        out.append((cur_head, "\n".join(cur)))
    if not out:
        out = [("", text)]
    return [(h or rel, body) for h, body in out]


def chunk_python(text, rel):
    """One chunk per top-level def/class — the per-primitive rule.

    A primitive's chunk carries its FULL source (signature + docstring + body),
    because 'read the row before you reuse it' (C-18) is unenforceable if the
    retrieved chunk drops the warning the docstring carries.
    """
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return [(rel, text)]
    lines = text.split("\n")
    out = []
    head = []
    first = None
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if first is None:
                first = node.lineno - 1
            start = node.lineno - 1
            for dec in getattr(node, "decorator_list", []):
                start = min(start, dec.lineno - 1)
            end = getattr(node, "end_lineno", node.lineno)
            out.append((node.name, "\n".join(lines[start:end])))
    head = "\n".join(lines[:first]) if first else text if not out else ""
    if head.strip():
        out.insert(0, (f"{Path(rel).stem} (module header)", head))
    return out or [(rel, text)]


def split_oversized(chunks):
    out = []
    for name, body in chunks:
        if len(body) <= MAX_CHUNK_CHARS:
            out.append((name, body))
            continue
        part, acc = 1, []
        size = 0
        for para in body.split("\n\n"):
            if size + len(para) > MAX_CHUNK_CHARS and acc:
                out.append((f"{name} [{part}]", "\n\n".join(acc)))
                part, acc, size = part + 1, [], 0
            acc.append(para)
            size += len(para)
        if acc:
            out.append((f"{name} [{part}]", "\n\n".join(acc)))
    return out


# ---------------------------------------------------------------------------
def walk(root):
    for d in INCLUDE_DIRS:
        base = root / d
        if not base.exists():
            continue
        for p in sorted(base.rglob("*")):
            if not p.is_file() or p.suffix not in INCLUDE_SUFFIXES:
                continue
            if EXCLUDE_PARTS & set(p.relative_to(root).parts):
                continue
            yield p
    for p in sorted(root.glob("*.md")):          # the canon and top-level docs
        yield p


def build(root, verbose=True):
    docs, skipped = [], 0
    for p in walk(root):
        rel = p.relative_to(root).as_posix()
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            skipped += 1
            continue
        if not text.strip():
            continue
        # THE DIET CLASS IS A PROPERTY OF THE FILE, carried onto every chunk from it —
        # so retrieval can be bounded by WHAT AN ARTIFACT IS rather than by where it
        # happens to sit. Path was the first bound and it leaked (see rag/diet.py).
        cls, how = classify(p, text)
        chunks = chunk_python(text, rel) if p.suffix == ".py" else chunk_markdown(text, rel)
        for name, body in split_oversized(chunks):
            if not body.strip():
                continue
            docs.append({"source": rel, "name": name, "text": body,
                         "cls": cls, "cls_how": how})
    # BM25 statistics
    df = {}
    for d in docs:
        d["tf"] = {}
        for t in tok(d["name"] + "\n" + d["text"]):
            d["tf"][t] = d["tf"].get(t, 0) + 1
        d["len"] = sum(d["tf"].values()) or 1
        for t in d["tf"]:
            df[t] = df.get(t, 0) + 1
    n = len(docs) or 1
    idf = {t: math.log(1 + (n - c + 0.5) / (c + 0.5)) for t, c in df.items()}
    avglen = sum(d["len"] for d in docs) / n
    index = {"version": 1, "n": n, "avglen": avglen, "idf": idf,
             "docs": [{"source": d["source"], "name": d["name"], "len": d["len"],
                       "tf": d["tf"], "text": d["text"], "cls": d["cls"],
                       "cls_how": d["cls_how"]} for d in docs]}
    if verbose:
        by_src = {}
        for d in docs:
            parent = str(Path(d["source"]).parent).replace("\\", "/")
            top = "(root)" if parent == "." else parent + "/"
            by_src[top] = by_src.get(top, 0) + 1
        print(f"  indexed {len(docs)} chunks from {len(set(d['source'] for d in docs))} files"
              f"{f' ({skipped} unreadable, skipped)' if skipped else ''}")
        for k in sorted(by_src):
            print(f"    {k:<28} {by_src[k]:>5} chunks")
        print("    knowledge/audit/             NOT INDEXED (by design — pointer-only)")
        by_cls, inferred = {}, 0
        for d in docs:
            by_cls[d["cls"]] = by_cls.get(d["cls"], 0) + 1
            inferred += 1 if d["cls_how"] == "heuristic" else 0
        print("  diet classes: " + " · ".join(f"{k} {v}" for k, v in sorted(by_cls.items())))
        if inferred:
            print(f"    {inferred} chunk(s) classified by HEURISTIC, not a declared marker.")
            print("    A heuristic is a guess: `python rag/diet.py --audit <dir>` lists them.")
    return index


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="report only; write nothing")
    ap.add_argument("--root", default=str(ROOT), help="tree to index")
    a = ap.parse_args()
    root = Path(a.root).resolve()
    print(f"[rag] ingesting {root}")
    index = build(root)
    if a.check:
        print("  --check: nothing written")
        return 0
    INDEX.write_text(json.dumps(index), encoding="utf-8")
    size = INDEX.stat().st_size / 1024
    print(f"  wrote {INDEX.relative_to(root).as_posix() if INDEX.is_relative_to(root) else INDEX}"
          f" ({size:.0f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
