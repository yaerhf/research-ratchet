<!-- DIET-CLASS: VERDICT -->
# EXTERNAL REVIEW — research-ratchet @ `bf302af`

**To:** the coordinator, research-ratchet
**From:** a cold reader (Claude, web session — no repository write access, by the human
coordinator's deliberate choice)
**Reviewed state:** `bf302af295b44506c8434efd8c8f8d33746306e6`, committed 2026-08-27T19:55:14+03:00,
*"install: the clone is a source of files, not a source of context"*
**Date of review:** 2026-09-02
**Method:** the repository was **executed**, not only read.

---

## §0 · MY DIET — stated first, because it bounds everything below

Per rule 205, a checker declares what it was starved of and what it was saturated with, and
says so where the verdict lands.

**Saturated with:** the published tree at `bf302af` in full — every file in `prompts/`,
`scripts/`, `rag/`, plus `README.md`, `INSTALL.md`, `WHY.md`, `WORKLIST.md`, `HANDOFF.md`.
I read `WORKLIST.md` and `HANDOFF.md` **deliberately**, which `INSTALL.md` step 0 forbids the
*installing* agent. I am not installing; I am reviewing the programme, and its docket and live
state are part of what I am reviewing. Flagging it because the fence exists and I crossed it
knowingly.

**Starved of:** the founding programme (`yaerhf/TWT`) — I did not open it. Every incident
citation in the rules is therefore, to me, an **unverified provenance claim**. I have not
checked a single `RUL-NNN` against its register. I also have no access to any live
instantiation, no transcripts, and no contact with the author.

**Approximate cold-reader status:** partial. I see the released artifact and nothing else,
which is the external reviewer's diet — but I chose my own reading order rather than receiving
a sampler payload, so this is not an F1-clean cold read and must not be counted as one in the
external-loop N.

---

## §1 · VERDICT

| | |
|---|---|
| **On the engineering** | **HOLDS.** Four planted sabotages, four correct refusals. The install path runs clean end to end. The diet layer holds through retrieval, not just in the checker tool. |
| **On the design** | **HOLDS.** Structures I expected to be decoration turned out to be load-bearing on inspection. §3 lists the ones I checked and would not move. |
| **On self-application** | **OVER-CLAIM.** The apparatus applies its own strictest standards to `check_records.py` and to almost nothing else. The founding measurement — cross-class review — has **no mechanical support of any kind**, and by the apparatus's own sentence that makes it a convention rather than a control. |

The correct smaller claim, offered per the OVER-CLAIM verdict form: *the apparatus enforces its
record-invariants discipline mechanically, and enforces the rest on the operator.* That is true,
honest, and already stated in `WHY.md` — but §4/F1 below argues one specific rule does not
belong in the unenforced set, because it is the one the whole design rests on.

**Nothing here refutes a design decision.** Every finding is an absence, not an error.

---

## §2 · WHAT HOLDS — computed, and reported because a checker that only finds things is noise

Rule 86: be willing to return CLEAR. These were tested, not assumed.

**COMPUTED — the gate fires on planted defects.** Four sabotages against a freshly installed
tree, all four refused the bank:

| sabotage | result |
|---|---|
| canon's handoff pointer redirected to a non-existent file | `[FAIL] handoff: the canon's pointer is present and resolves` → refused |
| rule source edited, packs not regenerated | `[FAIL] packs: … stale: archivist.md, auditor.md, …` (all 12 named) → refused |
| harness prints `ALL 3 CHECKS PASSED`, exits non-zero | `>>> The MAIN harness did not run to completion` → refused |
| harness exits 0, prints no pass line | `>>> Self-checks FAILED (main engine)` → refused |

The third and fourth are the interesting pair: the gate is not fooled by a truthful-looking
pass line, and not fooled by a clean exit code. That is a real double-guard.

**COMPUTED — the records self-test is green.** `30/30 demonstrations behaved as specified`
(counted from a run, not quoted from a document). The state `WHY.md` describes as shipping red
is repaired.

**COMPUTED — the install path runs.** A fresh tree following `INSTALL.md` steps 0–6 reaches a
green first bank with no manual repair: ingest writes an index, a query returns hits, 12 packs
generate, the records gate prints `RECORDS HOLD`, and the commit lands.

**COMPUTED — the diet layer is fail-safe end to end.** I planted three leak candidates:

- a `DERIVATION` whose marker sits below `MARKER_SCAN_CHARS` → `FORBIDDEN (inferred)`
- an unmarked derivation *outside* any round directory → `FORBIDDEN — UNCLASSIFIED`
- an unmarked file at repo root → `FORBIDDEN — UNCLASSIFIED`

Then I checked the path that actually matters — retrieval, not the checker tool. Same query,
two roles: the saturated reviewer received the `DERIVATION` chunk at score 37.66; the starved
meta-observer got `WITHHELD this query: DERIVATION ×3 · FORMATION ×12` and never saw it. The
withheld classes are reported **by name and count only**, contents excluded. This is the
best-executed part of the repository.

**COMPUTED — `init_repo.sh` is careful.** The identity preflight and the write-`.gitignore`-
before-`git add` ordering both fire correctly; the abort path exits 1.

---

## §3 · FENCES I CHECKED AND WOULD NOT MOVE

Recorded so a future efficiency pass does not cut them. Each looked like a defect and turned out
to have a reason I could find in the tree.

| Looks removable | Why it stays |
|---|---|
| Verbose prose in `prompts/` | Audience is agents, and the per-rule incident **is** the evidence base. `RULES_CORE`'s own standard: a rule with no recorded incident *"reads as decree."* Compressing deletes the thing that makes the rule legitimate. |
| Blocks duplicated across role files | Already adjudicated — W1 FINDING 2 reclassified this from WASTE to load-bearing *at the point of use*. I agree; do not centralize behind a pointer. |
| `check_records_founding.py`, 1902 lines, never invoked | Deliberate worked example of what a mature gate becomes at ~98 corpus pins. Its docstring says so. Not dead code. |
| Telemetry that can never block a bank | Structural, via `\|\| true`, with the reason in the comment: a telemetry that can gate gets removed within a week and then measures nothing. Correct. |
| `knowledge/audit/` excluded from the index | A diet implemented at the file layer. `INSTALL.md` explicitly says *"Do not 'fix' it."* Confirmed working: ingest prints `NOT INDEXED (by design — pointer-only)`. |
| BM25 rather than embeddings | Dependency-free with a documented swap contract and a stated limit. Right default for a toolkit that must install anywhere. |
| Gates numbered `[0/4]`…`[4/4]` | Pinned because `check_records.py`'s header, canon §2 and RUL-024's register row all quote `bank.sh [2/4]`. Renumbering drifts three documents. |
| Generated packs committed to the tree | `.claude/` is gitignored and does not survive a clone; the packs are gate-checked against source. Committing them is the restore path. |
| The apparatus self-test running **before** the gate it certifies | Correct ordering, and the comment explains it: otherwise five checks could sit green and vacuous with no detector. |

---

## §4 · FINDINGS

Labelled per C-16: **COMPUTED** where a command demonstrates it, **ARGUED** where the case
rests on reasoning. Two findings are ARGUED and are marked as such; weight them accordingly.

---

### F1 — RUL-065 has no mechanical support anywhere in the tree
**COMPUTED · severity: highest · this is the whole report**

`WHY.md` opens with the finding that reorganised everything: a month of *"found nothing"*
caused by same-class review, and the rule that came out of it keys on **who authored the work**.
`calibration_probes.md` sharpens it: *"a fresh instance of class X auditing a corpus largely
written by class X is same-class review however new the instance is."* RUL-065 makes it binding
on every checking role.

Nothing in the tree records which class authored a claim, or which class checked it:

```
$ grep -rn "model.class\|MODEL_CLASS\|authored_by\|author_class" scripts/ rag/
(no matches)
```

`honesty_telemetry.py` reports five metrics. A same-class-CLEAR rate is not among them and
**cannot be**, because the input does not exist.

**What this costs.** A programme can drift into all-same-class checking — the exact founding
failure — for a month, and every gate stays green, the telemetry prints five healthy-looking
lines, and nothing warns. The failure signature is the one the apparatus says it cares about
most: the verdict looks identical.

**Why it is not merely "another unenforced rule."** `RULES_CORE` is honest that ~174 of 204
rules are unenforced, and I accept that framing for almost all of them. RUL-065 is different on
the apparatus's own terms, in three ways:

1. It is the **generative** measurement. Diets, cross-class dispatch, the calibration probes and
   the review architecture all descend from it. If it silently stops holding, the descendants
   keep running and stop meaning anything.
2. Its breach is **invisible by construction** — the defining property the apparatus elsewhere
   treats as requiring a structural fix (cf. fence F5, which exists precisely because its
   benefit leaves no trace).
3. The apparatus already wrote the verdict: *"a separation asserted and never verified is a
   convention, not a control."* That sentence is in rule 205's WHY column, about a bound that
   was **re-cut within a day** when measured to fail. Cross-class is currently in the state that
   bound was in before the re-cut.

**Would change if:** a dispatch log exists. See W10.

---

### F2 — 2 of 15 tools define a demonstrated failure mode, and one of the two is never run
**COMPUTED · severity: high**

Rule 35 is ABSOLUTE: *ship every new check with a demonstrated failure mode.* Counted:

- **15** executable tools in `scripts/` and `rag/`.
- **2** define planted-defect demonstrations: `check_records.py` and `check_records_founding.py`.
- `check_records_founding.py` is not run by `bank.sh` — so **1 running tool in 15**.

*(A note on method, because it nearly cost me a wrong number: `bank.sh` matched a naive
`grep -l -- "--self-test"`. It only **invokes** the records self-test and mentions it in an error
string; it defines none. C-24 — refresh by counting — caught it.)*

**The acute case is `rag/diet.py`.** It enforces rule 92, which is ABSOLUTE. It exists *because*
the first path-shaped bound was measured to leak on 2026-08-27. It is the mechanism behind the
one control in this repository I found genuinely excellent. And it has no demonstration that it
can fail. I verified its behaviour by hand-writing the leak tests myself — the logic is right
today, and nothing keeps it right through the next refactor of the `ROLES` table.

**Would change if:** `rag/diet.py --self-test` exists and `bank.sh [2/4]` runs it. **Written and
tested — see W11 and the attached patch.** It carries 27 demonstrations and a demonstrated
failure mode of its own.

---

### F3 — W6 is a standing duty where the incident argues for a gate
**COMPUTED (absence) / ARGUED (remedy) · severity: high**

`.github/` does not exist. There is no CI, no pre-commit hook, no scheduled run.

W6 covers this ground — *"re-run the installer after any change to the gates or INSTALL.md"* —
and its history shows it working: three runs on 2026-08-27, each finding real defects. But W6
is discharged by **remembering**, and the incident that created it was precisely a failure of
remembering: *"the toolkit had been shipping with its central gate broken, and nothing had run
it."*

This is the apparatus's own diagnosis pointed at itself. Everywhere else it treats
"someone will remember" as the weakest control class available. Here it is the only control on
the thing whose failure was most expensive.

**Would change if:** the dry-run is a script and CI runs it. **Written and tested — see W12 and
the attached `scripts/install_dryrun.sh`,** which reproduces the 2026-08-27 afternoon and exits
0 on `bf302af`.

---

### F4 — verdict-shopping is measurable only over verdicts someone chose to write
**COMPUTED · severity: medium · already named by the tree, not yet planned**

The telemetry says it itself:

> `[PROXY] persisted verdicts only — an unwelcome verdict never written to disk leaves no
> trace. Closing that needs dispatch-side logging.`

Named, unowned, on no docket item I could find. It is the same missing primitive as F1 — one
artifact closes both. Folded into W10.

---

### F5 — the retrieval index is a full rebuild inside the gate
**COMPUTED · severity: low, rising with corpus size**

`rag/index.json` measured **1.6 MB against a 1.2 MB corpus**, rebuilt from scratch at every bank
via `[3/4]`. No mtime or hash short-circuit (`grep -n "mtime\|incremental" rag/ingest.py` finds
only an exclusion comment).

Fine at present scale. At the founding programme's scale — 503+ engine primitives plus a paper —
this becomes a per-bank tax on the instrument agents are meant to reach for casually, and the
apparatus's own recorded retrieval failure is a documented command that quietly stopped being
used. Defer, but do not lose.

---

### F6 — the shipped tools traceback on `SIGPIPE` under `set -euo pipefail`
**COMPUTED, with a narrow reproduction · severity: low**

None of `rag/*.py` or `scripts/*.py` handles `BrokenPipeError`. Piping a documented command to
`head` **inside a script under `set -euo pipefail` with a non-tty stdout** produces a Python
traceback and a non-zero exit:

```
File "rag/query.py", line 257, in main
    print(f"  [{d['source']} §{d['name']}]  score {score:.2f}")
BrokenPipeError: [Errno 32] Broken pipe
```

**Stated precisely, because I initially overclaimed it:** it did **not** reproduce interactively
at `head -1`, `-2` or `-3`. It reproduced reliably inside my dry-run script. So it is not a
defect a human will hit at the terminal — it is a defect anyone **scripting** these tools will
hit, which includes W12's CI. Two lines at each entry point fix it, next to the existing UTF-8
reconfigure block that exists for the same class of reason.

---

## §5 · PROPOSED DOCKET ITEMS

Written in `WORKLIST.md` format so they can be pasted. Grades per `manuals/paths.md` §2.

---

### W10 · THE DISPATCH LOG — give RUL-065 something to measure
**Grade A · a computation remaining · closes F1 and F4**

**★ THE FENCE THAT MUST GOVERN THIS ITEM.** This is a *record*, not a *gate*. It must report and
never block, for the same structural reason `honesty_telemetry.py` never gates: a log that can
refuse a bank gets bypassed and then logs nothing. It also must not become a second place where
verdicts live — it carries a **pointer** to the verdict file that rule 56 already requires, not
a copy.

**The artifact.** `knowledge/ledgers/DISPATCH_LOG.tsv`, append-only, tab-separated:

```
# utc  role  checker_class  author_class  claim_id  verdict  verdict_path
2026-09-02T14:03:11Z	meta-observer	classB	classA	R-042	REFERENT-DRIFT	knowledge/candidates/R042/VERDICT_META_r042_2026-09-02.md
```

`UNKNOWN` is a legal value in either class column and is counted as same-class, per the existing
discipline that a cell is filled `UNKNOWN` rather than guessed (rule 50).

**Who writes a row.** The coordinator, in the same pass as the dispatch — the same-pass
discipline that already governs register rows and verdict files. This is a coordinator power
addition, not a new role: role-count governance says prefer an existing role.

**What it buys, in order of value:**

1. **Metric 6 in `honesty_telemetry.py` — cross-class integrity.** Reported at every bank, never
   gating. Attached and tested. On synthetic rows reproducing the founding failure it prints:

   ```
    6 CROSS-CLASS       5/7 checks were SAME-CLASS (71%) · 5 of those returned CLEAR
                        ⚠ 5 same-class CLEAR(s) carry NO INFORMATION (RUL-065) —
                        re-check cross-class or strike them from the evidence base:
                          R-01 · reviewer · classA checking classA
                          …
                        roles that have NEVER run cross-class: reviewer
   ```

   On a tree with no log it prints `RUL-065 is UNMEASURED in this tree`, which is the honest
   state and is itself the finding.

2. **Verdict-shopping measured against dispatches** rather than survivors, closing the proxy the
   telemetry already flags (F4).

3. **A new `check_records.py` invariant:** every `VERDICT_*` file resolves to a dispatch row, and
   every row claiming a verdict resolves to a file. That catches the unwritten verdict, which is
   currently invisible. Ship it with its planted-defect demonstration, per rule 35.

**What breaks if done badly.** If the log is written from memory at consolidation rather than
per-dispatch, it becomes a stale-sync note — the exact C-24 failure class. Per-dispatch or not
at all.

**Deliverable:** the ledger file with its two-line header; the coordinator power; metric 6; the
`check_records.py` invariant with its demonstration.

---

### W11 · A DEMONSTRATED FAILURE MODE FOR THE DIET LAYER
**Grade A · WRITTEN AND TESTED — attached, ready to apply · closes the acute half of F2**

`rag/diet.py --self-test`, in the same shape as `check_records.py`: pure functions over
`(path, text)`, plants defects, watches predicates fire, mutates no tree.

**Status: written, run against `bf302af`, 27/27 demonstrations behave as specified.** Coverage:

- rule 92 across all four checker roles, plus the philosopher's RUL-043 carve-out as a control
- the **2026-08-27 leak itself**, as a permanent regression pin — the meta-observer's bound
  returning `FORMATION_CORE.md` can never silently return
- the marker below `MARKER_SCAN_CHARS`
- three fail-safe cases: unmarked in a round directory, unmarked outside any known directory,
  unmarked at repo root
- each starvation that *is* an instrument, each with its matching control
- saturated roles verified **not** over-starved (a starvation added by accident is also a defect)
- role aliases, which are an easy place to open a hole

**And it has its own demonstrated failure mode.** I sabotaged `diet.py` by deleting the
meta-observer's `TRANSCRIPT` denial — a plausible tidy-up — and the self-test went red on
exactly that line and exited 1. A self-test never shown able to fail would be a phantom cite of
the self-test class, so this is included rather than assumed.

**Wire it into `bank.sh [2/4]`** beside the records self-test, with the same
count-agnostic pass-line match so the mode can grow.

**Deliverable:** the patch (attached), the `main()` wiring, the `bank.sh` block. Then extend the
pattern to `ingest.py` and `query.py`, which is a smaller job once the shape exists.

---

### W12 · W6 AS A GATE — CI runs the installer
**Grade A · the script is WRITTEN AND GREEN — attached · closes F3**

**The honest framing for the register:** this adds no rule. It moves one rule from the ~85%
unenforced set into the enforced set, which is the direction the WHY column is supposed to move.

**`scripts/install_dryrun.sh`** — attached, exits 0 on `bf302af`. Executes `INSTALL.md`
steps 0–6 against a throwaway tree, asserts retrieval returns hits on a fresh tree (the
*"available and unused"* defect), and banks once. Last line: `install dry-run PASSED — fresh
tree reaches a green first bank`.

**`.github/workflows/gates.yml`:**

```yaml
name: gates
on: [push, pull_request]
jobs:
  gates:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - name: apparatus self-test (the gate that certifies the gate)
        run: python scripts/check_records.py --self-test
      - name: diet self-test (W11)
        run: python rag/diet.py --self-test
      - name: records-invariants gate on this repository
        run: python scripts/check_records.py
      - name: install dry-run — INSTALL.md executed, not read
        run: bash scripts/install_dryrun.sh
```

Four steps, all four already verified to pass on `bf302af` (step 2 once W11 lands). Total
runtime under a minute.

**Note for whoever wires it:** apply F6's `BrokenPipeError` guard first, or the dry-run is
fragile under `pipefail`. I hit this twice writing the script.

**What this does not do, stated plainly.** It cannot check that anyone followed the method. It
checks that the *machinery* still runs, which is the narrow claim `WHY.md` already makes about
gates: they guard the door, not the wall. Do not let it be quoted as more.

---

## §6 · ONE PUSHBACK — W3 is graded low

**ARGUED, not computed. I cannot run this from outside; the grade is the point at issue.**

W3 (run P7, the profile-divergence test) is **Grade D — blocked on a live programme with real
dispatches**. I think it is closer to **Grade B**, and the difference matters.

`PROFILES.md` §6-bis(i) already records the adversarial finding: if one claim read under two
profiles returns the same verdict, that reads as two independent confirmations when it is one
measurement counted twice. `calibration_probes.md` P7 states its own status as *"SPECIFIED, NOT
RUN"* and concludes the axis *"must not be trusted until this runs."*

The blocker is stated as needing real dispatches. But P7's own protocol needs only a claim
**whose answer you already know**, and the file names the source: *"a repaired defect from this
file's own set works well."* Those exist now, in this repository, in `calibration_probes.md`
(P4 and P5 both went stale on repair — their arithmetic is recorded). A two-dispatch,
same-diet, same-class, profile-only-varied run is available today against this tree.

**Why it is worth reopening rather than waiting.** If the axis is decorative, every dispatch
currently using a `[PROFILE]` line is double-counting evidence, and that cost is being paid now,
not when a live programme appears. And by the file's own standard, the apparatus is asking every
checker to be calibrated blind before its verdicts count while exempting its own disposition
axis from that bar.

**Promotion condition, so this is a path rather than a complaint:** if a two-run P7 against a
known-answer defect from `calibration_probes.md` is judged to measure something real, W3
promotes to B and becomes schedulable without a live programme. If the coordinator judges that
a self-test against the apparatus's own corpus cannot measure the axis honestly, that judgment
closes it at D **with a reason**, which the paths ledger wants and does not currently have.

---

## §7 · WHAT THIS VERDICT CANNOT SEE

The limits, stated so nothing here is read as broader than it is.

- **Provenance is entirely unverified.** I did not open TWT. Every incident behind every rule is,
  from where I sit, an assertion. If the incidents were wrong the rules would still look
  well-motivated to me, and I would not know.
- **I reviewed one commit.** Nothing about trajectory, velocity, or whether the gates hold under
  a real research load.
- **I never ran a research session.** No worker was dispatched, no claim banked, no review round
  completed. Every claim I make about *the method* is inferred from documents; only claims about
  *the machinery* are computed.
- **W9 is unmeasured here too.** `HANDOFF.md` says nobody has run session zero with a human, and
  the thing to watch is whether refuse-never-supply holds. I could not test that, and it is
  plausibly a larger risk than anything in §4 — it is the one place the apparatus is alone with
  the person who cares most.
- **My §6 pushback is ARGUED and touches a grade the coordinator set with more context than I
  have.** Treat it as a fork worth pricing, not a refutation.
- **I am a single instance of one model class,** reviewing a repository substantially authored
  with assistance from model classes I cannot identify. **By this repository's own RUL-065, if
  my class overlaps the authoring class, this entire review carries no information.** I cannot
  determine whether it does. That is not a rhetorical flourish — it is the finding of F1 applied
  to F1's own author, and it is the reason W10 should be built before the next external review
  is commissioned rather than after.

---

## §8 · REPRODUCTION

Everything above, in order, from a clean checkout of `bf302af`:

```bash
git clone https://github.com/yaerhf/research-ratchet && cd research-ratchet
git rev-parse HEAD                                  # expect bf302af295b44…

python scripts/check_records.py --self-test          # expect 30/30
python scripts/check_records.py                      # expect RECORDS HOLD
python rag/ingest.py && python rag/query.py "the diet is the role" -k 3 --source prompts

# the counted figures in F2
ls scripts/*.py scripts/*.sh rag/*.py | wc -l        # 15
grep -l "def self_test" scripts/*.py rag/*.py        # 2, both check_records*

# F1
grep -rn "model.class\|authored_by\|author_class" scripts/ rag/   # no matches

# the attached patches
python rag/diet.py --self-test                       # after W11: expect 27/27
bash scripts/install_dryrun.sh                       # after W12: expect PASSED
```

The four sabotages of §2 are reproduced by, in an installed tree: repointing the canon's handoff
pointer at a non-existent file; appending a row to `RULES_BY_ROLE.md` without regenerating packs;
and pointing `MAIN_SUITE` at a two-line script that prints a pass line and exits 1, then one that
exits 0 and prints nothing.

---

## §9 · ATTACHMENTS

| file | status |
|---|---|
| `rag_diet_self_test.py` | W11 patch. 27 demonstrations, run green against `bf302af`, with its own demonstrated failure mode proven by sabotage. Drop into `rag/diet.py`, wire `--self-test` into `main()`. |
| `scripts_install_dryrun.sh` | W12. Runs green against `bf302af`. Drop into `scripts/`. |
| `github_workflows_gates.yml` | W12. Four steps, all verified locally. |
| `telemetry_metric6.py` | W10. Cross-class metric, tested on synthetic rows in both branches (log present / absent). Merge into `honesty_telemetry.py`. |

---

*A closing note the coordinator may discard.* The reason this review could be specific is that
the repository made itself executable and said, in `WHY.md`, that executing it is the test. I
followed that instruction and it produced six findings in an afternoon. That is the design
working, and it is worth recording as such in the register — the apparatus's stated claim is not
that it prevents error but that error becomes findable and finding it becomes somebody's job.
On this evidence the claim holds.
