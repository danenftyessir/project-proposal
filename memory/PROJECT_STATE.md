---
file: PROJECT_STATE
revision: 6
status: PENDING_VERIFICATION
updated: 2026-11-06
updated_by: a13-memory-manager
based_on_commit: fee9a61
---

# Project State

Ringkasan kondisi aktual. Bila bertentangan dengan artefak repository, artefak yang berlaku (§A-12.3). Status berkas ini `PENDING_VERIFICATION` sampai A13 menjalankan rekonsiliasi pertama dari checkout utama setelah merge.

## Ringkasan

- Proposal Tugas Akhir Capstone IF4091 (individu), Danendra Shafi Athallah (13523136), bidang *AI/NLP Semantic Claim Intelligence*. Acuan tim: `Penyelarasan Pemahaman Capstone.md` (keputusan tim 30 Oktober 2026).
- Bab I: `bab1/Bab_I_Draft.md` DRAF 4 per 2026-11-06 (untracked; status `DRAF`, belum dinyatakan SELESAI). Memuat 18 penanda [MENUNGGU KEPUTUSAN]/[PERLU VERIFIKASI…]; I.1 16 paragraf, I.4 6 paragraf; I.2, I.3, I.5 dan paragraf gap belum ditulis; judul individual menunggu K2. QA: siklus 0 keempat auditor FAIL; siklus 1 a10 dan a08 PASS_WITH_NOTES, a07 dan a09 FAIL; siklus 2 keempatnya PASS_WITH_NOTES; setelah satu perbaikan terarah tambahan atas izin pengguna ("Satu perbaikan terarah (Recommended)", 2026-11-06) pemeriksaan terarah DRAF 4: a10, a08, a07, a09 PASS_WITH_NOTES. PASS_WITH_NOTES bukan persetujuan Supervisor/pengguna. Temuan terbuka di `FINDINGS_LOG.md`; butir terbuka baru Q-B1-a..g dan K1 diperluas di `OPEN_QUESTIONS.md`.
- Keputusan ruang lingkup Bab I (ringkasan; rujuk `DECISION_LOG.md` untuk teks dan bukti): D-21 cakupan rawat inap dan rawat jalan terbatas (K5); D-22 pembanding kombinasi (P2); D-23 dasar bukti kerugian/premis (P3), sebagian digantikan D-24; D-24 sumber keterangan kerugian = dokumen Penyelarasan tim; D-25 lingkup I.4 (di luar kajian individu); D-26 subbab I.6 dihapus; D-27 atribusi kondisi RSIA di I.1 ke dokumen Penyelarasan saja.
- Tenggat (jawaban pengguna 2026-11-06, Q-08 ditutup): Bab I dan Bab II memiliki dua tenggat, yaitu 6 November 2026 sebagai tenggat lunak ke dosen pembimbing dan 10 November 2026 sebagai tenggat final ke pusat. Per 2026-11-06 (hari ini) tenggat lunak jatuh hari ini, `bab1/Bab_I_Draft.md` berstatus DRAF 4 (belum selesai), K1 dan K2 masih TERBUKA, dan K5 DIPUTUSKAN D-21.
- Bab II: DRAFT 6 di `bab2/Bab_II_Revisi_Notulensi.md` (`DRAF`, belum ditinjau pembimbing). Berkas II.1–II.8 lama masih ada dan digantikan DRAFT 6.
- Bab III: bahan pindahan di `bab3/Bahan_Pindahan_dari_Bab_II.md` (`DRAF`, bahan mentah).
- Sistem orkestrasi: implementasi Phase 3 di worktree `setup/orchestration` (HEAD `fee9a61`, berkas setup terlacak git); belum di-merge ke `main` (TSK-004, TSK-007). Perubahan `memory/**` sesi 2026-11-06 dan `bab1/Bab_I_Draft.md` belum ter-commit sampai G3 disetujui.

## Status per bab

| Bab | Berkas utama | Status | Catatan |
|---|---|---|---|
| I | `bab1/Bab_I_Draft.md` (sha256 `d2391ed67af3`, dihitung 2026-11-06 dengan `sha256sum`; berkas tanpa CR sehingga sama dengan hash normalisasi LF) | `DRAF` (DRAF 4) | QA PASS_WITH_NOTES (4 auditor, bukan persetujuan); 18 penanda; I.2, I.3, I.5 dan paragraf gap belum ditulis; judul menunggu K2; tenggat lunak 6 Nov, final 10 Nov 2026 |
| II | `bab2/Bab_II_Revisi_Notulensi.md` | `DRAF` (DRAFT 6) | Docx resmi `bab2/13523136-…-Draft-Bab2.docx` memuat suntingan tangan; tidak disentuh agent |
| III | `bab3/Bahan_Pindahan_dari_Bab_II.md` | Bahan mentah | — |
| IV | — | Belum ada | — |

## Artifact Map

Hash dihitung dari checkout utama pada 2026-11-05 (read-only), dengan line ending CRLF dinormalisasi ke LF untuk berkas teks (`content_hash`), sehingga checkout dengan `core.autocrlf` berbeda tidak memicu S1. Kelas mengikuti §A-7.1.

| Path | Fungsi | Kelas | Pemilik | sha256 | Diverifikasi |
|---|---|---|---|---|---|
| `CLAUDE.md` | Instruksi penulisan proyek (hash dari checkout utama; worktree 7d59b85 dapat berbeda; hash worktree belum dihitung, menunggu TSK-014) | P2 | Pengguna | `52d5bf1e820a` | 2026-11-05 |
| `RULES.md` | Kaidah penulisan | P2 | Pengguna | `60e61524dba5` | 2026-11-05 |
| `CONTEXT_TRANSFER.md` | Handoff lama (SUPERSEDED, D-05) | P2 | Pengguna | `9fdd21ae6723` | 2026-11-05 |
| `Penyelarasan Pemahaman Capstone.md` | Acuan keputusan tim; memuat pengenal kunjungan (D-11) | P0 | Tim | `3a86d78df7a7` | 2026-11-05 |
| `[REVISI] Breakdown Proposal (2).pdf` | Rancangan TA; angka pending menunggu pembahasan tim (D-11, D-19) | P0 | Pengguna | `442ec77e18a6` | 2026-11-05 |
| `Sumber Literatur Bab 2.pdf` | Daftar literatur awal | P0 | Pengguna | `cfd6dd5183d7` | 2026-11-05 |
| `source/INDEKS.md` | Indeks sumber tingkat berkas (hash dari checkout utama; worktree 7d59b85 dapat berbeda; hash worktree belum dihitung, menunggu TSK-014) | P0 | Pengguna | `4eadbada866f` | 2026-11-05 |
| `bab1/Bab_I_Draft.md` | Bab I DRAF 4 (untracked sampai G3; status DRAF) | P1 | A03 | `d2391ed67af3` | 2026-11-06 |
| `bab2/Bab_II_Revisi_Notulensi.md` | Bab II DRAFT 6 | P1 | A03 | `8cd97bed5345` | 2026-11-05 |
| `bab2/Kebutuhan_Literatur_Revisi_Bab_II.md` | Kebutuhan literatur revisi Bab II | P1 | A03 | `a6a8171c0704` | 2026-11-05 |
| `bab3/Bahan_Pindahan_dari_Bab_II.md` | Bahan pindahan Bab II ke Bab I/III | P1 | A03 | `0f8adb3f6b7f` | 2026-11-05 |
| `bab2/13523136-Proposal-IF4091-Capstone-Individu-2026-Draft-Bab2.docx` | Docx resmi Bab II (suntingan tangan) | P1 (docx; tidak disentuh agent) | Pengguna | `8dfef4f3cdf2` | 2026-11-05 |
| `bab2/Proposal-IF4091-Capstone-Individu-2026_Draft-Bab2_Editorial.docx` | Docx editorial lama (ditimpa build_docx.py; skrip dilarang, P2-02) | P1 (docx) | Pengguna | `c22d55616989` | 2026-11-05 |
| `template/Template-Proposal-IF4091-Capstone-Individu-2026.docx` | Templat yang dipakai | P0 | Prodi | `a76030913c40` | 2026-11-05 |
| `template/Template-Proposal-IF4091-Capstone-Utama-2026.docx` | Templat kelompok (belum dikerjakan) | P0 | Prodi | `7b68ab0220e6` | 2026-11-05 |
| `tools/build_modular.py` | Build docx modular (persetujuan per eksekusi, P2-02) | P2 | Pengguna | `a2ec9fbf4fe0` | 2026-11-05 |
| `tools/build_docx.py` | Build lama; path Linux; dilarang (P2-02) | P2 | Pengguna | `1cec5d69ce7f` | 2026-11-05 |
| `tools/build_with_toc.py` | Build lama; path Linux; dilarang (P2-02) | P2 | Pengguna | `93ead561a068` | 2026-11-05 |
| `tools/verify_claims.py` | Pemeriksa klaim; ROOT path Linux (D-16) (hash dari checkout utama; worktree 7d59b85 dapat berbeda; hash worktree belum dihitung, menunggu TSK-014) | P2 | Pengguna | `07f08ab75675` | 2026-11-05 |
| `modular/13523136-Proposal-IF4091-Capstone-Individu-2026-Modular-Bab-II.docx` | Modul Bab II siap kumpul | P1 (docx) | A03 via build_modular | `8d0ebe0195e5` | 2026-11-05 |
| `modular/13523136-Proposal-IF4091-Capstone-Individu-2026-Modular-Bab-II_Editorial.docx` | Modul Bab II editorial | P1 (docx) | A03 via build_modular | `0febb48d3e88` | 2026-11-05 |

## Team Docs Manifest

Pemilik ditulis menurut nama berkas dan wajib dikonfirmasi pengguna (Q-P2-a); tidak ditebak dari metadata.

| Path | Pemilik | Bab | Diterima | sha256 | Status |
|---|---|---|---|---|---|
| `capstone-teammate-propose/Proposal_Bab_I_Muhammad_Raihaan_Perdana - Copy.docx` | Raihaan (menurut nama berkas) | I | ± 2026-10-20 | `0a73e924a649` | PENDING_VERIFICATION |
| `capstone-teammate-propose/Proposal_Bab_II_Muhammad_Raihaan_Perdana.docx` | Raihaan (menurut nama berkas) | II | ± 2026-10-20 | `875ca63cbd36` | PENDING_VERIFICATION |
| `capstone-teammate-propose/Draft Proposal TA BAB 2 M. Abizzar Gamadrian.docx` | Abizzar (menurut nama berkas) | II | 2026-11-05 | `b079b28779d4` | PENDING_VERIFICATION |
| `capstone-teammate-propose/Draft Bab 1 (1).docx` | Belum diketahui (Q-P2-a) | I | — | `ebce9752915e` | PENDING_VERIFICATION |

## Dokumen SUPERSEDED

| Dokumen | Digantikan oleh | Dasar |
|---|---|---|
| `CONTEXT_TRANSFER.md` (root) | `memory/` (tujuh berkas) | D-05; dibiarkan apa adanya sebagai arsip |
| `bab2/Pembuka_Bab_II.md`, `bab2/II.1_…md`–`bab2/II.8_…md` | `bab2/Bab_II_Revisi_Notulensi.md` | Header DRAFT 6 (status menurut naskah; belum dikonfirmasi pengguna) |

## Efisiensi

Run Log sesi 2026-11-05: 14 eksekusi agent (TSK-005, TSK-012, TSK-013); durasi total sekitar 458,7 s; token yang dilaporkan harness berjumlah 238.971 (mungkin kumulatif per instance, jadi bukan angka pasti). Dua eksekusi PARTIAL, dua BLOCKED (T-19). Data lengkap di `TASK_TRACKER.md` Run Log.

Sesi 2026-11-06 (`check_memory.py --metrics`, kumulatif seluruh log): 45 pemanggilan dari 44 tugas; per agent a02=2, a03=5, a04=4, a05=1, a07=5, a08=4, a09=4, a10=4, a12=2, a13=14; rata-rata siklus maksimum per tugas 0,41; 5 tugas mencapai batas 2 siklus; QA FAIL pada siklus 0: 4 dari 27; Skill tercatat n/a untuk 45. Eksekusi Bab I (TSK-023..028) siklus 0: a02 571,6 s / 177.917 token; a03 437,4 s / 131.150; empat auditor FAIL siklus 0 (a09 218,3 s, a08 234,4 s, a07 172,7 s, a10 75,1 s). Siklus berikutnya lewat SendMessage tanpa token tercatat (n/a). Satu retry setelah HTTP 429.
