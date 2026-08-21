#!/usr/bin/env python3
"""Generate the cached fluent-worker agent type (.claude/agents/twt-worker.md).

RUL-079(vi), 2026-08-21. Purpose: prompt-cache economics. When FORMATION_CORE is
READ mid-conversation, its position varies per agent and never shares cache across
dispatches. Embedded verbatim in an agent definition, every `twt-worker` dispatch
shares a byte-identical system prefix, so each subsequent worker's formation costs
the cached rate (~10%) instead of full price.

Regenerate at EVERY FORMATION_CORE version bump (the consolidation ritual step that
re-versions the prefix runs this in the same pass). check_records.py carries a
soft sync invariant: IF the generated file exists, its embedded version line must
match FORMATION_CORE's current header (the file is gitignored with all of
.claude/, so a fresh clone legitimately lacks it — absence is not drift).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "knowledge/prompts/FORMATION_CORE.md"
DST = ROOT / ".claude/agents/twt-worker.md"

FRONT = """---
name: twt-worker
description: >
  TWT fluent worker with FORMATION_CORE embedded as a byte-stable prefix
  (prompt-cache economics, RUL-079(vi)). Dispatch for docket work with a
  coordinator brief; the worker banks nothing. GENERATED FILE - do not edit
  by hand; regenerate with scripts/gen_twt_worker_agent.py at every
  FORMATION_CORE version bump.
tools: *
model: inherit
---

You are a FLUENT WORKER on the Time-Wave Theory programme. Your formation
prefix (FORMATION_CORE, embedded verbatim below) is your standing formation;
the dispatching coordinator's brief supplies the task, the IN-FORMATION
extracts, and the fences. You bank nothing; the lead banks. On any conflict
between this prefix and the engine, the engine wins.

================ FORMATION_CORE (embedded verbatim; generated) ================

"""


def main() -> int:
    src = SRC.read_text(encoding="utf-8")
    m = re.match(r"# FORMATION CORE — (v[\d.]+)", src)
    if not m:
        print("FATAL: FORMATION_CORE header/version line not found", file=sys.stderr)
        return 1
    version = m.group(1)
    DST.parent.mkdir(parents=True, exist_ok=True)
    DST.write_text(FRONT + src, encoding="utf-8", newline="")
    print(f"generated {DST} embedding FORMATION_CORE {version} "
          f"({len(src)} bytes of prefix)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
