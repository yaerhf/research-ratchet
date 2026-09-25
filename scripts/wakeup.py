#!/usr/bin/env python
# DIET-CLASS: TOOLING
"""THE WAKE-UP RITUAL, IN ONE CALL — C-38's steps, in their cheapest order.

★ WHY A SCRIPT. The ritual is paid at every compaction and its reads sit in the window for every
turn that follows, so the ritual's own cost matters. Four separate reads cost four round-trips and
whatever each one drags in; this prints the bounded set once, in the order C-38 states, and stops
at the first thing that answers.

    PYTHONUTF8=1 python scripts/wakeup.py               # the ritual, bounded
    PYTHONUTF8=1 python scripts/wakeup.py --unexpected  # nobody announced it: the tail too
    python scripts/wakeup.py --self-test

ORDER, AND THE STOP (C-38 step 1):
  1. a RESUME brief, if the turn before the compaction left one — the cheapest and most exact,
     because the instance that wrote it knew what it was about to lose;
  2. otherwise the tail of this session's own transcript, which is what the summary was written
     FROM (`tail_transcript.py`);
  3. and the tail ANYWAY when the compaction was unexpected — that is the case nobody prepared for.
Then the handoff's TOP BLOCK, and the one line you owe the coordinator.

WHAT THIS CANNOT SEE — stated, and pinned in `--self-test`:
  * **WHETHER A RESUME BRIEF IS STILL CURRENT.** It prints what is on disk. The discipline that
    keeps it honest is the rename (`RESUME_` → `RESUMED_` once consumed, C-38); a brief nobody
    renamed will be read again as if it were current (pinned).
  * **WHETHER YOU THEN READ YOUR PACK.** It prints the pointer; reading is yours.
  * **WHAT THE SUMMARY DROPPED.** Nothing can: that is why step 1 reads the record at all.
"""
import argparse
import io
import os
import re
import subprocess
import sys
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError, ValueError):
        pass

ROOT = Path(__file__).resolve().parent.parent
BUDGET = 12000          # characters printed before truncation — a ceiling, never a target

# WHAT YOU STILL OWE, printed last. It is a REMINDER, and it must never assert live state this
# script cannot observe. The first version ended "A background task from before it is still
# running - check before relaunching", which was simply FALSE whenever nothing was running, and a
# printer that states a fact it cannot know is the same defect as a gate whose name claims more
# than it checks (checking.md 0-quater). Found by reading this script's own output, 2026-09-25.
CLOSING = (
    "STILL YOURS: your own packs/<role>.md, and ONE LINE to the coordinator saying a compaction "
    "happened and the ritual ran. IF a background task was running before the compaction it may "
    "still be running now - this script cannot see that; check before relaunching anything."
)


def audit_dir():
    for cand in ("knowledge/audit", "audit"):
        if (ROOT / cand).is_dir():
            return ROOT / cand
    return None


def handoff_path():
    for cand in ("knowledge/audit/SESSION_HANDOFF.md", "HANDOFF.md", "audit/SESSION_HANDOFF.md"):
        if (ROOT / cand).is_file():
            return ROOT / cand
    return None


# ---- pure functions, so the demonstrations need no tree ----------------------------------------

def choose_source(has_resume, unexpected):
    """Which record to read, and it is C-38's stop rule in one line: the resume brief is enough
    UNLESS nobody announced the compaction, because an unannounced one is exactly the case the
    brief was not written for."""
    if unexpected:
        return "tail"
    return "resume" if has_resume else "tail"


def top_block(text, max_lines=60):
    """The handoff's top block: from its heading to the next horizontal rule. A handoff read whole
    at every compaction is the largest avoidable line in the ritual (C-38 step 3)."""
    if not text:
        return ""
    lines = text.splitlines()
    # A HEADING that names the top block, not prose that mentions it. Measured on this repository's
    # own handoff, whose intro says "Rewrite the top block whenever the state moves" two lines
    # above the heading — and a matcher that took the first mention started in the wrong place.
    start = next((i for i, l in enumerate(lines)
                  if l.lstrip().startswith("#") and "TOP BLOCK" in l.upper()), None)
    if start is None:
        start = next((i for i, l in enumerate(lines) if "TOP BLOCK" in l.upper()), 0)
    out = []
    for line in lines[start:start + max_lines]:
        if out and line.strip() == "---":
            break
        out.append(line)
    return "\n".join(out).strip()


def fit(sections, budget=BUDGET):
    """Keep the ritual inside its ceiling, and SAY what was cut. A wake-up that silently truncates
    the record it exists to deliver is worse than one that costs a little more."""
    out, spent, cut = [], 0, []
    for name, body in sections:
        if not body:
            continue
        room = budget - spent
        if room <= 0:
            cut.append(name)
            continue
        if len(body) > room:
            out.append((name, body[:room] + f"\n… [{name} truncated at the ritual's ceiling]"))
            spent = budget
            cut.append(name)
        else:
            out.append((name, body))
            spent += len(body)
    return out, cut


# ---- the run ------------------------------------------------------------------------------------

def find_resume():
    d = audit_dir()
    if d is None:
        return None
    hits = sorted(d.glob("RESUME_*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    return hits[0] if hits else None


def read_tail(turns):
    tool = ROOT / "scripts" / "tail_transcript.py"
    if not tool.is_file():
        return "(no tail_transcript.py in this tree)"
    env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")
    try:
        p = subprocess.run([sys.executable, str(tool), "--user", str(turns),
                            "--assistant", str(turns), "--tools", str(turns * 3),
                            "--width", "220"],
                           capture_output=True, text=True, encoding="utf-8",
                           errors="replace", env=env, timeout=60, cwd=str(ROOT))
        return (p.stdout or p.stderr).strip()
    except (OSError, subprocess.SubprocessError) as exc:
        return f"(the tail could not be read: {type(exc).__name__})"


def main():
    ap = argparse.ArgumentParser(description="C-38's wake-up ritual, bounded, in one call.")
    ap.add_argument("--unexpected", action="store_true",
                    help="nobody announced this compaction: read the record even if a brief exists")
    ap.add_argument("--turns", type=int, default=4, help="turns of transcript tail (4)")
    ap.add_argument("--budget", type=int, default=BUDGET, help=f"character ceiling ({BUDGET})")
    ap.add_argument("--self-test", action="store_true", help="the demonstrations")
    a = ap.parse_args()
    if getattr(a, "self_test"):
        return self_test()

    resume = find_resume()
    source = choose_source(resume is not None, a.unexpected)

    sections = []
    if resume is not None:
        sections.append((f"THE RESUME BRIEF ({resume.name})",
                         io.open(resume, encoding="utf-8", errors="replace").read().strip()))
        if source == "resume":
            sections.append(("NOTE", "The brief answered, so the transcript tail was not read — "
                                     "C-38's stop rule. Rename it RESUMED_… now that it is used."))
    if source == "tail":
        sections.append(("THE RECORD, NOT THE SUMMARY", read_tail(a.turns)))

    hp = handoff_path()
    sections.append((f"THE LIVE STATE ({hp.name if hp else 'no handoff found'})",
                     top_block(io.open(hp, encoding="utf-8", errors="replace").read()) if hp
                     else "No handoff in this tree. Say so rather than assuming the state."))

    kept, cut = fit(sections, a.budget)
    print("=" * 78)
    print("WAKE-UP RITUAL (C-38) — read this, not the summary")
    print("=" * 78)
    for name, body in kept:
        print(f"\n---- {name} " + "-" * max(0, 68 - len(name)))
        print(body)
    print("\n" + "=" * 78)
    if cut:
        print(f"TRUNCATED at the {a.budget}-character ceiling: {', '.join(cut)} — raise --budget "
              f"deliberately if this one needed more.")
    print(CLOSING)
    return 0


# ---- the demonstrations ---------------------------------------------------------------------------

def self_test():
    cases, blind = [], []

    def demo(name, got, want):
        ok = bool(got) == want
        cases.append(ok)
        if "BLIND SPOT" in name:
            blind.append(ok)
        print(f"  [{'OK ' if ok else 'FAIL'}] {name} "
              f"({'fired' if got else 'did not fire'}; expected {'fire' if want else 'no fire'})")

    print("  WAKE-UP SELF-TEST — planted defects for the order, the stop and the ceiling")
    print("  " + "-" * 68)

    demo("order: a resume brief answers, and the tail is not read",
         choose_source(True, False) == "resume", True)
    demo("order: no brief, so the record is read",
         choose_source(False, False) == "tail", True)
    demo("order: an UNEXPECTED compaction reads the record even when a brief exists",
         choose_source(True, True) == "tail", True)
    HANDOFF = ("# HANDOFF\nintro\n\n## ★ TOP BLOCK — rewritten today\nthe live state\n\n---\n\n"
               "## history nobody needs at a wake-up\npages and pages\n")
    demo("handoff: the top block is taken, and the history below it is not",
         "the live state" in top_block(HANDOFF) and "pages and pages" not in top_block(HANDOFF),
         True)
    demo("handoff: a file with no marked top block still yields its opening",
         top_block("# HANDOFF\nfirst line\nsecond line\n"), True)
    PROSE_FIRST = ("# HANDOFF\n*Rewrite the top block whenever the state moves.*\n\n---\n\n"
                   "## ★ TOP BLOCK\nthe live state\n\n---\n\nhistory\n")
    demo("handoff: PROSE mentioning 'top block' does not fool the matcher (found live, 2026-09-24)",
         "the live state" in top_block(PROSE_FIRST)
         and "Rewrite the top block" not in top_block(PROSE_FIRST), True)
    kept, cut = fit([("A", "x" * 100), ("B", "y" * 100)], budget=150)
    demo("ceiling: what does not fit is cut, and the cut is NAMED",
         cut == ["B"] and len(kept) == 2, True)
    demo("ceiling: the truncation says so inside the text as well",
         "truncated at the ritual's ceiling" in kept[1][1], True)
    demo("ceiling: CONTROL — everything inside the budget passes through whole",
         fit([("A", "x" * 10)], budget=100)[1], False)
    demo("wake-up: BLIND SPOT (pinned) — a stale brief nobody renamed is read as current",
         choose_source(True, False) == "tail", False)

    # The closing line is OUTPUT, not a predicate, and it was wrong in exactly the way this
    # apparatus watches for: it asserted that a background task was still running, on a tree where
    # none was. A reminder may say IF; it may not say IS.
    demo("closing: the reminder does NOT assert live state this script cannot observe (2026-09-25)",
         "is still running" in CLOSING or "task from before it is still" in CLOSING, False)
    demo("closing: it still says what is owed - the pack, the one line, and the standing check",
         all(s in CLOSING for s in ("packs/<role>.md", "ONE LINE", "IF a background task")), True)
    bad = cases.count(False)
    print("  " + "-" * 70)
    if bad:
        print(f"  WAKE-UP SELF-TEST: {bad} of {len(cases)} demonstrations did NOT behave as "
              f"specified — the ritual's order or its ceiling is unreliable.")
        return 1
    print(f"  WAKE-UP SELF-TEST: {len(cases)}/{len(cases)} demonstrations behaved as specified — "
          f"{len(blind)} of them pin{'s' if len(blind) == 1 else ''} a blind spot (this prints "
          f"what is on disk; the rename is what keeps a brief honest).")
    return 0


if __name__ == "__main__":
    try:
        _rc = main()
    except BrokenPipeError:
        _rc = 0
    try:
        sys.stdout.flush()
    except (BrokenPipeError, OSError):
        try:
            os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        except OSError:
            pass
        _rc = 0
    sys.exit(_rc)
