<!-- DIET-CLASS: GOVERNING -->
# SESSION HANDOFF — read this first

*The apparatus asks every programme to keep one of these and reach it by an explicit pointer.
This is research-ratchet's own. Rewrite the top block whenever the state moves.*

---

## ★ TOP BLOCK — state as of 2026-08-27

**What this repository is.** The generic edition of the apparatus: emptied of the founding
programme's object (TWT), MIT + CC BY 4.0, instantiable in one paste
(`INSTALL.md`). The docket is `WORKLIST.md`; the account that travels is `WHY.md`.

**Where the work stands.** W2, W4, W6, W7 discharged. W1's audit ran and its recommended build
is executed (per-role packs). W5's essay is written; the launch posts are the human's to send.
W3 is blocked on a live programme. **W8 — the benchmark — is designed and not started.**

**The one thing that must not be broken:** the tag `twt-apparatus-20260827` is a permanent
citation anchor — four citations in the founding programme's paper resolve through it (RUL-112).
Never delete, move, or rewrite it.

---

## ★ MY STANDING FENCE — read before doing anything on W8

**I am the MODIFIER, and I am BLIND.** I have not read the benchmark target's answer, its
mathematics, or the recent literature around it, and **I must not.**

**Why the split, and why this side of it.** The scorer's knowledge is the thing compaction must
never blur: a *partially* remembered answer key is worse than either knowing or not knowing —
vague directional knowledge, held without knowing you hold it, is precisely the contamination
the blind exists to prevent, and no summary can be trusted to drop it cleanly. The modifier's
value is apparatus context, and that is durable in files: this handoff, `WORKLIST.md`, the packs,
the manuals, the git history. **A successor can reconstruct apparatus context. It cannot
reconstruct having-not-read-the-article.**

**So, post-compaction self: you inherit the blind.** If the transcript ever appears to contain
the target's answer, treat the measurement as void and say so plainly rather than continuing —
a contaminated run reported honestly is recoverable; one reported clean is not. Methodology
reports are safe to receive; the mathematics is not.

**What the modifier does:** changes the apparatus from written instructions, keeping every
change GENERAL — justifiable for a programme in any field, with no reference to the target.
**What it never does:** hold the key, read the scores as a gradient, or fill an `[OBJECT-SLOT]`
(slots belong to the programme under test).

---

## ★ W8 — the decisions already made, so they are not re-litigated

- **The blind:** no founding tree (its formation prefix *states the target result*), no recent
  literature. Enforce with a `WITHHELD` diet class, not with discipline (`rag/diet.py`).
- **No part of the apparatus may know the target is reachable** — the run must look like
  ordinary research from inside.
- **Measurement:** rank apparatus VERSIONS against a fixed target; relative, not pass/fail.
- **Overfitting risk is small and concentrated** (human coordinator's argument, recorded in W8):
  guard slot content, unjustified numbers, and selection among equally-general changes — not
  everything. **File each instruction before its score is seen**; that closes the selection
  channel cheaply, where coarse scoring did not.
- **The second held-out problem is still unchosen.** Criteria: known answer · recent · a
  DIFFERENT branch from the first · comparable effort. **TWT is not a candidate** — it has no
  known answer to score against, and the apparatus was built on it, so it is the training set,
  not a held-out one. TWT's right role is the **deployment**: its stated target is a kernel
  family compatible with the empirical data and reproducing the numerical results, with the
  input count already structurally reduced from the incumbent's 19+ to roughly 4–6 and the
  kernel itself open behind one named gap.
- **Open, and the human's to decide:** which rung to open on, and the second problem.

---

## ★ THE TWO-SIDED CORRECTION NOW IN THE APPARATUS — do not let either side drift

The programme is correcting a measured pessimism, and the overshoot has its own cost. Both
sides are now built, and they belong together:

- **Against giving up too early:** C-34 (cross-domain reach), **C-35** (literature silence is a
  fact about people, not the problem), `manuals/paths.md` §2-bis (grade by what is MISSING;
  `C-unsearched` for the case the prior actually describes), the post-negative push.
- **Against never giving up:** `coordinator_agent.md` power 8 — **a line's budget is declared
  before it opens**, and when spent the line returns to the human with its residue. Not a
  stopping rule (one was tried and refused: it taxed the crisp declaration of a negative), and
  not the agent's call — *the risk is the human's to pay for*.
- **The guard between them:** disposition sets SEARCH DEPTH and never a tier. Optimism that
  reaches the tier column is a labelling error, not a mood.

---

## ★ HOW TO PICK UP THIS REPOSITORY COLD

1. `README.md` for what it is · `WHY.md` for why it is shaped this way.
2. `WORKLIST.md` — the docket, with the meaning-notes region that is never compressed.
3. `prompts/APPARATUS_MAP.md` §1 for the organigramme, §3 for the tree.
4. Before changing any rule: it lives in `RULES_CORE.md` or `RULES_BY_ROLE.md`, **and the packs
   must be regenerated** (`python scripts/gen_role_packs.py`) or the bank fails.
5. Before claiming anything works: `python scripts/check_records.py --self-test` then
   `python scripts/check_records.py`. And **if you touched the gates or `INSTALL.md`, re-run the
   installer** (W6) — an installer never run is a specification, not an installer.

**The standing lesson of this session, in one line:** every substantive defect found here was
found by *executing* something rather than reading it — the installer, the diet bound, the
pack gate, the retrieval index. Run the thing.
