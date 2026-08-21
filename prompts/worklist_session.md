# Reusable session — worklist-driven (the daily driver)

Paste into a fresh Claude Code session on `Deepseek`, in plan mode. This is the DEFAULT session: it
picks the next item off the roadmap, works it, and keeps the roadmap current. (Use
`theta_rel_session.md` instead when you specifically want to attack Θ_rel; `consolidation_session.md`
to prune.)

---

You are starting a TWT working session. The canon (CLAUDE.md) is loaded — follow it strictly:
NO-SM-RETREAT, the tier discipline, the no-toy rule, the guardrails. This is a WORKLIST-DRIVEN
session: knowledge/ledgers/TWT_worklist.md is the roadmap, and keeping it current is part of the job.
Stay in plan mode through step 3.

1. ORIENT. Read the worklist (V3-era, ~200 lines: WP-MASS-MEASURE, DM-V2-1, W-LIVE-4, W-LIVE-1,
   Paper-2 targets P2-1..P2-8, and the Standing principles block), then skim TWT_STRATEGIC_MAP.md
   (the static/dynamic fault line + sequencing) and the headers of TWT_NEGATIVES_LEDGER.md. The
   V2-era worklist (deep frontier + tiered inventory) is archived at
   `knowledge/ledgers/archive/TWT_worklist_V2era_2026-07-01.md` — consult for historical context
   only. Grade legend: [A] computation-remaining / closable · [B] mechanism-asserted / needs
   construction · [C] needs a new idea · ✅/DERIVED done.

2. SELECT the next item — propose exactly ONE, with reasoning (value × tractability), honoring the
   strategic map's sequencing:
   - Prefer gate-free STRUCTURAL progress and [A] closable items first ("close Layer 1 first") — these
     do not wait on the #1 gap.
   - Θ_rel / Layer-2 value-items are highest value but are ONE big dynamical bet; only take one if you
     have a SYMMETRY SHORTCUT to try (map §4a; precedent s=3), not a piecemeal crank.
   - Honor §C: the TOP is not a mass-verifier; count every tuned parameter; never let "recovers
     structure" slide into "computes a value" (values sit at the #1 gap).
   - Do NOT re-open a quark/dynamical dead end (N1–N9) unless you bring its "would change if" handle.
   - For a [C] needs-a-new-idea item, the right first move is Gemini ideation (step 4), not a solo build.
   State the item, its current grade/status, why now, and the planned approach; then exit plan mode for
   my approval.

3. RETRIEVE the precise context for the chosen item: call the twt.py primitives named on its worklist
   line; pull the relevant paper sections via RAG (python rag/query.py "..." -k 8 — cite
   [source §section]); read any negatives-ledger entry that touches it.

4. WORK. If the item is [B]/[C], get candidate mechanisms / external math from Gemini
   (python gemini/ask_gemini.py "..." [--mode research]) — everything it returns is CANDIDATE. Then
   DERIVE or REFUTE on the substrate. Prefer a symmetry shortcut before full construction. Verify every
   step in the engine (call twt.py primitives or write an MV / e(...) check); any numerical run
   ILLUSTRATES only (no-toy rule). Hold the guardrails (only E=I4·e5; e5 is phase; colour is ℤ3; charge
   from the winding). Tag every result; pressure-test "DERIVED" for substrate-specific vs
   generic-given-one-fact. Fitting a result is acceptable, as long as the method is honestly recorded.

5. REVIEW → CONSENSUS (canon §8a). Before banking anything load-bearing, dispatch the twt-reviewer
   subagent to attack the result (verdict: HOLDS / REFUTED / LOCATED-GAP / OVER-CLAIM). Then reconcile:
   for each point, either ACCEPT the verdict or PUSH BACK with a specific, engine-checked rebuttal
   (cite the primitive/output or canon rule — not insistence), and re-submit any pushback to a FRESH
   twt-reviewer dispatch. Iterate until you and the reviewer AGREE on the tier and scope of every
   point — the engine arbitrates factual disputes; neither side concedes just to agree. If you cannot
   converge in ~3 rounds, STOP and escalate to me with both positions, banking nothing. Only a
   consensus result proceeds.

6. BANK + MAINTAIN THE ROADMAP (this is what lets the next session pick up):
   - Update the item's block in TWT_worklist.md: change its Status (OPEN → LOCATED-GAP /
     RESEARCH-LEAD-CLOSED / etc.), cite the new twt.py primitive/check, and add any NEW sub-items
     you discovered.
   - Update the "Current state" header at the top of the worklist to reflect the new frontier;
     correct the suite-count line to the real number from `python3 twt_test.py`.
   - A DERIVED fact → a new twt.py primitive + a twt_test.py check (confirm the count rises, all pass).
     THEN add a corresponding `(R-NNN)` row to the V3 companion Section 1 (Result Index) — the paper
     body's inline (R-NNN) marker + the Index row are the two edits that graduate a new fact.
     A located gap → append to the negatives ledger (tried → failed because → would change if, next N#).
     A priority shift → update TWT_STRATEGIC_MAP.md.
   - Then: scripts/bank.sh "worklist: <item> -> <new status>; <one-line summary>"

Bottom line each session: ONE worklist item moved forward — closed, located, or sharpened — every step
engine-checked and reviewed, and the worklist + dashboard left accurate for whoever comes next.
Locating a gap precisely or banking a clean negative is not a failure.
