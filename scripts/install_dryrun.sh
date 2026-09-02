#!/usr/bin/env bash
# DIET-CLASS: TOOLING
#
# W6 AS A SCRIPT — the installer executed, not read.
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
# WHAT IT CHECKS, AND WHAT IT CANNOT. It checks that the MACHINERY still runs: that an adopter
# following INSTALL.md today reaches a green first bank. It cannot check that anyone followed
# the METHOD. The gates guard the door, not the wall — do not let this be quoted as more.
#
#     bash scripts/install_dryrun.sh        # exit 0 = a fresh tree reaches a green first bank
set -euo pipefail
SRC="$(cd "$(dirname "$0")/.." && pwd)"
TREE="$(mktemp -d)"
trap 'rm -rf "$TREE"' EXIT
export PYTHONUTF8=1

fail() { echo ">>> DRY-RUN FAILED: $*"; exit 1; }

echo "== install dry-run: $SRC -> $TREE"
cd "$TREE"

# ---- INSTALL.md step 0 — the apparatus into place -------------------------------------
mkdir -p knowledge/prompts
cp -r "$SRC/prompts/." knowledge/prompts/
cp -r "$SRC/scripts" .
cp -r "$SRC/rag" .
rm -f rag/index.json                     # generated, and untracked upstream
cp "$SRC/README.md" knowledge/prompts/APPARATUS_README.md
cp "$SRC/LICENSE" "$SRC/LICENSE-DOCS" knowledge/prompts/

# ---- step 2 — the tree ----------------------------------------------------------------
mkdir -p knowledge/corpus knowledge/ledgers knowledge/audit knowledge/candidates

# ---- step 2b — retrieval, and it must ANSWER ------------------------------------------
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

# ---- step 2b-bis — the packs ----------------------------------------------------------
echo "== [2b-bis] packs"
python scripts/gen_role_packs.py > /dev/null || fail "pack generation failed"
# The launch routine's formation step 4 loads this exact path. A dangling pointer there sends
# every session to RULES_BY_ROLE.md whole — the ~15,600-token file the packs exist to avoid.
[ -f knowledge/prompts/packs/coordinator.md ] || fail "packs/coordinator.md absent — the /coordinator routine's step 4 would dangle"
echo "  12 packs, and the launch routine's target resolves"

# ---- step 2c — the ledgers ------------------------------------------------------------
for f in NEGATIVES_LEDGER WINS_LEDGER RULING_REGISTER FAMILY_TREE CHECKER_CALIBRATION \
         EDIT_REACTION_LEDGER COMPARATIVE_LEDGER PHILOSOPHER_LOG REVERSAL_LEDGER \
         REDUCTIONS_LEDGER PATHS_LEDGER STRATEGIC_MAP; do
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

# ---- step 3 — the canon ---------------------------------------------------------------
cat > CLAUDE.md <<'CANON'
# DRY-RUN — THE CANON (v0)
Apparatus: research-ratchet.
## §0 THE OBJECT
An install dry-run. No object; this tree is never founded.
## §9 LIVE STATE
Read knowledge/audit/SESSION_HANDOFF.md FIRST each session — this pointer is its only path.
CANON

# ---- step 5 — the handoff -------------------------------------------------------------
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

# ---- step 6 — init and the first bank -------------------------------------------------
echo "== [6] init_repo.sh"
bash scripts/init_repo.sh | tail -2
echo "== [6] first bank"
bash scripts/bank.sh "ci: first bank on a fresh tree"
git log --oneline | head -2

echo "== install dry-run PASSED — a fresh tree reaches a green first bank"
