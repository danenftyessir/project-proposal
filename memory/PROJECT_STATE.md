---
file: PROJECT_STATE
revision: 20
status: PENDING_VERIFICATION
updated: 2026-11-07
updated_by: a13-memory-manager
based_on_commit: ecf15cf
---

# Project State

Ringkasan kondisi aktual. Bila bertentangan dengan artefak repository, artefak yang berlaku (§A-12.3). Status berkas ini `PENDING_VERIFICATION` sampai A13 menjalankan rekonsiliasi pertama dari checkout utama setelah merge.

## Ringkasan

- Proposal Tugas Akhir Capstone IF4091 (individu), Danendra Shafi Athallah (13523136), bidang *AI/NLP Semantic Claim Intelligence*. Acuan tim: `Penyelarasan Pemahaman Capstone.md` (keputusan tim 30 Oktober 2026).
- Bab I terbaru (TSK-059, menurut A01): `bab1/Bab_I_Draft.md` DRAF 10 dengan 39 penanda (I.1 12, I.2 8, I.3 7, I.4 4, I.5 8); I.5 Metodologi ditulis tanpa kerangka bernama (D-34); paragraf research gap I.1 belum ditulis; I.5 BELUM diperiksa QA; hash belum dihitung ulang (Artifact Map masih hash DRAF 8). Butir baru Q-B1-ad..ag. Build modular I dan II (TSK-061) disetujui operasional untuk satu eksekusi dengan keterbatasan sumber (bukan dari Markdown Bab I DRAF 10), tetapi GAGAL (ModuleNotFoundError lxml, tanpa retry); modul Bab I/II di modular/ BUKAN DRAF 10 dan tidak berubah oleh percobaan build gagal (Q-B1-ah, Q-B1-ai); Q-B1-ac ditutup dengan alasan. Rincian di bawah adalah catatan DRAF 8 (sebelumnya).
- Per 2026-11-07: D-35 (APPROVED) menempatkan peran migrasi Markdown final ke Docs/DOCX pada a03 dengan perbaikan `tools/build_modular.py` (tiga varian: editorial, formal, lengkap; jalur Google Docs); rincian terbuka Q-B1-ak..am. D-36 (APPROVED, 2026-11-07): a03 diberi wewenang edit khusus `tools/build_modular.py` (approval per perubahan, audit a12); wewenang belum berlaku operasional sampai AGENT_SPECIFICATIONS, hook guard, dan check_agents diubah (Q-B1-al; jalur pengeditnya Q-B1-an terbuka). Q-B1-aj DIPUTUSKAN. D-37 (APPROVED, 2026-11-07): perubahan spesifikasi, hook, check_agents, dan definisi a03 dikerjakan pengguna atau sesi Claude Code biasa di luar agent (Q-B1-an DIPUTUSKAN; Q-B1-al tetap TERBUKA sampai perubahan diterapkan dan check_agents lolos). D-38 (APPROVED, 2026-11-07): tiga varian = Editorial (...-Modular-Bab-{I-IV}_Editorial.docx, memuat catatan), Formal (...-Modular-Bab-{I-IV}.docx, siap kumpul meski ada celah), Lengkap (proposal utuh mengikuti templat Individu, acuan "Template-Proposal-IF4091-Capstone-Individu-2026 - Copy.docx" di root); keluaran DOCX saja, unggah ke Google Docs manual oleh pengguna (menyempitkan D-35); Q-B1-ak DIPUTUSKAN SEBAGIAN, sisa di Q-B1-ao..ar. D-39 (APPROVED, 2026-11-07): PDF hanya untuk varian Formal dan Lengkap (Editorial DOCX saja; memperluas D-38 untuk dua varian itu; Q-B1-ap DIPUTUSKAN; cara konversi PDF, izin Bash a03, dan kriteria audit a12 untuk PDF belum diputuskan). D-40 (APPROVED, 2026-11-07): varian Lengkap mengisi templat Individu dengan teks Bab I-IV langsung dari Markdown bab1/-bab4/, komponen pelengkap tanpa data diberi placeholder jelas, a12 memastikan placeholder tidak lolos ke berkas kumpul (Q-B1-ar DIPUTUSKAN). D-41 (APPROVED, 2026-11-07): varian Formal diturunkan dari Editorial dengan menghapus teks tersorot dan penanda berkurung tanpa pengganti; satu sumber Markdown, tanpa sintaks penanda baru (Q-B1-aq DIPUTUSKAN; konsekuensi: entri seperti Yang et al. bisa tidak lengkap di Formal, teks Formal hasil skrip berbeda dari Formal sekarang di modular/). Butir turunan terbuka Q-B1-as..av (pemeriksaan kelengkapan Formal, status placeholder templat, deteksi catatan tak berkurung, nasib Formal yang ada). D-42 (APPROVED, 2026-11-07): varian Lengkap merujuk template/Template-Proposal-IF4091-Capstone-Individu-2026.docx sebagai dasar; berkas "- Copy" di root tidak dirujuk skrip (menggantikan penunjukan "- Copy" pada D-38 sebatas penunjukan berkas; hash kedua berkas identik, fakta bukan keputusan; nasib berkas "- Copy" di luar persetujuan). Q-B1-ao DIPUTUSKAN; seluruh butir pembuka Q-B1-ak (a)-(d) terjawab (D-38..D-42), Q-B1-ak DIPUTUSKAN. Working tree per 2026-11-07 (diperiksa git status): hanya `memory/**` berubah belum ter-commit; `bab1/Bab_I_Draft.md`, modular/*.docx, `bab1/Bab1_Revisi1_IF4091.*`, `bab1/Proposal_IF4091_Bab_I.docx`, `bab2/Bab_II_Migrasi.*` sudah terlacak (HEAD b05a2e3 "feat: migrate docs agent"); berkas migrasi itu menurut brief A01 berasal dari LLM lain di luar sistem, belum diverifikasi isinya oleh A13 dan belum terdaftar di Artifact Map. Hash S1 (CLAUDE.md, source/INDEKS.md, Bab_I_Draft.md, verify_claims.py, dua modul Bab II) belum diperbarui.
- Yang menunggu pengguna (jalur build modular, per 2026-11-07): (1) Q-B1-al, perubahan spesifikasi, hook, check_agents, dan definisi a03 oleh pengguna atau sesi biasa (D-37), termasuk izin Bash a03 untuk konversi PDF bila D-39 dilaksanakan; (2) Q-B1-am, nasib skrip lama (D-16); (3) Q-B1-as..av, yaitu kelengkapan Formal setelah penanda dihapus, status placeholder templat, deteksi catatan tak berkurung, dan nasib Formal yang ada di modular/; (4) peringatan S1 check_memory: dua docx bab2/ tercatat di Artifact Map tetapi tidak ditemukan di worktree (`bab2/13523136-...-Draft-Bab2.docx` dan `bab2/...Draft-Bab2_Editorial.docx`), belum dijelaskan.
- Bab I (DRAF 8): `bab1/Bab_I_Draft.md` DRAF 8 per 2026-11-06 (DRAF 8 ter-commit di f3cb6ba "feat: bab 1.1-1.3", dibuat pengguna di luar A13; status `DRAF`, belum dinyatakan SELESAI). Memuat 31 penanda (cocok dengan header, diperiksa a10); I.2 ditulis (D-28), I.3 ditulis (D-31, D-33), I.4 diselaraskan (D-29, D-30); paragraf research gap I.1 dan I.5 belum ditulis; judul individual menunggu K2. QA I.3 DRAF 8 (TSK-042..045): a07 (S0 FAIL, S1 PASS_WITH_NOTES, S2 FAIL F-A07-0047, terarah PASS_WITH_NOTES), a09 dan a10 (S0, S1, S2, terarah PASS_WITH_NOTES); satu perbaikan terarah di luar batas siklus D-06 atas jawaban pengguna "Satu perbaikan terarah (Recommended)" (2026-11-06; konteks, bukan keputusan). Semua auditor PASS_WITH_NOTES; sisa LOW/INFO di FINDINGS_LOG (F-A07-0048, F-A09-0103, F-A09-0104); bukan persetujuan Supervisor/pengguna. Tantangan a05 F-A05-0002, 0006, 0007, 0009, 0012 tetap OPEN; F-A05-0008 IN_PROGRESS; Q-B1-t dan Q-B1-u baru. Catatan sebelumnya (DRAF 6):  QA I.2/I.4 DRAF 6: TSK-034 (a03) siklus 0, 1, 2 selesai; a07 (S0 FAIL, S1 dan S2 PASS_WITH_NOTES), a09 (S0 FAIL, S1 dan S2 PASS_WITH_NOTES), a10 (S1 dan terarah S2 PASS_WITH_NOTES). Siklus otomatis (maks 2, D-06) habis; satu perbaikan terarah tambahan hanya I.2 paragraf 1 (F-A07-0036) dilakukan atas izin pengguna 2026-11-06. Kondisi akhir QA I.2/I.4 DRAF 6: semua auditor PASS_WITH_NOTES, sisa temuan LOW/INFO di FINDINGS_LOG, bukan persetujuan Supervisor/pengguna. PASS_WITH_NOTES bukan persetujuan Supervisor/pengguna. QA DRAF 4 sebelumnya: keempat auditor PASS_WITH_NOTES setelah satu perbaikan terarah atas izin pengguna ("Satu perbaikan terarah (Recommended)", 2026-11-06). Temuan terbuka di `FINDINGS_LOG.md`; butir terbuka Q-B1-a..k dan K1 di `OPEN_QUESTIONS.md`.
- Keputusan ruang lingkup Bab I (ringkasan; rujuk `DECISION_LOG.md` untuk teks dan bukti): D-21 cakupan rawat inap dan rawat jalan terbatas (K5); D-22 pembanding kombinasi (P2); D-23 dasar bukti kerugian/premis (P3), sebagian digantikan D-24; D-24 sumber keterangan kerugian = dokumen Penyelarasan tim; D-25 lingkup I.4 (di luar kajian individu); D-26 subbab I.6 dihapus; D-27 atribusi kondisi RSIA di I.1 ke dokumen Penyelarasan saja.
- Tenggat (jawaban pengguna 2026-11-06, Q-08 ditutup): Bab I dan Bab II memiliki dua tenggat, yaitu 6 November 2026 sebagai tenggat lunak ke dosen pembimbing dan 10 November 2026 sebagai tenggat final ke pusat. Per 2026-11-06 (hari ini) tenggat lunak jatuh hari ini, `bab1/Bab_I_Draft.md` berstatus DRAF 8 (belum selesai), K1 dan K2 masih TERBUKA, dan K5 DIPUTUSKAN D-21.
- Bab II: DRAFT 6 di `bab2/Bab_II_Revisi_Notulensi.md` (`DRAF`, belum ditinjau pembimbing). Berkas II.1–II.8 lama masih ada dan digantikan DRAFT 6.
- Posisi Wave 1 (2026-11-06, TSK-055..058): tinjauan ulang a05 (F-A05-0008 RESOLVED; F-A05-0002 HIGH tetap OPEN; baru F-A05-0017..0022) dan a11 (PASS_WITH_NOTES; baru F-A11-0012..0014), pemeriksaan lintas proposal A06 (16 temuan, 2 HIGH, semua OPEN, pemilik dokumen anggota belum dikonfirmasi) dan pemeriksaan bukti Bab II oleh a02 (PARTIAL; 47 klaim; satu BERTENTANGAN B2-40, sisa scope dicatat) sudah dicatat di `FINDINGS_LOG.md`, `OPEN_QUESTIONS.md` (Q-B1-v..ab) dan `EVIDENCE_REGISTRY.md` rev 3; naskah belum diubah; TSK-057 (a03 Wave 2a) berjalan; semua itu bukan persetujuan.
- Bab III: bahan pindahan di `bab3/Bahan_Pindahan_dari_Bab_II.md` (`DRAF`, bahan mentah).
- Sistem orkestrasi: implementasi Phase 3 di worktree `setup/orchestration` (HEAD `b05a2e3` per 2026-11-07, sebelumnya f3cb6ba; berkas setup terlacak git); belum di-merge ke `main` (TSK-004, TSK-007). Perubahan `memory/**` sesi 2026-11-06 dan `bab1/Bab_I_Draft.md` (DRAF 8) ter-commit di f3cb6ba; per 2026-11-07 hanya `memory/**` yang berubah belum ter-commit. Commit dibuat pengguna sendiri di luar A13; persetujuan G3 lewat jawaban pengguna tidak tercatat sebagai approval_evidence (fakta operasional, bukan G3 yang disetujui). Pengguna menyatakan sudah push (pernyataan 2026-11-06); tidak terverifikasi karena upstream tidak terlihat di `git status -sb`.

## Status per bab

| Bab | Berkas utama | Status | Catatan |
|---|---|---|---|
| I | `bab1/Bab_I_Draft.md` (sha256 `05b369128553`, dihitung 2026-11-06 dengan `sha256sum`; berkas tanpa CR sehingga sama dengan hash normalisasi LF) | `DRAF` (DRAF 8) | QA PASS_WITH_NOTES (a07, a09, a10; bukan persetujuan); 31 penanda; I.2, I.3 ditulis, I.4 diselaraskan; paragraf gap I.1 dan I.5 belum ditulis; judul menunggu K2; tenggat lunak 6 Nov, final 10 Nov 2026 |
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
| `bab1/Bab_I_Draft.md` | Bab I DRAF 8 (DRAF 8 ter-commit di f3cb6ba; hash DRAF 8 dihitung 2026-11-06 dengan `sha256sum`, tanpa CR; status DRAF) | P1 | A03 | `05b369128553` | 2026-11-06 |
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

Sesi 2026-11-06 (`check_memory.py --metrics`, kumulatif seluruh log, per penutupan TSK-052): 76 pemanggilan dari 75 tugas; per agent a02=2, a03=11, a04=4, a05=2, a07=10, a08=4, a09=9, a10=7, a11=1, a12=2, a13=24; rata-rata siklus maksimum per tugas 0,25; 5 tugas mencapai batas 2 siklus; QA FAIL pada siklus 0: 8 dari 46; Skill tercatat n/a untuk 76. Eksekusi Bab I (TSK-023..028) siklus 0: a02 571,6 s / 177.917 token; a03 437,4 s / 131.150; empat auditor FAIL siklus 0 (a09 218,3 s, a08 234,4 s, a07 172,7 s, a10 75,1 s). Siklus berikutnya lewat SendMessage tanpa token tercatat (n/a). Satu retry setelah HTTP 429.
