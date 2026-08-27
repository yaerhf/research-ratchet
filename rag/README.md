<!-- DIET-CLASS: TOOLING -->
# THE RETRIEVAL LAYER — installed by default, optional by ruling

**Status: DEFAULT-INSTALLED, OPTIONAL** (human coordinator, 2026-08-27: *"The RAG is important
but can be optional. By default install it."*)

## What it is for

Two duties in the apparatus rest on this layer, and both degrade rather than break without it:

1. **`bank.sh` gate `[3/4]` re-indexes at every bank**, so the record stays retrievable as it
   grows. A record nobody can find drifts out of use — and the founding programme measured the
   consequence directly: when the documented retrieval command silently failed on the working
   box, retrieval stayed *"available and unused"* and every read-on-demand instruction
   degraded into a bulk read (`AGENT_RULES.md` §0, the environment-trap row).
2. **Query instead of bulk-load** (`RULES_BY_ROLE.md` #171; the doc-tree principle in
   `manuals/INDEX.md`). An agent that can query a primitive does not have to read the engine;
   that is the economics the whole lazy-loading design assumes.

The coherence keeper's fourth search axis — *the same object, however differently named; names
drift, objects do not* — is the one place retrieval is doing irreplaceable work rather than
saving tokens.

## ★ Diet bounds — retrieval must not breach a starvation

**The hazard:** only `knowledge/audit/` is excluded from the index. The round directories under
`knowledge/candidates/` — the derivations under review and every persisted verdict — *are*
indexed. So an unbounded query from a STARVED role is one keystroke from voiding the
measurement it was dispatched to make, and it leaves no trace: the verdict looks identical.

**The bound is over CONTENT, not paths — and that correction was forced by a measured defect.**
The first design bounded by directory. It leaked: `starved` allowed `prompts/`, and
`FORMATION_CORE.md` lives there, so the meta-observer's own bound returned the one file rule 92
(ABSOLUTE) forbids passing to a checker. **A bound that permits an absolute breach is not a
bound.** Now every artifact declares what it *is* —

```
<!-- DIET-CLASS: DERIVATION -->      markdown (invisible when rendered)
# DIET-CLASS: ENGINE                 code
```

— and `rag/diet.py` maps roles to the classes they may receive, each denial carrying its reason
so the auditor can check it rather than merely trust it. Unmarked files fall back to a path
heuristic that is **fail-safe, never fail-open**: an unmarked file in a round directory is
treated as a DERIVATION, and an UNCLASSIFIED artifact is refused to any role that carries a
starvation.

```bash
python rag/query.py "question" -k 8 --role meta-observer   # bounded retrieval
python rag/diet.py --role meta-observer FILE               # may I open this at all?
python rag/diet.py --role rederivation --list              # what may I see, and why not the rest
python rag/diet.py --audit knowledge/candidates            # what is still unmarked?
```

The brief's `[RETRIEVAL]` line names the **role** (never a bound — a role cannot be picked wrong
the way a flag can). The bound and anything WITHHELD are printed with the results, by class name
and never by content, so the transcript is the proof of what was in force.

**What this cannot do, said plainly.** Every role has a file-reading tool: this makes an
*accidental* breach hard, not a deliberate one impossible. That is the same honest position as
the rest of the apparatus — most rules have no mechanical enforcement, and the answer is to make
the break **cheap to declare and expensive to hide**, never to oversell the control. If you
breached your diet, say so in your report.

## Two scope decisions that are architectural

- **`knowledge/audit/` is NOT indexed, by design.** Governing records are reachable only by
  explicit pointer, and the session handoff's sole path is the canon's pointer line. This is a
  **diet implemented at the file layer** — the same instrument as the role diets. Do not
  "fix" it.
- **Code is chunked per primitive** (via `ast`), not per file, and each chunk carries the full
  docstring — because *read the row before you reuse it* (C-18) is unenforceable if the
  retrieved chunk drops the warning the docstring carries.

## Using it

```bash
python rag/ingest.py                 # build/refresh the index (bank.sh does this at [3/4])
python rag/ingest.py --check         # report what would be indexed; write nothing
python rag/query.py "question" -k 8
python rag/query.py "question" -k 8 --source code     # both engines + harnesses
```

`--source` shorthands: `paper` · `code` · `ledgers` · `prompts` · `scripts` · `all`.
Output is `[source §name]` + excerpt, which is the citation form the apparatus's rules require.

## What this implementation is, honestly

**A dependency-free lexical (BM25) reference implementation.** No embeddings, no model, no
network, no install step — it runs anywhere Python does, which is the property that matters for
an apparatus meant to be instantiated in one paste.

**Its limit, stated plainly:** lexical retrieval matches *words*, not *meaning*. It will miss a
paraphrase that shares no vocabulary with the text — precisely the case the keeper's "names
drift, objects do not" axis cares about most. The founding programme ran an embedding store on
a local GPU and got better recall there.

**Swapping it is expected and supported.** Keep the CLI contract in `query.py`'s header —
positional question, `-k`, `--source` with the same shorthands, `[source §name]` output — and
nothing else in the apparatus needs to change: `bank.sh` calls `ingest.py`, the documents quote
the `query.py` form, and `check_records.py` pins only that the `code` shorthand reaches the
companion engine.

## Running without it

A tree with no `rag/` is a legitimate configuration. What happens:

- `bank.sh` gate `[3/4]` prints a **loud SKIP** naming the layer as uninstalled and does not
  fail the bank. (A *failing* ingest still stops the bank — that is the recorded defect this
  gate exists around: `ingest.py` dying at the end of a run leaves the commit silently
  skipped, which is why the banking manual insists you verify with `git log`.)
- `check_records.py` reports the tooling-coherence check as `n/a` instead of failing it.
- Every "query the corpus" instruction in the apparatus degrades to "read the source" — which
  is *correct but expensive*, and the reason this layer is installed by default.
