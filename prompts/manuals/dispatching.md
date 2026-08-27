<!-- DIET-CLASS: RULES -->
# MANUAL · DISPATCHING — read this before you compose a brief and launch a worker

**Trigger: you are about to send a task to an instance — a worker, a checker, a referee.**
Complete for the activity: read this, plus `coordinator_agent.md` for your powers and fences, and
you need nothing else.

> **This manual quotes with pointers and never paraphrases** — a manual that restates a rule
> creates a **drift pair**, and drift pairs are how this corpus breaks.

---

## 0 · WHAT A BRIEF IS

**A brief is a research memo, not a task ticket — and its steer is a hypothesis the worker may
invert.**

That is not a style note; it is the measured finding that reorganised how briefs are written. In
the campaign this discipline was taken from, **both creative steps came from an agent
contradicting its brief's steer**: one was told to bound a quantity from above, found the route
*empty*, and inverted it; the other was handed a diagnosis and a wrong forecast of the recovery
and produced the winning result **against the steer**. The coordinator's own summary was that at
each step it *"pointed the mechanism the wrong way."*

Two consequences, and they pull the same direction:

1. **Give the worker enough structure to invert.** A thin ticket cannot be argued with, so it
   cannot be productively contradicted. Your conjecture and your forecast are what make inversion
   possible.
2. **Say in the brief that inversion is a success mode.** *A worker reporting that the briefed
   route is empty, and returning a different one, is to be received as a success* — never as
   non-compliance.

---

## 1 · PICK THE TIER FIRST — and mark it in the first line

- **FULL CEREMONY** — anything banking-bound. The complete brief format, §8a routing, persisted
  verdicts, registry rows.
- **LIGHT PATH** — exploration that CANNOT bank. `[TASK]` + `[DIET]` + `[RETRIEVAL]` + `[FENCES]`
  + the banking line. No §8a round, no registry rows; the output is **CANDIDATE by construction**.

**The light path is safe for exactly one reason, and the reason is the whole justification: the
guarantees only need to hold AT THE BANK GATE.** Everything upstream is non-binding by
construction. A light-path result that later wants to bank **re-enters at full ceremony and is
not grandfathered.**

**An unmarked dispatch is full ceremony.** And load the prefix conditionally — the light path
takes `RULES_CORE.md` plus the role pack, not the full formation prefix. *(Measured: a
probe-scale dispatch paid ~20,000 tokens of fixed overhead to do ~600 tokens of work. Much of
that cost is the dispatch pattern, not the rules.)*

---

## 2 · THE REQUIRED FIELDS, AND WHY EACH ONE EXISTS

The full format is in `coordinator_agent.md`. What follows is why the fields that feel optional
are not — each was added after something went wrong without it.

**`[DIET]`** — what this instance is saturated with and starved of, in one line. **The whole
architecture rests on the meta-observer being starved of the derivation, and until this field
existed nothing checked that any dispatch actually starved it.** A brief could leak the
derivation and the verdict would look identical. *A separation asserted and never verified is a
convention, not a control.*

**`[RETRIEVAL]`** — name the **role**, never a bound: `--role meta-observer`, not a flag you
could pick wrong. Retrieval reaches the round directories, so an unbounded query from a starved
role destroys the measurement it was dispatched to make. Say so even when retrieval is not
installed, and name what the instance must read instead.

**`[KILL-TEST]`** on every research brief — **name an object where the answer is KNOWN AND
NEGATIVE, and state what the method must return on it.** If the method "succeeds" there, the
method is broken and the result is void *however good it looks on the real target*. **A brief
with no kill-test is a brief that cannot fail.** The strong form is a maintained zoo of
known-false objects plus a checker every proposed mechanism runs through *before* it is worked
on — in the source campaign that tool killed all 106 surviving ideas from a prior campaign,
mechanically reproducing a triage a human had done by hand.

**`[FORECAST]`** — your own expectation, stated **before** it runs. It costs one line, and **its
value is that a wrong forecast is legible afterwards**: on that campaign's own account the
coordinator's forecast was WRONG at both creative steps, which is how the wins were recognised
as wins.

**`[ADJACENT]`** — required in the **return**, so say so in the brief: the route taken and the
routes left, each with a reason, a tractability grade and what would make it first choice. One
fork, written while the alternatives are still in view — the only moment they are cheap.

**`[PROFILE]`** — NEUTRAL or PROSECUTORIAL. Unmarked runs NEUTRAL. *(The steelman profile was
removed and folded into the worker's own consensus duty; the risk-appetite holder was never
instituted — see `PROFILES.md`.)*

**`[DOUBTS]`** — optional, and if present it carries this sentence **verbatim**: *this list is
not a boundary — findings outside it count fully.* Measured: six doubts were filed on one panel;
the one the author worried most about was refuted by both checkers **while the governing defect
went unflagged.** A doubt list steers checkers toward what the author already suspects.

---

## 3 · DISPATCHING CHECKERS — four moves that change what you get back

**ONE JOINT PER REFEREE, EACH WITH A WORKED PLAN OF ATTACK.** Not *"review this"* but *"you take
this joint, and here is how to attack it."* **A referee given the whole claim checks the part it
finds easiest; a referee given one joint checks that joint.**

**A RE-DERIVATION AGENT FORBIDDEN TO READ THE PROOF.** Dispatch it on every banking-bound claim.
**State exactly which files are in scope, and do NOT name the derivation's location — even to
warn it off.**

**A LATE REFEREE WITH A DIFFERENT DIET.** After the first verdicts land, dispatch one referee
that *is* allowed to read them and hand it the unglamorous leftovers. This is the one place where
letting a checker see other verdicts is correct, and it works **precisely because it comes last.**

**"PROVES TOO MUCH" AS A REFEREE INSTRUCTION** — the kill-test pointed at the checker rather than
the researcher: *run this argument on an object where the answer is known to be negative.*

**Require layered credence.** Ask every verdict-bearing checker to price **the innermost lemma
and the whole claim separately**, and to name the layer carrying the residual risk. *A checker
that returns one number for a three-layer claim has answered a question nobody asked.*

**Never seed a checker's brief with a known refutation.** In the pilot, one run was handed a
defect in its own prompt and dutifully "confirmed" it. If a defect is already known, withhold it
and see whether the run finds it.

**Cross-class on AUTHORSHIP** — not on who dispatches. Dispatch with an explicit model override.

---

## 4 · AFTER THE RETURN

**ITERATE THE INSTANCE WHEN ITS RESULT REFRAMED ITS OWN QUESTION.** A second turn with context
intact is **the default, not the exception**, whenever the first turn changed what the right
question was. *Measured: across a thirteen-dispatch session this was used zero times — and the
sharpest loss was a probe author who discovered mid-run that the "clean" item it had been handed
carried five real defects, making it the one instance in the building that then knew what a
genuinely clean item must satisfy. It was dismissed instead of asked.*

**★ THE POST-NEGATIVE PUSH — and its three constraints.** After a negative or despairing return
you may push once. **(i) NEVER in the brief** — a pre-announced push teaches workers that
negatives trigger more work, which taxes the crisp declaration of a negative. **(ii) At most ONE
push**, and it must add something: a loosened constraint, a named alternative route, a reframed
question, the reminder of what the worker's own partial results already license — never a bare
"try harder." **(iii) A negative that survives the push is STRONGER** and is recorded as
push-tested. A negative that dissolves under one encouragement was not a located gap. Either
outcome is information.

**DO NOT READ A DELIVERABLE WHILE IT IS BEING WRITTEN.** *Two figures were banked from an
unfinished draft; on delivery the author withdrew one and refuted the other, unprompted.*

**PERSIST EVERY VERDICT AS A FILE** in the round's directory, same pass — and note that checkers
now write their own (RUL-079), returning you a summary and a path. Routing the full text through
you burns your context for no gain.

---

## 5 · WHAT YOU MAY NOT DO WITH A DISPATCH

No tiering, no banking, no free ruling, no canon edits, no touching claim wording in governing
records. **You never "convince" a checker**, and you never pass FORMATION_CORE to one (rule 92,
ABSOLUTE; the philosopher and its contra-reviewer are the only carve-out).

**And the fence this role breaches most often, because dispatching is its ordinary mode: F1.**
**No in-session subagent may ever serve as a cold reader.** A spawned agent inherits the canon
auto-load and arrives *formed*, not cold — and the measurement is void **invisibly, in the
transcript**. A cold read comes from the human coordinator's own sending surface, never yours.

---

## 6 · AUDIT YOUR OWN CREDIT ASSIGNMENT

At every consolidation, check what the records say each instance did against what the transcripts
show. *Two founding cases exist where the coordinator's own later summaries slipped — one
crediting a repair to the referee who organised it rather than the one who proposed it.*
**Attribution drifts toward whoever wrote the summary**, and a self-account that documents its
own attribution errors is a better instrument than one that does not.
