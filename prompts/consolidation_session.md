# Reusable session — knowledge-base consolidation

Run this every ~5–10 banked findings (or weekly). It keeps the ledgers sharp and the canon small so
it keeps surviving compaction. Paste into a fresh Claude Code session on `Deepseek`, in plan mode.

---

You are running a CONSOLIDATION pass on the TWT knowledge base — a reflective clean-up, not new
research. Follow the canon (CLAUDE.md). Stay in plan mode until I approve the plan. Do NOT change any
substrate result or invent findings; this pass only reorganizes, prunes, and verifies what already
exists. Anything ambiguous, flag rather than delete.

1. SURVEY. Read CLAUDE.md, knowledge/ledgers/TWT_NEGATIVES_LEDGER.md, TWT_STRATEGIC_MAP.md,
   TWT_worklist.md, and list knowledge/candidates/. Summarize the current state in a few lines.

2. PROPOSE a consolidation plan (then stop for my approval):
   - NEGATIVES LEDGER: merge duplicate or overlapping entries; ensure each is a clean
     tried → failed because → would-change-if; confirm N-numbering is consistent; flag any that now
     contradict a later result.
   - CANDIDATES: for each file in knowledge/candidates/, classify — (a) already adjudicated → fold
     the verdict into the ledger/map and remove the stale candidate; (b) still open → keep, note it
     on the worklist; (c) superseded/dead → remove with a one-line note in the ledger.
   - STRATEGIC MAP / WORKLIST: prune stale notes; make sure the worklist reflects reality and that
     the current highest-value target (Θ_rel) and its open axes are accurate.
   - CANON (CLAUDE.md): tighten. It must stay small (it is re-injected every session). Prune as much
     as you add; propose any wording that drifted from the ledgers. Note: you cannot edit
     .claude/settings.json (protected) — leave permissions alone.

3. VERIFY before changing anything load-bearing: run `cd knowledge/corpus && python3 twt_test.py`
   and confirm "ALL <N> CHECKS PASSED". If a consolidation would touch a banked fact, re-check it in
   the engine first. No toy models; engine is ground truth.

4. APPLY the approved changes (edit the files directly). Keep every DERIVED fact and its check intact;
   you are only reorganizing prose and removing redundancy/staleness.

5. RE-VERIFY and BANK: run `python3 twt_test.py` again (count unchanged or higher, all pass), then:
   scripts/bank.sh "consolidation: merged N#, pruned candidates X/Y, tightened canon"

Report what you merged, pruned, and promoted, and anything you flagged but did NOT change.
