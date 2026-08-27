# Reusable session — coherence-audit REMEDIATION (audit → edits)

*(Generic edition, 2026-08-27.)* Turn a `coherence_audit.md` report into honest, reviewed edits
to the paper, the engine, the canon, and the ledgers. The audit only DIAGNOSED; this session
acts on it — carefully, because an audit finding is itself a reviewer claim that can be wrong.
Most fixes are DOWN-TAGGING / rewording so the HEADLINES match the already-honest files. Run on
a branch. Paste into a fresh session, in plan mode. Replace <DATE> with the audit's date.

---

You are remediating the programme against a global coherence audit at
`knowledge/reports/coherence_audit_<DATE>.md` (use the most recent). That report is a set of
skeptical referee CLAIMS — treat each as a PROPOSAL to adjudicate, NOT gospel; a finding can be
wrong. Your job: convert the SURVIVING findings into honest edits with the engine staying
green. The usual audit verdict is "make the headline match the (already-honest) files" — every
edit must move a claim toward its TRUE tier, never away. This is honesty-of-the-record, not new
research. Stay in plan mode through step 3.

0. SAFETY — work on a branch:
   `git switch -c fix/coherence-audit-<DATE>` (or a worktree).

1. INGEST THE AUDIT. Read the full report — especially the fractures, the suspect derivations,
   the frame violations, and the proposals. List every proposed change as a discrete line
   item: the claim · the file(s)/primitive(s) it touches · current tier/wording · the audit's
   recommended tier/wording.

   DEVELOPER POSITIONS TO VERIFY (NOT to assume) — ask the human coordinator's views on the
   audit. Treat each as a PUSHBACK to confirm or refute on the engine before it changes any
   edit; do not implement on say-so. If a position fails verification, say so — do not quietly
   drop it or quietly apply it.

2. ADJUDICATE each item — the §8a consensus loop applies, with the audit as the opening
   verdict and the developer positions as pushbacks. For each, ACCEPT or PUSH BACK with an
   engine-checked rebuttal (verify yourself: run the primitive, confirm what it actually
   returns, and separate "the primitive is fine" from "the headline is wrong"). For contested
   items dispatch the reviewer subagent; if you cannot converge in ~3 rounds, STOP and
   escalate — do NOT edit that item. Produce the final ACCEPTED edit list; exit plan mode for
   approval.

3. (APPROVAL GATE) — the human coordinator approves the edit list before any file changes.

4. APPLY, by edit type:
   - PRESERVE (do NOT down-tag) — results that genuinely hold stay exactly as strong. An
     audit's harshness is not evidence; a result with a gate-free engine identity behind it
     keeps its tier, with its honest scope stated (which quantities ride a gap and raise, and
     at which scale the relation holds).
   - SPLIT conflated findings — an audit often bundles a solid relation with an overstated
     recovery built on it. Down-tag only the overstated half; say so explicitly.
   - DOWN-TAG (the common case): change the TIER and the narrative claim to the true one
     (DERIVED → FRAMING / CANDIDATE / INPUT / FIT) in the paper, the strategic map, the
     worklist, and any overstated docstring. CRITICAL: do NOT delete or weaken the engine
     asserts — the math they prove is still true; you are correcting what the result MEANS and
     how strongly it is claimed. The suite count must NOT drop.
   - RECONCILE TONE where the map/canon elevate a code-CANDIDATE to "DERIVED": lower the
     headline to match the code. Fix the biggest coherence risk first — the audit names it.
   - CANON ↔ PAPER ALIGNMENT where the canon states more than the paper: make them agree —
     either tag it FRAMING in the canon OR add a FRAMING section to the paper. Ask which if
     unsure (canon edits are human-only).
   - NEW ARTIFACTS only if they survived review: add a proposed primitive ONLY if it COMPUTES
     something real — otherwise it is prose; record a negatives-ledger entry instead
     (tried → failed because → would change if).
   - CODE HYGIENE: guardrail-litmus tensions in primitives (reduce to the licensed reading, or
     tag FRAMING + ledger it); re-contaminations of a resolved ontology call (fix or flag per
     the resolution).

5. VERIFY: run the harness. All checks pass AND the count did not drop (down-tagging preserves
   the math). If a check now fails, you changed math, not a tier — revert and reconsider.

6. BANK + TAG:
   `PYTHONUTF8=1 bash scripts/bank.sh "remediation(coherence-audit <DATE>): align overstated headlines to the honest files; <specifics>"`
   `git tag -a audit-<DATE>-remediated -m "headlines aligned to honest files"`
   Merge the branch once satisfied.

Bank nothing the review loop did not agree on. A finding you and the reviewer cannot resolve
goes to the human coordinator, not into the files.
