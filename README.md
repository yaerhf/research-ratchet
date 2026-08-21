# research-ratchet

**An operating system for AI-agent-driven research under a human coordinator — published as the
working apparatus of the [Time-Wave Theory programme](https://github.com/yaerhf/TWT), where it was
built, measured, and repeatedly corrected by its own instruments.**

A ratchet moves one way and locks against slipping back. That is the design principle here:
research claims advance only through gates that verify them, every commitment is registered with
a revert path, and nothing enters the record silently — so knowledge can move forward, and can be
*deliberately* reversed, but cannot quietly regress or quietly inflate.

## What this is

The complete instrument set a research programme runs on when most of the researchers are AI
agents and the ontology is owned by one human:

- **`prompts/RULES_CORE.md`** — the ~32 rules every agent holds (tiers, honesty spine,
  commitment budget, verification discipline), each with its motivating incident and a general
  break clause: a recorded, reasoned break that serves a rule's purpose is compliance.
- **`prompts/RULES_BY_ROLE.md`** — role packs and activity blocks; each states only what it adds.
- **The roles, each defined by its information DIET** — what it is deliberately starved of is
  the instrument:
  - *adversarial reviewer* (`twt_reviewer_agent.md`) — saturated with the derivation; a refuting
    verdict must compute or is labeled ARGUED;
  - *meta-observer* (`meta_observer.md`) — **starved of the derivation**; asks whether the claim
    is about what it says it is about;
  - *coherence keeper* (`coherence_keeper.md`) — saturated with the whole result set; adjudicates
    collisions symmetrically (the old banked result is allowed to lose);
  - *re-derivation agent* (`rederivation_agent.md`) — receives a claim's bare statement only and
    proves it again unaided; a different route is worth more than agreement;
  - *apparatus auditor* (`removal_auditor_agent.md`) — what does each defensive structure
    prevent, at what cost, and was the spirit of the rules served (spot-check drawn
    content-addressed — the audited party never draws its own sample);
  - *philosopher* (`philosopher_ledger_agent.md`), *archivist*, *external-loop operator*,
    *decision-attention reader*, *register clerk*, and the *coordinator*
    (`coordinator_agent.md`) — the dispatcher that holds state, composes briefs with required
    kill-tests and forecasts, and may push once after a negative return, never in the brief.
- **`prompts/FORMATION_CORE.md`** — the versioned worker formation prefix (byte-stable for
  prompt caching; regenerated into a cached agent type by `scripts/gen_twt_worker_agent.py`).
- **`prompts/manuals/`** — activity manuals (banking carries both the demotion pass and the
  tier-raise pass: claims can be corrected in either direction, and a raise is never admissible
  on argument).
- **`prompts/APPARATUS_MAP.md`** — the organigramme: who holds what, who is starved of what.
- **`scripts/`** — the gates and instruments: `bank.sh` (nothing enters the record except
  through both test suites, the record-invariants gate, and a re-indexed retrieval store),
  `check_records.py` (the sentences that describe the tree are checked against the tree —
  counts by counting, pointers resolve, enacted rulings actually reach the files agents read),
  `honesty_telemetry.py` (verdict-shopping, record durability, refutation rate,
  pre-registration — reported at every bank, never gating), plus the release and generator
  tooling.

## The measured claims this design rests on

Every structure here exists because of a recorded incident, not a principle — the rules files
carry the incidents inline. The load-bearing measurements: same-class self-review found nothing
for a month while cross-class review of identical work surfaced real defects in one session;
a starved re-derivation agent, on its first dispatch, blindly reproduced a numerical result via
an independent closed form *and* strengthened it; checkers' proposed cures were twice refuted by
computation after their diagnoses were confirmed — so diagnosis and cure are priced separately;
and a vacuous check wearing an engine-exact tolerance is a recurring tell that the apparatus now
tests for (every new check ships with a demonstrated failure mode).

## Provenance and scope

This is a **working snapshot**, exported from the TWT programme's tree — file paths inside the
documents reference that tree, and the worked examples are TWT physics. The design goal on
record is **emptyability**: one project-specific folder such that emptying it leaves a complete,
project-agnostic research OS. That migration is specified but not yet executed; until it is,
read this repo as *the apparatus as it actually runs*, TWT-sited, rather than as a packaged
framework.

The physics it produced, with its own executable ground truth (503+ inline-checked primitives),
is at **[github.com/yaerhf/TWT](https://github.com/yaerhf/TWT)**.

## License

Code (`scripts/`) under AGPL-3.0 (`LICENSE`); documents (`prompts/`) under the documentation
license (`LICENSE-DOCS`) — both carried from the TWT repository.
