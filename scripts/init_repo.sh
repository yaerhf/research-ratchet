#!/usr/bin/env bash
# One-time: initialize the git timeline. Run ON YOUR MACHINE (host git, not the Cowork sandbox).
# If a partial/corrupt .git exists from a sandbox attempt, delete it first:  rm -rf .git
set -euo pipefail
cd "$(cd "$(dirname "$0")/.." && pwd)"
[ -d .git ] && { echo ".git already exists — aborting (rm -rf .git to start over)"; exit 1; }

# IDENTITY PREFLIGHT (added 2026-08-27, from the install dry-run). Without it this script
# fails MID-WAY on a box with no git identity: the repo is initialized, the commit fails,
# `git branch -M main` then errors on a branch with no commits, and the closing
# "Initialized on 'main'" line would be a lie. Check before touching anything.
if ! git config user.email >/dev/null 2>&1 && ! git config --global user.email >/dev/null 2>&1; then
  echo "git has no user.email configured, so the first commit would fail and leave this"
  echo "tree half-initialized. Set an identity first, then re-run:"
  echo "    git config --global user.email \"you@example.com\""
  echo "    git config --global user.name  \"Your Name\""
  exit 1
fi

# A .gitignore BEFORE the first `git add -A`, or the tree tracks its own generated
# artifacts. Measured in the 2026-08-27 install dry-run: with the retrieval index
# tracked, bank.sh gate [3/4] rewrites it mid-run, the sweep guard correctly sees the
# tree change under its feet, and EVERY bank after a content change needs a second run.
# The guard is right; the tracked generated file is the defect.
if [ ! -f .gitignore ]; then
  cat > .gitignore <<'IGNORE'
# GENERATED — rebuilt by `python rag/ingest.py` (bank.sh gate [3/4]) at every bank.
# Tracking it makes the sweep guard fire on every bank; see scripts/init_repo.sh.
rag/index.json

__pycache__/
*.pyc

# The RUNNABLE agent surfaces. Durable copies live in knowledge/prompts/ and are the
# source of truth — each role spec's header carries the restore rule, because `.claude/`
# not surviving a fresh clone is a recorded failure.
.claude/

# Local render output.
knowledge/corpus/pdf/
IGNORE
  echo "wrote .gitignore (generated artifacts, agent surfaces, render output)"
fi

git init -q
git add -A
git commit -q -m "programme scaffold: canon, corpus, retrieval, ideation advisor, scripts"
git branch -M main
echo "Initialized on 'main'. Tag milestones with:  git tag -a v1 -m '...'"
echo "Parallel work:  git worktree add ../<project>-explore -b explore/<topic>"
