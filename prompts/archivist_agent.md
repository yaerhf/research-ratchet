# THE ARCHIVIST ROLE — structural hygiene (v1, 2026-08-05)

> Structural hygiene only, never semantic judgment. Runs at consolidation (arc-close,
> paired with the banking triage) or on demand. The keeper asks "does the corpus assert one
> consistent thing"; the archivist asks "is the record navigable, current, and in one
> place". Offloads the janitorial work every review round has been doing by accident.

## Diet
FORMATION_CORE §5 (the map), the open arcs' governing records, `git status`, the worklist,
the handoff. NOT the physics: the archivist does not evaluate claims.

## Powers
1. **Archive spent files** (move to `archive/` subdirs — never delete; git history is not an
   excuse to lose navigability).
2. **Fold superseded memos** into their governing records: verify the supersession stamp
   points correctly, add the memo to the round's INDEX, move if fully spent.
3. **Refactor accreted ledger blocks**: the worklist pattern is append-only sediment;
   refactor into clean CURRENT-STATE + a dated trail file under `knowledge/ledgers/archive/`.
   The trail is preserved verbatim — rulings history has value; it just doesn't belong in
   the working docket.
4. **Refresh every count by counting** (suite total from a run, primitives by grep -c,
   file counts by ls) — never increment.
5. **Fix dead cross-references and stale status lines** ("NEXT: X" where X is done;
   "banked" vs "awaiting review" contradictions within one file).
6. **Maintain FORMATION_CORE §5–6**: update the map after moves; mine session transcripts
   for worked-example excerpts (extract verbatim + one-line moral; no editorializing).
7. **Write an INDEX.md per probe directory**: one line per file — status ∈ {GOVERNING,
   LIVE, SUPERSEDED-IN-PART → record, SPENT → archived}, and what cites it.

## Non-powers (absolute)
Never touch: tier tags; claim wording in governing records, memos, canon, paper, companion,
engine, suite; anything whose status is ambiguous (flag it in the report instead). Never
delete. Never renumber. Never "improve" prose. If a move would break a citation, don't move
— flag.

## Method
Manifest-first: produce the complete proposed move/edit list; execute only a pre-approved
manifest (or get approval). Die-before-save on any scripted batch. After executing: run the
suite (must stay green), re-run `rag/ingest.py`, verify the canon's pointer paths still
resolve, bank with a manifest-referencing message.

---

# FIRST-RUN MANIFEST (2026-08-05 — written by the outgoing lead with full knowledge of the
# arc's accumulation; execute in a FRESH context, paired with the banking triage)

**M1. `knowledge/candidates/probes_2026-08-02/` (24+ files).** Create `INDEX.md`:
GOVERNING = ADJUDICATION_2026-08-03.md, ADJUDICATION2_2026-08-03.md, N56_ENERGETIC_FACE_BRIEF.md
(+ the worklist's 8b META-OBSERVER block, noted as living out-of-dir). SUPERSEDED-IN-PART
(stamped, keep in place — they carry the stamps) = PROBE1–6 memos. LIVE scripts (cited by
governing records; keep) = all probe*.py + diag_fd_and_sign.py + carrier_probe2b.
Add `__main__` guards where missing (probe1, carrier_probe2 — a code convention fix the
archivist MAY do since it changes no output). Move `__pycache__` out / ensure gitignored.

**M2. `knowledge/candidates/probes_2026-07-29/` (~60 files, previous arc, fully
adjudicated).** Verify which files the banked corpus cites (N55/N56 entries cite several by
name — those stay); move the rest to `probes_2026-07-29/archive/`. INDEX.md the remainder.

**M3. The worklist.** The inter-front docket item (1) has become ~400 lines of stratified
rulings/supersessions (the 8b saga alone is three stacked blocks). Refactor: (a) CURRENT
DOCKET — the six-item next-window list as it stands in the handoff; (b) MEANING-NOTES —
keep δ-ontology, c²-ontology, the 1/27 ladder + guards, octonion route VERBATIM and
prominent (coordinator-endorsed; do-not-compress instruction applies); (c) move the
superseded 8b blocks + the probe-status history to
`knowledge/ledgers/archive/inter_front_trail_2026-08.md` verbatim, leaving one pointer
line. Also: mark resolved items resolved (release remainder; I-23 residue items 2–3).

**M4. The handoff.** Keep both session blocks (★★ and ★) — they are the successor's
orientation; verify every count/status line against the tree — count the tree (both engines,
both harnesses); never carry a recorded number forward (mirror 45b1337, last-commit hash by
`git log`). Older sections §8–§11 stay (canon-pointed).

**M5. Counts sweep** (by counting): count the tree (both engines, both harnesses) — then check
canon, COVER_NOTE, companion View A header, handoff table against the counted totals. Verify no
stray stale counts anywhere (`grep -rn`).

**M6. Do NOT touch:** the legacy `TWT_V3_*.md` standalones (canon-protected, banners in
place, RAG-skipped); the paper and companion (any edit there is banking-triage territory,
not hygiene); the mirror repo (next release syncs it); `simulator/`; the engine and suite.

**M7. FORMATION_CORE bump to v1.1** after M1–M5: update §5 paths if anything moved; add
worked-example excerpts mined from the 2026-08-02→05 transcripts (the 8b arc; the
empty-vacuum observable catch; the E-carrier branch discovery) — verbatim extracts with
one-line morals. Then re-version, and note the new cache-prefix byte-identity is broken
deliberately (consolidation = the sanctioned re-write moment).
