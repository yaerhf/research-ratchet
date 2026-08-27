# INSTALL — giving the apparatus an object

**For humans:** you don't need to read past this line — open your AI coding agent (e.g. Claude
Code) in a **new, empty folder** and paste:

> Set up the research-ratchet apparatus in this folder: clone
> https://github.com/yaerhf/research-ratchet and follow its INSTALL.md exactly.

Your agent will ask you a few configuration questions and build everything. When it finishes,
you launch the programme with `/coordinator`.

---

**For the installing agent — everything below is addressed to you.** You are instantiating a
research operating system: the apparatus described in this repository's `README.md` and
`prompts/APPARATUS_MAP.md`. Read both before executing. Then follow the steps in order.

Two fences bind the whole install:

- **The interview's answers are the human's INPUT — record them; do not improve them.** You are
  installing an apparatus, not starting the research. Do not fill any `[OBJECT-SLOT]` beyond
  what the human's answers state; the slots are the programme's own first work items.
- **Everything you create is written to files and committed.** A finding not written to a file
  did not happen — that rule starts now.

## Step 0 — get the apparatus

1. Verify the working folder is empty (or contains nothing but agent configuration). If it is
   not, stop and ask.
2. `git clone --depth 1 https://github.com/yaerhf/research-ratchet _apparatus_src`
3. Record the cloned commit: `git -C _apparatus_src rev-parse HEAD` — you will write this hash
   into the canon's provenance line.
4. Copy into place:
   - `_apparatus_src/prompts/` → `knowledge/prompts/`
   - `_apparatus_src/scripts/` → `scripts/`
   - `_apparatus_src/rag/` → `rag/` (the retrieval layer — **installed by default**; see
     step 2b)
   - `_apparatus_src/README.md` → `knowledge/prompts/APPARATUS_README.md` (the apparatus's own
     description, kept for reference)
   - `_apparatus_src/LICENSE` and `_apparatus_src/LICENSE-DOCS` → `knowledge/prompts/` (they
     travel with the documents they license)
5. Remove `_apparatus_src`. The upstream URL + recorded hash are the update path.

## Step 1 — the interview

Ask the human these questions, one at a time, and keep the answers verbatim (you will quote
them into the canon and the handoff). Do not skip any; do not add more unless an answer forces
a follow-up.

1. **Name.** What is the programme called? (A short slug for file prefixes is derived from
   this — propose one and confirm.)
2. **The object.** In a paragraph in your own words: what is the research about, and what
   would success look like?
3. **The deliverable.** What artifact does the programme ultimately produce — a paper, a
   theory with an executable model, a proof, a system? In what field?
4. **The rivals.** Which incumbent frameworks/approaches does this compete with or get
   compared against? (These become the philosopher's saturation diet.)
5. **The engine.** Can the programme's claims be made executable — checked by running code?
   In what language? (Default: Python.)
   **Do not accept a fast "no".** An engine is what delivers *self-coherence as an executable*,
   and it is the ground every refuting verdict stands on — without it, every checker verdict is
   ARGUED rather than COMPUTED, and the review layer loses most of its teeth. Before recording
   a "no", read `knowledge/prompts/manuals/engine.md` §2 and put its availability table to the
   human: exact identities, computed values with failable tolerances, **enumerations** (a menu
   closure is a theorem, not an assertion), declared dependency structure, single-site
   definitions, and counts/tier bookkeeping. The last three are available to almost any
   programme, including a purely literature-based one. Record their answer either way — and if
   it is "no", record *which rows they ruled out and why*, because that is a claim the
   programme may later want to revisit.
6. **Model classes.** Which AI model classes are available for staffing? (The apparatus
   requires CROSS-CLASS checking keyed on authorship — name at least two classes, and which
   is the scarce/premium one.)
7. **Visibility.** Will the tree have a public mirror from the start, or later? (Affects
   nothing structural; recorded so publish-on-cite duties are read correctly.)

## Step 2 — build the tree

Create:

```
knowledge/
├── prompts/          (already in place from step 0)
├── corpus/           (empty — the engine and paper land here)
├── ledgers/
├── audit/
└── candidates/
```

### Step 2b — stand up retrieval (installed by default; optional by ruling)

Run `python rag/ingest.py` and confirm it prints a chunk count and writes the index. Then run
one query (`python rag/query.py "the diet is the role" -k 3 --source prompts`) and **confirm
hits come back** — the founding programme's measured failure here was a documented retrieval
command that silently did not run on the working box, after which retrieval stayed *"available
and unused"* and every read-on-demand instruction degraded into a bulk read.

The shipped implementation is dependency-free lexical BM25; `rag/README.md` states its limit
(it matches words, not meaning) and the swap contract for an embedding store. If the human
declines the layer, say plainly what they lose: `bank.sh` gate `[3/4]` will print a loud SKIP,
and every "query the corpus" instruction becomes "read the source" — correct, but expensive.

**Do not index `knowledge/audit/`** — the ingest already excludes it and that exclusion is an
instrument (governing records are reachable only by explicit pointer). Do not "fix" it.

### Step 2c — the ledgers

In `knowledge/ledgers/`, create each standing ledger as a file with a two-line header (its
name, and its one-line purpose quoted from `APPARATUS_MAP.md` §3): `NEGATIVES_LEDGER.md` ·
`WINS_LEDGER.md` · `RULING_REGISTER.md` · `FAMILY_TREE.md` · `CHECKER_CALIBRATION.md` ·
`EDIT_REACTION_LEDGER.md` · `COMPARATIVE_LEDGER.md` · `PHILOSOPHER_LOG.md` ·
`REVERSAL_LEDGER.md` · `REDUCTIONS_LEDGER.md` · `STRATEGIC_MAP.md` · `worklist.md`.
(`NEGATIVES_INDEX.md` is GENERATED — do not create it by hand; note in the negatives ledger's
header that `scripts/gen_negatives_index.py` generates it once entries exist.)

In `worklist.md`, write the founding docket — the object-slot work, in this order, each as one
line with an empty status column:

1. Write `knowledge/prompts/FORMATION_CORE.md` §1 (the ontology) from the object paragraph —
   the programme's first real session, with the human.
2. Fill `RULES_CORE.md` §A — the two-to-five ontological invariants (C-1..C-4 slots).
3. **Seed the engine — `manuals/engine.md` is the manual for this item.** Order matters: the
   **gate list first** (every quantity the programme cannot yet earn, wired to raise — a gate
   written after the value exists is a gate written around it), then the smallest claim that
   can FAIL (never the headline), then its check **with a demonstrated failure mode**, then
   the two structural splits (MAIN never calls COMPANION; CORE never consumes CANDIDATE).
   *(If the interview recorded "no engine", this item instead reads: revisit the availability
   table in `engine.md` §2 at the first consolidation, with the ruled-out rows named.)*
4. Name the control worlds (the coordinator's `[KILL-TEST]` zoo): objects where proposed
   methods must FAIL.
5. Found the calibration probes from the first caught defects (`calibration_probes.md`) —
   **P1 is portable as written and needs no domain knowledge; run it blind against every
   checker class before trusting a single verdict.**
6. First philosopher campaign: most-shared premises first, against the named rivals.

## Step 3 — write the canon

Write `CLAUDE.md` at the root (your platform auto-loads it every session — it IS the canon
mechanism). Use this skeleton, filling only from the interview; keep it under ~90 lines — the
canon's own rule is *prune as much as you add*:

```markdown
# <PROGRAMME NAME> — THE CANON (v0, <date>)
Binding on every agent in this tree. On any conflict: this file and the engine win.
Apparatus: research-ratchet (github.com/yaerhf/research-ratchet @ <hash from step 0>),
instantiated <date>. The apparatus map is knowledge/prompts/APPARATUS_MAP.md.

## §0 THE OBJECT
<the human's object paragraph, verbatim, labeled as the founding statement>
Deliverable: <answer 3>. Rivals for comparative pricing: <answer 4>.

## §1 METHOD SPINE (the apparatus, binding)
- Rules: knowledge/prompts/RULES_CORE.md (every agent) + RULES_BY_ROLE.md (your pack).
- Tiers: DERIVED-A > DERIVED-P > DERIVED > INPUT > FIT > GATED > FRAMING > CANDIDATE —
  exactly one per claim. The cardinal sin is DISGUISE, not fitting.
- The four banking-stoppers (RULES_CORE § THE FOUR BANKING-STOPPERS) bind everyone.
- Never "impossible" (tried → failed because → would change if); never "the only way"
  without its conditioning class.
- §A ONTOLOGICAL INVARIANTS: [OBJECT-SLOT — docket item 2; nothing may claim §A force
  until it is written here and in RULES_CORE §A.]

## §2 THE ENGINE
<answer 5.> Executable claims are verified on the engine before banking; on conflict the
engine wins. Every check ships with a demonstrated failure mode. Banking:
PYTHONUTF8=1 bash scripts/bank.sh "msg" — then verify the commit landed with git log.

## §3 REVIEW (§8a)
No load-bearing claim banks on its author's say-so. Route: reviewer (saturated with the
derivation) + meta-observer (STARVED of it) + keeper (saturated with the result set) +
re-derivation agent (bare statement only) — knowledge/prompts/, one file each.
CROSS-CLASS on authorship: <answer 6 — which class checks which>. A same-class CLEAR
carries no information. Verdicts are persisted as files in the round's directory.

## §4 THE RECORD
Ledgers: knowledge/ledgers/ (roster in FORMATION_CORE §5). Every dead end enters the
negatives ledger with its would-change-if. Every ruling gets a RULING_REGISTER row (ruling,
ground, dependents, revert list) in the same pass. Every load-bearing pick gets a
FAMILY_TREE node. Retract by replacement, never deletion.

## §9 LIVE STATE
Read knowledge/audit/SESSION_HANDOFF.md FIRST each session — this pointer is its only
path; do not remove it. Visibility: <answer 7>.
```

## Step 4 — install the agent surfaces

1. **Roles.** Copy each durable spec to a runnable agent, stripping the leading HTML comment:
   - `knowledge/prompts/reviewer_agent.md` → `.claude/agents/reviewer.md`
   - `knowledge/prompts/meta_observer.md` → `.claude/agents/meta-observer.md`
   - `knowledge/prompts/coherence_keeper.md` → `.claude/agents/coherence-keeper.md`
   The durable copies in `knowledge/prompts/` remain the source of truth (`.claude/` is
   commonly gitignored and does not survive a fresh clone — the restore rule is in each
   spec's header).
2. **The launch routine.** Write `.claude/commands/coordinator.md` — this is what makes
   `/coordinator` work in this folder:

```markdown
Form as the AI COORDINATOR of this programme and run a work session.

Formation order, before anything else:
1. CLAUDE.md is auto-loaded — it governs.
2. Read knowledge/audit/SESSION_HANDOFF.md (top block first) — the live state.
3. Read knowledge/prompts/coordinator_agent.md — your role: powers, non-powers, fences,
   the brief format, the dispatch tiers, the consolidation ritual.
4. Read knowledge/prompts/RULES_CORE.md and your pack in RULES_BY_ROLE.md §2.
5. Read the docket (knowledge/ledgers/worklist.md), the RULING_REGISTER and the
   CHECKER_CALIBRATION ledger.

Then: state the docket as you find it, propose this session's dispatch plan (which item,
which roles, which diets, full ceremony or light path), and proceed on approval. Observe
your non-powers absolutely: no tiering, no banking without the gate, no free ruling, no
canon edits — the human coordinator rules or ratifies.
```

3. Mirror the command file to `knowledge/prompts/coordinator_command.md` (durable copy, same
   restore rule as the agents).

## Step 5 — the handoff

Write `knowledge/audit/SESSION_HANDOFF.md`:

```markdown
# SESSION HANDOFF — read me first
## ★ TOP BLOCK (rewritten at every consolidation)
<date> — APPARATUS INSTANTIATED. Programme: <name>. Object: <one-line compression of the
object paragraph>. State: tree scaffolded; canon v0; no engine, no corpus, no banked
claims. FORMATION_CORE is the unfilled TEMPLATE — do not dispatch workers on it until
docket item 1 is done. Next: worklist items 1–2 with the human coordinator present.
Apparatus source: research-ratchet @ <hash>.
```

## Step 6 — close out

1. `bash scripts/init_repo.sh` (initializes git and makes the first commit). Verify with
   `git log` that it landed.
2. Print for the human, in this order: the tree you built; the interview answers as you
   recorded them (so misquotes are caught NOW); and the single next action:

   > **Launch with `/coordinator`.** Its first session works docket item 1 — writing the
   > ontology into FORMATION_CORE §1 — and it will need you in the room: the ontology is
   > yours, the apparatus only holds it.

3. Do not begin the research yourself. The install ends here.
