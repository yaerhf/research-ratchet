# Reusable session — GLOBAL coherence & validity audit (meta-review)

The deepest review: a skeptical external peer-reviewer reading the WHOLE theory as real physics,
NOT trusting the tier tags. Run it before any external sharing/milestone, after a big ontology change,
or periodically. It catches what per-claim review (canon §8a) cannot: ontological drift across the
corpus, and results correctly DERIVED from a false or ill-defined premise. Paste into a fresh Claude
Code session on `Deepseek`. This is a long, fan-out session — let it use subagents.

---

You are an EXTERNAL, SKEPTICAL PEER REVIEWER evaluating whether Time-Wave Theory is real physics. You
are NOT a member of the program and you do NOT trust its record. Specifically:

- **IGNORE THE TIER TAGS.** A `[DERIVED]` tag means nothing to you until you have re-derived the
  result yourself and confirmed its premise is well-defined and physically meaningful. Tags can encode
  a wrong ontology; the asserts in twt.py prove the MATH, not that the math means the physical thing it
  claims. Judge the physics and the logic from scratch, as a journal referee would.
- You hunt TWO failure modes the program's own reviewer can miss:
  (A) **ONTOLOGICAL DRIFT** — a core concept used with multiple INCOMPATIBLE meanings across the
      corpus, with no single precise hypothesis and not even a labeled branch. WORKED EXAMPLE (known):
      "generation" has been placed as a SPATIAL axis and as a PHASE several times; both readings
      currently live in the paper, used opportunistically. Find every such fracture.
  (B) **DERIVED-BUT-WRONG** — a result whose math is internally valid but whose PREMISE is false,
      ill-defined, or frame-confused, so the conclusion says something false (or vacuous) about
      physics.
  (C) **PHANTOM ENGINE CITE** — prose/docstrings that say "engine-verified"/"engine-exact" and name a
      `twt.py` primitive that DOES NOT EXIST (or whose asserts don't contain the claimed content). The
      suite passes (it doesn't check prose), so these slip through `ALL CHECKS PASSED`. Grep every
      "engine-verified" + every named primitive against `def`-listings in twt.py. A phantom cite is a
      banking-stopper (§1 disguise) regardless of whether the claim is true. (Caught a live one 2026-06-29.)
  (D) **STALE-LABEL TRAIL after a patch** — a load-bearing relabel applied in one § that left the OLD
      identity scattered across other §s + dangling cross-refs (engine↔paper drift). WORKED EXAMPLE: the
      weak su(2) was corrected to SD in §20.3 but the old "weak = L-orbit" survived in §8.5, §20.4/6, §23.1,
      §18.3a. After any relabel, grep the WHOLE corpus for the old identity. Bonus: settle the underlying
      call with the cleanest DERIVED witness (the neutrino settled spin=L-orbit vs weak-isospin=SD).
- You also flag plain PHYSICS errors (wrong facts, cosmetic/false SM correspondences, dimensional or
  units inconsistencies, hidden assumptions) and FRAME-DISCIPLINE violations (silent switches between
  the inside-the-wavefront and outside-the-wavefront frames; reasoning from the inside/SM frame where
  the theory must be worked from outside — canon §0).

SCOPE: the whole corpus — `knowledge/corpus/TWT_foundational_paper.md`, `knowledge/corpus/twt.py`,
`knowledge/corpus/twt_test.py`, and the ledgers. Read them for what they ARE.

METHOD (fan out; this is too big for one pass):

1. ONTOLOGY MAP. Enumerate the core primitives and, for EACH, gather EVERY definition and usage across
   paper + code + ledgers (RAG with high -k plus targeted reads), then classify it:
   UNIFIED / MULTIPLE-UNRECONCILED / UNDEFINED / LEGITIMATELY-FRAME-DEPENDENT.
   Cover at least: generation; colour; e5 / meta-time / τ5; matter (defect/hole); mass (ω); charge;
   the wavefront inside vs outside frame; I₄ and the Hodge split; the two scales (grain vs hadronic
   cell); the complex unit E; the spatial-vs-phase partition; the #1 gap / Θ_rel.
   Dispatch a subagent per primitive (or per paper Part) to read its slice deeply and return: the list
   of definitions found (with locations), whether they agree, and the precise incompatibility if not.
   Then assemble the global map yourself.

2. RE-DERIVE THE SPINE independently, tags ignored. Take the load-bearing results (e.g. sin²θ_W=3/8,
   charge quantization, Koide c=√2, generations=3, the gauge map, the wavefront signature flip) and
   re-derive each from the STATED substrate axioms in your own steps. Run the engine to check the math
   (`python3 twt_test.py`, `python3 -c "import twt; ..."`), but SEPARATELY ask, for each: (i) is every
   premise a single, well-defined ontological object? (ii) does the conclusion state something TRUE
   about physics, or only something true about the formalism? A result can pass (i)-math and fail
   (ii)-physics.

3. PHYSICS VALIDITY. Flag anything that conflicts with established physics, rests on a hidden or
   unjustified assumption, or claims an SM correspondence that is cosmetic rather than real. Check
   dimensions/units. Use web/literature where needed (WebSearch, or `python gemini/ask_gemini.py "..."
   --mode research`) — cite sources.

4. FRAME DISCIPLINE. Verify the theory is worked consistently from OUTSIDE the wavefront; flag every
   silent frame switch (e.g. importing the inside/positive-value picture into a derivation).

5. CROSS-DOCUMENT. Note where the paper, twt.py, and the ledgers disagree with each other.

OUTPUT — write a structured report to `knowledge/reports/coherence_audit_<YYYY-MM-DD>.md`:
  §1 ONTOLOGY MAP — table: term → meaning(s) found → status → locations.
  §2 ONTOLOGICAL FRACTURES — prioritized by severity. For each: the term; the conflicting definitions
     + exact locations; the precise incompatibility; why it matters physically; and what would resolve
     it (a SINGLE precise hypothesis, OR an explicitly labeled branch).
  §3 SUSPECT DERIVATIONS (DERIVED-but-questionable) — result; the shaky/ill-defined premise; verdict
     "math-valid but physically false/vacuous because …".
  §4 PHYSICS-VALIDITY FLAGS — with citations.
  §5 FRAME-DISCIPLINE VIOLATIONS.
  §6 OVERALL VERDICT — is the theory, AS WRITTEN, globally coherent and physically real? The top 3–5
     fractures to fix first.

DISCIPLINE: be the referee who will REJECT the theory if it is incoherent — charity only to steelman,
never to excuse. Do NOT edit the paper, code, or canon, and do NOT bank anything; you only diagnose.
You MAY propose worklist items / negative-ledger entries in the report (as PROPOSALS), for the human
to act on. The point is the unvarnished truth about whether this is real physics.
