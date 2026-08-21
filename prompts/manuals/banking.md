# MANUAL · BANKING — read this before you bank anything

**Trigger: you are about to run `bank.sh`, commit, add a check, or graduate a result.**
Complete for the activity: read this and you need nothing else to bank correctly.
*(Written 2026-08-20 as the worked pattern for the manual scheme — `manuals/INDEX.md`.)*

---

## 0 · THE ONE-LINE VERSION

`PYTHONUTF8=1 bash scripts/bank.sh "$(cat msgfile)"` — **then verify with `git log` that the commit
actually landed.**

---

## 1 · HOW TO DO IT

1. **Settle the tree first.** `bank.sh` snapshots the working tree when it *starts* and re-checks
   before committing; if anything changes in between — another session, an editor, **a subagent
   still finishing** — it refuses. That guard is correct; do not work around it. Wait, then re-run.
2. **Put the message in a FILE and pass `"$(cat file)"`.** An oversized inline argument fails
   silently — the command returns nothing, the commit does not land, and the tree stays dirty.
   *(Measured on 2026-08-20.)*
3. **No backticks in a commit message.** The shell performs command substitution and silently eats
   the content. Use `git commit -F` if you must.
4. **Run it.** Five steps: honesty telemetry (reports, never gates) → both suites → the
   record-invariants gate → RAG re-ingest → sweep-guarded commit.
5. **★ VERIFY THE COMMIT LANDED — `git log --oneline -1` and `git status`.** `rag/ingest.py` can
   die with a transient error at the end of a run, after which the commit is skipped and the
   printed `Banked:` line is the only tell. **This has happened. Check every time.**

---

## 2 · WHAT MUST BE TRUE BEFORE YOU BANK

**Both suites green** (verify the *printed* totals, never a remembered number) · **records gate
passing** · **the tree settled**.

And the four **banking-stoppers**, none of which any gate can catch — they run on you. **These four are the whole list, and the term is reserved for them** (RULES_CORE.md § THE FOUR BANKING-STOPPERS): anything else that blocks a bank is a *blocking defect with an owner*, and you name the owner.

- **BANK BEFORE YOU CITE.** Never write "engine-verified" for something not yet in the source *and*
  the suite. The suite does not check prose, so a phantom cite passes every check and is still a
  disguise.
- **REGISTER EVERY IMPORT** — companion §13, with premises, level, ontology status and retirement
  handle. Pure mathematics is exempt. *Unregistered import = banking-stopper.*
- **REGISTER EVERY RULING** in the same pass, with its **ground**, dependents and revert list.
  *Unregistered ruling = banking-stopper.*
- **REGISTER EVERY LOAD-BEARING PICK** as a family-tree branch node with menu and revert clause;
  Core-touching picks need plain-language sign-off *first*.

---

## 3 · CHECKS — and the rule that changed on 2026-08-20

**A NEW CHECK SHIPS WITH ITS FAILURE DEMONSTRATION.** Show it failing against the broken state,
for the named reason, then passing. *A check never shown able to fail is a phantom-cite of the gate
class.*

**★ AND A CHECK MUST BE ABLE TO FAIL FOR A REASON THAT MATTERS (RUL-067).** The older rule *"add a
check for every banked fact"* collided with *"a tight tolerance on a vacuous check is a tell"* —
obeying the first mechanically manufactures what the second condemns. **Resolved in favour of the
second: a useless check is waste, and waste is not neutral — it is a false signal of verification
that costs a reader's trust in every other check beside it.**

So: **add a DISCRIMINATING check, or record why none exists.** *"No discriminating check is
possible here because…"* is a complete and acceptable answer, and a better one than a green
tautology. Before writing any check, ask the standing question: **what could have DISAGREED?**

**The live example, found in our own suite:** an assertion that `Q['u'] ≈ 2/3` where `Q['u']` is
computed as `(2·1 − 0)/3`. It verifies that Python performs division. It cannot detect any change
in physics content.

---

## 3a · THE TIER-RAISE PASS — how an UNDER-CLAIM finding actually moves a tier

*(Added 2026-08-21, R3 of `knowledge/audit/consolidation_2026-08-18/RULES_RESTRICTION_ANALYSIS_2026-08-21.md`;
human coordinator "adopt all". It is the demotion pass's own machinery run in reverse — and it is the
ONLY destination an `UNDER-CLAIM` verdict has.)*

**Why it exists.** Three checker vocabularies gained an `UNDER-CLAIM` verdict on 2026-08-21 and it had
nowhere to go: a finding that a claim earned MORE than it took could be recorded and then had to sit.
Core rule **C-31** makes the under-label a labeling error of the same class as the over-label; this is
the pass that repairs one.

**Run all four steps, in order:**

1. **Restate the claim at the WIDEST scope its computation supports.** Not the scope you would like —
   the scope the computation reaches. Say plainly what the gap was between that and the claim as it
   stood. *(This is the wide half of meta-observer rule 85; the narrow half runs unchanged.)*
2. **★ CARRY AN ENGINE CHECK WITH A DEMONSTRATED DISAGREEMENT MODE — ABSOLUTE, AND THE WHOLE GATE.**
   **A raise is NEVER admissible on argument.** Not on a checker's verdict, not on a re-reading, not on
   consensus, not on the author's own conviction. Write the check, then **show it failing** against the
   state where the raise would be wrong, for the named reason, and then passing (C-19 + RUL-067 +
   banking rule 35). **A raise that cannot exhibit a possible world in which it fails is REFUSED** —
   record it as an open would-raise-if under C-31 and stop.
3. **Edit the Result-Index row AND the dependency edges in the SAME pass** (banking rule 158). A tier
   that moves in one place and not the other manufactures exactly the drift pair §4 below exists to
   prevent — and the companion, not the body, is authoritative for the tag.
4. **Log a `knowledge/ledgers/TWT_REVERSAL_LEDGER.md` row.** A raise is a position the programme
   changed, and it is recorded like one: what it was, what it is, and what moved it.

**The honest cost, stated with the rule.** This pass makes a **label change cheaper**, and every one of
the five FOUND-LATER misses was a label-or-prose defect wrapped around correct mathematics — the
credulity-miss class, squarely. Step 2 is the mitigation and it is not cosmetic: it gates every raise on
the single instrument whose absence produced those misses. **If you are tempted to skip step 2 because
the raise is obviously right, that temptation is the measured failure mode, not an exception to it.**

---

## 4 · SWEEP DISCIPLINE, IF THE BANK CHANGES A LABEL

In reader order, and **it is longer than you think**: paper body → front matter → companion
Sections 1/2/3/4 *including the Engine↔Paper Map's reverse index* → engine docstrings **and
returned dict strings** → both harnesses' check-description strings → **all fourteen standing
ledgers** (the roster is FORMATION_CORE §5 and it is gate-pinned; **`TWT_NEGATIVES_INDEX.md` is
GENERATED — regenerate it, never hand-edit it**) → canon → worklist → handoff → `simulator/`.

**A value and its check move together or not at all** — a harness asserts on returned strings, so
renaming a value without its check breaks the suite, and renaming a description without its value
manufactures a drift pair.

**Retract by replacement, never by deletion.** Every withdrawal leaves a labelled corpse at the
site. **The paper is history-blind** — the corpse's *history* goes to the companion's development
log in the same pass.

---

## 5 · COUNTS

**Refresh by COUNTING, never by incrementing.** Suite totals from a run, rows by grep, files by
`ls`. The records gate pins several count-bearing prose sites and will refuse the bank if they have
drifted — that is the gate working, not an obstacle.

---

## 6 · WHAT YOU MAY NOT BANK

If you are a **worker**: nothing. Report as executed-and-unbanked; the lead banks.
If you are on the **light path** (exploratory dispatch): nothing — light-path output is CANDIDATE
by construction, and a result that later wants to bank **re-enters at full ceremony and is not
grandfathered**.
If a **§8a round has not closed** on a banking-bound claim: nothing.

**And the standing one:** a finding not written to a file did not happen — *and one written to a
file git ignores also did not happen.* `knowledge/prompts/` is gitignored wholesale; **force-add
anything new there.**
