# MANUAL · THE ENGINE — read this before you build or extend one

**Trigger: you are about to write the programme's first executable primitive, add one, or
decide whether the programme needs an engine at all.**
Complete for the activity: read this and you need nothing else to build one correctly.

> **The design statement, from the founding programme's human coordinator (2026-08-27):**
> *"What was good with it was that it delivered **self-coherence as an executable**."*
>
> That sentence is the whole manual. Everything below serves it.

---

## 1 · WHAT AN ENGINE IS — and what it is not

An engine is **the programme's claims rendered as running code, so that the corpus's
self-coherence is a property a machine can check rather than a matter anyone has to be trusted
about.**

It is **not**:

- **not a simulation** — a simulation explores what a model does; an engine asserts what the
  programme *claims*, and fails when the claims disagree with each other or with the data;
- **not a test suite for the code** — the harness tests the engine, but the engine's subject is
  the *research*, not the software;
- **not a toy model** — a toy illustrates; an engine arbitrates. (The founding programme's
  no-toy rule is exactly this line: conclusions come from the full-fidelity object, never from
  the anchor that was built to calibrate it.)

**What it buys you, concretely — three things nothing else in the apparatus supplies:**

1. **AN ARBITER.** *On any conflict between prose and the engine, the engine wins* (C-16). This
   is what ends otherwise unresolvable disputes. The founding measured case: two cross-class
   checkers returned **opposite verdicts** on one claim and **both were right about different
   objects**; a pointwise engine check settled it in a page. Without an engine, that argument
   runs until someone gets tired, and the tired party is not reliably the wrong one.
2. **REFUTATIONS THAT COMPUTE.** A checker's REFUTED / COLLISION / OVER-CLAIM verdict on an
   engine-reachable claim must carry a counter-**computation**, or it is labeled ARGUED and
   weighted lower (C-16's check-block extension). All four recorded founding checker mistakes
   were arguments a computation dissolved. **Without an engine every verdict is ARGUED, and
   arbitration has no ground to stand on** — the review layer loses most of its teeth.
3. **CLAIMS YOU CANNOT ACCIDENTALLY OVERSTATE.** A quantity the programme has not earned
   **raises** instead of returning a number (§4). You cannot quote what will not compute.

---

## 2 · IS IT RELEVANT HERE? — the question is narrower than "is my field computational"

**Ask: does any claim in this programme have content a machine could check?** Not *is the
subject mathematical* — the founding programme was theoretical physics, but the engine's real
subject was **its own bookkeeping about what it had proved**. That generalizes much further
than people expect. An engine is available wherever the corpus asserts any of:

| the programme asserts… | the engine renders it as… |
|---|---|
| an exact identity or algebraic relation | a symbolic check that fails if either side moves |
| a numerical value or bound | a computed value + a tolerance **that could fail** |
| *"the options are exactly these"* | an **enumeration** — C-32 makes a menu closure a theorem, and an argued closure closes nothing |
| a dependency or entailment structure | a graph the corpus declares, checked for cycles, orphans, and broken edges |
| a definition used in many places | one definition, one site, everything else derived from it — so a redefinition breaks loudly |
| counts, tiers, premise budgets | a census that recomputes them from the tree instead of trusting prose |
| a claimed empirical agreement | the comparison, run, with the disagreement mode exhibited |

**If none of those apply, say so in the canon and mean it** — but check the second column
first, because the last three rows are available to *almost any* programme, including a purely
literature-based one. And note the shadow instrument: the **reductions ledger** (*if antecedent
A holds, then C1…Cn follow, by proof P*) is an engine of implications for programmes whose
content resists code — with the same bar, that the implication is **proved, not asserted**.

**The measured reason to lean toward building one:** *a paper-only derivation can be not merely
unchecked but VACUOUS* (PAPER rule 155). The founding case was a stated requirement that, once
someone tried to write it down as a computation, turned out to constrain **nothing at all** in
the formalism it was written in. Prose cannot detect that about itself.

**The coordinator's standing duty:** when a docket item's claim is engine-reachable and no
primitive covers it, **propose the primitive in the brief** — and when the programme has no
engine at all and the table above says it could, that is a docket item, not a preference.

---

## 3 · THE THREE PROPERTIES THAT MADE THE FOUNDING ENGINE WORK

Copy these; they are why a hostile reader could be handed the thing and come back convinced.

**(i) IT COMPUTES; IT DOES NOT STORE.** A primitive that returns a stored literal proves
nothing — it is a number wearing a function's clothes. The founding engine's showcase check
computes a lattice-theoretic property *and the same call reports the contrasting value for the
structure where that property fails* — so the reader sees the discriminator, not the claim.
**Corollary — the referent rule (F2):** the name must survive contact with the body. The
founding failure: a function named for a topological computation whose only numeric inputs were
two hard-coded literals.

**(ii) IT REFUSES.** Quantities whose magnitude waits on an unbuilt piece of the theory are
wired to **raise**, not to return a plausible number:

```python
class GatedError(RuntimeError):
    """The programme has not earned this number yet. Raised, never returned."""

class UnderivedError(RuntimeError):
    """Structurally unbuilt — distinct from gap-gated. Keep the two apart (rule 41)."""
```

**Write the gate list BEFORE the values.** A gate added after the value exists is a gate built
*around* the value. And keep every gate reachable: the founding apparatus test found that of
five raising gates, **four fired under sabotage and one was unreachable because its
configuration was never constructed** — while both suites stayed green. An unreachable gate
guards nothing and reads as protection.

**(iii) IT SHIPS THE PLACE IT IS LOSING.** Return the honest tier and the conditioning *beside*
the number, in the same returned object — so a restatement elsewhere cannot quietly drop them
(the hedge-loss failure, FORMATION_CORE §2). The founding engine returns, in the same dict as
its headline number, the fact that the naive value is *"NOT a prediction"* plus its exclusion
split by conditioning. **No crank leads with its own worst result** — which is precisely why
doing so is load-bearing evidence, and it costs one dict key.

---

## 4 · HOW TO BUILD THE FIRST ONE

1. **Start with the smallest claim that can FAIL — never the headline.** The headline is the
   claim you are least able to see clearly; the first primitive exists to prove the *apparatus*
   works, not the theory.
2. **Write the gate list.** Every quantity the programme cannot yet earn, wired to raise, with
   the gate's reason in its message. This is the honest map of the programme's own edge, and it
   is cheapest to draw before there is anything to protect.
3. **Then the first computing primitive**, with its docstring carrying its **premises, its
   tier, and its conditioning** — because *read the row before you reuse it* (C-18) puts the
   docstring in the load-bearing path: an agent's whole basis for reusing your primitive is
   what you wrote there. The founding cost of skipping that read: two probes, against a
   docstring that warned verbatim against the exact conflation used.
4. **Then its check, in the harness — and ship the check with its DEMONSTRATED FAILURE MODE.**
   Run it against the broken state, show it exits non-zero *for the named reason*, then fix and
   show it pass. **A check never shown able to fail is a phantom-cite of the gate class**
   (`banking.md` §3). Negative-testing ten new founding checks found two defects **in the new
   checks themselves**.
5. **Make the check DISCRIMINATING, or record why none exists** (RUL-067). *"No discriminating
   check is possible here because…"* is a complete and acceptable answer — and a better one
   than a green tautology. **Before writing any check, ask the standing question: what could
   have DISAGREED?**
6. **Bank it** — `manuals/banking.md`. Never write "engine-verified" for something not yet in
   both the source and the suite (C-17): the suite does not check prose, so a phantom cite
   passes every gate and is still a disguise.

---

## 5 · STRUCTURE — two splits, and the rule for choosing a file

Adopt both from the start; retrofitting them is expensive.

- **MAIN never calls COMPANION.** The main engine is the spine; the companion holds auxiliary,
  exploratory or downstream machinery. One-way dependence keeps the spine's integrity
  independent of the periphery's churn.
- **CORE never consumes CANDIDATE.** Family-level results must not depend on instance-level
  picks, or the family's claims silently inherit one candidate's choices. In the founding tree
  the main module is a pure import **façade** over a core module and a candidate module, with
  an **AST guard in the harness** enforcing the split — so `import <engine>` is unchanged for
  every probe while the invariant is machine-checked.
- **Choose a new primitive's file by what it CONSUMES, not by where it feels foundational.**
  And if it is CORE while riding an entered datum or a posited premise, add its row to the
  core-provenance table in the same pass. **CORE is not a synonym for unconditional.**

**Retrieval note:** the index chunks code **per primitive**, so a primitive can be queried at a
fraction of the cost of reading the file (`rag/README.md`). Very long docstrings fragment
that — a cost of the docstring, not of the chunker.

---

## 6 · THE TRAPS — each one cost the founding programme real time

- **THE VACUOUS CHECK, wearing a tight tolerance.** `1e-12` is affordable precisely when
  nothing is being measured. The canonical specimen — an assertion whose two sides are the same
  expression by construction, so it tests floating-point division — is calibration probe P1
  (`calibration_probes.md`), and **it is the probe every checker must pass before its verdicts
  are trusted.**
- **THE VACUOUS DISCRIMINATOR.** Worse, because it wears an engine-exact coat: a founding
  worker "settled" a live question at maxdiff `0.0` — and a referee showed the *rival* reading
  produces the typographically identical formula in its own variable. **No possible corpus
  could have produced the disagreeing answer.** A discriminator needs a possible world where it
  fails, *exhibited*.
- **A VALUE AND ITS CHECK MOVE TOGETHER OR NOT AT ALL.** A rename moves prose, never returned
  values — harnesses may assert on returned strings, so renaming a value without its check
  breaks the suite, and renaming a description without its value manufactures a drift pair.
- **HAND-CHOSEN PROFILES ARE WITNESSES, NOT SOLUTIONS.** Quantitative claims need
  solver-produced inputs; a trial input may be quoted as a *bound*, labeled, never as the
  answer.
- **NEVER USE THE NORM OF A SMALL DIFFERENCE** as a verification metric where the engine prunes
  small coefficients — use coefficient-level max-difference, or any metric that cannot hide a
  difference below the pruning threshold.
- **NAME WHICH OBJECT YOU MEAN.** Where several distinct integrals, measures, costs or
  normalizations share a territory, say which is in play before quoting any law about it — this
  is the trap that produced the two-checkers-opposite-verdicts case in §1.

---

## 7 · WHAT THE ENGINE STILL DOES NOT GUARD — state this every time it is quoted

**The suites verify the mathematics, not the prose.** In the founding corpus, the bulk of
engine docstring content was prose no assert can express.

**And the gate machinery guards the door, not the wall.** It catches a gate that stopped
raising and a count that drifted. **It does not catch a *new* primitive that returns an
unearned number without touching any gate.** That remains a human duty — and it is precisely
the reason the §8a roles exist. An engine makes self-coherence executable; it does not make
honesty automatic.
