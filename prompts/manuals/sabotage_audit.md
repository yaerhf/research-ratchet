<!-- DIET-CLASS: RULES -->
# MANUAL · THE SABOTAGE AUDIT — measure what a suite of checks actually covers

**Trigger: you are about to trust a green suite** — yours, an adopter's, or one you inherited.
Complete for the activity: read this and you need nothing else to run one.

> **A green suite is evidence that nothing broke it, and evidence of nothing else.** The other half
> is this: plant a defect in the region a check CLAIMS to cover, run the checks, and watch. **A
> check that stays green on a planted defect has been DEMONSTRATED not to cover it.** Not argued —
> demonstrated, which is why this finding survives an argument with its author.

**Instrument:** `scripts/sabotage_audit.py`. **It never writes to the tree it audits** — every
sabotage happens in a copy (measured 2026-09-03: a `git checkout` used to undo a sabotage in place
also discarded ~130 lines of uncommitted work).

---

## 1 · THE BASELINE, AND WHY THE TOOL REFUSES WITHOUT IT

**The unmodified copy runs first.** If the checks are already red, every later result is void: you
cannot measure whether a check *fired* when it was firing before you touched anything. That is the
instrument-or-yardstick rule (`checking.md` §0-ter) built into a tool, and **it refuses rather than
reporting** — a report from a red baseline is worse than no report, because it looks like one.

---

## 2 · CHOOSING THE SABOTAGE — the judgment the tool cannot make

The tool plants and runs. **Deciding WHAT to plant is the whole skill**, and it has one rule:

**★ SABOTAGE WHAT A CHECK CLAIMS, NOT WHAT IS EASY TO BREAK.** Read the check's name, its docstring,
its CI step title — that is its claim (`checking.md` §0-quater: a gate's name is a claim). Then
break exactly the thing the claim covers. *Deleting a whole file proves nothing: everything fails.
Changing a comment proves nothing: nothing should fail.* **The informative sabotage is the smallest
edit that makes the claim false.**

**Four that pay, in order:**
1. **Weaken an obligation** — `MUST` to `SHOULD`, `>=` to `>`, a raise to a warning. The check that
   claims to enforce it should go red.
2. **Break a generated artifact by hand** — edit the output of a generator whose gate claims it is
   current. *This is where stamp-checking hides:* a gate comparing a recorded fingerprint stays
   green while the content is wrong.
3. **Make a record lie** — mark something present that is absent, name a path that does not resolve.
4. **Flip a declaration** — a class, a type, a status. Gates usually check that a declaration
   EXISTS, rarely that it is right, and the difference is a real hole worth locating.

**One sabotage, one claim, one edit.** An anchor that matches zero times or several is refused as
void rather than approximated — a sabotage you cannot point at is not evidence.

---

## 3 · READING THE RESULT

| verdict | what it means | what it does NOT mean |
|---|---|---|
| **CAUGHT** | the checks went red on this defect | that they cover the next one |
| **MISSED** | the checks stayed green with the defect in place | that the suite is bad — only that this claim is not enforced |
| **VOID** | baseline red, or the anchor did not land uniquely | anything at all |

**A MISSED is only a FINDING when a check claimed that region.** Where nothing claimed it, the same
result is an **un-attacked surface** — worth listing, never worth reporting as a hole. The tool
cannot tell these apart, and it says so; **you can, and that judgment is the value you add.**

**Report both halves:** what was planted and caught, what was planted and missed, **and what was
never planted.** Silence about a surface is not a clean bill on it (`self_review.md` §4).

---

## 4 · WHAT THIS ACTIVITY CANNOT DO — say it in the report, every time

- **It is a SAMPLE, never coverage.** Each CAUGHT covers one defect. A suite that catches five
  planted defects has caught five planted defects.
- **It cannot see a flaky suite.** One baseline run, one patched run: a suite that fails
  intermittently produces CAUGHT by luck, and nothing here distinguishes that from a real catch.
- **It cannot rank the holes.** Whether an unenforced claim matters is a question about the
  programme, not about the checks.

---

## 5 · MEASURED, ON THIS APPARATUS'S OWN GATE (2026-09-23)

Four sabotages against `check_records.py`, chosen against four of its own named claims: a
hand-edited role pack **caught** · a hand-edited published skill **caught** · a manual marked
present that does not exist **caught** · **a document declaring the WRONG diet class MISSED.**

**That last one is the demonstration that matters**, and not because it was a surprise: it is a
blind spot this apparatus had written down and pinned by hand that same morning — *the gate checks
that a class is DECLARED, not that it is right.* **The audit found it independently, from the
outside, by breaking things.** A practice that rediscovers a known hole without being told where to
look is one you can point at an unknown suite.
