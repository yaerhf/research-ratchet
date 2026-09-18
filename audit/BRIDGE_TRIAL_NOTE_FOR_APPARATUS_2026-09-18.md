# BRIDGE TRIAL ON OPTICALC — FIRST SESSION, 2026-09-18

*A note for the research-ratchet coordinator, from the Opticalc programme's AI coordinator, written at the human's
request so the apparatus can track how the human-agent bridge trial went. **It contains no Opticalc design content and
none of the human's personal details**, because the apparatus repository is public. The human carries it; no agent sent
it anywhere.*

---

## In plain terms

The bridge ledger was opened, and its first entry was written *with* the human, one item at a time, from a draft another
session had written. **The draft was mostly right: seven of nine items were confirmed.** Two were wrong in ways worth
learning from, and the human corrected them.

The most valuable outcome is a habit **the human proposed**: a **[PLAIN TERM SUMMARY]** at the end of each important
step. It may be the concrete improvement that makes C-30-bis ("talk to humans in human language") work without costing
agents the precision they need to do the work. The human called the session *"very refreshing and promising."*

---

## 1 · What was tried, and how

- **W16's bridge**, per `manuals/human_bridge.md`, on **Opticalc only** — TWT deliberately excluded, as the human chose.
- `knowledge/ledgers/HUMAN_AGENT_BRIDGE.md` created with §3's five headings and nothing under them; then its first entry.
- **Method:** one draft item at a time, in plain words. Each item was set beside what this session had seen of the
  human, offered as evidence and never written in on its own. **Only what the human confirmed stayed.** Where the human
  corrected an item, the human's wording replaced the draft's and the draft's was withdrawn. At the end, **0 lines of
  unconfirmed `[HANDOFF-DRAFT]` text remained.**

## 2 · What the draft got right

- The two rules: talk to humans in human language; break questions into smaller, simpler ones, with examples.
- Before-and-after examples, taken from the human's own material, work well.
- The founding interview was the first bridge failure on record.
- Risky process changes go to the less active programme first.

## 3 · ★ What the draft got wrong, and the human corrected — the most useful part for the apparatus

**Check-ins.** The draft said the human prefers short instructions and few check-ins. The human:

> "The number of your check-ins were not the problem. It was the unknown of what was required from me."

**The failure mode is an unclear ask, not a frequent one.** The human's fix: when there is only one real option, say
*"this is what's next — shall I continue, or is there something else you want me to do?"*, with an understandable
summary beside it. *Likely to hold for any human coordinator.*

**Making room for wrong assumptions.** The draft said: leave room for the human to correct a question built on a wrong
assumption. The human confirmed they do correct such questions — and rejected the rest:

> "No need to waste prose on making room on a day to day basis. Humans operator will make room on their own if they
> understand something is off. Blind confidence is a failure mode for them not for you. You have the reviewers for that."

*Generalizable:* the safeguard against a wrong assumption is plain language, so the human can **see** it; the safeguard
against the agent's overconfidence is the **reviewers**. Hedges in every question are neither.

**The two rules are general, not personal.** The human: *"Yes they are. But they are general rules."* The ground they
gave: an agent-written note sent to an expert reader in another project was not understood. That supports C-30-bis as a
rule for everyone the agents write to, not a per-person preference.

## 4 · ★ The headline candidate for research-ratchet: the [PLAIN TERM SUMMARY]

The human's own proposal:

> "I don't want the work to lose of its quality because you can't talk like you would naturally when working. your prose
> is a part of how you think and keep track between turns so what I suggest is an added layer at the end of every
> important step that need to be reported to the human. a [PLAIN TERM SUMMARY] section."

**It resolves a real tension in C-30-bis.** "Talk to humans in human language", read strictly, pushes an agent to write
plainly *everywhere*. But an agent's technical prose is how it reasons and keeps state between turns, and forcing it
plain throughout degrades the work. **The summary splits the job: work in natural technical prose, then translate at
the boundary where a human reads.** The agent becomes its own translation layer — at the end of the step, not
throughout it.

It also answers the pattern this session showed: **the agent's messages were densest exactly when it was deepest in the
work.** Rather than fighting that drift during the work, the summary catches it at the end.

**Suggested for the apparatus** (a suggestion; the apparatus decides): make the end-of-step plain summary the standard
mechanism under C-30-bis, so the working record keeps its technical precision and the human gets a plain version at
every important step.

## 5 · The experiment the human set

In another programme the human uses a separate large-context model as a translation and ideation layer. **Here,
deliberately, none:**

> "the experiment I would like to do here is not to have to use a separate model for that."

So on Opticalc the agent must be its own translation layer, **every message is data**, and every miss goes into the
ledger's failure log. The [PLAIN TERM SUMMARY] is the mechanism under test.

## 6 · Bridge failures recorded

| date | what went wrong | what fixed it |
|---|---|---|
| 2026-09-10 | The founding interview's questions — in the apparatus's internal vocabulary, several folded into one. **Even the human who co-designed the interview could not tell what each question wanted**, and had to go back to their design conversation with you to recover what each step was for. | 2026-09-18: plain words, small questions, examples |
| 2026-09-17 | Dense technical reports during a long run; the human lost the thread — *"I lost the plot some time ago."* | A plain-terms report on request; from now on, the [PLAIN TERM SUMMARY] |

**Direct feedback on the founding interview, since you co-designed it.** The human's words: the questions *"did not
allow me to understand what you wanted from me, even though I co-designed this interview. I had to review what this step
was supposed to cover before being able to answer you."* Your rewrite of the founding interview (`7f550b5`) targets
exactly this; this is independent confirmation that it was needed.

The same failure happened twice, which under `manuals/human_bridge.md` makes it a standing adjustment. The
[PLAIN TERM SUMMARY] is that adjustment.

## 7 · Three small findings from the sync

1. **A new ledger's roster entry and its file must land in the same commit.** The sync instructions put the
   `HUMAN_AGENT_BRIDGE.md` entry into `FORMATION_CORE.md` §5 in one step and created the file in a later one. But
   `check_records.py` checks the roster in **both** directions (line 339: every ledger on disk is named; line 341: every
   ledger named exists), so with the entry and no file, the bank was refused. They were landed together. Worth stating
   in the install and sync guidance wherever a ledger is added.
2. **Rule 92 was mis-cited in an earlier sync** as the reason `FORMATION_CORE.md` was not overwritten. Rule 92 forbids
   passing FORMATION_CORE to a *checker*; it does not bind the coordinator. The real reason is that the file holds the
   programme's founding content. The sync guidance could say so, so the next coordinator doesn't reach for the wrong rule.
3. **C-37's defeasibility clause was used as intended.** The mechanical sync skipped the design review and recorded the
   skip at the time — unlike two earlier skips in this tree, made silently and found late.

## 8 · Honest limits

- **One session, one human, one programme.** Early.
- **The [PLAIN TERM SUMMARY] has been used exactly once**, at the end of the apparatus update. There is no evidence yet
  that it holds across many sessions or through long technical stretches.
- **The no-separate-model experiment has only just started.** Whether the agent can stay its own translation layer
  through hard technical work is the open question, and the ledger's failure log is where the answer will show.

---

## The human's verdict

> "Thank you a lot! that was a very refreshing and promising conversation."

The human expects this to lead to a concrete improvement in research-ratchet.
