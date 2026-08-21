#!/usr/bin/env bash
# Render the foundational paper + companion to provenance-stamped PDFs.
#
#   scripts/render_pdf.sh              # -> knowledge/corpus/pdf/*.pdf
#   scripts/render_pdf.sh /some/dir    # custom output directory
#
# Requires: pandoc, and a LaTeX distribution providing lualatex (MiKTeX/TeX Live).
#
# ---------------------------------------------------------------------------
# WHY THIS SCRIPT LOOKS THE WAY IT DOES — two non-obvious decisions, both load-
# bearing. Do not "simplify" them away without re-checking the output.
#
# 1. FONT FALLBACK (scripts/pdf_header.tex). The paper carries almost all of its
#    mathematical notation inside Markdown *code spans*, so the MONOSPACE font
#    must cover a large Unicode set. Measured against the paper's own character
#    census (Greek, super/subscripts, blackboard bold, arrows, relations):
#        Cambria    0 code gaps / 1 prose gap
#        Consolas  35 code gaps   <- best monospace on the box, still short
#    Without the fallback chain roughly 3,500 notation characters render as
#    missing-glyph boxes. The chain keeps Consolas for the monospace *look* and
#    pulls anything it lacks from Cambria, then Segoe UI Symbol.
#    => lualatex is REQUIRED (pdflatex cannot do this at all).
#
# 2. --from=markdown+gfm_auto_identifiers. Both documents carry hand-written
#    tables of contents whose anchors follow GitHub's slug algorithm (an em-dash
#    surrounded by spaces yields a DOUBLE hyphen). Pandoc's default identifier
#    algorithm yields a single hyphen, so every internal TOC link in the PDF
#    silently dead-ends. This extension makes pandoc reproduce GitHub's slugs.
#
# 3. +autolink_bare_uris. The paper prints its repository URL as bare text, and
#    pandoc does NOT hyperlink bare URLs by default — without this the PDF shows
#    the address but no reader can click it. Verified: the first build had zero
#    URI annotations in 75 pages.
#
# 4. LAYOUT FILTERS.
#    pdf_center_equations.lua — the paper writes display equations as blockquoted
#      code spans, which pandoc renders indented and left-aligned. This centres
#      them. Its discriminator is measured, not guessed; see the header of that
#      file for the two wrong rules that were tried first.
#    pdf_balance_tables.lua — every table uses a uniform |---|---| separator, which
#      carries no width information, so pandoc makes all columns equal. That gives
#      the "#" column (widest cell: "16") the same page as "What it kills" (60+
#      chars). This sizes columns by mean content length instead.
#
# VERIFY THE OUTPUT, DO NOT TRUST THE EXIT CODE. pandoc exits 0 on a PDF with no
# glyphs and no links. scripts/verify_pdf.py checks page count, that the Unicode
# notation survived the fallback, and that links actually resolve.
# ---------------------------------------------------------------------------
set -euo pipefail
cd "$(cd "$(dirname "$0")/.." && pwd)"

OUTDIR="${1:-knowledge/corpus/pdf}"
HEADER="scripts/pdf_header.tex"
mkdir -p "$OUTDIR"

command -v pandoc   >/dev/null || { echo "pandoc not found — https://pandoc.org/installing.html"; exit 1; }
command -v lualatex >/dev/null || { echo "lualatex not found — install MiKTeX or TeX Live"; exit 1; }
[ -f "$HEADER" ]              || { echo "missing $HEADER"; exit 1; }

HASH="$(git rev-parse --short HEAD 2>/dev/null || echo 'no-git')"
TODAY="$(date +%Y-%m-%d)"
# The check count is read by RUNNING the suite, never by grepping source. (Fixed 2026-08-02:
# both old greps had gone silently dead — twt_test.py prints the count via an f-string, so the
# source literal is '{total}' not digits, and the de-historicization pass removed the paper's
# '(N checks at this revision)' line. Empty CHECKS then skipped the mirror README drift guard
# below without a word — a guard that greps nothing verifies nothing. Running the suite here
# also enforces release discipline: no PDF renders from a red tree.)
echo "Running BOTH suites to stamp the check counts (release discipline; ~3 min)..."
CHECKS="$( (cd knowledge/corpus && PYTHONUTF8=1 python twt_test.py 2>/dev/null) | grep -oE 'ALL [0-9]+ CHECKS PASSED' | grep -oE '[0-9]+' | head -1 || true)"
[ -n "$CHECKS" ] || { echo "MAIN SUITE DID NOT PASS (or its count line was not found) — fix before rendering."; exit 1; }
CHECKSC="$( (cd knowledge/corpus && PYTHONUTF8=1 python twt_companion_test.py 2>/dev/null) | grep -oE 'ALL [0-9]+ COMPANION CHECKS PASSED' | grep -oE '[0-9]+' | head -1 || true)"
[ -n "$CHECKSC" ] || { echo "COMPANION SUITE DID NOT PASS (or its count line was not found) — fix before rendering."; exit 1; }
STAMP="Rendered ${TODAY} · git ${HASH} · suite ${CHECKS}+${CHECKSC} checks (main+companion) · https://github.com/yaerhf/TWT"

render () {           # render <src.md> <out.pdf> <title> <geometry> <fontsize> [subtitle]
  echo "  -> $2"
  # Delete the previous output FIRST. Otherwise a failed build leaves the stale PDF
  # in place and the "Done" listing below reports success over an old file — this
  # actually happened (a broken Lua filter, exit 83, masked by the `|| true` on the
  # log filter). A missing file is a loud failure; a stale one is a silent lie.
  rm -f "$2"
  pandoc "$1" \
    --from=markdown+gfm_auto_identifiers+autolink_bare_uris \
    --lua-filter=scripts/pdf_unescape_pipes.lua \
    --lua-filter=scripts/pdf_center_equations.lua \
    --lua-filter=scripts/pdf_balance_tables.lua \
    --pdf-engine=lualatex -H "$HEADER" \
    --toc --toc-depth=2 \
    -V geometry:"$4" -V fontsize="$5" -V colorlinks=true \
    -V title="$3" ${6:+-V subtitle="$6"} \
    -V author="Yaer Aharon Haddad Fennech · Independent Researcher · hfyaer@gmail.com" \
    -V date="$STAMP" \
    -o "$2" 2>&1 | grep -iE "missing character|error" | head -20 || true
  [ -s "$2" ] || { echo "     BUILD FAILED — $2 was not produced"; exit 1; }
}

echo "Rendering (stamp: $STAMP)"
# The 6th arg is the cover SUBTITLE. It is an A/B variable in the external-review
# loop (knowledge/prompts/external_review_loop.md, Standing A/B items): the metric
# is the cold-read reference-class assignment rate per variant, so the two arms are
# this subtitle and a no-subtitle control (drop the 6th arg for the control). The
# TITLE string is deliberately unchanged between arms — the subtitle is additive, so
# no identity site (TOC, mirror README, cover note) moves and no sweep is triggered.
render knowledge/corpus/TWT_foundational_paper.md \
       "$OUTDIR/TWT_foundational_paper.pdf" \
       "Time-Wave Theory — Foundational Paper (V3)" \
       "margin=2.1cm" "10pt" \
       "Standard-Model structure from a single wave medium"

# The companion is bookkeeping: very wide tables (result index, import registry).
# Landscape + smaller type keeps them readable instead of clipped.
render knowledge/corpus/TWT_foundational_paper_companion.md \
       "$OUTDIR/TWT_foundational_paper_companion.pdf" \
       "Time-Wave Theory — Foundational Paper V3: Companion" \
       "margin=1.6cm,landscape" "9pt"

echo
echo "Done:"
ls -la "$OUTDIR"/*.pdf

# ---------------------------------------------------------------------------
# PUBLIC MIRROR SYNC + PUSH (coordinator-directed, 2026-07-30). The PDFs are the
# artifact we hand reviewers, so the moment they are rebuilt is the moment the
# public repo must match the corpus — this block exists so the push is never
# forgotten between paper reviews. Set TWT_SKIP_MIRROR=1 to render PDFs only.
# ---------------------------------------------------------------------------
MIRROR="${TWT_MIRROR_DIR:-$HOME/Claude/Projects/twt-engine}"
if [ "${TWT_SKIP_MIRROR:-0}" = "1" ]; then
  echo "Mirror sync SKIPPED (TWT_SKIP_MIRROR=1)."
elif [ ! -d "$MIRROR/.git" ]; then
  echo "WARNING: mirror not found at $MIRROR — public repo NOT updated."
else
  echo
  echo "Syncing public mirror: $MIRROR"
  cp knowledge/corpus/TWT_foundational_paper.md \
     knowledge/corpus/TWT_foundational_paper_companion.md \
     knowledge/corpus/twt.py \
     knowledge/corpus/twt_test.py \
     knowledge/corpus/twt_companion.py \
     knowledge/corpus/twt_companion_test.py \
     knowledge/corpus/D4_lattice_quartic_isotropy.md \
     knowledge/ledgers/TWT_NEGATIVES_LEDGER.md \
     knowledge/ledgers/TWT_FAMILY_TREE.md \
     knowledge/reviewer_package/COVER_NOTE.md \
     "$MIRROR/"
  # Suite-count drift guard. The README QUOTES each harness's own pass line for a
  # reviewer to compare against their terminal, so the two lines are checked
  # SEPARATELY against their own harness — not against the combined total. (The
  # pre-split guard compared the first match to main+companion and therefore
  # warned on a correct README the moment the engine split landed; it also only
  # ever looked at the main pattern, so companion drift was invisible to it.
  # scripts/check_records.py section 7b is the real gate — it fails the bank;
  # this stays as the render-time early warning.)
  MCOUNT="$(grep -oE 'ALL [0-9]+ CHECKS PASSED' "$MIRROR/README.md" | grep -oE '[0-9]+' | head -1 || true)"
  CCOUNT="$(grep -oE 'ALL [0-9]+ COMPANION CHECKS PASSED' "$MIRROR/README.md" | grep -oE '[0-9]+' | head -1 || true)"
  if [ "$MCOUNT" != "$CHECKS" ]; then
    echo "WARNING: mirror README quotes $MCOUNT main checks, harness prints $CHECKS — fix README before pushing."
  fi
  if [ "$CCOUNT" != "$CHECKSC" ]; then
    echo "WARNING: mirror README quotes $CCOUNT companion checks, harness prints $CHECKSC — fix README before pushing."
  fi
  git -C "$MIRROR" add -A
  if git -C "$MIRROR" diff --cached --quiet; then
    echo "Mirror already current — nothing to push."
  else
    git -C "$MIRROR" commit -m "sync from working corpus: $STAMP"
    git -C "$MIRROR" push origin main && echo "Mirror PUSHED to GitHub." \
      || echo "WARNING: push failed (offline? credentials?) — commit is local; push manually."
  fi
fi
