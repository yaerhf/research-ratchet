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
