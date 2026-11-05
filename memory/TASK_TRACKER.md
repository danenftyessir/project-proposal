---
file: TASK_TRACKER
revision: 4
status: CURRENT
updated: 2026-11-05
updated_by: a13-memory-manager
based_on_commit: 7d59b85
---

# Task Tracker

Tugas memakai ID `TSK-xxx` (berbeda dari ID uji teknis `T-xx`). Status: `TODO` · `DOING` · `BLOCKED` · `DONE` · `DROPPED`. Kolom *Keluaran* berisi path yang diperiksa S3 untuk tugas `DONE`.

## Tasks

| ID | Tugas | Status | Agent | Siklus | Keluaran | Gate | Catatan |
|---|---|---|---|---|---|---|---|
| TSK-001 | Phase 0: audit repository | DONE | (sesi setup) | — | — | — | Laporan di percakapan; ringkasannya di docs/ORCHESTRATION_ARCHITECTURE.md |
| TSK-002 | Phase 1: rancangan arsitektur | DONE | (sesi setup) | — | `docs/ORCHESTRATION_ARCHITECTURE.md` | Tinjauan pengguna | Kanonik v0.6 di worktree; salinan beku v0.5 untracked di checkout utama |
| TSK-003 | Phase 2: spesifikasi 13 agent | DONE | (sesi setup) | — | `docs/AGENT_SPECIFICATIONS.md` | Tinjauan pengguna | Kanonik v0.4 di worktree; salinan beku v0.3 untracked di checkout utama |
| TSK-004 | Phase 3: implementasi di worktree setup/orchestration | DOING | (sesi setup) | — | `.claude/settings.json`, `scripts/guard.py` | G3 (commit) | Belum di-commit |
| TSK-005 | Uji runtime T-01–T-29 yang memerlukan sesi Claude Code baru | DOING | A01, A13 | — | `docs/TESTING_CHECKLIST.md` | — | Sesi 2026-11-05: LULUS T-03, T-07b, T-08, T-09, T-14, T-17 (search tanpa filter project tercampur proyek lain), T-28b, T-29b. SEBAGIAN T-26 (Approval Request menyebut 8 berkas modular/, tetapi tools/build_modular.py tidak ada di worktree sehingga daftar tidak diverifikasi dari skrip). BLOCKED T-19 (cycle 1; menunggu TSK-014). T-15 tidak menguji hook (a04 tidak punya tool tulis; rancang ulang dengan agent ber-Write di luar scope). T-16 tidak sahih (A01 membaca agent-contract/SKILL.md sebelum uji; ulang di sesi baru). Kolom hasil di `docs/TESTING_CHECKLIST.md` (di luar write scope A13) perlu diperbarui oleh sesi setup. Sisanya setelah commit/merge |
| TSK-006 | Rekonsiliasi pertama memory dari checkout utama + migrasi root CONTEXT_TRANSFER (§A-9.6 butir 5) | TODO | A13 | — | — | — | PROJECT_STATE masih PENDING_VERIFICATION |
| TSK-007 | Merge setup/orchestration ke main (§A-15.3) | TODO | A13 | — | — | Gate tersendiri | Menunggu persetujuan pengguna |
| TSK-008 | Pasang core.hooksPath --local (D-12) | TODO | Pengguna/A13 | — | — | Persetujuan | Setelah merge, agar main memiliki scripts/git-hooks |
| TSK-009 | Buat .claude/settings.local.json dengan claudeMdExcludes di checkout utama (D-03) | TODO | Sesi setup | — | — | — | Setelah merge; lalu uji T-02 |
| TSK-010 | Perbaikan ROOT tools/verify_claims.py (D-16) | BLOCKED | — | — | — | Persetujuan | DEFERRED sampai perubahan pengguna di-commit |
| TSK-011 | Pembuatan manifest integritas RSIA (S12) | TODO | A13 | — | — | — | Di checkout utama, sebelum akses RSIA pertama |
| TSK-012 | init_reconcile awal sesi 2026-11-05 | DONE | A13 | 0 | — | — | PARTIAL: dilanjutkan oleh TSK-014 lalu TSK-006. Temuan F-A13-0001. Status DONE hanya untuk eksekusi; rekonsiliasi belum selesai |
| TSK-013 | Pencatatan D-20 | DONE | A13 | 0 | `memory/DECISION_LOG.md`, `memory/TASK_TRACKER.md` | — | Menambah D-20 dan TSK-014 |
| TSK-014 | Implementasi D-20: perluas allowlist Bash a13 (git ls-tree, git hash-object) dan a12 (mkdir/cp ke .scratch/**), perbaiki placeholder <SKILL_DIR:...> a12, tambah kasus selftest | TODO | Sesi setup | — | — | — | Ulang T-19 dan init_reconcile setelahnya. Menangani F-A12-0001, F-A12-0002, F-A12-0003 |
| TSK-015 | session_close sesi 2026-11-05 (memory, pemeriksaan pra-G3 tanpa commit) | DONE | A13 | 0 | `memory/TASK_TRACKER.md`, `memory/FINDINGS_LOG.md`, `memory/CONTEXT_TRANSFER.md`, `memory/PROJECT_STATE.md` | — | G3 belum diajukan; commit setup ditunda pengguna |
| TSK-016 | init_reconcile (siklus 0) + apply_reconcile usulan A1-A5 (siklus 1) di worktree | DONE | A13 | 1 | `memory/PROJECT_STATE.md`, `memory/FINDINGS_LOG.md`, `memory/TASK_TRACKER.md`, `memory/CONTEXT_TRANSFER.md` | Persetujuan pengguna "Terapkan A1–A5" (2026-11-05) | Siklus 0 PARTIAL: hash worktree diblokir guard (menunggu TSK-014). Siklus 1: anotasi Artifact Map, tambahan F-A13-0001, temuan F-A13-0003. Usulan B (menunggu checkout utama/merge, TSK-006/007) dan C tidak diterapkan |

## Run Log

Diisi A13 saat penutupan tugas dari Agent Report dan `.scratch/agent_runs.jsonl` (§A-12.6). Token dan durasi ditulis `n/a` bila tidak terlihat; tidak ditebak.

| Tanggal | Task | Agent | Cycle | Exec | QA | Temuan C/H/M/L | Skill | Durasi | Token |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-05 | TSK-012 | a13 | 0 | PARTIAL | NA | 0/0/1/0 | n/a | 38,9 s | 27081 |
| 2026-11-05 | TSK-005 (T-03) | a07 | 0 | COMPLETE | PASS_WITH_NOTES (uji, bukan audit) | 0/0/0/0 | n/a | 13,4 s | 11474 |
| 2026-11-05 | TSK-005 (T-07b) | a05 | 0 | COMPLETE | NA | 0/0/0/0 | n/a | 13,1 s | 10893 |
| 2026-11-05 | TSK-005 (T-08 b1) | a04 | 0 | COMPLETE | NA | 0/0/0/0 | n/a | 11,4 s | 11501 |
| 2026-11-05 | TSK-005 (T-08 b2) | a04 | 0 | COMPLETE | NA | 0/0/0/0 | n/a | 33,2 s | 12202 |
| 2026-11-05 | TSK-005 (T-15) | a04 | 0 | COMPLETE | NA | 0/0/0/0 | n/a | 9,9 s | 13268 |
| 2026-11-05 | TSK-005 (T-17) | a13 | 0 | COMPLETE | NA | 0/0/0/0 | n/a | 16,4 s | 19538 |
| 2026-11-05 | TSK-005 (T-14 tanpa G3) | a13 | 0 | PARTIAL | NA | 0/0/0/0 | n/a | 18,6 s | 21650 |
| 2026-11-05 | TSK-005 (T-14 G3 uji) | a13 | 1 | COMPLETE | NA | 0/0/0/0 | n/a | 113,6 s | 23366 |
| 2026-11-05 | TSK-005 (T-19) | a12 | 0 | BLOCKED | BLOCKED | 0/0/1/1 | n/a | 23,0 s | 13391 |
| 2026-11-05 | TSK-005 (T-19) | a12 | 1 | BLOCKED | BLOCKED | 0/0/0/1 | n/a | 21,8 s | 15233 |
| 2026-11-05 | TSK-005 (T-28b) | a02 | 0 | COMPLETE | NA | 0/0/0/0 | n/a | 52,0 s | 17434 |
| 2026-11-05 | TSK-005 (T-29b) | a03 | 0 | COMPLETE | NA | 0/0/0/0 | n/a | 38,8 s | 15615 |
| 2026-11-05 | TSK-013 | a13 | 0 | COMPLETE | NA | 0/0/0/0 | n/a | 54,6 s | 26325 |
| 2026-11-05 | TSK-016 (init_reconcile) | a13 | 0 | PARTIAL | NA | 0/0/1/0 | n/a | n/a | n/a |
| 2026-11-05 | TSK-016 (apply_reconcile A1-A5) | a13 | 1 | COMPLETE | NA | 0/0/1/0 | n/a | n/a | n/a |

Catatan: token = subagent_tokens menurut harness, mungkin kumulatif per instance.
