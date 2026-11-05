"""Memory integrity and stale-memory checks S1–S12 (docs/ORCHESTRATION_ARCHITECTURE.md §12.5, §12.6, §8.3).

Usage:
  python scripts/check_memory.py [--strict] [--allow-uncommitted]   full report (exit 1 when NOT_READY)
  python scripts/check_memory.py --hook                             SessionStart hook JSON (factual summary)
  python scripts/check_memory.py --metrics                          efficiency summary from the Run Log
  python scripts/check_memory.py --init-rsia-manifest               write .scratch/rsia/manifest.sha256 once
Options: --root DIR (artefacts to check; default repo root), --memory-dir DIR (default <root>/memory).

Read-only except --init-rsia-manifest, which writes only .scratch/rsia/manifest.sha256 and refuses to
overwrite an existing manifest. Reports never print RSIA file names or identifier matches.
"""
import json, re, subprocess, sys
from datetime import date
from pathlib import Path
import _common
from _common import content_hash, scan_identifiers, sha256_file

FILES = ["PROJECT_STATE", "DECISION_LOG", "OPEN_QUESTIONS", "TASK_TRACKER", "EVIDENCE_REGISTRY",
         "FINDINGS_LOG", "CONTEXT_TRANSFER"]
FM_KEYS = {"file", "revision", "status", "updated", "updated_by", "based_on_commit"}
FM_STATUS = {"CURRENT", "PENDING_VERIFICATION", "SUPERSEDED"}
DECIDED = {"APPROVED", "REJECTED", "WAIVED"}
EVIDENCE_KEYS = {"user_answer", "answered_at", "session_ref", "scope"}
OPEN_Q_CLOSED = {"DIPUTUSKAN", "DITUTUP DENGAN ALASAN"}
LEVEL_ORDER = {"NOT_READY": 3, "WARN": 2, "INFO": 1}


def arg_value(argv, name, default=None):
    return argv[argv.index(name) + 1] if name in argv and argv.index(name) + 1 < len(argv) else default


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    try:
        import yaml
        return yaml.safe_load(m.group(1)) or {}
    except ImportError:
        return dict(re.findall(r"^(\w+):\s*(.*?)\s*$", m.group(1), re.M))


def yaml_blocks(text):
    import yaml
    out = []
    for b in re.findall(r"```yaml\n(.*?)\n```", text, re.S):
        try:
            d = yaml.safe_load(b)
            if isinstance(d, dict):
                out.append(d)
        except yaml.YAMLError:
            out.append({"_parse_error": True})
    return out


def table(text, heading):
    """Rows of the first Markdown table under '## heading' as dicts keyed by header cells."""
    m = re.search(rf"^##\s+{re.escape(heading)}\s*$(.*?)(?=^##\s|\Z)", text, re.S | re.M)
    if not m:
        return []
    lines = [ln.strip() for ln in m.group(1).splitlines() if ln.strip().startswith("|")]
    if len(lines) < 2:
        return []
    cells = lambda ln: [c.strip() for c in ln.strip("|").split("|")]
    head = cells(lines[0])
    return [dict(zip(head, cells(ln))) for ln in lines[2:]]


def strip_code(s):
    return s.strip().strip("`").strip()


class Report:
    def __init__(self):
        self.items = []

    def add(self, code, level, msg):
        self.items.append((code, level, msg))

    @property
    def readiness(self):
        worst = max((LEVEL_ORDER[l] for _, l, _ in self.items), default=0)
        return "NOT_READY" if worst == 3 else "READY_WITH_WARNINGS" if worst == 2 else "READY"


def git(root, *args):
    r = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def check(root, mem, allow_uncommitted):
    rep, docs = Report(), {}
    if not mem.is_dir():
        rep.add("S9", "NOT_READY", f"direktori memory tidak ditemukan: {mem}")
        return rep, docs
    for name in FILES:
        p = mem / f"{name}.md"
        if not p.is_file():
            rep.add("S9", "NOT_READY", f"{name}.md tidak ada")
            continue
        text = p.read_text(encoding="utf8")
        fm = front_matter(text)
        docs[name] = (text, fm or {})
        if fm is None:
            rep.add("S9", "NOT_READY", f"{name}.md tanpa front matter")
            continue
        missing = FM_KEYS - set(fm)
        if missing:
            rep.add("S9", "NOT_READY", f"{name}.md: front matter tanpa {', '.join(sorted(missing))}")
        if fm.get("status") not in FM_STATUS:
            rep.add("S9", "NOT_READY", f"{name}.md: status '{fm.get('status')}' tidak valid")
        hits = scan_identifiers(text)                                                      # S11
        for pat, n in hits.items():
            rep.add("S11", "NOT_READY", f"{name}.md: {n} kecocokan pola pengenal '{pat}'")
    if "PROJECT_STATE" not in docs:
        return rep, docs
    ps_text, ps_fm = docs["PROJECT_STATE"]

    changed = missing_files = 0                                                            # S1
    for row in table(ps_text, "Artifact Map"):
        path, h = strip_code(row.get("Path", "")), strip_code(row.get("sha256", ""))
        if not path or h in {"", "—", "-"}:
            continue
        f = root / path
        if not f.is_file():
            missing_files += 1
            rep.add("S1", "WARN", f"artefak tercatat tidak ditemukan: {path}")
        elif content_hash(f, len(h)) != h:
            changed += 1
            rep.add("S1", "WARN", f"artefak berubah sejak dicatat: {path}")

    if "CONTEXT_TRANSFER" in docs:                                                         # S2
        ct_fm = docs["CONTEXT_TRANSFER"][1]
        try:
            if int(ct_fm.get("revision", 0)) < int(ps_fm.get("revision", 0)) or \
                    str(ct_fm.get("based_on_commit")) != str(ps_fm.get("based_on_commit")):
                rep.add("S2", "WARN", "memory/CONTEXT_TRANSFER.md tertinggal dari PROJECT_STATE")
        except (TypeError, ValueError):
            rep.add("S2", "WARN", "revisi CONTEXT_TRANSFER/PROJECT_STATE tidak dapat dibandingkan")

    if "TASK_TRACKER" in docs:                                                             # S3
        for row in table(docs["TASK_TRACKER"][0], "Tasks"):
            if row.get("Status", "").upper() != "DONE":
                continue
            for out in re.split(r"[,;]", row.get("Keluaran", "")):
                out = strip_code(out)
                if out and out not in {"—", "-"} and "/" in out and not (root / out).exists():
                    rep.add("S3", "NOT_READY", f"{row.get('ID')} DONE tetapi keluaran tidak ada: {out}")

    decisions = {}
    if "DECISION_LOG" in docs:                                                             # S10
        for d in yaml_blocks(docs["DECISION_LOG"][0]):
            if d.get("_parse_error"):
                rep.add("S10", "NOT_READY", "blok YAML DECISION_LOG tidak dapat diurai")
                continue
            did, status = str(d.get("id")), str(d.get("status", ""))
            decisions[did] = status
            if status.split()[0] in DECIDED:
                ev = d.get("approval_evidence") or {}
                miss = [k for k in EVIDENCE_KEYS if not ev.get(k)]
                if miss:
                    rep.add("S10", "NOT_READY", f"{did} {status} tanpa approval_evidence: {', '.join(miss)}")

    superseded = {k for k, v in decisions.items() if v.startswith("SUPERSEDED")}         # S4
    for name in ("OPEN_QUESTIONS", "TASK_TRACKER", "PROJECT_STATE", "EVIDENCE_REGISTRY", "FINDINGS_LOG"):
        if name not in docs:
            continue
        for ref in sorted(set(re.findall(r"\b(D-\d{2}|P2-0\d)\b", docs[name][0]))):
            if ref not in decisions:
                rep.add("S4", "NOT_READY", f"{name}.md merujuk {ref} yang tidak ada di DECISION_LOG")
    if "OPEN_QUESTIONS" in docs:
        today = date.today()
        for q in yaml_blocks(docs["OPEN_QUESTIONS"][0]):
            status = str(q.get("status", ""))
            is_open = not any(status.startswith(c) for c in OPEN_Q_CLOSED)
            refs = set(map(str, q.get("refs") or []))
            if is_open and refs & superseded:
                rep.add("S4", "NOT_READY", f"{q.get('id')} masih terbuka tetapi merujuk keputusan SUPERSEDED")
            upd = q.get("updated")
            if is_open and isinstance(upd, date) and (today - upd).days > 7:                 # S6
                rep.add("S6", "INFO", f"{q.get('id')} tidak diperbarui lebih dari 7 hari")

    if "EVIDENCE_REGISTRY" in docs:                                                        # S5
        for row in table(docs["EVIDENCE_REGISTRY"][0], "Klaim"):
            src = strip_code(row.get("Sumber (path)", ""))
            if src and "/" in src and not (root / src).exists():
                rep.add("S5", "WARN", f"{row.get('ID')}: sumber tidak ditemukan: {src}")

    for row in table(ps_text, "Team Docs Manifest"):                                       # S8
        path, h = strip_code(row.get("Path", "")), strip_code(row.get("sha256", ""))
        if not path or h in {"", "—", "-"}:
            continue
        f = root / path
        if not f.is_file() or content_hash(f, len(h)) != h:
            rep.add("S8", "WARN", f"dokumen tim berubah atau hilang dibanding manifest: {path}")

    if not allow_uncommitted:                                                              # S7
        dirty = git(root, "status", "--porcelain", "--", str(mem))
        if dirty:
            rep.add("S7", "NOT_READY", "ada perubahan memory/** yang belum di-commit")

    manifest = root / ".scratch" / "rsia" / "manifest.sha256"                              # S12
    rsia = root / "RSIA-source"
    if rsia.is_dir():
        if not manifest.is_file():
            rep.add("S12", "INFO", "manifest integritas RSIA belum dibuat (A13: --init-rsia-manifest)")
        else:
            expected = {}
            for ln in manifest.read_text(encoding="utf8").splitlines():
                h, _, p = ln.partition("  ")
                if p:
                    expected[p] = h
            bad = sum(1 for p, h in expected.items()
                      if not (rsia / p).is_file() or sha256_file(rsia / p) != h)
            extra = sum(1 for f in rsia.rglob("*") if f.is_file()
                        and f.relative_to(rsia).as_posix() not in expected)
            if bad or extra:
                rep.add("S12", "NOT_READY",
                        f"berkas asli RSIA tidak sesuai manifest: {bad} berubah/hilang, {extra} baru")
    return rep, docs


def metrics(docs):
    rows = table(docs.get("TASK_TRACKER", ("", {}))[0], "Run Log")
    if not rows:
        return "Run Log kosong."
    from collections import Counter
    per_agent = Counter(r.get("Agent", "?") for r in rows)
    tasks = {}
    for r in rows:
        try:
            c = int(r.get("Cycle", "0"))
        except ValueError:
            c = 0
        t = r.get("Task", "?")
        tasks[t] = max(tasks.get(t, 0), c)
    qa0 = [r for r in rows if r.get("Cycle") == "0" and r.get("QA") not in {"", "NOT_APPLICABLE", "—"}]
    fail0 = sum(1 for r in qa0 if r.get("QA") == "FAIL")
    skills = Counter(s.strip() for r in rows for s in r.get("Skill", "").split(",") if s.strip() not in {"", "—"})
    lines = [f"Pemanggilan: {len(rows)} dari {len(tasks)} tugas",
             "Per agent: " + ", ".join(f"{a}={n}" for a, n in sorted(per_agent.items())),
             f"Rata-rata siklus maksimum per tugas: {sum(tasks.values()) / len(tasks):.2f}",
             f"Tugas mencapai batas 2 siklus: {sum(1 for v in tasks.values() if v >= 2)}",
             f"QA FAIL pada siklus 0: {fail0}/{len(qa0)}" if qa0 else "QA siklus 0: belum ada data",
             "Skill: " + (", ".join(f"{s}={n}" for s, n in skills.items()) or "tidak ada")]
    return "\n".join(lines)


def init_manifest(root):
    rsia, manifest = root / "RSIA-source", root / ".scratch" / "rsia" / "manifest.sha256"
    if not rsia.is_dir():
        print("init-rsia-manifest: RSIA-source/ tidak ada di root ini; tidak ada yang dibuat")
        return 0
    if manifest.exists():
        print("init-rsia-manifest: manifest sudah ada; tidak ditimpa (hapus manual bila memang perlu dibuat ulang)")
        return 1
    files = sorted(f for f in rsia.rglob("*") if f.is_file())
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text("".join(f"{sha256_file(f)}  {f.relative_to(rsia).as_posix()}\n" for f in files),
                        encoding="utf8")
    print(f"init-rsia-manifest: {len(files)} berkas dicatat di .scratch/rsia/manifest.sha256")
    return 0


def main(argv):
    root = Path(arg_value(argv, "--root", str(_common.ROOT))).resolve()
    mem = Path(arg_value(argv, "--memory-dir", str(root / "memory"))).resolve()
    if "--init-rsia-manifest" in argv:
        return init_manifest(root)
    rep, docs = check(root, mem, "--allow-uncommitted" in argv)
    if "--metrics" in argv:
        print(metrics(docs))
        return 0
    if "--hook" in argv:
        counts = {}
        for code, level, _ in rep.items:
            counts.setdefault(level, set()).add(code)
        detail = "; ".join(f"{lvl}: {', '.join(sorted(c))}" for lvl, c in sorted(counts.items())) or "tidak ada temuan"
        msg = (f"Pemeriksaan memory proyek (scripts/check_memory.py): {rep.readiness}. {detail}. "
               "Rincian: python scripts/check_memory.py.")
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": msg}}))
        return 0
    print(f"Readiness: {rep.readiness}")
    for code, level, msg in sorted(rep.items, key=lambda x: (-LEVEL_ORDER[x[1]], x[0])):
        print(f"  [{level}] {code} {msg}")
    return 1 if ("--strict" in argv and rep.readiness != "READY") or rep.readiness == "NOT_READY" else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
