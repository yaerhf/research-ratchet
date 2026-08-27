<!-- DIET-CLASS: LEDGER -->
# THE APPARATUS'S OWN DOCKET

*research-ratchet is itself a programme, and it had no docket — which is the defect its own
archivist rules exist to catch. This is that docket: the work owed on the **apparatus**, not on
any object it is given. Instantiated programmes keep their own
`knowledge/ledgers/worklist.md`; this one governs the toolkit.*

**Grades are the tractability scale** (`manuals/paths.md` §2): **A** computation remaining ·
**B** mechanism asserted, construction needed · **C** needs a new idea · **D** blocked on a
named object elsewhere.

---

## W1 · THE EFFICIENCY AUDIT — duplicate activity across roles, and the cost per pass
**Grade B · opened 2026-08-27 on the human coordinator's directive · not started**

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
**Grade A · standing duty**

The 2026-08-27 dry-run found **eight defects** by executing `INSTALL.md` instead of reading it —
including the apparatus shipping with its own records gate red. **An installer never run is a
specification, not an installer.** Instantiate a throwaway programme, bank twice, verify with
`git log`; the whole pass costs minutes.

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
- **This repository is a programme too.** It has a docket now; it does not yet have an engine,
  a negatives ledger, or a paths ledger of its own. Whether it should is itself an open
  question — but the asymmetry is worth seeing: the apparatus asks every programme to keep
  records it does not fully keep about itself.
