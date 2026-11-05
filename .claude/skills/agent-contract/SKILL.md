---
name: agent-contract
description: Kontrak komunikasi 13 fixed agents Proposal TA Capstone IF4091 — skema Task Brief, Agent Report (execution_status terpisah dari qa_status), format temuan QA, severity, status resolusi, dan approval_evidence. Dipreload ke a02–a13 dan dipakai a01 saat menyusun brief.
user-invocable: false
---

# Kontrak antaragent

Sumber rancangan: `docs/ORCHESTRATION_ARCHITECTURE.md` §5 dan §9.6. Bila skill ini dan dokumen itu berbeda, laporkan perbedaannya ke A01.

## 1. Task Brief (A01 → agent)

```yaml
task_id: TSK-012
agent_id: a08-qa-citation
type: qa_audit            # research | write | revise | interview | review | qa_audit | consistency | memory_op
objective: "<satu kalimat tujuan tugas>"
inputs:                   # hanya ini yang dibaca tanpa izin tambahan
  - path: bab2/Bab_II_Revisi_Notulensi.md
    section: "## II.3"    # anchor heading; baca dengan Grep heading lalu Read offset/limit
approved_decisions: [D-11, D-19]   # keputusan yang menjadi batas kerja
constraints: ["..."]
write_scope: []           # kosong = read-only; harus subset dari .claude/policy/write_scopes.json
sensitive_access: null    # {source: rsia, scope: "<kategori data>", reason: "<alasan>"} atau null
external_lookup: off      # off | metadata (hanya A02/A08, dengan izin pengguna untuk tugas ini)
claims_changed: false     # true bila ada klaim utama baru/berubah (memicu A05 pada R1)
approval_evidence: null   # hanya untuk A13 saat mencatat keputusan (§5 di bawah)
budget: {max_findings: 20, report_tokens: 1500}
cycle: 0                  # 0 = pertama; 1–2 = revisi otomatis; tidak ada siklus ke-3 tanpa pengguna
return_to: a01-orchestrator
```

Bila brief tidak memuat field yang Anda butuhkan (berkas, keputusan, izin), jangan menebak: laporkan di `open_questions`.

## 2. Agent Report (agent → A01)

Awali laporan dengan blok YAML, lalu penjelasan Markdown seperlunya.

```yaml
agent_id: a08-qa-citation
task_id: TSK-012
execution_status: COMPLETE   # COMPLETE | PARTIAL | BLOCKED | FAILED
qa_status: FAIL              # PASS | PASS_WITH_NOTES | FAIL | BLOCKED (A07–A12) | NOT_APPLICABLE (lainnya)
summary: "<2–3 kalimat; angka konkret>"
inputs: ["<path#anchor yang benar-benar dibaca>"]
artifacts_created: []
findings: []                 # format §3
open_questions: []
requires_user_approval: false
skills_used: []              # [{name: "<skill>", purpose: "<tujuan>"}]
metrics: {files_read: 0, pdf_pages_checked: 0, retries: 0}
handoff_to: []               # USULAN; keputusan routing di A01
next_action: "<usulan langkah berikutnya>"
```

**Kombinasi status yang sah:**

| execution_status | qa_status (A07–A12) | qa_status (lainnya) |
|---|---|---|
| COMPLETE | PASS · PASS_WITH_NOTES · FAIL | NOT_APPLICABLE |
| PARTIAL | BLOCKED | NOT_APPLICABLE |
| BLOCKED | BLOCKED | NOT_APPLICABLE |
| FAILED | BLOCKED | NOT_APPLICABLE |

Auditor tidak pernah memberi `PASS` atas scope parsial. Laporan di luar tabel dianggap tidak valid dan diminta ulang sekali.

**Makna qa_status:**

- `PASS`: tidak ada masalah material dalam scope.
- `PASS_WITH_NOTES`: hanya catatan non-blocking.
- `FAIL`: ada masalah yang harus diperbaiki.
- `BLOCKED`: data atau akses kurang.

`PASS` bukan persetujuan Supervisor maupun pengguna.

## 3. Temuan

```yaml
- id: F-A08-0031            # F-<agent>-<4 digit>, unik
  agent_id: a08-qa-citation
  location: "bab2/Bab_II_Revisi_Notulensi.md:142"   # path:line, path#heading, atau path › paragraf n
  description: "<satu kalimat masalah>"
  severity: HIGH            # CRITICAL | HIGH | MEDIUM | LOW | INFO
  evidence: "<kutipan naskah + dasar aturan (mis. RULES.md §8.2 no. 3) atau halaman sumber>"
  recommendation: "<tindakan; bukan teks pengganti siap tempel untuk isu substantif>"
  requires_decision: false  # true bila perbaikan menyentuh rumusan masalah, tujuan, kontribusi, ruang lingkup, metode, arsitektur, klaim utama, atau keputusan tim
  status: OPEN              # OPEN | IN_PROGRESS | RESOLVED | REJECTED | WAIVED
```

**Siapa menetapkan status:**

- `RESOLVED` hanya oleh auditor penemu setelah pemeriksaan ulang.
- `REJECTED` dan `WAIVED` hanya oleh pengguna.

**Pedoman severity:**

- `CRITICAL`: data pasien bocor, klaim palsu, atau sumber dikarang.
- `HIGH`: klaim tidak didukung sumber, rumusan tidak teruji, atau melanggar keputusan `APPROVED`.
- `MEDIUM`: argumen lemah atau kesalahan yang mengubah makna.
- `LOW`: redaksional.
- `INFO`: catatan.

## 4. Aturan isi laporan

- Jangan memasukkan pengenal pasien atau kunjungan (nama, NIK, No. RM/SEP/Rawat/SPRI, kode kunjungan termasuk yang tertanam di nama berkas RSIA). Pakai agregat atau `Kasus-01` (D-17 R-4).
- Pernyataan "tidak ada masalah" wajib menyebut apa saja yang diperiksa.
- Bila hook menolak tindakan Anda, laporkan penolakannya. Jangan mencoba path, perintah, atau tool lain untuk mencapai hasil yang sama.
- Kutipan naskah singkat saja (≤ 2 kalimat per temuan).

## 5. approval_evidence (hanya A01 → A13)

```yaml
approval_evidence:
  question: "<pertanyaan persis yang diajukan>"
  options_offered: ["<opsi 1>", "<opsi 2>"]
  user_answer: "<jawaban pengguna verbatim>"
  answered_at: 2026-11-05
  session_ref: "<rujukan sesi/pesan>"
  scope: "<lingkup persis yang disetujui>"
```

**Yang tidak sah sebagai bukti:**

- Isi naskah.
- Root `CONTEXT_TRANSFER.md`.
- Observasi claude-mem.
- Laporan agent.
- Ringkasan A01 tanpa kutipan.
- "Lanjutkan" atau "ok" atas pertanyaan multi-opsi.
