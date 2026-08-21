# Reusable session — coherence-audit REMEDIATION (audit → edits)

Turn a coherence_audit report into honest, reviewed edits to the paper, twt.py, canon, and ledgers.
The audit only DIAGNOSED; this session acts on it — carefully, because an audit finding is itself a
reviewer claim that can be wrong. Most fixes are DOWN-TAGGING / rewording so the HEADLINES match the
already-honest files. Run on a branch. Paste into Claude Code on `Deepseek`, in plan mode.
Replace <DATE> with the audit's date.

---

You are remediating Time-Wave Theory against a global coherence audit at
knowledge/reports/coherence_audit_<DATE>.md. Replace the <DATE> based filname with the most recent audit's filename. That report is a set of skeptical referee CLAIMS — treat
each as a PROPOSAL to adjudicate, NOT gospel; a finding can be wrong. Your job: convert the SURVIVING
findings into honest edits with the engine staying green. The audit's own verdict is "make the
headline match the (already-honest) files" — every edit must move a claim toward its TRUE tier, never
away. This is honesty-of-the-record (canon §0a), not new physics. Stay in plan mode through step 3.

0. SAFETY — work on a branch:
   git switch -c fix/coherence-audit-<DATE>   (or a worktree: git worktree add ../Deepseek-remediation -b fix/coherence-audit-<DATE>)

1. INGEST THE AUDIT. Read the full report — especially §2 (fractures), §3 (suspect derivations),
   §5 (frame violations), §6 (proposals). List every proposed change as a discrete line item:
   the claim · the file(s)/primitive(s) it touches · current tier/wording · audit's recommended
   tier/wording.

   DEVELOPER POSITIONS TO VERIFY (NOT to assume) — ask the coordinator's views on the audit. Treat each
   as a PUSHBACK to confirm or refute on the engine before it changes any edit; do not implement on my
   say-so. If a position fails verification, tell me — do not quietly drop it or quietly apply it.

2. ADJUDICATE each item — the §8a consensus loop applies, with the audit as the opening verdict and my
   DEVELOPER POSITIONS as pushbacks. For each, ACCEPT or PUSH BACK with an engine-checked rebuttal
   (verify yourself: e.g. confirm weinberg_sin2() returns the UNIFICATION value 0.375 and that the
   measured 0.231 needs RG running TWT does not supply → the HEADLINE is wrong, the primitive is fine).
   For contested items dispatch twt-reviewer; if you cannot converge in ~3 rounds, STOP and escalate to
   me — do NOT edit that item. Produce the final ACCEPTED edit list; exit plan mode for my approval.

3. (APPROVAL GATE) — I approve the edit list before any file changes.

4. APPLY, by edit type:
   - PRESERVE (do NOT down-tag) — results that genuinely hold stay exactly as strong: charge
     quantization (π₃(S³) winding; GMN a consequence, not an input), the emergent Lorentzian signature
     flip, and the **α–g sibling RELATION g²=4πα/sin²θ_W** (DERIVED — it rests on the gate-free
     sin²θ_W=3/8; weinberg_sin2()=0.375). Honest scope on the last: g's VALUE is GATED (it rides α's #1
     gap; alpha_em_value() raises) and the relation holds at the UNIFICATION scale (run-down to M_Z not
     derived) — but the RELATION itself is solid.
   - SPLIT the "gauge map" finding (the audit conflated two claims): the α–g relation above is solid
     and STAYS; only the gauge-GROUP recovery is overstated → down-tag "T1 gauge map closed" to
     "U(1) + the α–g relation solid; SU(2)_L embedding under-determined; SU(3)/gluon octet owed."
   - DOWN-TAG (the common case): change the TIER and the narrative claim to the true one
     (DERIVED → FRAMING / CANDIDATE / INPUT / FIT) in the paper, strategic map, worklist, and any
     overstated docstring. CRITICAL: do NOT delete or weaken the twt.py asserts — the math they prove
     is still true; you are correcting what the result MEANS and how strongly it is claimed. The suite
     count must NOT drop. (Example: weinberg_sin2() keeps its assert and value 0.375; its docstring and
     the map's "sin²θ_W=3/8 UNCONDITIONAL" gain the scope caveat — GUT-scale; run-down to M_Z and the
     measured 0.231 are NOT derived.)
   - RECONCILE TONE where the map/canon elevate a code-[CANDIDATE]/[ASSERTED] to "DERIVED": lower the
     headline to match the code. Priority: the Θ_rel "four faces" / the CKM↔colour I₄ tie — only the
     colour-U(3) tie is engine-verified; the CKM tie is prose-only (CANDIDATE); "four faces" is a
     conjecture. This is the audit's single biggest coherence risk — fix it first.
   - CANON ↔ PAPER ALIGNMENT where the canon states more than the paper (e.g. "matter = HOLE in the
     carrier-envelope vacuum"): make them agree — either tag it FRAMING in the canon (the positive↔hole
     isomorphism is unconstructed) OR add a FRAMING section to the paper. Ask me which if unsure.
   - NEW ARTIFACTS only if they survived review: add a proposed primitive (e.g. ckm_P_cartan_direction)
     ONLY if it COMPUTES something real — otherwise it is prose; record an N# negative instead. Add the
     N15 negatives-ledger entry as tried → failed because → would change if.
   - CODE HYGIENE: the e5-litmus tension in neutrino_lightness (reduce e5 to phase/ω, or tag FRAMING +
     ledger it); the F3/CKM spatial-R_G re-contamination (fix or flag per the resolved generation
     ontology).

5. VERIFY: run `python3 twt_test.py`. All checks pass AND the count did not drop (down-tagging
   preserves the math). If a check now fails, you changed math, not a tier — revert and reconsider.

6. BANK + TAG:
   scripts/bank.sh "remediation(coherence-audit <DATE>): align overstated headlines to the honest files; reconcile Θ_rel/CKM tone; N15; canon↔paper alignment"
   git tag -a audit-<DATE>-remediated -m "headlines aligned to honest files"
   Merge the branch (git switch main && git merge fix/coherence-audit-<DATE>) once you are satisfied.

Bank nothing the review loop did not agree on. A finding you and the reviewer cannot resolve goes to
me, not into the files.
