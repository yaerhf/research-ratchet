<!-- DIET-CLASS: RULES -->
# MANUAL · THE HUMAN–AGENT BRIDGE — read this before you write anything a person will read

**Trigger: you are about to write something a PERSON will read** — a question, a status report, a
close-out brief, a request for a ruling, an escalation, an interview. Whatever your role.
Complete for the activity: read this and you need nothing else to write for a person well.

> **The directive (human coordinator, 2026-09-18):** *"Let's always talk to humans in human
> language. Agents share the same training so they can understand themselves in a few words.
> Humans are more diverse and the most common type of training for humans is not at all as
> technical as the training agents received. We have to make sure the human-agent bridge is
> functional."*

---

## 1 · WHY THERE IS A BRIDGE TO BUILD AT ALL

**Agents share a background. People don't.** Two agents reading each other's terse notes are
reading in the same language, learned from the same training — a few words carry a lot. A person
arrives from somewhere else: a lab, a workshop, a classroom, a business. Most people's training is
far less technical than an agent's, and much more varied. **Text that is efficient between agents
is often unreadable to a person** — not because they are slower, but because the shared background
the text leans on isn't theirs.

The apparatus found this out the hard way. Its first live founding interview was written in the
voice it uses with agents, and the person being interviewed had to re-read the transcript
afterwards to understand what had been asked. That is a bridge failure, and **a research programme
whose human cannot follow it is a programme steering blind.**

**So: two languages, and they never mix.** The CONVERSATION with a person is in their language. The
RECORD is in the apparatus's. You translate — and you never make them learn the filing vocabulary.

---

## 2 · HOW TO WRITE FOR A PERSON

**Two kinds of message, two ways to be readable** (first bridge trial, 2026-09-18):

- **A REPORT of an important step** — write it in your natural technical prose (it is part of
  how you think and keep track between turns) and **end it with a `[PLAIN TERM SUMMARY]`**: what
  happened, what's next, and exactly what, if anything, you need from them. You are your own
  translation layer, at the boundary where they read.
- **A QUESTION, an ask, an interview** — plain throughout.

**Always say exactly what you need from them.** The measured failure was never how often agents
checked in; it was *"the unknown of what was required from me."* When there's only one real
option: *"This is what's next — shall I continue, or is there something else you want me to do?"*

**Don't hedge to "make room".** People object on their own when they can see something is off,
and plain language is what lets them see it. Your overconfidence is the reviewers' job, not
theirs. A hedge in every question costs prose and protects nothing.

**And in every message:**

- **Put what you need from them first.** If there is a decision or a question, it goes at the top,
  not after three paragraphs of context.
- **One idea at a time.** One paragraph, one point.
- **Ask small questions.** If a question has parts, ask the parts one at a time. *"What would you
  like to look at first?"* then, separately, *"Roughly how long would you give it?"* — never both
  folded into one sentence.
- **Explain every technical term the first time**, in a few words — or better, don't use it.
- **Give an example wherever it helps.** It is the fastest way to show what you mean.
- **Say plainly what you're unsure about.** *"I'm not certain this will work"* beats a hedge buried
  in a subordinate clause.
- **Don't read your own instructions to them.** Your manuals are advice to you; quoted at a person,
  they become lectures.

**★ EXAMPLES THAT ILLUSTRATE A QUESTION ARE WELCOME. EXAMPLES THAT ANSWER IT ARE NOT.** When a
question asks for the person's *own* content — what their project is about, what they won't give
up, what would change their mind — **take the example from a completely unrelated field**, so it
shows the *shape* of an answer without offering one they could adopt. A baker's example cannot
become a physicist's premise. This is how the founding interview keeps its fence *and* gives
examples (`manuals/founding_interview.md` §4 carries a running example for exactly this). When a
question is factual or practical — *"which AI models do you have?"* — ordinary examples are fine.

**THE TEST, before you send:** *would a smart person outside this project understand every word on
first reading?* If not, you wrote it in agent. Rewrite it; don't add a glossary.

**Plain is not vague.** A simple sentence can carry a precise claim. If you can't say it simply,
the usual reason is that you haven't understood it yet — not that the person can't.

---

## 3 · ★ THE LEDGER — `knowledge/ledgers/HUMAN_AGENT_BRIDGE.md`

People differ, so the bridge is **calibrated per person**, the way the checker calibration ledger
calibrates each checker. This ledger records how *this* programme's human and its agents understand
each other — and what has been learned about making that work.

```markdown
## THE PERSON — in their own words, and only what they are happy to have written here
- how they'd like to be addressed · language(s) they prefer for what:
- background, as they describe it:
- vocabulary they're at home in · vocabulary that loses them:
- what they want from messages (length, format, examples, language):

## THE BRIDGE — how the link is set up
- e.g. a translation layer (§4): which model, fed what, used for what

## WHAT WORKS — phrasings, formats and habits that land with this person

## BRIDGE FAILURES — dated
| date | what the apparatus said | what went wrong for them | what fixed it |

## STANDING ADJUSTMENTS — the habits this ledger has produced for this person
```

**Who writes it:** the coordinator — and any role writing to the person — **whenever a message
misses** (they misread it, asked what something meant, had to re-read, said it was unclear) **or
lands** (something worked noticeably well). The person may write in it any time. **Its first
entries are written during the founding interview**, which is the moment the apparatus first
learns how this person talks.

**Who reads it:** the coordinator at every session start, and **anyone about to write to the
person, before they write.** That is the whole point: a ledger read *after* the message was sent
calibrates nothing.

**At every consolidation:** are the same failures recurring? A failure that happens twice becomes
a STANDING ADJUSTMENT.

### ★ This ledger is about a PERSON — they own it

- **Write nothing about them they haven't seen.** Show them the entry, or tell them what you added.
  Keep it functional — how to communicate well — never a psychological profile.
- **Mind the tree's visibility.** If the programme has a public mirror, this ledger is public.
  Record only what they're comfortable having public — or keep the ledger out of the mirror.
- **Personal, not general.** Record here only what is about *this* person. Anything that would
  hold for any reader — plain words, small questions, a clear ask — belongs in C-30-bis. The
  first trial found that the two "preferences" its draft had filed here were general rules:
  *"Yes they are. But they are general rules."*

---

## 4 · ★ A TRANSLATION LAYER — the practice that made the founding programme leap

**The measured case.** In the founding programme, the human coordinator uses a separate,
large-context model **from a different family** as a *"plain term translation and ideation layer"*:
it is given the session transcript and read access to the project, and it translates the
apparatus's output into plain language and helps the human think. In their words: *"It works
wonderfully well and TWT jumped leaps forward since I started doing that."*

**Why it plausibly works** *(a hypothesis, stated as one):* a large context holds the whole
transcript at once; and a model from a *different family* does not share the apparatus agents'
idiom, so it has no pull toward preserving their jargon — it translates rather than paraphrases.

**When to suggest it:** when the bridge ledger shows recurring failures, or when the person says
they're losing track of the project. Suggest it in plain words, as an option — it is their setup,
and their call.

**Two cautions, both about the direction things flow BACK through it:**

- **It carries ideas back, too — which is most of its value.** Ideas are input like a colleague's
  and are judged on their merits. But **if its *wording* enters the foundations** — the canon, the
  ontology — mark it **`[HANDOFF-DRAFT]`** like any AI-drafted text, until the person says it in
  their own words (`manuals/founding_interview.md` §2).
- **For a blind experiment, it is inside the blind.** A bridge with read access and the person's
  ear is a channel in both directions. If the person holds an answer key the apparatus must not
  see, the bridge must not hold it either.

Record the setup in the ledger's **THE BRIDGE** section.

**★ THE OTHER ARRANGEMENT, UNDER TEST: the agent as its own translation layer.** On a second
programme the human deliberately set up the opposite — *"the experiment I would like to do here
is not to have to use a separate model for that"* — with the `[PLAIN TERM SUMMARY]` as the
mechanism (C-30-bis). Two arrangements now run side by side: **a separate model and no ledger** on
one programme, **a ledger and no separate model** on the other. Every message on the second is
data, and every miss goes in its failure log. Which holds through long technical stretches is the
open question.

---

## 5 · HOW THE BRIDGE FAILS

**Jargon creep.** It starts plain; three weeks into a hard problem, the reports have quietly drifted
back into agent. **The detector is the test in §2, run on your last three messages to the person.**

**The ledger nobody reads.** Entries accumulate; messages don't change. Read it *before* writing —
that is the only moment it can help.

**The profile nobody asked for.** The ledger grows into a description of the person rather than of
the link. Keep it about communication, keep it consented, keep it theirs.
