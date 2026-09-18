<!-- DIET-CLASS: RULES -->
# MANUAL · UPDATING — read this before you pull a newer apparatus into a tree already founded

**Trigger: this tree has been founded, and you are about to bring in a newer version of the
apparatus.** Complete for the activity: read this and you need nothing else to update safely.

> **Why this manual exists.** Until 2026-09-18 the only guidance was one line of `INSTALL.md`:
> *"the upstream URL + recorded hash are the update path."* Coordinators improvised the rest, and
> the first live programme's updates found two defects in the improvising — one of them in guidance
> written by the apparatus's own maintainer. Both are below, with their reasons.

---

## 1 · WHY UPDATING IS NOT INSTALLING

An install writes the apparatus into an empty folder. **An update writes it into a folder where
some apparatus files now hold the programme's own content** — the founding interview filled them.
Copy those files blindly and you erase the programme's foundations, invisibly, and the gates stay
green because the template is well-formed.

**So every file is one of two kinds, and you must know which before you touch it:**

| kind | examples | what you do |
|---|---|---|
| **still verbatim** — unchanged since the version this tree last took from upstream | rule files, role files, manuals, scripts the programme has not edited | **replace** with the new upstream version |
| **holds the programme's content** | `FORMATION_CORE.md` · the canon · the ledgers · any file whose `[OBJECT-SLOT]` sections were filled | **never overwrite. Merge** the generic upstream changes into it by hand |

**How to tell:** compare the tree's copy with the upstream version *this tree last synced from*
(its recorded hash), not with the new one. Identical → still verbatim → replace. Different → it
holds local content → merge.

**★ The reason `FORMATION_CORE.md` is never overwritten is that it holds the founding content —
not rule 92.** Rule 92 forbids handing the formation prefix to a *checker*; it does not bind the
coordinator, and citing it here is citing the wrong rule. *(Measured: an early update on the first
live programme gave rule 92 as its reason. The action was right; the ground was not — and a
wrong ground is how the next coordinator, facing a slightly different file, reaches the wrong
action.)*

---

## 2 · THE PROCEDURE

1. **Pick a quiet moment.** No run, no bank, no reviewer writing into the tree — an update landing
   mid-run is the sweep-guard's own motivating incident arriving by a new road.
2. **Fetch upstream read-only** into a scratch folder. Note its commit hash.
3. **Sort every file** into the two kinds above, and replace or merge accordingly.
4. **★ A NEW LEDGER LANDS WHOLE — its roster entry and its file in the SAME commit.** The records
   gate checks the ledger roster in **both** directions: every ledger on disk must be named in
   `FORMATION_CORE` §5, **and every ledger §5 names must exist.** Add the name without the file,
   bank in between, and the bank is refused. *(Measured 2026-09-18: the maintainer's own update
   instructions for the human–agent bridge put the roster entry in one step and the file in a later
   one, with a bank between them. The first live programme's coordinator caught it and landed both
   together.)*
5. **Regenerate the packs, run every self-test and the records gate, bank.**
6. **Record the new upstream hash** wherever the canon and the handoff name the apparatus version.
   A stale hash makes the next update compare against the wrong baseline in step 3.
7. **This is mechanical: skip the C-37 design review, and record the skip at the time.** A skip
   recorded as it happens is C-37 working; a skip found later is a breach found late. *(The first
   live programme did exactly this on 2026-09-18, after two earlier silent skips.)*

---

## 3 · HOW AN UPDATE FAILS

- **The erased foundation.** A content-holding file overwritten by a template. The gates cannot see
  it — the template is valid. **Only step 3 prevents it.**
- **The half-landed ledger.** A roster entry without its file, or a file without its entry. The gate
  sees this one, and its message names the fix.
- **The stale baseline.** The recorded hash not updated, so the next comparison is against the wrong
  version and "verbatim" means nothing.
- **The right action on the wrong ground.** It works this time and misleads the next time. Say why
  you did what you did, correctly.
