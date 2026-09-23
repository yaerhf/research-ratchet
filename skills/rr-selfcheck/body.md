# Attack your own result before you ship it

Use this when you have a result — an analysis, a fix, a number, a claim — and you are about to hand
it over.

**What this produces:** demonstrated failures, and a list of the surfaces you did not attack.
**What it never produces:** independent agreement. You are checking your own work, and a clean pass
from the author of something is not evidence that the thing is right.

## The rule that makes it work

**A refutation of your own result is a result, and it counts as one.** The failure mode of
self-review is not blindness — you can see the flaws. It is **stopping**: the search ends when the
thing works, because a working answer was the objective. So restate the objective before you start:
**you are trying to break it, and breaking it is a success.**

## Before you look for flaws

1. **Write the attack list first**, before you know whether the result survives. Attacks chosen
   afterwards are the ones it already passes.
2. **Commit to a number.** At least five attacks, spread across the categories below. A quota takes
   the stopping decision away from the part of you that wants to stop.

## The categories

- **The data** — is the input what you think it is? Units, a stale file, a silent truncation, the
  empty case.
- **The arithmetic** — recompute by a second route. A number agreeing with itself is not a check.
- **The method** — does your check fire on a broken input? **If you have never seen it fail, you do
  not know that it works.**
- **The known-wrong case** — run the case whose answer you already know is wrong. A method that
  passes it is broken, and liking the real result does not repair it.
- **The frame** — is the claim about what it says? What did you assume that never became a
  sentence? *You will do worst here, because you cannot attack an assumption you never wrote down.*
- **What you removed** — every simplification removes something: a dimension, time, a coupling, a
  scale, a population. **Name what you removed**, then ask whether putting it back kills the result.
  A frozen version of something that moves is a removal like any other, and it is the one that hides
  itself, because it reads as a setting rather than a choice.
- **The transfer** — does it hold one step outside the case you ran, or only there?
- **The rival** — what else would produce exactly this output? Name the best competing explanation
  and say what separates them.

## Run them, do not imagine them

**An attack is a command and an output, not an opinion.** Where you can execute, execute: your bias
does not reach the result of a run. Where you cannot, say so — mark the attack as reasoned rather
than run, and mark the claim it touches accordingly.

## Attack what you wrote, not what you meant

Write the result down first, then attack the written version. Most of what a first reviewer returns
is the gap between the two.

## The report

- **N attacks run** — each with its command and its output, not a summary of them.
- **M that succeeded** — each stated plainly, with what it costs the result.
- **K surfaces not attacked** — named. **Silence about a surface is not a clean bill on it.**
- **One sentence, in your own words:** *none of this is confirmation by anybody but me.*

**If nothing broke, report that as what it is:** N attacks, none successful, these surfaces
untouched. The claim does not get stronger because its author failed to break it.

## The two things this cannot reach

- **An assumption you never wrote down.** There is nothing there to attack.
- **Your own route.** Once a derivation exists, the alternatives are downweighted. You can list
  them; you cannot un-see the path you took.

**The cheapest fix for both costs thirty seconds of somebody else's time:** paste the bare claim —
no derivation, no route, no hint of how you got there — into a fresh session, and ask it to reach
the result independently. If it lands somewhere else, you have just learned the one thing
self-review structurally cannot tell you.
