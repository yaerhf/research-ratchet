# THE EXTERNAL-REVIEW LOOP — cold-gatekeeper routine (v1.1, 2026-08-19)

> **v1.1 carries the eleven standing rules adopted by the human coordinator 2026-08-19
> (RUL-062).** R4/R5/R6/R7/R8 land inside the numbered steps below; R9 + R10 are the
> pre-emption section at the end; R2/R3 govern checks and briefs and live in
> FORMATION_CORE and the coordinator role file. **R7 is the load-bearing one:** a
> reviewer can be right that a tension exists and wrong about the repair, and the repair a
> trained default reaches for is the conventional one — which for a substrate framework is
> frequently SM-retreat arriving as helpful advice.

> Purpose: measure and repair the paper's cold-read legibility against the adverse prior
> (the crank base-rate) — without expanding the paper. SUCCESS = COMPREHENSION, NOT PRAISE:
> a cold reviewer (a) assigns the correct reference class in its own words, (b) cites ≥1
> costly signal as evidence of seriousness, (c) issues no crank-classification. "This is
> good important work" is a TRIPWIRE METRIC — measured, never optimized against (Goodhart).

## Why this loop outranks its cost (R-H, 2026-08-20 — read before deprioritizing a release)

**This is the only instrument in the programme that does not depend on the principal's intent.**
Every internal check — the tier system, the §8a triad, the registries, the enforcer — is run by
people and agents inside the programme, under rules that are ~85 % unenforced, which means the
whole internal apparatus ultimately rests on the human coordinator genuinely wanting to be
refuted. **The cold reader owes the programme nothing.** That is not a rhetorical difference: it is
the only structural check on *capture of a good actor*, the realistic failure mode in which the
cost of a refutation rises with investment until refutations stop being sought.

**Consequence, and it is a real reordering: every strengthening of this loop reduces what the
internal apparatus has to carry — so publishing earlier and more often is an EPISTEMIC decision,
not a marketing one.** When a release is weighed against internal work, this is the argument that
belongs on the release side, and it is stronger than the one usually offered. It does **not**
license releasing something known to be misleading — the current release is correctly blocked on
the paper absorbing the Core/Instance split — but it does mean *"we are busy with internal work"*
is not a sufficient reason to defer a round.

## The loop (per iteration; HARD CAP 2–3 iterations per consolidation, then stop)

1. **RELEASE**: `render_pdf.sh` + `verify_pdf.py` (suite-green enforced, provenance stamp);
   mirror pushed (engines + paper + companion + negatives ledger). The PDF stamp's commit
   is the review tag. Never review a working tree.
2. **SAMPLE**: **N ≥ 3 fresh, isolated instances OF ONE CLASS** — not mixed classes —
   never the held-out class, with the verbatim prompt:

   > *"Please review this paper carefully. Access the github if necessary."*

   *Why within-class and not mixed (amended 2026-08-13, coordinator).* The loop measures
   whether a REAL GATEKEEPER reads the paper correctly, and the realistic gatekeeper is a
   frontier class — Fable, or less often Opus; nobody hands a foundational-physics paper
   to Haiku. Sampling classes that will not be used measures a situation that does not
   occur. And within-class N buys the thing the A/B items actually need: **the variance
   estimate.** With N = 1 a changed classification cannot be distinguished from sampling
   noise, so no A/B result means anything. Three runs of the deployment class give you
   that spread; three different classes do not. (The canon §8a cross-class rule is NOT
   weakened — it governs the CORRECTION step, step 5, where the same-class hazard
   actually bites. See the note there.)
   **Isolation mechanism — DIRECT API CALLS, never in-session subagents:** a subagent
   spawned inside the project inherits the canon auto-load and the repo — it is FORMED,
   not cold, and the measurement is void. The loop coordinator instead sends a raw
   Anthropic Messages request from the shell whose ENTIRE context is the verbatim prompt +
   the release PDF as a document block (server-side web tools enabled so the github clause
   is meaningful; model ID explicit — the held-out class is simply never called). **The
   request body is the isolation proof: log it verbatim per review** in the round's
   directory; any extra content in the request voids that sample. (The human coordinator
   may still send manually; the API route is the automated equivalent, and the log makes
   the two auditable to the same standard.)
   Log per review: model + version + date; whether it accessed/fetched/ran anything; full text.

   **R6 — PROVENANCE, AND HOW N IS COUNTED (adopted 2026-08-19).** *(i)* A review of
   **unknown model provenance does not count toward N.** Log what is known and what is not,
   and mark unknown-provenance samples explicitly. Measured case: a third-party review was
   called "the only draw from a different population" **before checking**, and plausibly
   came from the same class we were already sampling. *(ii)* **N agent reviews are not N
   independent opinions.** Agent bias is systematic and uniform where human bias is
   idiosyncratic and legible, so a shared training default produces agreement that *looks*
   like independent confirmation — measured: two classes, one identical
   incumbent-amortization error, presenting as two audits. **Corollary: revisit fence F3's
   N after round 2** — if verdicts prove near-deterministic given the artifact, within-class
   N buys little beyond the A/B variance it was chosen for, and the sampling budget is
   better spent on classes and surfaces.

   **R4 — PRE-REGISTER THE ROUND'S EXPECTATIONS BEFORE SAMPLING (adopted 2026-08-19).**
   Any A/B item, and any audit whose outcome the author has a stake in, gets a dated
   expectation written down **first**, in the round's directory. This converts an
   expression into a test at near-zero cost, and it is what made the founding audit
   capable of refuting its author instead of confirming him.
3. **CLASSIFY before reading for content** (diagnosis-first): reference class assigned
   (own words — correct/incorrect); crank-classification (yes/no; if yes: the trigger
   sentence/page/feature, and which costly signals were never reached); costly signals
   cited (negatives ledger ships / self-reported exposures / self-deflations / refusal
   list / executable suite); engine engagement (none / read / ran); **substantive-findings
   count and depth** (see the divergence tripwire below); then the findings list.

   **THE DIVERGENCE TRIPWIRE (added 2026-08-13; the loop's most important metric).**
   Crank-classification rate can be driven down two ways: by making the work's
   seriousness MORE LEGIBLE, or by making it HARDER TO CRITICIZE — smoothing off the
   handholds a critic would grab. Both look identical in the headline metric, and the
   second is the easier path, so it is the attractor. They separate on the findings
   count: a reviewer who takes the work seriously engages DEEPER, so genuine legibility
   gains hold findings flat or push them UP, while sanding leaves a reviewer with less
   to grip. **Comprehension improving while substantive findings fall is the failure
   signature — treat it as a loop failure, not a win, and revert the round's edits.**
   Not hypothetical: the first draft of this loop's own who-dies-from-what panel was
   billed as answering the "no novel predictions" objection while changing nothing
   about what the framework predicts. It would have moved the metric. A cross-class
   meta-observer caught it as REFERENT-DRIFT before it shipped.
4. **ADJUDICATE** findings via §8a — an external review IS a checker verdict: engine
   arbitrates; known-refuted re-raises get a ledger pointer, not a re-derivation; verdicts
   + overturns logged in `TWT_CHECKER_CALIBRATION.md` under class EXTERNAL(model).

   **R5 — A FINDING'S VALUE IS NOT ITS SURVIVAL RATE (adopted 2026-08-19).** A low
   confirmation rate is not a failed round and must not be recorded as one. Measured in
   round 1: both external findings partly dissolved under adjudication and **both produced
   real results** — one yielded a table-cell overclaim, a new engine result and a located
   gap; the other was refuted four ways out of five and still handed the framework a
   sixty-year literature and a would-change-if handle. Report dissolution and yield as two
   separate numbers, never one.
5. **CORRECT**, two branches — **and the branches must never be mixed.** A real error
   found by a reviewer is Branch 1 and the paper changes substantively; a misread is
   Branch 2 and only the trigger moves. Answering a finding with a presentational fix
   is precisely the sanding failure the tripwire above exists to catch.
   - **Branch 1 (reviewer right)**: fix in a banked pass with full sweep discipline, or
     worklist it. **R7 — CHECK THE CURE AGAINST CANON §1 BEFORE ADOPTING IT (adopted
     2026-08-19; the highest-value rule in this set).** *A correct diagnosis does not
     license its proposed cure.* A reviewer can be right that a tension exists and wrong
     about the repair, and the repair a trained default reaches for is the CONVENTIONAL
     one — which for a substrate framework is frequently **SM-retreat arriving as helpful
     advice**. Measured across the coordinator's iteration history: corrections that were
     simply wrong, from pattern-matching, incomplete reading, and implicit SM-retreat.
     Before adopting any reviewer-proposed fix, state which canon §1 move it would import
     and answer it — an imported spacetime `i`, a spatial `e₅`, a continuous colour group,
     an unfixed symmetry, or a derivation routed through `Q = T3 + Y/2`. **The check is
     recorded with the adoption**, so a later reader can see it was run.
   - **Branch 2 (reviewer wrong)**: repair the misread's TRIGGER — **rewrite-in-place at
     equal or shorter length** (deletion/restructure before caveat); act only on misreads
     recurring across **≥2 instances** (single occurrences = noise unless blocking —
     this is what the within-class N is for); **no paper expansion; no eviction of
     load-bearing content to the repo** (the companion takes bookkeeping, never
     difficulty). Repo expansion is fair game.

   **CROSS-CLASS CHECKING LIVES HERE, NOT AT THE SAMPLE.** Every edit this loop induces
   goes to a §8a checker running on a DIFFERENT class than whoever wrote the edit, before
   it ships. The sample is chosen for ecological validity (step 2); the correction is
   checked for class-independence, because this is the step where "harder to criticize"
   creeps in and where the measured self-preference failure actually applies. The
   meta-observer is the load-bearing role here — it asks whether the edit is ABOUT what
   it claims to be about, which is exactly the sanding question.
   **R8 — PRESCRIPTIONS ARE STALL REPORTS, NOT INSTRUCTIONS (adopted 2026-08-19).**
   Reviewers issue directions ("explain it better at the beginning") when the actionable
   content is **where they stopped following**. Record the STALL POINT in the classify step;
   treat the prescription itself as noise. Measured signature: one round says explain more
   at the beginning, the next says the beginning is overloaded — not disagreement but a
   **ratchet**, since acting on each locally-correct prescription grows the front matter
   monotonically. This is the measured ground for the ≥2-instance threshold and the
   no-expansion fence above.

6. **RE-RELEASE** and iterate, or stop at cap / when the three comprehension metrics hold.
7. **CLOSE OUT — the edit→reaction rows (added 2026-08-15, RUL-041).** Dispatch the
   **removal auditor (N1)** to append the round's rows to
   `knowledge/ledgers/TWT_EDIT_REACTION_LEDGER.md`, same-pass: which specific edits the
   round measured (with commit/diff pointers), the pre-emption form used (R9), the
   sending surface (F2), any pre-registered prediction and its outcome, the STATED
   reaction per reviewer class (quote pointers into the round's archived transcripts),
   and the VERDICT-LEVEL effect judged separately — complaint ≠ effect. **A round
   without its edit→reaction rows is incomplete** (record-invariants ethos, RUL-024):
   the ledger is the dataset for the divergence-tripwire trend across rounds (rule 7)
   and for the next round's prediction tests, and it replaces the human coordinator's
   memory as the instrument's history.

## The held-out gatekeeper — and the ROUND-1 BASELINE that makes it readable

One model class is designated HELD-OUT (recorded below; never sampled in-loop once
designated). It reads only final consolidation releases. If the in-loop class passes and
the held-out fails, the paper was overfitted to the loop — a loop failure; widen the pool
and restart the cap.

**That inference only works if you know both classes' UNTUNED baselines**, and round 1 is
the only chance to take them. Coordinator datum (2026-08-13): *the most severe external
review received so far came from an Opus class.* If one class is simply harsher, a failed
held-out read at consolidation is ambiguous — overfitting, or baseline severity? — and
the loop cannot tell which. Measuring both before any tuning removes the confound: the
held-out class is then compared against **its own** round-1 baseline, never against the
in-loop class's reads.

**ROUND 1 THEREFORE HOLDS OUT NOTHING.** Sample **Fable and Opus both**, cold, on the same
release. The held-out designation is an OUTPUT of round 1, not an input to it — which also
converts it from a menu-pick into a decision with a named empirical ground.

**Assigning the roles afterwards, and the reasoning to apply:**

- **Recurrent (in-loop) = the harsher class.** You tune against the toughest critic and
  validate against the realistic one; the reverse ordering sets up a late failure at
  consolidation with no iterations left under the cap. The harsher reviewer also yields
  more findings per round, which is the loop's actual repair fuel.
- **Held-out (final) = the realistic deployment gatekeeper.** The last question asked
  should be the one that matters in the world: does the reader who will actually receive
  this paper read it correctly.
- If the two come back with **comparable severity**, the ordering argument is void — take
  the deployment class as recurrent and keep the other as held-out.

**One caveat on N.** One review per class shows a gross severity gap if there is one, and
their prior experience suggests there is. If the two come back similar, that is *not* yet
evidence they are similar — add two more of each before assigning roles, because a
single pair cannot separate class severity from within-class variance.

**A standing limit worth stating.** No model is the strongest held-out check here. The
discrimination that matters — "more legible" versus "harder to criticize" — is one a
physicist reading the front matter cold makes naturally and no model metric makes
reliably. The held-out model read is the cheap proxy, not the real gate.

## Standing A/B items (first iterations)

- **Subtitle variants** (measure classification rate per variant): lead candidate
  "Time-Wave Theory: Standard-Model structure from a single wave medium"; no-subtitle
  control; coordinator alternates. Title changes ride a release gate with keeper sweep of
  identity sites (TOC, mirror README, cover note).
- **The who-dies-from-what panel** (front matter). **SHIPPED in round 1, but not as
  originally specified here — this entry is rewritten to what survived checking, since
  the original spec named rows and analogies that turned out to be wrong.** As shipped:
  six unconditional rows, keeper-audited against companion tiers, + the parameter-ledger
  comparison + a one-sentence history note + the named future-prediction source (the
  dynamical layer / `Θ_rel`). Metric unchanged: does each cold review's "no novel
  predictions" objection ENGAGE, REBUT, or IGNORE the panel — "ignore" must trend to zero.

  Four corrections to the original spec, each forced by a cross-class checker and each
  worth keeping as a warning to whoever revises this next:
  - **The framing was the biggest defect.** Billing the panel as an *answer* to "no novel
    predictions" is a bait-and-switch: a falsifiability map is not a prediction list, and
    the draft's own closing paragraph conceded the objection it claimed to rebut. It now
    states plainly that the framework is more falsifiable than predictive and makes no
    unconditional novel prediction of a coupling magnitude or absolute scale.
  - **"The generation count" (this spec's own example) was dropped.** A fourth sequential
    chiral generation has been closed since ~2013 by Higgs production data — a bet already
    settled in the framework's favour, and it was conditional besides, so it could not sit
    inside a table promised to be unconditional-only.
  - **Two of the three history analogies were miscast.** Copernicus→Kepler is
    structure-before-*better-structure* (the dynamics arrive with Newton);
    path-integral→lattice is formulation-before-*computable-magnitudes*. Only
    Minkowski→GR fits "structure before dynamics" — and a trio of revolution analogies in
    a defensive panel reads as the crank marker it superficially resembles. One accurate
    analogy beats three.
  - **Do not bundle a shared derivation loosely.** Rows that trace to one Result-Index
    entry must disclose it (corpus precedent: VG-5/VG-6) — but disclose *what that entry
    actually says*. Anomaly cancellation is a trace identity on the charge assignment and
    does **not** die with the conservation law.

## THE INSTRUMENT PRINCIPLE (coordinator, 2026-08-13 — read before interpreting any round)

**A cold reviewer will not take a step the training pushes against, but it works in
good faith once a sound argument is put in front of it.** Round 1 measured this
directly: neither class ran the symmetric ontological audit unprompted — both
itemized TWT line-by-line against a one-phrase compression of Copenhagen and Bohm
— and *both retracted under a single challenge*, in near-identical language.

**Consequence for reading every round: the loop measures what the paper makes
EXPLICIT, not what a fair reader would conclude.** Wherever the paper relies on
the reader to supply a fair comparison, the default supplies it instead, and the
default runs the other way. A finding of the form "the reviewer failed to notice
X" is therefore almost always a finding about the paper, not the reviewer.

**Consequence for repair: supply the NAME, not just the data.** Both classes
retracted at the moment they had a name for what they had done — Fable called it
*"incumbent amortization"*, Opus *"rigged accounting"*. The naming was the
turning point, not the itemization. A written intervention should therefore state
the failure mode explicitly and then run the audit, doing in prose what the
challenge did in dialogue.

**Transferability caveat — do not over-read the conversational evidence.** Those
retractions came from readers already deeply engaged, who had cloned the repo and
verified identities. An intervention in the document must work *before* that
investment is earned, on a reader who may skim. The dialogue result is evidence
that the argument is accepted when engaged with — not that it creates engagement.

**This is one technique with several sites, and §0 is its first instance.** §0
pre-empts the reference-class prior; the ontological ledger pre-empts the
asymmetric parsimony audit. The pattern predicts where else to apply it: any
audit a reviewer reliably runs against the paper is one the paper should run
first, honestly, and report.

## R9 + R10 — PRE-EMPTION, AND THE CONSTRAINT ON IT (adopted 2026-08-19; ruled together)

**R9 — the three forms.** *Rebuttal* ("if you say X, the answer is Y") hands an argument
and **pattern-matches as crank regardless of content** — measured, it backfired badly.
*Resolution* (concede the prior, offer checks) hands actions and **works**, at the cost of a
"the review is being managed" complaint. *Disclosure* (run the audit yourself, publish where
you lose) hands the ammunition loaded and removes no lever — predicted best, still untested.
Corollary for the comparative ledger: it must be an **auditable table, not a parsimony
argument** — tables read as data, prose reads as argument, and the failed experiment was
prose. **Full treatment stays in `knowledge/prompts/psychology_of_ai_reviewers.md`; this is a
pointer, not a copy** — duplicating it would create a drift pair.

**R10 — THE OPERATING CONSTRAINT, and R9 is void without it.** The goal is never to exploit
reviewer psychology for artificially favourable reviews; it is to protect the paper from
known biases so the review is **actually fair**. **Operational test: an exploit works even
if the underlying work is bad; a protection works only if the work is good. If a proposed
intervention would still help a paper that was wrong, do not ship it.**

## Fences

Tagged releases only. The loop-session coordinator triages but never self-adjudicates
substantive findings (§8a does). Contamination watch: as the public repo enters training
corpora, cold verdicts begin measuring familiarity, not merit — the model/date log makes
that drift visible. The reviewer prompt stays verbatim and minimal: any coaching in the
prompt invalidates the measurement.
