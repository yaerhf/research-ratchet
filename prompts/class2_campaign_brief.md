# CLASS-2 CAMPAIGN BRIEF — handoff for delegate sessions (2026-07-05)

*Written by the 2026-07-05 Fable review session at coordinator direction (Yaer), for execution
by Opus/Sonnet-class instances with an ultracode (multi-agent) mandate. Fable-class token
budget is exhausted until allowance renewal; this brief pre-digests the strategy, the exact
formulations, the numerical targets, and the traps, so that a smaller-model session can make
real Class-2 progress without having to re-derive the strategy itself.*

*Standing: this brief is a PLAN, not a result. Nothing in it is banked by virtue of being
written here. Every computation it proposes must be independently run, engine-verified,
adversarially reviewed, and banked per canon before it counts. Where this brief states a fact,
verify it against the cited file/primitive before building on it — the brief can be stale or
wrong; the engine cannot.*

---

## 0. Orientation — read these, in this order, before any work

1. `CLAUDE.md` (auto-loaded canon — the operating system; §2 tiers, §4 negatives, §5 guardrails,
   §8a review).
2. `knowledge/ledgers/TWT_worklist.md` — the frontier state; the Class-2 program paragraph;
   the "How to work an item" cycle (binding).
3. Companion Section 12 (Closability classification) in
   `knowledge/corpus/TWT_foundational_paper_companion.md` — the authoritative Class-2 program
   statement (2a/2b routes, the four classes, the per-item table).
4. Negatives ledger rows **N31, N32a, N33, N34, N37, N42** in
   `knowledge/ledgers/TWT_NEGATIVES_LEDGER.md` — the campaign's specific pre-paid dead ends.
   Do not skip N33/N34: they are the record of the LAST over-determination attempt and why it
   failed.
5. Companion Section 13 (Import Registry) — read any row before reusing its import; the
   dispersive package is I-13; FDT is I-12 (definitional).

**Your model class and what it implies.** You are likely a smaller model than the session that
wrote this. Your comparative advantages: disciplined execution of well-posed computations,
sympy-exact identity checking, numerics with certificates, bookkeeping, and (with ultracode)
adversarial verification fleets. Your principal risk: generating plausible-sounding theory and
banking it. Compensating rules, absolute for this campaign:

- **(a)** Never bank anything the engine did not verify. Prefer sympy-exact > certified
  numerics > prose. A result you cannot express as an engine check is not ready.
- **(b)** If a step requires a new theoretical idea not pre-formulated in this brief: STOP,
  bank the located gap (tried → failed → would-change-if), and move to the next task. That is
  success, not failure (canon §4).
- **(c)** Every load-bearing claim goes to the `twt-reviewer` subagent (fresh context) and
  iterates to consensus; ≤3 rounds, then escalate to the coordinator with both positions.
  On pushback, lower the CLAIM (tier/scope/wording), never massage the RESULT.
- **(d)** Ultracode fleets are for: independent re-derivation of identities you intend to bank
  (2–3 refuters, distinct code paths — the R-144/R-149 review pattern), parallel grid/parameter
  sweeps, and extraction passes over the corpus. Fleets are NOT for brainstorming mechanisms —
  that produces CANDIDATE soup, and this campaign needs exact facts and clean negatives.

---

## 1. The reframe that makes Class 2 tractable

**Class 2 does NOT mean "derive the kernel."** Per companion Section 12, the realistic closure
is **input-plus-over-determination**, on two legs:

- **(2a) Invariant-hunting** — "statics cornering dynamics": exact facts that hold for ANY
  kernel, each shrinking the kernel's allowed family. Existence proofs that this route is real:
  R-114 (memoryless kernel excluded by defect existence), the s=3 Adler-zero, the Θ_rel
  Z3-isotropy dichotomy, and most recently the whole R-125→R-149 chain (symmetry-shortcut
  results that bypassed the unknown kernel entirely).
- **(2b) Kernel-as-counted-INPUT + registry over-determination** — promote a minimal causal
  kernel family (1–2 dials: an amplitude and a relaxation scale, PLUS the discrete
  fading-vs-hysteretic fork as a separate branch choice) to an honest counted INPUT, then
  over-determine it across the pending-values registry. Success either way: consistency
  collapses ~15 SM magnitudes onto ~2 counted dials (falsifiable by the over-determination
  itself); contradiction banks a negative that narrows the family.

**The N33 verdict is the campaign's starting condition.** The 2026-07-02 attempt found the
registry **rank-deficient**: effectively ONE usable anchor (the KSS-floor-to-GW170817-ceiling
bracket on a single zero-frequency transport coefficient) against a ≥2-parameter kernel.
N33 names **four missing inputs** — these are the campaign's acceptance criteria; memorize them:

1. A real **macromolecule-interferometry floor number** (currently a numberless placeholder).
2. The **`Λ ~ H²` residual coefficient** (currently a scaling form, no number).
3. A genuine **sum-rule / Kramers–Kronig datum with a real number** (a static-susceptibility
   value or a short-distance equal-time correlator — companion Section 6, principle 7).
4. **Independently-justified frequency assignments per anchor** (the bare assertion "different
   frequencies" is explicitly forbidden — N33).

Inputs (1) and (2) need laboratory/cosmology numbers or the kernel itself — outside your reach.
**Inputs (3) and (4) are partially manufacturable from the substrate today.** That, plus the
2a list in Wave 3, is where this campaign can actually move.

---

## 2. The campaign — four waves, each item independently bankable

Work items strictly per the worklist cycle (orient → select → retrieve → work → review →
bank + full corpus sync) — one item fully banked before the next.

### Wave 0 — calibration (first half-session)

- Run `python twt_test.py` (must print ALL CHECKS PASSED; count was **397** on 2026-07-05 —
  verify the printed number and treat it as the new baseline).
- Confirm you can bank: `scripts/bank.sh "msg"` (works end-to-end on this Windows box with
  `python`; git identity already set: Yaer / hfyaer@gmail.com).
- Windows practicals (paid-for lessons): long bash heredocs FAIL — Write the text to the
  scratchpad and `cat >>` it instead; re-Read a file before Edit after any external change;
  in multi-block edit scripts, save per-file immediately (die-before-save loses everything).

### Wave 1 — gate-free compute queue (well-posed numerics; builds trust; feeds 2b)

These are the named Class-1 leftovers. They are ideal ultracode work (parallel sweeps,
independent-code-path verification) and each produces a bankable result or negative.

**W1.1 — The ω ≠ 0 co-rotating Hessian** *(WP-MASS-MEASURE residue (ii); the worklist's "one
possibly-gate-free analysis face")*. R-142 certified the breathing-channel (ℓ=0) Hessian
strictly positive (~0.21, box-saturating) on the STATIC slice. Extend to the co-rotating frame
at ω ≠ 0: linearize around `R* = exp(ûωτ₅/2)R₀(x)` (the R-125 co-rotating construction — read
`defect_phase_collective_mode_at_k4` and `one_particle_pole_moduli_identification` in `twt.py`
first; reuse their harnesses). Deliverable: positivity persists at small ω (upgrades the
(S)-static premise toward (S)-rotating), or a located instability threshold in ω — EITHER is
bankable. Built-in self-check: the exact co-rotating zero mode (R-125's) must read numerically
zero in your Hessian — if it doesn't, your discretization is broken, not the physics.

**W1.2 — Beyond-rigid-rotor B = 2 quantization over the R-144 torus** *(the binding-magnitude
residual)*. Rigid-rotor overbinds by ~113 MeV (massless) / ~124 MeV (refit) vs the deuteron's
2.22 MeV — the known classical-Skyrme character. Compute the leading beyond-rigid-rotor
(vibrational/breathing) correction over the banked toroidal minimizer
(`full_field_b2_below_threshold_sc1_datum`). Honest goal: the correction's SIGN and order of
magnitude. Matching 2.22 MeV is NOT expected — say so in the banked scope.

**W1.3 — Massive-pion full-field run** *(named follow-up of R-137/R-138 × R-144)*. Re-run the
full-3D charge-conserving flow with the chiral-breaking probe term `(μ²/4)x²(1−cosF)` at
μ = 0.196/0.263 (probe/refit). Confirm the torus survives and the below-threshold margin holds
in full 3D. Mechanical; reuse the R-144 machinery, keep its charge-guard + resolution
discipline (lattice winding is smooth-sector-protected ONLY — two recorded unwinding events).

**W1.4 (optional) — B = 3 third SC-1 datum**. Rational-map B = 3 (tetrahedral; literature-known
shape) through the same certificated pipeline as R-135 (`multi_skyrmion_b2_classical_binding`).
Only if W1.1–W1.3 are banked and quality signals are green.

### Wave 2 — the 2b infrastructure (the campaign centerpiece)

**W2.1 — Bank the constraint table as an engine artifact.** A new primitive — proposed name
`kernel_overdetermination_table()` (does NOT exist yet; you create it) — returning as DATA
one row per registry constraint: (observable; banked structural link to the kernel object;
empirical value or bracket; frequency window + its justification status; independence status).
Pre-digested rows (verify each against its cited source before encoding):

| Row | Content | Status to encode |
|---|---|---|
| KSS/GW bracket | `η/s ≥ ℏ/4π` floor; GW170817 ceiling `η ≲ 10⁹–10¹⁰ Pa·s` (companion reproduction: `6.5×10⁹`) | the ONE usable anchor; zero-frequency; carry N33's entropy-density caveat as a named premise |
| K_c renormalization | kernel must produce EXACTLY `(19/2)√38 ≈ 58.56` between bare LSWT stiffness and `K_c = 2J/19` (N31, `Kc_magnon_stiffness_canted_FM_at_DJ` — sympy-exact target) | structural-target (sharpest row known) |
| Running µΨ₀ | implied 1.69 → 0.56 across generations (N37, `updown_mirror_multigen_avg_vs_lepton`); sign-pinned > 0 (N32a) | two numbers + a drift direction = a shape constraint |
| τ_mem | rich branch `τ_wave·exp(S/ℏ)`; the fading `[3,380]` range explicitly NOT pinned (N34 caution — never treat it as a quantitative target) | bracket-only |
| C_T | at the Sakharov scheme scale `Λ_S = √(2π) M_Pl` (which-Λ ruling 2026-07-30; the old `[0.16, 0.72]` bracket is retired); integrand FIXED as a quadratic form in `(S, [Ω,Ω])` (R-149 `texture_gauss_equation_riemann_closure`); unknown = the mode measure | structural-target (see W3.1) |
| 1/Θ₀ ↔ Λ_QCD | `195.4 MeV`, fit-invariant across the scheme fork (R-138); CANDIDATE identification (R-111) | candidate anchor |
| σ_QCD | `≈ 0.18–0.19 GeV²` (§C.5.12, OPEN) | numberless (needs the kernel) |
| Chain (4) missing energy | anomalous missing energy in precision decay spectra would MEASURE Im χ | future falsifier row |
| m_N = 3µ² | R-134's 0.28% zero-parameter convergence; E-channel-conditional; naive I₄ route BLOCKED (N12) | candidate row |
| α_em / α_s / α_W | structural links only (§B.5b); NO frequency justification exists yet | non-anchors until input (4) lands; do NOT count `g` separately (`g² = 4πα·8/3` — same unknown, N33) |

The primitive's assert = the usable-anchor COUNT. Banking this table is a genuine result: it
operationalizes N33's would-change-if and becomes the campaign's dashboard. (`sin²θ_W = 3/8`
is gate-free and must NOT appear as an Im χ sample — N33 names this exact miscount.)

**W2.2 — Manufacture N33 input (3): a sum-rule datum from statics.** This is the one missing
input the substrate can plausibly supply today, and it is itself a 2a move: **moment sum rules
are operator identities — statics cornering dynamics.** Pre-formulated:

- Compute equal-time commutator moments (f-sum-rule class) and/or the static susceptibility
  for the relevant response channel on the canted D4 ground state at `D/J = 0.79` — the N31
  LSWT machinery (`Kc_magnon_stiffness_canted_FM_at_DJ`) already computes exactly this class
  of quantity, sympy-exactly. The first frequency-moment of `Im χ` equals an equal-time
  commutator you can evaluate on the lattice; `∫ dω Im χ(ω)/ω` equals a static susceptibility.
  Either gives a genuine (moment, value) pair — N33's input (3).
- **The safety line that decides whether this survives review:** causality/analyticity
  (Kramers–Kronig) holds for ANY causal response function, driven or not — SAFE to use.
  The fluctuation–dissipation theorem does NOT hold here — its violation residual IS Θ_rel
  (Import Registry I-12, definitional). Use only commutator/operator-identity moments and
  KK-analyticity; the moment you invoke FDT you have assumed away the very object the program
  is hunting. State this discrimination explicitly in the banked docstring.
- **The wrong-object trap (the campaign's most likely failure):** name exactly WHICH χ —
  operator, channel, layer (grain vs cell), frequency window. `theta_rel_universality_located`
  R1 documents the precedent (a zero-frequency FDR and a finite-drive-frequency reactive ratio
  are different objects bridged only by the unbuilt kernel). If the channel of your computable
  moment cannot be matched to the channel of any registry anchor, bank THAT as the located gap
  — it is exactly the kind of precise negative this campaign wants.

**W2.3 — N33 input (4): frequency assignments as checkable statements.** For each anchor row,
write the frequency-window argument out (e.g. KSS samples ω → 0 transport; mass-sector anchors
sample ω ≈ m·c²/ℏ at the cell scale; `Λ ~ H²` samples ω ≈ H). Each assignment must carry a
justification or an explicit "UNJUSTIFIED" flag in the table. No bare assertions.

**W2.4 — Only after W2.1–W2.3: the 2-dial fit.** Parametrize the kernel family minimally
(amplitude χ₀ + relaxation scale τ; the fading-vs-hysteretic fork as a discrete branch, chosen
per branch and reported separately — N33: the fork is NOT a fittable knob). Fit against the
usable anchors; report the rank honestly. If still rank-deficient, bank the updated count and
the updated missing-input list — that IS the deliverable. **The promotion of the fitted family
to a counted INPUT is a coordinator decision — prepare the case; do not enact it.**

### Wave 3 — pre-formulated 2a invariant hunts (bounded, engine-checkable)

**W3.1 — Count the C_T mode-measure moments** *(P2-2 endgame; highest structural value)*.
R-149 fixed the induced-EH spectral integrand as a quadratic form in `(S, [Ω,Ω])`. The
question: under the symmetries the banked scaffold already establishes (Spin(4) frame action;
the compact SO(3)×SO(3) internal action of R-145; parity), **how many independent invariant
quadratic forms exist on that space?** Read `texture_gauss_equation_riemann_closure` and
`texture_frame_6to4_reduction` first and take the space's definition FROM THE ENGINE, not from
prose. This is pure Schur/commutant counting — the engine's home turf (precedent: R-124's
commutant-2 cross-check). Deliverable: "`C_T = Σ cᵢ Mᵢ` with N independent kernel moments" —
reduces C_T from an unknown FUNCTION to N unknown NUMBERS. If N ≤ 2, C_T joins the W2.4 fit.
Bankable for any N; a large N is still a banked structural fact.

**W3.2 — The µΨ₀ seat integral** *(W-LIVE-1 mechanism face)*. R-129 proved the coupling cannot
live in sign-gauge-respecting snapshot algebra — it must engage the winding topology; the
standing candidate seat is §D.4.4's `ρ_L` boundary term (R-110). Pre-formulated: compute the
`ρ_L` boundary integral EXPLICITLY on the banked profiles (the R-133 B = 1 hedgehog; the R-144
torus). If it vanishes identically → clean negative, the seat moves (bank it). If nonzero →
the coupling's FORM is derived (value still kernel-gated) and N37's running dial acquires a
candidate shape. Trap: N28/N32a — statics gives the mirror's two-ness, never the split's value;
you are deriving a SEAT, not µΨ₀ itself. Any value claim is an automatic OVER-CLAIM.

**W3.3 — The SNIC/Adler locking-threshold computation** *(the fork's own dynamical
discriminator — N33 would-change-if (iv); Section 12's named handle)*. Question: does a
hysteretic `τ_mem` clear the locking threshold in `theta_rel_rotating_wave_escape_located`?
Read that primitive first; this is a bounded dynamical-systems threshold computation, not open
theory. Either outcome advances the fork; an inconclusive outcome banks WHY (which missing
number blocks it).

**W3.4 (stretch; highest risk) — A second Θ_rel binary.** The Z3-isotropy dichotomy
(`theta_rel_z3_isotropy_dichotomy`) is the template: a kernel-free BINARY shared across faces.
Hunt the next one — e.g. does the coset-Cartan direction force a sign/ordering relation on the
CKM-P 3-distinct splitting (an inequality, not values)? Hold yourself to sympy-exact
statements; if after one honest attempt nothing exact emerges, bank the negative and stop.
Do NOT let this become mechanism-brainstorming.

### Wave 4 — synthesis and close-out

- Coverage discipline per bank (canon §10): engine primitive + suite check (verify the printed
  total INCREMENTS), companion Result Index row, paper passage if paper-worthy, worklist row —
  all in the SAME pass. `scripts/bank.sh` after each item.
- End of campaign: re-run the W2.1 rank count; write the campaign close-out in the worklist
  (which waves banked, which located gaps, the updated missing-input list for the next
  session); update `TWT_STRATEGIC_MAP.md` if the picture shifted.

---

## 3. The keys — traps this program has already paid for, mapped to THIS campaign

1. **Wrong-object χ conflation** (N11-R1, N33, N34) — the campaign-killer. Two dimensionless
   ratios or two response functions are the same object only if operator, channel, layer, and
   frequency all match. Name all four, every time.
2. **FDT is not available** — Θ_rel is DEFINED as its violation (I-12). Causality/KK: yes.
   FDT: no. (See W2.2.)
3. **WP-DC2 screens the fork in the macromolecule window** (N34 died partly on this): the
   Goldstone-protected decoherence floor is fork-blind at leading order — do not claim fork
   discrimination through it.
4. **Anchor-counting discipline** (N33): `g` is not a second anchor; `sin²θ_W` is not an Im χ
   sample; one-sided brackets are not (frequency, value) pairs; "different frequencies" without
   justification is forbidden.
5. **N42 — calibrate the load-bearing vertex**: any action-sign or dispersive work must derive
   the sign-sensitive vertex in-suite (series or positivity anchor) — machinery calibration
   cannot reach it; a Euclidean↔Minkowski transplant refuted the first R-148 build.
6. **Suite dead-check trap** (N31/N32a phantom checks): a check appended after `sys.exit()`
   never runs; a check never written still prints "PASS" for everything else. After banking,
   verify the printed TOTAL moved by your delta and grep `twt_test.py` for your check's call.
7. **Bank before you cite** — no "engine-verified" in any prose/docstring for a primitive not
   yet in the suite. This brief's proposed primitive names do not exist yet.
8. **Register imports** (canon §2; Section 13). Any external theorem used load-bearing gets its
   registry row in the same pass, with level (inside-frame vs substrate), status, retirement
   handle, revert clause. P2-3's a-theorem/KL leads are pre-registered at 13.3 — read before
   touching.
9. **Menu vs pick; L/Q ≠ SD/ASD** (the fibration in §A.5.2 is the honest bridge — R-140 lives
   in the CHIRAL basis, not the orbit basis); **two scales** (grain vs cell — never collapse);
   **quarks have no individual mass** (hadron masses verify; quark masses indicate);
   **e5-litmus** (e5 = phase, never a spatial DOF); the hole-image is a picture, not a premise.
10. **Never "impossible"** — every dead end lands in the ledger as
    tried → failed-because → would-change-if, with the next N-number.
11. **Reviewer reality**: expect the twt-reviewer to rebuild your pipeline independently on its
    own fields/code paths (R-144/R-149 precedent) — write your computations so that is easy
    (self-contained primitives, stated conventions, certificates).

---

## 4. Decision rights

- **You may decide alone:** running any computation above; banking negatives/located gaps;
  banking exact identities that survive review; table rows and their status labels; tiers up
  to FRAMING/CANDIDATE on your own new objects.
- **Coordinator (Yaer) decides:** counting ANY new INPUT (in particular the W2.4 kernel-family
  promotion); registering any NEW import (pre-registered rows may be used per their rows);
  ontology-level paper changes; reviewer deadlocks after 3 rounds; anything that would touch
  the canon.

## 5. Success criteria

- **Minimum honest success:** Wave 1 items banked + the W2.1 constraint table banked + one of
  {W2.2 sum-rule datum, its precise located-gap negative}.
- **Good:** + W3.1 moment count (any N) + W3.2 seat integral (either outcome).
- **Excellent:** W2.4 executed at honest rank ≥ 2 with a consistency verdict either way.
- **Still success:** every attempted item that failed is a ledger row sharp enough that the
  next session starts ahead of where you did.

*A finding not written to a file did not happen. Bank as you go.*
