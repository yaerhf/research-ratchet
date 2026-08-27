<!-- DIET-CLASS: LEDGER -->
# THE APPARATUS'S OWN DOCKET

*research-ratchet is itself a programme, and it had no docket — which is the defect its own
archivist rules exist to catch. This is that docket: the work owed on the **apparatus**, not on
any object it is given. Instantiated programmes keep their own
`knowledge/ledgers/worklist.md`; this one governs the toolkit.*

**Live state and the standing fences: [`HANDOFF.md`](HANDOFF.md) — read it first.**

**Grades are the tractability scale** (`manuals/paths.md` §2): **A** computation remaining ·
**B** mechanism asserted, construction needed · **C** needs a new idea · **D** blocked on a
named object elsewhere.

---

## W1 · THE EFFICIENCY AUDIT — duplicate activity across roles, and the cost per pass
**Grade B · FIRST PASS RUN and its recommended build EXECUTED 2026-08-27 · the unmeasured items below still stand**

> *"Research for duplicate activity in the different roles. And other ways to reduce process
> time and token consumption."*

**★ THE FENCE THAT MUST GOVERN THIS ITEM, or it will do damage.** The apparatus is built on
**deliberate redundancy**: four diets read one claim precisely so that each sees what the
others structurally cannot, and *the merge destroys a measurement, not merely tidiness*. An
efficiency pass that cannot tell **duplicate WORK** (waste) from **deliberate REDUNDANCY**
(the instrument) will strip exactly the structures that make the apparatus work — and it will
look like a win while doing it. So every candidate saving is classified first:

| class | example | verdict |
|---|---|---|
| **WASTE** | the same paragraph pasted into nine role files | remove or centralize |
| **REDUNDANCY** | reviewer and re-derivation agent both reaching the same result by different routes | **KEEP** — that convergence *is* the measurement |
| **RITUAL** | full ceremony paid on a dispatch that cannot bank | already fixed by the light path; look for more |

**Prior work to read before starting — do not re-derive it.** The light path (`coordinator_agent.md`,
dispatch tiers); the manuals scheme (`manuals/INDEX.md` — start knowing NAMES, read CONTENT on
demand); the formation-prefix cache (`gen_worker_agent.py`); query-instead-of-bulk-load
(`RULES_BY_ROLE` #171); the register-clerk pilot (a cheap class holding registers so expensive
classes ask instead of read); and the apparatus auditor's **Q2 — what does each structure cost
per pass**, which is the existing instrument for exactly this question and should probably
*run* this item rather than a new role being invented for it (role-count governance: adding a
role needs the human coordinator's approval).

**The measured baseline to beat.** A probe-scale dispatch was measured paying roughly
**20,000 tokens of fixed canon-plus-prefix overhead to do ~600 tokens of work.** That ratio,
re-measured, is this item's success criterion.

**One instance already found (2026-08-27), so the item starts with evidence rather than a
hunch.** Across the nine role files, **7% of substantive lines are duplicated** — 25 distinct
lines appearing in two or more files, 73 line-instances in total. The three largest blocks
appear **verbatim in three files each**: cross-class independence, cross-domain reach, and
self-persistence. They were written that way deliberately (a role file should be complete for
its role, as the manuals scheme argues), **but the apparatus's own hazard note says a document
duplicating a rule creates a DRIFT PAIR, and drift pairs are how this corpus breaks.** So the
question is live, not settled: quote-with-pointer, or own outright — never paraphrase.

**Where else to look, in the order a first pass should take them:**
1. **Per-dispatch fixed cost** — what every brief carries whether or not the task needs it.
2. **Re-reads across a session** — the same file opened by several roles in one arc; the
   register clerk exists for this and is still a PILOT with no measurement.
3. **Verdict routing** — RUL-079 already made the consensus loop run direct, worker↔reviewer,
   because routing rounds through the coordinator burned the coordinator's context. Is any
   channel still routed that need not be?
4. **The rules surface** — 204 rules split into packs precisely so no agent holds all of them.
   Measure what a role actually loads versus what it needs.
5. **Retrieval adoption** — the layer exists and the founding measurement was that it sat
   *available and unused*. Is it being used now, and what does a query cost against a read?

**Deliverable:** a table of candidate savings, each classified WASTE / REDUNDANCY / RITUAL,
each with its measured cost per pass and what breaks if it goes. **Report, do not cut** — the
deletion decision is the human coordinator's, and N1's founding finding stands: *a cut that
evaluates structures on recorded catches will remove exactly the invisible-benefit class and
nothing else.*

### FIRST PASS — measured 2026-08-27 · REPORT ONLY, nothing cut

**What each instance loads, in approximate tokens** (chars/4):

| document | tokens | who loads it |
|---|---|---|
| `RULES_BY_ROLE.md` | **15,571** | every role — **and nobody needs more than one pack of it** |
| `FORMATION_CORE.md` | 7,668 | workers only |
| `coordinator_agent.md` | 7,719 | the coordinator, every session |
| `RULES_CORE.md` | 6,527 | every agent, correctly — it is the universal core |
| `removal_auditor_agent.md` | 6,115 | once per consolidation |
| a checker's own role file | 1,400–4,200 | that role |

**★ FINDING 1 — WASTE, and it is the largest single item by a wide margin.**
`RULES_BY_ROLE.md` is **15.5k tokens** and is read whole by every dispatch that needs a pack —
because a file path handed to an agent gets read as a file. A role's actual pack is **2–3k**.
So roughly **12k tokens per dispatch** are spent delivering rules that bind somebody else.
Against the recorded baseline of ~20k fixed overhead per probe-scale dispatch, **this one item
is over half of it.**
*The fix is not deletion — it is GENERATION*: emit a per-role pack (core + that role's rules +
its activity blocks) the way `gen_worker_agent.py` already emits the cached worker prefix.
**What breaks if done badly:** a generated pack that drifts from its source is a drift pair with
a build step in front of it. Mitigations already in the apparatus: regenerate at consolidation,
and add a records-gate invariant that each generated pack matches its source.

**★ FINDING 2 — RECLASSIFIED, and this corrects the framing of this item as it was written.**
The ~5.7k tokens of blocks duplicated across role files — retrieval (9 files), refuting-verdict
(3), cross-class independence (3), self-persistence (3), cross-domain reach (4) — **cost nothing
per dispatch.** Each role loads only its own file, so a block appearing in nine files is
delivered once. **The duplication is a MAINTENANCE and DRIFT cost, not a token cost**, and W1's
opening framing implied otherwise.
The maintenance cost is real and was measured *in the act of creating it*: adding the retrieval
block this week meant editing nine files, and a later correction to the diet bound meant editing
them again. **The drift risk is the serious half** — nine copies of a rule is nine chances for
one to fall behind, which is the corpus's named failure mode.
**Do NOT centralize behind a pointer.** Each copy is load-bearing *at the point of use*: a role
that has to follow a pointer to learn its own diet bound is a role that will sometimes not
follow it, and the manuals principle is explicit that a document must be COMPLETE for its
activity. **The correct fix is the same as Finding 1: one source, generated into place.**

**★ FINDING 3 — REDUNDANCY. Do not touch, and the audit should say so in writing.**
Four diets reading one claim; the re-derivation agent proving independently what the reviewer
checked; the keeper re-examining what per-claim review already passed. These *look* like
duplicate activity and are the opposite: **the convergence of two independent routes is the
measurement.** The founding record shows what it buys — the same result produced by the worker
numerically, derived analytically by a referee briefed to break it, and reproduced from the bare
statement by an agent that had seen none of it, which returned two upgrades nobody had.

**★ FINDING 4 — RITUAL: already addressed, worth re-measuring rather than re-solving.**
The light path exists (`coordinator_agent.md`, dispatch tiers) and prescribes loading
`RULES_CORE.md` + the role pack instead of the full prefix. **It is unmeasured.** Whether
dispatches actually mark a tier, and whether the light path is used at all, is exactly the kind
of "available and unused" outcome the retrieval layer already suffered. A tier field in the
brief is cheap to count once a live programme is running.

**NOT YET MEASURED — needs a live programme, not this repository:**
re-reads across a session (the register clerk's whole justification, still an unmeasured PILOT);
verdict-routing volume; retrieval adoption (queries per session vs bulk reads). Each needs
dispatch-side logging that does not exist yet, and inventing it here would be guessing.

**RECOMMENDATION — one build, two guards.** Generate per-role packs; keep every block inline
where it is used; gate the generated artifacts against their sources.

### ENACTED 2026-08-27 (human coordinator: *"that's a huge waste… execute your plan"*)

`scripts/gen_role_packs.py` emits **twelve self-contained packs** to `prompts/packs/` — the
organigramme, the common core, that role's own rules, its activity blocks, and the manuals index
(names and triggers only, so manuals stay lazy-loaded on top). **Measured saving: 7,200–14,500
tokens per dispatch**, against the 22,161 a role used to load as core + the whole role file.
Nothing was removed, no role merged, no redundancy lost — a pack is a VIEW, and
`RULES_CORE.md` + `RULES_BY_ROLE.md` remain the sources and the authority.

**The two guards, because a generated view that drifts is a drift pair with a build step in
front of it:** every pack carries a **fingerprint of the sources it was cut from**, and
`check_records.py` fails the bank on any stale or unfingerprinted pack (three planted-defect
demonstrations; self-test now 24/24). Regenerate at every consolidation and whenever a rule
changes.

**And the auditor's line in every pack leaves its frequency OPEN, by directive** (*"do not write
that the enforcer is occasional — leave a doubt on this point"*). Every role now carries the
organigramme with the apparatus auditor on it, stated as **available, drawing its own sample,
content-addressed, never by the audited party — you will not know in advance whether this pass
is audited.** That is true (the cadence in its own file is a floor, not a ceiling) and it is the
instrument: telling every agent the audit is rare converts a live deterrent into a calculable
risk, when *its value depends on being BELIEVED to be callable, not on being called often.*

---

## W2 · THE TWO MANUALS THAT BIND MOST OFTEN
**Grade A · DISCHARGED 2026-08-27 — both written; `paper_editing.md`, `probing.md`, `releasing.md` remain owed and are lower value**

`checking.md` (reviewer, meta-observer, keeper, re-derivation agent, philosopher-as-checker) and
`dispatching.md` (composing a brief, launching a worker) are the two activities that bind on
almost every pass, and their
rules are currently spread across role files and packs. `paper_editing.md`, `probing.md` and
`releasing.md` stay owed and are lower value. **Watch W1's fence while writing them:** a manual
that paraphrases a rule creates the drift pair the manuals index itself warns about — quote with
a pointer, or own the rule outright.

## W3 · RUN P7, THE PROFILE-DIVERGENCE TEST
**Grade D — blocked on a live programme with real dispatches**

`calibration_probes.md` P7 is specified and has never run. Until it does, the profile axis is an
uncalibrated instrument, and the apparatus requires every checker to be calibrated blind before
its verdicts count. **The apparatus exempted its own disposition axis from its own bar** — that
is the finding to carry until the test is run.

## W4 · ALIGN THE FULLER ORGANIGRAMME
**Grade A · DISCHARGED 2026-08-27**

`APPARATUS_MAP.md` §1 now carries the same spine as the README — external reviewer → human
coordinator → AI coordinator → execution with the inner check beside it → philosopher with the
apparatus watchers beside it → the data bank — at the map's fuller grain (each role's diet, its
fences, its ruling IDs), with bidirectional arrows where traffic genuinely runs both ways.

**The note worth keeping, because the failure recurs:** mermaid ranks by LONGEST PATH, so a
return edge makes its source an ancestor and the renderer hoists it. Both drawings therefore
carry one visible edge per relationship (the return direction stated in the label) plus a single
invisible link for the order no truthful edge could supply — **neither the philosopher nor the
auditor clears a bank, and inventing an edge there to satisfy a layout would draw a gate that
does not exist in the apparatus.**

## W5 · THE OUTREACH PACKAGE
**Grade A · in progress 2026-08-27**

The essay built from the measured incidents, plus a Show HN text. The repo now reads well and
the install promise is true; what is missing is the account of *why the design is shaped this
way*, which is the part that travels.

## W6 · RE-RUN THE INSTALLER AFTER ANY CHANGE TO THE GATES OR INSTALL.md
**Grade A · standing duty · LAST RUN 2026-08-27, after the records-gate rewrite, the `bank.sh`
hardening and the two new INSTALL steps — PASSED**

The 2026-08-27 dry-run found **eight defects** by executing `INSTALL.md` instead of reading it —
including the apparatus shipping with its own records gate red. **An installer never run is a
specification, not an installer.** Instantiate a throwaway programme, bank twice, verify with
`git log`; the whole pass costs minutes.

**Second run, 2026-08-27 — clean, and it bought a demonstration the self-test cannot.** Fresh
clone → tree → retrieval → packs → canon → handoff → 13 ledgers → `init_repo.sh` → **first bank
in ONE run**. Then the new pack-currency gate was tested *in situ*: a rule was appended to
`RULES_CORE.md` without regenerating, and the bank **refused** — naming all twelve stale packs
and the command that fixes them; regenerating cleared it and the next bank landed in one run.
**A planted-defect demonstration proves a check CAN fire; this proved it fires on the real
thing, in the place it has to.**

## W7 · STANDING: CHECK THE FOUNDING TREE FOR APPARATUS DRIFT
**Grade A · standing duty · first pass run 2026-08-27**

> *Human coordinator: "check in the TWT folder (Deepseek folder) if the apparatus has new roles
> or new features in general."*

The apparatus grew inside the TWT programme and that programme is still running, so improvements
can appear there and never reach here. Drift now runs **both ways** — a first pass found this
repository AHEAD in most places — so the check is a comparison, not a pull.

**What to compare each pass:** the role-file roster · the manuals directory · the ledger roster ·
`scripts/` · and the highest `RUL-NNN` on each side (the cheapest single drift detector there is:
one number, and it names the gap).

**First pass, 2026-08-27 — findings:**

- **The occasional enforcer WAS implemented.** Adopted as RUL-066, then merged by RUL-072 into
  the apparatus auditor as **PART B** — one dispatch per consolidation, two questions: *was the
  spirit of the rules served?* and *what does each defensive structure prevent, at what cost?*
  The spot-check lottery survived the merge, content-addressed, with the audited party never
  drawing its own sample. `enforcer_agent.md` is a pointer stub in **both** trees. The
  "occasional" you remembered is the design: **the deterrent is AVAILABILITY, not frequency** —
  policing every pass would double the cost of every pass and turn a programme that runs on
  judgment into one that runs on compliance theatre.
- **No new roles in TWT.** Rosters match; TWT additionally keeps the TWT-specific session files
  the generic edition dropped.
- **This repository is AHEAD** on: `manuals/engine.md`, `manuals/paths.md`, the paths ledger,
  the diet-classification layer, the generic records gate. TWT may want to pull them.
- **★ ONE RULING FLOWS THE OTHER WAY — RUL-112 (2026-08-27), and it binds this repository.**
  TWT ruled research-ratchet dissociated as its own project, and enacted five legs. The one with
  teeth here: **the tag `twt-apparatus-20260827` is a permanent citation anchor** — the TWT paper
  cites the apparatus at that state, and the tag preserves it. **Never delete, move, or rewrite
  it.** It points at `2982c60`, the last TWT-sited commit, the same state `v0-twt-sited` marks.

**Next pass:** re-run the five comparisons; if the RUL numbers match, nothing rules-level has
moved.

### ★ THE ADOPTION LIST — what the founding tree should take from here (2026-08-27)

**Framed as candidates, not as a patch.** The apparatus's own adoption rule binds this transfer
exactly as it binds any other: *an adoption is SUBMITTED TO STUDY — registry row, adversarial
review, an honest imported-and-counted label, coherence tested like any candidate — admitted or
refused on that study, never on origin.* These were developed in a tree with **no object**, so
each carries assumptions that only a live corpus can test. Ordered by risk, not by novelty.

**1 · DIET-BOUNDED RETRIEVAL — a live exposure, not an improvement.** *(`rag/diet.py`, the
`[RETRIEVAL]` brief field, rule 205.)* The founding tree indexes `knowledge/candidates/` —
where the derivations under review and every persisted verdict live — and its `query.py` has no
role bound. So **its meta-observer is one query from the derivation it exists not to have seen,
and its checkers one query from FORMATION_CORE, which rule 92 forbids ABSOLUTELY** — and the
resulting verdict looks identical either way. Adopting this is closing a hole, not adding a
feature. Take the classification and the role table; the founding `query.py` (embeddings, GPU)
is the better retriever and should keep its implementation — only the bound needs porting.

**2 · THE PATHS LEDGER** *(`manuals/paths.md`, the `[ADJACENT]` brief field, the UNSTATED-FORK
verdict, rules 206–207, telemetry signal 5.)* Closes an asymmetry the founding tree has too: a
wrong claim is caught by six instruments; **a path never taken is caught by none.** Highest
value where research is actively running, because forks accrue every session and the ranking
decays silently. Its death trigger — re-rank the fork in the same pass a path dies — is the part
that must come with it; without it the ledger is a graveyard.

**3 · THE THREE MANUALS** — `checking.md`, `engine.md`, `paths.md`. Documentation, low risk,
immediate effect: `checking.md` alone consolidates what is currently spread across five role
files and two packs.

**4 · `bank.sh` LOUD-FAILURE HARDENING.** Lower value there (its engine exists, so the gate
runs), but the pattern holds: a gate that dies inside a command substitution says nothing, and
`set -euo pipefail` makes that the default failure mode.

**NOT for transfer, and why:** the generic records gate + the `check_records_founding.py` split
(the founding gate is **correct for the founding tree** — verified 28/28 there; the split exists
only because an adopter has no corpus to pin); `init_repo.sh`'s preflight and `.gitignore`
(that tree is long initialized); the empty-ledger fix in `gen_negatives_index.py` (its ledger is
populated); `WHY.md` and this worklist (repository-specific).

**FLOWING THE OTHER WAY:** RUL-112 only — recorded above, and already honoured here.

## W8 · THE BENCHMARK — rank apparatus versions against a known-answer problem
**Grade B · opened 2026-08-27 on the human coordinator's directive · design settled, not started**

**The idea.** Run the apparatus at a research target whose answer is **known to the human and
withheld from every instance** — recent enough that the literature has not absorbed it, so
reproduction cannot be recall. Then **rank apparatus versions** by how close they come to the
ideal path and how fast, iterating the apparatus rather than the problem.

**THE BLIND — decided, and one channel was already open.** No instance gets the founding tree
(its formation prefix *states the target result*, so any instance formed there has been handed
the answer) and none gets the recent literature. The generic edition is clean — verified, zero
mentions. **Enforce it with the tooling, not with discipline:** a `WITHHELD` diet class denied to
every research role, so `diet.py --role <you> <file>` refuses before a file is opened and any
breach must be declared.

**NO PART OF THE APPARATUS MAY KNOW THE TARGET IS REACHABLE** — that is the point of the test,
not a detail of it. It follows that the run must look like ordinary research from inside: an
apparatus told it is being benchmarked has been told somebody believes the problem is tractable.

**THE MEASUREMENT: relative, not pass/fail.** Version *n+1* against version *n* on the same
target, scored on distance from the ideal path (short, once known) and on time. Partial outcomes
stay informative, which absolute pass/fail does not.

**★ THE RULE THAT KEEPS IT HONEST — and it needs teeth, because this is a Goodhart setup by
construction.** Roles and prompts **stay general**: no change may be fitted to the target. That
is exactly what the divergence tripwire warns about — *the metric improved because the work got
better, or because the handles came off* — so intention is not enough. Two guards:
1. **Every apparatus change during the benchmark carries a rationale that never mentions the
   target** and would stand for a programme in any field. Auditable afterwards; it is precisely
   the apparatus auditor's spirit question.
2. **A second held-out problem in a different domain.** One benchmark can be overfitted; two
   cannot be as cheaply. **The generality claim needs its own control world** — the kill-test
   argument, pointed at the apparatus instead of at the research.

**THE SCORER'S FENCE — A ROLE SPLIT, NOT A PROMISE** (human coordinator, 2026-08-27). An
earlier version of this item proposed a TEMPORAL fence: freeze the apparatus, then read the key.
That is a convention, not a control — it rests on the architect's internal state, which nobody
can inspect and which cannot be shown to have failed. **Split the roles instead, so the
interface between them is an artifact:**

- **THE SCORER** holds the answer key and the recent literature, and scores runs against the
  ideal path. It writes **no apparatus text**.
- **THE MODIFIER** changes the apparatus and is blind to the key, the literature, and the
  scores. It works only from written instructions.

**Why this is the stronger arrangement, in the coordinator's own words:** *"making sure that you
give general modification instructions to the apparatus-modifying instance is already easier
than making sure that you modify the apparatus neutrally yourself."* The instruction is a
document. A document can be read by a third party and asked one question — **would this
instruction make sense for a programme in any field?** — which is exactly the apparatus
auditor's spirit question, and it is answerable. "Did you edit neutrally?" is not.

**★ THE OVERFITTING RISK IS REAL BUT CONCENTRATED — and an earlier draft of this item got its
size wrong** (human coordinator, 2026-08-27): *"the number of ways the apparatus can be modified
is huge. The probability that those modifications overfit is very small compared to the
probability that they improve general problem solving. And the stay-general guard amplifies that
exact ratio in the right direction."*

That is correct, and the correction matters for how the experiment is run. Apparatus changes live
at the level of roles, diets, briefs, ledgers and gates: **the abstraction gap between "every
brief carries a kill-test" and any particular target's solution is wide**, and unlike parametric
overfitting there is no channel with the bandwidth to memorise an answer. The stay-general rule
is also **generative rather than merely filtering** — forcing each change through a justification
that must hold for any programme makes general improvements more likely to be *found*, not only
overfitted ones less likely to pass. And the downside is **bounded and detectable**: an overfitted
change fails to transfer to the second problem, and that failure is itself a finding. Expected
value is clearly positive; run the experiment.

**So the guard should be targeted, not diffuse.** The risk is not spread across the modification
space — it concentrates in three places, all of them close to the problem:

1. **SLOT CONTENT.** `[OBJECT-SLOT]`s exist for programme-specific material, so filling one with
   something learned from the target — a control-world zoo, a domain search heuristic, a settled
   list — **is** overfitting: it is the one place the abstraction gap closes to zero. Slots are
   filled by the programme under test, never by the modifier.
2. **NUMBERS WITHOUT A REASON.** *Three referees not two · six rungs · push twice.* These look
   structural and are fitted; a gradient hides comfortably inside a tunable integer. Any number
   a change introduces carries the reason it is that number, or it is not a general change.
3. **SELECTION AMONG EQUALLY-GENERAL CHANGES.** The subtle one, and the real form of the risk:
   every candidate can be general while the *choice* of which to make is fitted, leaving a set of
   individually-defensible rules whose selection encoded the target.

**The mitigations, corrected.** An earlier draft said *score coarsely and late* to blunt the
score-as-gradient channel. **That was the wrong trade** — coarse scoring slows learning
substantially and blocks the selection channel only weakly. Score at whatever granularity is
useful. Block the channel where it actually runs:

- **FILE EACH INSTRUCTION BEFORE ITS SCORE IS SEEN.** Cheap, and it closes the selection channel
  directly: an instruction written before the number cannot have been chosen by it. This is the
  freeze-is-a-solo-commit discipline, applied to the experiment's own instructions.
- **THE SECOND HELD-OUT PROBLEM** stays the backstop, and now carries a sharper job: it tests the
  *selection*, not just the individual changes.
- **Audit against the three concentrations above**, not against a general suspicion — a diffuse
  caution catches nothing and taxes everything.

**A BASELINE ARM IS STILL WORTH ONE RUN** (bare dispatch, no apparatus, same budget and class) —
expected to fail, and expected to be sensitive to prompt specifics in a way that does not
generalise. That expectation is worth pre-registering, because if the bare arm *does* well the
benchmark is measuring the models rather than the method.

**WHAT TO MEASURE BESIDES THE HEADLINE**, and it is the half that stays informative when the
headline does not fall: did the negatives ledger accumulate would-change-ifs somebody could
test · did checkers **COMPUTE** rather than argue · did the re-derivation agent converge by a
different route · did the paths ledger's death trigger fire when a route died · did a checker
catch something real. A clean, well-recorded failure at a middle rung is still a result **about
the apparatus**.

**★ THE CONSTRUCT-VALIDITY LIMIT, and it is the sharpest objection to this whole item**
(human coordinator, 2026-08-27): *"maybe not about the fact that we should attempt a problem
with a closed result. The shape of TWT is a reality of research. Sometimes an increase in
parsimony and clarity is a valuable outcome. Maybe as much as an exact result."*

**This is a validity threat, not a preference — and it is the overfitting concern one level up.**
The earlier entry worried about apparatus changes fitted to a target; this is about the
BENCHMARK ITSELF fitting a *shape of success*. **Optimising an apparatus against closed-result
problems biases it toward problems that have closed results**, and most research does not. An
apparatus that only knows how to value an exact answer will quietly get worse at the work that
increases parsimony, locates a gap precisely, or replaces nineteen inputs with five — and it
would score that decline as progress.

**What survives the objection, and what has to be added.**

- **The closed-result arm stays, for one reason only: it is the only thing that can RANK.** A
  judgment-laden outcome cannot rank versions without the judgment becoming the measurement.
  Keep it — and keep it labelled as measuring **one shape** of success.
- **A SECOND AXIS is required, and the apparatus already owns the instruments for it.**
  Structural gain is measurable without a known answer: the **premise-cost readings**
  (FREE / CHEAP / COSTLY / CONVOLUTED — a programme accumulating FREE/CHEAP is converging, one
  accumulating COSTLY/CONVOLUTED is fitting), the **counted INPUT economy**, the comparative
  ledger's **debt structure** (named · payable · being worked), **gaps LOCATED versus left
  vague**, and tier honesty under adverse review. None of these needs anyone to know the answer.
- **The deployment is where axis 2 is measured** — a live programme with a real corpus, not a
  benchmark. Its target being open is not a defect of the measurement; it is the condition most
  research runs under.
- **And record parsimony as a WIN, or the apparatus teaches its agents which shape to value.**
  The wins ledger exists because twelve ledgers recorded failure and none recorded a result. A
  structural reduction is a win of a different shape, and if only exact results are ever entered
  there, the ledger becomes a lesson in what does not count.

**Neither axis alone is the picture.** Rank on the first; validate on the second; and treat a
version that climbs the benchmark while flattening the debt structure as the divergence tripwire
firing — comprehension up, findings down, one level up.

**PREREQUISITE — discharged 2026-08-27.** The predictable first failure is instances declaring
the target impossible on the prior that the literature would already have done it. **C-35** now
forbids that inference, and `manuals/paths.md` §2-bis carries the grading procedure with
`C-unsearched` for the case the prior actually describes.

---

## MEANING NOTES — do not compress

*(The founding worklist carried a region kept verbatim and never summarized, because the
compression pass is exactly what loses the reasoning behind a decision. This is that region.)*

- **Redundancy is not duplication.** Four diets on one claim is the instrument; the same
  paragraph in four files is waste. Every efficiency question in W1 turns on holding those
  apart, and the fast, wrong answer is to treat them as one thing.
- **The apparatus can only accumulate unless something prices removal.** Every structure here
  has a champion — its motivating incident — and no removal has one. Q2 (cost per pass) is the
  only mechanism by which this toolkit can shrink on evidence rather than on fatigue.
- **A tag can be load-bearing.** `twt-apparatus-20260827` is not housekeeping: four citations in
  another programme's paper resolve through it (RUL-112). Tags usually look disposable, which is
  exactly why this one is written down here — the cheapest way to break a published citation is
  to tidy up.
- **The regress question is closed** (human coordinator, 2026-08-27): for a repository whose
  work IS commits, git history is the negatives ledger and the paths ledger. The apparatus asks
  a *research* programme to keep records that a version-controlled toolkit already keeps.
- **This repository is a programme too.** It has a docket now; it does not yet have an engine,
  a negatives ledger, or a paths ledger of its own. Whether it should is itself an open
  question — but the asymmetry is worth seeing: the apparatus asks every programme to keep
  records it does not fully keep about itself.
