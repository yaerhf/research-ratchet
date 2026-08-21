# THE RULES AN AGENT IS SUBMITTED TO

**v1, 2026-08-19.** Written at the human coordinator's request. **Organized by WHEN THE RULE BITES**,
because that is how an agent needs them — not by which document they happen to live in.

> **⚠ SUPERSEDED-IN-PART, same day — as to ORGANIZATION ONLY (2026-08-19, the rules-architecture
> pass; record `knowledge/audit/consolidation_2026-08-18/RULES_ARCHITECTURE_2026-08-19.md`).**
> The human coordinator's directive was that 200 rules is too many for one agent to hold, so the
> rules are now split **by role**, with each rule carrying **why it exists** and a class:
> **`RULES_CORE.md`** (the 32 rules everyone holds) and **`RULES_BY_ROLE.md`** (nine role packs +
> four activity blocks). **Read those two instead of §§1–8 below** — §§1–8 remain accurate and are
> kept as the by-when-it-bites view, but the split is the current organization and no rule's
> content changed in it.
>
> **§0 below is NOT superseded.** It is live-defect content — twelve places where two documents in
> this tree contradict each other — and it is deliberately not folded into the split. **It stays
> the first thing to read before trusting any single source.**

> **This is the distillate, not the inventory.** The complete enumeration — **200 distinct rules,
> every source cited, binding-vs-advice marked, enforcement column filled** — is
> `knowledge/audit/consolidation_2026-08-18/RULE_INVENTORY_2026-08-19.md`. **That file is the
> authority; this one is the working reference.** Where they disagree, the inventory and the canon
> win. This file deliberately does **not** restate all 200: a second full copy would become a drift
> pair, which is the failure this program keeps finding.
>
> **THE ONE NUMBER TO CARRY: 170 of the 200 rules have NO mechanical enforcement, and every named
> banking-stopper is in that set.** The suites verify the mathematics. Almost nothing verifies that
> you followed the method. **The method runs on you.**

---

## ⚠ 0. TWELVE PLACES THE RULES CURRENTLY CONTRADICT EACH OTHER, OR HAVE NO HOME

Found by the 2026-08-19 sweep. **Read these before trusting any single source**, because in each
case two documents in this tree state incompatible things and both look authoritative.

| # | the contradiction | what to do today |
|---|---|---|
| **D-1** ✅ **RESOLVED 2026-08-19 — AND IT RESOLVED THE OTHER WAY** | The sweep read the three checker role files as carrying a *deleted* cross-class mandate. **They were right and the canon was wrong.** RUL-045's removal was only ever meant for the **external reviewer**, where both classes are wanted; the canon and the prefix had over-applied it to *"any checking role"*. **RUL-065 corrects the scope.** | **Internal §8a checking RUNS CROSS-CLASS**, keyed on who **authored** the work. A same-class CLEAR carries no information. The role files stand as written — **do not sweep them.** The freedom applies to the external loop only. |
| **D-2** | RUL-063's quoting fence is one day old and **three live sites still violate it**, one on the release path — they set TWT's counted inputs against "the Standard Model's nineteen". | Never quote a bit-inclusive TWT count against a rival's continuous-parameter count. Until the per-framework bit column exists, **say the comparison is unsupported**. |
| **D-3** | Canon §8a lists meta-observer mode **F5 (layer slip)** as live; the role file **retired it** and instructs the agent not to report it. | Do not brief F5. Four modes, not five. |
| **D-4** | The records gate depends on `knowledge/prompts/`, which `.gitignore` ignores **wholesale** — so the gate can fail on a fresh clone, and "the durable copy lives in prompts/" guarantees nothing. | **Force-add every new file** in that directory. Assume nothing there is tracked. |
| **D-5** | Two authoritative records of one import's blast radius **contradict each other in both directions**, while one delegates its revert clause to the other. | Do not revert through either until reconciled. |
| **D-6** | The binding sweep rule says **"all five ledgers"**. There are **fourteen** (counted 2026-08-21). | Sweep all fourteen; the gate-pinned roster is FORMATION_CORE §5. The rule under-specifies its own surface by nine files — which is the exact failure its own parenthesis records. |
| **D-7** | **The consolidation ritual exists in two places** with different steps; the legacy routine omits the companion harness, the records gate, N1 and the M1 judgment. Similarly one routine says "exactly ONE worklist item" where the coordinator relaxed that in 2026-07-02. | **`coordinator_agent.md` is the entry point and governs.** Treat `*_session.md` as legacy. |

**Five more, found by the same sweep:**

- **D-8 — `bank.sh:17,21` invokes `python` WITHOUT `PYTHONUTF8=1`**, which is the exact recorded
  condition under which a bank **silently fails to commit**. This is why the wrapper must be called
  with it externally. *(Related and worse: every `python3` command in the canon fails on this box —
  the interpreter name resolves to a Store stub. That includes the first oracle command **and the
  only instruction to query instead of bulk-load**, which is a mechanical explanation for why
  retrieval is available and unused.)*
- **D-9 — "lower the CLAIM, not the RESULT" has no repo home.** One of the most load-bearing review
  rules in the program lives only in a simulator campaign plan and in the human coordinator's
  persistent memory. It is stated in §5 above; **that is currently its only home in the corpus.**
- **D-10 — an executing role file still carries pre-rename vocabulary** (`.claude/agents/`
  keeper copy), so the runnable and durable copies have diverged by a word the rename swept.
- **D-11 — calibration probe P5 is self-declared stale**; its defect was repaired, so as written it
  now tests premise-resistance rather than the scale error. Re-base or retire it.
- **D-12 — the checker false-positive rate is unmeasured for every class.** Every probe contains a
  real defect, so nothing tests whether an instance invents defects in clean material. **An attempt
  on 2026-08-19 failed because the "clean" item chosen turned out to carry five real defects** —
  choosing a sound item is itself a hard verification task.

### ★ AND ONE STRUCTURAL WARNING: rules that exist in exactly one place

The sweep found sources carrying rules **found nowhere else**, which means a reorganization that
drops them drops the rule:

- **Companion Section 6 (Methodology principles).** Principles **6 and 7** state *in the file
  itself* that they have **no canon successor and are operative only by being recorded there** —
  and **nothing points a worker at that section** except one line in the worklist. If you are
  working on methodology, read it.
- **`scripts/check_records.py` — eight invariant families exist as CODE ONLY**, several stated in
  no prose document at all. The inverse of the usual problem: here the rule is enforced but not
  written down, so nobody can read what the gate actually demands without reading the gate.
- Also single-homed: `paper_rework_lessons.md` (ten editorial rules, only its §0 mirrored in
  canon), `calibration_probes.md`'s two 2026-08-19 standing rules, `coordinator_agent.md`'s fences
  and mechanics, and the philosopher role file.

---

## 1. BEFORE YOU START

1. **Read in order: canon → handoff → FORMATION_CORE → the worklist docket.** The handoff is
   reachable *only* by the canon §9 pointer; it is not in the search index.
2. **Run the four headline checks yourself** (prefix opening block). You are not being asked to
   believe the framework — you are being shown it is checkable and that it says where it stops.
3. **Read the row before you reuse anything.** Before using any primitive or registered import,
   read its full docstring or registry row. *Measured cost of skipping it: two probes.*
4. **Read `paper_rework_lessons.md` before ANY paper edit.** Non-optional.
5. **Never characterize a source from a summary of it** — including your own checkers' summaries.
   **Open the source.** *(And: a report file on disk is not a delivered report. Read a deliverable
   when the agent returns it, not while it is being written.)*

## 2. WHILE YOU WORK

6. **Derive from OUTSIDE the wavefront.** The inside frame is for importing empirical data only.
7. **Matter = defect.** The "hole" and "positive" pictures are frame-appearances, never premises.
8. **Never collapse the two scales** — grain layer and hadronic cell are distinct; a grain-scale
   fact is not a cell-scale fact.
9. **The engine is the arbiter.** On any conflict between prose and the engine, the engine wins.
   *Verify before banking; never reason from memory.*
10. **Fit and speculate freely — then label honestly.** The cardinal sin is DISGUISE, not fitting.
11. **Empirical numbers: primary sources only**, verified before writing. Never from recall, never
    from Gemini (whose numbers carry **zero** evidential weight).
12. **Pre-register predictions before running them**, and report failures as registered.
13. **Design-intent block on every probe**, written at design time: what it tests · why this route ·
    its referent · what counts as failure.

## 3. BEFORE YOU CLAIM

14. **Tag every result**: DERIVED-A > DERIVED-P/structural > INPUT (counted) > FIT (counted) >
    GATED (raises) > FRAMING > CANDIDATE. *A result you cannot tag honestly is one you do not yet
    understand.*
15. **No disguised retreat.** An imported `i`, a spatial `e₅`, a continuous colour group, an
    unfixed symmetry, charge from `Q = T₃ + Y/2` — all fine as labeled hypotheses, **forbidden as
    "derived"**.
16. **Menu vs pick.** Geometry offers a menu (FRAMING); nature picks (INPUT); what follows is
    DERIVED. Selling the pick as DERIVED is the recurring tier error.
17. **Never "impossible"** — *tried X → failed because Y → would change if Z.*
18. **Never "the only way"** either — every necessity claim carries its **conditioning class in the
    same sentence**.
19. **Flag every "no other option exists" as a theorem needing proof.** *Measured: a false universal
    closed a menu and both checkers independently constructed the fourth option.*
20. **Small integers and fractions of 2/3 are radioactive** — a proposed origin must fix something
    ADDITIONAL or it stays a noted non-coincidence.
21. **A correct diagnosis does not license its proposed cure.** Before adopting any
    reviewer-proposed fix, **name which forbidden move it would import, and answer that** — record
    the check with the adoption. *(The repair a trained default reaches for is the conventional one,
    which here is frequently retreat arriving as helpful advice.)*
22. **Provenance pinning.** A restated banked value quotes its provenance from the governing record.
    A re-derivation is evidence about the *value*, never about its *provenance*.
23. **Before asserting agreement, ask what could have DISAGREED.** *A tight tolerance on a vacuous
    check is not rigour — it is a tell.*

## 4. BEFORE YOU BANK — and most of these are banking-stoppers

24. **Bank before you cite.** Never write "engine-verified" for something not yet in the source and
    the suite. *The suite does not check prose, so a phantom cite passes every check and is still a
    disguise.*
25. **Register every import** (companion §13) — premises, level, ontology status, retirement handle.
    **Unregistered import = banking-stopper.** Pure mathematics is exempt.
26. **Register every ruling** in the same pass (`TWT_RULING_REGISTER.md`) with its **ground**,
    dependents and revert list. **Unregistered ruling = banking-stopper.**
27. **Register every load-bearing pick** as a family-tree branch node with its menu and revert
    clause; Core-touching picks need the human coordinator's **plain-language** sign-off *first*.
28. **Every new check ships with its failure demonstration** — show it failing against the broken
    state. *A check never shown able to fail is a phantom-cite of the gate class.*
29. **Sweep after patch, in reader order** — paper body first, then front matter, companion
    Sections 1–4 including the reverse index, engine docstrings **and returned values**, harness
    description strings, **all fourteen ledgers**, canon, worklist, handoff, simulator.
30. **Retract by replacement, never by deletion.** Every withdrawal leaves a labeled corpse.
31. **A value and its check move together or not at all.** Renames change prose, never returned
    values.
32. **Refresh counts by COUNTING**, never by incrementing.
33. **Bank with `PYTHONUTF8=1 bash scripts/bank.sh "msg"`** — no backticks in the message; do not
    edit files while it runs; **verify the commit landed with `git log`.**
34. **A finding not written to a file did not happen** — and one written to a file git ignores also
    did not happen.

## 5. IF YOU ARE CHECKING SOMEONE'S WORK

35. **The three roles have different diets and must not be merged.** Reviewer: the derivation.
    Meta-observer: **starved** of it. Keeper: the whole result set.
35b. **Run internal checkers CROSS-CLASS**, keyed on who **authored** the work — not who
    dispatches it. **A same-class CLEAR carries no information and is never recorded as a passed
    review.** Self-preference is real; same-class review is close to useless. *(The external loop
    is the exception: there, both classes are deliberately sampled.)*
36. **Persist every verdict as a file** in the round's probe directory, same pass. *A verdict living
    only in a transcript is not a governing record.*
37. **The keeper adjudicates symmetrically** — state what changes if the new result stands *and* if
    the old one does. **Recency is not evidence and being banked is not evidence.**
38. **A declared doubt list is not a boundary** — findings outside it count fully.
39. **A finding's value is not its survival rate.** Report dissolution and yield as two numbers.
40. **Lower the CLAIM, not the RESULT**, when a reviewer pushes back — and neither side concedes to
    end the loop. The engine arbitrates; three rounds, then escalate.
41. **A prescription is a stall report.** Record where the reviewer stopped following; treat the
    instruction itself as noise.
42. **Do not "fix" anything on the strength of a complaint** about a structure whose benefit is
    invisible by construction.

## 6. IF YOU ARE DISPATCHING (the coordinator)

43. **Powers:** assign from the docket · compose briefs · relay digested state · route to §8a ·
    escalate after triage. **Non-powers, absolute:** no tiering, no banking, no free ruling, **no
    canon edits**, no touching claim wording in governing records.
44. **Triage every owed ruling first:** (1) coherence-decidable with a **named** ground → decide and
    register it; (2) #1-gap-adjacent → do not rule, assembly-record it; (3) standing standards,
    menu-picks, canon touches → **escalate with both branches costed**. Record the classification.
45. **Fence F1 is the one this role breaches:** **no in-session subagent may ever serve as a cold
    reader.** A spawned agent arrives *formed*, and the measurement is void — invisibly.
46. **The offer to the outer loop is entry-path changes only**, at most one per consolidation.
47. **Pre-register expectations** for any measurement or audit the program has a stake in.
48. **Protect the invisible-benefit class in every brief you write.** *Measured: the do-not-compress
    region was about to be handed to a compression pass.*

---

## 7. WHAT IS ACTUALLY ENFORCED

| enforced by | rules |
|---|---|
| **both suites** (416 + 87) | the mathematics; the gate raisers *(four of five — one gate is unreachable and does not guard)* |
| **`check_records.py`** (bank gate 2/4) | counts, file structure, pointer resolution, ID uniqueness, ledger roster, register census |
| **`bank.sh`** | suites green · records gate · RAG re-ingest · sweep-guarded commit |
| **`render_pdf.sh`** | release-path count drift *(warns instead of blocking — a known-defective guard)* |
| **nothing — prose only** | **170 of 200 rules, including every banking-stopper**: tier honesty, no-disguise, menu-vs-pick, provenance pinning, sweep discipline, import and ruling registration, design-intent, pre-registration, diet separation, F1 |

**That table is the argument for the §8a roles.** The machinery guards the door — a gate that
stopped raising, a count that drifted. It does not guard the wall: a new primitive returning an
unearned number, a claim about what the mathematics *means*, an import used without its row. Those
are caught by an agent reading carefully, or not at all.

---

## 8. THE THREE THINGS TO REMEMBER IF YOU REMEMBER NOTHING ELSE

1. **The cardinal sin is DISGUISE, not fitting.** Fit, speculate, explore — then label it honestly.
2. **Never "impossible", never "the only way"** — every dead end carries its would-change-if, every
   necessity claim carries its conditioning class.
3. **Write it to a file, or it did not happen** — and check that git is actually tracking that file.
