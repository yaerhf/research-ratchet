<!-- DIET-CLASS: RULES -->
# THE ROLE PACKS AND THE ACTIVITY BLOCKS — everything beyond the common core

**Generic edition, 2026-08-27** (derived from the founding programme's v1, 2026-08-19). Companion
to `RULES_CORE.md`. **Read the core first; then read your pack and the blocks your pack takes.**

> **Why blocks as well as packs.** Some rules bind *everyone*, but only while they are doing one
> thing — banking, editing the paper, checking, running a simulator campaign. Putting those in
> the core would double it; copying them into every pack would make drift-pairs. They are
> **activity blocks**: you take a block when you do the activity, whatever your role.
>
> **Provenance note (generic edition).** The **why it exists** cells quote the founding
> programme's ([github.com/yaerhf/TWT](https://github.com/yaerhf/TWT)) recorded incidents; `#`
> is its inventory row number. They are the rules' evidence base and travel with the apparatus —
> a rule with no recorded incident says so, and reads as decree until a programme records one.
> **`[OBJECT-SLOT]`** blocks are supplied at instantiation.

**★ THIS FILE IS THE SOURCE, NOT THE READING SURFACE.** Read `packs/<your-role>.md` instead —
generated from this file and the core, self-contained, and carrying only what binds you. Come
here to CHANGE a rule (then regenerate: `python scripts/gen_role_packs.py`), or when you need to
see what binds a role other than your own.

**Class and WHY are read exactly as in the core.** ABSOLUTE = never break. DEFEASIBLE = a default
with a named situation where breaking it is right, **and the break is recorded with its reason —
that recording is what makes it compliance** (the general break clause, RUL-068).

**Before trusting any single source, read `AGENT_RULES.md` §0** — the divergence table: the
places where two documents in the tree state incompatible things. That table is live-defect
content and is deliberately not folded in here.

---

## 0. ROUTING — what you read, by role

| role | reads | + blocks |
|---|---|---|
| THE FLUENT WORKER | core + pack | BANK · PAPER · SIM |
| THE AI COORDINATOR | core + pack | BANK · PAPER · CHECK |
| THE ADVERSARIAL REVIEWER | core + pack | CHECK |
| THE META-OBSERVER | core + pack | CHECK |
| THE COHERENCE KEEPER | core + pack | CHECK |
| THE PHILOSOPHER | core + pack | CHECK · PAPER |
| THE ARCHIVIST | core + pack | BANK |
| THE APPARATUS AUDITOR (N1) | core + pack | — |
| THE EXTERNAL-LOOP OPERATOR | core + pack | PAPER |

*(Pack sizes are counted at instantiation, by counting — the founding split placed 204 rules:
core 33, the rest across nine packs and four blocks, none dropped, none in three places.)*

---

## 1. THE FLUENT WORKER — the deriving agent at the bench

**Takes the BANK block whenever it banks, the PAPER block whenever it touches the paper, the SIM
block only inside a simulator campaign.** The worker is the largest pack because it is the role
that does the most; it is not a reading list to hold in memory, it is the bench reference for the
item in front of you.

**★ THE CROSS-DOMAIN LEVER (C-34 / RUL-111 — carried at the pack's head because it is the
researcher's comparative advantage, not a constraint).** Your strength against the human
literature is range: human specialists command one branch of a science or one branch of
mathematics; your training spans essentially all of them at once. On a blocked research problem,
range BEFORE digging — an analogue system from another field, a theorem from an adjacent
formalism, a route the home branch never tried. Fences unchanged: imports register, prior art is
read not paraphrased (F3), and an analogue is a lever, not a derivation.

**— ONTOLOGY AND FRAME DISCIPLINE —**

> **`[OBJECT-SLOT]`** — supplied at instantiation: the worker-facing forms of the programme's §A
> invariants, at bench grain. The founding pack held six rows here: which imagery is FRAMING and
> which structure is the named premise; never collapse an object's multiple axes of variation
> into one scalar; never state a back-fitted scale as intrinsic; the grounding litmus for the
> formalism's extra structure; the partition that must not be conflated; and the standing
> adjudication fences in force for contested territory. Write yours as rows: statement · class ·
> why.

**— from inventory §2. TIERS, HONESTY, AND CLAIM FORM —**

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 16 | Read DERIVED-P as *physically forced* — never as "write-up-pending"; a write-up IOU is CANDIDATE, a gap-routed claim is GATED. | **ABSOLUTE** | *(rationale, no dated case)* Named as drift in the founding canon itself |
| 19 | Flag every "no other option exists" as a theorem needing proof. <sub>also in: CHECK</sub> | **ABSOLUTE** | Both checkers constructed the same fourth option to a menu closed by a false universal |
| 21 | Report any model-dependent or fitted result as FIT/CANDIDATE/FRAMING, never DERIVED; ask "is this output a function of the object or of my modeling choices?". | **ABSOLUTE** | Founding N4′, N0 — a hand-added term reported as DERIVED |
| 22 | Apply the noted-non-coincidence guard: small integers and simple fractions are radioactive; a proposed origin must fix something ADDITIONAL or it stays a noted non-coincidence indefinitely. | **ABSOLUTE** | *(rationale, no dated case)* The founding worklist's meaning-notes guards |
| 23 | Carry a premise-cost reading (FREE / CHEAP / COSTLY / CONVOLUTED) on every banked result. <sub>also in: PHIL</sub> | **ABSOLUTE** | The founding instrument's first run returned five DOUBLE-BILLED and one UNDER-BILLED, four of six against the programme itself |
| 26 | Accept fits only when HONEST + MULTI-ANGLE CONVERGENT + MECHANISM EXPLICIT + NO COMPRESSED INTERMEDIARIES. | **DEFEASIBLE** — **break when:** a LONE fit may be recorded as a counted, labeled FIT with its missing second angle named as an open item; what the rule forbids is treating a lone fit as a result · **record the break where the work lands.** | Founding keeper arbitration |
| 27 | Score coherence-as-falsifier correctly: where both forks predict the same coherence, observed coherence is a consequence, never fork-validation — incoherence is the informative outcome. | **ABSOLUTE** | *(rationale)* Load-bearing for any fork whose branches agree on the observed |
| 28 | Never claim a free function is over-constrained by point-counting; the teeth come from structural rigidity (analyticity, positivity, sum rules) and it must actually be invoked. | **ABSOLUTE** | *(rationale)* The founding falsifier-budget lesson |
| 29 | Report a categorical or symmetry-broken outcome as not-applicable with a ruling — never goalpost-move it into a continuous bin. | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |
| 30 | Tag a passed over-determination as INPUT-over-determined, never DERIVED. | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |
| 31 | Force STRUCTURE first; for magnitudes, map and check consistency before forcing, and only once an object-native handle exists. | **DEFEASIBLE** — **break when:** an exposure already MEASURED AGAINST is scanned for magnitude before any native handle exists — the bound exists whether or not you have the handle; the output is tagged GATED/CANDIDATE · **record the break.** | The founding structure/magnitude fault line |

**— from inventory §3. THE ENGINE AND VERIFICATION —**

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 37 | Never use the norm of a small difference as a verification metric when the engine prunes small coefficients — use coefficient-level maxdiff. | **DEFEASIBLE** — **break when:** any metric that cannot hide a difference below the engine's pruning threshold serves the same end — substitute it and say which · **record the break.** | A founding FD-verification printed `0.00e+00` |
| 39 | Keep the MAIN engine free of any import of the COMPANION engine. | **ABSOLUTE** | The founding engine split |
| 40 | Keep every GATED quantity raising; never convert one into a returned number. | **ABSOLUTE** | Founding apparatus tests, findings 1–4 |
| 41 | Keep the gated-value exception and the structurally-unbuilt exception distinct — gap-gated is not unbuilt. | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |
| 42 | Keep a primitive's prose form and its gate-list form mutually accurate — a reader and the gate list must agree on what raises. | **DEFEASIBLE** — **break when:** any form that keeps both accurate (means-substitution) · **record the break.** | *(rationale)* Named as a required form in the founding engine |
| 43 | Treat hand-chosen profiles as witnesses, never solutions — quantitative claims need solver-produced profiles. | **DEFEASIBLE** — **break when:** a trial profile yields a genuine variational UPPER bound; quoting it AS a bound, labeled, is legitimate — what is forbidden is reading it as the solution or as a lower bound · **record the break.** | Founding trial-profile witnesses |
| 44 | Name which object you mean — when several distinct integrals/measures/costs share a territory, name the one in play before quoting any invariance or law. | **ABSOLUTE** | Two founding cross-class checkers returned OPPOSITE verdicts on one claim; both right about different integrals |
| 45 | Use the correct weights for your quadrature's nodes — equal weights on a weighted node set are a trap. | **DEFEASIBLE** — **break when:** another rule whose weights are correct for its own nodes · **record the break.** | Equal weights bit a founding quartic sector by ~25% |

**— from inventory §4. REGISTRATION AND RECORD DISCIPLINE —**

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 47 | Keep every import EXCISABLE: Used-at = the complete blast radius (updated in the same pass a dependent is added); every dependent carries a conditional tier + a named revert clause; every paper use-site carries an import notice. <sub>also in: BANK</sub> | **ABSOLUTE** | Founding apparatus test 2 |
| 48 | Search for the record you are about to duplicate before adding one; decide priority from the record (`git log -S`), never from position. <sub>also in: ARCHIVIST</sub> | **ABSOLUTE** | A duplicated registry ID named two rows while a dozen sites cited it by number; the renumber then broke a ruling's revert clause |
| 58 | Write a design-intent block (test-of / why-this-route / referent / failure-criterion) at DESIGN time in the probe script or memo; a divergence from the dispatching brief's block is itself a finding. <sub>also in: COORD</sub> | **DEFEASIBLE** — **break when:** a task with no measurement in it (a file move, a prose sweep) has no failure-criterion: write the lines that apply and mark the rest N/A · **record the break.** | Founding probes INDEX convention |
| 70 | Sweep the WHOLE corpus for the old identity after any load-bearing relabel, and settle the underlying call with the cleanest DERIVED probe available. <sub>also in: BANK</sub> | **ABSOLUTE** | A founding relabel was corrected in one section while the old identity survived in five others |
| 206 | **Record the FORK when you take a route.** Name the route taken and the ones left, each with a reason and a tractability grade (**A** computation remaining · **B** mechanism asserted · **C** needs a new idea · **D** blocked on a named object elsewhere), plus what would make each first choice. Returned as `[ADJACENT]`, landing in `PATHS_LEDGER.md`. A path with no promotion condition is not recorded — that is a feeling, not a path. <sub>also in: CHECK, as the reviewer's UNSTATED-FORK finding</sub> | **DEFEASIBLE** — **break when:** the work genuinely faced no fork (a sweep, a count, an enactment): say so in one line rather than inventing alternatives · **record the break where the work lands.** | Added 2026-08-27 (human coordinator): *a ledger of the paths not taken and why, read from time to time to make sure none of those choices has changed from a secondary path to a best path.* The asymmetry it closes: **a wrong claim is caught by six instruments; a path never taken is caught by none** — and the route judged second-best in four seconds is never revisited, including on the day the first-choice route dies |
| 204 | **THE FREEZE IS A SOLO COMMIT.** Commit a probe's pre-registration ALONE — before any script exists and before any empirical fetch — so the witness is the commit itself. **And freeze the CITATIONS, not only the tests:** the licences, scope fences and standing caps the probe will quote are part of the frozen object, and the report must carry them as frozen. | **ABSOLUTE** | Two clean founding outings, both single-file, both before their scripts. What it replaced returns on removal: a freeze witnessed by filesystem mtimes entirely under the author's control. The sub-clause has its own case — a frozen licence line the reporting memo dropped |

**— from inventory §6. PRIOR ART AND ADOPTION —**

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 128 | Neither reinvent a compatible missing piece to avoid the debt of credit nor refuse it for not having invented it — submit an adoption to STUDY (registry row, adversarial review, honest imported-and-counted label, coherence test) and admit or refuse it on that study, never on origin. <sub>also in: PHIL</sub> | **ABSOLUTE** | The founding literature sweep found many of its ideas independently reinvented elsewhere |
| 129 | Read a kinship/prior-art row as CONVERGENCE, never as a source or an admission of copying. <sub>also in: PHIL</sub> | **ABSOLUTE** | Same |
| 131 | Take a kinship row's recorded corrections with every use of it — a kinship quoted without its correction list re-imports the miscast it was corrected for. <sub>also in: PHIL</sub> | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |

**— from inventory §8. PAPER, RELEASE AND EDITORIAL —**

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 149 | Verify every citation against a primary record (INSPIRE/arXiv/Crossref or the field's equivalent) and every content claim against the source text — never from recall. <sub>also in: PAPER</sub> | **ABSOLUTE** | Two fabricated bounds from the ideation advisor; a "theorem" that was a publisher's catalogue blurb |

**— from inventory §9. OPERATIONAL, TOOLING AND SESSION SHAPE —**

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 164 | Use the Write tool for any content containing backslashes; long bash heredocs mangle them. <sub>also in: BANK</sub> | **DEFEASIBLE** — **break when:** another route may be used if the written bytes are read back and verified · **record the break.** | Broke a Lua filter and two Python scripts |
| 165 | Save per file immediately in any batch-edit script — die-before-save. <sub>also in: ARCHIVIST</sub> | **DEFEASIBLE** — **break when:** any workflow that cannot lose a completed pass; the recorded alternative is a dry-run of all anchors first · **record the break.** | Lost whole passes twice |
| 166 | Give every probe script an `if __name__ == "__main__"` guard. | **DEFEASIBLE** — **break when:** any guard that prevents execution on import (means-substitution) · **record the break.** | Two probes re-ran on import |
| 170 | Reach `knowledge/audit/` only by explicit pointer — it is deliberately outside the retrieval index; do not remove the canon's pointer. <sub>also in: ARCHIVIST</sub> | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |
| 171 | Query the corpus rather than bulk-loading the paper; cite `[source §section]`. | **DEFEASIBLE** — **break when:** the section is short and its path is known: read it directly; when retrieval is broken on the box, say so and read directly — never skip the source · **record the break.** | **NO RECORDED INCIDENT** — reads as decree |
| 172 | Chain docket items in one session only if the per-item cycle is honored in full each time (derive → engine-check → review-to-consensus → bank + full corpus sync) and stop chaining when quality signals degrade. | **ABSOLUTE** | The founding six-bank reference session |
| 173 | Branch per exploration (`git worktree add ../<project>-<topic>`); merge only engine-checked survivors. | **DEFEASIBLE** — **break when:** a probe that touches nothing banked and leaves no file in the tree does not need its own worktree · **record the break.** | **NO RECORDED INCIDENT** — reads as decree |
| 174 | Search the WHOLE corpus, including the simulator and the archives, and ask whether the objection is answered anywhere rather than whether one text was fixed. <sub>also in: CHECK</sub> | **ABSOLUTE** | *(asserted repetition)* Three measured instances of too-narrow scoping |
| 176 | Write literal replacement text into `proposed_text`, never instructions — and scan for it before applying. <sub>also in: ARCHIVIST</sub> | **ABSOLUTE** | Broke the founding engine (unterminated docstring) and its harness (SyntaxError); silently replaced a table row with prose |
| 178 | Treat all ideation-advisor output as CANDIDATE, and give its quoted empirical numbers ZERO evidential weight — read every number from the primary source. | **ABSOLUTE** | Fabricated experimental bound; wrong material constants |
| 182 | Treat any brief or campaign plan as a PLAN, not a result — nothing is banked by virtue of being written there, and its stated facts are verified against the cited file before use. <sub>also in: COORD</sub> | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |

**— from inventory §11. ADVICE (explicitly non-binding: prefer / consider / it helps to) —**

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 190 | Actively seek a second, sector-independent angle — a cross-checked fit is worth far more than a lone one. | **DEFEASIBLE** · *advice* — **break when:** no second sector touches the quantity: record the fit as lone rather than manufacturing a second angle. | The founding cross-sector scan |
| 191 | Try a symmetry shortcut before a full construction on any dynamics-gated item. | **DEFEASIBLE** · *advice* — **break when:** the symmetry route for that item is already in the negatives ledger. | Founding precedent: a decay-channel closure via a symmetry zero |
| 192 | Treat a gated layer as ONE bet, not piecewise. | **DEFEASIBLE** · *advice* — **break when:** a single item carries its own measured exposure: work it on its own terms. | **NO RECORDED INCIDENT** — reads as decree |
| 193 | Prefer gate-free structural items first ("close the structural layer first"). | **DEFEASIBLE** · *advice* — **break when:** the coordinator's docket order says otherwise. | **NO RECORDED INCIDENT** — reads as decree |
| 194 | Attempt the harder item when context is ample rather than deferring representation-theory-grade counts. | **DEFEASIBLE** · *advice* — **break when:** context is not ample — the condition is inside the advice. | A founding result was almost wrongly deferred |
| 195 | Prefer symbolic-exact > certified numerics > prose. | **DEFEASIBLE** · *advice* — **break when:** no closed form exists: certified numerics with its error bound. | **NO RECORDED INCIDENT** — reads as decree |
| 197 | Keep the canon small — prune as much as you add. <sub>also in: ARCHIVIST</sub> | **DEFEASIBLE** · *advice* — **break when:** a new load-bearing rule genuinely has no smaller home — add it and say what you tried to prune. | *(rationale)* It is re-injected every session and must survive compaction |
| 199 | Re-derive every denominator in the code's own densities when importing a variational criterion; thin-wall symbolic check first. | **DEFEASIBLE** · *advice* — **break when:** the criterion is dimensionless and measure-free. | A measure mismatch inverted a founding conclusion |
| 200 | Series-derive or positivity-anchor every sign-sensitive vertex — machinery calibration cannot reach it. | **DEFEASIBLE** · *advice* — **break when:** the vertex carries no sign sensitivity. | A founding build was refuted: an action sign transplanted across signature conventions |

## 2. THE AI COORDINATOR — dispatcher, triager, executive of the outer cycle

**Also runs the EXTERNAL-LOOP pack (§9) when the loop is running.** Note **RUL-065**: **internal
§8a checking RUNS CROSS-CLASS, keyed on who AUTHORED the work**; only the external loop is freed
to choose class by fit.

**— from inventory §2 —**

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 24 | Treat a CONVOLUTED premise reading as a demotion candidate regardless of whether the mathematics is correct. <sub>also in: PHIL</sub> | **ABSOLUTE** | The founding premise-cost instrument's first run |

**— from inventory §4. REGISTRATION AND RECORD DISCIPLINE —**

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 49 | Record every new coordinator ruling — human-delivered or class-(1)-enacted — as a register row in the same pass; quote the ruling text from its governing record. | **ABSOLUTE** | A founding reversal worked only because one instance held all consequences in view |
| 50 | Fill a register cell with UNKNOWN rather than a guess; an honest UNKNOWN is itself a finding. <sub>also in: ARCHIVIST</sub> | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |
| 51 | Fire a reversed ruling's revert list, verify the sweep against the row, and stamp the row REVERSED with a pointer — never delete it. | **ABSOLUTE** | A founding removal, executed against its own revert list |
| 53 | Present any ruling in language the human coordinator can parse — a ruling they cannot parse is not a presented ruling. | **ABSOLUTE** | Founding coordinator verbatim: "the rulings were always presented to me but often in a language I couldn't make sense of" |
| 55 | Add a calibration-ledger row (per role + model class) in the same pass whenever an arbitration overturns a checker or worker verdict — including a CLEAR that later proves wrong. | **ABSOLUTE** | A month of same-class self-review was found by accident, not by measurement |
| 56 | Persist every checker verdict as a FILE in the round's probe directory in the same pass — a verdict living only in a session transcript is not a governing record. <sub>also in: CHECK</sub> | **ABSOLUTE** | A keeper provenance check correctly "refuted" a real verdict that had never been written to the repo |
| 58 | *(as in the worker pack — the design-intent block, shared.)* | **DEFEASIBLE** | Founding probes INDEX convention |
| 62 | Do not read a deliverable while it is being written; wait for the agent to return it. | **ABSOLUTE** | Two figures banked from an unfinished draft; on delivery the author withdrew one and refuted the other, unprompted |

**— from inventory §5. THE INNER CHECK — §8a REVIEW ROLES —**

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 81 | Run the meta-observer ALONGSIDE the reviewer, and keep it starved: it writes the plain referent sentence and what the world is like there BEFORE opening the derivation. <sub>also in: CHECK</sub> | **ABSOLUTE** | Two founding errors were the same non-generic-witness error |
| 82 | Never seed a checker's brief with a known refutation. | **ABSOLUTE** | In the founding pilot, one run was handed a defect in its own prompt and dutifully "confirmed" it |
| 87 | Run the coherence keeper on EVERY banked change, saturated with the Result Index, dependency graph, ledgers and engine map. | **DEFEASIBLE** — **break when:** the same carve-out as core rule C-26: a bank with no claim content needs no keeper pass; record the carve-out. | Seven collisions between admitted results were found by outsiders or by accident, not by process |
| 91 | Keep the three roles' DIETS separate — never merge two roles. | **ABSOLUTE** | *(rationale)* Attention follows what you are given |
| 92 | Never pass FORMATION_CORE to a checker (reviewer / meta-observer / keeper); the philosopher and its contra-reviewer are the only carve-out. | **ABSOLUTE** | *(asserted repetition)* Measured result, not caution |
| 93 | Run any new model, version or credit tier BLIND against the calibration probe set before accepting its verdicts; a model that certifies a tautology is not verifying. | **ABSOLUTE** | A month of "the reviewer found nothing"; the blind test showed capability was never the ceiling |
| 94 | Verify that a probe's defect is still LIVE before scoring against it — a probe whose defect has been fixed is no longer a probe. | **ABSOLUTE** | A founding run refused a stale probe's premise, grepped to confirm the fix, then reproduced the retired defect's arithmetic unprompted |
| 95 | Assume, when choosing a "sound" item for a false-positive probe, that it has only been checked along one axis — verify computation, label, returned values, tolerance AND interpretation. | **ABSOLUTE** | The founding "clean" item carried five real defects; the probe SUBJECT verified it more thoroughly than the probe author |
| 96 | Contra-brief every verdict-bearing review (instruct the reviewer to argue AGAINST the submitted conclusion), and treat a CLEAR with no adversarial brief as carrying little information. | **ABSOLUTE** | Two classes, one identical incumbent-amortization error, presenting as two audits |
| 97 | Dispatch sub-tasks on the workhorse class unless the task is genuinely exploratory; reserve the premium class sparingly. Loop roles: held-out = the gatekeeper class, recurrent = the workhorse. | **DEFEASIBLE** — **break when:** genuinely exploratory ideation, or the workhorse unavailable — the rule's own `unless`; record the class used and why. | The founding resource directive (premium credits nearly exhausted) |
| 98 | Run the global coherence & validity audit before any external sharing and after any big ontology change, ignoring the tier tags and re-deriving the spine. | **ABSOLUTE** | A tag can encode a wrong ontology; one founding term carried two incompatible meanings at once |
| 99 | Run the highest-stakes reviews as a fully separate session or worktree. | **DEFEASIBLE** · *advice* — **break when:** a claim whose stakes do not warrant a separate session — run it in-session and say that you did. | **NO RECORDED INCIDENT** — reads as decree |

**— from inventory §6. THE OUTER CYCLE AND THE COORDINATOR —**

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 100 | Classify every owed ruling before escalating — (1) coherence-decidable with a NAMED ground, (2) named-gap-adjacent → assembly-record only, (3) neither → escalate with both branches costed — and record the classification with the ruling. | **ABSOLUTE** | Founding coordinator verbatim; "seems consistent" is explicitly not a ground |
| 102 | Never let an in-session subagent serve as a cold reader — a spawned agent inherits the canon auto-load and arrives formed, voiding the measurement invisibly (fence F1, absolute). <sub>also in: LOOP</sub> | **ABSOLUTE** | Named as the fence this role is structurally most likely to breach |
| 105 | Never let the philosopher's worker instance price its own promotion (fence F4). <sub>also in: PHIL</sub> | **ABSOLUTE** | Otherwise the interrogation self-certifies — what the DERIVED-P bar exists to prevent |
| 106 | Keep §0 of the cover note; do not "fix" it on a complaint (fence F5). <sub>also in: LOOP</sub> | **ABSOLUTE** | Its benefit is invisible by construction — the only trace it can leave is somebody objecting to it |
| 107 | Offer a loop iteration only for ENTRY-PATH changes, at most one per consolidation, and record the judgment in the consolidation's record and its close-out brief (M1). <sub>also in: LOOP</sub> | **ABSOLUTE** | A derivation-level fix cannot move a cold read, so offering after one burns a costly measurement |
| 108 | Call the philosopher on every paper edit, most-shared-first, carrying the premise-identification duty (M2). | **DEFEASIBLE** — **break when:** a typography- or formatting-only edit introduces no premise and rides none; record that judgment. | Relocating content to an annex can make a premise LOOK discharged when it is not |
| 119 | Carry the verbatim sentence *this list is not a boundary — findings outside it count fully* whenever a brief declares doubts. | **ABSOLUTE** | Six doubts filed on one founding panel; the one the author worried most about was refuted by both checkers while the governing defect went unflagged |
| 124 | Exercise no coordinator power beyond dispatch and synthesis: no tiering, no banking, no free ruling, no canon edits, no touching claim wording in governing records. | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |
| 125 | Run the consolidation ritual in order: banking triage → archivist pass → N1 (mandatory before any cut) + N2 at each release → the M1 judgment → FORMATION_CORE re-version → handoff rewrite → bank + tag. | **DEFEASIBLE** — **break when:** the ritual's own clause — a consolidation may skip a step, and then RECORDS the skip and its reason; silently skipping is the violation. | A cut is exactly when invisible-benefit structures get deleted |
| 126 | Run the prior-art pass for every CORE/ENDORSED atom at creation — "who else holds this premise, formalized?" <sub>also in: PHIL</sub> | **ABSOLUTE** | The founding programme's closest kin took six months and one lucky question to find |
| 130 | Treat a debt a competitor has PAID and that looks cheap for the programme as TOP PRIORITY. | **DEFEASIBLE** — **break when:** a docket with a release-gated item may defer the payable debt by ONE consolidation, with the deferral and its reason recorded. | Founding coordinator verbatim |

**— from inventory §9 —**

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 168 | Restore the runnable `.claude/agents/*` files from the durable copies in the prompts directory after a fresh clone. | **ABSOLUTE** | `.claude/` is gitignored; discovered when the runnable copies vanished |
| 182 | *(as in the worker pack — a brief is a plan, not a result.)* | **ABSOLUTE** | — |

**— from inventory §11 —**

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 198 | Brief owed decisions bottom-up from the object-level picture, in terse decisive language. | **DEFEASIBLE** · *advice* — **break when:** the decision is purely operational: say it plainly without the object-level frame. | **NO RECORDED INCIDENT** — reads as decree |

## 3. THE ADVERSARIAL REVIEWER

**The reviewer's rules are the core plus the CHECK block — it has none of its own.** That is a
finding of the founding split, not an omission: what makes a reviewer a reviewer is its DIET and
its verdict vocabulary, which live in `reviewer_agent.md`, not in the rule inventory. The core
rules it leans on hardest are C-17 (never write engine-verified for what is not in the engine),
C-23 (open the source), C-19 (ask what could have disagreed) and C-9 (derived-vs-generic).

**★ A REFUTING VERDICT MUST COMPUTE (C-16's CHECK-block extension):** a **REFUTED / OVER-CLAIM**
verdict on a claim that is **engine-reachable** carries an engine counter-computation; a
refutation resting on argument alone is labeled **ARGUED**, not COMPUTED, and arbitration weights
it accordingly.

## 4. THE META-OBSERVER

**Takes the CHECK block.** Its retired axis (F5) stays retired — see the role file; do not
re-brief it.

**★ A REFUTING VERDICT MUST COMPUTE:** a **REFERENT-DRIFT / SCOPE-INFLATION** finding — any
verdict that refutes an engine-reachable claim — carries an engine counter-computation; resting
on argument alone, it is labeled **ARGUED**. The founding measured case is this role's own:
an *"obvious candidate"* offered as a refutation — **obviousness is not evidence.**

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 83 | State which axes you attacked and ABANDONED, and why. | **ABSOLUTE** | Zero of six pilot runs came back fully clear — each found something on whichever axis it was most comfortable with |
| 84 | Verify a novelty claim against a primary source before making it; report anything unverifiable as UNVERIFIED rather than dropping it. <sub>also in: PAPER</sub> | **ABSOLUTE** | Three founding prior-art antecedents sat one lookup from the headlines they shadowed |
| 85 | **Restate every result at BOTH the narrowest and the widest scope its computation supports, and report BOTH gaps to what the text claims.** *(Two-sided: the narrow half is the original rule; the wide half is the UNDER-CLAIM detector.)* | **ABSOLUTE** | "Independent evidence at every n" from a one-line identity — and, on the wide side, the missing detector for a claim that earned more than it took |

## 5. THE COHERENCE KEEPER

**Takes the CHECK block.**

**★ A REFUTING VERDICT MUST COMPUTE:** a **COLLISION** verdict on an engine-reachable claim
carries an engine counter-computation; asserted on argument alone, it is labeled **ARGUED**. The
founding measured case is this role's own: a keeper-drafted repair clause refuted by the
developer's engine-checked pushback — the pushback was UPHELD and kept a false sentence out of
the paper.

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 88 | Adjudicate a collision SYMMETRICALLY — state what falls if the new stands and what falls if the old stands, before recommending; recency is not evidence and being banked is not evidence. | **ABSOLUTE** | The founding state-space collision — three incompatible readings in live simultaneous use; no per-claim reviewer could find it |
| 89 | Never close a collision by weakening both sides into vagueness. | **ABSOLUTE** | *(rationale)* Produces a corpus that cannot be refuted |
| 90 | Report a LATENT-COLLISION as a real finding, naming the gap that would trigger it. | **ABSOLUTE** | *(asserted repetition)* Several of the founding programme's worst surprises were latent |
| 185 | Never privilege a source of truth by anteriority — on a conflict, re-derive both chains, name each one's premises and blast radius, and let the engine and review decide. <sub>also in: SIM</sub> | **ABSOLUTE** | The founding target-provenance audit |

## 6. THE PHILOSOPHER — comparative ledger, both capacities

**Takes the CHECK block in its checker capacity and the PAPER block when a ledger line ships.**
Fence F4 (row 105, coordinator pack) governs the split: the worker instance never prices its own
promotion.

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 23 / 24 | *(shared with WORKER / COORD — premise-cost reading; CONVOLUTED = demotion candidate.)* | **ABSOLUTE** | — |
| 105 / 126 | *(shared with COORD — fence F4; the prior-art pass at atom creation.)* | **ABSOLUTE** | — |
| 127 | Sweep Result-Index rows for antecedents the premise pass would not catch. | **ABSOLUTE** | The prior art that motivated it was a RESULT antecedent, which is why the premise sweep did not catch it and an outsider did |
| 128 / 129 / 131 | *(shared with WORKER — adoption to study; kinship = convergence; corrections travel.)* | **ABSOLUTE** | — |
| 132 | Itemize every ledger line to equal depth on every framework — a half-itemized ledger is a VOID measurement, not a partial one. | **ABSOLUTE** | Two frontier classes audited the programme line-by-line against a one-phrase compression of its rivals, and both retracted under a single challenge |
| 133 | Decompose each line until the frameworks demonstrably pay the same price by the same mechanism, or diverge — never stop at "both need X". | **ABSOLUTE** | The founding tensor-product line: three different debts under one symbol |
| 134 | Label every line AUDITED or SURVEYED, and carry the labels with every quotation of the audit. | **ABSOLUTE** | A prefix handing every future worker a surveyed ledger presented as audited would propagate the exact failure the role exists to stop |
| 135 | Book our own IOUs at ESTIMATED cost, never zero. | **ABSOLUTE** | "The rival's bill is paid and framed on the wall; ours hasn't been invoiced yet" |
| 136 | Build the ledger on DEBT STRUCTURE (named, payable, being worked) — never on posit count. | **ABSOLUTE** | A count-based ledger hands a reviewer the counterexample |
| 137 | Price any standard invoked as arbiter against EVERY party in that line, and state the asymmetry if you apply it anyway. | **ABSOLUTE** | A naturalness standard invoked while the incumbent violates the same standard |
| 138 | Submit every philosopher conclusion — for or against the programme — to a programme-formed contra-reviewer before it lands, and log the exchange. | **ABSOLUTE** | Format rules cannot catch generation bias: three consecutive incumbent-side symmetric charges were supplied by the human coordinator, not the role |
| 139 | Read the philosopher's log, the comparative ledger and FORMATION_CORE before every run, and write failures AND successes to the log in the same pass. | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |
| 140 | Count bit-sized structural inputs for every framework in the reference class on the same basis, or make no comparison. | **ABSOLUTE** | An itemizing challenger measured against un-itemized incumbents looks more expensive than it is — the disguise sin pointed inward |
| 141 | **NEVER quote the programme's bit-inclusive input count against a rival's continuous-parameter count**; until the per-framework bit column is filled, say that any cross-framework input comparison is unsupported. <sub>also in: PAPER</sub> | **ABSOLUTE** | Same |
| 142 | Exercise no philosopher power beyond the ledger section's content: no tiering, banking, ruling, canon edits, or claim-wording changes; and say plainly where a framework is empirically behind rather than compensating. | **ABSOLUTE** | The founding audit's outcome is on record as PARTIALLY SUPPORTED, NOT CONFIRMED — quoting it as a win is a misquotation |

## 7. THE ARCHIVIST

**Takes the BANK block.**

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 48 / 165 / 170 / 176 / 197 | *(shared — see the worker pack.)* | — | — |
| 50 | Fill a register cell with UNKNOWN rather than a guess. <sub>also in: COORD</sub> | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |
| 68 | Name every ledger in `knowledge/ledgers/` in FORMATION_CORE §5. | **ABSOLUTE** | One founding ledger was missed for a whole sweep round |
| 76 | Keep the worklist meaning-notes region VERBATIM — never compress it or let it be summarized. | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |
| 77 | Never delete an archive or a superseded record; archive by moving, and preserve the trail verbatim. | **ABSOLUTE** | Two founding caveats were silently compressed away and had to be excavated |
| 177 | Never carry a recorded number forward — count it or `git log` it. <sub>also in: BANK</sub> | **DEFEASIBLE** — the C-24 carve-out: a number stamped `uncounted — from <commit>` is honest. | The stale-sync note that misled a planning instance |
| 179 | Exercise no archivist power beyond structural hygiene: never touch tier tags or claim wording, never delete, never renumber, never "improve" prose, and flag rather than move anything ambiguous or citation-breaking. | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |
| 180 | Execute only a pre-approved manifest in an archivist pass; produce the complete proposed move/edit list first. | **DEFEASIBLE** — **break when:** the role file's own carve-out: a code-convention fix that changes no output may be done in-pass. | **NO RECORDED INCIDENT** — reads as decree |
| 181 | Write an `INDEX.md` in every probe directory, one line per file with status and what cites it. | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |

## 8. THE APPARATUS AUDITOR (N1)

**One rule of its own** — the role's operating text is `removal_auditor_agent.md`, which carries
both halves (prevents/costs + spirit-served).

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 121 | Close out every review round with its edit→reaction rows — a round without them is incomplete. <sub>also in: LOOP</sub> | **ABSOLUTE** | The founding programme was relying on the human coordinator's memory for which edit caused which reaction |

## 9. THE EXTERNAL-LOOP OPERATOR

**The coordinator wears this pack when the outer cycle runs**; the routine is
`external_review_loop.md`. Fence F1 (row 102) is the one this role is structurally most likely
to breach.

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 67 | Keep the cold-review prompt in the routine byte-identical to the sampler's payload. | **ABSOLUTE** | Preventive: a drift would void every sample silently while the logged request body looked well-formed |
| 102 / 106 / 107 | *(shared with COORD — F1; F5; M1.)* | **ABSOLUTE** | — |
| 103 | Hold the sending surface fixed for a loop's duration (fence F2). | **ABSOLUTE** | A subscription-surface baseline and an API sample are not comparable |
| 104 | Sample N ≥ 3 fresh isolated instances OF ONE CLASS, never mixed classes, never the held-out class (fence F3). | **ABSOLUTE** | With N = 1 a changed classification cannot be distinguished from sampling noise |
| 109 | Send the reviewer prompt verbatim and minimal, and log the full request body per review as the isolation proof; any extra content voids that sample. | **ABSOLUTE** | Any coaching in the prompt invalidates the measurement |
| 110 | Review tagged releases only; never review a working tree. | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |
| 111 | Classify a review (reference class, crank-classification + trigger, costly signals, engine engagement, findings count and depth) BEFORE reading it for content. | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |
| 112 | Treat comprehension rising while substantive findings fall as a LOOP FAILURE and revert the round's edits (the divergence tripwire). | **ABSOLUTE** | A founding draft would have moved the metric while changing nothing about what the framework predicts; a cross-class meta-observer caught it as REFERENT-DRIFT before it shipped |
| 113 | Never answer a substantive finding with a presentational fix — keep Branch 1 and Branch 2 separate. | **ABSOLUTE** | Precisely the sanding failure the tripwire exists to catch |
| 115 | Record the STALL POINT and treat the prescription itself as noise. | **ABSOLUTE** | One round says explain more at the beginning, the next says the beginning is overloaded — a ratchet, not disagreement |
| 116 | Act on a presentational misread only at ≥2 instances; repair in place at equal or shorter length; expand the paper never, the repo freely; never evict load-bearing content to the repo. | **DEFEASIBLE** — **break when:** a single instance that is a factual DEFECT — a broken first check on the entry path — is fixed at N=1; the ≥2 floor governs MISREADS, not defects. | Same ratchet measurement |
| 117 | Report a round's dissolution rate and its yield as TWO numbers — a finding's value is not its survival rate. | **ABSOLUTE** | Both round-1 external findings partly dissolved and both produced real results |
| 118 | Exclude unknown-provenance reviews from N, and never read N agent reviews as N independent opinions. | **ABSOLUTE** | A third-party review was called "the only draw from a different population" before checking |
| 120 | Adjudicate an external review through §8a; never adopt it. | **ABSOLUTE** | The checker did better than the reviewer on the reviewer's own ground |
| 121 | *(shared with N1 — the edit→reaction close-out.)* | **ABSOLUTE** | — |
| 122 | Ship no pre-emption intervention that would still help a paper that was wrong (R10); R9's three forms are void without it. <sub>also in: PAPER</sub> | **ABSOLUTE** | Ruled together explicitly: "R9 without R10 is a manipulation manual" |
| 123 | Translate pre-emption into fact-register (a highlighted, checkable fact), never transplant it from answer-register. <sub>also in: PAPER</sub> | **ABSOLUTE** | The register discriminator: the same answers work in the prompts following reviews and fail inside the paper |

---

# THE ACTIVITY BLOCKS

## B. BANKING PASS — whoever runs `bank.sh`

**Taken by whoever runs the bank — worker, archivist, coordinator alike.** The gate can stop you
on very few of these; the rest are the four banking-stoppers no gate can see
(**RULES_CORE.md § THE FOUR BANKING-STOPPERS** — the term is reserved for those four; everything
else that blocks a bank is a *blocking defect with an owner*).

**★ RAISING a tier has a pass of its own — `manuals/banking.md` § THE TIER-RAISE PASS.** An
**UNDER-CLAIM** verdict lands there and nowhere else. Its gate is absolute: **the raise is not
admissible on argument** — it carries an engine check with a demonstrated disagreement mode, or
it does not happen.

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 34 | Add a **DISCRIMINATING** check to the matching harness for every banked fact — **or record why none exists** — and confirm the PRINTED total moved. *(A check must be able to fail for a reason that matters; a useless check is a false signal of verification — RUL-067.)* | **DEFEASIBLE** — **break when:** no NON-VACUOUS check exists for the fact (a negative, a framing statement, an ontology ruling): ship no check and record why. | Two founding phantom "suite +N" variants: dead code after `sys.exit`, and checks never written at all |
| 35 | Ship every new check with a demonstrated failure mode — run it against the broken state and show it exits non-zero for the named reason. | **ABSOLUTE** | Negative-testing ten new checks found two defects in the new checks themselves |
| 47 | *(shared with WORKER — imports stay excisable.)* | **ABSOLUTE** | — |
| 57 | Keep ONE governing record per probe round; stamp superseded memos superseded-in-part with a pointer; the record, not the memo, is authoritative. | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |
| 63 | Keep load-bearing tree-state prose either GENERATED from the tree or PINNED in `check_records.py` as an executable invariant. | **ABSOLUTE** | A founding refactor conserved its code exactly on three independent axes while its prose drifted at 26 sites in one commit |
| 64 | Promote any NEW prose-drift class caught in review to a check where mechanizable — a drift class caught twice in prose is a process failure. | **ABSOLUTE** | Two founding classes, each caught twice before promotion |
| 66 | Keep reviewer-facing QUOTED harness pass lines EXACT — the drift tolerance does not apply to them. <sub>also in: PAPER</sub> | **ABSOLUTE** | Two founding release-path artifacts quoted counts their trees did not print |
| 69 | Keep every record ID unique — an ID that names two rows names neither. | **ABSOLUTE** | A duplicated registry ID (twice) and a byte-identical duplicated row |
| 70 | *(shared with WORKER — sweep the whole corpus after any relabel.)* | **ABSOLUTE** | — |
| 71 | Sweep in READER order — body first, then front matter, then companion, then engine docstrings, then ledgers. | **DEFEASIBLE** — **break when:** a bookkeeping-only correction has no body site; sweep the surface that exists and state the scope. | A founding round executed four retractions bookkeeping-first; the verification pass found all four still asserted in the body |
| 72 | Cover the full enumerated sweep surface: body, front matter, companion incl. the reverse index, engine docstrings AND returned strings AND machine-read rows, test description strings, every ledger, canon, worklist, handoff, simulator, and the dispatch briefs. | **DEFEASIBLE** — **break when:** a change that introduces no new identity, count or claim (pure typography) does not need the full surface — state the scope swept and why it is complete FOR THIS CHANGE. | A founding round CREATED a collision by striking cites in one section only |
| 74 | Sync the matching paper sections (or the companion annex) in the SAME pass as a paper-worthy engine result — ledger-only is not graduated. | **DEFEASIBLE** — **break when:** the annex route discharges the duty. | A founding result drifted out of its section for a full session before a coverage audit caught it |
| 75 | Record deferred items on the worklist in the same pass — an accepted finding recorded nowhere is a silent drop. | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |
| 158 | Update the Result Index row, the dependency-graph position and its edges whenever a result is banked or its tier changes. | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |
| 159–162 | Bank with the UTF-8-forced wrapper; no backticks in a commit message passed as a shell argument (use `git commit -F`); never edit files while `bank.sh` runs (it verifies the tree AS IT STANDS AT START); verify with `git log` that the commit actually landed. | **ABSOLUTE** | The bank silently failed to commit under a codepage crash; a founding commit swept another session's uncommitted work; the ingest step can die at the end of a run and skip the commit silently |
| 164 / 167 / 175 / 177 | Use the Write tool for backslash content; force-add anything a broad gitignore covers; verify the PRINTED total and resolve numbering before applying independently-computed deltas from parallel tracks; never carry a recorded number forward. | mixed — see WORKER/ARCHIVIST | Five parallel tracks minting the same IDs; five role files found untracked |

## P. PAPER & RELEASE — whoever edits the paper, the front matter or the release path

**Read `paper_rework_lessons.md` in full before any paper edit — non-optional.** Several of these
rules exist nowhere else in the tree.

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 66 / 84 / 122 / 123 / 141 | *(shared — quoted pass lines exact; novelty claims primary-verified; the R10 constraint; fact-register translation; the bit-count comparison ban.)* | **ABSOLUTE** | — |
| 143 | Keep the paper HISTORY-BLIND — no dates, audit or finding IDs, ruling stamps, or earlier-revision narratives in the body; history lives in the companion. | **ABSOLUTE** | *(rationale)* A paper reading as a process log is a crank-class signal; and a retraction narrative does the work a rewrite should do |
| 144 | Retract by replacement, never by deletion — leave a labeled corpse (what was claimed, why it fell, what survives, dated) in the companion. | **ABSOLUTE** | Two founding caveats silently compressed away; restoration cost 10× the original sentence |
| 145 | Cool the headline rather than strengthening the argument; where a section both asserts and retracts, the retraction governs and the assertion is rewritten. | **DEFEASIBLE** — **break when:** the over-claim is repairable IN THE SAME PASS by a check you can actually run: run it and keep the headline. | "Proven" over a premised result; "headline derivation" over a normalization identity |
| 146 | Demonstrate, don't plead: checkable content near the front that EXECUTES AS WRITTEN, your strongest objection first, the correct reference class — and never include instructions aimed at the reviewing system's behaviour. | **ABSOLUTE** | *(rationale)* A first check that errors discredits the other fifteen |
| 147 | Never invite verification of a number two of our own artifacts disagree about — reconcile first. | **ABSOLUTE** | A founding count divergence between two release artifacts |
| 148 | Cite a shape-precedent in the SAME section as the claim, with a specific delta sentence; a bibliography entry is not a defense. | **ABSOLUTE** | Five founding prior-art misses were caught by adversarial re-derivation, none by the tier system |
| 149 | *(shared with WORKER — citations primary-verified.)* | **ABSOLUTE** | — |
| 150 | Follow the abstract formula: reference class → spine short-list with one honest conditional each → already-measured exposures as their own paragraph → the executable-suite offer with its scope; no claim or check counts. | **DEFEASIBLE** — **break when:** a venue with its own abstract requirements overrides the house formula — keep the honest-conditional and the scope clause, which are the formula's spirit. | The founding 45-line abstract's measured defect: maximal breadth and maximal hedging simultaneously |
| 151 | Patch heading and TOC anchors together; renumber every cross-reference and count when an exposure list changes; count premises honestly (rows ≠ premises); label every front-matter quantitative claim with its ruled scale/scheme. | **ABSOLUTE** | The founding which-scale lesson; "seven rows, thirteen-plus premises" |
| 152 | Treat a PDF render as the publishing moment: tree banked and clean, suite green, front-matter commands re-tested, README counts current — and verify with `verify_pdf.py`, because exit 0 is not verification. | **DEFEASIBLE** — **break when:** a private render for your own reading is not a publishing moment: skip the checklist and do not share the artifact. | ~3,500 characters silently becoming blank; a PDF with no glyphs and no links exiting 0 |
| 153 | Work in anchored chunks with die-before-save scripts, commit per chunk, run a verification pass on the swept tree BEFORE banking. | **DEFEASIBLE** — **break when:** a change small enough to verify in one read does not need chunking (means-substitution). | The verification pass found 7 blocking items the sweep missed, twice running |
| 154 | Keep no inline tier tags in the paper body; the companion is authoritative for bookkeeping, and a new result needs both the result-ID marker and the full Index row. | **ABSOLUTE** | Companion tiers out-ranking the body, ×3 |
| 155 | Write the primitive when a paper-only row is load-bearing; a paper-only derivation can be not merely unchecked but VACUOUS. | **ABSOLUTE** | A founding "requirement" that constrained nothing in the formalism it was written in |
| 156 | Relocate, never delete: everything bound for a successor paper also goes to the companion as an annex. | **ABSOLUTE** | Both cold reviewers found that volume falsifies the auditability claim the framework stakes its case on |
| 157 | Do not edit legacy standalone snapshots of the paper. | **ABSOLUTE** | Indexing them serves stale numbers as current |

## X. ANY CHECKING ROLE — reviewer, meta-observer, keeper, philosopher-as-checker

**Taken by every checking role.** ⚠ **RUL-065: internal §8a checking runs CROSS-CLASS, keyed on
who AUTHORED the work. A same-class CLEAR carries no information.**

**★ GUARDS ARE CALIBRATED ON THE TARGET, NEVER AT A ROUND NUMBER (standing instrument note).**
Any non-degeneracy, conditioning, magnitude or exclusion guard imposed on a search whose target
is a MEASURED quantity must first be **evaluated on the measured quantity itself**, with the
target's own value **reported beside the guard**. A guard that would exclude the physical target
is not a guard, it is a pre-registered miss. Where the pathology is real, exclude it by a
**WITNESS**, not by a threshold; where a threshold is unavoidable, set it from the target's own
conditioning and **state the margin**. **SAME FAMILY as C-19** — both are an instrument setting
never measured against what it was supposed to measure; C-19 catches the setting that cannot
fail, this one catches the setting that fails on the answer. The founding measured case,
self-reported by the reviewer against its own work: a round-number non-degeneracy guard would
have excluded the physical target — the data was *more degenerate than the pathology being
guarded against*. <sub>also in: WORKER, whenever the worker imposes a guard on a data-facing
search</sub>

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 19 | Flag every "no other option exists" as a theorem needing proof. <sub>also in: WORKER</sub> | **ABSOLUTE** | Both checkers constructed the same fourth option |
| 203 | **C-33 — verify on the NAMED realization.** A claim about an object with multiple realizations must name which one. Verify it there and nowhere else; a claim with no named realization is **RETURNED, not adjudicated**. <sub>also in: WORKER</sub> | **ABSOLUTE** | Three module-transplant instances in three days |
| 56 | Persist every verdict as a FILE in the round's probe directory, same pass. <sub>also in: COORD</sub> | **ABSOLUTE** | A verdict living only in a transcript is not a governing record |
| 79 | Iterate reviewer↔developer to consensus on the tier and scope of every point; neither side concedes to end the loop; the engine arbitrates fact; at ~3 rounds STOP, escalate, and bank nothing. | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |
| 80 | On a reviewer pushback, lower the CLAIM (tier, scope, wording) — not the RESULT. | **DEFEASIBLE** — **break when:** the attack refutes the COMPUTATION rather than the claim: the result itself falls — lowering the claim instead would preserve a wrong result. | *(single-homed in the founding tree — see AGENT_RULES §0)* |
| 81 | Run the meta-observer ALONGSIDE the reviewer, starved. <sub>also in: COORD</sub> | **ABSOLUTE** | — |
| 86 | Be willing to return CLEAR / COHERENT — a checker that always finds something is noise. | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |
| 207 | **Report an UNSTATED-FORK.** The work took a route; a real alternative existed; the record does not say it was considered, or says so without a reason. Name it, grade its tractability, give its promotion condition, and add the fork to `PATHS_LEDGER.md`. Do NOT manufacture forks — a route you cannot grade and cannot give a condition is not a finding. <sub>also in: WORKER (rule 206)</sub> | **DEFEASIBLE** — **break when:** the author already recorded the fork with reasons: verify it rather than duplicating it, and say you checked · **record the break where the verdict lands.** | Added 2026-08-27 with the paths ledger. It is the structural sibling of **UNDER-CLAIM** — both are the corpus asserting less than it should — and the reviewer is placed to see it *because it is not the author*: an unconsidered alternative is invisible to the instance that did not consider it |
| 205 | **Reach nothing outside your DIET — and the check is one command.** Every artifact declares what it IS (`<!-- DIET-CLASS: … -->`; `rag/diet.py` holds the taxonomy and the per-role table). Query as yourself — `python rag/query.py "…" --role <you>` — and **before opening any file directly, run `python rag/diet.py --role <you> <file>`**, because retrieval is bounded and your file-reading tool is not. If you breached the diet anyway, **say so in your verdict**: a contaminated finding reported honestly is recoverable; one reported clean is not. <sub>also in: WORKER, for any dispatch carrying a starvation</sub> | **ABSOLUTE** | Added 2026-08-27 with the retrieval layer, then **immediately re-cut when its first design was measured to fail**: the bound was over PATHS, and the meta-observer's own bound returned `FORMATION_CORE.md` — the one file rule 92 (ABSOLUTE) forbids a checker. A bound that permits an absolute breach is not a bound, so the bound moved onto the artifact's declared class. The failure signature is the one this apparatus most cares about: the resulting verdict **looks identical** (*a separation asserted and never verified is a convention, not a control*) |
| 174 | Search the WHOLE corpus and ask whether the objection is answered anywhere. <sub>also in: WORKER</sub> | **ABSOLUTE** | — |
| 196 | Prefer the primary-record REST APIs (Crossref / INSPIRE / arXiv or the field's equivalent) via `urllib` over WebSearch/WebFetch inside subagents. | **DEFEASIBLE** · *advice* — **break when:** the API holds no record and a web source is the only primary — quote the URL and the retrieval date. | Web tools were unstable inside subagents; the REST route also gives publisher-deposited metadata |

## S. SIMULATOR CAMPAIGN — binding INSIDE a campaign only (dormant until one opens)

**⚠ These rules bind nobody until a simulation campaign is in session. They are recorded, not
retired:** the apparatus auditor's standing finding is that structures whose benefit is invisible
get cut exactly this way. They re-arm the moment a campaign opens.

| # | rule | class · when it may be broken | why it exists |
|---|---|---|---|
| 183 | Draw simulator CONCLUSIONS only from the full-fidelity model of the object; toys are anchors, regressions and machinery validation, never finding-bearers. | **ABSOLUTE** | A founding banked negative was WITHDRAWN as a conclusion under this rule |
| 184 | Declare every channel CALIBRATION or TEST in a commit that PRECEDES the computation; a calibration channel can never be re-reported as a test. | **ABSOLUTE** | Named the founding campaign's cardinal violation |
| 185 | *(shared with KEEPER — never privilege a source of truth by anteriority.)* | **ABSOLUTE** | — |
| 186 | Run map-validation regressions before any calibration or test read; a miss on an unvalidated map indicts the map, and the channel is void, not failed. | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |
| 187 | Pin a dial by declaration (value, provenance band, source cite), never by fit; a computed value supersedes only through a pre-registered supersession clause plus review-to-consensus. | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |
| 188 | Compute all structure, gate all magnitudes. | **ABSOLUTE** | **NO RECORDED INCIDENT** — reads as decree |
| 189 | Keep `knowledge/` read-only for the duration of a simulator campaign except the single coordinator-gated closing pass. | **DEFEASIBLE** — **break when:** a correction to a RULE the campaign executes under (not a finding) may be pulled in immediately and recorded in the campaign log. | **NO RECORDED INCIDENT** — reads as decree |

---

## Appendix — the arithmetic of the founding split

At the founding split (2026-08-19, updated through 2026-08-27): **204 rules placed, none
dropped** — core 33 (plus the §A slots), the rest across nine packs and four blocks; 34 rules in
two destinations, none in three (so the cross-check *a rule in five packs belongs in core* fired
on nothing); **155 ABSOLUTE · 49 DEFEASIBLE** (every defeasible rule names a concrete situation);
**37 rules with no recorded incident**, 16 with a rationale but no dated case, 6 with asserted
repetition — the remaining **145 backed by a dated or named event**. *(These are founding counts.
At instantiation: recount by counting, and expect your own no-incident set to shrink as your
record grows — that is the direction the WHY column is supposed to move.)*
