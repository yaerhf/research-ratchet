<!-- DIET-CLASS: VERDICT -->
# W8 DESIGN REVIEW — the verdict, as received

**Reviewed:** `audit/W8_DESIGN_FOR_REVIEW_2026-09-17.md` (v1) and the repository's own W8 docket
entry, README and C-37 text.
**Reviewer:** external, outside the apparatus, no write access.
**Date:** 2026-09-17. **Kept verbatim.**

**Handling:** same fence as the package it reviews — it establishes that a known-answer target
exists, so **it must never reach an instance under test.**

---

> I read the package against the repository's own docket entry for W8 (WORKLIST.md), the README,
> and the C-37 text in W14. Answering the three questions as posed, and holding to §8: nothing
> below proposes a replacement design, and nothing touches the target.
>
> ## 1 · Can this design fail?
>
> Partly. The kill-tests are real in intent but not yet real in form, because neither states a
> magnitude.
>
> **(a) The identical pair** says the measurement "must show no improvement." Two runs of a
> stochastic system will never score identically, so as written the test either fails trivially
> (any nonzero difference) or is read charitably and cannot fail. A correct version has to
> declare, before either run, what difference counts as "improvement" — and then that same number
> becomes the minimum detectable effect for every real ranking, which with one pair at rung 0 may
> be large enough to swallow the effect W8 hopes to see. There is a second way (a) passes
> vacuously: if both runs of the current apparatus fail the target outright, both score at
> maximum distance, agree perfectly, and tell you nothing. (a) is only informative at a rung
> where the score has variance.
>
> **(b) The degraded apparatus** has a confound in the score itself. The score is distance *and*
> time. Degrading the apparatus removes ceremony, which removes time. A broken version can
> therefore score *better* on one component while worse on the other, and if the rule for
> combining the two is settled after the result, (b) can always be explained. The combination
> rule has to be fixed before (b) runs. Separately, the degradation is chosen by the author as
> one "we believe matters" — that selects for the outcome. A test with only expected-to-fail
> degradations cannot be surprised; a correct one would need at least one pre-registered
> degradation *expected not to matter*, so both directions of the instrument are exercised.
>
> **The failure criterion "any instance found to have held the key."** The `WITHHELD` diet class
> stops file opens. It does not address training data, and "recent enough that the literature has
> not absorbed it" is a belief about model classes that nothing in the design tests per class
> before the run. The bare arm measures this only indirectly and only after budget is spent.
>
> ## 2 · Does it answer the question asked?
>
> Not quite, and the gap is in a place the package does not name.
>
> The declared question is *does this apparatus make research better*. The run measures *does
> version n+1 reach one known result closer and faster than version n*. §9 concedes the
> construct-validity distance honestly, so I will not spend words there. The unnamed gap is
> upstream: **who writes the modification instructions?** §2.5 says the modifier works "from
> written instructions"; the docket says the scorer "writes no apparatus text"; nobody is
> assigned to author them. Every candidate author — the human, the scorer — holds the key. The
> design fences the *score number* ("filed before score seen"), but an instruction-writer who has
> read run *n*'s trace, and who knows the ideal path, can see exactly where the run diverged from
> it. A general-sounding instruction selected on that knowledge passes the third-party "would
> this hold in any field?" check and still carries direction. The fence covers the number and
> leaves the trace open. Until instruction authorship is a named role with a declared diet, the
> intervention W8 is ranking is partly authored by the key.
>
> A related question the package should answer explicitly: what does the *modifier* see of run
> *n*? If it reads the transcript, its §1 declaration ("I have not read the target's
> mathematics") is true only for iteration one.
>
> Also: time as a score component answers "is the apparatus cheap" alongside "is it better," and
> it structurally rewards stripping the redundancy W1 explicitly protects. A version that quietly
> drops a checker gets faster. The package should say whether that outcome is a win or the
> divergence tripwire.
>
> ## 3 · What will it miss?
>
> **Mid-run human rulings.** The apparatus, by its own map, requires a human to rule what
> coherence cannot decide. The frozen fixture constrains the founding conversation only. Every
> ruling, ratification and push during the run is a live channel from the key-holder into the
> tree, and it is neither scripted nor listed among the controls. Either the human rules (a leak
> the design does not see) or the run is human-free (not the apparatus as drawn, and that should
> be a stated limit).
>
> **The docket itself.** The package's §0 fence protects the package. But the W8 entry in the
> toolkit's WORKLIST.md states that a known-answer problem is being run blind, describes the
> fence, and pointers to the package. If the installed tree carries the toolkit's docket, or an
> instance under test can reach it, the fence is describing the thing it hides. Whether
> `WITHHELD` covers WORKLIST.md and HANDOFF.md is not stated and needs to be.
>
> **Alternative valid routes.** "Distance from the ideal path" presumes one path. The
> re-derivation agent's whole value in this apparatus is that a *different* route is worth more.
> A run reaching the result by a route the scorer did not anticipate has no defined score.
>
> **Model drift between versions.** Versions *n* and *n+1* run at different times against
> externally updated models. W10's dispatch log records which model was named, not which weights
> ran. A ranking cannot separate the apparatus change from the provider's.
>
> **Honest failure.** The docket's "what to measure besides the headline" list (did checkers
> compute, did the death trigger fire) is not in the package's scoring. A well-recorded failure
> and a badly-recorded one score the same on distance, and that is precisely the difference the
> apparatus claims to make.
>
> ---
>
> None of this is "is it good." The design can be made falsifiable by stating three numbers and
> one role before anything runs; as submitted, it cannot yet be broken because it has not yet
> said what breaking it looks like.

---

## ADJUDICATION — 2026-09-17, by the design's author

**All twelve findings CONFIRMED. None withdrawn, none downgraded.** Two were already known to
the author and are credited as independent confirmations rather than as new: the docket leak
(found the same afternoon, before the verdict returned) and the construct-validity distance
(§9 of the package, which the reviewer correctly declined to spend words on).

**The sharpest is Q2's: instruction authorship was never assigned to anybody.** The role split
had two seats — scorer and modifier — and a third function sitting between them that nobody
held. *The fence covers the number and leaves the trace open* is exactly right, and it is the
same defect class as the one this apparatus was caught in twice this month: a separation
asserted at the place it is easy to assert, and left open at the place it actually leaks.

**The verdict's closing sentence is the operative one** — *it cannot yet be broken because it
has not yet said what breaking it looks like.* The v2 design answers it with three
pre-registered numbers and one new role; see `W8_DESIGN_FOR_REVIEW_2026-09-17.md` §0-bis for
what changed and why.

**On method:** the reviewer held §8 exactly — no replacement design was proposed anywhere, and
the target was never touched. Every finding names what is wrong and what a correct component
would have to satisfy, which is what makes the design still the author's to fix. *That is the
first end-to-end demonstration that C-37's reviewer discipline survives contact with a reviewer
who had plenty to say.*
