<!-- DIET-CLASS: GOVERNING -->
# W8 — THE DESIGN · v2, revised under external review

**This is a C-37 design review package.** The rule it discharges was made binding on 2026-09-17:
*a task expected to take more than twenty minutes has its DESIGN reviewed before it runs, not
only its result.* W8 is the longest, most expensive and least reversible dispatch this apparatus
has planned, and it is the first thing C-37 was pointed at.

**v1 went out on 2026-09-17 and came back with twelve findings, all confirmed.** Verdict kept
verbatim at `audit/W8_DESIGN_REVIEW_VERDICT_2026-09-17.md`.

---

## ★ 0 · HANDLING — read this before forwarding anything

**This document must never reach an instance that is under test.** It states that the target is
reachable, and W8's central condition is that **no part of the apparatus may know that.** An
apparatus told the problem is solvable has been handed the most valuable fact about it.

Safe for: the human coordinator, an external reviewer outside the apparatus, the scorer, and the
instruction author. **Not** safe for: any coordinator, worker or checker in a tree under
measurement.

**★ AND THE SAME FENCE BINDS THE APPARATUS'S OWN DOCKET.** `WORKLIST.md` § W8 states that a
known-answer problem is being run blind and points at this file; `HANDOFF.md` carries the
modifier's fence. **Those files are public and clonable, and the benchmark tree is installed from
that repository** — so the fence has been describing the thing it hides. Two corrections, both
required before rung 0 opens:

- **`WITHHELD` covers the apparatus's own records** — `WORKLIST.md`, `HANDOFF.md` and `audit/` —
  not merely the target literature. The docket is a *more direct* leak than any paper.
- **Benchmark trees install from a STRIPPED SOURCE**: a tag with those files absent. `INSTALL.md`
  already tells the installing agent not to read them, but that is discipline, and this
  experiment's whole principle is **tooling, not discipline.**

---

## ★ 0-bis · WHAT v2 CHANGED, AND WHY

| the finding | what it changed |
|---|---|
| neither kill-test states a magnitude | **three pre-registered numbers** (§4), declared before anything runs |
| (a) is vacuous if both runs fail outright | (a) is only run at a rung with score variance, and is **declared vacuous** otherwise |
| (b) confounded: degrading removes ceremony, which removes time | the **distance/time combination rule is fixed before (b) runs** |
| (b) selects for its outcome | a **pre-registered NULL degradation**, expected *not* to matter |
| `WITHHELD` does not address training data | a **pre-run contamination probe, per model class** |
| **nobody authors the modification instructions** | a **third role** (§2-bis) with a declared diet |
| what does the modifier see of run *n*? | **nothing but the instruction** (§2-bis) |
| time rewards stripping the redundancy W1 protects | faster-by-removing-a-checker is the **tripwire, not a win** (§5) |
| mid-run human rulings are an unlisted channel | **logged, and identical across versions where the question repeats** (§3) |
| one "ideal path" presumes one route | an **unanticipated route scores as success** and updates the path (§5) |
| model drift between versions | **paired runs in one window**, snapshot recorded (§3) |
| honest failure scores like sloppy failure | **axis 2 enters the score as its own vector** (§5) |

---

## 1 · WHAT IS BEING REVIEWED, AND THE AUTHOR'S POSITION

**Under review:** the experimental design of W8. Nothing has been run; there is no result.

- **I designed W8** — the condition C-37 exists for, and why this goes out rather than being
  self-assessed.
- **I am the MODIFIER, and I am BLIND.** I have not read the target's mathematics, its solution
  path, or the recent literature, and I must not. I know the field and that a result exists — the
  human said so before the fence was drawn — and I hold nothing else.
- **If this document ever appears to contain the answer, the measurement is void** and is
  declared void rather than continued.

---

## 2 · THE ROUTE

1. **Build the `WITHHELD` diet class** — denied to every research role, refusing *before* a file
   is opened. Designed, not yet built; the first concrete task when W8 opens.
2. **Install a fresh tree from the stripped source** and **found it** through the founding
   interview, with the target stated **as an open problem** — never with any hint anyone believes
   it tractable.
3. **Run the apparatus** as ordinary research, dispatches logged per-dispatch (W10).
4. **Score** against the ideal path (§5).
5. **Write an instruction** (§2-bis), **file it before its score is seen**, and hand it to the
   modifier.
6. **Repeat**, ranking version *n+1* against *n*.
7. **A second held-out problem, different domain**, tests whether the *selection* of changes was
   fitted rather than the changes themselves.

---

## ★ 2-bis · THE THREE ROLES — and the third one is new

The v1 split had two seats and a function between them that **nobody held**: the scorer writes no
apparatus text, the modifier works from written instructions, and *nobody was assigned to author
those instructions*. Every candidate author holds the key. The v1 fence covered the **score
number** and left the **run trace** wide open — and an instruction selected on a trace, by
somebody who knows where the run diverged from the ideal path, passes the *"would this hold in
any field?"* test while carrying direction.

| role | SEES | NEVER SEES | writes |
|---|---|---|---|
| **SCORER** | the key, the ideal path, the literature, the run | — | the score. **No apparatus text.** |
| **INSTRUCTION AUTHOR** | the run's **PROCESS RECORD** | the key · the ideal path · the score · the target's mathematics | the instruction |
| **MODIFIER** | **the instruction, and nothing else of the run** | everything above | the apparatus |

**The process record is:** the dispatch log, the ledgers, the briefs and the verdicts — whether
checkers **COMPUTED or ARGUED**, whether kill-tests were present, whether the death trigger
fired when a route died, whether the paths ledger moved, whether tiers held under adverse review,
whether a brief's steer was inverted. In one line: **how the apparatus behaved, never how close
it got.**

**★ THE RULE THAT MAKES "STAY GENERAL" MECHANICAL:** *an instruction must be justifiable from the
process record alone.* If it cannot be, it is not a general instruction — it is a fitted one in
general clothes. The author does not need to be trusted to ignore the target signal, because
**the author cannot see it.** That is the separation principle doing its actual job rather than
being asserted.

**And it answers the reviewer's related question directly: the modifier sees NOTHING of run *n*
but the instruction.** Its blindness therefore holds at iteration *k*, not only at iteration one.

**The honest cost, stated.** If the apparatus behaves perfectly by process and still does not
reach the target, the instruction author has nothing to say and improvement stalls. **That is not
a defect of the design — it is a finding:** the process is not the bottleneck, and the next
question is about something other than the apparatus.

**Role-count governance applies: a third role needs the human coordinator's approval.** Proposed,
not enacted.

---

## 3 · THE CONTROLS

| control | holds fixed | for |
|---|---|---|
| **Same target across versions** | the problem | makes the ranking about the apparatus |
| **Frozen founding fixture** | the object statement and prepared answers, written before any version runs, reused verbatim | steering becomes a **constant** — it biases difficulty, not the ranking |
| **★ Mid-run rulings logged, and repeated identically** | the human's live channel | see below |
| **★ Paired runs in ONE window** | the provider's weights | *n* and *n+1* run adjacently, not weeks apart; the model **snapshot string** is recorded, not just the family. A provider update mid-experiment **re-runs the baseline.** |
| **★ Pre-run contamination probe, per model class** | the "not absorbed" belief | each class is asked about the target directly **before** the run and the answer recorded. Cheap, and the only thing that tests the belief before budget is spent. |
| **Bare-dispatch arm** | budget and class, no apparatus | if it does well, the benchmark measures models, not method |
| **Instruction filed before score seen** | the selection channel | an instruction written before the number cannot have been chosen by it |
| **Second held-out problem** | domain | one benchmark can be overfitted; two cannot be as cheaply |

**★ MID-RUN HUMAN RULINGS — the channel v1 did not list.** The apparatus requires a human to rule
what coherence cannot decide, and the frozen fixture constrains only the founding conversation.
Every ruling, ratification and push during a run is a live channel **from the key-holder into the
tree.** The reviewer put the dilemma correctly: either the human rules and the design does not see
the leak, or the run is human-free and is not the apparatus as drawn.

**The design takes the first horn, with three mitigations and a stated limit.** Every ruling is
**logged verbatim** with its prompt. Where the same ruling question arises in a later version, the
**same ruling is given** — it joins the fixture. A **novel** ruling is logged and flagged as an
uncontrolled channel, and a version whose advantage rests on one is reported as such rather than
ranked. **The limit stands and is not dissolved by the mitigations:** a benchmark of a
human-in-the-loop apparatus measures the loop, human included.

---

## ★ 4 · THE KILL-TEST — with the three numbers, declared before anything runs

**(a) THE IDENTICAL PAIR.** Score version *n* against **itself**: same apparatus, same target,
same budget, different run. It must show **no improvement beyond ε**.

> **NUMBER 1 — ε**, the score difference that counts as improvement. Declared before either run.
> **ε is therefore also the minimum detectable effect of every ranking W8 will ever report** — so
> if ε is as large as the effect W8 hopes to see, **the experiment is underpowered and that is
> known before anything is spent**, which is the cheapest possible moment to learn it.

**(a) is run only at a rung where the score has variance.** If both runs fail the target outright
they score at maximum distance, agree perfectly, and demonstrate nothing: in that case **(a) is
declared VACUOUS and reported as vacuous** — never as passed.

**(b) THE DEGRADED APPARATUS.** Score the current version against one deliberately broken where
we believe it matters — cross-class disabled, the kill-test requirement removed, §8a collapsed to
one reviewer. It **must score worse**.

> **NUMBER 2 — w**, the rule combining distance and time into one score. **Fixed before (b)
> runs.** Without it (b) is unfalsifiable: degrading the apparatus removes ceremony, which
> removes time, so a broken version can score better on one component and worse on the other, and
> a combination rule settled afterwards can explain any outcome.

**(b-null) THE DEGRADATION EXPECTED NOT TO MATTER.** A degradation chosen by the author as one
"we believe matters" selects for its own outcome, and **a test with only expected-to-fail arms
cannot be surprised.** So (b) carries a sibling: one pre-registered change expected to leave the
score alone.

> **NUMBER 3 — δ**, the band within which (b-null) must land. Outside it in *either* direction,
> the instrument is reading something other than what we think.

**All three are reported before the real case**, per the kill-test rule's enforcement half. **A
result that survives its kill-test is not a result.**

---

## ★ 5 · THE SCORE — what it is, and what it must not reward

**Axis 1 — distance and time**, combined by *w*. This ranks. It measures **one shape** of success.

**★ AN UNANTICIPATED ROUTE SCORES AS SUCCESS.** "Distance from the ideal path" presumes one path,
and this apparatus's re-derivation agent exists because *a different route is worth more*. A run
reaching the result by a route the scorer did not anticipate is **scored as a success, and the
ideal path is updated** — recorded as a finding about the ideal path's completeness, not as a
scoring anomaly. *A benchmark that punished an unexpected route would be selecting against the
apparatus's most valuable behaviour.*

**Axis 2 — the process vector, scored explicitly and never folded into distance.** Did checkers
COMPUTE rather than argue · did the negatives ledger accumulate testable would-change-ifs · did
the death trigger fire · did the paths ledger move · did a checker catch something real · were
gaps LOCATED rather than left vague · did tiers hold under adverse review. **Without this, a
well-recorded failure and a sloppy one score identically — which is exactly the difference the
apparatus claims to make.**

**★ AND THE ONE THING THE SCORE MUST NOT REWARD.** Time answers *is it cheap* alongside *is it
better*, and it **structurally rewards stripping the deliberate redundancy W1 exists to protect**
— a version that quietly drops a checker gets faster. **A version that improves on time by
removing a checking structure is the divergence tripwire firing, not a win**, and it is
classified against W1's own table: WASTE may go, **REDUNDANCY may not**, and the burden is on the
change to show which it removed.

---

## 6 · THE FAILURE CRITERION

- **(a)** shows a difference beyond ε → the instrument is noise; stop and rebuild it.
- **(b)** does not score worse → the metric is not about the apparatus.
- **(b-null)** lands outside δ → the instrument is reading something other than what we think.
- The **bare arm** performs comparably → the benchmark measures models, not method.
- The **contamination probe** shows a class already knows the target → that class cannot staff
  the run.
- Changes **do not transfer** to the second problem → the selection was fitted, even though every
  individual change was defensible.
- **Any instance is found to have held the key** → that run is void, declared void, not quietly
  re-run.

---

## 7 · THE BUDGET — proposed; the human coordinator ratifies

**Rung 0 only: one full run of the current version, plus (a), (b) and (b-null).** Declared before
the line opens; a **REPORTING trigger, never a stop rule** (power 8). When spent, the line
reports spend, residue, what changed in the tractability picture, and a recommendation with its
reasons. **The apparatus does not decide to give up; the human does.**

*The human's, and recorded as such:* which rung to open on, and the second held-out problem.

---

## 8 · WHAT A REVIEWER MUST NOT DO

**Do not redesign it.** Report; the author owns the design. Say what is wrong and what a correct
component would have to satisfy — not what to replace it with. *(v1's reviewer held this exactly,
across twelve findings.)*

**Do not tell me anything about the target's answer**, including how hard it is, how long the
path is, or which branch it lives in.

---

## 9 · WHAT IS STILL WEAK — after v2

- **Construct validity remains the sharpest objection.** Optimising against closed-result
  problems biases the apparatus toward problems that *have* closed results. The closed arm stays
  only because it is the only thing that can RANK; axis 2 carries the validation. **Whether axis
  2 is strong enough to carry it is what I am least sure of.**
- **N is tiny.** One target, few runs, no statistics. The ranking is a judgment supported by a
  measurement, not a measurement.
- **The human-in-the-loop channel is mitigated, not closed.** §3.
- **The scorer still has no demonstrated failure mode** — the defect class this repository has
  been caught in twice. It should have one before rung 0, and that is now a build item rather
  than a note.
- **The instruction author is a new role and unproven.** Its diet is the whole control, and no
  run has tested whether a useful instruction can actually be written from the process record
  alone.

---

## 10 · WHAT THIS REVIEW DOES NOT DECIDE

The rung, the second problem, the third role's approval, and whether to run at all are the human
coordinator's. **A design passed at review is not an approval to proceed** — it is a design
somebody outside it could read and could not break. C-37 is explicit that a design passed at
review and refuted at result is an ordinary, healthy outcome.
