---
file: FINDINGS_LOG
revision: 4
status: CURRENT
updated: 2026-11-05
updated_by: a13-memory-manager
based_on_commit: 7d59b85
---

# Findings Log

Temuan QA lintas sesi (format §A-5.3), hanya yang non-`INFO`. `RESOLVED` hanya oleh auditor penemu setelah pemeriksaan ulang; `REJECTED` dan `WAIVED` hanya oleh pengguna, dengan rujukan bukti persetujuan.

## Temuan

| ID | Agent | Lokasi | Deskripsi | Severity | Status | Bukti persetujuan (untuk REJECTED/WAIVED) |
|---|---|---|---|---|---|---|
| F-A13-0001 | a13 | `memory/PROJECT_STATE.md` Artifact Map; `scripts/check_memory.py` | Artifact Map dihitung dari checkout utama, sedangkan check_memory dijalankan di worktree; rekonsiliasi dilakukan di checkout utama setelah merge. Bukti A01: `git diff --stat 7d59b85 -- CLAUDE.md RULES.md source/INDEKS.md tools/verify_claims.py` kosong di worktree, sehingga selisih hash S1 "berubah" berasal dari working copy checkout utama yang berbeda dari 7d59b85. Pada pemeriksaan ulang peringatan S1 RULES.md tidak muncul lagi (12 → 11 WARN); penyebab belum diketahui. Tambahan TSK-016 (Glob worktree 2026-11-05): lima berkas S1 (Penyelarasan Pemahaman Capstone.md, bab2/Bab_II_Revisi_Notulensi.md, bab2/Kebutuhan_Literatur_Revisi_Bab_II.md, bab3/Bahan_Pindahan_dari_Bab_II.md, tools/build_modular.py) dan tiga dokumen S8 (Proposal_Bab_I_Muhammad_Raihaan_Perdana - Copy.docx, Draft Proposal TA BAB 2 M. Abizzar Gamadrian.docx, Draft Bab 1 (1).docx) tidak ada di worktree. Hash sha256 worktree untuk CLAUDE.md, source/INDEKS.md, tools/verify_claims.py belum dihitung (guard menolak; menunggu TSK-014) | MEDIUM | OPEN | — |
| F-A13-0002 | a13 | `memory/TASK_TRACKER.md` baris TSK-002 dan TSK-003 (kolom Catatan) | Perubahan memory di luar daftar yang dilaporkan. Fakta: A01 membaca Catatan TSK-002 = "v0.5" dan TSK-003 = "v0.3" di awal sesi; saat TSK-015 dimulai isinya sudah "Kanonik v0.6 di worktree; salinan beku v0.5 untracked di checkout utama" (TSK-003: v0.4 dan v0.3). Pada TSK-015 saya tidak mengubah kedua baris itu (hanya TSK-005, baris baru, Run Log, revisi), tetapi berkas sudah rev 2 oleh TSK-013 (rev 1 oleh sesi setup). Tugas yang mengubahnya tidak dapat dipastikan: berkas untracked sehingga tidak ada diff; kandidatnya TSK-012, TSK-013, atau sesi setup. Laporan TSK-013 dan TSK-015 tidak menyebut perubahan ini | LOW | OPEN | — |
| F-A12-0001 | a12 | prompt `.claude/agents/a12-qa-integrity.md` | Placeholder `<SKILL_DIR:…>` tidak terisi di prompt a12 | MEDIUM | OPEN (ditangani D-20/TSK-014) | — |
| F-A12-0002 | a12 | guard Bash a12 | `find` ditolak guard untuk a12 | LOW | OPEN (ditangani D-20/TSK-014) | — |
| F-A12-0003 | a12 | guard Bash a12 | `mkdir` ditolak guard untuk a12 | LOW | OPEN (ditangani D-20/TSK-014) | — |
| F-A13-0003 | a13 | `docs/TESTING_CHECKLIST.md:39,155`; `docs/ORCHESTRATION_ARCHITECTURE.md:1176`; `memory/CONTEXT_TRANSFER.md` rev 3 | Angka hasil selftest tidak konsisten antardokumen. Fakta: TESTING_CHECKLIST baris 39 dan 155 menyatakan 114/114; ORCHESTRATION_ARCHITECTURE baris 1176 menyatakan 102 uji; CONTEXT_TRANSFER rev 3 menyatakan 102/102. Selftest tidak dijalankan oleh a13; angka final belum diketahui. requires_decision: false | MEDIUM | OPEN | — |
