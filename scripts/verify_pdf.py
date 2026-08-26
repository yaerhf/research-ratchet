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

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BASE = os.path.join(ROOT, "knowledge", "corpus", "pdf")

# (rendered pdf, its markdown source, minimum plausible page count).
# The Core paper joined this list at the 2026-08-21 relocation leg: it is the
# front-facing artifact, so an unverified render of it is the one that would
# actually reach a cold reader. Its floor is lower than the other two because it
# is deliberately ~6x shorter — a shared floor of 20 would have been a guess
# dressed as a check.
DOCS = [
    ("TWT_core_paper.pdf", "TWT_core_paper.md", 15),
    ("TWT_foundational_paper.pdf", "TWT_foundational_paper.md", 20),
    ("TWT_foundational_paper_companion.pdf",
     "TWT_foundational_paper_companion.md", 20),
]

# Characters absent from every monospace font available — their presence in the
# extracted text proves the fallback chain fired.
#
# PER-DOCUMENT, and that matters (relocation leg 2026-08-21). Six of these do not
# occur in the Core paper's source at all, so testing the full list against it
# would report a font regression that never happened — a false alarm is as bad as
# a vacuous check, and harder to unlearn. The set actually tested is the
# intersection with the document's own source, and the count is printed; if the
# intersection collapses the check is refused rather than passed silently.
CANARIES = ["η", "⁽", "⁴", "≲", "∈", "π", "ℍ", "ℤ", "⟨", "⟩", "⇒", "Λ", "Θ", "θ"]
MIN_CANARIES = 5

KIND = {0: "none", 1: "goto", 2: "uri", 3: "launch", 4: "named", 5: "gotor"}

fail = 0
for name, src_name, min_pages in DOCS:
    path = os.path.join(BASE, name)
    if not os.path.exists(path):
        print("MISSING: %s" % name)
        fail += 1
        continue

    src_path = os.path.join(ROOT, "knowledge", "corpus", src_name)
    if not os.path.exists(src_path):
        print("MISSING SOURCE: %s (cannot pick canaries for %s)" % (src_name, name))
        fail += 1
        continue
    with open(src_path, encoding="utf-8") as fh:
        src = fh.read()
    canaries = [c for c in CANARIES if c in src]

    doc = fitz.open(path)
    text = "".join(p.get_text() for p in doc)
    links = [l for p in doc for l in p.get_links()]

    print("\n=== %s ===" % name)
    print("  pages           : %d" % doc.page_count)
    print("  extracted chars : %d" % len(text))

    if doc.page_count < min_pages:
        print("  PAGE COUNT      : FAIL — %d < %d, likely a truncated build"
              % (doc.page_count, min_pages))
        fail += 1

    if len(canaries) < MIN_CANARIES:
        print("  GLYPHS          : FAIL — only %d canaries occur in %s; the glyph "
              "check would be near-vacuous" % (len(canaries), src_name))
        fail += 1
    else:
        missing = [c for c in canaries if c not in text]
        if missing:
            print("  GLYPHS          : FAIL — absent: %s" % " ".join(missing))
            fail += 1
        else:
            print("  GLYPHS          : PASS — all %d canaries present in this "
                  "document (of %d in the list)" % (len(canaries), len(CANARIES)))

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
