# THE STANDALONE-NOTE COLD REVIEW — the durable send routine

*The note-level sibling of `knowledge/prompts/external_review_loop.md`. That routine governs
sends of the **paper package**; this one governs sends of a **single standalone note** — a
self-contained document (an algebra note, a lattice note, a probe report) handed to a cold
reviewer with no TWT framing at all.*

**Why this file exists.** The instrument was built and used on 2026-08-25 (two sends, two
reviewers, two of that window's four highest-yield reactions) and then lived **only** in a dated
round directory — `knowledge/audit/standalone_reviews_2026-08-25/SEND_INSTRUCTIONS.md`, which a
future worker has no reason to open, alongside a dated note saying one of its two send targets has
since been split in two. The paper-level prompt is pinned byte-exact across two files precisely
because *any coaching invalidates the measurement*; the note-level prompt carried the identical
fence and **no pin at all**. This is the pin. (Removal audit 2026-08-25, §3.6 / structure L2.)

---

## 1. THE PROMPT — verbatim, and it is the whole instrument

Nothing is added. No framing, no context, no "we think this is right, check it", no naming of
the framework, the round, the author, or what a good answer would look like.

- **Prompt, verbatim, nothing added:**
  > Please review this note carefully.

**This string is byte-pinned** (`scripts/check_records.py` §7d) against its quotation in the
2026-08-25 send package. The two sites must agree exactly; a drift between them would void every
sample **silently**, because the routine would document one instrument while the send used
another and nothing in the returned review would look wrong.

**If you believe the prompt should change**, change it here *and* record the change as a new
instrument — do not edit it quietly. Samples taken under different prompts are not comparable, and
the comparability across sends is the only reason the measurement is worth anything.

## 2. ONE FILE PER SEND

**One note, one reviewer, one send.** A reviewer who receives two notes is measuring the **pair**
— the relationship between them, the shared vocabulary, the implied programme — and is no longer
a cold reader of either. Where a note has been split, the parts are **separate send decisions**,
not one send with two attachments.

The only permitted attachment beyond the note itself is a file the **note's own text names** as
its reproduction script or data. Nothing else travels with it.

## 3. THE FENCES

- **Fresh context, no TWT framing beyond the note itself and its named attachments.** The note's
  own citations are the reviewer's map.
- **Neither reviewer is told of the other**, of the review round, of the mirror, or of any prior
  adjudication — unless they find it themselves.
- **A note's own status header stays as written** (e.g. "pre-review draft"). Being reviewed is its
  purpose; dressing it up changes what is being measured.
- **If a reviewer asks for context, that request is itself a finding** about the note's
  self-containedness. File it, answer minimally, and record what was sent in reply.
- **The send is the human's** (fence F1): the package is prepared here, the send is not automated.

## 4. WHAT COMES BACK

File each returned review **verbatim** in the round's directory. Adjudication follows the round-4
pattern: verdicts are **adjudicated, never adopted**, and anything that would bank goes to
cross-class checkers. Reviewer-class balance across a pair of sends is a deliberate choice — record
which class read which note, because it is the only way class variance on notes gets measured.

---

*Governing precedent and the first use of this routine:
`knowledge/audit/standalone_reviews_2026-08-25/SEND_INSTRUCTIONS.md` (the send package, with its
dated post-return notes) · RUL-101 / E-8 · the paper-level sibling
`knowledge/prompts/external_review_loop.md`.*
