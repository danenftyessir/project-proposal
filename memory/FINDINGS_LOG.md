---
file: FINDINGS_LOG
revision: 8
status: CURRENT
updated: 2026-11-06
updated_by: a13-memory-manager
based_on_commit: fee9a61
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
| F-A04-0002 | a04 | `bab2/Bab_II_Revisi_Notulensi.md:15` | Pembuka Bab II membatasi rawat inap, keputusan tim mencakup rawat jalan terbatas (kini D-21). requires_decision: true | MEDIUM | OPEN | — |
| F-A04-0003 | a04 | `Penyelarasan Pemahaman Capstone.md:35` | Rumusan 1 menguji kombinasi tanpa pembanding (kini ditangani keputusan P2, D-22). requires_decision: true | MEDIUM | OPEN | — |
| F-A04-0004 | a04 | `Penyelarasan Pemahaman Capstone.md:321-339` | Ambang masih usulan awal; Bab I tidak boleh menyajikannya sebagai target; beri penanda [MENUNGGU KEPUTUSAN]. requires_decision: true | MEDIUM | OPEN | — |
| F-A04-0005 | a04 | `Penyelarasan Pemahaman Capstone.md:17, :65-80` | Semua angka masalah sama dengan angka Penyelarasan, tertahan D-19; jangan masukkan angka, jangan ganti dengan kata kabur. requires_decision: false | MEDIUM | OPEN | — |
| F-A04-0006 | a04 | `Penyelarasan Pemahaman Capstone.md:17, :98` | Premis tersembunyi bahwa ketidaksesuaian CPPT–resume menyebabkan pending, padahal klaim penurunan pending dilarang; kini ditangani keputusan P3 (D-23): dasar wawancara pihak RSIA, klaim dibatasi pada keterangan narasumber; naskah belum diubah, menunggu pemeriksaan ulang a04. requires_decision: true | MEDIUM | IN_PROGRESS | — |
| F-A04-0007 | a04 | `bab2/Bab_II_Revisi_Notulensi.md:118` vs `Penyelarasan Pemahaman Capstone.md:55` | Bab II membahas graf pengetahuan, sedangkan cara pemeriksaan tim rule-based dan RAG; peran di metode Bab I belum jelas. requires_decision: true | MEDIUM | OPEN | — |
| F-A04-0008 | a04 | `Penyelarasan Pemahaman Capstone.md:347` | Daftar jenis ketidaksesuaian dan satuan hitung presisi/recall belum final (Q-TEAM butir 1). requires_decision: true | MEDIUM | OPEN | — |
| F-A04-0009 | a04 | `memory/OPEN_QUESTIONS.md` K1, K2 | Judul (K2) dan gaya sitasi (K1) tidak menghambat substansi; pakai judul capstone dengan penanda dan konvensi sitasi Bab II sekarang. requires_decision: false | LOW | OPEN | — |
| F-A07-0004 | a07 | Bab I, I.4 (lingkup kajian) | Konsistensi antar-entri CPPT di I.4; lingkup diputuskan D-25 (di luar kajian individu). Deskripsi dan severity rinci ada di laporan a07 (tidak ada di brief TSK-029). requires_decision: true | n/a | IN_PROGRESS | — |
| F-A07-0005 | a07 | Bab I, I.4 (lingkup kajian) | Penautan ibu-bayi di I.4; diputuskan D-25 (di luar kajian individu; pemilik di tim perlu dipastikan). Severity ada di laporan a07. requires_decision: true | n/a | IN_PROGRESS | — |
| F-A07-0010 | a07 | Bab I, I.1 (atribusi kondisi RSIA) | Atribusi ke wawancara; diputuskan D-27 (dokumen Penyelarasan saja). Severity ada di laporan a07. requires_decision: true | n/a | IN_PROGRESS | — |
| F-A07-0012 | a07 | Bab I | Tidak ditangani keputusan 2026-11-06; deskripsi rinci ada di laporan a07 (tidak ada di brief TSK-029) | n/a | OPEN | — |
| F-A10-0001 | a10 | Bab I, I.6 Sistematika Penulisan | Subbab I.6 di luar templat Individu I.1-I.5; diputuskan dihapus (D-26). Severity ada di laporan a10. requires_decision: true | n/a | IN_PROGRESS | — |
| F-A10-0002 | a10 | Bab I, I.6 Sistematika Penulisan | Terkait I.6; ditangani D-26. Severity ada di laporan a10. requires_decision: true | n/a | IN_PROGRESS | — |
| F-A02-0001 | a02 | `source/INDEKS.md:13-34,200-203` | INDEKS tidak cocok dengan struktur folder setelah restrukturisasi. requires_decision: false | MEDIUM | OPEN | — |
| F-A02-0002 | a02 | `source/01_Regulasi…/Permenkes_26_2021_Pedoman_INA-CBG.pdf` | PDF resmi tanpa lapisan teks; halaman diverifikasi dari salinan JDIH (a08 membaca hlm. 23, 53, 54, 7 secara visual dari salinan resmi dan identik). requires_decision: false | MEDIUM | OPEN | — |
| F-A02-0003 | a02 | `Penyelarasan Pemahaman Capstone.md:51` | Pasal 26 PMK 24/2022 tidak identik dengan resume medis; di Bab I ditulis sebagai tafsiran. requires_decision: false | MEDIUM | IN_PROGRESS | — |
| F-A02-0004 | a02 | `.scratch/bab1_evidence.md` bagian C (P-6) | Tidak ada sumber yang menyatakan ketidaksesuaian CPPT–resume menimbulkan pending/kerugian; ditulis sebagai premis BELUM DIVERIFIKASI. requires_decision: false | MEDIUM | IN_PROGRESS | — |
| F-A07-0001 | a07 | `bab1/Bab_I_Draft.md:38,48-56` | Masalah konkret di RSIA terkait CPPT lawan resume belum ditunjukkan; menunggu keputusan pengguna/tim atas angka (D-19). requires_decision: true | MEDIUM | OPEN | — |
| F-A07-0019 | a07 | `bab1/Bab_I_Draft.md:60` | Dukungan rawat jalan hanya disebut "lebih lemah"; perlu dinyatakan per mata rantai. requires_decision: false | LOW | OPEN | — |
| F-A07-0020 | a07 | `bab1/Bab_I_Draft.md:84` | Episode rawat inap didefinisikan mulai tanggal masuk, tetapi SPRI hari yang sama dimasukkan ke episode yang sama; pengecualian belum ditandai. requires_decision: false | LOW | OPEN | — |
| F-A08-0004 | a08 | `bab1/Bab_I_Draft.md:56` | Muroli dkk. (2020) disitasi tanpa entri daftar pustaka; menunggu K1. requires_decision: true | MEDIUM | OPEN | — |
| F-A08-0005 | a08 | `bab1/Bab_I_Draft.md:42,62` | Penyelarasan dirujuk di prosa tanpa entri; menunggu K1. requires_decision: true | LOW | OPEN | — |
| F-A08-0010 | a08 | `bab1/Bab_I_Draft.md:52` | Dicabut oleh a08: halaman naskah benar menurut salinan Berita Negara | n/a (dicabut) | RESOLVED | — |
| F-A08-0013 | a08 | `source/INDEKS.md:201`; `bab1/Bab_I_Draft.md:58` | Dua salinan PMK 24/2022 beda paginasi; salinan acuan halaman belum ditetapkan. Dicatat walau INFO karena butuh keputusan. requires_decision: true | INFO | OPEN | — |
| F-A09-0006 | a09 | `bab1/Bab_I_Draft.md` | "deidentifikasi" vs "de-identifikasi" (Bab II); bentuk baku belum diverifikasi (KBBI). requires_decision: true | LOW | OPEN | — |
| F-A09-0017 | a09 | `bab1/Bab_I_Draft.md:40,62` | "diinput"/"penginputan" belum diverifikasi. requires_decision: true | LOW | OPEN | — |
| F-A09-0018 | a09 | `bab1/Bab_I_Draft.md:38` | "capstone" tegak atau miring belum diputuskan. requires_decision: true | LOW | OPEN | — |
| F-A09-0038 | a09 | `bab1/Bab_I_Draft.md:58-60` | Urutan paragraf lingkup tim dan sintesis rawat inap/jalan. requires_decision: false | LOW | OPEN | — |
| F-A09-0039 | a09 | `bab1/Bab_I_Draft.md:46-52` | Enumerasi pertama/kedua/ketiga berulang di empat paragraf. requires_decision: false | LOW | OPEN | — |
| F-A09-0040 | a09 | `bab1/Bab_I_Draft.md:52` | "sumber" dua makna; "yang ditelaah" dua kali. requires_decision: false | LOW | OPEN | — |
| F-A10-0006 | a10 | `bab1/Bab_I_Draft.md:34,36` | Heading bab dan subbab sama tingkat; perlu aturan pemetaan ekspor. requires_decision: false | LOW | OPEN | — |
| F-A10-0009 | a10 | `bab1/Bab_I_Draft.md` I.1 | I.1 16 paragraf, templat meminta "ringkas"; pilihan meringkas lagi ada pada penulis. requires_decision: false | LOW | OPEN | — |
| F-A10-0010 | a10 | `bab2/Bab_II_Revisi_Notulensi.md:13` | Judul Bab II "Studi Literatur" vs templat "Kajian Pustaka". requires_decision: true | LOW | OPEN | — |
| F-A10-0016 | a10 | `bab1/Bab_I_Draft.md:137-138` (Catatan kerja) | Penunjuk paragraf 11 basi; seharusnya paragraf 13. requires_decision: false | LOW | OPEN | — |

Catatan TSK-030: temuan lain yang dinyatakan RESOLVED oleh auditor penemu pada siklus 1-2 dan pemeriksaan terarah DRAF 4 (a09 sebagian besar dari F-A09-0001..0037; a08 0001/0002/0003/0006/0008/0011/0012/0014; a07 0002/0003/0006-0009/0011/0013-0017; a10 0003/0004/0007/0008/0012/0013/0015) tidak dicatat per baris; ringkasan di Run Log/TASK_TRACKER. Baris F-A07-0004/0005/0010/0012 dan F-A10-0001/0002 tetap `n/a` untuk severity karena brief TSK-030 tidak memuatnya.