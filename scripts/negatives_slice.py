#!/usr/bin/env python
# DIET-CLASS: TOOLING
"""THE NEGATIVES SLICE — the dead ends near THIS step, copied whole; the rest left for the sweep.

★ WHY (C-40, 2026-10-01, on the human's word). The negatives index was the first cut at the cost of
reading every recorded dead end at every start: one line per entry, the would-change-if VERBATIM.
At scale it is no longer enough. Measured the day this was written, sizes only: the founding tree's
index is ≈ 42k tokens (estimated, characters ÷ 4) and only 3.1× smaller than its ledger, because the
verbatim conditions — kept whole on purpose — are most of it; the optical tree's is 6.4× smaller.
A record that grows with history cannot be read whole at every start. **So an agent reads the
entries KEYED to the step in hand, and the whole index is read at a named SWEEP.**

WHAT A SLICE IS, AND THE GUARDS THAT MAKE IT SAFE
  * ENTRIES COPIED BYTE FOR BYTE. A slice selects whole entry blocks from the index and never
    rewrites them: every would-change-if arrives verbatim, because it is the way back into a dead
    end and a summary is exactly what loses it.
  * THE KEY IS PRINTED with the slice, so whoever reads a brief or a verdict can see what was
    searched for and judge what a miss means.
  * AN EMPTY SLICE SAYS "NOTHING MATCHED THIS KEY" — never "nothing was tried here". An empty
    field that reads as a clear route is the failure this guards against.
  * NAMED ENTRIES ARE NEVER DROPPED: an ID given with --id is always included, whatever the cap.

HOW ENTRIES ARE CHOSEN: every ID named with --id, then the entries sharing the most informative
words with the key (each shared word weighted by how rare it is across the index), up to --top.
Deterministic: the same index and key give the same slice.

WHAT THIS CANNOT SEE — stated, and pinned in `--self-test`:
  * THE SAME DEAD END IN OTHER WORDS. Matching is on words. A route that died under one vocabulary
    and returns under another shares no key word with its entry and is not selected. That is why
    the breadth roles read the WHOLE index (the wide pass, whose job is the dead end in costume;
    the keeper; the coordinator's consolidation sweep), and why the sweep exists at all.
  * WORDS THE INDEX COMPRESSED AWAY. A key word that appears only in the full ledger entry, not in
    its compressed gist, does not select it.

RUN
    python scripts/negatives_slice.py --key "what this step is about" [--id N12 ...] [--top 12]
    python scripts/negatives_slice.py --key-file BRIEF.md            # key on a brief's own text
    python scripts/negatives_slice.py --key "..." --stats            # sizes only, no content
    python scripts/negatives_slice.py --self-test
    (--root TREE or --index FILE to slice another tree's index)
"""
import argparse
import math
import re
import sys
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError, ValueError):
        pass

ROOT = Path(__file__).resolve().parent.parent
TOP = 12            # a programme setting, not a rule: what fits its readers is its own to choose
HEAD = re.compile(r"^###\s+(\S+)")
WORD = re.compile(r"[a-z][a-z0-9]{2,}")
STOP = set("""the and for with that this from into onto over under than then them they their there
were was are been being have has had not but its it's can could would should will may might must
also only very more most such each every any all some none one two three via per our your you who
what when where which while why how out off use used using does did done make made tried failed
change would because verbatim compressed nearest ledger heading above see entry full index""".split())


# ---- pure functions, so the demonstrations need no tree -----------------------------------------

def parse(text):
    """→ [(id, block_text)] in index order. An entry is a `### ID` heading and every line up to
    the next heading or rule. Text with no such heading yields [] — the caller refuses, rather
    than guessing at a format it does not know."""
    entries, cur_id, cur = [], None, []
    for line in (text or "").splitlines():
        m = HEAD.match(line)
        if m or line.startswith("## ") or line.strip() == "---":
            if cur_id is not None:
                entries.append((cur_id, "\n".join(cur).rstrip()))
            cur_id, cur = (m.group(1), [line]) if m else (None, [])
            continue
        if cur_id is not None:
            cur.append(line)
    if cur_id is not None:
        entries.append((cur_id, "\n".join(cur).rstrip()))
    return entries


def _fold(w):
    """A plural is the same word. Measured on the first real run (the optical tree, 2026-10-01): a
    key saying `lenslet` missed the entry about `lenslets` — the one dead end that step most needed.
    Plurals only: a heavier stemmer would join words that are not the same, and a false match costs
    a reader's attention where a missed one costs the dead end."""
    return w[:-1] if len(w) > 4 and w.endswith("s") and not w.endswith("ss") else w


def words(text):
    return {_fold(w) for w in WORD.findall((text or "").lower()) if w not in STOP}


def _same_id(a, b):
    """N1 is not N12: compare whole IDs, ignoring case and a separating dash."""
    norm = lambda s: s.strip().strip("*:").upper().replace("-", "")
    return norm(a) == norm(b)


def select(entries, key="", ids=(), top=TOP):
    """→ (chosen entries in index order, key words used). Named IDs first and never capped."""
    # Tracked by POSITION. The first version tracked object identity and scored a rebuilt tuple,
    # so nothing scored was ever found again: every key selected nothing, and its own demo caught it.
    named = {pos for pos, (eid, _) in enumerate(entries) if any(_same_id(eid, i) for i in ids)}
    kw = words(key)
    n = len(entries)
    df = {}
    for _, block in entries:
        for w in words(block) & kw:
            df[w] = df.get(w, 0) + 1
    scored = []
    for pos, (_, block) in enumerate(entries):
        if pos in named:
            continue
        shared = words(block) & kw
        if shared:
            scored.append((-sum(math.log((n + 1) / (df[w] + 0.5)) for w in shared), pos))
    scored.sort()
    room = max(0, top - len(named))
    picked = named | {pos for _, pos in scored[:room]}
    return [e for pos, e in enumerate(entries) if pos in picked], sorted(kw)


def render(chosen, total, key, ids, kw):
    out = [f"## NEGATIVES SLICE — {len(chosen)} of {total} recorded dead ends (C-40)",
           f"KEY: {key.strip()[:300] or '(none)'}" + (f" · NAMED: {', '.join(ids)}" if ids else ""),
           f"KEY WORDS: {', '.join(kw) or '(none after stop-words)'}",
           ""]
    if not chosen:
        out += ["**Nothing matched this key.** That is NOT a finding that nothing was tried here:",
                "the slice matches words, and a dead end recorded in other words is not selected.",
                "Read the whole index if this step is new ground (C-40's sweep)."]
    else:
        out += [f"*{total - len(chosen)} entries NOT read here. A dead end in other words is missed by "
                f"design; the whole index is read at the sweep (C-40).*", ""]
        for _, block in chosen:
            out += [block, ""]
    return "\n".join(out).rstrip() + "\n"


# ---- the tree ----------------------------------------------------------------------------------

def find_index(root):
    led = Path(root) / "knowledge" / "ledgers"
    hits = sorted(p for p in led.glob("*.md") if p.name.upper().endswith("NEGATIVES_INDEX.MD")) \
        if led.is_dir() else []
    return hits[0] if hits else None


def main():
    ap = argparse.ArgumentParser(description="The dead ends near this step, copied whole (C-40).")
    ap.add_argument("--key", action="append", default=[], help="what this step is about")
    ap.add_argument("--key-file", help="use a brief's own text as the key")
    ap.add_argument("--id", action="append", default=[], help="an entry ID always to include")
    ap.add_argument("--top", type=int, default=TOP, help=f"entries at most, named ones aside ({TOP})")
    ap.add_argument("--root", default=str(ROOT), help="the tree whose index to slice")
    ap.add_argument("--index", help="the index file itself")
    ap.add_argument("--stats", action="store_true", help="sizes only — prints no content")
    ap.add_argument("--self-test", action="store_true", help="the demonstrations")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    idx = Path(a.index) if a.index else find_index(a.root)
    if idx is None or not idx.is_file():
        print("[slice] no negatives index found (knowledge/ledgers/*NEGATIVES_INDEX.md). "
              "Generate it: python scripts/gen_negatives_index.py")
        return 2
    text = idx.read_text(encoding="utf-8", errors="replace")
    entries = parse(text)
    if not entries:
        print(f"[slice] {idx.name}: no `### ID` entries recognized — this tool does not guess at "
              f"a format it does not know. Read the index whole, and say so.")
        return 2
    key = " ".join(a.key)
    if a.key_file:
        key += " " + Path(a.key_file).read_text(encoding="utf-8", errors="replace")
    chosen, kw = select(entries, key, a.id, a.top)
    out = render(chosen, len(entries), key, a.id, kw)
    if a.stats:
        print(f"[slice] {idx.name}: {len(entries)} entries, {len(text):,} characters "
              f"(≈ {len(text) // 4:,} tokens, estimated)")
        print(f"[slice] this key selects {len(chosen)} entries: {len(out):,} characters "
              f"(≈ {len(out) // 4:,} tokens, estimated) — {len(out) / max(len(text), 1):.1%} of the "
              f"index")
        return 0
    print(out, end="")
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

    print("  NEGATIVES-SLICE SELF-TEST — planted defects for the key, the copy and the empty slice")
    print("  " + "-" * 68)

    INDEX = "\n".join([
        "# NEGATIVES INDEX", "", "---", "",
        "### N1 — cache in the edge runtime",
        "- *(COMPRESSED)* **tried** sqlite cache · **failed** native modules unsupported",
        "- **VERBATIM:** would change if the runtime gains native module support", "",
        "### N12 — spectral fit of the kernel",
        "- *(COMPRESSED)* **tried** polynomial kernel · **failed** diverges at high frequency",
        "- **VERBATIM:** would change if a damping term is derived rather than fitted", "",
        "### N13 — kernel normalisation",
        "- *(COMPRESSED)* **tried** unit normalisation · **failed** breaks the cache invariant",
        "- **VERBATIM:** would change if the invariant is shown to be conventional", "",
        "---", "", "## Ledger topic headings", "- topics"])
    E = parse(INDEX)
    ids = [e[0] for e in E]
    demo("parse: CONTROL — three entries, the trailing topic list is not an entry",
         ids != ["N1", "N12", "N13"], False)
    demo("parse: text with no `### ID` entries yields nothing (the tool then refuses, never guesses)",
         parse("N1: a line\nN2: another line\n"), False)

    pick = lambda **k: [e[0] for e in select(E, **k)[0]]
    demo("key: an entry sharing the key's words is selected", "N12" in pick(key="kernel diverges"),
         True)
    demo("key: a PLURAL in the key finds the singular in the entry (found live: lenslets/lenslet)",
         "N12" not in pick(key="kernels"), False)
    demo("key: CONTROL — an entry sharing none of them is not",
         "N1" in pick(key="kernel diverges"), False)
    # `cache` is in two entries and `spectral` in one: with room for one, the rarer word wins.
    demo("key: the RARER shared word decides the order (spectral, in one entry, beats cache, in two)",
         select(E, key="cache spectral", top=1)[0][0][0] != "N12", False)
    demo("named: an ID given by name is included even when no word matches",
         "N1" not in pick(key="damping", ids=["N1"]), False)
    demo("named: N1 does not drag in N12 or N13 (whole IDs, not prefixes)",
         {"N12", "N13"} & set(pick(key="", ids=["N1"])), False)
    demo("named: a named entry is never dropped by the cap",
         "N1" not in pick(key="kernel spectral normalisation", ids=["N1"], top=1), False)
    demo("key: a key made only of stop-words selects nothing, not everything",
         pick(key="the and would change"), False)

    chosen = select(E, key="damping")[0]
    demo("copy: the selected entry is the index's block BYTE FOR BYTE (would-change-if verbatim)",
         not chosen or chosen[0][1] not in INDEX or "would change if a damping term is derived "
                                                    "rather than fitted" not in chosen[0][1], False)
    # The demo above checks what select() returns. The sabotage audit cut each PRINTED entry to its
    # heading and every demo stayed green (2026-10-01): the copy has to be checked where it is read.
    demo("copy: the PRINTED slice carries each selected entry whole, would-change-if included",
         not chosen or chosen[0][1] not in render(chosen, len(E), "damping", [], ["damping"]),
         False)
    empty = render([], len(E), "quantum gravity", [], ["gravity", "quantum"])
    demo("empty: an empty slice says NOTHING MATCHED THIS KEY",
         "Nothing matched this key" not in empty, False)
    demo("empty: and never that nothing was tried, or that the route is clear",
         any(s in empty.lower() for s in ("no dead ends", "route is clear", "clear route")),
         False)
    demo("render: CONTROL — the key is printed with the slice",
         "KEY: damping" not in render(chosen, len(E), "damping", [], ["damping"]), False)

    demo("slice: BLIND SPOT (pinned) — the same dead end in OTHER WORDS is not selected",
         "N1" in pick(key="memoization layer on serverless workers"), False)
    demo("slice: BLIND SPOT (pinned) — a word only the full ledger entry holds selects nothing",
         pick(key="libsqlite3 binding segfault"), False)

    bad = cases.count(False)
    print("  " + "-" * 70)
    if bad:
        print(f"  NEGATIVES-SLICE SELF-TEST: {bad} of {len(cases)} demonstrations did NOT behave as "
              f"specified — a slice could drop a dead end or claim a clear route.")
        return 1
    print(f"  NEGATIVES-SLICE SELF-TEST: {len(cases)}/{len(cases)} demonstrations behaved as "
          f"specified — {len(blind)} of them pin a blind spot (matching is on words; the sweep "
          f"covers what it misses).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
