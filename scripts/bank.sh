#!/usr/bin/env bash
# Bank a finding: verify the oracle, rebuild the retrieval index, commit the timeline.
# Run from anywhere inside the repo, ON YOUR MACHINE (needs git + a GPU for embeddings).
# GENERIC EDITION (2026-08-27): the founding programme's working gate, carried as the
# reference implementation — re-point the tree paths at instantiation.
#   scripts/bank.sh "N10: tried X -> failed because Y -> would change if Z"
set -euo pipefail
MSG="${1:-bank: update knowledge base}"
cd "$(git rev-parse --show-toplevel)"

# Windows/Git-Bash: the suites and the record gate print ★/⇒/§; without UTF-8 mode a
# captured run dies on cp1252 and bank.sh silently fails to commit (recorded defect).
export PYTHONUTF8=1

# HONESTY TELEMETRY (R-F, 2026-08-20). REPORTS, NEVER GATES — it always exits 0 and
# `|| true` makes that structural: a telemetry that can block a bank gets removed
# within a week and then measures nothing. It runs HERE, before TREE_SNAPSHOT, because
# it appends its history line to knowledge/audit/HONESTY_TELEMETRY_LOG.tsv — writing
# after the snapshot would trip the sweep guard below and refuse the bank.
# Numbered [0/4], NOT [1/5]: "bank.sh gate [2/4]" is quoted in check_records.py's header,
# in canon §2 and in RUL-024's register row — renumbering the gates would drift all three.
echo "[0/4] honesty telemetry (R-F; reports only, never gates)..."
python scripts/honesty_telemetry.py || true

# Concurrent-edit sweep guard (RUL-024 promotion, 2026-08-13; motivating incident: commit
# 210643e swept another session's uncommitted probe work into an unrelated bank message).
# bank.sh verifies the tree AS IT STANDS AT START; if the tree changes while the suites/RAG
# run (another session, an editor, a subagent), the commit would sweep UNVERIFIED and
# MIS-ATTRIBUTED content. Snapshot now, re-check before committing, refuse on drift.
TREE_SNAPSHOT="$(git status --porcelain | git hash-object --stdin)"

# ★ THE ENGINE GATE — and the state EVERY new programme starts in.
# The harness filenames are the programme's own (the founding programme's were
# twt_test.py / twt_companion_test.py). Override per-run or export in your shell.
MAIN_SUITE="${MAIN_SUITE:-twt_test.py}"
COMPANION_SUITE="${COMPANION_SUITE:-twt_companion_test.py}"
CORPUS_DIR="${CORPUS_DIR:-knowledge/corpus}"
#
# A tree with no engine yet is NOT a broken tree — it is docket item 3, and a new
# programme lives there for its first weeks. But an absent gate must be LOUD: the
# apparatus's own measured failure class is a gate that stopped guarding while
# everything stayed green. Absent engine -> a stated SKIP; present engine that fails
# -> a hard stop with the output. What must never happen is what an install dry-run
# found here on 2026-08-27: `set -euo pipefail` aborting the command substitution
# with NO message, leaving the adopter a truncated line and no diagnosis.
CHECKS=""; CHECKSC=""
if [ ! -f "$CORPUS_DIR/$MAIN_SUITE" ]; then
  echo "[1/4] engine self-checks — SKIPPED: no harness at $CORPUS_DIR/$MAIN_SUITE."
  echo "      This tree has no engine yet. That is an honest state (docket item 3;"
  echo "      manuals/engine.md) and it is NOT a passed gate: until an engine exists"
  echo "      every checker verdict is ARGUED rather than COMPUTED, and the review"
  echo "      layer is running on argument alone. Set MAIN_SUITE / COMPANION_SUITE"
  echo "      (or CORPUS_DIR) once you have one; nothing else needs to change."
else
  echo "[1/4] engine self-checks ($MAIN_SUITE + $COMPANION_SUITE)..."
  if ! out="$(cd "$CORPUS_DIR" && python "$MAIN_SUITE" 2>&1)"; then
    echo "$out" | tail -20
    echo ">>> The MAIN harness did not run to completion — not banking."; exit 1
  fi
  echo "$out" | tail -14
  if ! echo "$out" | grep -qE "ALL [0-9]+ CHECKS PASSED"; then
    echo ">>> Self-checks FAILED (main engine) — not banking. Fix the oracle first."; exit 1
  fi
  CHECKS="$(echo "$out" | grep -oE "ALL [0-9]+ CHECKS PASSED" | grep -oE "[0-9]+" | head -1)"
  if [ -f "$CORPUS_DIR/$COMPANION_SUITE" ]; then
    if ! outc="$(cd "$CORPUS_DIR" && python "$COMPANION_SUITE" 2>&1)"; then
      echo "$outc" | tail -20
      echo ">>> The COMPANION harness did not run to completion — not banking."; exit 1
    fi
    echo "$outc" | tail -14
    if ! echo "$outc" | grep -qE "ALL [0-9]+ COMPANION CHECKS PASSED"; then
      echo ">>> Self-checks FAILED (companion engine) — not banking."; exit 1
    fi
    CHECKSC="$(echo "$outc" | grep -oE "ALL [0-9]+ COMPANION CHECKS PASSED" | grep -oE "[0-9]+" | head -1)"
  else
    echo "      (no companion harness — single-engine tree)"
  fi
fi

echo "[2/4] record-invariants gate (prose vs tree; policy 2026-08-13)..."
# APPARATUS SELF-TEST FIRST (pin, 2026-08-25 consolidation, removal audit §3.3).
# The gate's five apparatus checks (§11b(W), 11c, 11d, 11e, 11f) claim non-vacuity
# ONLY via the planted-defect demonstrations in --self-test — and the removal audit
# measured that the mode was invoked NOWHERE: not here, not in a manual, not in a
# rules file. A refactor that breaks a predicate then leaves all five GREEN AND
# VACUOUS with no detector. Run it before the gate it certifies. Cost: 0.09 s, no
# tree mutation (the mode is pure text predicates by construction).
# The pass line is matched COUNT-AGNOSTICALLY (N/N, not 15/15) so adding a
# demonstration never breaks the gate — the mode is designed to grow.
if ! st_out="$(python scripts/check_records.py --self-test 2>&1)"; then
  echo "$st_out" | tail -30
  echo ">>> APPARATUS SELF-TEST FAILED — a record-invariants check could not be shown to fire"
  echo ">>> on its own planted defect (or a control fired on clean text). The gate below would"
  echo ">>> pass VACUOUSLY. Fix the predicate (scripts/check_records.py self_test()) before banking."; exit 1
fi
if ! echo "$st_out" | grep -qE "SELF-TEST: [0-9]+/[0-9]+ demonstrations behaved as specified"; then
  echo "$st_out" | tail -30
  echo ">>> APPARATUS SELF-TEST did not print its all-behaved-as-specified line — not banking."; exit 1
fi
echo "$st_out" | tail -2
# Counts are passed ONLY when an engine actually printed them — a gate told "0 checks"
# by a tree that has no harness would be checking prose against a number nobody counted.
if [ -n "$CHECKS" ]; then set -- --main "$CHECKS" --companion "${CHECKSC:-0}"; else set --; fi
if ! python scripts/check_records.py "$@"; then
  echo ">>> RECORD-INVARIANTS FAILED — the records drifted from the tree."
  echo ">>> Fix the documents at the sites the gate named above, then re-bank."; exit 1
fi

echo "[3/4] rebuilding the retrieval index..."
# THE RETRIEVAL LAYER IS INSTALLED BY DEFAULT AND IS OPTIONAL BY RULING (2026-08-27).
# It is a real instrument — gate [3/4] keeps the record retrievable, and the
# query-instead-of-bulk-load economics rest on it — but a programme may run without
# it. So its ABSENCE is reported LOUDLY and never silently: an uninstalled instrument
# is an honest state, a gate that quietly stopped guarding is not (the apparatus's own
# measured class: of five raising gates, one was unreachable and both suites stayed
# green). A FAILING ingest still stops the bank, because that is the recorded defect
# this gate exists around: rag/ingest.py can die at the end of a run and leave the
# commit skipped while the printed line looks fine.
if [ -f rag/ingest.py ]; then
  python rag/ingest.py
else
  echo ">>> [3/4] SKIPPED — rag/ingest.py is not present in this tree."
  echo ">>>       The retrieval layer is OPTIONAL but INSTALLED BY DEFAULT; this tree"
  echo ">>>       is running without it. Agents must then READ what they would have"
  echo ">>>       queried, and every 'query the corpus' instruction in the apparatus"
  echo ">>>       (RULES_BY_ROLE #171; manuals/INDEX.md) degrades to a bulk read."
  echo ">>>       Install it:  python rag/ingest.py   (see rag/README.md)"
fi

echo "[4/4] committing timeline..."
TREE_NOW="$(git status --porcelain | git hash-object --stdin)"
if [ "$TREE_NOW" != "$TREE_SNAPSHOT" ]; then
  echo ">>> SWEEP GUARD: the working tree changed while bank.sh was running."
  echo ">>> Committing now would sweep unverified, mis-attributed content into this bank"
  echo ">>> (the 210643e incident class). NOT committing. Re-run bank.sh on the settled tree."
  exit 1
fi
git add -A
if git diff --cached --quiet; then echo "(nothing to commit)"; else git commit -m "$MSG"; fi
echo "Banked: $MSG"
