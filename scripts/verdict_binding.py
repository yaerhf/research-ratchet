#!/usr/bin/env python
# DIET-CLASS: TOOLING
"""VERDICT BINDING — a verdict names the bytes it judged, and says what its checker read.

★ WHY (W29, 2026-09-28, two ideas from an independent orchestration system, the Bureau by
Novadiem Studio — credited, not copied: that repository carries no licence).

1. A VERDICT IS BOUND TO WHAT IT REVIEWED. The dispatcher stages the verdict file with the
   artifacts under review and a hash of each. When the artifact changes afterwards, the verdict
   no longer describes it, and until now nothing said so: a verdict on a claim edited after
   review read exactly like a current one. That is rule 94's stale probe on the verdict side.
2. THE CHECKER DECLARES WHAT IT READ, AND THE LIST IS CHECKED BOTH WAYS. MISSING: an artifact it
   was given and never opened. OUTSIDE THE DIET: a file its role may not receive — which is rule
   205 checked after the fact instead of only asked for. A read outside the diet table is not
   refused if it is DECLARED with its reason (`outside-diet:`), because rule 205's own standard
   is that a breach reported honestly is recoverable and one reported clean is not. Only the
   UNDECLARED one fails.

THE FORMAT — an HTML comment, invisible when rendered, like the DIET-CLASS marker. It must start
at the beginning of a line and outside any code fence (so documentation SHOWING the format is
never read as a binding — the founding check that matched its own documentation is why):

    <!-- VERDICT-BINDING v1
    role: reviewer
    reviewed: knowledge/candidates/R001/DERIVATION.md sha256:<hex>
    read: knowledge/candidates/R001/DERIVATION.md sha256:<hex>
    read: knowledge/ledgers/NEGATIVES_LEDGER.md sha256:<hex>
    outside-diet: knowledge/candidates/R001/NOTES.md — why it was opened
    accepted-change: knowledge/candidates/R001/DERIVATION.md sha256:<hex> — why it still applies
    superseded-by: knowledge/candidates/R001/VERDICT_REV_r002.md
    -->

`reviewed:` is written by the DISPATCHER (`stage`), `read:` by the CHECKER (`read`), and
`accepted-change:` by whoever edits a reviewed artifact and holds that the verdict still applies
(a typo fix) — the break clause, made visible: a new hash is accepted only WITH a reason.

THE HASH is sha256 of the file with CRLF normalized to LF. Not decoration: this repository runs
`core.autocrlf=input`, so a file stamped from a Windows working copy with CRLF endings is checked
out on CI with LF ones, and a raw-byte hash would report every such verdict stale.

WHAT THIS CANNOT SEE — stated, and pinned in `--self-test`:
  * WHETHER THE CHECKER READ WHAT IT LISTS. The read list is the checker's ASSERTION: it proves
    the evidence set that was claimed, never the care, and a file listed but never opened passes.
  * A FORBIDDEN FILE OPENED AND NOT LISTED. The diet check sees the list, not the reads.
  * A MEANING CHANGE ACCEPTED UNDER A FALSE REASON. The hash binds bytes; whether "typo fix" is
    true is a reader's judgment.
  * AN UNBOUND VERDICT. A verdict with no binding block is COUNTED, never checked.

RUN
    python scripts/verdict_binding.py stage VERDICT.md --role reviewer ARTIFACT [ARTIFACT...]
    python scripts/verdict_binding.py read VERDICT.md FILE [FILE...] [--outside-diet "reason"]
    python scripts/verdict_binding.py accept VERDICT.md ARTIFACT --reason "why it still applies"
    python scripts/verdict_binding.py supersede VERDICT.md --by NEW_VERDICT.md
    python scripts/verdict_binding.py check          # the whole tree; exit 1 on a failure
    python scripts/verdict_binding.py --self-test
"""
import argparse
import hashlib
import re
import sys
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError, ValueError):
        pass

ROOT = Path(__file__).resolve().parent.parent
OPEN = "<!-- VERDICT-BINDING"
CLOSE = "-->"
LINE = re.compile(r"^(role|reviewed|read|outside-diet|accepted-change|superseded-by):\s*(.*)$")
HASHED = re.compile(r"^(\S+)\s+sha256:([0-9a-f]{64})(?:\s+(?:—|--|-)\s+(.*))?$")
REASONED = re.compile(r"^(\S+)\s+(?:—|--|-)\s+(.+)$")
SKIP_DIRS = {".git", "dist", "node_modules", "__pycache__", ".venv", "venv"}


# ---- pure functions, so the demonstrations need no tree ------------------------------------------

def norm_sha(data):
    """sha256 over the bytes with CRLF normalized to LF (see the module docstring)."""
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def find_block(text):
    """→ (first, last) line indices of the binding block, or None. Outside code fences only."""
    lines = (text or "").splitlines()
    fenced = False
    for i, line in enumerate(lines):
        if line.startswith("```") or line.startswith("~~~"):
            fenced = not fenced
            continue
        if not fenced and line.startswith(OPEN):
            for j in range(i + 1, len(lines)):
                if lines[j].strip() == CLOSE:
                    return i, j
            return i, None
    return None


def parse(text):
    """→ the binding as a dict, or None when the file carries none. A half-written block is not
    None: it parses with `errors`, because a broken binding is a defect, not an absence."""
    span = find_block(text)
    if span is None:
        return None
    first, last = span
    lines = text.splitlines()
    b = {"role": None, "reviewed": [], "read": [], "outside": [], "accepted": [],
         "superseded_by": None, "errors": []}
    if last is None:
        b["errors"].append("the binding block is never closed with -->")
        last = len(lines)
    for raw in lines[first + 1:last]:
        line = raw.strip()
        if not line:
            continue
        m = LINE.match(line)
        if not m:
            b["errors"].append(f"unreadable line: {line[:70]}")
            continue
        key, val = m.group(1), m.group(2).strip()
        if key == "role":
            b["role"] = val or None
        elif key == "superseded-by":
            b["superseded_by"] = val or None
        elif key in ("reviewed", "read"):
            h = HASHED.match(val)
            if not h or h.group(3):
                b["errors"].append(f"{key}: expects 'PATH sha256:HEX', got: {val[:70]}")
            else:
                b[key].append((h.group(1), h.group(2)))
        elif key == "accepted-change":
            h = HASHED.match(val)
            if not h or not (h.group(3) or "").strip():
                b["errors"].append("accepted-change: a new hash is accepted only WITH a reason "
                                   f"('PATH sha256:HEX — why'), got: {val[:70]}")
            else:
                b["accepted"].append((h.group(1), h.group(2), h.group(3).strip()))
        elif key == "outside-diet":
            r = REASONED.match(val)
            if not r:
                b["errors"].append(f"outside-diet: expects 'PATH — reason', got: {val[:70]}")
            else:
                b["outside"].append((r.group(1), r.group(2).strip()))
    return b


def stale(b, current):
    """Reviewed artifacts whose bytes are no longer the bytes judged. `current(path)` → hash or
    None. A change is excused only by an accepted-change carrying the CURRENT hash."""
    out = []
    accepted = {(p, h) for p, h, _ in b["accepted"]}
    for path, judged in b["reviewed"]:
        now = current(path)
        if now is None:
            out.append(f"{path}: the artifact this verdict judged no longer exists")
        elif now != judged and (path, now) not in accepted:
            out.append(f"{path}: changed since the verdict was written")
    return out


def coverage(b):
    """MISSING: given for review, never declared read. OTHER VERSION: declared read, but with a
    hash that is not the one staged — the checker judged a different text than it was given."""
    out = []
    read = {}
    for path, h in b["read"]:
        read.setdefault(path, set()).add(h)
    for path, judged in b["reviewed"]:
        if path not in read:
            out.append(f"{path}: given for review and never declared read")
        elif judged not in read[path]:
            out.append(f"{path}: read in a different version than the one staged for review")
    return out


def diet_violations(b, allowed, self_path=""):
    """→ (fails, declared). Every path in the manifest AND the read list is checked against the
    role's diet. A forbidden STAGED artifact is a dispatch defect (rule 92 at the dispatch step)
    and cannot be excused by the checker; a forbidden READ is excused only if declared."""
    fails, declared = [], []
    outside = {p: r for p, r in b["outside"]}
    for path, _ in b["reviewed"]:
        ok, why = allowed(b["role"], path)
        if not ok:
            fails.append(f"{path}: STAGED for a {b['role']} but outside its diet ({why})")
    seen = set()
    for path, _ in b["read"]:
        if path in seen or path == self_path:
            continue
        seen.add(path)
        ok, why = allowed(b["role"], path)
        if ok:
            continue
        if path in outside:
            declared.append(f"{path}: read outside the diet, declared — {outside[path]}")
        else:
            fails.append(f"{path}: read outside the {b['role']} diet and NOT declared ({why})")
    return fails, declared


def audit(text, current, allowed, self_path=""):
    """→ (fails, notes) for one verdict file; (None, None) when it carries no binding."""
    b = parse(text)
    if b is None:
        return None, None
    if b["superseded_by"]:
        return [], [f"superseded by {b['superseded_by']} — not checked"]
    fails = list(b["errors"])
    if not b["role"]:
        fails.append("no role: the diet cannot be checked without one")
    if not b["reviewed"]:
        fails.append("no reviewed artifact: a binding that binds nothing")
    fails += stale(b, current)
    fails += coverage(b)
    notes = []
    if b["role"]:
        f, notes = diet_violations(b, allowed, self_path)
        fails += f
    return fails, notes


def with_lines(text, new_lines):
    """Insert lines just before the binding block's closing -->."""
    first, last = find_block(text) or (None, None)
    if last is None:
        raise ValueError("no closed binding block to extend")
    lines = text.splitlines()
    tail = "\n" if text.endswith("\n") else ""
    return "\n".join(lines[:last] + list(new_lines) + lines[last:]) + tail


def stub(role, reviewed):
    """The verdict file as the dispatcher stages it, before the checker writes a word."""
    return "\n".join(["<!-- DIET-CLASS: VERDICT -->", f"{OPEN} v1", f"role: {role}"]
                     + [f"reviewed: {p} sha256:{h}" for p, h in reviewed]
                     + [CLOSE, "", "# VERDICT", "",
                        "*(staged by the dispatcher; the checker writes the verdict below)*", ""])


# ---- the tree ----------------------------------------------------------------------------------

def rel(path):
    p = Path(path).resolve()
    try:
        return p.relative_to(ROOT).as_posix()
    except ValueError:
        raise SystemExit(f"[binding] {path} is outside this tree ({ROOT})")


def current_hash(path):
    p = ROOT / path
    try:
        return norm_sha(p.read_bytes()) if p.is_file() else None
    except OSError:
        return None


def diet_allowed(role, path):
    """The tree's own diet table decides — rag/diet.py, never a copy of it here."""
    sys.path.insert(0, str(ROOT / "rag"))
    import diet
    try:
        cls, _ = diet.classify(ROOT / path)
        return diet.check(role, cls)
    except SystemExit:
        return False, f"unknown role {role!r} in rag/diet.py"


def tree_report(root=None):
    """→ (fails, notes, n_bound, unbound) over every markdown file in the tree."""
    root = Path(root or ROOT)
    fails, notes, n_bound, unbound = [], [], 0, []
    for p in sorted(root.rglob("*.md")):
        if SKIP_DIRS & set(p.relative_to(root).parts):
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        r = p.relative_to(root).as_posix()
        f, n = audit(text, current_hash, diet_allowed, self_path=r)
        if f is None:
            if "VERDICT" in p.name.upper():
                unbound.append(r)
            continue
        n_bound += 1
        fails += [f"{r}: {x}" for x in f]
        notes += [f"{r}: {x}" for x in n]
    return fails, notes, n_bound, unbound


# ---- the commands ------------------------------------------------------------------------------

def cmd_stage(a):
    v = Path(a.verdict)
    if v.exists() and parse(v.read_text(encoding="utf-8", errors="replace")) is not None:
        raise SystemExit(f"[binding] {v} is already staged — a manifest is never rewritten; "
                         f"supersede the verdict instead")
    reviewed = []
    for f in a.artifacts:
        r = rel(f)
        h = current_hash(r)
        if h is None:
            raise SystemExit(f"[binding] {r} does not exist — nothing to stage")
        ok, why = diet_allowed(a.role, r)
        if not ok:
            raise SystemExit(f"[binding] {r} is outside the {a.role} diet ({why}) — a checker is "
                             f"never STAGED a forbidden artifact")
        reviewed.append((r, h))
    v.parent.mkdir(parents=True, exist_ok=True)
    v.write_text(stub(a.role, reviewed), encoding="utf-8")
    print(f"[binding] staged {v} for a {a.role}: {len(reviewed)} artifact(s) bound")
    return 0


def _load(verdict):
    v = Path(verdict)
    text = v.read_text(encoding="utf-8", errors="replace") if v.is_file() else ""
    b = parse(text)
    if b is None or b["errors"]:
        raise SystemExit(f"[binding] {v} carries no usable binding — stage it first")
    return v, text, b


def cmd_read(a):
    v, text, b = _load(a.verdict)
    lines = []
    for f in a.files:
        r = rel(f)
        h = current_hash(r)
        if h is None:
            raise SystemExit(f"[binding] {r} does not exist")
        ok, why = diet_allowed(b["role"], r)
        if not ok and not a.outside_diet:
            raise SystemExit(f"[binding] {r} is outside the {b['role']} diet ({why}).\n"
                             f"           If you opened it, DECLARE it: add --outside-diet "
                             f"\"why\". Declared is recoverable; hidden is not (rule 205).")
        lines.append(f"read: {r} sha256:{h}")
        if not ok:
            lines.append(f"outside-diet: {r} — {a.outside_diet}")
    v.write_text(with_lines(text, lines), encoding="utf-8")
    print(f"[binding] {v}: {len(a.files)} read(s) declared")
    return 0


def cmd_accept(a):
    if not a.reason.strip():
        raise SystemExit("[binding] a change is accepted only with a reason")
    v, text, b = _load(a.verdict)
    r = rel(a.artifact)
    if r not in {p for p, _ in b["reviewed"]}:
        raise SystemExit(f"[binding] {r} is not an artifact this verdict reviewed")
    h = current_hash(r)
    v.write_text(with_lines(text, [f"accepted-change: {r} sha256:{h} — {a.reason.strip()}"]),
                 encoding="utf-8")
    print(f"[binding] {v}: the change to {r} is accepted, with its reason on the record")
    return 0


def cmd_supersede(a):
    v, text, _ = _load(a.verdict)
    v.write_text(with_lines(text, [f"superseded-by: {rel(a.by)}"]), encoding="utf-8")
    print(f"[binding] {v} is superseded by {a.by}")
    return 0


def cmd_check(_a):
    fails, notes, n_bound, unbound = tree_report()
    for n in notes:
        print(f"  [note] {n}")
    if unbound:
        print(f"  [note] {len(unbound)} verdict file(s) carry no binding and are not checked")
    for f in fails:
        print(f"  [FAIL] {f}")
    print(f"  {n_bound} bound verdict(s), {len(fails)} failure(s)")
    return 1 if fails else 0


# ---- the demonstrations -------------------------------------------------------------------------

def self_test():
    cases, blind = [], []

    def demo(name, got, want):
        ok = bool(got) == want
        cases.append(ok)
        if "BLIND SPOT" in name:
            blind.append(ok)
        print(f"  [{'OK ' if ok else 'FAIL'}] {name} "
              f"({'fired' if got else 'did not fire'}; expected {'fire' if want else 'no fire'})")

    print("  VERDICT-BINDING SELF-TEST — planted defects for the binding, the coverage and the diet")
    print("  " + "-" * 68)

    H1, H2, H3 = norm_sha(b"the claim, v1\n"), norm_sha(b"the claim, v2\n"), norm_sha(b"ledger\n")
    D, L, F, S = ("r/DERIVATION.md", "ledgers/NEG.md", "prompts/FORMATION_CORE.md",
                  "r/VERDICT_META.md")
    DENY = {"reviewer": {F}, "meta-observer": {F, D}}

    def allowed(role, path):
        if role not in DENY:
            return False, f"unknown role {role!r}"
        return (path not in DENY[role]), "denied by the planted table"

    def binding(role="reviewer", reviewed=((D, H1),), read=((D, H1),), extra=()):
        return "\n".join(["# verdict", f"{OPEN} v1", f"role: {role}"]
                         + [f"reviewed: {p} sha256:{h}" for p, h in reviewed]
                         + [f"read: {p} sha256:{h}" for p, h in read]
                         + list(extra) + [CLOSE, "CLEAR"])

    def run(text, now=None):
        # `now or {...}` read an EMPTY tree (every file deleted) as "use the defaults", and the
        # deletion demo went red on a correct instrument — the yardstick failed, not the tool.
        now = {D: H1, L: H3, F: H3} if now is None else now
        return audit(text, lambda p: now.get(p), allowed, self_path=S)

    GOOD = binding()
    demo("binding: CONTROL — a well-formed verdict on unchanged bytes, fully read", run(GOOD)[0],
         False)
    demo("binding: a verdict whose artifact was EDITED after review (rule 94, verdict side)",
         run(GOOD, {D: H2})[0], True)
    demo("binding: a verdict whose artifact was deleted", run(GOOD, {})[0], True)
    ACC = binding(extra=[f"accepted-change: {D} sha256:{H2} — a typo in a heading"])
    demo("binding: CONTROL — the edit accepted WITH a reason, on the current bytes",
         run(ACC, {D: H2})[0], False)
    demo("binding: an accepted change with NO reason is refused",
         run(binding(extra=[f"accepted-change: {D} sha256:{H2}"]), {D: H2})[0], True)
    demo("binding: an accepted change on bytes that moved AGAIN",
         run(ACC, {D: norm_sha(b"v3\n")})[0], True)
    demo("binding: CONTROL — a superseded verdict is not held to its old bytes",
         run(binding(extra=["superseded-by: r/VERDICT_2.md"]), {D: H2})[0], False)
    demo("binding: CONTROL — CRLF and LF endings hash the same (core.autocrlf=input)",
         norm_sha(b"a\r\nb\r\n") != norm_sha(b"a\nb\n"), False)
    demo("binding: CONTROL — the format SHOWN inside a code fence is not a binding (documentation)",
         parse("```\n" + GOOD + "\n```\n") is not None, False)
    demo("binding: a half-written block is a defect, not an absence",
         run("# v\n" + OPEN + " v1\nrole: reviewer\n")[0], True)
    demo("binding: a line the format does not know is reported",
         run(binding(extra=["verdict: CLEAR, trust me"]))[0], True)

    demo("coverage: an artifact given for review and never declared read",
         run(binding(read=()))[0], True)
    demo("coverage: the checker read a DIFFERENT version than the one staged",
         run(binding(read=((D, H2),)))[0], True)
    demo("coverage: CONTROL — an extra in-diet file read (a ledger) is not a finding",
         run(binding(read=((D, H1), (L, H3))))[0], False)

    META = dict(role="meta-observer", reviewed=((L, H3),), read=((L, H3), (D, H1)))
    demo("diet: a meta-observer that read the derivation and did not say so (rule 205)",
         run(binding(**META))[0], True)
    fails, notes = run(binding(**META, extra=[f"outside-diet: {D} — step 3, after the referent "
                                              "sentence was written"]))
    demo("diet: CONTROL — the same read DECLARED passes, and is reported as a note",
         fails or not notes, False)
    # The read is DECLARED here on purpose. The first version of this demo also read the file
    # undeclared, so the read check fired and masked the staging check — the sabotage audit
    # deleted the staging check and this line stayed green (2026-09-28).
    demo("diet: a reviewer STAGED the formation prefix — rule 92 at the dispatch step",
         run(binding(reviewed=((F, H3),), read=((F, H3),),
                     extra=[f"outside-diet: {F} — it was in the packet"]))[0], True)
    demo("diet: a role the diet table does not know", run(binding(role="oracle"))[0], True)
    # Both found missing by the same audit: two refusals with no demonstration at all.
    demo("binding: a binding with no role (the diet cannot be checked)",
         run(binding(role=""))[0], True)
    demo("binding: a binding that binds nothing", run(binding(reviewed=(), read=()))[0], True)

    t = with_lines(GOOD, ["read: x sha256:" + H3])
    demo("editing: CONTROL — a declared read lands inside the block, before its close",
         parse(t) is None or ("x", H3) not in parse(t)["read"], False)

    demo("binding: BLIND SPOT (pinned) — a file LISTED as read but never opened passes",
         run(binding(read=((D, H1), (L, H3))))[0], False)
    demo("binding: BLIND SPOT (pinned) — a forbidden file OPENED and not listed passes",
         run(binding(role="meta-observer", reviewed=((L, H3),), read=((L, H3),)))[0], False)
    demo("binding: BLIND SPOT (pinned) — a meaning change accepted as a 'typo' passes",
         run(binding(extra=[f"accepted-change: {D} sha256:{H2} — typo"]), {D: H2})[0], False)

    bad = cases.count(False)
    print("  " + "-" * 70)
    if bad:
        print(f"  VERDICT-BINDING SELF-TEST: {bad} of {len(cases)} demonstrations did NOT behave "
              f"as specified — a verdict could read as current when it is not.")
        return 1
    print(f"  VERDICT-BINDING SELF-TEST: {len(cases)}/{len(cases)} demonstrations behaved as "
          f"specified — {len(blind)} of them pin a blind spot (the read list is an assertion; the "
          f"hash binds bytes, not meaning).")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Bind a verdict to what it judged and what it read.")
    ap.add_argument("--self-test", action="store_true", help="the demonstrations")
    sub = ap.add_subparsers(dest="cmd")
    s = sub.add_parser("stage", help="the dispatcher: stage a verdict file with its artifacts")
    s.add_argument("verdict")
    s.add_argument("--role", required=True)
    s.add_argument("artifacts", nargs="+")
    r = sub.add_parser("read", help="the checker: declare what it read")
    r.add_argument("verdict")
    r.add_argument("files", nargs="+")
    r.add_argument("--outside-diet", default="", metavar="REASON",
                   help="declare a read the role's diet does not allow, and why")
    c = sub.add_parser("accept", help="accept a change to a reviewed artifact, with a reason")
    c.add_argument("verdict")
    c.add_argument("artifact")
    c.add_argument("--reason", required=True)
    u = sub.add_parser("supersede", help="mark a verdict superseded by a newer one")
    u.add_argument("verdict")
    u.add_argument("--by", required=True)
    sub.add_parser("check", help="check every bound verdict in the tree")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    handlers = {"stage": cmd_stage, "read": cmd_read, "accept": cmd_accept,
                "supersede": cmd_supersede, "check": cmd_check}
    if a.cmd not in handlers:
        ap.print_help()
        return 2
    return handlers[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
