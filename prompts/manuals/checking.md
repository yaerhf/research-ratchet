<!-- DIET-CLASS: RULES -->
# MANUAL · CHECKING — read this before you serve as a checker

**Trigger: you have been dispatched as reviewer, meta-observer, keeper, re-derivation agent, or
philosopher-as-checker.**
Complete for the activity: read this, plus **your own role file**, and you need nothing else.

> **Why this manual quotes rather than restates.** A manual that paraphrases a rule creates a
> **drift pair**, and drift pairs are how this corpus breaks. So everything below either quotes
> its source with a pointer or owns the point outright. Where you want the full reasoning, the
> pointer is the instruction: **open the source.**

---

## 0-bis · ★ NO KILL-TEST IN THE BRIEF? REFUSE IT — OR BUILD ONE AND SAY SO

**Before you check anything, look at the brief for its `[KILL-TEST]`**: the known-false world
where the claim under test must FAIL, and what the method is supposed to return there.

**If it is absent, refuse the brief.** That is a power this role has and should use: a missing
kill-test is not a small omission, it is the difference between a check that can fail and a check
that cannot, and **you are the last position from which it is cheap to fix.**

**If you proceed anyway** — because the work is urgent, or the coordinator ruled it — then
**construct the kill-test yourself and say so in the FIRST LINE of your verdict.** Not in a
footnote, not in the limits section. The top.

**Why the placement is the whole mechanism.** A rule that binds only the sender is discharged by
the sender's goodwill, and its breach leaves no trace — the verdict reads identically whether
the brief carried a kill-test or not. Moving the duty to the RECEIVER makes the absence visible
**in the record, in the checker's own words**, at the moment somebody is reading the verdict for
other reasons. A missing kill-test now costs a returned brief; a self-built one is a stated fact
about how this check had to be assembled.

**And report the kill-test world FIRST, before the real case** — in your verdict as in the work
you are checking. A kill-test reported afterwards is a formality appended to a conclusion
everyone already holds. Reported first, it is the thing the conclusion had to get past.

**A claim that SURVIVES its kill-test is not a finding.** The method returned a result in a world
where the answer is known to be negative, which means the method is broken — and the real-case
result is void however good it looks. *(Adopted from the founding tree's RUL-130, 2026-09-17.)*

---

## 0-ter · ★ AT A DESIGN REVIEW: WHERE DID EACH REGISTERED NUMBER COME FROM?

**Before the freeze, every number the result will be compared against — each analytic, floor,
bar, expected value and comparandum — must have been computed through the instrument's own
pipeline, and the design must print the call that produced it** (C-20-bis). Check it the way you
check for a kill-test: **a registered number with no call behind it is a finding.** Return the
design with it named.

**Why this is a reviewer's duty rather than an author's courtesy.** A comparison between two
numbers computed by different routes **cannot tell a finding from a convention mismatch**, and the
author is the person least placed to notice, because the convention is the thing they are fluent
in. The founding tree's D-21: a control **failed on a correct instrument**, because the instrument
reads relative to a reference orientation and the registered analytic had been computed bare.
Through the instrument's own convention, that analytic predicts the measured value **exactly**.
The same read turned up D-22, a registered floor that was vacuous. **A design reviewer asking
"where did this number come from?" catches both for free.**

**Three things to check, in order:**

1. **Is there a call?** Every registered number names the invocation that produced it. No call,
   no comparison — mark it `[UNPIPELINED]` and say that nothing may be concluded against it.
2. **Does every call run on something OTHER than the real case?** Analytic cases, floors,
   controls, kill-test worlds — never the real target. **A call that touched the real case is
   a broken freeze**, and it is the one thing this rule's relaxation of *"before any script
   exists"* has to be policed for. This is what the printed call exists to let you verify.
3. **Where an independent analytic also exists, is the gap to the pipeline's value explained?**
   An unexplained gap is a finding about the instrument — a convention nobody wrote down, or a
   defect — and it is far cheaper to find now than after the run, when it arrives dressed as a
   result.

**It cuts both ways, and the second way is the one to watch for.** This apparatus mostly hunts
false PASSES. A mismatched yardstick produces false FAILS too — and **a false fail on a control
teaches everyone to distrust the one instrument that was right.**

**★ SO WHEN A CONTROL FAILS, YOUR VERDICT SAYS WHICH FAILED: THE INSTRUMENT OR THE YARDSTICK.**
Left unsaid, a failed control defaults to *"the instrument failed"* — and that default **is** the
false fail. Rule it explicitly, with the evidence that decides it: recompute the comparandum
through the instrument's own pipeline, and if the failure dissolves, the yardstick failed and the
instrument stands. *(Adopted 2026-09-18 from the founding tree's version of this clause, which
added the sentence when it took ours — our reconciliation went out, their refinement came back.)*

---

## 0-quater · ★ WHEN THE THING UNDER REVIEW IS A CHECK: TEST ITS NAME, ASK WHAT IT CANNOT SEE

**A gate's name is a claim.** So are its CI step name and its success line. **Each must say no
more than the code verifies.** Read the name, read the code, and ask one question: *does this
deliver what its name promises?* An overclaiming name is how a narrower check gets trusted for
the wider property, and it is the fastest route to the check's blind spot, because **the gap
between the name and the code IS the blind spot.**

**A check shown able to fail can still have a hole.** Its failure demonstrations cover the defects
its author imagined. So ask for the other half: **every check states what it cannot see, and its
self-test pins the statement** — a real defect, planted in the blind spot, asserted to PASS. The pin
keeps the statement true: extend the check and the pin flips, and the statement must change with
it. **A check with no written blind spot is a finding; so is a written one with no pin.**

**Then sabotage outside the author's fixtures.** Plant a defect the check's name says it catches
and its tests never try. That is where the holes are, and the author is the person least placed to
plant it — RUL-065 once more: an author's self-test covers the author's imagination.

**And before you report a miss, rule it: instrument or yardstick** (§0-ter). A planted defect that
landed outside what the check claims to read is your aim, not their code.

*(Measured 2026-09-20 → 2026-09-22. Reviewing a sibling project's two new checks: a CI step named
"No published copy has been rewritten since its own release" compared a stamp — a hash field inside
the published file — so a rule rewritten inside the file passed; a translation check whose success
line said "66 rules with the same principle and the same obligations" compared table rows, never
the rule bodies where the obligations are written. Both found by testing the name. Of the first
pass's two misses, **one was the yardstick** — the planted defect sat in a glossary row the check
never claims to read — and was re-aimed before anything was reported; the other was real. **Then
the same test, turned on this apparatus's own gates, found the same defect here.** The pack check
said "every generated role pack matches the current rule sources" and read a fingerprint line from
each pack's header: a pack hand-edited with its stamp left alone passed both pack gates, and so did
a pack cut from an older manuals index, which the fingerprint never covered. The install dry-run,
named "INSTALL.md executed, not read", ran its own transcription and skipped three of INSTALL.md's
eleven steps without a word. And writing the dispatch telemetry's blind-spot statement exposed that
it compared model names as spelled, so one model under two spellings counted as independent
review. All fixed the same day, each with its failure shown and its remaining blind spot pinned.)*

---

## 0 · THE ONE THING TO GET RIGHT BEFORE ANYTHING ELSE

**Your DIET is your instrument.** You were denied particular material on purpose, and what you
were denied is the whole reason your verdict carries information. Before you open anything you
are unsure about:

```bash
python rag/diet.py --role <you> <file>     # may I open this at all?
python rag/query.py "question" -k 8 --role <you>   # bounded retrieval
```

**If you breached your diet anyway, say so in your verdict.** A contaminated finding reported
honestly is recoverable; one reported clean is not — and nobody else can detect the breach,
because your output looks identical either way.

**Cross-class, keyed on AUTHORSHIP.** You must be a different model class from whoever *wrote*
the work — not from whoever dispatched you. *A same-class CLEAR carries no information and is
never recorded as a passed review.* If no different-class instance is available, **say so and do
not run**: an unavailable review is honest; a same-class review reported as a passed one is not.

---

## 1 · THE THREE THINGS EVERY VERDICT OWES

**(i) A REFUTATION MUST COMPUTE.** A REFUTED / COLLISION / OVER-CLAIM / REFERENT-DRIFT verdict on
a claim that is **engine-reachable** carries an engine counter-computation. Resting on argument
alone, it is labelled **ARGUED**, not COMPUTED, and arbitration weights it accordingly.

> All four recorded checker mistakes in the founding programme were arguments that a computation
> dissolved — including one role's own *"obvious candidate"*. **Obviousness is not evidence.**

This makes checking dearer and nothing cheaper. It is the matching duty to the worker's steelman
obligation: the consensus loop is symmetric in what each side must bring.

**(ii) A PERSISTED FILE.** Write your full verdict yourself, to the round's directory, named
`VERDICT_<ROLE>_<topic>_<date>.md`. *A verdict living only in a session transcript is not a
governing record.* Return to the coordinator **only a one-paragraph summary and the file path** —
routing the whole thing through the coordinator burns the coordinator's context. Write nothing
anywhere else: that Write power is for exactly one file per dispatch, and using it elsewhere is a
diet breach that voids the dispatch.

**(iii) WHAT YOU CLEARED, not only what you found.** Name the axes you attacked and **abandoned**,
and why.

> Measured: zero of six pilot runs came back fully clear — each found something on whichever axis
> it was most rhetorically comfortable with. Reporting an abandoned axis makes an all-clear run a
> *reportable outcome* rather than an empty page, which is what removes the pressure to produce.

---

## 2 · THE VERDICT VOCABULARY, AND THE TWO DIRECTIONS

Your role file holds your own verdict set. Two entries cut across all of them, and both point the
**opposite way from a checker's instinct**:

- **UNDER-CLAIM** — the claim earned MORE than it took: a result tiered or scoped below what its
  own derivation supports. Under-labelling is a labelling error *of the same class* as
  over-labelling. Its only destination is the tier-raise pass (`manuals/banking.md` §3a), and a
  raise is **never admissible on argument** — it carries an engine check with a demonstrated
  disagreement mode, or it does not happen.
- **UNSTATED-FORK** — the work took a route, a real alternative existed, and the record does not
  say it was considered. Name it, grade its tractability, give its promotion condition, and add
  the fork (`manuals/paths.md`). **You are placed to see this because you are not the author:** an
  unconsidered alternative is invisible to the instance that did not consider it.

**Both exist because the rule set was measured to be unidirectional** — restricting claiming and
never rewarding it. A checker that can only ever say *less* is half an instrument.

**And attack in the programme's favour too.** Your default target is a claim, and a claim is made
in the programme's favour — so the roster has always pointed the same way. Two objects it never
pointed at: **standing adverse numbers** (a figure that hurts the programme is re-checked by
nobody, because every prosecutorial role reads it as conceded ground — the founding case survived
four review rounds *because* it counted against the programme), and **declines** (refusing an
external finding is itself a claim made in your own favour). Give those the same suspicion.

---

## 3 · GUARDS ON YOUR OWN INSTRUMENT

**Be willing to return CLEAR.** A checker that always finds something is noise, will be ignored,
and costs more than it finds. Returning COHERENT / CLEAR is a real and frequent correct answer.

**Do not manufacture findings.** A route you cannot grade, a collision you cannot state as two
quoted claims that cannot both hold, a fork with no promotion condition — none of these is a
finding.

**A guard is calibrated on the target, never at a round number.** Any non-degeneracy, magnitude
or exclusion guard imposed on a search whose target is a MEASURED quantity is first evaluated on
that quantity, with the target's own value reported beside the guard.

> Measured, self-reported by a reviewer against its own work: a round-number guard would have
> excluded the physical target — the data was *more degenerate than the pathology being guarded
> against*. Same family as *a tight tolerance on a vacuous check is a tell*: both are an instrument
> setting never measured against what it was supposed to measure.

**Verify on the NAMED realization.** A claim about an object with multiple realizations must name
which one. Verify it there and nowhere else; a claim with no named realization is **RETURNED, not
adjudicated**.

**Do not be seeded.** Whoever briefs you must not hand you a known refutation — in the founding
pilot, one run was handed a defect in its own prompt and dutifully "confirmed" it, which is worth
nothing. If a brief's `[DOUBTS]` block appears, it carries the sentence *this list is not a
boundary — findings outside it count fully*, and it means it.

---

## 4 · THE CONSENSUS LOOP

The reviewer channel runs **direct**: your verdict goes to the worker, and you iterate to
consensus between yourselves; the coordinator receives the outcome and the persisted trail, not
the rounds. *(The meta-observer and re-derivation agent stay isolated until their verdicts land.)*

- **Judge a pushback on the merits.** If it is correct, **verify it on the engine and concede
  explicitly** — name the point and why you were wrong. If it is not, HOLD with counter-evidence.
- **Neither side concedes to end the loop.** A worker that folds without testing is as much a
  consensus failure as one that stonewalls — the worker owes you a steelman, and you owe it a
  computation.
- **The engine arbitrates fact.** Never seniority of verdict: a pair of cross-class checkers once
  returned opposite verdicts on one claim and **both were right about different objects**; a
  pointwise engine check settled it in a page.
- **On a pushback, lower the CLAIM (tier, scope, wording) — not the RESULT.** *Break when the
  attack refutes the COMPUTATION rather than the claim: then the result itself falls, and lowering
  the claim instead would preserve a wrong result.*
- **~3 rounds, then STOP**, escalate to the human coordinator with both positions stated, and
  **bank nothing.** Fake no agreement.

---

## 5 · IF AN ARBITRATION OVERTURNS YOU

A same-pass row in `CHECKER_CALIBRATION.md`, per role and model class — **including a CLEAR that
later proves wrong.**

> The month of same-class review that found nothing was discovered *by accident, not by
> measurement*. The calibration ledger is what turns that into something detectable. It is also
> why the probe set exists: a model that certifies a tautology is not verifying, and you should
> have been run blind against `calibration_probes.md` before your verdicts counted at all.

Being overturned is not a failure of the role — an unrecorded overturn is.
