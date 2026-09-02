#!/usr/bin/env python
# DIET-CLASS: TOOLING
"""RECORD-INVARIANTS gate — the sentences that describe the tree, checked against the tree.

THE POLICY. The suites verify the mathematics; this verifies the PROSE ABOUT THE TREE —
rosters, pointer paths, counts, what-runs-what. Load-bearing tree-state prose is either
GENERATED from the tree or PINNED here as an executable invariant. A drift class caught
twice in prose is a process failure: when a review catches a new one, the fix INCLUDES
adding its invariant here.

★ WHY THIS FILE EXISTS SEPARATELY (generic edition, 2026-08-27) — and the measurement that
forced it. The founding programme's gate is a mature instrument with ~98 pins onto its own
corpus: quoted sentences, engine filenames, section numbers. Shipped unchanged to an adopter
it does not merely fail, it fails WRONGLY. An install dry-run found it crashing with a Python
traceback on a tree that has no engine yet (`ast.parse(None)`), and found its own `--self-test`
RED in the apparatus's own repository — 2 of 28 planted-defect demonstrations pinned to
founding content the generic edition no longer carries. Since `bank.sh` refuses to bank unless
that self-test passes, **the apparatus was shipping with its central gate red, and nothing had
run it since the emptying.**

So the gate is split, honestly:

  * THIS FILE checks the invariant families true of ANY tree — the ledger roster, the manuals
    index, pointer resolution, the handoff's only path, the role roster, diet markers, and
    count-bearing prose. It runs green on a fresh install and on the apparatus repo itself.
  * `scripts/check_records_founding.py` keeps the founding implementation VERBATIM as the
    worked example of what a mature gate becomes once a programme has a corpus to pin. It is
    not run by `bank.sh`. Read it when you are ready to add object-specific pins — that is the
    direction this file is meant to grow.

EVERY CHECK HERE SHIPS WITH A DEMONSTRATED FAILURE MODE (`--self-test`), because a check never
shown able to fail is a phantom cite of the gate class. The predicates are PURE FUNCTIONS OVER
TEXT precisely so a demonstration can plant a defect and watch the check fire without mutating
the tree.

RUN
    python scripts/check_records.py                             # structural invariants
    python scripts/check_records.py --main 412 --companion 81   # + count-bearing prose
    python scripts/check_records.py --self-test                 # the demonstrations
Exit 0 = the records hold. Exit 1 = the prose has drifted; fix the documents.
"""
import argparse
import re
import os
import sys
from pathlib import Path

# THE CONSOLE THIS PRINTS INTO MAY NOT BE UTF-8, and these tools quote DOCUMENTS — whose
# headings carry stars, arrows and em-dashes. On a cp1252 console one such character raised
# UnicodeEncodeError and killed the tool at the moment it had already found the answer.
# The founding programme's measured retrieval failure is exactly this shape: a documented
# command that silently does not run on the working box, after which retrieval stays
# "available and unused". bank.sh exports PYTHONUTF8=1; a human typing the documented form
# does not, so each entry point makes itself safe.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError, ValueError):
        pass


def _closed_pipe_exit(code):
    """Return an exit code that does not treat a CLOSED READER as a failure.

    `python rag/query.py ... | head -3` closes the pipe while we are still writing.
    On POSIX that surfaces as BrokenPipeError at the print; on Windows CPython
    raises OSError EINVAL when it flushes the std streams at interpreter shutdown
    and then exits 120. Either way, under `set -euo pipefail` — which means any
    script and any CI job — a documented, correct invocation fails the run.

    Measured 2026-09-02 (exit 120 on Windows, reproduced at >64 KB of output into
    `head -1`); found by a cold external review, which hit it twice while writing
    the install dry-run. Pointing the fd at the null device is what makes the
    interpreter's own shutdown flush a no-op.
    """
    try:
        sys.stdout.flush()
    except (BrokenPipeError, OSError):
        code = 0
    try:
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
    except (OSError, ValueError):
        pass
    return code


ROOT = Path(__file__).resolve().parent.parent
DRIFT_TOL = 2       # narrative counts may lag the tree by this much between consolidations

FAILS, WARNS, NOTES = [], [], []


def _ck(name, cond, detail=""):
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}")
    if not cond:
        FAILS.append(name)
        if detail:
            print(f"         {detail}")


def _warn(name, cond, detail=""):
    print(f"  [{'OK ' if cond else 'WARN'}] {name}")
    if not cond:
        WARNS.append(name)
        if detail:
            print(f"         {detail}")


def _read(rel):
    p = ROOT / rel
    try:
        return p.read_text(encoding="utf-8", errors="replace") if p.is_file() else None
    except OSError:
        return None


def apparatus_dir():
    """Layout-robust: an instantiated tree keeps the apparatus at knowledge/prompts/, while
    the research-ratchet repository ships it at prompts/. Supporting both is what lets ONE
    gate run before and after instantiation."""
    for cand in ("knowledge/prompts", "prompts"):
        if (ROOT / cand).is_dir():
            return cand
    return None


def is_instantiated():
    """A tree with ledgers has been given an object; the apparatus repository has not."""
    return (ROOT / "knowledge" / "ledgers").is_dir()


# ======================================================================
# THE PREDICATES — pure over text/lists, so --self-test can plant defects.
# ======================================================================
GENERATED_LEDGERS = {"NEGATIVES_INDEX.md"}      # generated on demand; absence is not drift


def roster_unnamed(roster_text, ledger_files):
    """Ledgers on disk that the roster does not name.

    The founding failure this generalizes: a binding sweep rule said "all five ledgers" when
    there were fourteen — under-specifying its own surface by nine files. A ledger nobody
    names is a ledger nobody sweeps."""
    named = set(re.findall(r"([A-Za-z][A-Za-z0-9_]*\.md)", roster_text or ""))
    return sorted({f for f in ledger_files
                   if f.endswith(".md") and f not in named and f not in GENERATED_LEDGERS})


def roster_missing(roster_text, ledger_files):
    """Ledgers the roster names that do not exist (generated ones exempt)."""
    named = set(re.findall(r"`([A-Z][A-Za-z0-9_]*\.md)`", roster_text or ""))
    return sorted(named - set(ledger_files) - GENERATED_LEDGERS)


def manuals_unlisted(index_text, manual_files):
    listed = set(re.findall(r"`([a-z_]+\.md)`", index_text or ""))
    return sorted({f for f in manual_files
                   if f.endswith(".md") and f != "INDEX.md" and f not in listed})


def manuals_phantom(index_text, manual_files):
    """A manual the index calls WRITTEN that does not exist — the phantom-cite class,
    pointed at the documentation tree."""
    written = set(re.findall(r"\|\s*`([a-z_]+\.md)`\s*\|[^|]*\|\s*\*\*WRITTEN\*\*",
                             index_text or ""))
    return sorted(written - set(manual_files))


POINTER = re.compile(r"`((?:knowledge|scripts|rag)/[A-Za-z0-9_./-]+\.(?:md|py|sh|json|tsv))`")


def unresolved_pointers(text, exists):
    """Cited paths that do not resolve. `exists` is injected so a demonstration can supply a
    fake filesystem."""
    out = []
    for m in set(POINTER.findall(text or "")):
        if any(c in m for c in "<>*"):
            continue                            # a template, not a pointer
        if not exists(m):
            out.append(m)
    return sorted(out)


def count_drift(prose_text, actual, tol=DRIFT_TOL):
    """Count-bearing prose vs the counted tree. Exact-quoted harness pass lines get NO
    tolerance — they are what a reviewer is invited to reproduce."""
    drift = []
    for m in re.finditer(r"ALL (\d+) (?:COMPANION )?CHECKS PASSED", prose_text or ""):
        n = int(m.group(1))
        if n != actual:
            drift.append((f"exact-quoted pass line ({n})", actual, 0))
    for m in re.finditer(r"two suites \((\d+) \+ (\d+) = (\d+)", prose_text or ""):
        if abs(int(m.group(3)) - actual) > tol:
            drift.append((f"map total ({m.group(3)})", actual, tol))
    return drift


def undeclared_diets(files_and_heads):
    """Artifacts with no declared DIET-CLASS. A heuristic is a guess, and a role feeding
    itself the wrong diet by accident is what the declaration exists to prevent."""
    return sorted(name for name, head in files_and_heads if "DIET-CLASS:" not in (head or ""))


def handoff_unreachable(canon_text, exists):
    """The handoff sits outside the retrieval index by design, so the canon's pointer is its
    ONLY path. A canon that stops naming it makes the live state unreachable."""
    m = re.search(r"((?:knowledge/)?audit/[A-Za-z0-9_./-]*HANDOFF[A-Za-z0-9_.-]*\.md)",
                  canon_text or "", re.I)
    if not m:
        return "the canon names no SESSION_HANDOFF path"
    return "" if exists(m.group(1)) else f"the canon points at {m.group(1)}, which is absent"


def stale_packs(fingerprint_of_sources, pack_fingerprints):
    """Generated role packs that were cut from a different version of the sources.

    A generated VIEW that drifts from its source is a drift pair with a build step in
    front of it — which is why the packs exist only alongside this check. `pack_fingerprints`
    maps pack name -> the fingerprint it records (None if it records none)."""
    return sorted(name for name, fp in pack_fingerprints.items()
                  if fp != fingerprint_of_sources)


FLOOR_ITEMS = (
    ("the object",                                 ("object",)),
    ("the deliverable",                            ("deliverable",)),
    ("a success criterion",                        ("success",)),
    ("a falsifier",                                ("falsif", "abandon", "would end")),
    ("a CORE commitment with its kill condition",  ("kill condition",)),
    ("the first graded docket item",               ("docket",)),
)


def founding_unrecorded(formation_text, founding_exists):
    """A tree whose ONTOLOGY is written but which records no founding interview.

    The object slots are filled in one session with the human coordinator present, and that
    session leaves a governing record naming who said what (`manuals/founding_interview.md`).
    A filled ontology with no such record has lost the provenance of its own premises — the
    phantom-cite class, pointed at the foundations: the programme can no longer answer *who
    actually said this?* about the picture every worker is formed on."""
    sec = re.search(r"(?ms)^## 1\. .*?(?=^## )", formation_text or "")
    if not sec:
        return ""                       # no template shape to judge — say nothing
    if "[OBJECT-SLOT]" in sec.group(0):
        return ""                       # not founded yet; nothing is owed
    return "" if founding_exists else ("FORMATION_CORE §1 is filled but no founding record "
                                       "exists (audit/FOUNDING_INTERVIEW.md)")


def founding_floor_gaps(founding_text):
    """Floor items the founding record does not appear to name.

    ITS OWN LIMIT, STATED: this is a keyword reading, not a comprehension. It catches the
    record that never asked the question — overwhelmingly the falsifier and the kill
    condition, which are the two the room most wants to skip — and it cannot catch a record
    that names an item and answers it badly. That is why it WARNS rather than blocks: a gate
    that stops a bank on a word-match would teach programmes to write the words."""
    low = (founding_text or "").lower()
    return [label for label, keys in FLOOR_ITEMS if not any(k in low for k in keys)]


DISPATCH_COLS = 7


def dispatch_rows(log_text):
    """Parse the dispatch log into rows. Comments and short lines are ignored, because a
    half-written row is a logging defect and not a verdict claim."""
    out = []
    for line in (log_text or "").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        fld = [x.strip() for x in line.split("	")]
        if len(fld) >= DISPATCH_COLS:
            out.append(fld)
    return out


def verdicts_unlogged(logged_paths, verdict_files):
    """Persisted verdicts that NO dispatch row points at.

    ★ THIS IS THE ONE THAT CATCHES VERDICT-SHOPPING'S BLIND SPOT. The telemetry's
    refutation signal says so itself: it measures "persisted verdicts only — an unwelcome
    verdict never written to disk leaves no trace." Logging at DISPATCH time rather than at
    verdict time turns that around: the dispatch is recorded before its answer is known, so
    a verdict that appears with no dispatch behind it, or a dispatch that never produced one,
    both become visible. This half catches the first."""
    return sorted(set(verdict_files) - set(logged_paths))


def dispatch_phantom_verdicts(logged_paths, exists):
    """Dispatch rows naming a verdict file that does not exist — the phantom-cite class,
    pointed at the dispatch log. A row may legitimately carry no verdict yet (an open
    dispatch); it may not carry a path to a file nobody wrote."""
    return sorted(p for p in set(logged_paths)
                  if p and p.upper() not in ("", "-", "PENDING", "NONE") and not exists(p))


ROLE_FILE = re.compile(r"`([a-z_]+\.md)`")
ROLE_HINT = ("agent", "meta_observer", "coherence_keeper", "register_clerk",
             "decision_attention_reader", "external_review_loop")


def missing_roles(map_text, exists):
    """Every role the map tabulates has its durable file. A role reconstructed at each
    dispatch is a role that will drift."""
    return sorted({f for f in ROLE_FILE.findall(map_text or "")
                   if any(h in f for h in ROLE_HINT) and not exists(f)})


# ======================================================================
def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--main", type=int, default=None, help="printed MAIN suite total")
    ap.add_argument("--companion", type=int, default=None, help="printed COMPANION suite total")
    ap.add_argument("--self-test", action="store_true", help="run the planted-defect demos")
    a = ap.parse_args()
    if a.self_test:
        return self_test()

    ap_dir = apparatus_dir()
    if not ap_dir:
        print("[gate] no apparatus directory (looked for knowledge/prompts/ and prompts/)")
        return 1
    inst = is_instantiated()
    print(f"RECORD-INVARIANTS GATE · apparatus at {ap_dir}/ · "
          f"{'instantiated tree' if inst else 'apparatus repository (no object yet)'}")
    print("-" * 78)

    def exists(rel):
        return (ROOT / rel).exists()

    fc = _read(f"{ap_dir}/FORMATION_CORE.md") or ""

    # 1 — LEDGER ROSTER
    if inst:
        led = sorted(p.name for p in (ROOT / "knowledge" / "ledgers").glob("*.md"))
        un, mi = roster_unnamed(fc, led), roster_missing(fc, led)
        _ck("ledger roster: every ledger on disk is named in FORMATION_CORE §5",
            not un, f"unnamed: {', '.join(un)}")
        _ck("ledger roster: every ledger FORMATION_CORE §5 names exists",
            not mi, f"named but absent: {', '.join(mi)}")
    else:
        NOTES.append("ledger roster — no knowledge/ledgers/ yet; checked once instantiated")

    # 2 — MANUALS INDEX (the manuals INDEX asks for this pin in its own text)
    man_dir = ROOT / ap_dir / "manuals"
    if man_dir.is_dir():
        idx = _read(f"{ap_dir}/manuals/INDEX.md") or ""
        mans = sorted(p.name for p in man_dir.glob("*.md"))
        ul, ph = manuals_unlisted(idx, mans), manuals_phantom(idx, mans)
        _ck("manuals: every manual present is listed in INDEX.md",
            not ul, f"unlisted: {', '.join(ul)}")
        _ck("manuals: every manual INDEX.md marks WRITTEN exists",
            not ph, f"marked WRITTEN but absent: {', '.join(ph)}")

    # 3 — POINTER RESOLUTION
    for label, rel in (("the canon", "CLAUDE.md"),
                       ("FORMATION_CORE", f"{ap_dir}/FORMATION_CORE.md"),
                       ("the apparatus map", f"{ap_dir}/APPARATUS_MAP.md")):
        text = _read(rel)
        if text is None:
            if not (rel == "CLAUDE.md" and not inst):
                NOTES.append(f"pointers — {label} absent ({rel})")
            continue
        bad = unresolved_pointers(text, exists)
        _ck(f"pointers: every path cited in {label} resolves",
            not bad, f"unresolved: {', '.join(bad[:6])}")

    # 4 — THE HANDOFF'S ONLY PATH
    if inst:
        problem = handoff_unreachable(_read("CLAUDE.md") or "", exists)
        _ck("handoff: the canon's pointer is present and resolves", not problem, problem)

    # 5 — ROLE ROSTER
    gone = missing_roles(_read(f"{ap_dir}/APPARATUS_MAP.md") or "",
                         lambda f: exists(f"{ap_dir}/{f}"))
    _ck("roles: every role file the map tabulates exists",
        not gone, f"missing: {', '.join(gone)}")

    # 5b — GENERATED ROLE PACKS ARE CURRENT
    packs_dir = ROOT / ap_dir / "packs"
    if packs_dir.is_dir():
        import hashlib
        h = hashlib.sha1()
        for rel in (f"{ap_dir}/RULES_CORE.md", f"{ap_dir}/RULES_BY_ROLE.md"):
            h.update((_read(rel) or "").encode("utf-8"))
        want = h.hexdigest()[:12]
        got = {}
        for pk in sorted(packs_dir.glob("*.md")):
            m = re.search(r"fingerprint ([0-9a-f]{12})",
                          pk.read_text(encoding="utf-8", errors="replace")[:1200])
            got[pk.name] = m.group(1) if m else None
        st = stale_packs(want, got)
        _ck("packs: every generated role pack matches the current rule sources",
            not st, f"stale: {', '.join(st)} — regenerate: python scripts/gen_role_packs.py")

    # 6 — DIET MARKERS
    heads = []
    for p in sorted((ROOT / ap_dir).rglob("*.md")):
        try:
            heads.append((p.relative_to(ROOT).as_posix(),
                          p.read_text(encoding="utf-8", errors="replace")[:400]))
        except OSError:
            pass
    und = undeclared_diets(heads)
    _warn("diet: every apparatus document declares its DIET-CLASS", not und,
          f"{len(und)} inferred by heuristic, e.g. {', '.join(und[:3])}")

    # 7 — COUNT-BEARING PROSE
    if a.main is not None:
        total = a.main + (a.companion or 0)
        drift = count_drift("\n".join(filter(None, [_read("CLAUDE.md"), fc])), total)
        _ck("counts: count-bearing prose matches the counted tree",
            not drift, "; ".join(f"{w} vs tree {act} (tol {t})" for w, act, t in drift[:4]))

    # 8 — FOUNDING (the session that filled the slots left a record, and it met the floor)
    if inst:
        fr = None
        for cand in ("knowledge/audit/FOUNDING_INTERVIEW.md", "audit/FOUNDING_INTERVIEW.md"):
            if exists(cand):
                fr = cand
                break
        problem = founding_unrecorded(fc, fr is not None)
        _ck("founding: a filled ontology carries its founding record", not problem, problem)
        if fr:
            gaps = founding_floor_gaps(_read(fr) or "")
            _warn("founding: the record names every floor item", not gaps,
                  f"not named: {'; '.join(gaps)} — manuals/founding_interview.md §3")
        elif not problem:
            # No record AND nothing owed: the tree is simply not founded yet. Say so as a
            # note — never alongside the failure above, where a benign line reads as
            # reassurance standing next to a defect.
            NOTES.append("founding — not founded yet; /coordinator's next session is the "
                         "FOUNDING INTERVIEW (manuals/founding_interview.md)")
    else:
        NOTES.append("founding — the apparatus repository has no object to found; checked "
                     "once instantiated")

    # 9 — THE DISPATCH LOG (W10): verdicts and dispatches account for each other
    if inst:
        dl = _read("knowledge/ledgers/DISPATCH_LOG.tsv")
        if dl is None:
            NOTES.append("dispatch log — knowledge/ledgers/DISPATCH_LOG.tsv absent; RUL-065 "
                         "is UNMEASURED in this tree (manuals/dispatching.md §0-ter)")
        else:
            rows = dispatch_rows(dl)
            logged = [r[6] for r in rows]
            vfiles = []
            for d in ("knowledge/candidates", "knowledge/audit"):
                base = ROOT / d
                if base.is_dir():
                    vfiles += [p.relative_to(ROOT).as_posix()
                               for p in base.rglob("VERDICT*.md")]
            un = verdicts_unlogged(logged, vfiles)
            ph = dispatch_phantom_verdicts(logged, exists)
            _ck("dispatch: every persisted verdict has a dispatch row",
                not un, f"unlogged: {', '.join(un[:5])}")
            _ck("dispatch: every verdict a row names exists",
                not ph, f"named but absent: {', '.join(ph[:5])}")

    # 10 — OBJECT-SLOT ACCOUNTING (informational; a slot is a docket item, not a defect)
    slots = sum((_read(f"{ap_dir}/{p.name}") or "").count("[OBJECT-SLOT]")
                for p in (ROOT / ap_dir).glob("*.md"))
    if slots:
        NOTES.append(f"object slots still unfilled: {slots} — each is a docket item, "
                     f"not a defect")

    print("-" * 78)
    for n in NOTES:
        print(f"  [note] {n}")
    if WARNS:
        print(f"  {len(WARNS)} warning(s) — reported, never blocking.")
    if FAILS:
        print(f"\n>>> RECORD-INVARIANTS FAILED ({len(FAILS)}) — the prose has drifted from the "
              f"tree.\n>>> Fix the documents at the sites named above, then re-run.")
        return 1
    print("  RECORDS HOLD.")
    return 0


# ======================================================================
def self_test():
    """PLANTED-DEFECT DEMONSTRATIONS — each check shown firing on a defect and staying quiet
    on the repaired control, over text held in memory. The tree is never mutated."""
    cases = []

    def demo(name, got, want):
        ok = bool(got) == want
        cases.append(ok)
        print(f"  [{'OK ' if ok else 'FAIL'}] {name} "
              f"({'fired' if got else 'did not fire'}; expected {'fire' if want else 'no fire'})")

    roster = "`NEGATIVES_LEDGER.md` · `WINS_LEDGER.md` · `worklist.md`"
    disk = ["NEGATIVES_LEDGER.md", "WINS_LEDGER.md", "worklist.md", "PATHS_LEDGER.md"]
    demo("ledger roster: a ledger on disk the roster does not name",
         roster_unnamed(roster, disk), True)
    demo("ledger roster: CONTROL — the same disk once the roster names it",
         roster_unnamed(roster + " · `PATHS_LEDGER.md`", disk), False)
    demo("ledger roster: CONTROL — a GENERATED ledger absent from disk is not drift",
         roster_missing(roster + " · `NEGATIVES_INDEX.md`", disk), False)
    demo("ledger roster: a roster naming a ledger that does not exist",
         roster_missing(roster + " · `GHOST_LEDGER.md`", disk), True)

    idx = "| `banking.md` | bank anything | **WRITTEN** |"
    demo("manuals: a manual present but unlisted in the index",
         manuals_unlisted(idx, ["banking.md", "paths.md"]), True)
    demo("manuals: a manual marked WRITTEN that does not exist",
         manuals_phantom(idx, []), True)
    demo("manuals: CONTROL — index and directory agreeing",
         manuals_unlisted(idx, ["banking.md"]) + manuals_phantom(idx, ["banking.md"]), False)

    have = {"knowledge/ledgers/NEGATIVES_LEDGER.md"}
    demo("pointers: a cited path that does not resolve",
         unresolved_pointers("see `knowledge/ledgers/GONE.md`", lambda r: r in have), True)
    demo("pointers: CONTROL — a cited path that resolves",
         unresolved_pointers("see `knowledge/ledgers/NEGATIVES_LEDGER.md`",
                             lambda r: r in have), False)
    demo("pointers: CONTROL — a template placeholder is not a pointer",
         unresolved_pointers("write `knowledge/audit/<round>/REPORT.md`", lambda r: False),
         False)

    demo("counts: an exact-quoted pass line disagreeing with the tree",
         count_drift("prints ALL 412 CHECKS PASSED across", 415), True)
    demo("counts: CONTROL — the same line once it agrees",
         count_drift("prints ALL 415 CHECKS PASSED across", 415), False)
    demo("counts: a map total beyond tolerance",
         count_drift("the two suites (400 + 87 = 487) cover it", 600), True)
    demo("counts: CONTROL — a map total inside tolerance",
         count_drift("the two suites (400 + 87 = 487) cover it", 488), False)

    demo("diet: an artifact with no declared class",
         undeclared_diets([("a.md", "# heading")]), True)
    demo("diet: CONTROL — the same artifact once it declares one",
         undeclared_diets([("a.md", "<!-- DIET-CLASS: ROLE -->\n# heading")]), False)

    demo("handoff: a canon naming no handoff at all",
         handoff_unreachable("## §9 read the live state", lambda r: True), True)
    demo("handoff: a canon whose handoff pointer does not resolve",
         handoff_unreachable("read knowledge/audit/SESSION_HANDOFF.md first",
                             lambda r: False), True)
    demo("handoff: CONTROL — pointer present and resolving",
         handoff_unreachable("read knowledge/audit/SESSION_HANDOFF.md first",
                             lambda r: True), False)

    demo("packs: a generated pack cut from an older version of the sources",
         stale_packs("abc123abc123", {"reviewer.md": "abc123abc123",
                                      "keeper.md": "0000deadbeef"}), True)
    demo("packs: a pack carrying no fingerprint at all",
         stale_packs("abc123abc123", {"reviewer.md": None}), True)
    demo("packs: CONTROL — every pack cut from the current sources",
         stale_packs("abc123abc123", {"reviewer.md": "abc123abc123",
                                      "keeper.md": "abc123abc123"}), False)

    demo("roles: a role the map tabulates whose file is gone",
         missing_roles("| Reviewer | `reviewer_agent.md` |", lambda f: False), True)
    demo("roles: CONTROL — the same row once the file exists",
         missing_roles("| Reviewer | `reviewer_agent.md` |", lambda f: True), False)

    FILLED = "\n".join(["## 1. THE ONTOLOGY",
                        "The field is the sole substrate; the layers never collapse.",
                        "", "## 2. THE DISCIPLINE", ""])
    TEMPLATE = "\n".join(["## 1. THE ONTOLOGY",
                          "> **`[OBJECT-SLOT]`.** The dense statement of the object itself.",
                          "", "## 2. THE DISCIPLINE", ""])
    demo("founding: an ontology written with no founding record behind it",
         founding_unrecorded(FILLED, False), True)
    demo("founding: CONTROL — the same ontology once the record exists",
         founding_unrecorded(FILLED, True), False)
    demo("founding: CONTROL — an UNFILLED template owes no record",
         founding_unrecorded(TEMPLATE, False), False)
    demo("founding: CONTROL — a document with no §1 at all is not judged",
         founding_unrecorded("## 4. TRAPS AND CONVENTIONS\nnothing here\n", False), False)

    RECORD = ("the object: the tempo field. the deliverable: a paper. success: a kernel "
              "family compatible with the data. falsifier: any measured drift. CORE, with "
              "its kill condition: the invariance fails. first docket item, grade B.")
    demo("founding: a record that never asked for a falsifier or a kill condition",
         founding_floor_gaps("object, deliverable, success, docket — and nothing else"), True)
    demo("founding: CONTROL — a record naming every floor item",
         founding_floor_gaps(RECORD), False)

    VF = ["knowledge/candidates/R001/VERDICT_META_r001.md",
          "knowledge/candidates/R001/VERDICT_REV_r001.md"]
    demo("dispatch: a persisted verdict that no dispatch row accounts for",
         verdicts_unlogged([VF[0]], VF), True)
    demo("dispatch: CONTROL — every verdict has its row",
         verdicts_unlogged(VF, VF), False)
    demo("dispatch: a row naming a verdict file nobody wrote",
         dispatch_phantom_verdicts(VF, lambda p: False), True)
    demo("dispatch: CONTROL — the same rows once the files exist",
         dispatch_phantom_verdicts(VF, lambda p: True), False)
    demo("dispatch: CONTROL — an OPEN dispatch (no verdict yet) is not a phantom",
         dispatch_phantom_verdicts(["PENDING", "-", ""], lambda p: False), False)
    TAB, NL = chr(9), chr(10)
    TSV = NL.join([
        "# utc" + TAB + "role" + TAB + "checker_model" + TAB + "author_model"
        + TAB + "claim" + TAB + "verdict" + TAB + "path",
        TAB.join(["t", "reviewer", "opus", "fable", "R-1", "CLEAR", "v1.md"]),
        "a malformed row carrying no tabs at all",
    ]) + NL
    demo("dispatch: CONTROL — a malformed row is skipped, not read as a verdict claim",
         len(dispatch_rows(TSV)) != 1, False)

    bad = cases.count(False)
    print("-" * 70)
    if bad:
        print(f"  SELF-TEST: {bad} of {len(cases)} demonstrations did NOT behave as specified "
              f"— a check that cannot be shown to fire verifies nothing.")
        return 1
    print(f"  SELF-TEST: {len(cases)}/{len(cases)} demonstrations behaved as specified.")
    return 0


if __name__ == "__main__":
    try:
        _rc = main()
    except BrokenPipeError:      # the reader went away; that is not our error
        _rc = 0
    sys.exit(_closed_pipe_exit(_rc))
