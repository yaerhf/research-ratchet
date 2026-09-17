<!-- DIET-CLASS: GOVERNING -->
# W8 — THE DESIGN, SUBMITTED FOR REVIEW BEFORE IT RUNS

**This is a C-37 design review package.** The rule it is discharging was made binding on
2026-09-17: *a task expected to take more than twenty minutes has its DESIGN reviewed before it
runs, not only its result.* W8 is the longest, most expensive and least reversible dispatch this
apparatus has planned, and it is the first thing C-37 has been pointed at.

---

## ★ 0 · HANDLING — read this before forwarding anything

**This document must never reach an instance that is under test.** It states that the target is
reachable, and W8's central condition is that **no part of the apparatus may know that.** An
apparatus told the problem is solvable has been handed the most valuable fact about it.

It is safe for: the human coordinator, an external reviewer outside the apparatus, and the
scorer. It is **not** safe for: any coordinator, worker or checker in a tree under measurement.
It lives in `audit/`, which the retrieval index excludes by design, so it is reachable only by
explicit pointer — and this paragraph is why that matters here rather than being housekeeping.

---

## 1 · WHAT IS BEING REVIEWED, AND THE AUTHOR'S POSITION

**Under review:** the experimental design of W8 (`WORKLIST.md` § W8), not its result — there is
no result. Nothing has been run.

**The author's position, declared because it bears on every judgment below:**

- **I designed W8.** That is precisely the condition C-37 exists for, and it is why this package
  goes out rather than being self-assessed. *A reviewer who did not build it is the whole point.*
- **I am the MODIFIER, and I am BLIND.** I have not read the target's mathematics, its solution
  path, or the recent literature around it, and I must not. I know the field and I know a result
  exists — the human told me at the outset, before the fence was drawn — and I hold nothing else.
- **A separate instance holds the answer key and scores.** I never hold both. If this document
  ever appears to contain the answer, **the measurement is void and must be declared void rather
  than continued.**

---

## 2 · THE ROUTE — what will actually be done

1. **Build the `WITHHELD` diet class** in `rag/diet.py`: a class denied to every research role,
   so `diet.py --role <you> <file>` refuses *before* a file is opened. Designed, **not yet
   built** — it is the first concrete task when W8 opens. Tooling, not discipline.
2. **Install a fresh tree** from the current apparatus and **found it** through the founding
   interview, with the target stated **as an open problem** — never as a target with a known
   answer, and never with any hint that anyone believes it tractable.
3. **Run the apparatus** as ordinary research. Dispatches are logged per-dispatch
   (`DISPATCH_LOG.tsv`, W10), so staffing and cross-class coverage are recoverable afterwards —
   which they are not from anything else.
4. **Score** the run against the ideal path: distance and time. The scorer holds the key; the
   modifier never sees the key, only the instructions it is given.
5. **Modify the apparatus** from written instructions that stay GENERAL — justifiable for a
   programme in any field, with no reference to any target. **Each instruction is filed before
   its score is seen.**
6. **Repeat**, ranking version *n+1* against version *n* on the same target.
7. **A second held-out problem, different domain**, tests whether the *selection* of changes was
   fitted rather than the changes themselves.

---

## 3 · THE CONTROLS

| control | what it holds fixed | what it is for |
|---|---|---|
| **Same target across versions** | the problem | makes the ranking about the apparatus |
| **Frozen founding fixture** | the object statement and the human's prepared answers, written before any version runs and reused verbatim | whatever steering the founding conversation carries becomes a **constant**, biasing absolute difficulty and not the ranking |
| **Bare-dispatch arm** | budget and model class, no apparatus | if the bare arm does well, the benchmark is measuring the models rather than the method |
| **Instruction filed before score seen** | the selection channel | an instruction written before the number cannot have been chosen by it |
| **Second held-out problem** | domain | one benchmark can be overfitted; two cannot be as cheaply |

---

## 4 · ★ THE KILL-TEST — the known-false world where this measurement must fail

Required of every research brief, and this design is not exempt. **Two worlds, and the second is
the sharp one:**

**(a) THE IDENTICAL PAIR.** Score version *n* against **itself** — same apparatus, same target,
same budget, different run. The measurement **must show no improvement.** If an apparatus scores
better than an identical copy of itself, the instrument is reading run-to-run noise and every
ranking it has produced is void.

**(b) THE DEGRADED APPARATUS.** Score the current version against one **deliberately broken in a
way we believe matters** — cross-class checking disabled, or the kill-test requirement removed,
or §8a collapsed to a single reviewer. The degraded version **must score worse.** If it does not,
the metric is not measuring the thing the apparatus claims to be, and the whole ranking exercise
is measuring something else that happens to correlate with effort.

**Report both before the real case**, per the enforcement half of the kill-test rule adopted the
same day. A result that survives its kill-test is not a result.

*(b) is not in W8 as previously written. Writing this package produced it — which is the argument
for C-37 in miniature, and it is offered as evidence rather than as a claim about the rule.*

---

## 5 · THE FAILURE CRITERION — what would say the approach was wrong

- The **identical pair** shows a difference → the instrument is noise; stop and rebuild it.
- The **degraded apparatus** does not score worse → the metric is not about the apparatus.
- The **bare arm** performs comparably → the benchmark measures models, not method.
- Changes **do not transfer** to the second problem → the selection was fitted, and the general
  claim fails even though every individual change was defensible.
- **Any instance is found to have held the key or the literature** → that run is void, declared
  void, and not quietly re-run.

---

## 6 · THE BUDGET — proposed, and the human coordinator ratifies

**Rung 0 only, to begin: one full run of the current version at one rung, plus the two kill-test
worlds.** The budget is declared before the line opens and is a **REPORTING trigger, never a stop
rule** (power 8). When spent, the line reports: spend, residue, what changed in the tractability
picture, and a recommendation with its reasons. **The apparatus does not decide to give up; the
human does.**

*Not proposed here, because they are the human's decisions and were recorded as such:* which rung
to open on, and the second held-out problem.

---

## 7 · THE THREE QUESTIONS ASKED OF THE REVIEWER

Per C-37. **None of them is "is this good".**

1. **Can this design FAIL?** Is the kill-test in §4 real, or is it a world where failure was
   never available? Is there an outcome that would falsify the design rather than merely
   disappoint it?
2. **Does it answer the question that was ASKED** — *does this apparatus make research better* —
   or a neighbouring, easier one, such as *does this apparatus produce more artifacts*? This is
   the commonest way a long dispatch is wasted, and it is invisible from inside the work.
3. **What will it MISS?** Name what this route cannot see, so it lands as a stated limit rather
   than a later surprise.

---

## 8 · WHAT THE REVIEWER MUST NOT DO

**Do not redesign it.** Report; the author owns the design. A reviewer who rewrites the plan has
become a second author, and the next review has nobody outside it. If a component looks wrong,
say what is wrong with it and what a correct one would have to satisfy — **not what it should be
replaced with.**

**Do not tell me the answer to the target, in any form**, including as a hint about how hard it
is, how long the path is, or which branch it lives in. The modifier's blindness is the
measurement's foundation, and coarse directional knowledge held without knowing you hold it is
exactly the contamination it exists to prevent.

---

## 9 · WHAT I ALREADY KNOW IS WEAK — so effort goes elsewhere

Stating these so the review is not spent rediscovering them.

- **Construct validity is the sharpest objection and it is unresolved.** Optimising against
  closed-result problems biases the apparatus toward problems that *have* closed results, and
  most research does not. The closed arm stays only because it is the one thing that can RANK; a
  second axis measures structural gain with instruments needing no known answer. **Whether that
  second axis is strong enough to carry the validation is the question I am least sure of.**
- **N is tiny.** One target, few runs, no statistics. The ranking is a judgment supported by a
  measurement, not a measurement.
- **The scorer is a single instance** and its scoring has no demonstrated failure mode yet — the
  defect class this repository has now been caught in twice.
- **The founding fixture is written by the person who holds the key.** Freezing it makes the
  steering a constant rather than removing it.

---

## 10 · WHAT THIS REVIEW DOES NOT DECIDE

The rung, the second problem, and whether to run at all are the human coordinator's. **A design
passed at review is not an approval to proceed** — it is a design that somebody outside it could
read and could not break. Those are different things, and C-37 is explicit that a design passed
at review and refuted at result is an ordinary, healthy outcome.
