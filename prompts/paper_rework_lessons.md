# Paper-rework lessons — the standing editorial discipline (banked 2026-07-31)

*Coordinator-directed: "bank the lessons for subsequent reworks of the paper." Distilled from the
2026-07-28 external review (Parts VI–VII), the post-review note (Part II, the notice design), the
which-Λ round's three cross-class reports, and the C/D/E adjudication round's verification pass.
Read this BEFORE any front-matter edit, section restructure, retraction, or PDF/mirror release.
Primary sources: `knowledge/audit/external_review_2026-07-28/`,
`knowledge/audit/cde_audit_2026-07-30/ADJUDICATION_RECORD.md`.*

## 0. THE PAPER IS HISTORY-BLIND (coordinator design ruling, 2026-07-31 — governs everything below)
The paper must not narrate its own past: no revision dates, audit or finding IDs, ruling stamps,
"earlier revisions said / withdrawn / restored / relabelled" narratives, reviewer or process
references. That role belongs to the COMPANION (Result Index notes + Section 7 development log),
which records what changed, when, and why. The paper states the CURRENT claim in a
straightforward voice — fully conscious of the THEORY'S flaws (premises, conditionals, exposures
and open gaps are stated as present-tense facts about the theory) and unconscious of the
DOCUMENT'S history. Lesson 7 is amended accordingly: the labeled corpse of a retraction lives in
the companion, never in the paper body. When patching the paper, write the claim as if it had
always been stated correctly, and log the change in the companion in the same pass.

## 1. The reader-path law (the keeper's orientation lesson — the round's costliest)
**The strong claim must not survive where the reader meets it first while the retraction lives
where only an auditor looks.** When a result is retracted or re-tiered, sweep in READER order:
paper body FIRST (headline, section title, opening sentence), then abstract/front matter, then
companion rows, then engine docstrings, then ledgers. The C/D/E round executed four retractions
bookkeeping-first and the verification pass found all four still asserted in the body — the
inverse (and more dangerous) orientation of the old companion-outranks-body pattern.

## 2. Headlines must not outrun fine print (review VI-3 — "the cheapest fix with the largest gain")
The fine print is usually already right; the fix is almost always to COOL THE HEADLINE, not to
strengthen the argument. Instances paid for: "proven g₁ = g₂" over a premised one; "headline
derivation" over a normalization identity; "second cleanest" surviving its own re-ranking two
sentences away. When a section both asserts and retracts, the retraction governs and the
assertion must be rewritten — never leave both.

## 3. Demonstrate, don't plead (the notice design; post-review Part II)
Anti-pattern-match is earned by three things only: (a) checkable content near the front (the
five-minute commands must EXECUTE AS WRITTEN — test them in a clean clone; a first check that
errors discredits the other fifteen); (b) the author's strongest objection stated first (no
crank leads with "our natural value is excluded by orders of magnitude"); (c) the correct
reference class ("structural-derivation programme with one named unbuilt object", never
"unified theory"). NEVER include instructions aimed at the reviewing system's behaviour. Do not
invite verification of any number two of our own artifacts disagree about — reconcile first,
advertise second.

## 4. Prior art belongs AT the claim site (the Trayling lesson; handoff §11's pattern, 6th instance)
A bibliography entry is not a defense. Any claim with a shape-precedent cites the precedent in
the SAME section with a specific delta sentence ("developed independently of X, which reaches
related conclusions by different means; the delta is …"). Five prior-art misses were caught by
adversarial re-derivation and none by the tier system; the sixth (Trayling 1999's √(3/5) without
master groups) sat one arXiv lookup away from the headline it shadowed. Citations are
primary-verified only (INSPIRE/arXiv API records; beware dating traps — LDG is 1998, its arXiv
posting 2004), and content claims about a source are verified against its text, never recalled.

## 5. The abstract formula (applied 2026-07-31)
Reference class first → the spine short-list with ONE honest conditional each (full inventory
stays in §E.2) → the already-measured exposures as their own paragraph (the single most
credibility-building text in the paper) → the executable-suite offer with its scope stated ("a
passing check is bookkeeping, not physics"). No claim counts, no check counts in the abstract.
Nothing the body does not claim; nothing weaker than the body claims either.

## 6. Sweep mechanics (what actually failed, twice, under volume)
A relabel is not done until greped across: paper body, abstract/front matter, companion Sections
1/2/3/4 (the Engine↔Paper Map's reverse index included — the round CREATED a collision by
striking cites in Section 1 only), engine docstrings AND returned dict strings AND machine-read
rows (prose vs field of one primitive diverged twice), twt_test check-description strings (they
pin wording), all five ledgers (TWT_EOM_MAP.md was missed for a whole round), canon, worklist,
handoff, simulator/discoveries + twtsim comments, and the dispatch briefs in knowledge/prompts/.
Suite checks that pin old wording will fail honestly — re-key them, and record which are
wording-guards vs real computations (only the latter count as verification).

## 7. Retract by replacement, never by deletion
Every withdrawal keeps a labeled corpse at the site: what was claimed, why it fell, what
survives, dated. (V1's stability-scan caveat and E(q) derivation were silently compressed away
in V3 and had to be excavated by an auditor — restoration costs 10× the original sentence.)

## 8. Structural hygiene that bit
Heading renames break the hand-written GFM TOC anchors — patch heading + TOC together, or leave
the heading and fix the body. Numbered-exposure renumbering (four→five) must sweep every
"§E.3.5(n)" cross-reference AND the notice's counts. Premise tables: rows ≠ premises — count
honestly ("seven rows, thirteen-plus premises"). Every quantitative claim in front matter is a
consumer of some ruled scale/scheme — label it (the which-Λ lesson).

## 9. Release discipline (PDFs = publishing moment)
`render_pdf.sh` now syncs + pushes the public mirror with a suite-count drift guard. Before any
render: tree banked and clean, suite green, front-matter commands re-tested, README counts
current. Verify output with `verify_pdf.py` — exit 0 is not verification.

## 10. Process shape that worked (repeat it)
Patch in anchored chunks with die-before-save scripts → commit per chunk → cross-class
verification pass on the swept tree BEFORE bank (it found 7 blocking items the sweep missed,
twice running) → fix same day → bank.sh. Deferred items go to the worklist IN THE SAME PASS —
an accepted finding recorded nowhere is a silent drop.

## Lesson (2026-08-21, RUL-086(ii) — from external round 2): FAIR, NOT HARSH

The harsh register has a measured external cost: a referee counted the hedge vocabulary (136
"premise" / 144 "posit" / 122 "named" / 167 "open" / 75 "gated"), reported that "most paragraphs
state a result and then retract most of it in the same breath," and concluded no claim could be
located that was both new and unconditional. The human coordinator's ruling: *"Being fair yes,
being harsh no. It reads as the AI collaborators refusing to endorse it."* The binding form:
**every claim is stated once, at its full earned strength, with its condition stated once beside
it — and never re-hedged downstream.** The tier still wins over the prose in both directions
(RUL-076: under-claiming is the same labeling error as over-claiming). The register test for any
paper text: a referee quoting any headline sentence finds it exactly as strong as its tier — no
stronger, no weaker, and visibly stood-behind.
