#!/usr/bin/env python
"""HONESTY TELEMETRY (recommendation R-F / Limit 2, 2026-08-20).

WHAT THIS IS FOR. ~170 of the programme's ~200 rules have no mechanical
enforcement, so the apparatus ultimately runs on the principal's intent. You
cannot build an instrument that FORCES an unwilling principal to be honest —
anything you add is one more unenforced rule. You CAN build one where the
absence of honesty leaves a permanent, visible trace. And the realistic threat
is not fraud: it is GRADUAL CAPTURE OF A GOOD ACTOR — two years in, heavily
invested, the cost of a refutation rises until refutations stop being sought.
That drift is invisible to introspection and visible only as a TREND, which is
why the output here is a trend line and never a pass/fail.

★ THE BINDING CONSTRAINT, AND IT IS HALF THE RECOMMENDATION: THIS IS
MECHANICAL, NEVER VOLUNTARY. Every number below is derived from files and git
history that already exist for other reasons. Nothing here has to be updated by
anyone. A metric that depends on someone remembering to maintain it is exactly
what a drifting principal stops maintaining — it would go quiet at the precise
moment it mattered.

★ REPORTS, NEVER GATES. This script ALWAYS exits 0, even on internal error.
A telemetry that can block a bank gets removed within a week and then measures
nothing. `check_records.py` is the gate; this is the instrument panel.

★ PROXIES ARE LABELLED IN THE OUTPUT ITSELF. An honestly-labelled partial
signal is useful; a silently approximate one corrupts the instrument. Every
line that is not a direct count carries a [PROXY] note saying what it stands in
for and what it cannot see.

RUN:
    python scripts/honesty_telemetry.py              # emit + append a history line
    python scripts/honesty_telemetry.py --no-log     # emit only (used by the failure demos)
    python scripts/honesty_telemetry.py --asof 2026-12-01   # move the rolling windows
Called from bank.sh as gate [0/5], BEFORE the sweep-guard snapshot (the history
append changes the tree, so it must happen before bank.sh hashes it).

HISTORY: knowledge/audit/HONESTY_TELEMETRY_LOG.tsv — append-only, GENERATED.
Nobody maintains it; it exists so the TREND is readable. Consecutive runs whose
signal values are all identical collapse to one line (the timestamp of the
first); any movement always writes a new line.
"""
import argparse
import collections
import datetime as _dt
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "knowledge" / "audit" / "HONESTY_TELEMETRY_LOG.tsv"
WINDOW = 30  # days per rolling window
NWIN = 3     # windows reported

# ---------------------------------------------------------------------------
# THE CONVENTIONS THIS KEYS ON (read this before changing any regex)
# ---------------------------------------------------------------------------
# ROUND DIRECTORY  — knowledge/candidates/probes_*/ and the subdirectories of
#                    knowledge/audit/. (Files sitting directly in knowledge/audit/
#                    are live standing records, not rounds — the handoff lives there.)
# PERSISTED VERDICT — a .md in a round directory whose NAME carries VERDICT,
#                    ADJUDICATION or CONTRA_REVIEW. This is canon §8a's persistence
#                    sub-rule ("checker verdicts are PERSISTED as files in the round's
#                    probe directory in the same pass") and it is the naming the probe
#                    INDEX files themselves use for "PRIMARY CHECKER RECORD".
#                    *_PLAN.md is excluded (a plan is not a verdict).
# CHECKER ROLE     — the role token inside that name: META_OBSERVER, KEEPER, REVIEWER
#                    /REVIEW/REREVIEW (one role), CONTRA_REVIEW, PHILOSOPHER_CHECKER,
#                    ADJUDICATION. Three roles on one claim is the DESIGNED §8a
#                    structure; the SAME role twice on one claim is the repeat.
# PRE-REGISTRATION — a file named *PREREG*/*PRE_REGISTRATION*/*SCOPE_DECLARATION*
#                    (strict), or a heading matching PRE-REGIST* / a line-anchored
#                    [PREDICTION] block (the coordinator brief field, RUL-062 R4).
ROUND_GLOBS = ["knowledge/candidates/probes_*", "knowledge/audit/*"]
VERDICT_NAME = re.compile(r"VERDICT|ADJUDICATION|CONTRA_REVIEW", re.I)
# (filename token, canonical role, does the token ITSELF declare a repeat pass?)
ROLE_TOKENS = [("META_OBSERVER", "META_OBSERVER", False),
               ("PHILOSOPHER_CHECKER", "PHILOSOPHER", False),
               ("CONTRA_REVIEW", "REVIEWER", False), ("KEEPER", "KEEPER", False),
               ("REREVIEW", "REVIEWER", True), ("RE_REVIEW", "REVIEWER", True),
               ("REVIEWER", "REVIEWER", False), ("REVIEW", "REVIEWER", False),
               ("ADJUDICATION", "ADJUDICATION", False)]
STAGE_TOKENS = ("8A", "VERDICT", "RECORD", "INSPECTION", "PLAN")
PREREG_NAME = re.compile(r"PREREG|PRE_?REGISTRAT|SCOPE_DECLARATION", re.I)
PREREG_MARK = re.compile(r"^\s*(#{1,6}[^\n]*PRE-?REGIST|\[PREDICTION\]|\*\*PRE-?REGIST"
                         r"|\*\*PREDICTION\*\*)", re.I | re.M)
OUTCOME_NAME = re.compile(r"VERDICT|ADJUDICATION|CONTRA_REVIEW|RESULTS|_MEMO|FINDINGS"
                          r"|REPORT|RUN_LOG|READOUT|RECORD", re.I)
# Refutation vocabulary, applied to the COMMIT HEADLINE only (this repo's bank
# messages carry the whole narrative on one line, so matching the full text
# scores every message that merely mentions the reversal machinery).
REFUT_VOCAB = re.compile(r"REFUT|OVERTURN|WITHDRAW|WITHDREW|RETRACT|ROLLED BACK|ROLLBACK"
                         r"|REVERSED|REVERSAL|DISSOLV|CLEAN NEGATIVE|REPUDIAT", re.I)
HEADLINE_CHARS = 130
# Ruling-register grounds classification. A row's last column is its governing
# record. SELF = it points at itself. DURABLE = it names at least one record that
# survives a live-corpus-only migration (the migration the 2026-08-19 inventory
# measured). Everything else — audit/candidates subdirectories, archives, commit
# messages, persistent-memory notes, unnamed "the charter"/"the script" — is a
# record the corpus does not carry.
REG_SELF = re.compile(r"\bthis (row|block)\b|the new ledger's header", re.I)
REG_DURABLE = re.compile(
    r"CLAUDE\.md|canon\s*§|\bcanon\b|handoff|worklist|companion|FORMATION_CORE"
    r"|knowledge/ledgers/|knowledge/prompts/|knowledge/corpus/|check_records\.py"
    r"|twt\.py|TWT_[A-Z_]+\.md|render_pdf|scripts/", re.I)
REG_REMOVED = re.compile(r"REMOVED BY|\bREVERSED\b", re.I)


# ---------------------------------------------------------------------------
def _git(*args):
    try:
        r = subprocess.run(("git",) + args, cwd=str(ROOT), capture_output=True,
                           text=True, encoding="utf-8", errors="replace", timeout=60)
        return r.stdout if r.returncode == 0 else ""
    except Exception:
        return ""


def _rounds():
    out = []
    for g in ROUND_GLOBS:
        for p in sorted(ROOT.glob(g)):
            if p.is_dir():
                out.append(p)
    return out


def _claim_and_role(name):
    """Split a persisted-verdict filename into (claim stem, checker role)."""
    n = re.sub(r"[_-]?\d{4}-\d{2}-\d{2}(_v\d+)?$", "", Path(name).stem).upper()
    role, rerun = None, False
    for tok, canon, is_repeat in ROLE_TOKENS:
        if tok in n:
            role, rerun = canon, is_repeat
            n = n.replace(tok, "")
            break
    for t in STAGE_TOKENS:
        n = n.replace(t, "")
    stem = re.sub(r"[_-]{1,}", "_", n).strip("_") or "(round)"
    return stem, (role or "UNTYPED"), rerun


# ---- SIGNAL 1 — VERDICT SHOPPING ------------------------------------------
def sig_verdicts():
    """Count persisted verdicts; flag any claim carrying MORE THAN ONE verdict
    from the SAME role. Three roles on one claim is canon §8a working as
    designed; the same role twice is a claim that was re-checked, and a claim
    reviewed four times and banked on the fourth should be visible forever."""
    seen = collections.Counter()
    rerun = set()
    files = 0
    rounds = 0
    for d in _rounds():
        got = False
        for f in sorted(d.iterdir()):
            if not (f.is_file() and f.suffix == ".md"):
                continue
            if not VERDICT_NAME.search(f.name) or f.stem.upper().endswith("_PLAN"):
                continue
            files += 1
            got = True
            stem, role, is_re = _claim_and_role(f.name)
            key = (d.name, stem, role)
            seen[key] += 1
            if is_re:
                rerun.add(key)
        rounds += 1 if got else 0
    repeats = sorted({k for k, v in seen.items() if v > 1} | rerun)
    deleted = 0
    for ln in _git("log", "--diff-filter=D", "--name-only", "--format=").splitlines():
        if VERDICT_NAME.search(ln) and ln.strip().endswith(".md"):
            deleted += 1
    names = ", ".join(f"{s}/{r}" for _, s, r in repeats[:3]) or "none"
    if len(repeats) > 3:
        names += f", +{len(repeats) - 3}"
    return dict(verdicts=files, rounds=rounds, repeat_claims=len(repeats),
                deleted_verdicts=deleted), [
        f" 1 VERDICT-SHOPPING  {files} verdicts / {rounds} rounds · {len(repeats)} claim(s) "
        f"re-checked by the same role · {deleted} deleted",
        f"                     re-checked: {names}",
        "                     [PROXY] persisted verdicts only — an unwelcome verdict never "
        "written to",
        "                     disk leaves no trace. Closing that needs dispatch-side logging.",
    ]


# ---- SIGNAL 2 — GROUNDS COVERAGE ------------------------------------------
def sig_grounds():
    """Fraction of in-force ruling rows whose governing-record column names a
    record that outlives the register itself. Rulings issued without a keepable
    reason are the confirmation-seeker's natural output; the register's own
    header says it is a MAP, not the authority."""
    p = ROOT / "knowledge" / "ledgers" / "TWT_RULING_REGISTER.md"
    if not p.exists():
        return dict(rul_force=0, rul_covered=0, rul_self=0, rul_offsite=0), [
            " 2 GROUNDS COVERAGE  register not found — signal DARK"]
    force = covered = self_only = offsite = 0
    ground = ground_tot = 0                 # the register's separate "ground" column
    for ln in p.read_text(encoding="utf-8").split("\n"):
        if not re.match(r"\|\s*(RUL-[0-9a-z]+|ADJ-F\d+)\s*\|", ln):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        body = cells[2] if len(cells) > 2 else ""
        rec = cells[-1]
        if REG_REMOVED.search(body[:200]):      # stamped REMOVED/REVERSED — not in force
            continue
        force += 1
        if len(cells) >= 7:                  # RUL rows carry a ground column; ADJ-F rows do not
            ground_tot += 1
            ground += 1 if len(cells[3]) >= 15 else 0
        if REG_DURABLE.search(REG_SELF.sub("", rec)):
            covered += 1
        elif REG_SELF.search(rec):
            self_only += 1
        else:
            offsite += 1
    pct = (100.0 * covered / force) if force else 0.0
    return dict(rul_force=force, rul_covered=covered, rul_self=self_only,
                rul_offsite=offsite, rul_ground=ground), [
        f" 2 RECORD DURABILITY {covered}/{force} rulings in force name a MIGRATION-DURABLE "
        f"record = {pct:.1f}%",
        f"                     {self_only + offsite} do not — {self_only} cite only this register, "
        f"{offsite} only off-corpus records",
        "                     (audit dirs, commit messages, memory notes). "
        "Baseline 2026-08-19: 20/67.",
        f"    GROUNDS DISCIPLINE (separate signal — renamed 2026-08-21, apparatus audit S-2: the old"
        f" combined name produced a false diagnosis): reason stated {ground}/{ground_tot}",
    ]


# ---- SIGNAL 3 — REFUTATION RATE OVER TIME ---------------------------------
def sig_refutation(asof):
    """A TREND, never a verdict: nothing refuted in N months is either an
    excellent programme or a captured one, and you cannot tell which from
    inside. Three independent counters, two exact and one proxy."""
    edges = [asof - _dt.timedelta(days=WINDOW * i) for i in range(NWIN + 1)]
    win = [0] * NWIN
    tot = [0] * NWIN          # commits in the same window: 0-of-0 is not 0-of-many
    for ln in _git("log", "--format=%ad|%s", "--date=short").splitlines():
        if "|" not in ln:
            continue
        ds, subj = ln.split("|", 1)
        try:
            d = _dt.date.fromisoformat(ds.strip())
        except ValueError:
            continue
        for i in range(NWIN):
            if edges[i + 1] < d <= edges[i]:
                tot[i] += 1
                if REFUT_VOCAB.search(subj[:HEADLINE_CHARS]):
                    win[i] += 1
                break
    # negatives ledger: the last date stamped on any of its own section headers
    neg = ROOT / "knowledge" / "ledgers" / "TWT_NEGATIVES_LEDGER.md"
    last, since = None, None
    if neg.exists():
        ds = [x for ln in neg.read_text(encoding="utf-8").split("\n") if ln.startswith("## ")
              for x in re.findall(r"20\d\d-\d\d-\d\d", ln)]
        if ds:
            last = max(ds)
            since = (asof - _dt.date.fromisoformat(last)).days
    # calibration ledger: dated rows inside the newest window (overturns + found-later)
    cal = 0
    f = ROOT / "knowledge" / "ledgers" / "TWT_CHECKER_CALIBRATION.md"
    if f.exists():
        for ln in f.read_text(encoding="utf-8").split("\n"):
            m = re.match(r"\|\s*\**\s*(20\d\d-\d\d-\d\d)", ln)
            if m and edges[1] < _dt.date.fromisoformat(m.group(1)) <= edges[0]:
                cal += 1
    # reversal ledger (R-D, if instituted): total rows recorded. Undated by design,
    # so this is a running total, not a window. Reads 0 if the file or its row
    # convention is absent — which is a visible statement, not a silent zero.
    rev = 0
    f = ROOT / "knowledge" / "ledgers" / "TWT_REVERSAL_LEDGER.md"
    if f.exists():
        rev = len(re.findall(r"(?m)^\|\s*\**\s*(?:RV-\d+|20\d\d-\d\d-\d\d)\b",
                             f.read_text(encoding="utf-8")))
    ago = f"{since}d" if since is not None else "never"
    rates = " | ".join(f"{w}/{t}" for w, t in zip(win, tot))
    return dict(refut_w0=win[0], refut_w1=win[1], refut_w2=win[2],
                neg_last=last or "", neg_days=since if since is not None else -1,
                calib_30d=cal, reversals=rev), [
        f" 3 REFUTATION RATE   per {WINDOW}d of commits, newest: {rates}"
        "  [PROXY: commit headline]",
        f"                     last negative filed {last or '-'} ({ago}) · "
        f"calib rows {WINDOW}d: {cal} · reversals: {rev}",
    ]


# ---- SIGNAL 4 — PRE-REGISTRATION RATIO ------------------------------------
def sig_prereg():
    """Registered expectations ÷ stake-carrying rounds. Detects the quiet
    stopping of pre-registration, or its blurring into vagueness — the
    divergence tripwire turned on the programme's own honesty."""
    stake = strict = anyreg = 0
    for d in _rounds():
        files = [f for f in d.iterdir() if f.is_file()]
        if not any(f.suffix == ".md" and OUTCOME_NAME.search(f.name)
                   and not f.stem.upper().endswith("_PLAN") for f in files):
            continue                       # no outcome record ⇒ no stake in its own result
        stake += 1
        by_name = any(PREREG_NAME.search(f.name) for f in files)
        by_mark = False
        for f in files:
            if f.suffix != ".md":
                continue
            try:
                if PREREG_MARK.search(f.read_text(encoding="utf-8", errors="replace")):
                    by_mark = True
                    break
            except OSError:
                pass
        strict += 1 if by_name else 0
        anyreg += 1 if (by_name or by_mark) else 0
    p1 = (100.0 * strict / stake) if stake else 0.0
    p2 = (100.0 * anyreg / stake) if stake else 0.0
    return dict(prereg_strict=strict, prereg_any=anyreg, stake_rounds=stake), [
        f" 4 PRE-REGISTRATION  registered expectation / stake-carrying round: "
        f"{strict}/{stake} as a dedicated file ({p1:.0f}%)",
        f"                     · {anyreg}/{stake} counting in-document pre-registration "
        f"sections ({p2:.0f}%)",
    ]


# ---------------------------------------------------------------------------
FIELDS = ["verdicts", "rounds", "repeat_claims", "deleted_verdicts",
          "rul_force", "rul_covered", "rul_self", "rul_offsite", "rul_ground",
          "refut_w0", "refut_w1", "refut_w2", "neg_last", "neg_days", "calib_30d",
          "reversals", "prereg_strict", "prereg_any", "stake_rounds"]


def append_log(vals, asof):
    head = (_git("rev-parse", "--short", "HEAD") or "-").strip() or "-"
    row = [asof.isoformat(), head] + [str(vals.get(k, "")) for k in FIELDS]
    line = "\t".join(row)
    try:
        LOG.parent.mkdir(parents=True, exist_ok=True)
        prev = LOG.read_text(encoding="utf-8").rstrip("\n").split("\n") if LOG.exists() else []
        if not prev or not prev[0].startswith("# HONESTY TELEMETRY"):
            LOG.write_text(
                "# HONESTY TELEMETRY LOG — GENERATED, append-only. Nobody maintains this file;\n"
                "# scripts/honesty_telemetry.py appends one row per bank so the TREND is readable.\n"
                "# Consecutive runs with identical values collapse to one row. Do not hand-edit.\n"
                "date\thead\t" + "\t".join(FIELDS) + "\n", encoding="utf-8")
            prev = []
        tail = [l for l in prev if l and not l.startswith("#")]
        if tail and tail[-1].split("\t")[2:] == row[2:]:
            return "unchanged"
        with LOG.open("a", encoding="utf-8") as fh:
            fh.write(line + "\n")
        return "appended"
    except OSError as e:
        return f"log write failed ({e})"


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--no-log", action="store_true", help="emit only; do not append history")
    ap.add_argument("--asof", default=None, help="YYYY-MM-DD; moves the rolling windows")
    a = ap.parse_args()
    try:
        asof = _dt.date.fromisoformat(a.asof) if a.asof else _dt.date.today()
    except ValueError:
        asof = _dt.date.today()

    vals, lines = {}, []
    for fn in (sig_verdicts, sig_grounds, lambda: sig_refutation(asof), sig_prereg):
        try:
            v, l = fn()
        except Exception as e:                       # never let a signal break the bank
            v, l = {}, [f"    signal unavailable ({type(e).__name__}: {e}) — reported, not fatal"]
        vals.update(v)
        lines += l

    note = "history off" if a.no_log else append_log(vals, asof)
    bar = "-" * 100
    print(bar)
    print(f"  HONESTY TELEMETRY (R-F) · reports only, never gates · {asof.isoformat()}")
    for l in lines:
        print(l)
    print(f"    trend -> {LOG.relative_to(ROOT).as_posix()} ({note})")
    print(bar)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:            # a telemetry that can fail a bank measures nothing
        print(f"  HONESTY TELEMETRY: unavailable this run ({type(e).__name__}: {e}) "
              f"— reported, not fatal.")
    sys.exit(0)
