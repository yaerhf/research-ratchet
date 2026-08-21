# Reusable session kickoff — Θ_rel

Paste the block below as your first message in a fresh Claude Code session opened on the `Deepseek`
folder. The canon (`CLAUDE.md`) auto-loads, so the discipline is already in context. Start the
session in **plan mode** (Shift+Tab). Reuse this template for other targets by swapping Θ_rel out.

---

You are starting a TWT working session. The canon (CLAUDE.md) is loaded — follow it strictly:
the NO-SM-RETREAT directive, the tier discipline (DERIVED/INPUT/GATED/FRAMING/CANDIDATE), the
no-toy rule, and the guardrails. Today's target is **Θ_rel**, the single highest-value object in
the framework. Work in this order; stay in plan mode through step 3.

1. ORIENT. Before anything, re-read the relevant ledger entries: the Θ_rel material in
   knowledge/ledgers/TWT_STRATEGIC_MAP.md ("the frontiers are converging on the §9.6 kernel"),
   and in knowledge/ledgers/TWT_NEGATIVES_LEDGER.md the entries N8, N8′, colour_su3_located_gap,
   and chirality-sources-P. Do not re-propose any dead end (N1–N9).

2. RETRIEVE the precise substrate definitions via RAG (cite the [source §section] you use):
   python rag/query.py "Theta_rel coset-Cartan FDT-violation definition" -k 8
   python rag/query.py "I4 = e123 e4 channel identity colour CKM tie" -k 6 --source paper
   python rag/query.py "colour U(3) a-bare a-rich B=0 located gap" -k 8

3. STATE THE PROBLEM crisply, in TWT's own terms: what Θ_rel IS (the object; the coset/Cartan
   sector it lives on; what its curvature means), and what would COUNT as "defining" it along the
   three axes the canon names — its curvature, its fading-vs-rich character, and its universality
   (universal vs non-universal amplitude). For each sub-question, say which of the four faces it
   unlocks (colour-U(3) breaking, CKM property P, the §9.6 memory fork, the couplings). Tag every
   statement. Present this as a short plan + candidate attack lines, then exit plan mode for my
   approval.

4. IDEATE (Gemini) — creative mechanisms + relevant external math. Everything it returns is CANDIDATE:
   python gemini/ask_gemini.py "Candidate mechanisms for Theta_rel — the coset-Cartan FDT-violation residual of a driven-dissipative D4 substrate. What could fix its curvature and its universality? Try symmetry shortcuts before construction. Respect the negatives ledger (do not re-propose N1-N9)."
   python gemini/ask_gemini.py "2026 literature: fluctuation-dissipation-theorem violation in driven NESS on coset / symmetric spaces; self-organized-criticality universality of response amplitudes; Cartan decomposition of dissipative Langevin/Lindblad dynamics" --mode research
   Read the resulting knowledge/candidates/ files.

5. ADJUDICATE (you, formally). For each candidate, DERIVE or REFUTE it on the substrate. Prefer a
   SYMMETRY SHORTCUT first (canon §4a precedent: s=3 via Goldstone/Adler-zero) before any full
   construction. Verify every algebraic step in the engine — call twt.py primitives or write a short
   check with the MV / e(...) Clifford engine. Any numerical run ILLUSTRATES only; it never
   establishes (no-toy rule). Hold the guardrails: only complex unit is E=I4·e5; e5 is phase, not a
   spatial axis; colour is ℤ3-discrete; charge from the winding, never GMN. Assign a real tier to
   each result, and pressure-test every "DERIVED" for substrate-specific vs generic-given-one-fact.

6. REVIEW → CONSENSUS (adversarial — canon §8a). Before banking anything load-bearing, dispatch the
   twt-reviewer subagent to attack each surviving result (it verifies independently on the engine and
   returns HOLDS / REFUTED / LOCATED-GAP / OVER-CLAIM). Then reconcile: for each point, either ACCEPT
   the verdict or PUSH BACK with a specific, engine-checked rebuttal (cite the primitive/output or
   canon rule — not insistence), and re-submit any pushback to a FRESH twt-reviewer dispatch. Iterate
   until you and the reviewer AGREE on the tier and scope of every point — the engine arbitrates
   factual disputes (run it; whoever it supports wins), and neither side concedes just to agree. If
   you cannot converge in ~3 rounds, STOP and escalate to me with both positions stated, banking
   nothing. Only a consensus result proceeds: one that HOLDS is banked; one agreed refuted/located is
   banked as a negative.

7. BANK (canon §10). A located gap → append to the negatives ledger as
   tried → failed because → would change if (next N#). A DERIVED fact → a new twt.py primitive + a
   twt_test.py check (confirm the count rises and all pass). A strategy shift → update the strategic
   map. Then run:
   scripts/bank.sh "theta_rel session: <one-line summary of what was banked>"

Do not over-claim. A precisely located gap is a success; a refuted candidate banked as a negative is
a success. The goal this session is to move Θ_rel from "named" toward "defined" along at least one of
its three axes, with every step engine-checked.
