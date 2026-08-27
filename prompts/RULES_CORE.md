# THE COMMON CORE — the 32 rules every agent holds without looking anything up

**v1, 2026-08-19.** The role-split half of the rules architecture (`knowledge/audit/consolidation_2026-08-18/RULES_ARCHITECTURE_2026-08-19.md`), designed on the human coordinator's directive: *200 rules is too many for one agent to hold; split them into a small common core plus role packs; **the rules should not be enforced, but the SPIRIT of the rules should**.*

> **What this file is.** The rules that bind EVERY role. Everything else lives in `RULES_BY_ROLE.md` — nine role packs and four activity blocks, each stating only what it adds. The complete enumeration, with sources, remains `knowledge/audit/consolidation_2026-08-18/RULE_INVENTORY_2026-08-19.md`; **it is the authority and no rule's content was changed by the split.** Row numbers below are its row numbers.
>
> **The test for being here is UNIVERSALITY, not importance.** A rule is core only if every role could breach it. Importance was explicitly not the test: the phantom-cite rule and the e5 litmus are equally important, and only the first is core, because an archivist can breach the first and cannot breach the second.

## How to read a rule here

Every rule carries a **CLASS** and a **WHY**.

- **ABSOLUTE** — never break. No situation makes breaking it right. If you think you have found one, you have found something to escalate, not something to do.
- **DEFEASIBLE** — a default that is usually right, with a **named situation** where following it is the wrong move. **A break that is recorded with its reason is COMPLIANCE.** A silent break is not.
- **WHY** — the motivating incident, quoted from the inventory. Where the inventory records none, this file says so rather than inventing a rationale: *no recorded incident* is itself a finding about the rule.

**★ THE GENERAL BREAK CLAUSE (RUL-068, 2026-08-20 — enacted; it replaced the 43 per-rule permission proposals as a mechanism).** A DEFEASIBLE rule may be broken when **following it would defeat its own stated purpose**, provided the break is **(a) named in the pass that makes it, (b) justified by the rule's own purpose — never by convenience, time or difficulty, and (c) recorded where that pass's outcome is recorded.** **An unrecorded break is a violation; a recorded, reasoned break is COMPLIANCE.** ABSOLUTE rules have no break clause at all. The per-rule **break-when** situations listed in this file and in `RULES_BY_ROLE.md` are **ILLUSTRATIONS of this clause** — worked examples of a rule's purpose being served by breaking its letter — not separate grants; the clause also binds rules written after it, which an enumerated list cannot. *[RECORDED]* means the tree already states the exception. (The files' earlier bold notice that these were unenacted proposals was itself two rulings stale — struck at R1 of the 2026-08-21 restriction analysis.)

**★ THE APPARATUS AUDITOR — `knowledge/prompts/removal_auditor_agent.md` (the ex-enforcer's spirit-of-the-rules question is its PART B: ADOPTED RUL-066, merged RUL-072).** Callable at the coordinator's request, plus one spot-check per consolidation on a pass drawn content-addressed by the auditor — never by the audited party. It asks whether the SPIRIT was served, not whether the letter was followed. **A recorded, reasoned break is compliance; the thing it hunts is a rule followed to the letter while its spirit was defeated** — a sweep that touched every site and fixed nothing, a tier tag that is technically defensible and misleads, a check that passes and verifies nothing. It does not adjudicate physics; §8a does that.

---

## A. THE FRAME AND THE ONTOLOGY — four facts you never reason past

**C-1.** Use the INSIDE frame only to import empirical data; derive from OUTSIDE the wavefront.

- **DEFEASIBLE** — **break when:** constructing or checking the wavefront-lock dictionary itself is an inside-frame derivation; do it with the frame named in the same sentence and the output tagged a dictionary statement, never a substrate derivation · **record the break and its reason where the work lands.**
- **WHY:** N49: a "hard constraint" (C9) was built, reviewed HOLDS twice and banked on an inside-frame observed rate bounding an outside-frame kernel property; only human questioning caught it; full rollback by git revert
- <sub>inventory row 1 · binds all · enforcement: prose-only</sub>

**C-2.** Never collapse a grain-layer fact into a cell-layer fact or the reverse — **except through a stated map, named as such.**

- **ABSOLUTE**
- **WHY:** *(rationale, no dated case)* Canon calls it "a recurring source of error"
- **SCOPE CLAUSE added 2026-08-21** (R8 of the restriction analysis; adopt-all): RUL-058 makes the **grain→cell map a Core commitment** and *"a real physical relation, plausibly wave-driven, not a bookkeeping device"* — so the unqualified wording read as forbidding the Core's own object. Crossing the layers is permitted **only** through a map that is named as a map at the crossing; an unnamed crossing is the original error and is what this rule still forbids absolutely.
- <sub>inventory row 4 · binds all · enforcement: prose-only</sub>

**C-3.** Assign quarks NO individual mass; fit and verify only against hadron masses; never quote a standalone quark mass; the top is not a verifier.

- **ABSOLUTE**
- **WHY:** W-LIVE-MASS-AUDIT 2026-06-29: snapping disguised as derivation; the V1 30-hadron-fit script was kept out of the repo
- <sub>inventory row 6 · binds all · enforcement: partial — `twt.py` L4968 MASS ONTOLOGY block, `PDG_QUARK_MASSES` witness-only, `baryon_mass_shared_rotor_nonadditive`</sub>

**C-4.** Derive charge from the topological winding, never from `Q = T3 + Y/2`; GMN's `c = 1/2` is a consistency check, never an input.

- **ABSOLUTE**
- **WHY:** *(rationale, no dated case)* The cleanest circularity available to this program; charge quantization is the one end-to-end-derived spine result
- <sub>inventory row 8 · binds all · enforcement: prose-only</sub>

## B. TIERS AND CLAIM FORM — the honesty spine

**C-5.** Never present an import, fit or guess as DERIVED — the cardinal sin is disguise, not fitting — **and never present a derived result as an import, a fit or a framing.**

- **ABSOLUTE**
- **WHY:** *(asserted repetition, no single dated case)* Recurring; the program's founding failure class
- **MIRROR CLAUSE added 2026-08-21** (R2 of the restriction analysis; adopt-all): this rule named only one of the two labeling errors. The other has its own rule — **C-31** — and its own measured case.
- <sub>inventory row 14 · binds all · enforcement: prose-only</sub>

**C-6.** Tag every claim with exactly one tier from DERIVED-A / DERIVED-P / DERIVED / INPUT / FIT / GATED / FRAMING / CANDIDATE. **The tier may be written as tier + raise-condition** — `FRAMING → DERIVED-A if X` — which is still exactly one tier, with the missing direction encoded (C-31).

- **ABSOLUTE**
- **WHY:** **NO RECORDED INCIDENT** — the inventory's incident cell is empty. This rule currently reads as decree; if you know the incident, record it.
- **RAISE-CONDITION FORM permitted 2026-08-21** (R2 of the restriction analysis; adopt-all). It is a form of the ONE tier, not a second tier: the claim is used at the tier on the left, always. Writing the right-hand side never licenses using the claim at it.
- <sub>inventory row 13 · binds all · enforcement: prose-only</sub>

**C-7.** Label every fit FIT and COUNT it against parameter economy; count every named INPUT.

- **ABSOLUTE**
- **WHY:** **NO RECORDED INCIDENT** — the inventory's incident cell is empty. This rule currently reads as decree; if you know the incident, record it.
- <sub>inventory row 15 · binds all · enforcement: prose-only</sub>

**C-8.** Keep menu and pick distinct: the menu is FRAMING, the pick is the INPUT bit, the consequences are DERIVED.

- **ABSOLUTE**
- **WHY:** Worked example: weak isospin — menu {SD chiral, L-orbit}, pick = 1 INPUT bit, V−A derived-given-it
- <sub>inventory row 20 · binds all · enforcement: prose-only</sub>

**C-9.** Pressure-test every DERIVED tag for substrate-specific vs generic-given-one-coarse-fact, and label the qualifier.

- **ABSOLUTE**
- **WHY:** The Sakharov `Λ²` — real but generic-given-4D, not a dynamical derivation
- <sub>inventory row 10 · binds all · enforcement: prose-only</sub>

**C-10.** Never write "impossible"; record every dead end as tried X → failed because Y → would change if Z.

- **ABSOLUTE**
- **WHY:** N0, the cautionary fake-negative
- <sub>inventory row 17 · binds all · enforcement: prose-only</sub>

**C-11.** Never write "the only way"/"forced"/"guaranteed" without its CONDITIONING CLASS in the same sentence.

- **ABSOLUTE**
- **WHY:** The Sakharov "guarantee" — honest in its fine print, false as a headline (pivot record §4). Ancestor: option (iv), a menu closed by "every involution fails somewhere", refuted independently by both checkers
- <sub>inventory row 18 · binds all · enforcement: prose-only</sub>

**C-31.** A claim recorded **below** the tier its own evidence supports is a labeling error of the same class as one recorded above it. State the tier the evidence supports; where a claim is tagged below DERIVED, carry a **WOULD-RAISE-IF** in the same place its tier is recorded — **what is missing, and what would supply it.**

- **ABSOLUTE**
- **WHY:** 2026-08-19 — the AI coordinator banked a criticism of its own work that the author refuted on delivery; RV-4: *self-directed error is not more accurate for being unflattering.* And C-5 named only one of the two labeling errors. It is the structural twin of C-10, whose escape-hatch design the programme has already cashed twice (N4, N27); it is also the only place an **UNDER-CLAIM** verdict can land — the label alone supplies no destination.
- **WHAT IT DOES NOT DO:** it adds a sentence to a claim. **It moves no tier and banks nothing.** Actually raising a tier is a separate, gated pass — `manuals/banking.md` § THE TIER-RAISE PASS.
- <sub>added 2026-08-21 · R2 of `knowledge/audit/consolidation_2026-08-18/RULES_RESTRICTION_ANALYSIS_2026-08-21.md`, human coordinator "adopt all" · binds all · enforcement: prose-only</sub>

**C-32.** A menu whose alternatives are **all** refuted — **each refutation engine-checked** — no longer contains a pick: the survivor is DERIVED, and the branch node records the refutations.

- **ABSOLUTE**, and the gate is ABSOLUTE with it: **every "no other option exists" closure is a theorem needing proof** (inventory row 19, already in force), and **every refutation in the menu is engine-checked**. A menu closed by argument, by exhaustion of imagination, or by any refutation that cannot be run closes nothing and promotes nothing.
- **WHY:** The negative control is FORMATION_CORE **Ex.5, option (iv)** — a ruling taken on a three-option menu closed by *"every involution fails somewhere"*, refuted independently by **both** checkers, each constructing the same fourth option. Menu closure is the programme's demonstrated weak spot (Ex.5; Ex.7's uncomputed `{J, D}` menu). This rule is the honest promotion direction — the one that lets a real result stop being counted as a pick — and it is gated on the single instrument whose absence produced the failure.
- **COST, STATED:** this is the only core rule that can move something from INPUT to DERIVED. Treat a menu you closed yourself with the suspicion the record says it has earned.
- <sub>added 2026-08-21 · R10 of the restriction analysis, human coordinator "adopt all" · gate = inventory row 19 · binds all · enforcement: prose-only</sub>

**C-33.** Every claim about an object with **multiple realizations** names WHICH realization in the same sentence — the **module and the side** for a representation, chirality, singlet or doublet claim; the **grading** for a chirality claim; the **basis, frame or layer** wherever those vary. Checkers verify the claim **on the named realization**. A claim with no named realization is **returned, not adjudicated**.

- **ABSOLUTE**
- **WHY:** Three instances in three days, all the same shape — a label transplanted across realizations with no bridge: the §4-bis cost-table error, the r3 reviewer's step (b), K2's misclassification. The canon §0 grain/cell and inside/outside layer rules are this same duty at coarser grain; C-33 is its sentence-level form.
- **WHAT IT DOES NOT DO:** it does not decide which realization is right. Naming one is the cost of being adjudicable, not a pick — and where the realization is genuinely open, the sentence names the branch node.
- <sub>added 2026-08-23 · RUL-094 Q6, human coordinator "ADOPT. And maybe generalize?" · binds all · enforcement: prose-only</sub>

**C-34.** In research work, deliberately exploit the agent's comparative strength over the human literature: **cross-domain reach**. Human researchers specialize — one branch of physics, one branch of mathematics — because a lifetime forces it; an agent's training spans essentially all branches at once, so on any blocked problem the levers the literature never tried are the agent's to try: an analogue system from another field, a theorem from an adjacent formalism, an invariant-theory or dynamical-systems or statistical-mechanics route into a problem the home branch attacks head-on. **Briefs to research workers carry this reminder explicitly**, and a worker blocked in the home formalism ranges before digging deeper.

- **DEFEASIBLE** — **break when:** the task is mechanical (a sweep, a count, an enactment) and range would be noise — the rule taxes tunnel vision on research, never focus on execution.
- **WHY:** Human coordinator, 2026-08-27, verbatim: *"the strength of an AI agent compared to the human literature lies in his cross-domain expertise. AI agents' training time is immense compared to the one of humans. Where humans tend to specialize in one branch of physics or one branch of math, AI agents can use a wide range of levers."* The programme's own record is already this shape — the helimagnet/magnon machinery on the substrate, the Arnold-tongue apparatus, the Molien/invariant-theory counts, the Skyrme toolbox — each an import from a branch no single-specialty route would have combined.
- **WHAT IT DOES NOT DO:** it relaxes nothing. A cross-domain import registers like any import (companion §13); prior art is read, not paraphrased (F3); an analogue is a lever, not a derivation — the result still computes on the engine or carries its honest tier.
- <sub>added 2026-08-27 · human coordinator directive, RUL-111 · binds all, researchers specifically · enforcement: prose-only · AGENT_RULES inventory row owed at next consolidation</sub>


**C-12.** Tag every open question PINNABLE / UNPINNABLE / UNKNOWN-KNOWABILITY. Expanding on an unpinnable one is DEPRIORITIZED, not forbidden — a worker who expands anyway must state, in the same pass, the **would-change-if**: what observation or structure would make the question pinnable after all (softened from a ban by the human coordinator, 2026-08-21, RUL-076 — the ban was one of the adverse reviews' named self-issued stop orders).

- **DEFEASIBLE** — **break when:** a dedicated inquiry into whether an item classed UNPINNABLE really is unpinnable — that tests the classification rather than expanding the answer · **record the break and its reason where the work lands.** (The former stamp on this clause is discharged by the same ruling.)
- **★ THE TAGGER OWES THE ESCAPE HATCH TOO (added 2026-08-21, R4 of the restriction analysis; adopt-all).** **Every UNPINNABLE tag carries its would-change-if in the same sentence, exactly as every dead end does** — what observation, structure or built object would make the question pinnable after all. RUL-076 put that duty on the worker who expands anyway; this puts it where the door is actually closed. **A conditional unknowability** — *"unpinnable until the kernel exists"* — **recorded without its re-entry condition is a fake impossibility with a knowability tag on it**, which is canon §4's own discipline defeated by a rule. The measured case: four of five routes closed in one pass, one of them on the ground *"probably too small and too foreign for any realistic probe anyways"*. This clause taxes STOPPING, never claiming — it moves no tier.
- **WHY:** Coordinator, 2026-08-18: "the gap-#1 question taught me that some things cannot be known from inside the frame" — and 2026-08-21: a priority with a named re-entry condition serves that purpose; a flat ban was the cheapest legitimate way to stop working.
- <sub>inventory row 25 · binds all · enforcement: prose-only</sub>

**C-13.** Never harden #1-gap-routed content past CANDIDATE — **and every #1-gap routing names WHICH §D.5 object the answer needs, and WHAT about it.**

- **ABSOLUTE**
- **WHY:** **NO RECORDED INCIDENT** — the inventory's incident cell is empty. This rule currently reads as decree; if you know the incident, record it.
- **★ THE ROUTING MUST NAME ITS OBJECT (added 2026-08-21, R4 of the restriction analysis; adopt-all).** *"It routes through the gap"* is an **unlocated** gap wearing a located gap's tag. Name the §D.5 object (the driven-dissipative EOM, the `Im χ` form, the memory kernel, Θ_rel, the dictionary crossing) **and what about it** the answer needs — a value, a sign, a form, an existence statement. This is the RUL-030 class-(2) assembly record's whole point: a puzzle piece is only findable by a future assembly if it says which hole it fits. Taxes stopping, not claiming.
- <sub>inventory row 101 · binds all · enforcement: prose-only</sub>

## C. COMMITMENT — what LEVEL is this, and who signed for it

**C-14.** Ask at which LEVEL a commitment sits — Core axiom, endorsement, or V3 pick — before asserting anything is forced.

- **ABSOLUTE**
- **WHY:** The pivot's motivating error: a pick presented as a Core consequence ("V3 took a bullet", 2026-08-17)
- <sub>inventory row 11 · binds all · enforcement: prose-only</sub>

**C-15.** Enter every load-bearing pick in the family tree in the same pass, with menu, why, revert clause and what rides it. **A NON-CORE pick then PROCEEDS on that recorded branch node alone — no sign-off, no wait.** A **CORE-touching** pick wants the coordinator's plain-language sign-off BEFORE the pick; where the work cannot wait, it may proceed **flagged PINNED-presumptive on the recorded branch node, with the sign-off owed and DATED** on the node.

- **ABSOLUTE** — the entry in the tree is what is absolute. The recording is never optional; the waiting is.
- **WHY:** Keeper sweep finding F4, 2026-08-18: a load-bearing pick (V3-11) carrying no stamp at all — **which is exactly what a blocking rule produces: the pick gets made anyway and does not get recorded.**
- **★ PINNED-PRESUMPTIVE IS A STATED CLASS (added 2026-08-21, R12 of the restriction analysis; adopt-all).** The tree already contains it — **V3-11 stands PINNED-presumptive, non-Core, proceeding on its node** — and the coordinator may re-stamp it at any time. A flagged provisional pick is strictly better than the measured outcome, which was a silent one. Both halves are stated here at equal volume on purpose: a worker meets the sign-off clause first and reads it as a stop where none was owed.
- <sub>inventory row 52 · binds all · enforcement: partial — check_records §10 (node-ID contiguity only)</sub>

## D. VERIFICATION — the engine and the question behind every check

**C-16.** Verify every algebraic claim on the engine before banking; on any conflict the engine wins.

- **ABSOLUTE**
- **WHY:** **NO RECORDED INCIDENT** — the inventory's incident cell is empty. This rule currently reads as decree; if you know the incident, record it.
- **★ AND IT EXTENDS INTO THE CHECK BLOCK — A REFUTING VERDICT MUST COMPUTE (added 2026-08-21, R5 of the restriction analysis; adopt-all).** **A checker returning REFUTED / COLLISION / OVER-CLAIM on a claim that is ENGINE-REACHABLE carries an engine counter-computation. A refutation resting on argument alone is labeled ARGUED, not COMPUTED, and arbitration weights it accordingly.** Four recorded checker mistakes, and all four were arguments a computation dissolved: the 2026-08-21 keeper cure (refuted by the developer's engine-checked pushback — the Γ channel is traceless bond-by-bond); the 2026-08-21 meta-observer's *"obvious candidate"* (obviousness is not evidence); the 2026-08-13 external R-016 finding (*"you don't need the kernel to test it"* — the test cannot be run); the 2026-08-12 "tautology" (settled by the lead's pointwise engine check). **This makes CHECKING dearer and nothing cheaper.** It composes with RUL-075's steelman duty on the worker: the consensus loop is now symmetric in what each side must bring.
- <sub>inventory row 32 · binds all · enforcement: bank.sh [1/4] (both harnesses must pass); the ARGUED/COMPUTED label is prose-only</sub>

**C-17.** Never write "engine-verified"/"engine-exact" for a primitive not yet in the engine with the claimed asserts.

- **ABSOLUTE**
- **WHY:** A phantom cite passed 280/280; caught only by a coherence audit, 2026-06-29
- <sub>inventory row 33 · binds all · enforcement: prose-only — banking-stopper</sub>

**C-18.** Read a primitive's full docstring, or a registered import's full row, BEFORE using it in a new construction.

- **ABSOLUTE**
- **WHY:** The 8b probe used banked boost machinery whose docstring warned verbatim against the exact conflation used; cost two probes
- <sub>inventory row 38 · binds all · enforcement: prose-only</sub>

**C-19.** Before asserting agreement, ask what could have DISAGREED — a tight tolerance on a vacuous check is a tell, not rigour.

- **DEFEASIBLE** — **break when:** a deliberate regression PIN (a byte-identity or count guard) is knowingly vacuous as physics; ship it labeled as a pin, saying plainly that nothing physical could have disagreed · **record the break and its reason where the work lands.**
- **WHY:** `0.00e+00` from MV pruning; "E₂/E₄ = 1.000000" where c₄* is defined as that ratio; a literal 2X/X check
- <sub>inventory row 36 · binds all · enforcement: prose-only</sub>

**C-20.** Pre-register expectations, in a dated record, before ANY measurement or stake-carrying audit — not only ledger runs — and report the outcome against them either way.

- **ABSOLUTE**
- **WHY:** 8b's Derrick-point prediction failed cleanly and was worth more than a confirmation; the founding audit refuted its own author because the expectation was written first
- <sub>inventory row 59 · binds all · enforcement: prose-only</sub>

## E. THE RECORD — what makes a result exist

**C-21.** Write or update the companion §13 row for any load-bearing external import IN THE SAME banking pass (premises, level, ontology status, retirement handle); pure mathematics is exempt.

- **ABSOLUTE**
- **WHY:** The R-145-session import audit
- <sub>inventory row 46 · binds all · enforcement: prose-only — banking-stopper</sub>

**C-22.** Quote a restated banked or credited value's provenance FROM the governing record; a checker's re-derivation is evidence about the value, never about its provenance.

- **ABSOLUTE**
- **WHY:** The ψ-repair meta-observer silently replaced the credited δ_D's hadron-route provenance with a quark-mass scheme point and the lead propagated it; only the human coordinator caught it
- <sub>inventory row 60 · binds all · enforcement: prose-only</sub>

**C-23.** Never characterize a section, paper or result from a summary of it — including your own checkers' summaries. Open the source.

- **DEFEASIBLE** — **break when:** a TRIAGE pass that only decides which sources to open may work from index lines — provided nothing is characterized in a governing record on that basis · **record the break and its reason where the work lands.**
- **WHY:** Three instances in one round, two about citations, one in a banked governing document
- <sub>inventory row 61 · binds all · enforcement: prose-only</sub>

**C-24.** Refresh every count by COUNTING (a suite run, an AST count, `ls`), never by incrementing.

- **DEFEASIBLE** — **break when:** when the tree cannot be counted at that moment (mid-surgery, a red suite), write the number stamped `uncounted — from the run at <commit>`; never as a current count · **record the break and its reason where the work lands.**
- **WHY:** The "mirror sync owed at 45b1337" note misled a planning instance; stacked session blocks made history read as state
- <sub>inventory row 65 · binds all · enforcement: partial — census tolerance ±5</sub>

**C-25.** Graduate every finding into a file in the same session — a finding not written to a file did not happen.

- **ABSOLUTE**
- **WHY:** **NO RECORDED INCIDENT** — the inventory's incident cell is empty. This rule currently reads as decree; if you know the incident, record it.
- <sub>inventory row 73 · binds all · enforcement: prose-only</sub>

## F. BEFORE YOU BANK

**C-26.** Bank no load-bearing claim on the developer's say-so — dispatch the adversarial reviewer first.

- **DEFEASIBLE** — **break when:** a bank carrying NO claim — an archivist hygiene pass, a count refresh, a revert of an already-refuted result — proceeds without §8a; name which carve-out applies · **record the break and its reason where the work lands.**
- **WHY:** The ledger's "separate MC + Reviewer + Coordinator" precedent
- <sub>inventory row 78 · binds all · enforcement: prose-only</sub>

**C-27.** Name which canon §1 move a reviewer-proposed cure would import, answer it, and record the check WITH the adoption — a correct diagnosis does not license its cure.

- **ABSOLUTE**
- **WHY:** *(asserted repetition, no single dated case)* Measured across the coordinator's iteration history: corrections that were simply wrong, from pattern-matching, incomplete reading, and implicit SM-retreat. The only rule in the set whose absence can put a §1 violation INTO the corpus
- <sub>inventory row 114 · binds all · enforcement: prose-only</sub>

**C-28.** Refuse to bank on a red suite or a failed record-invariants gate.

- **ABSOLUTE**
- **WHY:** **NO RECORDED INCIDENT** — the inventory's incident cell is empty. This rule currently reads as decree; if you know the incident, record it.
- <sub>inventory row 163 · binds all · enforcement: bank.sh [1/4], [2/4]</sub>

### ★ THE FOUR BANKING-STOPPERS — and the term is reserved for them

*(Added 2026-08-21, R7(c)+(d) of the restriction analysis; adopt-all. The measured class is `METHODOLOGY_KEEPER_VERDICT` S-4 — a blocking clause with "no canon standing and no owner", recorded and then repeated twice.)*

**These four, and only these four, are BANKING-STOPPERS. None of them is a gate any script can see; they run on you.**

1. **PHANTOM CITE** — "engine-verified"/"engine-exact" written for a primitive not yet in the source *and* the suite (**C-17**).
2. **UNREGISTERED IMPORT** — a load-bearing external theorem used without its companion §13 row in the same pass; pure mathematics is exempt (**C-21**).
3. **UNREGISTERED RULING** — a ruling recorded without its `TWT_RULING_REGISTER.md` row (ruling, ground, dependents, revert list) in the same pass. **THIS BINDS EVERY AGENT, not the coordinator alone.** It was written into the coordinator pack only (inventory row 49) while canon §2 binds all — it is stated here so the agents it binds actually read it.
4. **SILENT LOAD-BEARING PICK** — a load-bearing pick made without its family-tree branch node (**C-15**). *(Note what this does and does not stop: the missing NODE is the stopper. A non-Core pick proceeding on a recorded node, or a Core-touching pick proceeding flagged PINNED-presumptive with the sign-off dated and owed, is compliant — see C-15.)*

**Everything else that blocks a bank is a BLOCKING DEFECT WITH AN OWNER, not a banking-stopper.** Say which it is, and name the owner. The distinction is load-bearing: a stopper is a standing prohibition every agent carries without lookup, and inflating the term into every local blocking clause is what produced a clause declaring the current tree formally unbankable — which restrained nobody, because it was simply untrue.

## G. HOW YOU START, HOW YOU WRITE

**C-29.** Follow the bootstrap order: canon → SESSION_HANDOFF → strategic map + negatives ledger → RAG for specifics → engine verification → bank.

- **DEFEASIBLE** — **break when:** a narrowly scoped DISPATCHED sub-task works from the coordinator's curated brief instead of the full chain — and says so, so the substitution is visible (this pass is an instance) · **record the break and its reason where the work lands.**
- **WHY:** *(rationale, no dated case)* The fresh-window failure the canon exists for
- <sub>inventory row 169 · binds all · enforcement: prose-only</sub>

**C-30.** Prefer plain words over learned ones wherever meaning survives.

- **ABSOLUTE**
- **WHY:** Coordinator: "I was handicapped by jargon during this work and I don't want to impose this on others"
- <sub>inventory row 54 · binds all · enforcement: prose-only</sub>

---

## The one number to carry

**About 174 of the 204 rules have no mechanical enforcement, and every one of the four banking-stoppers is in that set.** *(The inventory's §E headline says 169; a recount off its own table gives 15 fully enforced · 15 partial · 170 prose-only, and the four rules added since — C-31, C-32 (2026-08-21), C-33 (2026-08-23) and C-34 (2026-08-27) — are all prose-only, giving 15 · 15 · 174 = 204. The discrepancy is bookkeeping and changes nothing: every banking-stopper is prose-only under either count. See the architecture report §6.)* The suites verify the mathematics. Almost nothing verifies that you followed the method. **The method runs on you** — which is why the classification above matters: an absolute rule you break silently is invisible, and a defeasible rule you break in the open costs nothing.

## Where to go next

| you are | read |
|---|---|
| about to derive, probe, or compute | `RULES_BY_ROLE.md` § WORKER |
| about to run `bank.sh` | `RULES_BY_ROLE.md` § BANKING PASS |
| about to edit the paper | `RULES_BY_ROLE.md` § PAPER & RELEASE **and** `paper_rework_lessons.md` in full |
| checking someone's work | `RULES_BY_ROLE.md` § ANY CHECKING ROLE + your own pack |
| dispatching | `RULES_BY_ROLE.md` § THE AI COORDINATOR + `coordinator_agent.md` |
| unsure which of two documents to believe | `AGENT_RULES.md` §0 — the twelve-entry divergence table (D-1 since resolved), kept there deliberately |

