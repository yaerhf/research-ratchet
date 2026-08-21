#!/usr/bin/env bash
# Bank a finding: verify the oracle, rebuild the RAG index, commit the timeline.
# Run from anywhere inside the repo, ON YOUR MACHINE (needs git + the 4090 for embeddings).
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

echo "[1/4] substrate self-checks (twt_test.py + twt_companion_test.py)..."
out="$(cd knowledge/corpus && python twt_test.py 2>&1)"; echo "$out" | tail -14
if ! echo "$out" | grep -qE "ALL [0-9]+ CHECKS PASSED across"; then
  echo ">>> Self-checks FAILED (main engine) — not banking. Fix the oracle first."; exit 1
fi
outc="$(cd knowledge/corpus && python twt_companion_test.py 2>&1)"; echo "$outc" | tail -14
if ! echo "$outc" | grep -qE "ALL [0-9]+ COMPANION CHECKS PASSED across"; then
  echo ">>> Self-checks FAILED (companion engine) — not banking. Fix the oracle first."; exit 1
fi

echo "[2/4] record-invariants gate (prose vs tree; policy 2026-08-13)..."
CHECKS="$(echo "$out" | grep -oE "ALL [0-9]+ CHECKS PASSED" | grep -oE "[0-9]+")"
CHECKSC="$(echo "$outc" | grep -oE "ALL [0-9]+ COMPANION CHECKS PASSED" | grep -oE "[0-9]+")"
if ! python scripts/check_records.py --main "$CHECKS" --companion "$CHECKSC"; then
  echo ">>> RECORD-INVARIANTS FAILED — the records drifted from the tree. Fix the documents (scripts/check_records.py lists the sites), then re-bank."; exit 1
fi

echo "[3/4] rebuilding RAG index (embeddings on the GPU)..."
python rag/ingest.py

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
