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

**The hazard, stated plainly:** only `knowledge/audit/` is excluded from the index. The round
directories under `knowledge/candidates/` — which hold **the derivations under review and every
persisted verdict** — *are* indexed. So an unbounded query from a STARVED role is one keystroke
from voiding the measurement it was dispatched to make, and it leaves no trace: the verdict
looks identical.

`--diet` applies the bound mechanically and **prints it with the results**, so the transcript
carries proof of what was in force:

| bound | reaches | for |
|---|---|---|
| `open` | everything indexed | worker · reviewer · keeper · philosopher · coordinator · auditor · archivist · clerk · N2 |
| `starved` | everything **except the round directories** | the meta-observer |
| `bare-statement` | canon, engine and ledgers **only** | the re-derivation agent |

The dispatching brief's `[RETRIEVAL]` line names the bound (`coordinator_agent.md`, brief
format); the apparatus auditor checks that line against what the transcript shows, exactly as
it checks `[DIET]` against what the brief contained. `--exclude SUBSTR` (repeatable) narrows
further. **A diet bound is not a courtesy — it is the instrument.**

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
