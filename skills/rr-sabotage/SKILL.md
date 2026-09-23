---
name: rr-sabotage
description: Measure what a test suite really covers: plant defects in a COPY and see whether the checks go red. Use to audit tests, find checks that cannot fail, or judge a green suite. Never writes to your repo.
allowed-tools: Bash(python ${CLAUDE_SKILL_DIR}/audit.py *)
license: CC BY 4.0 (docs) / MIT (code)
---

# Find out what your tests actually cover — by breaking things on purpose

**Use this when** somebody asks whether the tests are any good, what they actually cover, whether a
green suite can be trusted, how to audit or stress-test the checks, whether there are tests that
cannot fail, or how much of the code is really protected.

A green test suite is evidence that nothing broke it. It is evidence of nothing else.

This skill runs the other half: **plant a defect in the code a check claims to cover, run the
checks, and see whether they go red.** A check that stays green with a defect in place has been
*demonstrated* not to cover it — not argued, demonstrated, which is why the finding survives an
argument with whoever wrote the test.

**Everything happens in a copy. The repository you point this at is never written to.**

## How to run it

`audit.py` is bundled with this skill. It needs the command that runs the checks, and one or more
sabotages. **In Claude Code it is at `${CLAUDE_SKILL_DIR}/audit.py`** (pre-approved in this skill's
frontmatter, so it runs without a prompt); elsewhere, run it from wherever the skill was unpacked.

```bash
python ${CLAUDE_SKILL_DIR}/audit.py --command "pytest -q" \
  --plant "src/cart.py::if total > limit::if total >= limit" \
  --label "boundary loosened by one"
```

**It needs a repository on disk and a command that runs its checks** — so it belongs where your code
lives (Claude Code, or any session with a working directory). On the web app it can only reach files
you have uploaded into the sandbox.

Or a plan file, which is the normal way once there is more than one:

```json
[
  {
    "label": "discount can now exceed the total",
    "file": "src/pricing.py",
    "find": "discount = min(discount, total)",
    "replace": "discount = discount",
    "claims": "test_discount_never_exceeds_total"
  }
]
```

```bash
python audit.py --command "npm test" --plan sabotages.json
```

The tool runs the **unmodified** copy first. **If the checks are already red it refuses**, because
nothing can be concluded about a check that was failing before you touched anything.

## Choosing what to break — this is the whole skill

The tool plants and runs. Deciding *what* to plant is the judgement, and it has one rule:

**Break what a check claims, not what is easy to break.** Read the test's name, its docstring, its
CI step title — that is its claim. Then make the smallest edit that makes the claim false. Deleting
a file proves nothing, because everything fails. Editing a comment proves nothing, because nothing
should.

Four kinds that reliably pay:

1. **Weaken an obligation.** `>=` becomes `>`, a raise becomes a warning, a required field becomes
   optional. The test that claims to enforce it should go red.
2. **Hand-edit a generated artifact** whose check claims it is up to date. This is where
   *stamp-checking* hides: a check that compares a recorded hash or a version line stays green
   while the content underneath it is wrong.
3. **Make a record lie.** Mark something present that is absent, point a path at nothing, claim a
   file exists.
4. **Flip a declaration** — a type, a class, a status, a flag. Checks usually verify that a
   declaration *exists*, rarely that it is *right*, and the gap between those is a real hole.

**One sabotage, one claim, one edit.** An anchor that matches zero times or several is refused
rather than approximated: a sabotage you cannot point at is not evidence.

## Reading the result

- **CAUGHT** — the checks went red on this defect. It does **not** mean they cover the next one.
- **MISSED** — the checks stayed green with the defect in place.
- **VOID** — the baseline was red, or the anchor did not land exactly once. It means nothing at all.

**A MISSED is a finding only when a check claimed that region.** Where nothing claimed it, the same
result is an *un-attacked surface* — worth listing, never worth reporting as a hole. The tool cannot
tell these apart. You can, and that judgement is the value you add.

## What to report

- What you planted and it was caught.
- What you planted and it was missed — **with the check that claimed to cover it**, named.
- **What you never planted.** Silence about a surface is not a clean bill on it.
- And the limit, in your own words: **this is a sample, never coverage.** Five planted defects
  caught means five planted defects were caught.

Two more limits worth stating when they apply: a **flaky** suite produces CAUGHT by luck and nothing
here can tell that from a real catch; and whether an unenforced claim *matters* is a question about
the project, not about the tests.

## A worked result

Run against the gate of the repository this skill comes from, with four sabotages aimed at four of
its own named claims: a hand-edited generated file — caught. A hand-edited published artifact —
caught. A record marked present that was absent — caught. **A document declaring the wrong class —
missed.**

That last one was already written down as a known blind spot in that project, hours earlier, by
hand: the gate checks that a class is *declared*, not that it is *right*. The audit found it
independently, from the outside, by breaking things. **A method that rediscovers a known hole
without being told where to look is one you can point at a suite nobody has audited.**

---

*This skill is one activity from **research-ratchet**, a methodological apparatus for
AI-assisted research under a human coordinator: https://github.com/yaerhf/research-ratchet*

*What you get here is the discipline. **The apparatus adds what a single session cannot:** roles
that are starved of information so their agreement means something, gates that refuse a commit
until its checks have been shown able to fail, and records that outlive the conversation. If this
was useful, that is where it comes from.*

*Docs CC BY 4.0, code MIT. Derived from `prompts/manuals/sabotage_audit.md` at d4c73a15d0d6.*
