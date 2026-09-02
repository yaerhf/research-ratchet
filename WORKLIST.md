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
**Grade A — RE-GRADED 2026-09-02 from D. Runnable today; nothing is blocking it.**

`calibration_probes.md` P7 is specified and has never run. Until it does, the profile axis is an
uncalibrated instrument, and the apparatus requires every checker to be calibrated blind before
its verdicts count. **The apparatus exempted its own disposition axis from its own bar** — that
is the finding to carry until the test is run.

**★ THE RE-GRADE, AND IT IS AN INSTANCE OF THE FAILURE §2-bis EXISTS AGAINST.** The old D read
*"blocked on a live programme with real dispatches"* — a D that names an object, as the
procedure requires, but **the wrong object.** A cold external reviewer put P7's own protocol
against that grade, and the protocol asks for something we already have: *"take a claim whose
answer you already know (a repaired defect from this file's own set works well) — dispatch it
twice, blind, same diet, same model class, same brief, changing only the `[PROFILE]` line."*
Repaired defects with recorded arithmetic exist in that file now. Two sessions, one
pre-registration, and the measurement is done.

**Graded by the procedure rather than by feel:** *is the route specified, with only execution
left?* The honest test in §2-bis is **could you write the brief for it right now** — and you
could. That is **A**, not the reviewer's B: nothing needs building, only doing. Length is not
intractability, and neither is unfamiliarity.

**What was actually behind the D, named so it is not lost:** a *construct-validity* worry —
that P7 run against the apparatus's own corpus measures something narrower than P7 run against
live research. That worry is real and it belongs in the result's stated limits. **It is not a
tractability blocker, and filing it as one closed a route nobody had tried.** §2-bis: grade the
ROUTE, never the ANSWER; a credence about what the result would be worth is not a statement
about whether the work can be done.

*(If the human coordinator judges that a self-test against our own corpus cannot measure the
axis honestly, that judgment closes W3 at D **with a reason** — which the paths ledger wants and
the old grade did not have.)*

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

**Third run, 2026-08-27 — after W9 (session zero), and it found the defect W9 was built to
prevent.** Fresh tree → packs → 13 ledgers → canon → handoff → the launch routine's founding
check, run as written. It reported the tree **FOUNDED**. It was not: the check searched
`FORMATION_CORE.md` for the stamp, and the template's own header — the paragraph explaining what
the stamp is — contains the word. **A launching coordinator would have skipped the founding
interview entirely and dispatched workers onto an empty template**, which is precisely the
failure the whole build exists to stop. Fixed by moving the signal to the one thing that cannot
be confused with a description of itself: **does the RECORD exist?** The stamp stays as a label
a worker can see, and is no longer the check. Then the full lifecycle was exercised end to end —
unfounded (gate green, note printed) → interview run → founded (both founding checks green) →
record removed with the ontology left filled (**gate FAILS**, correctly).
**The lesson, and it generalizes past this instance: a check that matches its own documentation
verifies nothing.** It is the phantom-cite class turned on a gate, and only executing the check
on a real tree could have surfaced it.

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

## W9 · SESSION ZERO — THE FOUNDING INTERVIEW · **BUILT 2026-08-27**

> **Directive (human coordinator, 2026-08-27, immediately before the first trial run):** *"When
> the coordinator launches for the first time, he should start interviewing the human to settle
> the foundations and goals of the research."*

**The gap it closed, and it was a hole in the middle of the install.** `INSTALL.md` already ended
by telling the human *"its first session works docket item 1 — writing the ontology — and it
will need you in the room."* **No routine existed for that session.** The apparatus shipped
thirty-two `[OBJECT-SLOT]`s, an installer explicitly forbidden to fill them, and nothing at all
describing the conversation that does — so the most consequential hour in a programme's life was
left to whatever the coordinator improvised, in a role whose ordinary mode is dispatching.

**Built:**

- **`manuals/founding_interview.md`** — the routine, complete for its activity: why two
  interviews exist and must not merge (the installer's *configuration* vs this one's
  *foundations*), the eight questions with the bad answer each attracts, what the session
  writes, and the failure modes of the instrument itself.
- **The fence: refuse, never supply.** The coordinator may refuse an answer as unusable, ask the
  forcing question, and read back a structuring of the human's own words. It may not propose
  content, offer an example answer, default a gap, or smooth a hedge into confident prose.
  *If the apparatus writes the ontology, every later "the canon says" is the apparatus quoting
  itself and the human's ratification ratifies a mirror.* This is the separation principle
  (F1/F4) applied to the human/apparatus interface, and the record's `[HUMAN]`/`[APPARATUS]`
  authorship marks are what make it checkable rather than asserted.
- **The FLOOR** — six items, below which no worker may be dispatched; everything else is
  `[OPEN — founding]` with a promotion condition and goes to the docket. It is deliberately low,
  because founding is not where a programme learns what it is about; working is. It sits between
  two failure modes: infinite founding and premature dispatch.
- **C-36 — the founder's conviction is not a tractability verdict.** The exact twin of C-35:
  one stops you inheriting a stranger's pessimism from the literature's silence, the other stops
  you inheriting the founder's mood from the room you are in. Both are *a fact about people
  entered as a fact about the problem*, and both directions cost.
- **Mechanical first-launch detection** — a `FOUNDED <date>` stamp in `FORMATION_CORE`'s header
  plus the record's existence. **Tooling, not discipline:** the launching coordinator checks a
  stamp rather than judging whether the tree feels founded.
- **The re-founding trigger** — when a CORE commitment's kill condition fires, the founding
  record reopens *in the same pass that records the death*. Sibling of the paths ledger's death
  trigger, and for the same reason: the foundations were correct when they were laid and nobody
  is scheduled to notice when they stop being.
- **Wired in:** the `/coordinator` launch routine (founding check first, plus the CORE-rows read
  at every session start), `coordinator_agent.md` (SESSION ZERO, the diet, a new absolute
  non-power), `FORMATION_CORE`'s header, `manuals/dispatching.md` §0-bis, the manuals INDEX.
- **Gated:** `check_records.py` family 8 — a filled ontology must carry its founding record
  (hard), and the record should name every floor item (warning, because it is a keyword reading
  and *a gate that stops a bank on a word-match would teach programmes to write the words*).
  Six planted-defect demonstrations; the self-test is 30/30.

**Fixed in passing:** the `/coordinator` routine still told the coordinator to read
`RULES_BY_ROLE.md §2` — a drift pair left by W1's pack enactment, pointing every launch at the
~15,600-token file the packs exist to avoid. It now reads `packs/coordinator.md`.

**Verified by execution, not by reading** (W6 third run, same day): the launch routine's founding
check was run on a real tree and **reported a fresh tree FOUNDED** — defeated by the template
paragraph that documents the stamp. The signal moved to the record's existence, and the full
lifecycle was then exercised in both directions. That defect was invisible on the page.

**Still open — and it is the trial run's job, not a build item:** nobody has run this interview
*with a human*. Its structure is verified; its questions are a specification. **The first trial
run measures them**: which the human found unanswerable, which slots came back
`[OPEN — founding]`, and above all whether **refuse-never-supply** survives contact with a human
who wants help answering — the moment the fence is designed for is also the moment it is most
socially expensive to hold.

---

## ★ THE FIRST EXTERNAL REVIEW — 2026-09-02, against `bf302af`

**The record:** `audit/EXTERNAL_REVIEW_2026-09-02_bf302af.md`, kept verbatim as received. It sits
in `audit/`, which the retrieval index excludes by design — a governing record is reachable by
explicit pointer, and this is that pointer.

**What it was.** A cold reader with no write access, commissioned by the human coordinator, which
**executed the repository rather than reading it**: four planted sabotages against a fresh
install, the diet layer probed through retrieval rather than through the checker tool, and three
patches written, run, and shipped with the report. Verdict: engineering HOLDS, design HOLDS,
**self-application OVER-CLAIMS** — the apparatus applies its strictest standard to
`check_records.py` and to almost nothing else.

**Its diet, declared and partial:** it read `WORKLIST.md` and `HANDOFF.md` deliberately, which
`INSTALL.md` step 0 forbids the *installing* agent — correctly, since it was reviewing the
programme rather than instantiating it, and it flagged the crossing itself. It did not open the
founding tree, so **every incident citation in the rules is, to it, an unverified provenance
claim.** It says so. **It is not F1-clean and must not be counted in the external-loop N.**

**★ AND IT TURNED ITS OWN FINDING ON ITSELF, which is the part worth keeping.** A single instance
of one model class reviewed a repository authored with help from classes it cannot identify —
and by RUL-065, *if those classes overlap, the entire review carries no information.* It cannot
determine whether they do. **Neither can we, because nothing in this tree records authorship.**
That is F1 applied to F1's own author, and it is the argument for building W10 **before**
commissioning the next review rather than after.

**Adjudication — every counted claim was recounted here, and every patch was run before it was
believed.** All six findings CONFIRMED. Two defects were found in the supplied patches by
executing them, which is the standard the report itself set:

| finding | adjudication |
|---|---|
| **F1** cross-class has no mechanical support | CONFIRMED — `grep` finds no author class, no checker class; telemetry has five signals and none is cross-class. **Open as W10.** |
| **F2** 2 of 15 tools carry a demonstration, one never run | CONFIRMED, count reproduced including its near-miss (`bank.sh` matches a naive grep but only *invokes* a self-test). **Acute half closed as W11.** |
| **F3** no CI; W6 is discharged by remembering | CONFIRMED. **Script closed as W12; the workflow is the human's call.** |
| **F4** verdict-shopping measurable only over written verdicts | CONFIRMED — the telemetry says it itself. Closes with W10. |
| **F5** index rebuilt whole at every bank | CONFIRMED — 1708 KB index against 1484 KB of source. Low, deferred, recorded. |
| **F6** tools die when their reader closes | CONFIRMED **with a correction**: on this box it is not `BrokenPipeError` at the print but `OSError` EINVAL at CPython's shutdown flush, exiting **120**. A guard catching only `BrokenPipeError` would have missed it. **Closed** at all six entry points. |

**Defects found IN the review's own patches, by running them:**

1. **`telemetry_metric6.py` fails OPEN on `UNKNOWN`.** Its prose says an unattributable class
   *"is counted as same-class"*; its code compares the two columns for equality, so a row of
   `classA / UNKNOWN` scores as **cross-class**. On three synthetic rows it reported **1/3
   same-class where the honest answer is 2/3** — an unattributable dispatch *flatters* the very
   metric built to catch flattery. Must be fixed before W10 ships.
2. **It reintroduces the cp1252 crash** — a `⚠` glyph, in a tool `bank.sh` runs under `|| true`,
   so the crash would be **swallowed** and the telemetry would just stop reporting. That also
   exposed a gap in our own morning's fix: `honesty_telemetry.py` had been missed. Guarded now.

---

## W10 · THE DISPATCH LOG — give RUL-065 something to measure
**Grade A · DISCHARGED 2026-09-03 · closes F1 and F4**

**Built:** `knowledge/ledgers/DISPATCH_LOG.tsv` (created at install, step 2c) · coordinator
**power 10**, one row per dispatch in the same pass · `manuals/dispatching.md` **§0-ter** ·
telemetry **signal 6** · two `check_records.py` invariants with six planted-defect demonstrations
(self-test now 36/36) · a regression pin in the install dry-run that an EMPTY log must still
report `RUL-065 UNMEASURED`, because an empty log and a healthy one must not read alike.

**★ THE DESIGN CHANGED ON THE HUMAN COORDINATOR'S CORRECTION (2026-09-02), and the correction is
the load-bearing part.** Both the review's proposal and the plan that followed it assumed a
`checker_class` / `author_class` pair implied by a staffing directive. That premise is false
here: *"roles are not attributed by model. Sometimes I can ask for a Fable coordinator, sometimes
Opus. To each one its chance."*

Three consequences, and the first is the one that decided the timing:

1. **A varying assignment cannot be reconstructed after the fact from anything.** A fixed
   role→class directive could have been read off a document at any later date; a per-dispatch
   choice leaves no trace outside the moment it is made. **The gap the review found was worse
   than the review thought, not better** — recorded at dispatch, or lost.
2. **The column is a MODEL, not a class.** The model is the observable; sameness is inferred
   from it. A `[OBJECT-SLOT]` staffing table would have been a fiction dressed as a directive.
3. **The rotation itself is a strength worth naming** — deliberate variation is exactly the
   anti-monoculture practice RUL-065 argues for. What was missing was never the practice; it was
   any record that the practice happened.

**The `UNKNOWN` rule, and why it is the opposite of the reference implementation.** `UNKNOWN` is
legal in either column and **counts as SAME-class** — fail-safe, exactly like an unmarked file in
the diet layer. The patch that arrived with the review compared the two columns for equality, so
`opus / UNKNOWN` scored as a *cross-class* check: **an unattributable dispatch would flatter the
very metric built to catch flattery.** Measured on synthetic rows (1/3 same-class where the
honest answer is 2/3) before the fix was written. *Unattributable is not evidence of
independence, and a metric that scored it so would reward leaving the column blank.*

**What it still cannot see, stated so it is not over-read.** It records what the coordinator was
told. It cannot verify that the model named is the model that ran, and a programme that dispatches
without logging shows `0 logged` forever — which is why the *gate* pins the divergence
independently: every persisted verdict must have a row, and every row must name a file that
exists. The log reports; the gate refuses.

**The gap.** `WHY.md` opens with the founding measurement: a month of *"found nothing"* caused by
same-class review. Every diet, the cross-class dispatch rule, the calibration probes and the
review architecture descend from it. **Nothing in this tree records which class authored a claim
or which class checked it**, so the generative measurement is exactly what rule 205's WHY column
calls *a separation asserted and never verified* — a convention, not a control. Its breach is
invisible by construction: the gates stay green, the telemetry prints five healthy lines, and the
verdict looks identical.

**The fence that must govern it.** A **record, not a gate** — it reports and never blocks, for the
same structural reason the telemetry never gates: a log that can refuse a bank gets bypassed and
then logs nothing. And it must not become a second place verdicts live: it carries a **pointer**
to the verdict file, never a copy.

**The artifact.** `knowledge/ledgers/DISPATCH_LOG.tsv`, append-only:
`utc · role · checker_class · author_class · claim_id · verdict · verdict_path`. `UNKNOWN` is a
legal value in either class column and **counts as SAME-class** — fail-safe, like the diet
layer's unmarked-file rule. *(The supplied patch gets this backwards; see above.)*

**Written per-dispatch by the coordinator, in the same pass** — the discipline that already
governs register rows and verdict files. **Reconstructed at consolidation it is a stale-sync note
and worse than nothing** (the C-24 class).

**What it buys:** metric 6 in the telemetry (same-class rate, same-class CLEARs that carry no
information, roles that have *never* run cross-class, and `RUL-065 is UNMEASURED` when the log is
absent — the honest state, and itself the finding); verdict-shopping measured against dispatches
rather than survivors; and a `check_records.py` invariant that every `VERDICT_*` file resolves to
a dispatch row and every row claiming a verdict resolves to a file — which catches the **unwritten
verdict**, currently invisible. Ship it with its planted-defect demonstration (rule 35).

**★ WHY THE TIMING IS LOAD-BEARING.** The first trial run is queued. **Run #1's dispatch data can
only be collected once**, and W8 ranks apparatus *versions* — a comparison that needs to know
which class did what. Built after the run, the first data point is gone.

## W11 · A DEMONSTRATED FAILURE MODE FOR THE DIET LAYER
**Grade A · DISCHARGED 2026-09-02**

`rag/diet.py --self-test`: 27 planted-defect demonstrations — rule 92 across all four checker
roles with the philosopher's RUL-043 carve-out as a control, **the 2026-08-27 leak pinned as a
permanent regression**, the marker below `MARKER_SCAN_CHARS`, three fail-safe cases, every
starvation that *is* an instrument with its matching control, saturated roles verified **not**
over-starved, and the role aliases. Wired into `bank.sh [2/4]`, matched count-agnostically so the
mode can grow. **Its own failure mode is demonstrated, not asserted** — deleting the
meta-observer's `TRANSCRIPT` denial turns exactly that line red and exits 1, verified here by
doing it.

## W12 · W6 AS A GATE
**Grade A · the script is DISCHARGED 2026-09-02 · the CI workflow is the human coordinator's call**

`scripts/install_dryrun.sh` executes `INSTALL.md` steps 0–6 against a throwaway tree and banks
once; green, exit 0. Two assertions ride along as regression pins for defects this week actually
produced: that retrieval **answers** on a fresh tree rather than merely writing an index, and that
a fresh tree reports **NOT FOUNDED** — the W9 check that was defeated by the paragraph documenting
it.

**Framing for the register, kept honest:** this adds no rule. It moves one rule out of the ~85%
unenforced set, which is the direction the WHY column is supposed to move. **And it cannot check
that anyone followed the method** — it checks that the machinery still runs. The gates guard the
door, not the wall; do not let it be quoted as more.

---

## W13 · A DEMONSTRATED FAILURE MODE FOR THE CROSS-CLASS PREDICATE
**Grade A · DISCHARGED 2026-09-03 · from the external reviewer's second pass**

**★ THE FINDING, AND IT IS THE SHARPEST THIS APPARATUS HAS RECEIVED FROM OUTSIDE.** On
2026-09-02 the reviewer's own `same_class` shipped fail-OPEN under a fail-safe docstring; we
found it, fixed it, and **shipped the fix with no demonstration.** The reviewer then put the
inversion back into a copy of `ea0d60d` and ran every gate this repository had:

```
python scripts/check_records.py --self-test    PASS (did not notice)
python rag/diet.py --self-test                 PASS (did not notice)
python scripts/check_records.py                PASS (did not notice)
bash scripts/install_dryrun.sh                 PASS (did not notice)
```

**Reproduced here verbatim before a line was written.** The telemetry then reported
`0/3 checks were SAME-CLASS (0%)` on a log where **every row is unattributable**, with
`3 unattributable — counted as same-class` printed *directly beneath it*: the two claims
contradicting each other on adjacent lines of one report, and green everywhere. As the reviewer
put it, the metric built to catch flattery **flattered hardest exactly when it knew least** —
and it would have been most wrong at adoption, when a tree starts with placeholder columns,
which is when it is most likely to be believed and least likely to be checked.

**★ THE STRUCTURAL CAUSE, NAMED, BECAUSE THE FIX IS NOT A PATCH.** The telemetry sits outside
every gate *by construction*: `bank.sh` runs it under `|| true`, and **that is correct and
stays** — a telemetry that can block a bank gets removed within a week and then measures
nothing. But `|| true` was protecting the **report** from failing a bank while silently
protecting the **predicate** from ever being checked. Those are different things.
**The report never gates. Its predicate always does.**

**And the measurement that caught the original defect did not run again.** The comment above
`same_class()` records *"measured on synthetic rows (1/3 where the honest answer is 2/3)"*. That
measurement was real and it worked — and it was a one-off, which is exactly the distinction this
tree draws everywhere else. **A check never shown able to fail is a phantom cite of the gate
class**, and that verdict does not stop applying because the check is ours.

**Built:** `scripts/honesty_telemetry.py --self-test`, **19 demonstrations** — eight of them
pinning the 2026-09-02 inversion permanently (`UNKNOWN` either side, blank, whitespace,
lowercase `unknown`), the arithmetic asserted rather than the prose (*a wholly unattributable log
reports 3/3, never 0/3, and says `100%` in the printed line*), controls for genuine cross-class
pairs, a same-class REFUTED that is **not** a no-information CLEAR, and a worker dispatch that is
not a check at all. `sig_crossclass()` was split so `_crossclass_report(rows)` is **pure over
rows** — the same discipline every other predicate here follows, so a demonstration can plant
defects without touching a tree.

**Its own failure mode is demonstrated, not asserted:** the inversion restored on a COPY turns
8 of 19 red and exits 1, naming the pinned line first.

**Wired into both gates** — `bank.sh [2/4]` beside the other two self-tests, and a fifth CI step.
Re-running the reviewer's experiment against the gates as they now stand: **caught twice**, once
by its own step and once transitively inside the install dry-run, which runs `bank.sh`.

**Counted progress on F2: 4 of 16 executable tools now carry their own demonstrations, up from
2 of 15** at `bf302af` — and all four of them run.

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
- **The founding question a record must be able to answer is *"who actually said this?"*** An
  invented premise and a stated one read identically once they are written up well — that is the
  whole reason the founding record marks authorship line by line instead of asserting a fence.
  The detector is blunt and it works: run your eye down the `[HUMAN]` lines alone and ask whether
  they still say something. If the object only holds together with the apparatus's lines carrying
  it, the apparatus wrote the programme.
- **This repository is a programme too.** It has a docket now; it does not yet have an engine,
  a negatives ledger, or a paths ledger of its own. Whether it should is itself an open
  question — but the asymmetry is worth seeing: the apparatus asks every programme to keep
  records it does not fully keep about itself.
