#!/usr/bin/env bash
# DIET-CLASS: TOOLING
#
# W6 AS A SCRIPT — INSTALL.md's steps, executed on a fresh tree.
#
# ★ WHY THIS EXISTS. W6 is the standing duty "re-run the installer after any change to the
# gates or INSTALL.md", and its history is the argument for automating it: three runs on
# 2026-08-27 found eight defects, a stale-pack refusal, and a founding check that reported a
# fresh tree FOUNDED. But W6 is discharged by REMEMBERING, and the incident that created it
# was precisely a failure of remembering — the toolkit shipped with its central gate red and
# nothing had run it. Everywhere else this apparatus treats "someone will remember" as the
# weakest control class available; here it was the only control on the most expensive failure.
# Named by a cold external review at bf302af (2026-09-02, finding F3).
#
# WHAT IT CHECKS. That the MACHINERY still runs: a fresh tree taken through INSTALL.md's steps
# reaches a green first bank. The steps are TRANSCRIBED here, not read from INSTALL.md, so a guard
# runs first: the steps INSTALL.md declares (its "Step N" headings) must equal the steps this
# script declares (its "INSTALL.md step N" section markers), in the same order, each one
# executed or marked SKIPPED with its reason.
#
# WHAT IT CANNOT SEE — written 2026-09-22, when this header still said "the installer executed,
# not read" and nothing checked the claim:
#   * a command changed INSIDE a transcribed step. The guard checks that every step is here, not
#     that each one still does what INSTALL.md now says;
#   * the steps it declares and does not run (listed at the end of every run, reasons inline);
#   * whether anyone followed the METHOD. The gates guard the door, not the wall — do not let
#     this be quoted as more.
#
#     bash scripts/install_dryrun.sh        # exit 0 = a fresh tree reaches a green first bank
set -euo pipefail
SRC="$(cd "$(dirname "$0")/.." && pwd)"
TREE="$(mktemp -d)"
trap 'rm -rf "$TREE"' EXIT
export PYTHONUTF8=1

fail() { echo ">>> DRY-RUN FAILED: $*"; exit 1; }

echo "== install dry-run: $SRC -> $TREE"

# ---- the transcription guard: every INSTALL.md step accounted for, in order ------------------
# Measured 2026-09-22: this script carried markers for 8 of INSTALL.md's 11 steps. Steps 1, 4 and
# 4c were skipped without a word, while the CI step was named "INSTALL.md executed, not read".
SELF="$SRC/scripts/install_dryrun.sh"
want="$(grep -oE '^#{2,3} Step [0-9][0-9a-z-]*' "$SRC/INSTALL.md" | sed -E 's/^#+ Step //' || true)"
have="$(grep -oE '^# ---- INSTALL\.md step [0-9][0-9a-z-]*' "$SELF" | sed -E 's/^# ---- INSTALL\.md step //' || true)"
skipped="$(grep -E '^# ---- INSTALL\.md step [0-9][0-9a-z-]* .*SKIPPED' "$SELF" \
           | sed -E 's/^# ---- INSTALL\.md step ([0-9][0-9a-z-]*).*/\1/' | paste -sd' ' - || true)"
[ -n "$want" ] || fail "INSTALL.md has no 'Step N' headings: the transcription guard has nothing to compare"
if [ "$want" != "$have" ]; then
  echo "  INSTALL.md declares:  $(echo $want)"
  echo "  this script declares: $(echo $have)"
  fail "INSTALL.md and this dry-run no longer declare the same steps. Add, rename or reorder this script's 'INSTALL.md step N' sections to match, each executed or marked SKIPPED with its reason."
fi
echo "  transcription guard: all $(echo "$want" | wc -l | tr -d ' ') INSTALL.md steps declared here, in order"
cd "$TREE"

# ---- INSTALL.md step 0 — the apparatus into place -------------------------------------
mkdir -p knowledge/prompts
cp -r "$SRC/prompts/." knowledge/prompts/
cp -r "$SRC/scripts" .
cp -r "$SRC/rag" .
rm -f rag/index.json                     # generated, and untracked upstream
cp "$SRC/README.md" knowledge/prompts/APPARATUS_README.md
cp "$SRC/LICENSE" "$SRC/LICENSE-DOCS" knowledge/prompts/

# ---- INSTALL.md step 1 — SKIPPED: the interview is a conversation with a person ------------
# A dry-run has no person to ask. What it can check about this step, it checks below (W9): a
# fresh tree reports NOT FOUNDED, so a launching coordinator's first session IS the interview.

# ---- INSTALL.md step 2 — the tree ----------------------------------------------------------
mkdir -p knowledge/corpus knowledge/ledgers knowledge/audit knowledge/candidates

# ---- INSTALL.md step 2b — retrieval, and it must ANSWER ------------------------------
# The founding programme's measured failure: a documented retrieval command that silently did
# not run on the working box, after which retrieval stayed "available and unused" and every
# read-on-demand instruction degraded into a bulk read. An index that writes is not enough.
echo "== [2b] ingest"
python rag/ingest.py > /dev/null || fail "ingest did not complete"
q_out="$(python rag/query.py "the diet is the role" -k 3 --source prompts)"
case "$q_out" in
  *"hit(s)"*) echo "  retrieval answers on a fresh tree" ;;
  *) fail "retrieval returned no hits on a fresh tree" ;;
esac

# ---- INSTALL.md step 2b-bis — the packs ----------------------------------------------
echo "== [2b-bis] packs"
python scripts/gen_role_packs.py > /dev/null || fail "pack generation failed"
# The launch routine's formation step 4 loads this exact path. A dangling pointer there sends
# every session to RULES_BY_ROLE.md whole — the ~15,600-token file the packs exist to avoid.
[ -f knowledge/prompts/packs/coordinator.md ] || fail "packs/coordinator.md absent — the /coordinator routine's step 4 would dangle"
echo "  12 packs, and the launch routine's target resolves"

# ---- INSTALL.md step 2c — the ledgers ------------------------------------------------
for f in NEGATIVES_LEDGER WINS_LEDGER RULING_REGISTER FAMILY_TREE CHECKER_CALIBRATION \
         EDIT_REACTION_LEDGER COMPARATIVE_LEDGER PHILOSOPHER_LOG REVERSAL_LEDGER \
         REDUCTIONS_LEDGER PATHS_LEDGER STRATEGIC_MAP HUMAN_AGENT_BRIDGE; do
  printf '<!-- DIET-CLASS: LEDGER -->\n# %s\nPurpose: standing ledger.\n' "$f" \
    > "knowledge/ledgers/$f.md"
done
printf '<!-- DIET-CLASS: LEDGER -->\n# worklist\nPurpose: the docket.\n\n| # | item | status |\n|---|---|---|\n| 1 | THE FOUNDING INTERVIEW | |\n' \
  > knowledge/ledgers/worklist.md
# W10 — the dispatch log. Header only; the coordinator appends one row per dispatch.
printf '# utc\trole\tchecker_model\tauthor_model\tclaim_id\tverdict\tverdict_path\n' \
  > knowledge/ledgers/DISPATCH_LOG.tsv

# ---- W10 — an EMPTY log must report RUL-065 as UNMEASURED, not as healthy ---------------
# The failure mode a metric like this invites is printing a reassuring 0% same-class on no
# data. The honest state of a tree that has logged nothing is "unmeasured", and that IS the
# finding — so it is pinned here rather than trusted.
tel_out="$(python scripts/honesty_telemetry.py 2>&1 || true)"
case "$tel_out" in
  *"UNMEASURED"*) echo "  telemetry reports RUL-065 UNMEASURED on an empty log" ;;
  *) fail "an empty dispatch log did not report RUL-065 as UNMEASURED" ;;
esac

# ---- INSTALL.md step 3 — the canon ---------------------------------------------------
cat > CLAUDE.md <<'CANON'
# DRY-RUN — THE CANON (v0)
Apparatus: research-ratchet.
## §0 THE OBJECT
An install dry-run. No object; this tree is never founded.
## §9 LIVE STATE
Read knowledge/audit/SESSION_HANDOFF.md FIRST each session — this pointer is its only path.
CANON

# ---- INSTALL.md step 4 — SKIPPED: the agent surfaces are not yet executed here -------------
# Step 4 copies three role specs into .claude/agents/ (frontmatter at line 1) and writes the
# /coordinator launch routine from a block in INSTALL.md. A first bank needs none of it, which is
# why this script never noticed it skipped them. Executing them, with the routine taken FROM
# INSTALL.md rather than retyped here, is a docket item (W18). Until then this is a stated gap.

# ---- INSTALL.md step 4c — SKIPPED: a fresh tree has no engine ------------------------------
# Step 4c names the harness bank.sh runs once an engine exists. A fresh tree has none, and the
# correct behaviour is that bank.sh says so and carries on, which the first bank at step 6 runs.
# Its other half — a harness NAMED but absent is refused, not skipped — is pinned after step 6.

# ---- INSTALL.md step 5 — the handoff -------------------------------------------------
printf '<!-- DIET-CLASS: GOVERNING -->\n# SESSION HANDOFF — read me first\n## TOP BLOCK\nAPPARATUS INSTANTIATED. NOT YET FOUNDED.\n' \
  > knowledge/audit/SESSION_HANDOFF.md

# ---- W9 — the founding check, asserted in BOTH directions -----------------------------
# ★ THE REGRESSION PIN FOR THE DEFECT OF 2026-08-27. The first version of this check searched
# FORMATION_CORE.md for the stamp — and the template header that EXPLAINS the stamp contains
# the word, so it reported a fresh tree FOUNDED and a launching coordinator would have skipped
# session zero entirely. The signal is the RECORD's existence, which cannot be confused with a
# description of itself. A check that matches its own documentation verifies nothing.
echo "== [W9] the founding check"
[ ! -f knowledge/audit/FOUNDING_INTERVIEW.md ] || fail "fresh tree already carries a founding record"
grep -q "FOUNDING INTERVIEW" knowledge/prompts/manuals/founding_interview.md \
  || fail "the manual the launch routine names is absent or empty"
echo "  a fresh tree reports NOT FOUNDED, and the manual resolves"

# ---- INSTALL.md step 6 — init and the first bank -------------------------------------
echo "== [6] init_repo.sh"
bash scripts/init_repo.sh | tail -2
echo "== [6] first bank"
bash scripts/bank.sh "ci: first bank on a fresh tree"
git log --oneline | head -2

# ---- W18 — a harness named for ANOTHER programme is refused, not skipped ----------------------
# Two programmes on one machine, one engine name exported in a shell profile: the second tree's
# bank looked for the first tree's harness, and answered "this tree has no engine yet" with its
# engine checks skipped. Pinned here so the refusal cannot quietly revert.
echo "== [4c] a harness named but absent stops the bank"
if col_out="$(MAIN_SUITE=another_programme_test.py bash scripts/bank.sh "ci: must not bank" 2>&1)"; then
  fail "a harness named but absent was banked through: the engine checks were silently skipped"
fi
case "$col_out" in
  *"ANOTHER"*"programme"*) echo "  refused, and the message names the likely cause" ;;
  *) fail "the bank stopped without naming the likely cause (a profile export for another programme)" ;;
esac

echo "== install dry-run PASSED — a fresh tree reaches a green first bank"
echo "   INSTALL.md steps declared and NOT run: ${skipped:-none} (reasons at each in scripts/install_dryrun.sh)"
