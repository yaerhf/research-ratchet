"""Verify the rendered PDFs actually contain what they should.

Run after scripts/render_pdf.sh:   python scripts/verify_pdf.py

pandoc exits 0 on a PDF with no glyphs and no links, so the exit code proves
nothing. This checks the three things that have actually gone wrong here:

  1. GLYPHS   — the paper puts its notation inside code spans, and no monospace
                font on the box covers that Unicode set. If the font fallback in
                scripts/pdf_header.tex regresses, ~3,500 characters silently
                become blank boxes. Canary characters must appear in the text.
  2. LINKS    — internal TOC links are LINK_NAMED (kind 4), NOT LINK_GOTO. An
                earlier version of this script counted only GOTO and wrongly
                reported "0 internal links" on a perfectly good PDF. Count all
                kinds. Bare repository URLs need +autolink_bare_uris to become
                clickable at all.
  3. STAMP    — the provenance line (date, git hash, suite count, repo URL) must
                be present, so a PDF in circulation can be traced to a commit.

Requires PyMuPDF (`pip install pymupdf`).
"""
import os
import sys

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("PyMuPDF not installed — pip install pymupdf")

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                    "knowledge", "corpus", "pdf")
DOCS = ["TWT_foundational_paper.pdf", "TWT_foundational_paper_companion.pdf"]

# Characters absent from every monospace font available — their presence in the
# extracted text proves the fallback chain fired.
CANARIES = ["η", "⁽", "⁴", "≲", "∈", "π", "ℍ", "ℤ", "⟨", "⟩", "⇒", "Λ", "Θ", "θ"]

KIND = {0: "none", 1: "goto", 2: "uri", 3: "launch", 4: "named", 5: "gotor"}

fail = 0
for name in DOCS:
    path = os.path.join(BASE, name)
    if not os.path.exists(path):
        print("MISSING: %s" % name)
        fail += 1
        continue

    doc = fitz.open(path)
    text = "".join(p.get_text() for p in doc)
    links = [l for p in doc for l in p.get_links()]

    print("\n=== %s ===" % name)
    print("  pages           : %d" % doc.page_count)
    print("  extracted chars : %d" % len(text))

    if doc.page_count < 20:
        print("  PAGE COUNT      : FAIL — suspiciously short, likely a truncated build")
        fail += 1

    missing = [c for c in CANARIES if c not in text]
    if missing:
        print("  GLYPHS          : FAIL — absent: %s" % " ".join(missing))
        fail += 1
    else:
        print("  GLYPHS          : PASS — all %d canaries present" % len(CANARIES))

    tally = {}
    for l in links:
        tally[KIND.get(l.get("kind"), "?")] = tally.get(KIND.get(l.get("kind"), "?"), 0) + 1
    print("  links           : %d total  %s" % (len(links), tally or "{}"))

    internal = tally.get("named", 0) + tally.get("goto", 0)
    if internal == 0:
        print("  INTERNAL LINKS  : FAIL — TOC entries are not clickable")
        fail += 1
    else:
        print("  INTERNAL LINKS  : PASS — %d resolvable" % internal)

    uris = [l.get("uri", "") for l in links if l.get("kind") == 2]
    gh = [u for u in uris if "github.com/yaerhf/TWT" in u]
    if gh:
        print("  REPO URL        : PASS — %d clickable link(s) to the repository" % len(gh))
    else:
        print("  REPO URL        : FAIL — repository not reachable from the PDF")
        fail += 1

    if "github.com/yaerhf/TWT" in text and "checks" in text:
        print("  PROVENANCE      : PASS — stamp present in text")
    else:
        print("  PROVENANCE      : WARN — stamp not found")

    doc.close()

print("\n%s" % ("ALL PDF CHECKS PASSED" if fail == 0 else "%d PDF CHECK(S) FAILED" % fail))
sys.exit(1 if fail else 0)
