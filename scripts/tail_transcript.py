#!/usr/bin/env python
# DIET-CLASS: TOOLING
"""TAIL THIS SESSION'S OWN TRANSCRIPT — the record the compaction summary was written FROM.

★ WHY THIS EXISTS. A compaction hands the next instance a SUMMARY: an account of the
conversation written by the instance that was about to lose it. A summary keeps what it judged
important, and **the parts it drops leave no gap where they were** — the instance that resumes
cannot know what it lost. The only defence is mechanical: before resuming, read the tail of the
record itself. That is the wake-up ritual (`RULES_CORE.md` C-38); this is its first step.

    PYTHONUTF8=1 python scripts/tail_transcript.py        # the window, newest last
    python scripts/tail_transcript.py --user 10 --tools 60
    python scripts/tail_transcript.py --file <path.jsonl>  # a specific transcript
    python scripts/tail_transcript.py --self-test          # the demonstrations

HOW IT FINDS THE TRANSCRIPT. The harness keeps one JSONL per session under
`~/.claude/projects/<folder>/`. Rather than reproduce the folder-name mangling, this reads each
candidate's own `cwd` field and takes the NEWEST transcript whose `cwd` is this folder. A
mangling rule is a guess about someone else's tool; a field in the file is the file's own answer.

WHAT IT SHOWS: the coordinator's messages, this agent's replies, and its tool calls, in order,
each truncated. Where the transcript records a compaction boundary, it says so, so the reader can
see which turns the summary was made from.

WHAT IT CANNOT SEE — stated, and pinned in `--self-test`:
  * WHAT WAS NEVER WRITTEN DOWN. It reads the transcript, not the world. A decision taken and
    never said, or work done in a subagent's own thread, is not here (pinned).
  * THINKING. Reasoning blocks are skipped: they are long, they are not the record, and the
    ritual wants what was SAID, DECIDED and RUN.
  * TRUTH. It shows what was said, including anything said wrongly. It is a record, not a judge.
  * A WINDOW, NOT A HISTORY. Defaults keep the last few turns of each kind. **The window is the
    safety margin, never the budget** (C-38-bis): what matters belongs in a file, in the turn it
    arose.
"""
import argparse
import io
import json
import os
import sys
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError, ValueError):
        pass


def _closed_pipe_exit(code):
    """A reader that went away is not our error (measured: OSError EINVAL / exit 120)."""
    try:
        sys.stdout.flush()
    except (BrokenPipeError, OSError):
        try:
            os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        except OSError:
            pass
        return 0
    return code


# ---- pure functions over entries, so the demonstrations need no session on disk --------------

def parse_lines(lines):
    """(entries, skipped). A malformed line is skipped and counted, never fatal: a transcript is
    being appended to while this runs, so the last line can be half-written."""
    out, skipped = [], 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except ValueError:
            skipped += 1
    return out, skipped


def transcript_cwd(entries):
    """The folder a transcript belongs to, from the file's own first answer."""
    for e in entries:
        cwd = e.get("cwd")
        if cwd:
            return cwd
    return None


def pick_transcript(candidates, cwd):
    """`candidates` is [(path, mtime, its cwd)] — the newest one belonging to THIS folder, or
    None. Returning None is the honest answer, and the caller says so rather than guessing."""
    here = os.path.normcase(os.path.normpath(str(cwd)))
    mine = [(mtime, path) for path, mtime, c in candidates
            if c and os.path.normcase(os.path.normpath(str(c))) == here]
    return max(mine)[1] if mine else None


def _digest(name, payload, width):
    """One line saying what a tool call actually did."""
    if not isinstance(payload, dict):
        return str(payload)[:width]
    for key in ("command", "file_path", "pattern", "description", "url", "prompt", "query"):
        if payload.get(key):
            text = str(payload[key]).strip().splitlines()
            head = text[0] if text else ""
            more = f" (+{len(text) - 1} more lines)" if len(text) > 1 else ""
            return (head[:width] + more)
    return json.dumps(payload, ensure_ascii=False)[:width]


def _blocks(content):
    return content if isinstance(content, list) else [{"type": "text", "text": content or ""}]


def collect(entries, users=6, assistants=10, tools=30, width=400):
    """The window: the LAST n of each kind, merged back into transcript order.

    Subagent threads (`isSidechain`) are excluded — they are another agent's conversation, and
    this reader answers what happened in THIS one."""
    said, replied, called, marks = [], [], [], []
    for i, e in enumerate(entries):
        if e.get("isSidechain"):
            continue
        if e.get("isCompactSummary") or e.get("subtype") == "compact_boundary":
            marks.append((i, "-- COMPACTION BOUNDARY: the summary was written from the turns "
                             "above --"))
            continue
        kind = e.get("type")
        if kind not in ("user", "assistant"):
            continue
        message = e.get("message") or {}
        # Month-day AND time: a transcript spans days, and two sessions an hour apart on
        # different days read as adjacent without the date.
        stamp = (e.get("timestamp") or "")[5:16].replace("T", " ")
        for b in _blocks(message.get("content")):
            if not isinstance(b, dict):
                continue
            btype = b.get("type")
            if btype == "text" and (b.get("text") or "").strip():
                text = " ".join((b.get("text") or "").split())[:width]
                if kind == "user":
                    said.append((i, f"{stamp}  HUMAN     {text}"))
                else:
                    replied.append((i, f"{stamp}  agent     {text}"))
            elif btype == "tool_use":
                called.append((i, f"{stamp}  [tool] {b.get('name', '?')}: "
                                  f"{_digest(b.get('name'), b.get('input'), width // 2)}"))
            # thinking and tool_result are deliberately not shown (see the header)
    # `tail(x, 0)` must give NOTHING. Measured on the first live run: `x[-0:]` is `x[0:]`, so
    # --tools 0 printed every tool call in the session. A window argument of zero meaning
    # "everything" is the opposite of what it says.
    def tail(seq, n):
        return seq[-n:] if n > 0 else []

    kept = tail(said, users) + tail(replied, assistants) + tail(called, tools) + marks
    lines, previous = [], None
    for _, line in sorted(kept, key=lambda pair: pair[0]):
        if line.startswith("--") and line == previous:
            continue            # one compaction leaves both a boundary and a summary entry
        lines.append(line)
        previous = line
    return lines


# ---- the demonstrations ----------------------------------------------------------------------

def self_test():
    cases, blind = [], []

    def demo(name, got, want):
        ok = bool(got) == want
        cases.append(ok)
        if "BLIND SPOT" in name:
            blind.append(ok)
        print(f"  [{'OK ' if ok else 'FAIL'}] {name} "
              f"({'fired' if got else 'did not fire'}; expected {'fire' if want else 'no fire'})")

    def entry(kind, content, **extra):
        e = {"type": kind, "timestamp": "2026-09-23T09:15:00Z", "cwd": "/tree",
             "message": {"role": kind, "content": content}}
        e.update(extra)
        return e

    HUMAN = entry("user", [{"type": "text", "text": "adopt the ritual"}])
    AGENT = entry("assistant", [{"type": "text", "text": "adopting it now"}])
    THINK = entry("assistant", [{"type": "thinking", "thinking": "SECRET REASONING"}])
    TOOL = entry("assistant", [{"type": "tool_use", "name": "Bash",
                                "input": {"command": "bash scripts/bank.sh 'x'\nsecond line"}}])
    RESULT = entry("user", [{"type": "tool_result", "content": "RECORDS HOLD"}])

    print("  TRANSCRIPT-READER SELF-TEST — planted defects for the window and the finder")
    print("  " + "-" * 68)

    demo("a malformed line is skipped and counted, never fatal",
         parse_lines(['{"type":"user"}', 'half-written {', '']) == ([{"type": "user"}], 1), True)
    demo("the coordinator's words are shown",
         any("adopt the ritual" in l for l in collect([HUMAN])), True)
    demo("a tool call is shown with its name and what it ran",
         any("Bash" in l and "bank.sh" in l for l in collect([TOOL])), True)
    demo("a multi-line command says how much was cut, rather than hiding it",
         any("+1 more lines" in l for l in collect([TOOL])), True)
    demo("reasoning is NOT shown (it is not the record)",
         any("SECRET REASONING" in l for l in collect([THINK])), False)
    demo("tool OUTPUT is not shown either — the window is turns, not results",
         any("RECORDS HOLD" in l for l in collect([RESULT])), False)
    demo("a compaction boundary is marked where it happened",
         any("COMPACTION BOUNDARY" in l
             for l in collect([HUMAN, entry("system", None, subtype="compact_boundary"), AGENT])),
         True)
    MANY = [entry("user", [{"type": "text", "text": f"message {n}"}]) for n in range(5)]
    win = collect(MANY, users=2)
    demo("the window keeps the LAST turns, not the first",
         any("message 4" in l for l in win) and not any("message 0" in l for l in win), True)
    demo("asking for NONE of a kind shows none of it (the -0 slice, found on the first live run)",
         collect(MANY + [TOOL], users=0, tools=0), False)
    demo("one compaction prints ONE boundary line, not one per marker entry",
         len([l for l in collect([HUMAN, entry("system", None, subtype="compact_boundary"),
                                  entry("system", None, isCompactSummary=True), AGENT])
              if "BOUNDARY" in l]) == 1, True)
    demo("order is transcript order, human before the reply it produced",
         collect([HUMAN, AGENT])[0].find("HUMAN") > -1, True)
    demo("the finder takes the newest transcript belonging to THIS folder",
         pick_transcript([("/p/old.jsonl", 1, "/tree"), ("/p/new.jsonl", 2, "/tree"),
                          ("/p/other.jsonl", 3, "/elsewhere")], "/tree") == "/p/new.jsonl", True)
    demo("the finder says nothing rather than guessing when no transcript is this folder's",
         pick_transcript([("/p/other.jsonl", 3, "/elsewhere")], "/tree") is None, True)
    demo("BLIND SPOT (pinned) — a subagent's own thread is not in this window",
         any("ran in a subagent" in l for l in
             collect([entry("assistant", [{"type": "text", "text": "ran in a subagent"}],
                            isSidechain=True)])), False)

    bad = cases.count(False)
    print("  " + "-" * 70)
    if bad:
        print(f"  TRANSCRIPT-READER SELF-TEST: {bad} of {len(cases)} demonstrations did NOT "
              f"behave as specified — the wake-up ritual's first step is unreliable.")
        return 1
    print(f"  TRANSCRIPT-READER SELF-TEST: {len(cases)}/{len(cases)} demonstrations behaved as "
          f"specified — {len(blind)} of them pin{'s' if len(blind) == 1 else ''} a blind spot "
          f"(something this reader is documented NOT to show).")
    return 0


# ---- the run ---------------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Tail this session's own transcript.")
    ap.add_argument("--file", help="a transcript to read instead of finding this folder's")
    ap.add_argument("--user", type=int, default=6, help="coordinator messages to keep (6)")
    ap.add_argument("--assistant", type=int, default=10, help="agent replies to keep (10)")
    ap.add_argument("--tools", type=int, default=30, help="tool calls to keep (30)")
    ap.add_argument("--width", type=int, default=400, help="characters per line (400)")
    ap.add_argument("--self-test", action="store_true", help="the demonstrations; reads nothing")
    a = ap.parse_args()

    if getattr(a, "self_test"):
        return self_test()

    if a.file:
        path = Path(a.file)
        if not path.is_file():
            print(f"no transcript at {path}")
            return 1
    else:
        root = Path.home() / ".claude" / "projects"
        if not root.is_dir():
            print(f"no transcript store at {root} — this harness keeps its sessions elsewhere, "
                  f"so pass --file. The rest of the ritual (your pack, the handoff) still runs.")
            return 1
        candidates = []
        for f in root.glob("*/*.jsonl"):
            try:
                with io.open(f, encoding="utf-8", errors="replace") as fh:
                    head, _ = parse_lines([fh.readline() for _ in range(40)])
                candidates.append((f, f.stat().st_mtime, transcript_cwd(head)))
            except OSError:
                continue
        path = pick_transcript(candidates, Path.cwd())
        if path is None:
            print(f"no transcript under {root} records this folder as its cwd "
                  f"({Path.cwd()}). Nothing to read back: say so rather than trusting the "
                  f"summary, and run the rest of the ritual (your pack, the handoff).")
            return 1

    entries, skipped = parse_lines(
        io.open(path, encoding="utf-8", errors="replace").read().splitlines())
    lines = collect(entries, a.user, a.assistant, a.tools, a.width)
    print(f"== the tail of this session's own record: {path}")
    print(f"   {len(entries)} entries read"
          + (f", {skipped} unparseable line(s) skipped" if skipped else "")
          + f"; window = last {a.user} human, {a.assistant} agent, {a.tools} tool calls.")
    print("   Reasoning, tool output and subagent threads are not shown. Read this, not the "
          "summary, for what was said, decided and run.")
    print("   " + "-" * 74)
    for line in lines:
        print("   " + line)
    print("   " + "-" * 74)
    print("   Then: your pack, the handoff's top block, and one line to the coordinator "
          "saying a compaction happened (C-38).")
    return 0


if __name__ == "__main__":
    try:
        _rc = main()
    except BrokenPipeError:
        _rc = 0
    sys.exit(_closed_pipe_exit(_rc))
