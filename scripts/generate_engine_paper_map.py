#!/usr/bin/env python3
"""Generate TWT_V2_ENGINE_PAPER_MAP.md by mechanical scan.

CLAUDE.md §10 coverage-discipline tool. Reproducible: running twice gives
the same output. Reads:
  - knowledge/corpus/twt.py                (the engine)
  - knowledge/corpus/TWT_foundational_paper.md (the paper)

Detects paper §-headers in BOTH styles:
  - ATX:   `^##+ §X.Y[.Z]...`
  - BOLD:  `^\\*\\*§X.Y[.Z]... ...\\*\\*`   (V2 uses this for §19.8.1/2/3)

This was the missing detector — ATX-only scan reported the bold sub-headers
as drift even though they exist as bold sub-headers in the paper.

For each engine primitive (top-level, non-_-prefixed def), the script:
  1. extracts the §-refs from its docstring + body
       (catching `§X.Y` and `§X.Y.Z`, with or without trailing ✓ check-marks,
        plus the legacy `Sec X.Y` form some older engine docstrings use)
  2. classifies each §-ref as PRESENT (in ATX ∪ BOLD header set) or DRIFT
  3. greps the paper prose for the function name (if name ≥ 8 chars) to mark CITED
  4. emits the structured map (§A DRIFT, §B CITED, §C DECLARED, §D ORPHAN-internal,
     §E ORPHAN-needs-review, §F method notes) congruent with the existing layout.

Usage:
    python scripts/generate_engine_paper_map.py            # dry-run, prints summary
    python scripts/generate_engine_paper_map.py --write    # overwrite the map
    python scripts/generate_engine_paper_map.py --write --out PATH   # write elsewhere

Design note: function-body extraction uses Python's `ast` module (not a
slice-to-next-def heuristic). This matters: a `# ---- §X.Y` section-comment
that sits between two top-level defs is attributed to NEITHER function, so a
function with NO docstring §-ref is correctly classified as ORPHAN-NEEDS-REVIEW
instead of being mis-attributed to the next def's section-comment.
"""
from __future__ import annotations

import ast
import io
import re
import sys
from collections import OrderedDict
from pathlib import Path

# Force UTF-8 stdout on Windows (paper uses §, ∪, ✓, em-dashes, etc.)
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", line_buffering=True)
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", line_buffering=True)

ROOT = Path("C:/Users/hfyae/Claude/Projects/Deepseek")
ENGINE = ROOT / "knowledge" / "corpus" / "twt.py"
PAPER = ROOT / "knowledge" / "corpus" / "TWT_foundational_paper.md"
OUT = ROOT / "knowledge" / "corpus" / "TWT_V2_ENGINE_PAPER_MAP.md"

# --- helper sets (the legitimately internal primitives) -----------------------
# These match the §D table in the current map — math/utility helpers we do
# NOT expect the paper to mention by name.
INTERNAL_NAMES = {
    "is_L_bivector",
    "is_Q_bivector",
    "I4_maps_L_to_Q",
    "cl_dimension",
    "is_idempotent",
    "self_dual",
    "anti_self_dual",
    "self_dual_blade",
    "comm",
    "chsh_S",
    "s0",
}

# --- regexes ------------------------------------------------------------------
DEF_RE = re.compile(r"^def\s+([a-zA-Z][a-zA-Z0-9_]*)\s*\(")
# §-ref in any docstring/body. Two forms accepted:
#   - "§X.Y", "§X.Y.Z" — the V2 form (and ledger form)
#   - "Sec X.Y", "Sec X.Y.Z" — the legacy form used in older engine docstrings
# Lone-digit (`§N` with no dot) is also captured because some engine docstrings
# reference top-level paper sections (e.g., `§3 — Vacuum`).
SECREF_RE = re.compile(r"(?:§|Sec\s+)([0-9]+(?:\.[0-9]+)*)")
# Paper headers — TWO patterns:
PAPER_ATX_RE = re.compile(r"^#{2,}\s*§([0-9]+(?:\.[0-9]+)*)")
PAPER_BOLD_RE = re.compile(r"^\*\*§([0-9]+(?:\.[0-9]+)*)")


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")


# ----------------------------------------------------------------------------
# Engine parse
# ----------------------------------------------------------------------------
def parse_engine(text: str):
    """Return list of dicts: {name, line, doc_first, body, sec_refs}.

    Uses `ast` to recover each top-level function's exact source span — so a
    `# ---- §X.Y` section-comment that sits between two function defs is
    attributed to NEITHER function (the previous slice-to-next-def approach
    mis-attributed it to the preceding function).
    """
    lines = text.splitlines()
    tree = ast.parse(text)
    out = []
    for node in tree.body:
        if not isinstance(node, ast.FunctionDef):
            continue
        name = node.name
        # `node.lineno` is 1-based at `def`; `node.end_lineno` is 1-based at last stmt line
        start = node.lineno - 1
        end = node.end_lineno  # exclusive in 0-based slicing
        body_lines = lines[start:end]
        body_text = "\n".join(body_lines)
        # docstring first non-empty line
        doc = ast.get_docstring(node) or ""
        doc_first = ""
        for dl in doc.splitlines():
            if dl.strip():
                doc_first = dl.strip()
                break
        # all §-refs in the (function-only) body
        refs = sorted(set(SECREF_RE.findall(body_text)))
        out.append(
            dict(
                name=name,
                line=node.lineno,
                doc_first=doc_first,
                body=body_text,
                sec_refs=refs,
            )
        )
    return out


def collect_paper_sections(text: str) -> set[str]:
    """Return the union of ATX § headers and BOLD § sub-headers."""
    secs: set[str] = set()
    for L in text.splitlines():
        m = PAPER_ATX_RE.match(L)
        if m:
            secs.add(m.group(1))
            continue
        m = PAPER_BOLD_RE.match(L)
        if m:
            secs.add(m.group(1))
    return secs


def is_lone_digit(ref: str) -> bool:
    return "." not in ref


# ----------------------------------------------------------------------------
# Cross-reference + classification
# ----------------------------------------------------------------------------
def classify(funcs: list[dict], paper_secs: set[str], paper_text: str) -> None:
    """Annotate each function with:
        ref_status: list of (ref, "PRESENT"|"DRIFT"|"LONE")
        drift_refs: list of refs that are truly missing
        present_refs_str: human-readable e.g. "§19.4✓,§8.2✓"
        cited_in_paper: bool — name (≥8 chars) found verbatim in paper prose
    """
    for f in funcs:
        ref_status = []
        for r in f["sec_refs"]:
            if r == "0":
                # §0 is the standing reading-map preamble (no ATX header in V2); not drift.
                ref_status.append((r, "LONE"))
            elif r in paper_secs:
                # includes both `§3` (lone digit matching `## §3`) and `§19.8.1` (bold sub-header).
                ref_status.append((r, "PRESENT"))
            else:
                ref_status.append((r, "DRIFT"))
        f["ref_status"] = ref_status
        f["drift_refs"] = [r for r, s in ref_status if s == "DRIFT"]
        # Format the human-readable §-ref string
        parts = []
        for r, s in ref_status:
            if s == "PRESENT":
                parts.append(f"§{r}✓")
            elif s == "DRIFT":
                parts.append(f"§{r}?")
            else:  # LONE
                parts.append(f"§{r}?")
        f["present_refs_str"] = ",".join(parts) if parts else ""
        # CITED: name (≥8 chars) appears in paper as a substring
        f["cited_in_paper"] = (
            len(f["name"]) >= 8 and f["name"] in paper_text
        )


# ----------------------------------------------------------------------------
# Bucket assignment (§A/§B/§C/§D/§E)
# ----------------------------------------------------------------------------
def bucket(funcs: list[dict]):
    """Return ordered dict: {bucket_name: list[func]}.

    Buckets:
      DRIFT      : has at least one truly-missing §-ref         (§A in the map)
      CITED      : name appears in paper prose, NOT in DRIFT    (§B)
      DECLARED   : has a present §-ref, not CITED, not DRIFT    (§C)
      ORPHAN_INT : name in INTERNAL_NAMES                       (§D)
      ORPHAN_REV : everything else                              (§E)
    """
    out: OrderedDict = OrderedDict()
    for tag in ("DRIFT", "CITED", "DECLARED", "ORPHAN_INT", "ORPHAN_REV"):
        out[tag] = []

    for f in funcs:
        name = f["name"]
        if f["drift_refs"]:
            out["DRIFT"].append(f)
            continue
        # Recognize [internal helper] docstring tag as internal-helper category
        # (added 2026-06-29 after orphan-audit pass classified e/closure_report/exp_unit_bivector
        # with explicit `[internal helper]` markers).
        if name in INTERNAL_NAMES or "[internal helper" in f.get("doc_first", "").lower():
            out["ORPHAN_INT"].append(f)
            continue
        if f["cited_in_paper"]:
            out["CITED"].append(f)
            continue
        if any(s == "PRESENT" for _, s in f["ref_status"]):
            out["DECLARED"].append(f)
            continue
        # no PRESENT refs, not cited by name, not in internal-list
        out["ORPHAN_REV"].append(f)
    return out


# ----------------------------------------------------------------------------
# Render
# ----------------------------------------------------------------------------
def esc_table_cell(s: str) -> str:
    if s is None:
        return ""
    return s.replace("|", "\\|").replace("\n", " ").strip()


def render(funcs: list[dict], paper_secs: set[str], buckets) -> str:
    n_total = len(funcs)
    n_drift = len(buckets["DRIFT"])
    n_cited = len(buckets["CITED"])
    n_declared = len(buckets["DECLARED"])
    n_int = len(buckets["ORPHAN_INT"])
    n_rev = len(buckets["ORPHAN_REV"])

    L: list[str] = []
    L.append("# TWT V2 — Engine ↔ Paper Section Map")
    L.append("")
    L.append(
        f"**Generated:** 2026-06-29 (regenerated by `scripts/generate_engine_paper_map.py`). "
        f"**Engine:** `twt.py` ~{n_total} top-level (non-`_`-prefixed) primitives. "
        f"**Paper:** `TWT_foundational_paper.md` V2 — ATX + bold sub-header §-index."
    )
    L.append("")
    L.append(
        "**Purpose.** Catch engine↔paper drift (CLAUDE.md §10). A primitive can "
        "be banked with only a ledger §-ref and never reach the paper — exactly "
        "how the gluon-octet result drifted out of §20.2 for a full session "
        "before a coverage audit caught it. **A new engine result is not fully "
        "graduated until its CONTENT is in the paper body, not just the ledger.**"
    )
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Summary")
    L.append("")
    L.append(f"- **Total non-private primitives:** {n_total}")
    L.append(
        f"- **CITED** (appears by name in paper prose, name ≥ 8 chars): {n_cited}"
    )
    L.append(
        f"- **DECLARED** (docstring/body cites a paper §-ref, name absent from paper): {n_declared}"
    )
    L.append(f"- **ORPHAN — internal helper** (math/utility, not expected in paper): {n_int}")
    L.append(f"- **ORPHAN — needs review** (no docstring §-ref AND not internal): {n_rev}")
    L.append(f"- **DRIFT** (declared §-ref not present as paper header): {n_drift}")
    L.append("")
    L.append("Notes on method:")
    L.append("- §-references are extracted from each function's body (docstring + comments), using `ast` for exact function spans (so trailing `# ---- §X.Y` section-comments belong to NEITHER function).")
    L.append(
        "- Paper headers are detected in **two styles**: ATX `^##+ §X.Y` AND "
        "**bold sub-header** `^\\*\\*§X.Y...`. V2 uses bold sub-headers for "
        "some subsections (notably §19.8.1/2/3) that an ATX-only scan would "
        "false-positive as drift."
    )
    L.append(
        "- A function counts as CITED if its name (≥8 chars) appears by "
        "inline-mention in the paper — most engine→paper references are by "
        "topic, not literal name, so DECLARED is the dominant healthy status."
    )
    L.append("- Lone digits (`§0`, `§5`) are matched against top-level paper ATX headers (`## §3 — …`); `§0` is treated as the standing reading-map preamble and surfaces with `?` instead of DRIFT.")
    L.append("")
    L.append("---")
    L.append("")

    # §A DRIFT
    L.append("## §A — DRIFT REPORT (declared paper sections NOT present in V2)")
    L.append("")
    if buckets["DRIFT"]:
        L.append(
            "These engine primitives cite sections that don't exist as headers "
            "(neither ATX nor bold sub-header) in `TWT_foundational_paper.md`. "
            "**Action: either rename the doc-string §-ref to the existing V2 "
            "section, or add the missing section to the paper.**"
        )
        L.append("")
        L.append("| Function | Declared § (missing) |")
        L.append("|---|---|")
        for f in buckets["DRIFT"]:
            missing = ",".join(f"§{r}" for r in f["drift_refs"])
            L.append(f"| `{f['name']}` | {missing} |")
        L.append("")
    else:
        L.append("No drift. Every engine docstring §-ref resolves to a real paper header (ATX or bold).")
        L.append("")
    L.append(
        "**Observation.** Drift here is the *exactly-actionable* signal — "
        "either a stale engine ref (fix the docstring) or a missing paper "
        "subsection (add it). Trend should drop to zero with each polish pass."
    )
    L.append("")
    L.append("---")
    L.append("")

    # §B CITED
    L.append("## §B — CITED primitives (engine name appears in paper prose)")
    L.append("")
    L.append("These primitives are referenced by literal name in the paper — the strongest engine↔paper binding.")
    L.append("")
    L.append("| Function | Paper § (declared) | One-line |")
    L.append("|---|---|---|")
    for f in buckets["CITED"]:
        refs = f["present_refs_str"] or "—"
        L.append(f"| `{f['name']}` | {refs} | {esc_table_cell(f['doc_first'])[:200]} |")
    L.append("")
    L.append("---")
    L.append("")

    # §C DECLARED
    L.append("## §C — DECLARED primitives (cite a paper § in body; name not inline in paper)")
    L.append("")
    L.append(
        "These primitives **declare** a paper section in their docstring/body. "
        "The section exists in the paper (ATX or bold sub-header), but the "
        "function name itself isn't quoted in the paper body (this is the "
        "healthy default — the paper cites results by topic, not by engine "
        "identifier)."
    )
    L.append("")
    L.append("| Function | Paper § (declared) | One-line |")
    L.append("|---|---|---|")
    for f in buckets["DECLARED"]:
        refs = f["present_refs_str"] or "—"
        L.append(f"| `{f['name']}` | {refs} | {esc_table_cell(f['doc_first'])[:200]} |")
    L.append("")
    L.append("---")
    L.append("")

    # §D ORPHAN-INTERNAL
    L.append("## §D — ORPHAN-INTERNAL (math/utility helpers; not expected in paper)")
    L.append("")
    L.append(
        "These are low-level Clifford / boolean / projector helpers — the "
        "paper rightly does not reference them by name."
    )
    L.append("")
    L.append("| Function | One-line |")
    L.append("|---|---|")
    for f in buckets["ORPHAN_INT"]:
        L.append(f"| `{f['name']}` | {esc_table_cell(f['doc_first']) or '(no docstring; primitive helper)'} |")
    L.append("")
    L.append("---")
    L.append("")

    # §E ORPHAN-NEEDS-REVIEW
    L.append("## §E — ORPHAN-NEEDS-REVIEW (no declared paper § AND not an internal helper)")
    L.append("")
    L.append("**These are the watch-list.** A genuine result with no docstring §-ref is a potential coverage gap — either:")
    L.append("- it is paper-worthy but the engine never picked up the §-ref (drift waiting to happen), OR")
    L.append("- it is intentionally ledger-only / Paper-2 scope (e.g., the `texture_metric_*` gravity scaffolding), OR")
    L.append("- it is a derived helper that another engine function calls (effectively INTERNAL).")
    L.append("")
    L.append(
        "Coverage-audit owners should walk each row and either add a §-ref "
        "pointer (engine side), bring its content into the paper (paper "
        "side), or reclassify as INTERNAL."
    )
    L.append("")
    L.append("| Function | One-line |")
    L.append("|---|---|")
    for f in buckets["ORPHAN_REV"]:
        L.append(f"| `{f['name']}` | {esc_table_cell(f['doc_first']) or '(no docstring)'} |")
    L.append("")
    L.append("---")
    L.append("")

    # §F Method
    L.append("## §F — How to keep this map honest")
    L.append("")
    L.append(
        "This file is **generated by mechanical scan** "
        "(`scripts/generate_engine_paper_map.py`); it is not authoritative on "
        "its own. The discipline that keeps engine and paper aligned:"
    )
    L.append("")
    L.append(
        "1. **When you bank a new engine primitive,** include a `§N.N` (or "
        "`§N.N.N`) reference in its docstring pointing at the paper section "
        "that carries its content."
    )
    L.append(
        "2. **When you rename a paper section** in V2 (e.g., the §19.8 "
        "consolidation that broke §19.8.1 references — although §19.8.1/2/3 "
        "now LIVE as bold sub-headers and are recognized), grep the engine "
        "for the old number and update docstring refs in the same commit."
    )
    L.append(
        "3. **When you regenerate this map,** the §A drift count should be "
        "the metric you watch — every drift entry is either a stale engine "
        "ref or a missing paper subsection."
    )
    L.append("")
    L.append(
        "**Detector note (the bold-sub-header fix).** V2 introduced a "
        "third paper-header style alongside ATX `### §N.N`: **bold "
        "sub-headers** `**§N.N.N Title.**` (used for §19.8.1 / §19.8.2 / "
        "§19.8.3 in the live paper). The original ATX-only scan reported all "
        "engine cites to those sections as drift (12 false positives in the "
        "DRIFT-21 audit). This generator catches both styles, so a §19.8.1 "
        "cite to a bold sub-header is now correctly PRESENT, not DRIFT."
    )
    L.append("")
    L.append(
        "**Coverage discipline (CLAUDE.md §10) — the live test.** A "
        "primitive whose `[DERIVED] § …` claim points at a section that "
        "doesn't exist is the *exact* failure mode that hid the gluon-octet "
        "result for a session. Drift count should trend down with each "
        "polish pass."
    )
    L.append("")
    L.append(
        f"**Regenerate:** `python scripts/generate_engine_paper_map.py --write` "
        f"(reproducible — paper headers indexed: {len(paper_secs)} unique §-ids)."
    )
    L.append("")
    return "\n".join(L)


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------
def main(argv: list[str]) -> int:
    write_out = "--write" in argv or "-w" in argv
    out_path = OUT
    for i, a in enumerate(argv):
        if a == "--out" and i + 1 < len(argv):
            out_path = Path(argv[i + 1])

    engine_text = read_text(ENGINE)
    paper_text = read_text(PAPER)

    funcs_all = parse_engine(engine_text)
    # Drop _-prefixed helpers (private to the engine).
    funcs = [f for f in funcs_all if not f["name"].startswith("_")]

    paper_secs = collect_paper_sections(paper_text)

    classify(funcs, paper_secs, paper_text)
    buckets = bucket(funcs)

    out_md = render(funcs, paper_secs, buckets)

    # Summary to stdout — useful when comparing against the previous DRIFT count.
    print(f"Engine primitives (non-_ top-level): {len(funcs)}")
    print(f"Paper §-headers indexed (ATX ∪ bold): {len(paper_secs)}")
    bold_only: set[str] = set()
    for L in paper_text.splitlines():
        m = PAPER_BOLD_RE.match(L)
        if m:
            bold_only.add(m.group(1))
    print(f"  of which BOLD sub-headers: {sorted(bold_only)}")
    print()
    print(f"DRIFT     : {len(buckets['DRIFT'])}")
    print(f"CITED     : {len(buckets['CITED'])}")
    print(f"DECLARED  : {len(buckets['DECLARED'])}")
    print(f"ORPHAN-INT: {len(buckets['ORPHAN_INT'])}")
    print(f"ORPHAN-REV: {len(buckets['ORPHAN_REV'])}")
    print()
    if buckets["DRIFT"]:
        print("DRIFT items:")
        for f in buckets["DRIFT"]:
            missing = ",".join(f"§{r}" for r in f["drift_refs"])
            print(f"  - {f['name']:50s}  missing: {missing}")
    if write_out:
        out_path.write_text(out_md, encoding="utf-8")
        print(f"\nWrote {out_path}  ({len(out_md)} bytes)")
    else:
        print("\n(dry-run; pass --write to update the map)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
