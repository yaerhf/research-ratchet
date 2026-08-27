<!-- DIET-CLASS: GOVERNING -->
# SESSION HANDOFF — read this first

*The apparatus asks every programme to keep one of these and reach it by an explicit pointer.
This is research-ratchet's own. Rewrite the top block whenever the state moves.*

---

## ★ TOP BLOCK — 2026-08-27, written immediately before a deliberate compaction

**What this repository is.** The generic edition of the apparatus: emptied of its founding
object (the TWT programme), MIT + CC BY 4.0, instantiable in one paste (`INSTALL.md`). Docket:
`WORKLIST.md`. The account that travels: `WHY.md`. Everything is committed and pushed; the tree
was clean at handoff.

**Where the work stands.** W2, W4, W6, W7 discharged. W1's audit ran and its recommended build
shipped (per-role packs, 7k–14.5k tokens saved per dispatch). W5's essay is written and the
launch posts are the human's to send. W3 is blocked on a live programme. **W8 — the benchmark —
is designed in full and not started.**

**W9 — SESSION ZERO, built 2026-08-27, immediately before the first trial run.** `/coordinator`
now checks one thing before anything else: **does `knowledge/audit/FOUNDING_INTERVIEW.md`
exist?** If not, that session IS the founding interview — it interviews the human to settle the
foundations (`manuals/founding_interview.md`), and no worker may be dispatched until the floor
is met. The fence is **refuse, never supply**; the twin rule is **C-36** (the founder's
conviction is not a tractability verdict, as C-35 says the literature's silence is not).
**Nobody has run this with a human yet** — the first trial run is its measurement, and the thing
to watch is whether refuse-never-supply holds when the human asks for help answering.

**★ WHAT IS IN FLIGHT RIGHT NOW.** The human coordinator is searching for a **candidate
benchmark target**: a result published after this model's training cutoff, recent enough that
the literature has not absorbed it, with a known answer they hold and the apparatus does not.
**When they return with one, do not ask for the mathematics.** See the fence below — it is the
single most important thing on this page.

**The one thing that must never be broken:** the tag `twt-apparatus-20260827` is a permanent
citation anchor — four citations in the founding programme's paper resolve through it (RUL-112).
Never delete, move, or rewrite it.

---

## ★ MY STANDING FENCE — read before doing anything on W8

**I am the MODIFIER, and I am BLIND.** I have not read any benchmark target's answer, its
mathematics, or the recent literature around it, and **I must not.**

**Why this side of the split.** The scorer's knowledge is the thing compaction must never blur:
a *partially* remembered answer key is worse than either knowing or not knowing — vague
directional knowledge, held without knowing you hold it, is precisely the contamination the
blind exists to prevent, and no summary can be trusted to drop it cleanly. The modifier's value
is apparatus context, and that is durable in files. **A successor can reconstruct apparatus
context; it cannot reconstruct having-not-read-the-article.**

**So, post-compaction self: you inherit the blind.**
- Methodology reports, campaign accounts, process descriptions — **safe to receive.**
- The target's mathematics, its solution path, its literature — **refuse, and say why.**
- If the transcript ever appears to contain the answer, **treat the measurement as void and say
  so plainly** rather than continuing. A contaminated run reported honestly is recoverable; one
  reported clean is not.

**What the modifier does:** changes the apparatus from written instructions, keeping every
change GENERAL — justifiable for a programme in any field, with no reference to any target.
**What it never does:** hold the key, read scores as a gradient, or fill an `[OBJECT-SLOT]`
(slots belong to the programme under test, never to the apparatus).

---

## ★ W8 — decided, so it is not re-litigated

- **The blind:** no founding tree (its formation prefix *states* the result the founding
  programme cited), no recent literature. Enforce with a `WITHHELD` diet class in `rag/diet.py`
  — tooling, not discipline. *(That class is designed and NOT YET BUILT — it is the first
  concrete task when W8 opens.)*
- **No part of the apparatus may know the target is reachable.** The run must look like ordinary
  research from inside; an apparatus told it is being benchmarked has been told someone believes
  the problem is tractable.
- **Measurement:** rank apparatus VERSIONS against a fixed target. Relative, not pass/fail.
- **Overfitting is small and concentrated** — guard slot content, unjustified numbers, and
  selection among equally-general changes. **File each instruction before its score is seen**;
  that closes the selection channel where coarse scoring did not.
- **Construct-validity limit, recorded as a threat not a preference:** optimising against
  closed-result problems biases the apparatus toward problems that *have* closed results. The
  closed arm stays only because it is the one thing that can RANK; a **second axis** measures
  structural gain with instruments needing no known answer (premise-cost readings, counted input
  economy, debt structure, gaps located vs vague, tier honesty).
- **The second held-out problem is unchosen.** Criteria: known answer · recent · a DIFFERENT
  branch from the first · comparable effort. **TWT is not a candidate** — no known answer to
  score against, and the apparatus was built on it, so it is the training set. TWT's role is the
  **deployment**, and its target is well-posed though open: a kernel family compatible with the
  empirical data and reproducing the numerical results, inputs already structurally reduced from
  the incumbent's 19+ to roughly 4–6, the kernel open behind one named gap.
- **The human's to decide:** which rung to open on, and the second problem.

---

## ★ THE TWO-SIDED CORRECTION — do not let either side drift

- **Against giving up too early:** C-34 (cross-domain reach), **C-35** (literature silence is a
  fact about people, not about the problem), `manuals/paths.md` §2-bis (grade by what is
  MISSING; `C-unsearched` for the case the prior actually describes), the post-negative push.
- **Against never giving up:** power 8 — a line's budget is declared before it opens, and when
  spent the line **REPORTS**. A reporting trigger, never a stop rule: **the apparatus does not
  decide to give up.** Its whole contribution is a good report — spend, residue, what changed in
  the tractability picture, and a recommendation *with its reasons*.
- **The guard between them — power 9, the THREE REGISTERS.** WORKING is **optimistic, always**;
  RANKING and REPORTING are **calibrated** (markedly less pessimistic than the trained default,
  and not overcorrected); DECIDING is **the human's**. Both leaks are labelling errors, not
  moods. Test: *would this grade survive being shown to someone who does not want the project to
  succeed?*

---

## ★ OPERATIONAL NOTES — things this session learned the hard way

- **The loop after any rule change:** edit the source (`RULES_CORE.md` / `RULES_BY_ROLE.md`) →
  `python scripts/gen_role_packs.py` → `python scripts/check_records.py --self-test` →
  `python scripts/check_records.py` → `python rag/ingest.py` → commit. **Skipping the
  regeneration fails the bank** (the pack-currency gate), which is the gate working.
- **Long commit messages break the shell.** Write the message to a file in the scratchpad and
  use `git commit -F <file>`. Apostrophes and long bodies broke two attempts this session.
- **★ THE HEREDOC HALVES BACKSLASHES IN THIS SHELL — measured 2026-08-27, and quoting the
  delimiter (`<<'PY'`) does NOT prevent it.** A patch script written with `"\\n"` (intending a
  literal `\n` in the output file) reached Python as `"\n"` and wrote a REAL newline, producing
  an unterminated string literal; `\\.` in a regex reached Python as `\.` and raised an
  invalid-escape SyntaxWarning. **So: never put a backslash in a heredoc'd patch script.** Use
  the Edit/Write tools for anything containing escapes, or build strings with
  `"\n".join([...])` written by a tool rather than by the shell. This class has now bitten
  three times; that is why it is starred.
- **Never `sed -i` a Python file with regex containing `|`** — one such edit clobbered a region
  of `bank.sh` by matching text the same edit had just inserted. Restore with
  `git checkout <file>` and redo with explicit anchors.
- **The house voice for commits:** dense, narrative, stating the measurement and the reasoning,
  in the apparatus's own idiom. They are part of the record, not labels.

---

## ★ HOW TO PICK THIS UP COLD

1. `README.md` for what it is · `WHY.md` for why it is shaped this way.
2. `WORKLIST.md` — the docket, with a meaning-notes region that is never compressed.
3. `prompts/APPARATUS_MAP.md` §1 organigramme, §3 the tree.
4. Changing a rule: source files, **then regenerate the packs**, or the bank fails.
5. Claiming something works: run the self-test and the gate. **If you touched the gates or
   `INSTALL.md`, re-run the installer** (W6) — an installer never run is a specification.

**The standing lesson of this session, in one line:** every substantive defect found here was
found by **executing** something rather than reading it — the installer, the diet bound, the
pack gate, the retrieval index, the records gate's own self-test. **Run the thing.**

**And its sharpest instance, 2026-08-27:** the founding check shipped, was run once on a real
tree, and reported a **fresh tree FOUNDED** — because it searched for a word that the paragraph
documenting it contains. It read perfectly on the page. **A check that matches its own
documentation verifies nothing**, and nothing but execution finds that.
