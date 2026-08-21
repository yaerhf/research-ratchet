#!/usr/bin/env bash
# Render the foundational paper to a standalone, math-rendered HTML for comfortable reading.
# Optional convenience — VS Code's Markdown preview (Ctrl+Shift+V) already renders the math.
# Requires pandoc (https://pandoc.org/installing.html).
#   scripts/render_paper.sh            # -> knowledge/corpus/TWT_foundational_paper.html
#   scripts/render_paper.sh out.html   # custom output path
set -euo pipefail
cd "$(cd "$(dirname "$0")/.." && pwd)"
SRC="knowledge/corpus/TWT_foundational_paper.md"
OUT="${1:-knowledge/corpus/TWT_foundational_paper.html}"
command -v pandoc >/dev/null || { echo "pandoc not found — install from https://pandoc.org/installing.html"; exit 1; }
pandoc "$SRC" --standalone --mathjax --toc --toc-depth=2 \
  --metadata title="Time-Wave Theory — Foundational Paper" \
  -o "$OUT"
echo "Rendered -> $OUT  (open in any browser)"
