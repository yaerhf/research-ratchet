#!/usr/bin/env python3
"""Generate the NEGATIVES INDEX — the bootstrap read for canon Sec.4.

R11(i) of `knowledge/audit/consolidation_2026-08-18/RULES_RESTRICTION_ANALYSIS_2026-08-21.md`
(human coordinator "adopt all", 2026-08-21). The adverse review's REMOVE 3: a worker's first
hour spends ~75,000 tokens at a 6:1 failure-to-success ratio, largely on the full negatives
ledger. The fix is NOT to stop reading the negatives — canon Sec.4's targeted-read requirement
is preserved exactly — but to read a GENERATED one-line-per-entry index first and pull the full
entry on demand.

WHAT IS GENERATED, AND WHAT IS VERBATIM
  - the ID                          : parsed from the ledger
  - a one-line TRIED/FAILED gist    : COMPRESSED, and marked as such
  - the WOULD-CHANGE-IF             : ***VERBATIM***, never compressed

The would-change-if is the re-attack handle — the one field a compression could destroy — so it
is copied byte-for-byte. Everything else in this file is a pointer, and the ledger is the record.

TOLERANCE BY DESIGN. The ledger's entry format varies (bold-run entries under a topic heading;
`##`-header entries; named non-numeric entries). The parser is best-effort: an entry it cannot
decompose is listed with its ID and a see-the-ledger note rather than dropped or guessed at.
The run reports its counts, so a parse regression is visible rather than silent.

USAGE
    PYTHONUTF8=1 python scripts/gen_negatives_index.py            # write the index
    PYTHONUTF8=1 python scripts/gen_negatives_index.py --check    # report only, write nothing
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "knowledge" / "ledgers" / "TWT_NEGATIVES_LEDGER.md"
INDEX = ROOT / "knowledge" / "ledgers" / "TWT_NEGATIVES_INDEX.md"

# An entry starts either as a `##` header or as a bold run at the head of a line.
# Both forms are in live use in the ledger; neither is going away.
RE_HEADER = re.compile(r"^##\s+(N[0-9A-Za-z′'\-]*)\s*(?:[—–-]\s*)?(.*)$")
RE_BOLD = re.compile(r"^\*\*(N[0-9A-Za-z′'\-]*)\s*(?:[—–-]\s*)(.*)$")

# Field bullets. The ledger uses "TRIED:", "FAILED BECAUSE:", "FAILED (closed) BECAUSE:",
# "WOULD CHANGE IF:", "WOULD CHANGE IF (unchanged):", "Refined would-change-if:", ...
RE_TRIED = re.compile(r"^[-*]?\s*\**\s*TRIED\b\s*\**\s*:?\s*(.*)$", re.IGNORECASE)
RE_FAILED = re.compile(r"^[-*]?\s*\**\s*FAILED\b([^:]*):\s*(.*)$", re.IGNORECASE)
RE_WCI = re.compile(
    r"^[-*]?\s*\**\s*(?:WOULD[ ‑-]CHANGE[ ‑-]IF|WOULD CHANGE IF|"
    r"REFINED WOULD-CHANGE-IF|WCI)\b(.*)$",
    re.IGNORECASE,
)


def _strip_md(text):
    """Flatten a line for the one-line gist: drop emphasis, collapse whitespace.

    ONLY `*` is stripped. Underscores and backticks are LEFT ALONE on purpose: in this
    corpus `_` is a subscript (`R_G`, `V_PMNS`, `e_4`) and stripping it silently renames
    the object the entry is about — the referent-drift class, manufactured by a tidier.
    """
    text = re.sub(r"\*+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _gist(text, limit=200):
    """Compress to one sentence-ish line. Marked COMPRESSED wherever it is printed."""
    text = _strip_md(text)
    if not text:
        return ""
    if len(text) <= limit:
        return text
    cut = text[:limit]
    # prefer a clause boundary so the compression does not end mid-word
    for sep in ("; ", ". ", ", "):
        idx = cut.rfind(sep)
        if idx > limit * 0.55:
            return cut[: idx + 1].rstrip() + " …"
    return cut.rsplit(" ", 1)[0] + " …"


def parse(lines):
    """Return (entries, topic_headings). Best-effort; never raises on odd formatting."""
    entries = []
    topics = []
    current = None
    topic = None

    for raw in lines:
        line = raw.rstrip("\n")

        m_h = RE_HEADER.match(line)
        m_b = RE_BOLD.match(line)

        if line.startswith("## ") and not m_h:
            # A topic heading that is not itself an N-entry (e.g. "CKM / generation-mixing").
            # It CLOSES the open entry: without that, an entry whose last bullet is followed
            # by a new section absorbs the whole next section and reports another entry's
            # text as its own failure line. (Found by reading the generated N0 row, whose
            # "failed" gist had come from three sections further down.)
            if current:
                entries.append(current)
                current = None
            topic = _strip_md(line[3:])
            if topic:
                topics.append(topic)
            continue

        if m_h or m_b:
            if current:
                entries.append(current)
            m = m_h or m_b
            title = _strip_md(m.group(2)).rstrip("*").strip()
            current = {
                "id": m.group(1).strip(),
                "title": title,
                "topic": topic if m_b else None,
                "tried": "",
                "failed": "",
                "wci": [],
            }
            continue

        if current is None:
            continue

        m_w = RE_WCI.match(line)
        if m_w:
            # VERBATIM: keep the whole line as written, minus a leading LIST BULLET only.
            # `\s+` is required after the marker: without it a line that opens with the
            # bold marker `**Would change if:**` loses one of its asterisks.
            current["wci"].append(re.sub(r"^[-*]\s+", "", line).strip())
            continue

        m_t = RE_TRIED.match(line)
        if m_t and not current["tried"]:
            current["tried"] = m_t.group(1)
            continue

        m_f = RE_FAILED.match(line)
        if m_f and not current["failed"]:
            current["failed"] = m_f.group(2)
            continue

    if current:
        entries.append(current)
    return entries, topics


def render(entries, topics):
    out = []
    add = out.append

    # "pointer-only" means exactly one thing everywhere in this file and in the run
    # report: no would-change-if line was parsed. That is the field the index exists to
    # carry, so it is the field the count is about.
    unparsed = [e for e in entries if not e["wci"]]

    add("# THE NEGATIVES INDEX — one line per located gap, and every WOULD-CHANGE-IF verbatim")
    add("")
    add("> **GENERATED FILE. Do not edit by hand.** Regenerate with")
    add("> `PYTHONUTF8=1 python scripts/gen_negatives_index.py`. The record is")
    add("> `knowledge/ledgers/TWT_NEGATIVES_LEDGER.md`; this is a reading aid over it.")
    add("")
    add("**What this is for.** Canon §4 requires you to read the negatives before re-opening")
    add("anything, so you neither repeat a dead end nor mistake a located gap for a wall. The full")
    add("ledger is long, and a worker's first hour was measured spending most of its budget there at")
    add("a 6:1 failure-to-success ratio. **Read this index at bootstrap; pull the FULL entry from the")
    add("ledger the moment an item is actually in your way.** The targeted-read requirement is")
    add("unchanged — this changes when you pay for it, not whether.")
    add("")
    add("**What is verbatim and what is not.** The **WOULD-CHANGE-IF is copied VERBATIM** — it is the")
    add("re-attack handle and a compression could destroy it. The tried/failed line is **COMPRESSED**")
    add("and is marked so. Never quote the compressed line as the ledger's wording, and never conclude")
    add("a route is closed from this file alone.")
    add("")
    add("**The unifying read (from the ledger, unchanged):** every entry is the same missing thing —")
    add("the unbuilt dynamical layer (the #1 gap) — seen from a different angle. **None is a")
    add("structural impossibility.**")
    add("")
    add(f"*Entries indexed: **{len(entries)}** · with a parsed would-change-if: "
        f"**{sum(1 for e in entries if e['wci'])}** · listed pointer-only: **{len(unparsed)}**.*")
    add("")
    add("---")
    add("")

    for e in entries:
        head = f"### {e['id']}"
        if e["title"]:
            head += f" — {e['title']}"
        add(head)
        if e["topic"]:
            # "preceding", not "under": the ledger appends later entries after a section
            # ends, so the nearest heading above is a locator, not always a parent.
            add(f"*(nearest ledger heading above: {e['topic']})*")
        add("")
        gist_bits = []
        if e["tried"]:
            gist_bits.append("**tried** " + _gist(e["tried"]))
        if e["failed"]:
            gist_bits.append("**failed** " + _gist(e["failed"]))
        if gist_bits:
            add("- *(COMPRESSED)* " + " · ".join(gist_bits))
        if e["wci"]:
            for w in e["wci"]:
                add(f"- **VERBATIM:** {w}")
        else:
            add("- **No would-change-if line parsed — SEE THE LEDGER ENTRY IN FULL.** "
                "(This is a parser limit, not a claim that the route has no re-entry condition; "
                "canon §4 says every dead end has one.)")
        add("")

    add("---")
    add("")
    add("## Ledger topic headings (context for the bold-run entries above)")
    add("")
    for t in topics:
        add(f"- {t}")
    add("")
    add("*Generated by `scripts/gen_negatives_index.py` from `TWT_NEGATIVES_LEDGER.md`. "
        "Counts by counting, never incremented (C-24).*")
    return "\n".join(out) + "\n"


def main(argv):
    check_only = "--check" in argv
    if not LEDGER.exists():
        print(f"ERROR: ledger not found at {LEDGER}")
        return 2
    lines = LEDGER.read_text(encoding="utf-8").splitlines()
    entries, topics = parse(lines)

    with_wci = sum(1 for e in entries if e["wci"])
    without = [e["id"] for e in entries if not e["wci"]]

    print(f"negatives index: parsed {len(entries)} entries from "
          f"{LEDGER.relative_to(ROOT)} ({len(lines)} lines)")
    print(f"  with a would-change-if : {with_wci}")
    print(f"  pointer-only           : {len(without)}"
          + (f"  -> {', '.join(without)}" if without else ""))
    print(f"  topic headings         : {len(topics)}")

    if not entries:
        print("ERROR: zero entries parsed - refusing to write an empty index.")
        return 1

    text = render(entries, topics)
    if check_only:
        print("--check: nothing written.")
        return 0
    INDEX.write_text(text, encoding="utf-8")
    print(f"wrote {INDEX.relative_to(ROOT)} ({len(text.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
