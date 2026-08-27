<!-- DIET-CLASS: ROLE -->
# THE APPARATUS — organigramme, roles, and where everything lives

**Generic edition, 2026-08-27** (derived from the founding programme's v1, 2026-08-19, written at
the human coordinator's request: *"draw an organigramme of the apparatus with the roles and folder
organization. I need to see it clear-minded."*).

> **What this is.** The apparatus has an unusual amount of machinery — role definitions with
> deliberately different information diets, standing registries, an executable oracle, a records
> gate, an outer review cycle. This is the one drawing of it. **It is descriptive, not
> normative** — the binding rules live in `RULES_CORE.md` and `RULES_BY_ROLE.md`, and the
> programme's canon governs both.
>
> **Provenance note (generic edition).** Incident citations and `RUL-NNN`/`R-NNN`/`N-NN`
> identifiers in this file point into the founding programme's registers
> ([github.com/yaerhf/TWT](https://github.com/yaerhf/TWT)) — they are the design's evidence
> trail, kept per this apparatus's own rule that a structure with no recorded incident reads as
> decree. Blocks marked **`[OBJECT-SLOT]`** are supplied by the programme that instantiates the
> apparatus.

---

## 1. THE ORGANIGRAMME

```mermaid
flowchart TB
    XR["<b>EXTERNAL REVIEWER</b> — the outer cycle<br/><b>STARVED of everything but the artifact</b><br/>held-out class · recurrent class<br/><i>fence F1: never formed in-session</i>"]
    HC["<b>HUMAN COORDINATOR</b><br/>owns the ontology · rules · ratifies<br/><i>final authority; the only one who rules class-(3)</i>"]
    AC["<b>AI COORDINATOR</b> — the entry point<br/>saturated with STATE<br/>dispatches · composes briefs · triages · escalates<br/><i>cannot tier, bank, rule freely, or edit the canon</i>"]

    subgraph EXEC ["EXECUTION AND §8a — per claim, cross-class on AUTHORSHIP"]
        direction LR
        W["<b>FLUENT WORKERS</b><br/>diet: FORMATION_CORE + one brief<br/><i>execute; bank nothing</i><br/><i>RUL-075: STEELMAN before conceding —<br/>question the adversarial review</i>"]
        subgraph INNER ["THE INNER CHECK — four diets on one claim"]
            direction LR
            RV["<b>REVIEWER</b><br/>saturated: the derivation<br/><i>sound and honestly tiered?</i><br/><i>a refutation COMPUTES<br/>or is labeled ARGUED</i>"]
            MO["<b>META-OBSERVER</b><br/><b>STARVED of the derivation</b><br/><i>is it ABOUT what it says?</i><br/><i>owns prior-art (F3)</i>"]
            KP["<b>KEEPER</b><br/>saturated: the whole result set<br/><i>does the corpus assert one thing?</i><br/><i>the OLD result may lose</i>"]
            RD["<b>RE-DERIVATION AGENT</b><br/><b>STARVED of derivation,<br/>probes, ALL verdicts</b><br/><i>prove it again; a different<br/>route beats agreement</i>"]
        end
        W -->|"unbanked result"| INNER
    end

    subgraph META ["THE APPARATUS PRICES AND WATCHES ITSELF"]
        direction LR
        PH["<b>THE PHILOSOPHER</b> (split role, fence F4)<br/>worker capacity: isolated premises + literature<br/>checker capacity: starved of our derivations,<br/>saturated with the RIVALS<br/><i>+ contra-reviewer, RUL-044</i>"]
        AUD["<b>APPARATUS AUDITOR</b> (N1 + ex-enforcer, RUL-072)<br/>what does it prevent · at what cost · was the<br/>SPIRIT served <i>· MANDATORY before any cut</i><br/><b>DECISION-ATTENTION READER</b> (N2, at each release)<br/><b>ARCHIVIST</b> · <b>REGISTER CLERK</b> (pilot, RUL-079)"]
    end

    subgraph BANK ["THE DATA BANK — the record, and the only way into it"]
        direction LR
        GATE["<b>THE GATE</b> · scripts/bank.sh<br/>1. suites green → 2. records gate<br/>→ 3. re-index → 4. sweep-guarded commit<br/><i>honesty telemetry reports, never gates</i>"]
        REC["<b>THE RECORD</b><br/>corpus · engine · paper · companion<br/>the standing ledgers: negatives · <b>paths</b> · wins<br/>rulings · family tree · calibration · reversals"]
        GATE ==>|"admits"| REC
    end

    GEM["<b>IDEATION ADVISOR</b> — ideation only<br/><i>numbers carry ZERO evidential weight</i>"]

    XR <-->|"the human sends the release · the cold verdict comes back<br/>never through the AI coordinator (fence F1)"| HC
    HC <-->|"rulings · ratification · priorities<br/>owed rulings, costed both ways"| AC
    AC <-->|"briefs: kill-test · forecast · diet · retrieval bound<br/>verdicts, persisted as files"| EXEC
    AC <-->|"dispatches<br/>debt · spirit-served · re-ranked paths"| META
    EXEC -->|"results priced · passes audited"| META
    AC ==>|"banks — nothing enters on an author's say-so"| BANK
    REC -.->|"formation · diet-bounded retrieval"| EXEC
    GEM -.->|"CANDIDATE only"| AC

    %% A standing prior-art role was RETIRED into the meta-observer's F3 axis (RUL-073) —
    %% that work structurally lives there, since the reviewer has no web tools.
    %% ROLE-COUNT GOVERNANCE (RUL-074): adding roles AND changing any count constraint are
    %% both under the HUMAN COORDINATOR'S approval; a freeze was proposed by an adverse
    %% review and REFUSED (bloat noted, approval gate preferred).
    %% Layout only: mermaid ranks by longest path, so the record's feed back up to execution
    %% would otherwise sink the execution row below the bank. The invisible link supplies the
    %% order no truthful edge could — neither the philosopher nor the auditor clears a bank.
    META ~~~ BANK
```

**Read the diagram by DIET, not by hierarchy.** Every instrument here is defined by what it is
**starved of** and what it is **saturated with**. Merging two roles destroys a measurement, not
merely tidiness — the meta-observer is only useful *because* it never sees the derivation.

---

## 2. THE ROLES, ONE LINE EACH

| role | file | starved of | saturated with | its one question |
|---|---|---|---|---|
| Human coordinator | — | — | the ontology, the years behind it | *is this what I mean?* |
| **AI coordinator** | `coordinator_agent.md` | — | state | *who should hold what?* |
| Fluent worker | `FORMATION_CORE.md` + brief | everything not in its brief | its task | *what does the substrate say?* |
| Reviewer | `reviewer_agent.md` | — | the derivation | *sound and honestly tiered?* |
| Meta-observer | `meta_observer.md` | **the derivation** | the claim, the world | *is it ABOUT what it says?* |
| Keeper | `coherence_keeper.md` | — | the whole result set | *does the corpus assert one thing?* |
| Philosopher (worker) | `philosopher_ledger_agent.md` | — | isolated premises + literature | *could this have been otherwise?* |
| Philosopher (checker) | same file, F4 split | our derivations | the rivals | *what does it cost, against what?* |
| External reviewer | `external_review_loop.md` | **everything but the artifact** | — | *is it legible from outside?* |
| Apparatus auditor (N1) | `removal_auditor_agent.md` | — | the defensive structures | *what breaks if this goes?* |
| Decision-attention reader (N2) | `decision_attention_reader.md` | — | the release artifact | *what must the human decide?* |
| Archivist | `archivist_agent.md` | **the physics** | the record's shape | *is it navigable and current?* |
| Register clerk (PILOT) | `register_clerk.md` | the research corpus | the registers, at formation | *what does the record say, verbatim?* |
| Re-derivation agent | `rederivation_agent.md` | **derivation, probes, all verdicts** | the bare statement | *can I prove it again, unaided?* |

**Why N1, N2 and the re-derivation agent have durable files:** a role whose reasoning is
reconstructed at each dispatch is a role that will drift — N1's own first run reported that
defect about itself. N1 carries recommendation **R-A** built in, so it asks two questions rather
than one: *what does this prevent?* **and *what does it cost per pass?*** The second exists
because **every addition to this apparatus has a champion — its motivating incident — and no
removal has one**, which means the apparatus can otherwise only accumulate until impatience
removes things, and impatience removes exactly the class N1 protects. N2 runs at each release,
asking what the human must DECIDE and whether their agents can extract it.

---

## 3. FOLDER ORGANIZATION — the reference layout of an instantiated programme

*(This repository ships the `prompts/` and `scripts/` halves. The rest of the tree comes into
existence when the apparatus is given an object.)*

```
CLAUDE.md                    THE CANON — auto-loaded into every session, un-compactable.
                             Binding on everyone. Keep it small; prune as much as you add.

knowledge/
├── prompts/                 ★ THE APPARATUS ITSELF (this repository's prompts/)
│   ├── FORMATION_CORE.md      the worker prefix (versioned; changes only at consolidation)
│   ├── APPARATUS_MAP.md       this file
│   ├── AGENT_RULES.md         the by-when-it-bites view + the live divergence table
│   ├── RULES_CORE.md          the core rules that bind everyone · RULES_BY_ROLE.md  the role packs
│   ├── PROFILES.md            the disposition axis (steelman RESOLVED into the worker duty, RUL-075)
│   ├── packs/                 ★ GENERATED per-role rule packs — what a dispatch loads
│   ├── manuals/               activity manuals — banking.md (demotion AND tier-raise passes) ·
│   │                          engine.md (SELF-COHERENCE AS AN EXECUTABLE: is an engine
│   │                          relevant here, and how to build one that arbitrates)
│   ├── removal_auditor_agent.md  ★ THE APPARATUS AUDITOR (N1 + ex-enforcer): prevents/costs + spirit-served
│   ├── enforcer_agent.md          pointer stub only — merged into the auditor (RUL-072); kept so old pointers resolve
│   ├── decision_attention_reader.md  N2 — at each release: what must the human DECIDE?
│   ├── rederivation_agent.md  prove it again from the BARE STATEMENT (forbidden the derivation)
│   ├── register_clerk.md      registers held in context, quote-only, read-only (RUL-079 pilot)
│   ├── coordinator_agent.md   ★ THE ENTRY POINT ROUTINE (incl. the post-negative push, RUL-078)
│   ├── reviewer_agent.md / meta_observer.md / coherence_keeper.md      the §8a triad
│   ├── philosopher_ledger_agent.md · archivist_agent.md                other roles
│   ├── external_review_loop.md    the OUTER CYCLE routine
│   ├── standalone_review_send.md  the note-level cold-review send (byte-pinned prompt)
│   ├── calibration_probes.md      run BLIND before trusting any checker
│   ├── paper_rework_lessons.md    read before ANY paper edit
│   └── psychology_of_ai_reviewers.md · coherence_audit.md · adversarial_review.md · remediation_session.md
│
├── corpus/                  THE ARTIFACT + THE ORACLE                       [OBJECT-SLOT]
│   ├── <paper>.md               the foundational paper · HISTORY-BLIND by ruling
│   ├── <paper>_companion.md     Result Index · dependency graph · dev log · import registry
│   ├── <engine>.py              MAIN engine — executable ground truth
│   ├── <engine>_companion.py    COMPANION engine (MAIN never calls it)
│   └── the two test harnesses   every check ships with a demonstrated failure mode
│
├── ledgers/                 THE STANDING LEDGERS — all indexed by RAG; roster gate-pinned
│   ├── NEGATIVES_LEDGER.md      tried → failed because → would change if
│   ├── NEGATIVES_INDEX.md       GENERATED — one line per entry, would-change-ifs VERBATIM
│   ├── WINS_LEDGER.md           wins recorded AS wins (a row here never upgrades a tier)
│   ├── RULING_REGISTER.md       rulings in force + GROUNDS + revert lists
│   ├── FAMILY_TREE.md           commitment levels: the pick register, with revert clauses
│   ├── CHECKER_CALIBRATION.md   overturned verdicts + blind probe runs
│   ├── EDIT_REACTION_LEDGER.md  edit → external reaction history
│   ├── COMPARATIVE_LEDGER.md    the ontological debt ledger (philosopher's output)
│   ├── PHILOSOPHER_LOG.md       the philosopher's own failures and successes
│   ├── PATHS_LEDGER.md          the paths NOT taken, ranked by tractability; re-ranked when one dies
│   ├── REVERSAL_LEDGER.md       positions the programme changed and what changed them
│   ├── REDUCTIONS_LEDGER.md     the forward object: if A holds, C1..Cn follow, by proof
│   ├── STRATEGIC_MAP.md · worklist.md  (docket + the do-not-compress meaning-notes region)
│   └── <domain ledgers>         whatever the object demands                 [OBJECT-SLOT]
│
├── audit/                   GOVERNING RECORDS, dated  ⚠ NOT in the RAG index, BY DESIGN
│   ├── SESSION_HANDOFF_*.md     ★ READ FIRST — live state; reachable ONLY via the canon pointer
│   └── <arc directories>/       adjudications, consolidations, review rounds — each with INDEX.md
│
└── candidates/              CANDIDATE material — probes, memos, unadjudicated work

scripts/     bank.sh (the only way in) · gen_role_packs.py (per-role rule packs; regenerate
               at every consolidation — a stale pack fails the bank)
             · check_records.py (the records gate; runs on any tree)
             · check_records_founding.py (the founding gate, kept as the worked example of a
               mature one — ~98 pins onto its own corpus; not run by bank.sh)
             · honesty_telemetry.py
             · gen_worker_agent.py · gen_negatives_index.py · release tooling
rag/         ingest.py · query.py — the retrieval layer. INSTALLED BY DEFAULT, OPTIONAL by
             ruling (2026-08-27): bank gate [3/4] re-indexes at every bank and prints a loud
             SKIP if the layer is absent; `knowledge/audit/` is never indexed (a diet at the
             file layer). Shipped lexical + dependency-free; swappable — see rag/README.md
```

**Three structural lessons from the founding programme, worth carrying:**
1. **Check what git actually tracks.** The founding tree gitignored its apparatus directory
   wholesale; five role files were found untracked. A finding written to a file git ignores did
   not happen — force-add anything a broad ignore covers.
2. **Keep `knowledge/audit/` deliberately outside RAG**, so governing records are reachable only
   by explicit pointer. The handoff's sole path is the canon's pointer line. **Do not remove it.**
3. **Index and chunk the engines per primitive** — a primitive can then be *queried* at a
   fraction of the context of reading the file. Long docstrings fragment that.

---

## 4. THE THREE CYCLES

**INNER — per claim.** worker produces → §8a checks with three different diets → coordinator
triages → banks. *Nothing is banked on the developer's say-so alone.*

**MIDDLE — per arc.** docket item → work → consolidation (banking triage · archivist pass · N1 ·
the M1 offer judgment · prefix re-version · handoff rewrite · bank + tag).

**OUTER — per release.** release → cold measurement → adjudicate → correct → re-release.
*The programme's only external forcing function.* The coordinator drives it and never forms the
reader.

---

## 5. THE ENTRY POINT

**`coordinator_agent.md` is the entry point.** A session starts by forming the coordinator, which
then dispatches everything else. The consolidation ritual lives there authoritatively.

The surviving specialist routines the coordinator dispatches into: `external_review_loop.md`
(the outer cycle), `standalone_review_send.md` (note-level cold sends), `coherence_audit.md` +
`remediation_session.md` (the global audit and its repair pass), `adversarial_review.md` (the
separate-build review form). *(The founding programme's session-type entry points —
worklist/consolidation/campaign briefs — were superseded by the coordinator routine and are not
carried in the generic edition; its tree retains them.)*

---

## 6. WHAT THE APPARATUS DOES NOT DO — measured, not assumed

Recorded here because a map that shows only what works is a sales brochure. All four were
established in the founding programme by deliberately breaking things (2026-08-19):

- **One gate does not guard.** Of five raising gates, four fired under sabotage and one was
  unreachable because its configuration was never constructed. Both suites stayed green.
- **Striking an import-registry row broke nothing and warned nobody** — uniqueness was checked,
  referential integrity was not.
- **The suites verify the mathematics, not the prose.** The bulk of engine docstring content is
  prose no assert can express — claims with no equation and no number.
- **The gate machinery guards the door, not the wall.** It catches a gate that stopped raising.
  It does not catch a *new* primitive that returns an unearned number without touching a gate.
  That remains a human duty, and it is the reason the §8a roles exist.
