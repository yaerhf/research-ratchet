<!-- DIET-CLASS: GOVERNING -->
# LAUNCH DRAFTS — the README's opening and the Discord post, 2026-09-30

*Drafts for the human coordinator. **Nothing here is live:** the README is unchanged until the human
approves the opening below, and the post is the human's to publish, when the human decides (the
timing waits on the founding tree's kernel candidate — see the end). Target: Anthropic's Discord,
the built-with-Claude thread, where the Bureau was posted.*

---

## 1. THE README'S NEW OPENING

*Goes directly under the `# research-ratchet` title. The current tagline paragraph and everything
after it stay, below these lines. Written for someone who has never met the apparatus: no
vocabulary of its own before the reader has a reason to learn it (C-30-bis).*

> **An agent that checks its own research agrees with itself.** research-ratchet is a set of rules
> and roles for Claude Code that keeps a claim from being checked by the mind that made it — and
> gives every claim several checkers, each deliberately kept from seeing something different. One
> reads the derivation and argues against it. One never sees it, and asks whether the claim is
> about what it says. One holds every other result and looks for collisions. One gets only the bare
> statement and has to reach it alone.
>
> Every claim carries an honest label — derived, assumed, fitted, or still a candidate. Every dead
> end is recorded with what would reopen it. Nothing enters the record except through a gate that
> checks it, and a human rules on what no check can decide.
>
> **Try it:** your agent sets it up from [one paste, in about 15 minutes](#try-it--one-paste-about-15-minutes).
> **It suits** open-ended research, where being quietly wrong is the real risk. It is heavy for a
> quick task.

---

## 2. THE DISCORD POST

*In the thread's own format, the one the Bureau used: the idea, what it does, how Claude helped,
the limits, what it touches. Every claim below is from the record; the measured ones are quoted
from the README's own "measured claims" section.*

**Title:** research-ratchet: a research apparatus for Claude Code where every claim gets several checkers, each starved of something different

**Body:**

*(Optional first line, if posted next to the Bureau: "If the Bureau's cold reviewer made sense to
you, this is the same instinct, applied to research instead of code.")*

Built with Claude Code, for Claude Code. The idea behind it: an agent that checks its own research agrees with itself — and a fresh reviewer isn't enough either, because a reviewer who reads the argument gets pulled into it. So every claim gets several checkers, each deliberately kept from seeing something different: a reviewer who reads the derivation and argues against it; a meta-observer who never sees it and asks whether the claim is even about what it says; a keeper who holds every other result and looks for collisions; and a re-derivation agent who gets only the bare statement and has to get there alone.

What it does: one paste sets up a research folder — rules, role agents, a record, and a `/coordinator` command that runs a work session. Research claims have no test suite, so the design is built around honesty about what is actually established: every claim carries a label (derived, assumed, fitted, or still a candidate), dead ends are recorded with what would reopen them, and nothing enters the record except through a gate that checks it. A human owns the questions no check can decide.

How Claude helped: Claude runs every role, and has built most of the apparatus with me — including against its own work. Two moments. The founding measurement: for a month, review found nothing. The reviewers were the same model class as the author; cross-class review of the identical work surfaced real defects in one session. Checks now run across model classes, and a log records who wrote what. And this week: the apparatus's own sabotage tool planted 13 bugs in a copy of a check Claude had just written, and 3 slipped past the tests Claude wrote for it. Caught and fixed before it shipped.

It's not magic. It's dense and has its own vocabulary, it costs real tokens, and so far it has run on two programmes, both coordinated by one person. It's a method more than a product. Its automated checks each state in writing what they can't see.

What it touches: it runs on your machine, in the folder you point it at. It writes its agent definitions and a `/coordinator` command into that folder's `.claude/` directory, spawns Claude subagents, runs its own Python scripts, commits to your local git repository through its gate, and reads your Claude Code session transcripts locally (for recovering after a context compaction). No hooks, no GitHub operations, no pushes, no backend. Agents look things up online only when Claude Code lets them.

Free and open: code under MIT, documents under CC BY 4.0. Repo: https://github.com/yaerhf/research-ratchet

---

## 3. BEFORE POSTING — checked, or owed

- [x] **No hooks, no GitHub operations, no push** in the install or the bank — checked in
  `INSTALL.md` and `scripts/*.sh`, 2026-09-30.
- [x] **The benchmark target is not mentioned** anywhere in either draft.
- [x] **The README's provenance line carried a count forward** ("503+ inline-checked engine
  primitives" in the founding tree). **Replaced 2026-09-30 on the human's wording:** "it works on
  hundreds of engine-checked primitives" — true without a number that can go stale (C-24). The
  dated external review that quotes 503+ is a record of its day and is left as it is.
- [ ] **The README's first screen after the new opening is still the apparatus's own idiom** (the
  diagram). Acceptable once the opening has told the reader why to care; worth a second look.
- [x] **Timing — RULED 2026-09-30 by the human coordinator: post when the founding tree's kernel
  candidate comes back, positive or negative.** Verbatim: *"I just wanna wait until TWT's kernel
  comes back in the case it comes back positive. If it comes back negative we'll also post it at
  that time. But if we post it now, we get about the same impact as a negative kernel without
  giving it a chance."* The ground: the README links that tree as the reference instantiation,
  and its cold reviews have often answered *"we need to see the kernel finished to say if it's
  any good"*. **Until then, nothing here is posted.**
- [ ] **The README's new opening (§1) awaits the human's approval.** Not applied.
