#!/usr/bin/env python
"""RECORD-INVARIANTS gate (standing policy, coordinator-directed 2026-08-13).

THE POLICY: load-bearing prose about the tree's state — counts, file structure,
what-runs-what, pointer paths — must be either generated from the tree or PINNED
here as an executable invariant. The suite verifies the mathematics; this gate
verifies the sentences that describe what was executed. Motivating record: the
2026-08-13 keeper round found the engine split's code conserved exactly on three
independent axes while its prose drifted at 26 sites in one commit; earlier
instances of the same class: the phantom-cite discipline (canon §2), the dead
render-guard greps (I-23 round), the five-answer check-count divergence.

RUN: standalone (structural + census invariants; count-total checks are skipped
without arguments) or from bank.sh as gate [2/4]:
    python scripts/check_records.py --main 412 --companion 81
Exit 0 = all invariants hold; exit 1 = the records have drifted from the tree —
fix the documents (or, if a count legitimately moved, update the count-bearing
sites) before banking.

TOLERANCE: count-bearing sites may lag the tree by at most DRIFT_TOL between
consolidations (counts are refreshed by counting at consolidation, not at every
bank); beyond that the gate FAILS. Exact-quoted harness totals must be exact.

EXTENDING (the policy's teeth): when a review catches a NEW prose-drift class,
the fix INCLUDES adding its invariant here where mechanizable. A drift class
caught twice in prose is a process failure. Keep every entry keyed to a measured
failure, never speculative; keep this file small enough to read.
"""
import argparse
import ast
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRIFT_TOL = 2  # tightened 5 -> 2 at the 2026-08-21 apparatus audit (U-1): max observed lag over
               # 26 banks and every count-bearing site was 2; the old width let the canon sit
               # wrong for four consecutive banks while the exact-match region self-corrected.

FAILS = []


def _ck(name, cond):
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}")
    if not cond:
        FAILS.append(name)


def _read(rel):
    p = ROOT / rel
    return p.read_text(encoding="utf-8") if p.exists() else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--main", type=int, default=None,
                    help="main-harness printed total (from bank.sh)")
    ap.add_argument("--companion", type=int, default=None,
                    help="companion-harness printed total (from bank.sh)")
    args = ap.parse_args()

    print("=" * 70)
    print("  RECORD-INVARIANTS gate (prose vs tree; policy 2026-08-13)")
    print("=" * 70)

    # ---- 1. STRUCTURE: the files the records name must exist -------------
    print("structure:")
    for rel in [
        "knowledge/corpus/twt.py", "knowledge/corpus/twt_companion.py",
        "knowledge/corpus/twt_test.py", "knowledge/corpus/twt_companion_test.py",
        "CLAUDE.md", "knowledge/audit/SESSION_HANDOFF_2026-07-27.md",
        "knowledge/ledgers/TWT_worklist.md",
        "knowledge/ledgers/TWT_NEGATIVES_LEDGER.md",
        "knowledge/prompts/FORMATION_CORE.md",
        "knowledge/candidates/probes_2026-08-02/ADJUDICATION3_2026-08-12.md",
        "knowledge/audit/engine_split_classification_2026-08-12.md",
        # methodology registers (proposals 1+3 implemented 2026-08-13):
        "knowledge/ledgers/TWT_RULING_REGISTER.md",
        "knowledge/ledgers/TWT_CHECKER_CALIBRATION.md",
        # standing ledgers instituted during the 2026-08 arc (archivist pass 2026-08-18,
        # brief item E-4): these carry live pointers from the canon, the role files and
        # FORMATION_CORE, and had no existence invariant.
        "knowledge/ledgers/TWT_COMPARATIVE_LEDGER.md",
        "knowledge/ledgers/TWT_EDIT_REACTION_LEDGER.md",
        "knowledge/ledgers/TWT_FAMILY_TREE.md",
    ]:
        _ck(f"exists: {rel}", (ROOT / rel).exists())

    # ---- 2. SPLIT INVARIANT: MAIN never imports COMPANION ----------------
    print("split invariant:")
    twt_src = _read("knowledge/corpus/twt.py") or ""
    _ck("twt.py (MAIN) contains no 'import twt_companion' statement",
        not any(ln.strip().startswith(("import twt_companion",
                                       "from twt_companion"))
                for ln in twt_src.splitlines()))

    # ---- 3. GATE LIVENESS: bank.sh greps match what the harnesses print --
    print("gate liveness (a guard that greps nothing verifies nothing):")
    bank = _read("scripts/bank.sh") or ""
    tmain = _read("knowledge/corpus/twt_test.py") or ""
    tcomp = _read("knowledge/corpus/twt_companion_test.py") or ""
    _ck("bank.sh gates on the MAIN pass-line pattern",
        "ALL [0-9]+ CHECKS PASSED across" in bank)
    _ck("bank.sh gates on the COMPANION pass-line pattern",
        "ALL [0-9]+ COMPANION CHECKS PASSED across" in bank)
    _ck("twt_test.py prints a matching pass line",
        "CHECKS PASSED across" in tmain)
    _ck("twt_companion_test.py prints a matching pass line",
        "COMPANION CHECKS PASSED across" in tcomp)

    # ---- 4. MIRROR SCOPE (RATIFIED, coordinator 2026-08-13): both engines
    print("mirror scope (ratified: both engines ship):")
    render = _read("scripts/render_pdf.sh") or ""
    for f in ("twt.py", "twt_companion.py", "twt_test.py",
              "twt_companion_test.py",
              # human ruling 2026-08-21: the paper's family-tree pointer must
              # resolve for an external reader, so the tree ships with the mirror.
              "TWT_FAMILY_TREE.md"):
        _ck(f"render_pdf.sh mirror copy list includes {f}", f in render)

    # ---- 5. TOOLING COHERENCE: rag 'code' shorthand covers both engines --
    print("tooling:")
    ragq = _read("rag/query.py") or ""
    _ck("rag/query.py 'code' source shorthand covers the companion engine",
        "twt_companion" in ragq)

    # ---- 6. CENSUS: doc-quoted def counts vs the tree (AST truth) --------
    print("census (AST truth vs count-bearing sites; tol ±%d):" % DRIFT_TOL)

    def _counts(rel):
        tree = ast.parse(_read(rel))
        fns = [n.name for n in tree.body if isinstance(n, ast.FunctionDef)]
        pub = [n for n in fns if not n.startswith("_")]
        return len(pub)

    pub_main = _counts("knowledge/corpus/twt.py")
    pub_comp = _counts("knowledge/corpus/twt_companion.py")

    # SITE REGISTRY — count-bearing prose. Adding a count to a document means
    # adding a row here (or generating the sentence from the tree instead).
    census_sites = [
        ("CLAUDE.md", r"MAIN engine\*\* \(~(\d+) public primitives",
         pub_main, "canon §6 main census"),
        ("CLAUDE.md", r"COMPANION engine\*\* \(~(\d+) public primitives",
         pub_comp, "canon §6 companion census"),
        ("CLAUDE.md", r"the MAIN engine \(~(\d+) public primitives",
         pub_main, "canon Pointers main census"),
        ("knowledge/reviewer_package/COVER_NOTE.md",
         r"engine: (\d+) public primitives \((\d+) main \+ (\d+) companion\)",
         (pub_main + pub_comp, pub_main, pub_comp), "COVER_NOTE census"),
    ]
    for rel, pat, truth, label in census_sites:
        text = _read(rel)
        m = re.search(pat, text) if text else None
        if not m:
            _ck(f"{label}: pattern found in {rel}", False)
            continue
        got = tuple(int(g) for g in m.groups())
        want = truth if isinstance(truth, tuple) else (truth,)
        ok = len(got) == len(want) and all(
            abs(g - w) <= DRIFT_TOL for g, w in zip(got, want))
        _ck(f"{label}: {got} vs tree {want} (tol ±{DRIFT_TOL})", ok)

    # ---- 7. TOTALS: doc-quoted check counts vs the live harness totals ---
    if args.main is None or args.companion is None:
        print("totals: SKIPPED (no --main/--companion; bank.sh supplies them)")
    else:
        print("totals (live harness prints vs count-bearing sites):")
        m_, c_, t_ = args.main, args.companion, args.main + args.companion
        total_sites = [
            ("CLAUDE.md",
             r"ALL CHECKS PASSED\" \((\d+) as of", (m_,), "canon §6 main total"),
            ("knowledge/reviewer_package/COVER_NOTE.md",
             r"(\d+) checks \((\d+) main \+ (\d+) companion\)",
             (t_, m_, c_), "COVER_NOTE totals"),
            ("knowledge/ledgers/TWT_worklist.md",
             r"\*\*(\d+) MAIN \+ (\d+) COMPANION = (\d+) as of",
             (m_, c_, t_), "worklist header totals"),
            ("knowledge/audit/SESSION_HANDOFF_2026-07-27.md",
             r"\*\*(\d+) MAIN \+ (\d+) COMPANION = (\d+), both green\*\*",
             (m_, c_, t_), "handoff table totals"),
            ("knowledge/prompts/FORMATION_CORE.md",
             r"two suites \((\d+) \+ (\d+) = (\d+)",
             (m_, c_, t_), "FORMATION_CORE map totals"),
        ]
        for rel, pat, want, label in total_sites:
            text = _read(rel)
            m = re.search(pat, text) if text else None
            if not m:
                _ck(f"{label}: pattern found in {rel}", False)
                continue
            got = tuple(int(g) for g in m.groups())
            ok = len(got) == len(want) and all(
                abs(g - w) <= DRIFT_TOL for g, w in zip(got, want))
            _ck(f"{label}: {got} vs live {want} (tol ±{DRIFT_TOL})", ok)

    # ---- 7b. VERBATIM REVIEWER-FACING PASS LINES ------------------------
    # NEW DRIFT CLASS (external-review loop, iteration 1, 2026-08-13). Distinct
    # from section 7: these sites do not *describe* a total, they QUOTE the
    # harness output and instruct a cold reviewer to compare it against what
    # their own terminal prints. DRIFT_TOL therefore does NOT apply — a lagging
    # quote here is not a stale count, it is a costly signal that fails in the
    # reviewer's hands at the exact moment it is meant to land. Measured
    # failure: COVER_NOTE §0 said "ALL 81 COMPANION CHECKS PASSED" against a
    # tree printing 87, and the public mirror README said 464 against 414 —
    # both on the release path, both invisible to every prior gate (the render
    # script's mirror-README guard only WARNS, and it greps the main pattern
    # only). The mirror is what a reviewer actually clones, so it is checked
    # here too; it lives outside ROOT and is skipped when absent.
    if args.main is None or args.companion is None:
        print("verbatim pass lines: SKIPPED (no --main/--companion)")
    else:
        print("verbatim pass lines (exact — quoted for a reviewer to compare):")
        quote_sites = [
            (ROOT / "knowledge/reviewer_package/COVER_NOTE.md",
             "COVER_NOTE §0"),
            (Path(os.environ.get("TWT_MIRROR_DIR",
                                 Path.home() / "Claude/Projects/twt-engine"))
             / "README.md", "mirror README"),
        ]
        for path, label in quote_sites:
            if not path.exists():
                print(f"  [SKIP] {label}: not present at {path}")
                continue
            text = path.read_text(encoding="utf-8")
            for pat, want, kind in [
                (r"ALL (\d+) CHECKS PASSED across (\d+) modules",
                 args.main, "main"),
                (r"ALL (\d+) COMPANION CHECKS PASSED across (\d+) modules",
                 args.companion, "companion"),
            ]:
                m = re.search(pat, text)
                if not m:
                    _ck(f"{label}: quotes the {kind} pass line", False)
                    continue
                _ck(f"{label}: {kind} pass line quotes {m.group(1)}, "
                    f"harness prints {want} (must be EXACT)",
                    int(m.group(1)) == want)

    # ---- 7c. THE COLD-REVIEW PROMPT: routine text == what the sampler sends
    # PREVENTIVE, not reactive (the only entry here that is). The external-review
    # loop's own fence is "the reviewer prompt stays verbatim and minimal: any
    # coaching in the prompt invalidates the measurement" — so the prompt is the
    # single highest-stakes string in the loop, it lives in two files that must
    # agree, and a drift between them voids every sample SILENTLY: the routine
    # would document one instrument while the sampler shipped another, and the
    # logged request body would look perfectly well-formed. Six lines to pin.
    routine = _read("knowledge/prompts/external_review_loop.md")
    sampler = _read("knowledge/audit/external_review_2026-08-13/send_cold_review.py")
    if routine and sampler:
        print("cold-review prompt (routine text == sampler payload):")
        m = re.search(r'PROMPT = "([^"]+)"', sampler)
        _ck("sampler defines a PROMPT string", bool(m))
        if m:
            _ck(f"routine quotes the sampler's prompt verbatim: {m.group(1)!r}",
                m.group(1) in routine)

    # ---- 8. POINTER RESOLUTION: paths the canon/records rely on ----------
    print("pointers:")
    for src, rel in [
        ("canon bootstrap step 2", "knowledge/audit/SESSION_HANDOFF_2026-07-27.md"),
        ("FORMATION_CORE §5 record", "knowledge/candidates/probes_2026-08-02/ADJUDICATION_2026-08-03.md"),
        ("FORMATION_CORE §5 record", "knowledge/candidates/probes_2026-08-02/ADJUDICATION2_2026-08-03.md"),
        ("FORMATION_CORE §5 record", "knowledge/candidates/probes_2026-08-02/ADJUDICATION3_2026-08-12.md"),
        # (probe-dir INDEX rows replaced 2026-08-21 by the GENERATED form below — the
        # archivist observed the hard-coded family was itself the enumeration-drift class:
        # a new probes_* dir silently escaped the invariant until someone added a row.)
        ("canon Pointers (ruling register)", "knowledge/ledgers/TWT_RULING_REGISTER.md"),
        ("canon Pointers (checker calibration)", "knowledge/ledgers/TWT_CHECKER_CALIBRATION.md"),
        # archivist pass 2026-08-18 (brief E-4): the arc's other standing ledgers are
        # pointed at from live prose but were never pointer-checked.
        ("canon §2 (RUL-048 commitment budget)", "knowledge/ledgers/TWT_FAMILY_TREE.md"),
        ("coordinator role file", "knowledge/ledgers/TWT_EDIT_REACTION_LEDGER.md"),
        ("philosopher role file", "knowledge/ledgers/TWT_COMPARATIVE_LEDGER.md"),
    ]:
        _ck(f"{src} -> {rel}", (ROOT / rel).exists())
    # GENERATED probe-dir INDEX invariant (2026-08-21): every probes_*/ directory carries
    # an INDEX.md — the archivist role's power (7), now enumerated from the tree itself.
    probe_dirs = sorted(p for p in (ROOT / "knowledge/candidates").glob("probes_*") if p.is_dir())
    missing_idx = [p.name for p in probe_dirs if not (p / "INDEX.md").exists()]
    _ck(f"every probes_* dir carries an INDEX.md ({len(probe_dirs)} dirs; missing: "
        f"{missing_idx or 'none'})", not missing_idx)
    # the citing prose must actually NAME the path it is credited with (pointer liveness,
    # same failure shape as the canon Pointers block below: a pointer nobody writes down
    # is not a pointer):
    for citer, path in [
        ("CLAUDE.md", "knowledge/ledgers/TWT_FAMILY_TREE.md"),
        ("knowledge/prompts/coordinator_agent.md",
         "knowledge/ledgers/TWT_EDIT_REACTION_LEDGER.md"),
        ("knowledge/prompts/philosopher_ledger_agent.md",
         "knowledge/ledgers/TWT_COMPARATIVE_LEDGER.md"),
    ]:
        src_text = _read(citer) or ""
        _ck(f"{citer} names {path}", path in src_text)
    # the canon POINTERS BLOCK must actually NAME the two registers (pointer liveness,
    # scoped to the fenced block per keeper S-1 — a whole-file grep goes vacuous the
    # moment other canon sections also mention the registers):
    canon = _read("CLAUDE.md") or ""
    mp = re.search(r"## Pointers\s*```(.*?)```", canon, re.S)
    pointers_block = mp.group(1) if mp else ""
    _ck("CLAUDE.md Pointers fenced block found", bool(pointers_block))
    for reg in ("TWT_RULING_REGISTER.md", "TWT_CHECKER_CALIBRATION.md"):
        _ck(f"CLAUDE.md Pointers block names {reg}", reg in pointers_block)

    # ---- 9. REGISTER CENSUS (keeper S-2, under the RUL-024 policy): row counts in the
    # ruling register vs the count-bearing prose sites ------------------------------
    print("register census:")
    reg_text = _read("knowledge/ledgers/TWT_RULING_REGISTER.md") or ""
    n_rul = len(re.findall(r"^\| RUL-\d", reg_text, re.M))   # \d excludes the header's RUL-ID
    n_adj = len(re.findall(r"^\| ADJ-F", reg_text, re.M))
    _ck(f"ruling register parses: {n_rul} RUL rows, {n_adj} ADJ-F rows",
        n_rul > 0 and n_adj > 0)
    for rel, label in [
        ("knowledge/ledgers/TWT_worklist.md", "worklist register counts"),
        ("knowledge/audit/SESSION_HANDOFF_2026-07-27.md", "handoff register counts"),
    ]:
        text = _read(rel) or ""
        mm = re.search(r"(\d+) ruling rows \+ (\d+) adjudication\s+fences", text)
        if not mm:
            _ck(f"{label}: pattern found in {rel}", False)
            continue
        got = (int(mm.group(1)), int(mm.group(2)))
        ok = abs(got[0] - n_rul) <= DRIFT_TOL and abs(got[1] - n_adj) <= DRIFT_TOL
        _ck(f"{label}: {got} vs tree ({n_rul}, {n_adj}) (tol ±{DRIFT_TOL})", ok)

    # ---- 10. RECORD-ID UNIQUENESS ---------------------------------------
    # NEW DRIFT CLASS (archivist pass 2026-08-18, promoted under RUL-024 / canon §2's
    # extension duty). The class was caught TWICE in prose, which the policy calls a
    # process failure, and both misses were invisible to every prior gate:
    #   (i)  Import-Registry ID `I-23` named TWO different rows — Collins et al. 2004
    #        (companion §13.1) and the mass→weight chain (§13.2) — while a dozen sites
    #        cited "I-23" by number, so every one of those citations was ambiguous. The
    #        registry's entire excision discipline (13.4: Used-at = blast radius, revert
    #        clause) is keyed to the ID, so a duplicated ID is not cosmetic: it makes the
    #        blast radius uncomputable. Fixed by renumbering Collins to I-28.
    #   (ii) companion Section 3 View A carried TWO byte-identical `B_minus_L_anomaly`
    #        rows, so the table's own row count disagreed with its primitive count.
    # An ID that names two rows names neither. Checked on every ID-bearing record.
    print("record-id uniqueness (an ID that names two rows names neither):")
    comp = _read("knowledge/corpus/TWT_foundational_paper_companion.md") or ""

    def _dups(seq):
        seen, dup = set(), []
        for x in seq:
            if x in seen and x not in dup:
                dup.append(x)
            seen.add(x)
        return dup

    imp_ids = re.findall(r"^\| (I-\d+) \|", comp, re.M)
    d = _dups(imp_ids)
    _ck(f"companion Section 13 import-registry IDs unique ({len(imp_ids)} rows; "
        f"duplicates: {d or 'none'})", not d and bool(imp_ids))

    i0 = comp.find("\n## View A ")
    i1 = comp.find("\n### View A.")
    if i0 == -1 or i1 == -1 or i1 <= i0:
        _ck("companion View A section located", False)
        va_rows = []
    else:
        va_rows = [ln.split("|")[1].strip() for ln in comp[i0:i1].splitlines()
                   if ln.startswith("| ") and not ln.startswith("|---")
                   and not ln.startswith("| Primitive")]
        d = _dups(va_rows)
        _ck(f"companion View A primitive rows unique ({len(va_rows)} rows; "
            f"duplicates: {d or 'none'})", not d and bool(va_rows))

    # NB the `[a-z]?` suffix form is real — RUL-014b exists; a regex without it silently
    # skips that row, which is the vacuous-guard class §3 exists to prevent.
    reg_ids = re.findall(r"^\| (RUL-\d+[a-z]?) \|", reg_text, re.M)
    d = _dups(reg_ids)
    _ck(f"ruling-register RUL IDs unique ({len(reg_ids)} rows; "
        f"duplicates: {d or 'none'})", not d and bool(reg_ids))

    # The family tree's branch-node IDs: unique AND contiguous from V3-1. The tree's node
    # COUNT is a quantity other records quote (and it legitimately runs ahead of a dated
    # stamping tally — V3-11 was added after the RUL-047 stamping, which is why the tally
    # is NOT compared against it here); what is mechanizable, and what protects the count
    # from becoming meaningless, is that the IDs themselves form a clean run.
    tree_text = _read("knowledge/ledgers/TWT_FAMILY_TREE.md") or ""
    v3 = [int(n) for n in re.findall(r"^\| V3-(\d+) \|", tree_text, re.M)]
    _ck(f"family-tree V3 node IDs unique and contiguous V3-1..V3-{len(v3)} "
        f"(found {sorted(v3)})",
        bool(v3) and sorted(v3) == list(range(1, len(v3) + 1)))

    # ---- 10b. COMPANION SECTION-3 COUNT-BEARING PROSE --------------------
    # Promotion candidate handed over by the Phase-0 leg (its report §C, M-7 item (i)):
    # View A's own row count had drifted by 7 before anyone counted, and NOTHING pinned
    # it. These three sentences describe the tree and are now generated-checkable.
    print("companion Section 3 self-description (tol ±%d):" % DRIFT_TOL)
    for pat, truth, label in [
        (r"The table below lists the\s*\n?(\d+) load-bearing-primitive rows",
         len(va_rows), "View A row count"),
        # the Δ list is backtick-delimited entries; count only the list lines (those that
        # BEGIN with a backtick), never the surrounding prose, which also uses backticks.
        (r"The following (\d+) entries \(counted",
         sum(len(re.findall(r"`([A-Za-z_][A-Za-z0-9_*]*)`", ln))
             for ln in comp[comp.find("\n### View A."):
                            comp.find("\n## View B")].splitlines()
             if ln.startswith("`") and (ln.endswith(",") or ln.endswith("`"))),
         "View A.Δ entry count"),
        (r"MAIN: \d+ module-level defs = (\d+) public", pub_main,
         "Section 3 MAIN public census"),
        (r"COMPANION: \d+ defs = (\d+) public", pub_comp,
         "Section 3 COMPANION public census"),
    ]:
        m = re.search(pat, comp)
        if not m:
            _ck(f"{label}: pattern found in the companion", False)
            continue
        got = int(m.group(1))
        _ck(f"{label}: {got} vs tree {truth} (tol ±{DRIFT_TOL})",
            abs(got - truth) <= DRIFT_TOL)

    # ---- 11. THE STANDING-LEDGER ROSTER ----------------------------------
    # FORMATION_CORE §5 enumerates the standing ledgers "so nothing is missed by a
    # too-narrow search (a measured failure, three times)" — TWT_EOM_MAP.md was missed
    # for a whole sweep round. That roster is only protective while it is COMPLETE, and
    # nothing checked it. Bidirectional: every ledger on disk must be named, and every
    # name must resolve.
    print("standing-ledger roster (FORMATION_CORE §5 list vs knowledge/ledgers/):")
    fc = _read("knowledge/prompts/FORMATION_CORE.md") or ""
    on_disk = sorted(p.name for p in (ROOT / "knowledge/ledgers").glob("*.md"))
    missing = [n for n in on_disk if n not in fc]
    _ck(f"every ledger in knowledge/ledgers/ is named in FORMATION_CORE "
        f"({len(on_disk)} files; unnamed: {missing or 'none'})", not missing)

    # ---- cached-worker prefix sync (RUL-079(vi)) -------------------------
    # Soft invariant: .claude/ is gitignored, so absence on a fresh clone is
    # legitimate; but IF the generated twt-worker agent exists, its embedded
    # FORMATION_CORE version must match the source header (a stale embedded
    # prefix silently forms every worker on an old contract).
    tw = ROOT / ".claude/agents/twt-worker.md"
    fc_head = (_read("knowledge/prompts/FORMATION_CORE.md") or "").splitlines()[0][:40]
    if tw.exists():
        print("cached-worker prefix sync (soft — skipped when the gitignored file is absent):")
        _ck(f"twt-worker embeds current FORMATION_CORE header ({fc_head!r}...)",
            fc_head in tw.read_text(encoding="utf-8"))

    # ---- rules-files ruling sync (R1 of the 2026-08-21 restriction analysis) --
    # RUL-068 enacted the general break clause and withdrew the per-rule [PROPOSED]
    # permission mechanism; RUL-066/072 adopted-then-merged the enforcer. The rules
    # files told agents the OPPOSITE for a day — the drift class caught twice
    # (engine split's 26 sites; F-A of the restriction analysis), hence this check.
    print("rules-files ruling sync (RUL-066/067/068 executed; no stale [PROPOSED] stamps):")
    for rel in ("knowledge/prompts/RULES_CORE.md", "knowledge/prompts/RULES_BY_ROLE.md"):
        txt = _read(rel) or ""
        stale = txt.count("*[PROPOSED]*")
        _ck(f"{rel}: no *[PROPOSED]* permission stamps survive (found {stale})", stale == 0)
    core_txt = _read("knowledge/prompts/RULES_CORE.md") or ""
    _ck("RULES_CORE.md states the RUL-068 general break clause",
        "GENERAL BREAK CLAUSE (RUL-068" in core_txt)

    # ---- 12. WITHDRAWN-GROUND SWEEP (RUL-082 / RV-7; reviewer recommendation) -
    # The canon's own named recurring failure is "a local relabel leaves a TRAIL of
    # stale labels across the corpus", and the C-32 promotion produced a live instance:
    # the withdrawn causal ground "weak = SD is neutrino-forced / the neutrino picks SD"
    # survived at four governing sites AFTER the paper, companion and family tree were
    # swept, and one of them was guarded by a passing suite check. Per the
    # record-invariants policy (a drift class caught twice in prose is a process
    # failure), the class is promoted to a check here.
    #
    # DESIGN, stated so the check can be judged:
    #  * scope = the LIVE governing files only. Dated audit records, archives, candidate
    #    probes and the canon-declared legacy standalones are HISTORY and must keep the
    #    state they were written in; firing on them would be the defect, not the catch.
    #  * a hit is EXEMPT when it sits in an explicitly-marked supersession context — the
    #    same line, the 40 preceding lines, or the 3 following lines carry one of the
    #    marker tokens. That is how the corpus legitimately QUOTES the withdrawn phrase
    #    (the engine's retained-history banner; the companion's R-079 note; the
    #    comparative ledger's audited row with its annotation directly beneath).
    #  * CLAUDE.md is reported but NON-FATAL. The lead may not edit the canon, so a hard
    #    failure there would block every bank on an edit only the coordinator can make.
    #    The exact diffs are written out for them; the WARN is the standing reminder and
    #    disappears when they are applied.
    #
    # WHAT IT DOES NOT GUARANTEE, stated so nobody over-trusts it: the marker window is a
    # HEURISTIC. A stale assertion that happens to sit within 40 lines of an unrelated
    # "no longer" or "RV-7" is exempted and will not be caught — that is a false NEGATIVE
    # the check accepts in exchange for never firing on the corpus's legitimate quotations
    # of the withdrawn phrase. Negative-tested 2026-08-21, three trials: a fresh unmarked
    # assertion in the harness FIRES; deleting the engine's supersession banner (the exact
    # pre-repair state) FIRES; an unmarked assertion planted in a dated audit record does
    # NOT fire (the inverse control — history must keep the state it was written in). The
    # second trial had to be rebuilt: hand-stripping marker tokens left "RV-6/RV-7" behind
    # and the check passed, which is itself the demonstration that the window is generous.
    print("withdrawn-ground sweep (RUL-082/RV-7: 'weak = SD is neutrino-forced' is retired):")
    WITHDRAWN = ("neutrino-forced", "neutrino picks sd", "neutrino-linked")
    MARKERS = ("superseded", "withdrawn", "rv-7", "is false", "historical assessment",
               "retained verbatim", "no longer")
    LIVE = ["knowledge/prompts/FORMATION_CORE.md", "knowledge/prompts/RULES_CORE.md",
            "knowledge/prompts/RULES_BY_ROLE.md", "knowledge/corpus/twt.py",
            "knowledge/corpus/twt_companion.py", "knowledge/corpus/twt_test.py",
            "knowledge/corpus/twt_companion_test.py",
            "knowledge/corpus/TWT_foundational_paper.md",
            "knowledge/corpus/TWT_foundational_paper_companion.md"]
    LIVE += sorted("knowledge/ledgers/" + q.name
                   for q in (ROOT / "knowledge/ledgers").glob("*.md"))

    def _unmarked_hits(rel):
        txt = _read(rel)
        if txt is None:
            return []
        lines = txt.splitlines()
        low = [ln.lower() for ln in lines]
        out = []
        for i, ln in enumerate(low):
            if not any(w in ln for w in WITHDRAWN):
                continue
            window = low[max(0, i - 40):i + 4]
            if any(m in w for w in window for m in MARKERS):
                continue
            out.append(f"{rel}:{i + 1}")
        return out

    bad = [h for rel in LIVE for h in _unmarked_hits(rel)]
    _ck("no LIVE governing file asserts the withdrawn ground unmarked "
        f"(hits: {bad or 'none'})", not bad)
    canon_hits = _unmarked_hits("CLAUDE.md")
    if canon_hits:
        print(f"  [WARN] CLAUDE.md still asserts the withdrawn ground at {canon_hits} \u2014 "
              f"NON-FATAL by design (canon edits are the coordinator's). Diffs: "
              f"knowledge/audit/consolidation_2026-08-21/CANON_DIFFS_WEAK_SD_2026-08-21.md")
    else:
        print("  [OK ] CLAUDE.md carries no unmarked withdrawn-ground assertion")

    # ---- verdict ---------------------------------------------------------
    print("-" * 70)
    if FAILS:
        print(f"  RECORD-INVARIANTS: {len(FAILS)} FAILURE(S) — the records have "
              f"drifted from the tree. Fix the documents before banking.")
        for f in FAILS:
            print(f"    - {f}")
        sys.exit(1)
    print("  RECORD-INVARIANTS: ALL HOLD (prose matches tree).")
    sys.exit(0)


if __name__ == "__main__":
    main()
