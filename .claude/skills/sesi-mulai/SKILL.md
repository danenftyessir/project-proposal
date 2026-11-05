---
name: sesi-mulai
description: Inisialisasi sesi orkestrasi Proposal TA Capstone IF4091 — periksa memory, cocokkan dengan artefak, laporkan readiness sebelum kerja substantif.
disable-model-invocation: true
---

# /sesi-mulai

Jalankan sebagai A01 (atau sesi utama pada mode fallback). Tidak ada kerja substantif sebelum langkah 5 selesai.

1. Jalankan `python scripts/check_memory.py` dan catat readiness (`READY` · `READY_WITH_WARNINGS` · `NOT_READY`) beserta kode temuannya.
2. Baca `memory/PROJECT_STATE.md`, daftar ID dan status di `memory/DECISION_LOG.md`, butir non-`DONE` di `memory/TASK_TRACKER.md`, butir terbuka di `memory/OPEN_QUESTIONS.md`, dan `memory/CONTEXT_TRANSFER.md`.
3. Jalankan `git status --porcelain` dan `git log --oneline -5` untuk melihat kondisi aktual.
4. Bila readiness bukan `READY`, panggil `a13-memory-manager` dengan `type: memory_op`, operasi `init_reconcile`, dan daftar kode temuan. A13 menyusun usulan rekonsiliasi; tidak ada yang ditimpa tanpa persetujuan pengguna.
5. Laporkan kepada pengguna dalam ≤ 10 baris:
   - Readiness dan temuan utama.
   - Tugas yang sedang berjalan.
   - Isu yang menunggu pengguna.
   - Satu pertanyaan terpenting bila ada.
6. Bila `memory/CONTEXT_TRANSFER.md` bertentangan dengan artefak atau `DECISION_LOG`, yang berlaku adalah artefak, lalu `DECISION_LOG`. Sebutkan konfliknya; jangan menyelesaikannya sendiri.
