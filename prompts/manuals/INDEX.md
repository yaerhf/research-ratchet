# ACTIVITY MANUALS — the lazy-loaded documentation tree

**v1, 2026-08-20**, on the human coordinator's directive: *"Can we issue manuals for activities,
containing the how-to and the rules that go along with them? It might also reduce initial token
count. The agent reads a manual only if needed. We could extend this principle as a documentation
tree of which the agent only knows the items initially."*

---

## THE PRINCIPLE

**An agent's starting context carries the INDEX, not the content.** It knows that a manual exists
and what it covers — one line each. **It opens one only when it is about to do that activity.**

This replaces the earlier "activity blocks" design, and it is better for the reason the coordinator
gave: **the block scheme still shipped the rules to everyone who might do the activity; the manual
ships only the name.** Measured motivation: a probe-scale dispatch was paying roughly **20,000
tokens of fixed overhead to do ~600 tokens of work**, and the activity rules were part of that
freight.

**Why this is safe.** Activity rules bind *during the activity*, not before it. An agent that never
edits the paper never needed the paper rules; an agent about to edit the paper reads them **at the
moment they become binding**, which is also the moment it will actually retain them.

**Why it is not merely a folder.** Three properties make it a tree rather than a pile:

1. **Every manual is REACHABLE FROM THIS INDEX and from nowhere else** — one entry point, so a
   manual cannot go unreferenced and quietly stale. `check_records` should pin that.
2. **A manual is COMPLETE for its activity.** An agent that reads it needs nothing else to act
   correctly. If a rule matters during banking, it is in the banking manual — even if it also
   lives in the core.
3. **The index line states the TRIGGER, not the topic.** *"Read this before you touch the paper"*
   beats *"paper editing"*, because an agent scanning an index is deciding whether it is about to
   do the thing.

---

## THE MANUALS

| manual | **read this if you are about to…** | status |
|---|---|---|
| `banking.md` | **bank anything** — run `bank.sh`, commit, or add a check | **WRITTEN** |
| `paper_editing.md` | touch `TWT_foundational_paper.md` or its companion | owed |
| `checking.md` | serve as reviewer, meta-observer, keeper, or contra-reviewer | owed |
| `dispatching.md` | compose a brief and launch a worker | owed |
| `probing.md` | build a probe, a simulation, or a numerical experiment | owed |
| `releasing.md` | render a PDF, sync the mirror, or publish anything | owed |

**Owed manuals are not missing rules** — the rules exist in `RULES_CORE.md`, `RULES_BY_ROLE.md`
and the role files, and remain binding. What is owed is their *migration* into activity form.
**Until a manual is written, its activity's rules are read from the role packs as before.**

---

## THE EXTENSION — a documentation tree, not just manuals

The same principle generalizes past activities. **An agent should start knowing the NAMES of things
and reading the CONTENT on demand**, wherever the content is large and conditionally needed:

- **already works this way:** the governing records in `knowledge/audit/` (named in the map, opened
  when relevant), the engine primitives (queried, not bulk-loaded — *see the retrieval note below*)
- **should work this way and does not yet:** the eleven-plus ledgers, the paper's parts, the
  companion's sections, the import registry

**The retrieval half is the enabling condition and it is currently broken.** A query against the
index costs roughly **8× less** than reading the engine, both engines are already indexed per
primitive, and **the documented invocation fails on this machine** — which is why nobody queries.
Fix that and the doc-tree principle becomes cheap everywhere at once; leave it broken and every
"read on demand" instruction degrades into a bulk read.

---

## THE HAZARD, NAMED

**A tree of manuals is a tree of places for a rule to go stale**, and this programme has measured
that exact failure — a binding sweep rule that said *"all five ledgers"* when there were eleven,
under-specifying its own surface by six files.

**So: a manual duplicating a rule creates a drift pair, and drift pairs are how this corpus breaks.**
Two mitigations, both required:

- **The manual QUOTES with a pointer, or OWNS outright — never paraphrases.** If the banking manual
  restates a core rule, it quotes it verbatim and names where it lives. Paraphrase is what drifts.
- **`check_records` should verify the index lists every manual present and every manual is
  reachable from the index.** Cheap, mechanical, and it is the same invariant family that already
  catches an unnamed ledger.
