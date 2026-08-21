#!/usr/bin/env bash
# One-time: initialize the git timeline. Run ON YOUR MACHINE (host git, not the Cowork sandbox).
# If a partial/corrupt .git exists from a sandbox attempt, delete it first:  rm -rf .git
set -euo pipefail
cd "$(cd "$(dirname "$0")/.." && pwd)"
[ -d .git ] && { echo ".git already exists — aborting (rm -rf .git to start over)"; exit 1; }
git init -q
git add -A
git commit -q -m "TWT scaffold: canon, corpus, RAG, Gemini advisor, scripts"
git branch -M main
echo "Initialized on 'main'. Tag milestones with:  git tag -a v1 -m '...'"
echo "Parallel work:  git worktree add ../Deepseek-explore -b explore/<topic>"
