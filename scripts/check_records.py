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
import sys
from pathlib import Path

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

    # 8 — OBJECT-SLOT ACCOUNTING (informational; a slot is a docket item, not a defect)
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

    demo("roles: a role the map tabulates whose file is gone",
         missing_roles("| Reviewer | `reviewer_agent.md` |", lambda f: False), True)
    demo("roles: CONTROL — the same row once the file exists",
         missing_roles("| Reviewer | `reviewer_agent.md` |", lambda f: True), False)

    bad = cases.count(False)
    print("-" * 70)
    if bad:
        print(f"  SELF-TEST: {bad} of {len(cases)} demonstrations did NOT behave as specified "
              f"— a check that cannot be shown to fire verifies nothing.")
        return 1
    print(f"  SELF-TEST: {len(cases)}/{len(cases)} demonstrations behaved as specified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
