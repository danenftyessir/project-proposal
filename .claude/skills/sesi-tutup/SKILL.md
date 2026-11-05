---
name: sesi-tutup
description: Penutupan sesi orkestrasi Proposal TA Capstone IF4091 — validasi artefak, perbarui memory lewat A13, periksa Git, ajukan gate G3 sebelum commit/push.
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
3. A13 memperbarui `TASK_TRACKER` (termasuk Run Log), `OPEN_QUESTIONS`, `EVIDENCE_REGISTRY`, `FINDINGS_LOG`, `PROJECT_STATE` (Artifact Map, revisi, *Efisiensi* dari `--metrics`), dan `memory/CONTEXT_TRANSFER.md`. Lalu ia menjalankan `python scripts/check_memory.py --strict --allow-uncommitted` dan `python scripts/check_staged.py --paths <berkas yang akan di-stage>`.
4. Ajukan **G3** kepada pengguna:
   - Daftar path yang akan di-stage, satu per satu.
   - Pesan commit.
   - Branch target.
   - Hasil kedua pemeriksaan di langkah 3.

   Tanpa jawaban persetujuan yang eksplisit, tidak ada commit.
5. Setelah disetujui, A13 menjalankan `git add -- <path>` per path, `python scripts/check_staged.py`, lalu `git commit`. Push hanya bila pengguna juga menyetujui push: `git fetch` dulu dan berhenti bila *diverged*.
6. Verifikasi push (`git status -sb` tidak *ahead*, dan `git ls-remote origin <branch>` = `git rev-parse HEAD`) sebelum melaporkan berhasil. Bila belum di-push, laporkan apa adanya.
