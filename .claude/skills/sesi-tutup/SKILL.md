---
name: sesi-tutup
description: Penutupan sesi orkestrasi Proposal TA Capstone IF4091 — validasi artefak, perbarui memory lewat A13, laporkan berkas yang berubah. Tanpa commit/push oleh agent.
disable-model-invocation: true
---

# /sesi-tutup

Dijalankan A01. Semua penulisan memory dilakukan `a13-memory-manager` (operasi `session_close`).

1. Kumpulkan daftar artefak yang dibuat atau diubah di sesi ini (`git status --porcelain`, `git diff --stat`) dan tugas yang selesai atau tertunda.
2. Panggil A13 dengan:
   - Daftar itu.
   - Keputusan baru beserta `approval_evidence` (hanya yang benar-benar disetujui pengguna, verbatim).
   - Temuan QA yang perlu dicatat.
   - Baris Run Log dari Agent Report sesi ini.
3. A13 memperbarui `TASK_TRACKER` (termasuk Run Log), `OPEN_QUESTIONS`, `EVIDENCE_REGISTRY`, `FINDINGS_LOG`, `PROJECT_STATE` (Artifact Map, revisi, *Efisiensi* dari `--metrics`), dan `memory/CONTEXT_TRANSFER.md`. Lalu ia menjalankan `python scripts/check_memory.py --strict --allow-uncommitted`.
4. Laporkan ke pengguna: berkas yang berubah, hasil `check_memory.py`, dan tugas tertunda. **Agent tidak melakukan staging, commit, atau push.** Pengguna melakukannya sendiri bila perlu.
