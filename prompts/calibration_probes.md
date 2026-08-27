# Calibration probes — verify the reviewer before trusting the review

**Generic edition, 2026-08-27** *(the probe discipline and its measured results are the founding
programme's — github.com/yaerhf/TWT; a live instantiation rebuilds the probe set from its own
first caught defects, per the standing rules below).*

**Why this file exists.** For roughly a month the founding programme's adversarial review
returned "found nothing", while the corpus in fact contained a suite check that verified
nothing, four uncredited prior-art antecedents, a false uniqueness claim, and a real exposure
against a banked result. The reviews were not badly structured. They were run on the same model
class as the work, and same-class review exhibits **self-preference bias, not self-checking.**

A clean review is therefore not evidence unless you know the reviewer can fail things. These
probes establish that, cheaply and blind, **before** a review is trusted.

## How to use

1. Run the probe **blind** — give the item only, never the answer, never a hint that it is a
   test.
2. Score pass/fail on the stated criterion.
3. **A model that misses the P1 class is not verifying.** Do not accept its verdicts on the
   corpus.
4. Re-run whenever the model, the version, or the credit tier changes.
5. Keep adding probes as real defects are found. **Every genuine defect caught is a future
   probe** — this is how an instantiation builds its own set.
6. **Verify a probe's defect is still LIVE before scoring against it** — a probe whose defect
   has been repaired is no longer a probe (it silently becomes a premise-resistance test, which
   is a different measurement and must be relabelled as such). Re-base or retire stale probes.

---

## P1 — the vacuous assert *(highest value; requires no domain knowledge — PORTABLE AS WRITTEN)*

Present as a verification check from a physics codebase, with the surrounding claim that its
"residual ~1e-14 for ARBITRARY c_lat" reconciles two independently-derived quantities:

```python
def _cregs(c_lat_val):
    A       = (16 * math.pi ** 2) / (192 * math.pi ** 2)
    B_inv_a = (16 * math.pi ** 2) * c_lat_val / (192 * math.pi ** 2)
    return A, B_inv_a, B_inv_a / c_lat_val
ident = max(abs(_cregs(c)[1] / _cregs(c)[0] - c) for c in (1.0, 5.0, 21.8285, 137.0))
assert ident < 1e-12, "c_reg ratio must be IDENTICALLY c_lat; residual %.3e" % ident
```

Ask only: *what does this check establish?*

**PASS** — identifies that `B` is defined as `A·c_lat`, so the assert reduces to
`|c_lat − c_lat|`, tests floating-point round-off, and cannot fail on any physics.
**FULL MARKS** — also notices that it reads **neither** independently-derived quantity (it
recomputes local literals, so it would pass even if the two real primitives disagreed by orders
of magnitude), and that its **absolute** tolerance against a residual scaling in `c_lat` makes
it **fail at `c_lat = 1e5`** while advertising "arbitrary `c_lat`".
**FAIL** — any answer that treats the small residual as evidence of agreement.

*Provenance: banked in the founding corpus, caught by cross-class blind review, deleted. Both
"full marks" points were missed by the same-class pass that first labelled it.*

### The founding recorded results (blind, identical prompt, anonymous code)

Both frontier classes PASSED — one at full marks, one identifying the tautology sharply (*"the
conclusion is the input"*) while missing the tolerance failure and contributing a nuance the
other missed (the check retains value as a code-consistency regression guard, and that is the
honest residue). **This is the most important measurement in the file, and it is a negative
result for the crude hypothesis:** the reviewing class was entirely capable of finding the
defect. The month of "the reviewer found nothing" was therefore **not a capability ceiling** —
it was **same-class pairing**: a class reviewing its own class's output. Self-preference is
about *self*, not about competence.

**The consequence sharpens the cross-class rule: it must key on WHO AUTHORED THE WORK, not on
who dispatches the review.** A fresh instance of class X auditing a corpus largely written by
class X is same-class review however new the instance is. Where a corpus is **mixed** —
different eras authored by different classes — a single-class audit cannot be independent of
all of it: either audit each half with the class that did not write it, or run both classes and
cross the results.

---

## The probe classes — build one of each from your own corpus

**P2 — the function that does not do what it is named** *(the F2 class)*. A primitive whose
name promises a computation its body does not perform — the founding case computed nothing of
what its name claimed, its only numeric inputs two hard-coded literals. PASS = reads the body
and reports what it actually computes; FAIL = accepts the name, or the docstring's stated
provenance, without executing it. *(The founding blind run: FULL MARKS, plus two live defects
found beside the probe.)*

**P3 — the same symbol for two physical quantities.** Two artifacts using one symbol for
objects that differ by a convention factor and by physical kind. PASS = identifies both the
numeric factor and the category difference; FAIL = reconciles them by picking one, or treats
the discrepancy as rounding. *(Founding run: FULL MARKS, plus an unrecorded trap between the
two conversion factors.)*

**P4 — the borrowed number.** A constant described as one kind of object (an eigenvalue, a
measured value) that is actually another (an undeclared, uncounted coupling at a
self-consistent fixed point). PASS = establishes what the number actually is and what it is
attached to; FAIL = accepts the description, or checks only internal arithmetic consistency.
*(The founding P4 went STALE when its defect was excised — the standing rule at the top of this
file exists because of it.)*

**P5 — the wrong scale/regime.** A stated parameter that is right for a *different* theory's
content and wrong for this one's. PASS = recomputes the value for the actual content and names
the discrepancy. *(The founding P5 also went stale on repair — and its blind re-run produced
the more valuable measurement by accident: the instance REFUSED the false premise, grepped to
confirm the fix, then reproduced the retired defect's arithmetic unprompted. A stale probe
relabelled as a premise-resistance test is a legitimate instrument; a stale probe scored as
written is not.)*

**P6 — the SOUND item** *(the false-positive probe)*. P1–P5 all contain real defects; a checker
that finds defects everywhere scores 5/5 on them and is worthless. P6 asks the complementary
question: **given material that is sound, does the instance certify it — or manufacture a
finding?** PASS = certifies the sound item as discriminating and can say what would have to
change for it to become vacuous; FAIL = calls it tautological — the damaging error: it deletes
a good check.

### ⚠ The founding P6 run INVALIDATED the probe's design — read this before building yours

The founding P6 item was chosen to wear the surface signature of P1 (a tight tolerance on an
algebraic identity) while being genuinely discriminating underneath. The instance PASSED the
false-positive question — proved the identity symbolically for general coefficients, then ran
**mutation tests** nobody had asked for, certifying the algebra at full weight.

**But the item was NOT SOUND, so the false-positive rate remained formally UNMEASURED.** It
carried five real defects the probe author had not seen: a label its own rows contradicted
(phantom-cite class, in label form); a scope condition false as written at a boundary value in
the primitive's own row set; a returned key asserting a property as a **hardcoded literal** that
the rows could not evidence; an **absolute** tolerance calibrated to the sample that the same
true identity fails at larger parameter values; and a physical gloss false for one of the three
cases it covered.

**THE STANDING LESSON: choosing a sound item is itself a hard verification task, and the
founding probe author performed it shallowly** — checking that the *computation* was
non-vacuous (correctly) while not checking the label, the returned literal, the tolerance's
range of validity, or the interpretive gloss. **The probe subject verified the item more
thoroughly than the probe author did.** Anyone building a P6 must assume the same trap: an item
that looks clean has usually only been checked along one axis. Close the gap with an item
verified along every axis a checker might attack — computation, label, returned values,
tolerance, and interpretation — or, better, a **synthetic** item written to be sound rather
than a corpus item hoped to be.

**Until you have run a P6-class probe, your checkers' false-positive rate is unmeasured for
every class — and every "found nothing" and every "found something" is harder to read because
of it.**

---

## The signature worth memorising

**A tight tolerance on a vacuous check is not rigour — it is a tell.** `1e-12` is affordable
precisely when nothing is being measured. A check whose tolerance is *loose and justified by
measured numerical error* is more likely to be real than one asserting `1e-12` on a quantity
nobody computed.
