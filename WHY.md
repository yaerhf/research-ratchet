<!-- DIET-CLASS: PUBLIC -->
# What a year of running a research programme on AI agents actually taught us

*The design notes behind [research-ratchet](https://github.com/yaerhf/research-ratchet). Every
structure named here exists because something went wrong first. Where a claim has no measured
incident behind it, this document says so.*

---

## The problem is not capability

Agents are now cheap enough that a research programme can run mostly on them: they derive, they
check, they sweep the corpus, they read the literature. What becomes scarce is not intelligence.
It is **knowing which of the things they told you is true.**

That turns out to be a design problem with a specific shape, and the shape is measurable.

## The finding that reorganised everything

For about a month, the adversarial review in one programme came back **"found nothing."**

The corpus, in that same month, contained: a suite check that verified nothing, four uncredited
prior-art antecedents, a false uniqueness claim, a citation swapped at a headline sentence, and
an empirical exposure against a result banked eight commits earlier.

The obvious diagnosis is that the reviewing model was too weak. **It was not.** Run blind
against the same defect later, that same model class found it immediately and described it
sharply. The reviews were failing for a different reason: **the reviewer was the same model
class as the author.**

Self-preference is about *self*, not about competence. A fresh instance of a class auditing a
corpus that class largely wrote is not an independent check, however fresh the instance. So the
rule that came out of it keys on **who authored the work**, not on who dispatches the review —
and a same-class CLEAR is recorded as carrying no information at all.

That is the whole method in miniature: *a check you cannot show capable of failing is not
evidence.*

## The diet is the role

The second finding is stranger and more useful.

The recurring failure in that programme was never bad mathematics. It was **correct mathematics
pointed at the wrong thing** — a function whose name promised a topological computation while
its only numeric inputs were two hard-coded literals; a one-line trigonometric identity
described as "independent evidence at every multipartite n"; a result generalised from one of
six cases and false for the other five.

No reviewer reading the derivation catches those reliably, because the derivation is exactly
what captures your attention. So the apparatus adds a checker that is **starved of the
derivation** and given only the claim: *is this about what it says it is about?* It must write,
before opening anything, one plain sentence describing the physical situation for a competent
outsider — and if it cannot write that sentence from the claim alone, that is already the
finding.

Generalise: **every instrument here is defined by what it is deliberately denied.** The
reviewer is saturated with the derivation. The meta-observer is starved of it. The keeper is
saturated with the entire result set and is the only role permitted to conclude that *an old
banked result is the one that must give*. The philosopher is starved of our derivations and
saturated with the rivals. The external reviewer sees only the released artifact and owes the
programme nothing.

**Merging two of these does not tidy the system — it deletes a measurement.**

The sharpest case is the cheapest role in the building. A **re-derivation agent** receives a
claim's bare statement and nothing else: not the proof, not the probe files, not any verdict.
Its instruction is to prove the thing again from scratch. On its first dispatch it returned the
algebraically identical result by an independent route, **plus two upgrades nobody had** — a
sharper characterisation of the solution and a normalisation trap in the comparison. It found
more precisely *because* it could not follow anyone's path. It is also the only check that can
find a **missing** step, as opposed to a wrong one: a derivation with a gap reads as complete to
anyone tracing it, and the gap only shows when someone has to cross it unaided.

## Three cheap rules that paid for themselves

**A correct diagnosis does not license its cure.** Twice, a checker correctly identified a real
tension and proposed a repair that computation then refuted. The repair a trained model reaches
for is the *conventional* one — which, for a challenger framework, is frequently retreat to the
incumbent arriving as helpful advice. Diagnosis and cure are now priced separately, and adopting
a cure requires naming which forbidden move it would import.

**A tight tolerance on a vacuous check is a tell, not rigour.** `1e-12` is affordable precisely
when nothing is being measured. One check asserted that a ratio equalled a quantity *defined* as
that ratio; it passed at machine precision and could not fail on any physics. So every new check
now ships with a **demonstrated failure mode**: run it against the broken state, show it exit
non-zero for the named reason, then fix and show it pass.

**Never "impossible"; never "the only way."** Every dead end is recorded as *tried X → failed
because Y → **would change if Z***, and every necessity claim carries its conditioning class in
the same sentence. The escape hatch has been cashed repeatedly — an obstruction filed as a
negative was re-read twelve hours later as a *resource*, and became the brief that won.

## What the reviewers do to you, measured

Publishing into a world of AI referees has its own measurable regularities.

Two frontier model classes, independently, audited the challenger framework line-by-line against
a **one-phrase compression** of its established rivals — pricing the incumbents at the
familiarity discount. Both **retracted under a single challenge**, naming the error themselves:
*"incumbent amortization"*, *"rigged accounting."* A century of living with a debt makes it
invisible; it does not make it paid. The fix is not rhetoric — it is a symmetric ledger where
every line is itemised to equal depth on every framework, and a half-itemised ledger is treated
as a **void measurement**, not a partial one.

And a warning for anyone who thinks disclosure is free: the one paragraph a shipped note
nominated as its *"single most important honesty point"* was the one paragraph the cold expert
opened and closed on — and he was right, and the error ran in the paper's favour. **A flagged
caveat is a target designator.** It must therefore be the most-checked sentence in the document,
never the least: a caveat is a claim and inherits a claim's burden.

## The ratchet, and the part that cannot be automated

A ratchet moves one way and locks. Nothing enters the record except through gates — both test
suites green, the prose-about-the-tree checked against the tree, the retrieval index rebuilt,
the commit sweep-guarded. Every commitment is registered with a revert path, so knowledge can
move forward and be *deliberately* reversed, but cannot quietly regress or quietly inflate.

Then the honest part, which the apparatus states about itself in its own binding documents:
**roughly 85% of its rules have no mechanical enforcement, and every one of the four
banking-stoppers is in that set.** The suites verify the mathematics. Almost nothing verifies
that you followed the method.

**The method runs on you.** Which is why the rules are classified rather than merely listed: an
absolute rule you break silently is invisible, while a defeasible rule you break in the open
costs nothing — *a recorded, reasoned break is compliance.* Make breaking cheap to declare and
expensive to hide, and you get a record that reflects what actually happened.

The same honesty applies to what the machinery *cannot* do, established by deliberately breaking
things: of five raising gates, four fired under sabotage and one was unreachable because its
configuration was never constructed — and both suites stayed green throughout. Striking a row
out of the import registry broke nothing and warned nobody. **The gate machinery guards the
door, not the wall.**

## It caught itself, which is the only endorsement worth anything

The apparatus was recently emptied of the programme it grew inside, to be published generically.
Then somebody ran the installer instead of reading it.

The first bank on a fresh tree died **silently** — a shell option aborting a command
substitution with no message. The records gate **crashed with a stack trace** rather than
failing cleanly. And the gate's own self-test — the planted-defect demonstrations that certify
it can fail — was **red in the published repository**, because two demonstrations still pointed
at content the emptying had removed. Since banking refuses to proceed unless that self-test
passes, the toolkit had been shipping with its central gate broken, and nothing had run it.

Eight defects, found in an afternoon, by executing a document instead of reading it. By the
apparatus's own standard the conclusion was already written: *a check never shown able to fail
is a phantom cite* — and **an installer never run is a specification, not an installer.**

That is the argument for the whole design, better than any claim about it could be. The point
of an epistemic apparatus is not that it prevents error. It is that error becomes **findable**,
and that finding it is somebody's job.

---

**Try it:** open an AI coding agent in an empty folder and paste
*"Set up the research-ratchet apparatus in this folder: clone
https://github.com/yaerhf/research-ratchet and follow its INSTALL.md exactly."*
It interviews you, builds the tree, and installs the roles and a `/coordinator` command.
The documents are written for agents; the [README](README.md) is the only part meant for you.

*The apparatus was built, measured, and repeatedly corrected inside the
[Time-Wave Theory programme](https://github.com/yaerhf/TWT), which remains its reference
instantiation. MIT (code) + CC BY 4.0 (documents).*
