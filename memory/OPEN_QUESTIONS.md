---
file: OPEN_QUESTIONS
revision: 40
status: CURRENT
updated: 2026-11-09
updated_by: a13-memory-manager
based_on_commit: 4351fe5
---

# Open Questions

Isu terbuka dan permintaan persetujuan. Status: `TERBUKA` · `MENUNGGU DATA` · `MENUNGGU ANGGOTA` · `MENUNGGU PEMBIMBING` · `DIPUTUSKAN → D-xx` · `DITUTUP DENGAN ALASAN`. Tidak ada butir yang diselesaikan sistem tanpa keputusan pengguna (S-3).

## K1–K7 (konflik antardokumen, docs/ORCHESTRATION_ARCHITECTURE.md Lampiran A)

```yaml
id: K1
question: Gaya sitasi akhir — penulis-tahun sementara dengan hlm. (CONTEXT_TRANSFER kep. 1, header DRAFT 6) atau APA (keputusan tim 30 Oktober di Penyelarasan)?
why: A03 dan A08 memerlukan konvensi tetap; sampai diputuskan, A08 tidak menilai format terhadap salah satu gaya (S-14)
affected: [A03, A08, bab2/Bab_II_Revisi_Notulensi.md]
class: L3
pic: Pengguna
ask_to: Tim / pembimbing
status: TERBUKA
updated: 2026-11-06
refs: [D-11, F-A08-0004, F-A08-0005, F-A08-0013]
extended: 'Per 2026-11-06 K1 juga menaungi: (1) bentuk sitasi sekunder untuk Muroli dkk. (2020); (2) atribusi dokumen tim Penyelarasan di daftar pustaka; (3) salinan acuan halaman PMK 24/2022 (usulan agent, bukan keputusan: Berita Negara).'
```

```yaml
id: K2
question: Judul capstone mana yang berlaku — judul lama di CONTEXT_TRANSFER kep. 18 atau judul baru di Penyelarasan (menunggu persetujuan pembimbing, isu tim 9)?
why: Menentukan keselarasan Bab I dan kontribusi individu
affected: [Bab I, sampul docx]
class: L3
pic: Abizzar (menurut Penyelarasan)
ask_to: Pembimbing
status: MENUNGGU PEMBIMBING
updated: 2026-11-05
refs: []
```

```yaml
id: K3
question: Peran Abizzar — frontend/antarmuka (CONTEXT_TRANSFER §1) atau ketua tim, Claim Review & Resolution Engineering (Penyelarasan)?
why: A06 memerlukan pembagian peran yang benar untuk memeriksa tumpang tindih kontribusi
affected: [A06]
class: L3
pic: Pengguna
ask_to: Tim
status: TERBUKA
updated: 2026-11-05
refs: []
```

```yaml
id: K4
question: Branch kerja proposal — CONTEXT_TRANSFER menyebut claude/determined-davinci-ueb8i9, sedangkan kerja aktual di main
why: A13 perlu tahu branch target commit proposal
affected: [A13]
class: L4
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-05
refs: []
```

```yaml
id: K5
question: Cakupan perawatan — rawat inap saja (CONTEXT_TRANSFER) atau rawat inap dan rawat jalan terbatas (Penyelarasan)?
why: Menentukan ruang lingkup Bab I
affected: [Bab I, A07, A11]
class: L3
pic: Pengguna
ask_to: Tim
status: DIPUTUSKAN → D-21
updated: 2026-11-06
refs: [D-21, D-19]
follow_up: 'TERBUKA: selaraskan pembuka Bab II (bab2/Bab_II_Revisi_Notulensi.md:15) dan II.1 Rekam Medis Rawat Inap; bentuk dokumen rawat jalan di RSIA belum dipastikan (Q-TEAM butir 4); dasar kuantitatif tertahan D-19. Naskah belum diubah.'
```

```yaml
id: K6
question: Lingkup kerja agent — CONTEXT_TRANSFER membatasi pada Bab II satu subbab per chat, sedangkan pekerjaan berjalan sudah Bab I
why: A01 memerlukan batas lingkup tugas
affected: [A01, A03]
class: L2
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-05
refs: [D-05]
```

```yaml
id: K7
question: CLAUDE.md induk IF4071 termuat di sesi proyek
why: Instruksi tidak relevan masuk konteks
affected: [semua sesi di checkout utama]
class: L4
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
note: Mitigasi teknis D-03 (claudeMdExcludes, omitClaudeMd) tanpa mengubah berkas induk; diuji T-02 setelah merge
updated: 2026-11-05
refs: [D-03]
```

## Penafsiran yang menunggu konfirmasi

```yaml
id: I-1
question: Apakah pertanyaan klarifikasi Supervisor tidak dihitung dalam batas tiga pertanyaan per sesi wawancara?
why: Penafsiran P2-04 yang berlaku sementara di prompt A04
affected: [A04, A01]
class: L4
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-05
refs: [P2-04]
```

```yaml
id: I-2
question: Apakah satu sesi wawancara berarti satu tugas wawancara A04 dari awal sampai ringkasan?
why: Penafsiran P2-04 yang berlaku sementara di prompt A04
affected: [A04, A01]
class: L4
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-05
refs: [P2-04]
```

## Dokumen tim dan data

```yaml
id: Q-P2-a
question: Siapa pemilik capstone-teammate-propose/Draft Bab 1 (1).docx/.pdf?
why: A06 tidak menebak pemilik dokumen
affected: [A06, PROJECT_STATE Team Docs Manifest]
class: L3
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-06
refs: [F-A06-0006, F-A06-0014, Q-B1-aa]
```

```yaml
id: Q-P2-b
question: Siapa penulis Penyelarasan Pemahaman Capstone.md, dan adakah versi yang lebih baru di luar repo?
why: Penyelarasan adalah acuan kelompok untuk A06
affected: [A06]
class: L3
pic: Pengguna
ask_to: Tim
status: TERBUKA
updated: 2026-11-05
refs: []
```

```yaml
id: Q-P2-c
question: Dokumen Bab Abizzar — Bab II tersedia sejak 2026-11-05 (menurut nama berkas); apakah Bab I juga akan tersedia?
why: Pemeriksaan tiga arah A06
affected: [A06]
class: L3
pic: Pengguna
ask_to: Tim
status: MENUNGGU ANGGOTA
updated: 2026-11-06
refs: [F-A06-0014, Q-B1-aa]
```

```yaml
id: Q-TEAM
question: Sembilan hal yang belum ditetapkan di Penyelarasan (bagian "Yang Masih Perlu Ditetapkan")
why: Berdampak pada ketiga anggota; dicatat sebagai rujukan, bukan disalin
affected: [Bab I, A06, A11]
class: L3
pic: Abizzar (menurut Penyelarasan)
ask_to: Tim / RSIA mitra / pembimbing
status: MENUNGGU ANGGOTA
updated: 2026-11-05
refs: []
```

```yaml
id: Q-RSIA-1
question: Apakah penyimpanan data pasien RSIA di folder OneDrive organisasi sesuai perjanjian data dengan RSIA?
why: Data asli dan turunan (.scratch/rsia/) tersinkron ke OneDrive (§A-8.3 risiko sisa 4)
affected: [D-17]
class: L3
pic: Pengguna
ask_to: Tim / RSIA mitra
status: TERBUKA
updated: 2026-11-05
refs: [D-17]
```

```yaml
id: Q-08
question: Tenggat Bab I 10 November 2026 hanya tercatat di work-state claude-mem; apakah benar?
why: claude-mem hanya alat recall; fakta wajib diverifikasi ke pengguna atau artefak
affected: [A01, TASK_TRACKER]
class: L4
pic: Pengguna
ask_to: Pengguna
status: DITUTUP DENGAN ALASAN (dijawab pengguna 2026-11-06; fakta jadwal, bukan keputusan akademik)
updated: 2026-11-06
refs: [TSK-017]
answer: >
  Ada dua tenggat untuk Bab I dan Bab II: 6 November 2026 = tenggat lunak ke dosen pembimbing;
  10 November 2026 = tenggat final ke pusat. Tenggat 10 November di work-state claude-mem
  hanya benar sebagai tenggat final, bukan satu-satunya tenggat.
approval_evidence:
  question: "Untuk mencatat Q-08, saya menafsirkan 6 November sebagai tenggat lunak ke dosen pembimbing dan 10 November sebagai tenggat final ke pusat, keduanya untuk Bab I dan Bab II. Apakah pemetaan ini benar?"
  options_offered: ["Ya, benar", "Terbalik"]
  user_answer: "Ya, benar (didahului pernyataan pengguna: 'tenggatnya ada 2, tanggal 6 nov dan 10 nov' dan 'bab 1 dan 2 dan itu soft deadline untuk dosen pembimbing sebelum dikirim ke pusat finalnya')"
  answered_at: 2026-11-06
  session_ref: "sesi /sesi-mulai 2026-11-06, jawaban AskUserQuestion Tenggat"
  scope: "Hanya fakta tenggat: 6 Nov 2026 = tenggat lunak Bab I dan II ke dosen pembimbing; 10 Nov 2026 = tenggat final Bab I dan II ke pusat"
```

## Pertanyaan tersisa wawancara a04 (TSK-018, menunggu jawaban pengguna)

```yaml
id: Q-A04-a
question: Apakah graf pengetahuan Bab II (II.4.2) bagian dari metode Bab I?
affected: [Bab I, Bab II]
class: L3
pic: Pengguna
status: TERBUKA
updated: 2026-11-06
refs: [F-A04-0007, D-34]
```

```yaml
id: Q-A04-b
question: Apakah rumusan individual mengambil bagian rumusan 4 (kejelasan alasan dan rujukan)?
affected: [Bab I]
class: L3
pic: Pengguna
status: DIPUTUSKAN → D-28
updated: 2026-11-06
refs: [D-28, F-A04-0004]
```

```yaml
id: Q-A04-c
question: Berapa jumlah kasus di balik "jumlah kasusnya mencukupi" (Penyelarasan Pemahaman Capstone.md:61)?
affected: [Bab I, A11]
class: L3
pic: Pengguna
status: TERBUKA
updated: 2026-11-08
refs: [D-19, F-A05-0034, F-A11-0016, F-A11-0018]
note: Kemajuan 2026-11-08 (siklus 2 DRAF 13): jumlah episode per jenis perawatan tidak dapat dinilai; data agregat (`.scratch/rsia/agregat/`) tidak ada. Relevan untuk kelayakan stratum rawat jalan. Tetap TERBUKA.
```

```yaml
id: Q-A04-d
question: Satuan hitung presisi/recall: per temuan, per jenis, atau per episode?
affected: [Bab I, A11]
class: L3
pic: Pengguna
ask_to: Tim
status: TERBUKA
updated: 2026-11-06
refs: [F-A04-0008, Q-TEAM]
```

```yaml
id: Q-A04-e
question: Apakah isi kualitatif wawancara Direktur RSIA boleh diparafrasakan di latar belakang (D-19 hanya mengatur angka)?
affected: [Bab I]
class: L3
pic: Pengguna
status: DIPUTUSKAN → D-24
updated: 2026-11-06
refs: [D-19, D-23, D-24]
```

```yaml
id: Q-A04-f
question: Judul individual Bab I apa yang dipakai?
affected: [Bab I]
class: L3
pic: Pengguna
status: TERBUKA
updated: 2026-11-06
refs: [K2, F-A04-0009]
```

## Butir baru dari QA Bab I DRAF 4 (TSK-030, 2026-11-06)

Semua butir berikut TERBUKA; tidak ada yang diputuskan.

```yaml
id: Q-B1-a
question: Bentuk baku menurut KBBI untuk capstone (tegak/miring), diinput/penginputan, dan deidentifikasi/de-identifikasi?
affected: [Bab I, Bab II]
class: L4
pic: Pengguna
status: TERBUKA
updated: 2026-11-06
refs: [F-A09-0006, F-A09-0017, F-A09-0018]
```

```yaml
id: Q-B1-b
question: Bagaimana F-A07-0001 (masalah konkret CPPT lawan resume di RSIA belum ditunjukkan) diselesaikan, mengingat angka tertahan D-19?
affected: [Bab I]
class: L3
pic: Pengguna
ask_to: Tim
status: MENUNGGU ANGGOTA
updated: 2026-11-06
refs: [F-A07-0001, D-19]
```

```yaml
id: Q-B1-c
question: Siapa pemilik di tim untuk penautan ibu-bayi (Penyelarasan:43) setelah lingkup I.4 diputuskan di luar kajian individu?
affected: [Bab I, A06]
class: L3
pic: Pengguna
ask_to: Tim
status: MENUNGGU ANGGOTA
updated: 2026-11-06
refs: [D-25, F-A07-0005]
```

```yaml
id: Q-B1-d
question: Konfirmasi pembimbing atas urutan paragraf 1 I.1 (masalah dulu, rujukan capstone kemudian) dibanding templat
affected: [Bab I]
class: L3
pic: Pengguna
ask_to: Pembimbing
status: MENUNGGU PEMBIMBING
updated: 2026-11-06
refs: []
```

```yaml
id: Q-B1-e
question: Judul Bab II mana yang berlaku, "Studi Literatur" (naskah) atau "Kajian Pustaka" (templat)?
affected: [Bab II]
class: L3
pic: Pengguna
ask_to: Pembimbing
status: TERBUKA
updated: 2026-11-06
refs: [F-A10-0010]
```

```yaml
id: Q-B1-f
question: Apa definisi "rawat jalan terbatas" dan bentuk dokumen rawat jalan di RSIA (Q-TEAM butir 4)?
affected: [Bab I, Bab II]
class: L3
pic: Pengguna
ask_to: Tim / RSIA mitra
status: MENUNGGU ANGGOTA
updated: 2026-11-08
refs: [D-21, Q-TEAM, F-A07-0019, F-A04-0010, F-A04-0011]
note: 'Pernyataan pengguna 2026-11-08 (BUKAN keputusan; premis, belum diverifikasi ke aturan atau RSIA). Pertanyaan a04 P1 (verbatim): "Pertanyaan a04 (P1 dari 3), diteruskan verbatim. Konteks (ringkas): I.4 paragraf 2 membatasi dokumen pada \"CPPT dan resume medis\"; paragraf 4 hanya memuat penanda #28 tanpa batas rawat jalan; I.1 paragraf 4 menyebut resume medis belum tentu ada pada setiap episode rawat jalan; Penyelarasan:279 memakai frasa \"atau padanannya\" yang tidak ada di I.4; I.2 menyatakan kedua pertanyaan berlaku pada rawat inap dan rawat jalan. Pertanyaan: Dalam kajian Anda, apakah episode rawat jalan yang tidak memiliki resume medis berada di luar kajian, ataukah dokumen padanannya dikaji sebagai pengganti resume medis? Jawaban \"belum dapat diputuskan sebelum tim atau RSIA menjawab butir 4\" juga sah." Opsi: Di luar kajian | Dokumen padanan dikaji | Belum dapat diputuskan. Jawaban teks bebas pengguna (verbatim, bukan salah satu opsi): "Rawat jalan juga semua harusnya ada resume medisnya karena jika tidak tidak bisa klaim bpjs". Tidak menetapkan batas operasional rawat jalan: penanda #28 tetap [MENUNGGU KEPUTUSAN]; Q-TEAM butir 4 dan butir ini tetap terbuka.'
```

```yaml
id: Q-B1-g
question: "Laporan utama capstone" yang dirujuk Bab I tidak ada di repo; di mana berkasnya, atau rujukan diganti Penyelarasan?
affected: [Bab I]
class: L3
pic: Pengguna
ask_to: Tim
status: TERBUKA
updated: 2026-11-06
refs: [F-A08-0005]
```

```yaml
id: Q-B1-h
question: Apakah satuan keputusan Q2 (rumusan 2 I.2, kejelasan alasan dan rujukan) ditetapkan per kelompok penilai (tenaga ahli dan pengguna proksi terpisah) atau gabungan, dan siapa yang menilai (Q-TEAM butir 7)?
affected: [Bab I, A06, A11]
class: L3
pic: Pengguna
ask_to: Tim
status: MENUNGGU ANGGOTA
updated: 2026-11-06
refs: [D-30, D-28, Q-TEAM, F-A07-0022]
```

## Butir baru dari QA I.2/I.4 DRAF 6 (TSK-040, 2026-11-06)

Semua butir berikut TERBUKA/menunggu; tidak ada yang diputuskan. Sumber: laporan QA TSK-034..039 melalui A01; penggantian F-A07-0037 (INFO).

```yaml
id: Q-B1-i
question: Susunan Bab II mana yang berlaku, DRAFT 6 (bab2/Bab_II_Revisi_Notulensi.md) atau berkas modular II.1-II.8? Asumsi kerja A01 saat ini "DRAFT 6 yang berlaku" (menurut PROJECT_STATE); menunggu konfirmasi pengguna
affected: [Bab II]
class: L4
pic: Pengguna
status: TERBUKA
updated: 2026-11-06
refs: [Q-B1-e]
```

```yaml
id: Q-B1-j
question: Selisih minimum presisi dan recall kombinasi atas masing-masing komponen (D-29) belum ada di daftar Q-TEAM Penyelarasan (butir 8 hanya memuat angka ambang 13 ukuran); perlu diusulkan ke tim
affected: [Bab I, A06]
class: L3
pic: Pengguna
ask_to: Tim
status: MENUNGGU ANGGOTA
updated: 2026-11-06
refs: [D-29, D-22, F-A07-0032, F-A07-0037, F-A09-0075]
```

```yaml
id: Q-B1-k
question: Dampak lintas proposal yang belum diperiksa: (1) Penyelarasan:35 belum memuat pembanding D-22 maupun kriteria D-29 (A06 belum dijalankan); (2) irisan I.4 paragraf 5 / rumusan 2 dengan rumusan 4 Abizzar belum diperiksa. Perlu A06 dan konfirmasi tim
affected: [Bab I, A06]
class: L3
pic: Pengguna
ask_to: Tim
status: MENUNGGU ANGGOTA
updated: 2026-11-06
refs: [D-22, D-29, D-30, Q-B1-j, F-A06-0001]
```

## Butir baru dari penulisan I.3 DRAF 7 (TSK-047, 2026-11-06)

Semua butir TERBUKA/menunggu. D-31 hanya memutuskan redaksi tujuan utama; ketiga butir ini tidak diputuskan olehnya.

```yaml
id: Q-B1-l
question: Skala penilaian kejelasan alasan dan rujukan serta cara merangkum nilainya belum diputuskan; Penyelarasan:339 hanya menyebut skala sebagai usulan dalam ambang Q-TEAM butir 8
affected: [Bab I]
class: L3
pic: Pengguna
ask_to: Tim
status: MENUNGGU ANGGOTA
updated: 2026-11-06
refs: [D-30, Q-B1-j]
marker: I.3 paragraf 3
```

```yaml
id: Q-B1-m
question: Rujukan maju I.3 paragraf 1 "prosedur pengukurannya diuraikan pada Subbab I.5" harus dipenuhi saat I.5 ditulis atau dihapus
affected: [Bab I]
class: L4
pic: Pengguna
status: TERBUKA
updated: 2026-11-06
refs: [D-31]
```

```yaml
id: Q-B1-n
question: Di mana pengembangan komponen (aturan rule-based dan pemeriksaan AI/NLP berbasis RAG) oleh penulis dijelaskan: paragraf research gap I.1 atau I.5?
affected: [Bab I]
class: L3
pic: Pengguna
status: TERBUKA
updated: 2026-11-06
refs: [D-31, F-A10-0105, D-34]
```

## Butir baru dari QA dan tinjauan kritis I.3 DRAF 7 (TSK-049, 2026-11-06)

D-32 hanya memutuskan bahwa D-29 dipertahankan dan mekanisme ditandai; kelima butir ini tidak diputuskan olehnya.

```yaml
id: Q-B1-o
question: Mekanisme kombinasi rule-based dan AI/NLP berbasis RAG (union, irisan, penyaringan, atau pembentukan bertahap) belum ditetapkan; harus ditetapkan sebelum pengujian dan harus memungkinkan kedua arah hasil (kombinasi lebih tinggi maupun tidak lebih tinggi daripada komponen)
affected: [Bab I, I.2, I.3]
class: L3
pic: Pengguna
ask_to: Tim
status: MENUNGGU ANGGOTA
updated: 2026-11-06
refs: [D-32, D-29, F-A11-0001, F-A05-0001, F-A06-0006]
```

```yaml
id: Q-B1-p
question: Titik ukur kombinasi terhadap rekonsiliasi antarpemeriksaan milik Abizzar (Penyelarasan:183) dan perlakuan temuan ganda
affected: [Bab I, A06]
class: L3
pic: Pengguna
ask_to: Tim
status: MENUNGGU ANGGOTA
updated: 2026-11-06
refs: [D-32, F-A11-0003, F-A06-0006, F-A05-0018]
```

```yaml
id: Q-B1-q
question: Operator ambang ">" (naskah) atau ">=" (tabel Penyelarasan:327-339)
affected: [Bab I, I.2]
class: L3
pic: Pengguna
ask_to: Tim / pembimbing
status: MENUNGGU ANGGOTA
updated: 2026-11-06
refs: [F-A11-0010, F-A06-0007]
```

```yaml
id: Q-B1-r
question: Aturan pencocokan temuan-label, agregasi mikro atau makro, dan perlakuan nilai 0/0 pada presisi dan recall
affected: [Bab I, I.2]
class: L3
pic: Pengguna
ask_to: Tim
status: MENUNGGU ANGGOTA
updated: 2026-11-06
refs: [F-A11-0005, F-A05-0003, Q-A04-d]
```

```yaml
id: Q-B1-s
question: Adakah ringkasan agregat jumlah episode dan sebaran jenis di luar .scratch/rsia/agregat/ yang dapat dirujuk tanpa membuka data RSIA?
affected: [Bab I]
class: L4
pic: Pengguna
status: TERBUKA
updated: 2026-11-06
refs: [Q-A04-c]
```

```yaml
id: Q-B1-t
question: Bagaimana hasil rawat inap dan rawat jalan dilaporkan (terpisah atau gabungan), dan apakah pembanding berupa kondisi saat ini (tanpa sistem) dimasukkan? Sengaja tidak masuk penanda I.5; menunggu keputusan pengguna. Bagian pelaporan (terpisah atau gabungan) DIPUTUSKAN → D-56 (terpisah, 2026-11-08). Bagian pembanding tidak dibahas D-56 (lihat D-22).
affected: [Bab I]
class: L3
pic: Pengguna
status: DIPUTUSKAN → D-56 (bagian pelaporan)
updated: 2026-11-08
refs: [F-A05-0007, F-A05-0014, F-A10-0119, D-56, D-22]
```

```yaml
id: Q-B1-u
question: Apa arti "temuan ganda" (definisi tim; metrik rumusan 3 Abizzar di Penyelarasan) untuk dipakai di I.3? Perlu pengecekan A06 terhadap definisi rumusan a03 yang tanpa atribusi.
affected: [Bab I]
class: L3
pic: Tim
status: MENUNGGU ANGGOTA
updated: 2026-11-06
refs: [F-A07-0048, Q-B1-p, F-A06-0005]
```

## Butir baru dari tinjauan ulang a05/a11, A06 lintas proposal, dan a02 Bab II (TSK-058, 2026-11-06)

Semua butir TERBUKA/menunggu; tidak ada yang diputuskan. Pemilik dokumen anggota belum dikonfirmasi (Q-P2-a); nama anggota di bawah mengikuti Penyelarasan atau nama berkas, bukan fakta terkonfirmasi.

```yaml
id: Q-B1-v
question: Siapa pemilik kejelasan bukti/relevansi, bagaimana peran tenaga ahli versus pengguna proksi (penilai), dan di mana skor kejelasan disimpan (ada tabrakan istilah "penilaian")?
affected: [Bab I, A06]
class: L3
pic: Abizzar
ask_to: Tim
status: MENUNGGU ANGGOTA
updated: 2026-11-06
refs: [F-A06-0003, F-A06-0004, Q-B1-l]
```

```yaml
id: Q-B1-w
question: Siapa pemilik konsistensi antar-entri CPPT di tingkat tim (Penyelarasan:53 tanpa pemilik, rumusan, atau jenis ketidaksesuaian)?
affected: [Bab I, A06]
class: L3
pic: Pengguna
ask_to: Tim
status: MENUNGGU ANGGOTA
updated: 2026-11-06
refs: [F-A06-0010, F-A05-0021, D-25]
```

```yaml
id: Q-B1-x
question: Di mana batas antara penautan ibu-bayi (di luar kajian, D-25) dan aturan pemeriksaan pasangan ibu-bayi yang tercatat milik Danen? Tergantung Q-TEAM butir 1
affected: [Bab I, A06]
class: L3
pic: Pengguna
ask_to: Tim
status: MENUNGGU ANGGOTA
updated: 2026-11-06
refs: [F-A06-0009, D-25, Q-TEAM]
```

```yaml
id: Q-B1-y
question: Bagaimana jawaban "tidak" ditafsirkan mengingat plafon presisi/recall = 1 (D-29 menjadi pasti "tidak") dan apa kondisi keabsahan jawaban (termasuk opsi "tidak dapat disimpulkan")?
affected: [Bab I, I.2, I.3]
class: L3
pic: Pengguna
ask_to: Tim
status: TERBUKA
updated: 2026-11-06
refs: [F-A11-0012, F-A05-0017, F-A05-0020, D-29, D-33, F-A11-0015, Q-B1-bj]
```

```yaml
id: Q-B1-z
question: Nuansa klaim "tidak ada resource CPPT" pada SATUSEHAT di Bab II:87 (narasi perkembangan penyakit dikirim lewat ClinicalImpression, Bab 6 panduan); bagaimana dipakai di Bab I/III?
affected: [Bab I, Bab II, Bab III]
class: L3
pic: Pengguna
status: TERBUKA
updated: 2026-11-06
refs: [B2-48, EVIDENCE_REGISTRY]
```

```yaml
id: Q-B1-aa
question: Konfirmasi pemilik Draft Bab 1 (1) dan apakah ada versi anggota yang lebih baru (dua dokumen anggota tampak usang; tanggal manifest Raihaan Bab I "± 2026-10-20" tidak cocok isinya karena sampul memakai judul baru 30 Okt)
affected: [A06, PROJECT_STATE Team Docs Manifest]
class: L3
pic: Pengguna
ask_to: Tim
status: MENUNGGU ANGGOTA
updated: 2026-11-06
refs: [Q-P2-a, Q-P2-c, F-A06-0014]
```

```yaml
id: Q-B1-ab
question: source/INDEKS.md usang (menyebut folder 01-12, sedangkan struktur kini 01-17); perbarui atau abaikan?
affected: [source/INDEKS.md]
class: L4
pic: A13/Pengguna
status: TERBUKA
updated: 2026-11-06
refs: [TSK-055]
```

## Butir baru dari keputusan D-34 (TSK-060, 2026-11-06)

```yaml
id: Q-B1-ac
question: Permintaan versi modular Bab I dan II (empat berkas di modular/: Bab-I_Editorial, Bab-I, Bab-II_Editorial, Bab-II). build_modular.py membaca master docx resmi bab2/...-Draft-Bab2.docx, BUKAN bab1/Bab_I_Draft.md maupun Markdown Bab II terbaru, sehingga hasil build tidak memuat naskah Bab I DRAF terbaru. Bagaimana dilanjutkan, dan apakah Approval Request build_modular (P2-02) disetujui?
affected: [modular/, bab1, bab2]
class: L2/L3
pic: Pengguna
status: DITUTUP DENGAN ALASAN (disetujui untuk satu eksekusi; keterbatasan sumber tetap berlaku untuk eksekusi berikutnya; jalur docx dari Markdown Bab I belum ada)
updated: 2026-11-06
refs: [P2-02, D-34, TSK-061]
note: Persetujuan operasional P2-02 untuk satu eksekusi dan empat berkas (bukti di TASK_TRACKER TSK-061); bukan keputusan DECISION_LOG dan bukan DIPUTUSKAN.
```

## Butir baru dari penulisan I.5 (TSK-059, 2026-11-06)

```yaml
id: Q-B1-ad
question: Bagaimana cara menilai "lebih tinggi" (I.5) dan apa kondisi keabsahan jawaban? Sebagian (tafsir "tidak" dan keabsahan jawaban) beririsan dengan Q-B1-y; butir ini mencakup cara menilai "lebih tinggi" pada I.5.
affected: [Bab I, I.5]
class: L3
pic: Pengguna
ask_to: Tim
status: MENUNGGU ANGGOTA
updated: 2026-11-06
refs: [F-A11-0006, F-A11-0012, F-A05-0017, Q-B1-y]
```

```yaml
id: Q-B1-ae
question: Versi dokumen mana yang dilabeli dan diuji, dan apakah mode AI/NLP penuh atau inkremental?
affected: [Bab I, I.5]
class: L3
pic: Pengguna
ask_to: Tim
status: MENUNGGU ANGGOTA
updated: 2026-11-06
refs: [F-A11-0004]
```

```yaml
id: Q-B1-af
question: Dua inferensi penulis baru di I.5 perlu dinilai pengguna apakah merupakan keputusan metodologi. (1) Paragraf 4, "data uji tidak dipakai menyusun/menyesuaikan pemeriksaan": turunan Penyelarasan:297 tetapi tidak eksplisit di sana. (2) Paragraf 7.
affected: [Bab I, I.5]
class: L3
pic: Pengguna
status: TERBUKA
updated: 2026-11-06
refs: [TSK-059, D-34]
note: Inferensi penulis (a03), belum disetujui; bukan keputusan.
```

```yaml
id: Q-B1-ag
question: Apakah penilaian kejelasan oleh pengguna proksi berlangsung dalam sesi uji peninjauan yang sama (Penyelarasan:304, :312)?
affected: [Bab I, I.5, A06]
class: L3
pic: Pengguna
ask_to: Tim
status: MENUNGGU ANGGOTA
updated: 2026-11-06
refs: [TSK-059, Penyelarasan:304, Penyelarasan:312, A06]
```

## Butir baru dari kegagalan build modular (TSK-061/063, 2026-11-06)

```yaml
id: Q-B1-ah
question: lxml, LibreOffice, dan pdftotext belum tersedia untuk build_modular (build gagal ModuleNotFoundError lxml, build_modular.py baris 29). Apakah pengguna akan memasangnya (lxml; LibreOffice di C:\Program Files\LibreOffice\program\soffice.exe atau env SOFFICE; pdftotext dan pdfinfo di PATH), dan apakah build diulang dengan Approval Request baru (persetujuan P2-02 untuk satu eksekusi sudah terpakai)?
affected: [modular/, tools/build_modular.py]
class: L4
pic: Pengguna
status: TERBUKA
updated: 2026-11-06
refs: [TSK-061, TSK-063, P2-02, Q-B1-ac]
note: Pemasangan paket dilakukan pengguna, bukan agent. Keempat berkas modular tidak tersentuh.
```

```yaml
id: Q-B1-ai
question: Jalur pembuatan docx modular dari Markdown Bab I belum ada (build_modular tidak membacanya; build_docx.py dan build_with_toc.py dilarang P2-02). Bagaimana jalur itu disediakan?
affected: [modular/, bab1, tools/]
class: L3
pic: Pengguna
status: TERBUKA
updated: 2026-11-07
refs: [TSK-061, P2-02, Q-B1-ac, D-35]
note: D-35 menetapkan penempatan peran (a03 + perbaikan build_modular) tetapi belum menjawab rincian teknis jalur Markdown; tetap TERBUKA (lihat Q-B1-aj..am)
```

## Butir baru dari keputusan D-35 (penempatan peran migrasi ke Docs, 2026-11-07)

```yaml
id: Q-B1-aj
question: Siapa yang boleh mengedit tools/build_modular.py? a03 hanya berwenang menulis bab*/ dan .scratch/**, sedangkan D-35 menugaskan perbaikan skrip itu.
affected: [tools/build_modular.py, write_scopes]
class: L4
pic: Pengguna
status: DIPUTUSKAN → D-36
updated: 2026-11-07
refs: [D-35, D-36, P2-02]
note: D-36 (2026-11-07) memberi a03 wewenang edit khusus tools/build_modular.py; lingkup hanya siapa yang berwenang
```

```yaml
id: Q-B1-ak
question: Bagaimana definisi tiga varian modular (editorial, formal, lengkap) dan format keluaran Google Docs (mis. impor DOCX atau pembuatan langsung)?
affected: [tools/build_modular.py, modular/]
class: L3
pic: Pengguna
status: DIPUTUSKAN → D-38, D-39, D-40, D-41, D-42
updated: 2026-11-07
refs: [D-35, D-38, D-39, D-40, D-41, D-42, Q-B1-ao, Q-B1-ap, Q-B1-aq, Q-B1-ar]
note: D-38 (2026-11-07) menetapkan nama dan makna tiga varian serta keluaran DOCX saja (Google Docs manual oleh pengguna). Sisa terbuka pada butir Q-B1-ao..ar (a-d).
note_2: Progres 2026-11-07 - (b) PDF DIPUTUSKAN D-39 (Q-B1-ap); (d) perakitan varian Lengkap DIPUTUSKAN D-40 (Q-B1-ar). Sisa terbuka: (a) Q-B1-ao (templat dasar) dan (c) Q-B1-aq (penanda editorial).
note_3: Progres 2026-11-07 - (c) Q-B1-aq DIPUTUSKAN D-41. Dari butir (a)-(d) pembuka hanya Q-B1-ao yang tersisa (kedua templat hash identik; dasar templat belum dipilih pengguna). Butir turunan baru dari D-41: Q-B1-as..av.
note_4: Progres 2026-11-07 - (a) Q-B1-ao DIPUTUSKAN D-42. Seluruh butir pembuka (a)-(d) kini terjawab (D-38..D-42); butir ini DIPUTUSKAN. Butir turunan Q-B1-as..av, Q-B1-al, dan Q-B1-am tetap berdiri sendiri dan tidak berubah.
```

```yaml
id: Q-B1-al
question: Apakah AGENT_SPECIFICATIONS/ORCHESTRATION serta hook guard dan check_agents perlu diubah untuk memberi a03 wewenang tambahan sesuai D-35?
affected: [docs/, .claude/]
class: L4
pic: Pengguna
status: TERBUKA
updated: 2026-11-07
refs: [D-35, D-36, Q-B1-aj, Q-B1-an]
note: D-36 menjadikan perubahan AGENT_SPECIFICATIONS, ORCHESTRATION, hook guard, dan check_agents konsekuensi wajib; pelaksanaan dan jalur pengeditnya belum diputuskan (Q-B1-an); tetap TERBUKA
note_2: D-37 (2026-11-07) memutuskan pelaksana perubahan = pengguna atau sesi Claude Code biasa di luar agent. Butir ini tetap TERBUKA sampai perubahan benar-benar diterapkan dan check_agents lolos (belum terjadi saat dicatat).
note_3: D-50 (2026-11-07) menetapkan jalur PDF Formal/Lengkap = di dalam tools/build_modular.py (tanpa izin Bash baru, tanpa perubahan allowlist guard). D-51 membolehkan draf patch memuat aturan ask Edit(./tools/build_modular.py) di .claude/settings.json. Butir tetap TERBUKA sampai perubahan diterapkan; lihat Q-B1-ay dan Q-B1-az.
note_4: Progres 2026-11-07 (TSK-072) - patch final disusun a03 di .scratch/patch_Q-B1-al.md (32 perubahan: 25 SIAP DITERAPKAN, 7 OPSIONAL-BELUM DIKONFIRMASI) tetapi BELUM diterapkan pengguna. Butir OPSIONAL belum dikonfirmasi pengguna. Q-B1-ay DIPUTUSKAN D-52, Q-B1-az DIPUTUSKAN D-53, kriteria audit PDF a12 D-54 (rujuk D-39). Urutan penerapan usulan a03: guard, settings.json, write_scopes.json + AGENT_SPECIFICATIONS §4 serentak lalu check_agents, dokumen dan definisi agent, opsional, check_agents lagi, uji manual T-14/T-30, pencatatan a13. Saran A01 (bukan keputusan): terapkan 25 butir SIAP dulu, pertimbangkan tiga perubahan check_agents belakangan. Tetap TERBUKA.
```

```yaml
id: Q-B1-am
question: Bagaimana nasib D-16 (perbaikan skrip build lama untuk path /home/user/project-proposal dan outline Bab II lama II.1-II.8) setelah D-35 memusatkan build pada build_modular.py?
affected: [tools/, D-16]
class: L3
pic: Pengguna
status: DIPUTUSKAN → D-44
updated: 2026-11-07
refs: [D-35, D-16, D-44, P2-02]
note: D-44 (2026-11-07) - pilihan A01 atas delegasi pengguna ("2-4. lakukan sesuai preferensi anda"; pengguna tidak menyebut opsi), dapat dibatalkan pengguna kapan saja - build_docx.py dan build_with_toc.py tidak diperbaiki, tetap dilarang (P2-02); build_modular.py satu-satunya jalur; penghapusan kedua berkas oleh pengguna di luar sistem. Teks D-16 sebenarnya tentang tools/verify_claims.py (konflik cakupan dicatat, tidak diselesaikan).
```

```yaml
id: Q-B1-an
question: Siapa atau jalur mana yang mengedit docs/AGENT_SPECIFICATIONS.md, docs/ORCHESTRATION_ARCHITECTURE.md, scripts/guard.py (kebijakan), scripts/check_agents.py, dan definisi agent a03, sebagai konsekuensi wajib D-36? Berkas-berkas itu di luar write_scope A01 dan A13; belum ada agent yang berwenang atasnya.
affected: [docs/, scripts/, .claude/]
class: L4
pic: Pengguna
status: DIPUTUSKAN → D-37
updated: 2026-11-07
refs: [D-36, D-37, Q-B1-al, Q-B1-aj]
note: D-37 (2026-11-07) memutuskan perubahan dikerjakan pengguna atau sesi Claude Code biasa di luar agent; lingkup hanya jalur pelaksanaan. Q-B1-al tetap TERBUKA.
```

```yaml
id: Q-B1-ao
question: Apakah "Template-Proposal-IF4091-Capstone-Individu-2026 - Copy.docx" di root identik dengan template/Template-Proposal-IF4091-Capstone-Individu-2026.docx, dan mana yang menjadi dasar skrip (varian Lengkap)?
affected: [tools/build_modular.py, template/]
class: L3
pic: Pengguna
status: DIPUTUSKAN → D-42
updated: 2026-11-07
refs: [D-38, D-42, Q-B1-ak]
note_2: D-42 (2026-11-07) - varian Lengkap merujuk template/Template-Proposal-IF4091-Capstone-Individu-2026.docx; berkas "- Copy" di root tidak dirujuk skrip (nasibnya di luar persetujuan; pengguna memutuskan di luar sistem).
note: A13 menghitung hash sha256 kedua berkas pada 2026-11-07 dan keduanya SAMA (awalan a76030913c40); itu hanya fakta byte, bukan keputusan mana yang menjadi dasar skrip. Isi templat tidak dibaca.
```

```yaml
id: Q-B1-ap
question: Apakah PDF termasuk keluaran skrip? Bab I dan II sudah punya pdf dari migrasi di luar sistem; D-38 hanya menetapkan DOCX.
affected: [tools/build_modular.py, bab1/, bab2/]
class: L3
pic: Pengguna
status: DIPUTUSKAN → D-39
updated: 2026-11-07
refs: [D-38, D-39, Q-B1-ak]
note: D-39 (2026-11-07) - Editorial DOCX saja; Formal dan Lengkap DOCX dan PDF. Cara konversi PDF, izin Bash a03 (Q-B1-al/D-37), dan kriteria audit a12 untuk PDF belum diputuskan.
```

```yaml
id: Q-B1-aq
question: Apa isi tepat penanda atau catatan editorial yang dibawa varian Editorial, dan apa yang harus hilang dari varian Formal?
affected: [tools/build_modular.py, modular/]
class: L3
pic: Pengguna
status: DIPUTUSKAN → D-41
updated: 2026-11-07
refs: [D-38, D-41, D-43, Q-B1-ak, Q-B1-as, Q-B1-at, Q-B1-au, Q-B1-av]
note_d43: D-43 (2026-11-07) mengubah sebagian D-41 - Formal memakai teks pengganti Y dari {{ed:X||cl:Y}} bila ditulis; penanda tanpa pengganti tetap dihapus.
note: D-41 (2026-11-07) - Formal diturunkan dari Editorial dengan menghapus teks tersorot dan penanda berkurung tanpa pengganti; tanpa sintaks baru, satu sumber. Fakta a12 (TSK R5-Q-B1-aq, pengamatan): Editorial memuat 17 catatan tersorot kuning (Bab I:1, II:14 termasuk catatan sitasi, III:1, IV:1) = 3 DATA BELUM TERSEDIA + 9 SESUAIKAN DENGAN BAB I + 4 PERLU VERIFIKASI SUMBER + 1 catatan "Format sitasi sementara" (tak berkurung); Formal tanpa highlight dan tanpa penanda berpola; struktur identik; diff baris-per-baris belum dilakukan. Bukti kerja di .scratch/ed/ dan .scratch/render/.
```

```yaml
id: Q-B1-ar
question: Bagaimana varian Lengkap menggabungkan Bab I-IV dan komponen pelengkap (halaman judul, abstrak, daftar isi, daftar pustaka) sesuai templat?
affected: [tools/build_modular.py, template/]
class: L3
pic: Pengguna
status: DIPUTUSKAN → D-40
updated: 2026-11-07
refs: [D-38, D-40, Q-B1-ak, Q-B1-ao]
note: D-40 (2026-11-07) - isi Bab I-IV dari Markdown bab1/-bab4/, pelengkap berplaceholder jelas; a12 memastikan tidak ada placeholder lolos ke berkas kumpul. Isi tiap komponen pelengkap dan templat acuan (Q-B1-ao) belum diputuskan.
```

```yaml
id: Q-B1-as
question: Apakah penghapusan penanda tanpa pengganti (D-41) dapat menyisakan kalimat tidak utuh atau entri daftar pustaka tidak lengkap di Formal (mis. entri Yang et al., Formal sekarang "dkk." vs Editorial penulis lengkap + penanda), dan siapa serta bagaimana memeriksanya?
affected: [tools/build_modular.py, modular/]
class: L3
pic: Pengguna
status: DIPUTUSKAN → D-45
updated: 2026-11-07
refs: [D-41, D-43, D-45, Q-B1-aq, Q-B1-ak]
note: Usul A01 sebelumnya: a12 memeriksa hasil Formal; a09 bila teks berubah. Entri bisa tidak lengkap karena penanda dihapus tanpa pengganti.
note_2: D-45 (2026-11-07) - pilihan A01 atas delegasi pengguna (tanpa opsi spesifik; dapat dibatalkan): a12 memeriksa Formal hasil build (kalimat dan entri pustaka utuh, tak ada penanda tersisa); a09 ikut bila teks berubah. D-43 (Y dipakai bila ada) mengurangi kasus entri tidak lengkap seperti Yang et al.
```

```yaml
id: Q-B1-at
question: Apakah placeholder templat yang ada di Formal (tanggal sampul "Bandung, <tanggal>", "<jika diperlukan>", "<diisi sesuai sumber yang dirujuk pada bab ini>", "Lampiran A. Contoh Judul Lampiran", teks panduan templat di Bab I dan III) termasuk "siap kumpul" menurut D-38 dan D-40?
affected: [tools/build_modular.py, modular/, template/]
class: L3
pic: Pengguna
status: DIPUTUSKAN → D-46
updated: 2026-11-07
refs: [D-38, D-40, D-41, D-46, Q-B1-aq]
note: Fakta a12 (pengamatan): placeholder itu ada di KEDUA varian (Editorial dan Formal) yang ada sekarang.
note_2: D-46 (2026-11-07) - pilihan A01 atas delegasi pengguna (tanpa opsi spesifik; dapat dibatalkan): placeholder templat di Formal dilaporkan a12 sebagai temuan ringan, tidak memblokir; hanya Lengkap gagal bila placeholder tersisa (D-40).
```

```yaml
id: Q-B1-au
question: Apa aturan deteksi catatan editorial tak berkurung seperti "Format sitasi sementara" agar ikut terhapus dari Formal (pencarian penanda berpola tidak menjaringnya)?
affected: [tools/build_modular.py, modular/]
class: L3
pic: Pengguna
status: DIPUTUSKAN → D-47
updated: 2026-11-07
refs: [D-41, D-47, Q-B1-aq]
note: Catatan sitasi itu tersorot kuning di Editorial; D-41 menyebut teks tersorot dan penanda berkurung dihapus, tetapi aturan deteksi untuk kasus tak berkurung belum ditetapkan.
note_2: D-47 (2026-11-07) - pilihan A01 atas delegasi pengguna (tanpa opsi spesifik; dapat dibatalkan): skrip menghapus teks tersorot dan catatan "Format sitasi sementara" secara eksplisit; a12 memeriksa tak ada sorotan atau kata kunci itu di Formal.
```

```yaml
id: Q-B1-av
question: Apakah berkas Formal yang ada sekarang di modular/ dibangun ulang dengan skrip (D-41) atau dibiarkan?
affected: [modular/, tools/build_modular.py]
class: L3
pic: Pengguna
status: DIPUTUSKAN → D-48
updated: 2026-11-07
refs: [D-41, D-48, Q-B1-aq, Q-B1-aw, P2-02]
note: Teks Formal hasil skrip akan berbeda dari Formal yang ada sekarang (konsekuensi D-41). Membangun ulang tetap memerlukan persetujuan operasional P2-02 per eksekusi.
note_2: D-48 (2026-11-07) - pilihan A01 atas delegasi pengguna (tanpa opsi spesifik; dapat dibatalkan): Formal yang ada dibangun ulang bila skrip siap, dengan Approval Request P2-02 per eksekusi menyebut berkas modular/ yang ditimpa. Skrip belum siap (Q-B1-aw).
```

```yaml
id: Q-B1-aw
question: Skrip tools/build_modular.py perlu disesuaikan: (i) sumber MASTER, (ii) input Markdown Bab II DRAFT 6 (bab2/Bab_II_Revisi_Notulensi.md) dan Bab I (bab1/Bab_I_Draft.md), (iii) varian Lengkap dari template/, (iv) PDF untuk Formal dan Lengkap. Bagaimana dan oleh siapa?
affected: [tools/build_modular.py, modular/, bab1/, bab2/]
class: L3
pic: Pengguna
status: TERBUKA
updated: 2026-11-07
refs: [D-35, D-36, D-37, D-39, D-40, D-42, D-43, Q-B1-al, Q-B1-ai, Q-B1-ax]
note: Pengamatan A01 dari pembacaan tools/build_modular.py (bukan keputusan; belum diverifikasi A13): (i) skrip bergantung pada MASTER bab2/13523136-...-Draft-Bab2.docx yang tidak ada lagi di disk, jadi belum dapat dijalankan; (ii) skrip hanya membaca Markdown Bab II lama (bab2/Pembuka_Bab_II.md dan II.[0-9]_*.md; outline II.1-II.8), belum Bab_II_Revisi_Notulensi.md (DRAFT 6) dan belum Bab_I_Draft.md; (iii) modular/ Bab II karena itu masih berasal dari outline lama. Wewenang edit a03 (D-36) belum operasional sampai Q-B1-al diterapkan.
note_2: Kemajuan 2026-11-07: D-49 menetapkan input Bab I = bab1/Bab_I_Draft.md; D-50 menetapkan PDF Formal/Lengkap dibuat di dalam skrip. Perlu mencakup: sumber MASTER yang hilang, input DRAFT 6 dan Bab I Markdown, varian Lengkap dari template/, PDF Formal/Lengkap. Tetap TERBUKA.
```

```yaml
id: Q-B1-ax
question: Apakah isi docx sementara di bab1/ dan bab2/ (hasil migrasi LLM lain) dipindahkan ke modular/, dan kapan?
affected: [bab1/, bab2/, modular/]
class: L3
pic: Pengguna
status: TERBUKA
updated: 2026-11-07
refs: [Q-B1-aw, D-48]
note: Bergantung pada hasil audit a12 TSK R5 yang sedang berjalan dan pada Q-B1-aw. Pernyataan pengguna 2026-11-07 (verbatim, konteks dua docx bab2/ yang tidak ditemukan): "semua itu di modular/, yang bab1/ dan bab2/ itu baru sementaranya aja docx dan pdf nya". Artefak resmi ada di modular/; docx/pdf bab1/ dan bab2/ sementara hasil migrasi LLM lain.
note_2: Kemajuan 2026-11-07: D-49 memutuskan sumber Bab I = bab1/Bab_I_Draft.md (DRAF 10). Belum diputuskan: pemindahan Bab II, waktu pemindahan, dan nasib berkas sementara. Tetap TERBUKA.
```

```yaml
id: Q-B1-ay
question: Apakah scripts/selftest.py boleh diubah sebagai bagian patch a03 (usulan a03, di luar daftar berkas D-37)?
affected: [scripts/selftest.py]
class: L3
pic: Pengguna
status: DIPUTUSKAN → D-52
updated: 2026-11-07
refs: [D-37, D-51, D-52, Q-B1-al]
note: Disebut sebagai tidak diputuskan di D-51. D-52 (2026-11-07) - pilihan A01 atas delegasi pengguna ("lakukan sesuai preferensi anda"; tanpa opsi spesifik; dapat dibatalkan): selftest.py tidak diubah sekarang; uji manual T-14 dan T-30 setelah patch diterapkan.
```

```yaml
id: Q-B1-az
question: Apakah audit a12 atas perubahan D-36 mencakup diff tools/build_modular.py (kartu A12 tidak memuat tools/ dalam akses bacanya)?
affected: [.claude/agents/, tools/build_modular.py]
class: L3
pic: Pengguna
status: DIPUTUSKAN → D-53
updated: 2026-11-07
refs: [D-36, D-51, D-53, Q-B1-al]
note: Disebut sebagai tidak diputuskan di D-51. D-53 (2026-11-07) - pilihan A01 atas delegasi pengguna ("lakukan sesuai preferensi anda"; tanpa opsi spesifik; dapat dibatalkan): a12 hanya mengaudit berkas hasil build; diff skrip ditinjau pengguna lewat prompt ask per edit (D-51); akses baca a12 tidak diperluas ke tools/.
```

## Butir baru dari revisi I.4 DRAF 11, QA siklus 0, dan pernyataan pengguna (TSK-075..077, 2026-11-08)

```yaml
id: Q-B1-ba
question: Bagaimana konflik sumber tentang penguncian CPPT dan resume medis diselesaikan? Penyelarasan (baris 17, 84; Q-TEAM butir 5) dan naskah (I.1 p12, p14; I.4 p6 "kedua dokumen dikunci") mengandaikan keduanya terkunci, sedangkan klarifikasi RSIA yang disampaikan pengguna 2026-11-08 menyatakan CPPT tidak dapat diubah, resume medis masih dapat diubah (koreksi langsung jarang), dan melarang asumsi keduanya terkunci permanen.
affected: [Bab I, I.1, I.4, Penyelarasan]
class: L3
pic: Pengguna
ask_to: Tim / RSIA mitra
status: MENUNGGU ANGGOTA
updated: 2026-11-08
refs: [D-55, D-56, D-57, D-21, D-24, D-27, F-A05-0024, F-A07-0051, F-A11-0004, Q-B1-ae, Q-TEAM butir 5, Q-B1-bb, Q-B1-bc]
note: KONFLIK SUMBER, tidak diselesaikan A13. Status pernyataan pengguna 2026-11-08 (jawaban teks bebas atas AskUserQuestion "I.4 paragraf 6"; pengguna TIDAK memilih satu pun dari tiga opsi A01: kembalikan ke batas kesimpulan saja / pertahankan batas kajian dan putuskan / tunda dengan penanda): klarifikasi pihak RSIA yang disampaikan tidak langsung (sumber dan waktu tidak disebut; belum ada di dokumen Penyelarasan). BUKAN keputusan; tidak mengubah D-55, D-56, D-21; paragraf 6 I.4 tidak diputuskan; tidak boleh diatribusikan di naskah (D-24, D-27) tanpa keputusan baru. Pengguna sendiri meminta "jangan langsung mengubah keputusan atau memperluas ruang lingkup proposal".
user_statement_verbatim: "Teman-teman, ada klarifikasi tambahan dari pihak RSIA terkait alur dokumentasi medis yang perlu kita perhatikan dalam penyelarasan proposal.Beberapa hal yang sudah dikonfirmasi:1. **CPPT tidak dapat diubah setelah dicatat.** Informasi ini sudah diklarifikasi sebelumnya, sehingga tidak perlu ditanyakan kembali.2. **Resume medis masih dapat diubah.** Namun, koreksi langsung terhadap resume relatif jarang dilakukan. Jika ditemukan ketidaksesuaian, pihak rumah sakit biasanya memberikan klarifikasi atau penjelasan mengenai dokumentasi tersebut.Implikasinya, kita perlu membedakan antara temuan audit yang membutuhkan klarifikasi dan temuan yang memang memerlukan koreksi. Tidak semua temuan harus otomatis dianggap sebagai kesalahan yang wajib diperbaiki.Untuk penyelarasan proposal, mohon perhatikan beberapa hal berikut:- Fokus penelitian tetap pada kesiapan dokumen sebelum klaim BPJS diajukan.- Audit perlu ditempatkan dalam alur penyusunan dan pemeriksaan resume medis sebelum pengajuan klaim.- Jangan menggunakan asumsi bahwa CPPT dan resume medis sama-sama terkunci secara permanen.- Informasi bahwa CPPT tidak dapat diubah, sedangkan resume medis masih dapat diubah, perlu tercermin secara tepat dalam uraian proses bisnis dan batasan penelitian.Masih ada beberapa hal yang perlu kita pastikan:1. Kapan resume medis pertama kali disusun dalam alur pelayanan?2. Pada tahap mana audit dilakukan?3. Bagaimana mekanisme tindak lanjut jika ditemukan ketidaksesuaian antara CPPT dan resume medis?4. Data historis apa yang tersedia untuk pengujian: resume versi pertama, versi akhir, atau riwayat perubahan?Explore juga C:\\Users\\HYPE R Series\\worktrees\\project-proposal-setup\\Penyelarasan Pemahaman Capstone.md karena itu dari client yang mungkin saja jawabannya terlampir disana.Mohon jangan langsung mengubah keputusan atau memperluas ruang lingkup proposal berdasarkan klarifikasi ini. Kita perlu menyelaraskan temuan tersebut dengan keputusan yang sudah disepakati dan mencatat hal-hal yang masih memerlukan konfirmasi."
note_2: Pemeriksaan A01 (bukan A13) atas Penyelarasan terhadap konflik ini (dilaporkan A01; belum diverifikasi A13 ke berkas): baris 17 ("CPPT dan resume dikunci setelah layanan selesai"), baris 84 dan Q-TEAM butir 5 ("CPPT dan resume yang sudah terkunci") mengandaikan keduanya terkunci. Butir Q-TEAM 5 (prosedur membuka kembali CPPT dan resume terkunci) berstatus "Perlu ditanyakan". Kemajuan 2026-11-08 (siklus 1 DRAF 12, laporan A01/a05, belum diverifikasi A13 ke berkas): paragraf 6 sudah mengikuti D-57 dan memuat penanda #33 yang merujuk arti penguncian I.1 p14 (F-A07-0051 RESOLVED oleh a07), tetapi I.1 baris 75 dan 89 ("CPPT dan resume medis dikunci setelah pelayanan selesai"; premis kedua "sebelum CPPT dan resume medis dikunci") masih mengandaikan keduanya dikunci, bertentangan dengan arah klarifikasi RSIA; I.1 tidak diubah (menunggu keputusan). Status tetap MENUNGGU ANGGOTA. Konflik juga menyentuh F-A05-0024 (arti penguncian belum diketahui) dan F-A07-0051 (p6 belum dikaitkan dengan penanda arti penguncian di I.1 p14).
```

```yaml
id: Q-B1-bb
question: Bagaimana jawaban atas empat pertanyaan pengguna 2026-11-08 diperoleh? (1) Kapan resume medis pertama kali disusun dalam alur pelayanan? (2) Pada tahap mana audit dilakukan? (3) Bagaimana mekanisme tindak lanjut bila ditemukan ketidaksesuaian CPPT-resume? (4) Data historis apa yang tersedia untuk pengujian (resume versi pertama, versi akhir, atau riwayat perubahan)?
affected: [Bab I, I.1, I.4, I.5]
class: L3
pic: Pengguna
ask_to: Tim / RSIA mitra
status: MENUNGGU ANGGOTA
updated: 2026-11-08
refs: [Q-B1-ba, Q-B1-ae, F-A11-0004, F-A07-0050, D-55, Q-TEAM butir 5]
note: Satu butir untuk empat pertanyaan (bukan empat butir), karena jawabannya bersumber sama (tim/RSIA) dan saling bergantung. Hasil pemeriksaan A01 atas Penyelarasan (dibaca A01 2026-11-08; belum diverifikasi A13), hanya fakta teks: (1) TIDAK terjawab; hanya baris 17 (wawancara Direktur RSIA, September 2026) "resume medis disusun ulang secara manual pada akhir masa rawat" dan baris 280 "resume baru bermakna setelah resume ada". (2) TIDAK terjawab untuk RSIA; baris 17 menyebut pemeriksaan kesiapan dokumen masih manual; yang ada hanya jadwal pemeriksaan SISTEM (baris 56, 280). (3) TIDAK terjawab untuk RSIA; baris 21, 130, 142 hanya alur sistem; Q-TEAM butir 5 "Perlu ditanyakan". (4) TIDAK terjawab; baris 61, 290, 297 hanya "data terdeidentifikasi, izin diperoleh, jumlah kasusnya mencukupi, dibagi per pasien"; versi pertama/akhir/riwayat perubahan tidak disebut. Pertanyaan 4 beririsan dengan Q-B1-ae (versi dokumen pada data uji).
```

```yaml
id: Q-B1-bc
question: Bagaimana rumusan I.4 paragraf 6 diputuskan (kembali ke batas kesimpulan saja, pertahankan batas kajian, atau tunda dengan penanda)? Rumusan DRAF 11 ("batas kajian"; dokumen terkunci "tidak termasuk kajian") melampaui lingkup D-55 (hanya batas kesimpulan).
affected: [Bab I, I.4 p6, I.5 p2]
class: L3
pic: Pengguna
ask_to: Tim / RSIA mitra
status: DIPUTUSKAN → D-57
updated: 2026-11-08
refs: [D-57, D-55, F-A07-0050, F-A05-0023, F-A05-0024, F-A07-0051, F-A04-0012, Q-B1-ba, Q-B1-ae]
note: Rumusan p6 adalah akibat brief A01 pada R1, bukan keputusan pengguna; tetap dalam DRAF 11 sampai ada keputusan. Pengguna 2026-11-08 menjawab AskUserQuestion "I.4 paragraf 6" dengan teks bebas, tidak memilih opsi (lihat Q-B1-ba). Tidak ada keputusan baru dicatat pada saat itu.
note_2: DIPUTUSKAN → D-57 (2026-11-08, pilihan "Batas kesimpulan saja (Rekomendasi)"), hanya untuk rumusan paragraf 6. Arti penguncian (Q-B1-ba), data uji (F-A11-0004, Q-B1-ae), dan Q-B1-bd tetap terbuka. F-A07-0050, F-A05-0023, F-A05-0024 tetap OPEN sampai auditor penemu menyatakan lain.
```

```yaml
id: Q-B1-bd
question: Bagaimana I.2 (aturan jawaban p6-p7), I.3, I.5, dan ringkasan batas I.2 p8 diselaraskan dengan D-56 (pelaporan rawat inap dan rawat jalan terpisah) dan D-55, termasuk syarat D-29/ambang per jenis perawatan?
affected: [Bab I, I.2, I.3, I.5]
class: L3
pic: Pengguna
ask_to: Tim / RSIA mitra
status: DIPUTUSKAN → D-58 (hanya bentuk jawaban)
updated: 2026-11-08
refs: [D-58, D-56, D-55, D-29, D-21, F-A07-0049, F-A07-0053, F-A05-0025, F-A05-0026, F-A05-0027, F-A05-0028, F-A05-0029, F-A05-0032, F-A04-0013]
note_2: Diperluas 2026-11-08 (siklus 1 DRAF 12): butir turunan F-A05-0032 (cakupan pertanyaan I.2 terikat batas kajian vs batas kesimpulan D-57/D-55 yang lebih sempit; lokasi I.4 p6, I.2 p8, I.5 p2). Status tetap terbuka.
note: Auditor DRAF 11 siklus 0 melaporkan aturan jawaban I.2/I.3 masih tunggal sedangkan I.4 p7 sudah memisahkan kesimpulan per jenis perawatan; syarat D-29 per jenis perawatan belum diatur. F-A05-0026 bagian (b) bergantung pada kutipan Penyelarasan:279 yang a05 ambil dari konteks, belum diverifikasi a05. Belum ada keputusan; naskah I.2, I.3, I.5 tidak diubah pada R1.
```

```yaml
id: Q-B1-be
question: Apakah usulan a03 atas F-A04-0010 (batas dokumen "atau padanannya" pada I.4 p2 dan p4) dan F-A04-0013 (batas jenis ketidaksesuaian dan ketergantungan pada label tenaga ahli) diterapkan?
affected: [Bab I, I.4]
class: L3
pic: Pengguna
ask_to: Tim / RSIA mitra
status: MENUNGGU ANGGOTA
updated: 2026-11-08
refs: [F-A04-0010, F-A04-0013, F-A07-0052, F-A05-0027, Q-B1-f, Q-TEAM butir 1, Q-TEAM butir 4]
note: Usulan a03 belum diterapkan; menunggu keputusan. Terkait batas rawat jalan (Q-B1-f) dan daftar jenis ketidaksesuaian (Q-TEAM butir 1).
```

```yaml
id: Q-B1-bf
question: Verifikasi halaman Permenkes 26/2021 hlm. 48-54 yang dirujuk I.4 paragraf 3: siapa memeriksa (usul: a08, tugas baru)?
affected: [Bab I, I.4 p3, source/01_Regulasi]
class: L3
pic: Pengguna
ask_to: Tim / RSIA mitra
status: MENUNGGU ANGGOTA
updated: 2026-11-08
refs: [F-A04-0015, F-A02-0002]
note: Belum diverifikasi siapa pun: a04 (F-A04-0015, INFO), a05, dan a07 juga tidak memeriksa. Usul A01: tugas a08 (sumber PDF resmi tanpa lapisan teks, lihat F-A02-0002). Butir verifikasi, bukan keputusan akademik.
```

```yaml
id: Q-B1-bg
question: Berapa ambang per jenis perawatan (rawat inap, rawat jalan), apa kondisi keabsahan jawaban per stratum (mis. stratum kosong atau kecil), dan berapa selisih minimum pada kriteria D-29, setelah D-58?
affected: [Bab I, I.2, I.3, I.5]
class: L3
pic: Pengguna
ask_to: Tim / RSIA mitra
status: MENUNGGU ANGGOTA
updated: 2026-11-08
refs: [D-58, D-29, D-56, Q-TEAM butir 8, Q-B1-y, Q-B1-ad, Q-B1-j, F-A05-0026, F-A11-0015, F-A05-0034, F-A11-0016, F-A11-0017, Q-A04-c, Q-B1-bj]
note: Tidak diputuskan D-58. Menurut catatan A01, membutuhkan Approval Request lanjutan dan pembahasan tim. Butir turunan dari Q-B1-bd.
```

```yaml
id: Q-B1-bh
question: Apakah tim dan pembimbing menyetujui bahwa tiap pertanyaan penelitian menghasilkan dua jawaban terpisah (rawat inap dan rawat jalan), padahal rumusan 1 di Penyelarasan:35 memuat satu jawaban ya/tidak per rumusan capstone?
affected: [Bab I, I.2, I.3, Penyelarasan]
class: L3
pic: Pengguna
ask_to: Tim / Pembimbing
status: MENUNGGU ANGGOTA
updated: 2026-11-08
refs: [D-58, D-56, D-22, F-A06-0001, Q-B1-k, F-A05-0037, F-A07-0054]
note: D-58 mengubah arti jawaban rumusan capstone, sehingga perlu pembahasan dengan tim/pembimbing (catatan A01). Bukan keputusan; D-58 berlaku sebagai keputusan pengguna untuk proposal individu ini sampai ada hasil pembahasan.
```

```yaml
id: Q-B1-bi
question: Bagaimana cakupan pertanyaan I.2 (seluruh masa prapengajuan) diselaraskan dengan batas kesimpulan I.4 (sebelum penguncian) menurut D-57 dan D-55 (F-A05-0032)?
affected: [Bab I, I.2 p8, I.4 p6, I.5 p2]
class: L3
pic: Pengguna
ask_to: Tim / RSIA mitra
status: MENUNGGU ANGGOTA
updated: 2026-11-08
refs: [F-A05-0032, F-A05-0028, D-57, D-55, D-58, Q-B1-bd, Q-B1-ba]
note: TIDAK diputuskan D-58; butir turunan dari Q-B1-bd. F-A05-0032 tetap OPEN (diturunkan a05 ke LOW pada siklus 2; DRAF 13 menandai penanda Q-B1-bi di naskah).
```

```yaml
id: Q-B1-bj
question: Bagaimana syarat D-29 diberlakukan untuk rawat jalan bila rawat jalan hanya diperiksa dengan satu aturan (Penyelarasan:279), sehingga syarat itu bisa sudah pasti "tidak"? Opsi a11 (F-A11-0015) adalah (a) D-29 tetap dan kepastian "tidak" dinyatakan; (b) AI/NLP mencakup jenis rawat jalan; (c) hanya syarat pertama untuk rawat jalan (menantang D-29/D-58); (d) pertanyaan pertama rawat jalan dinyatakan tidak dapat diuji (menantang D-58).
affected: [Bab I, I.2, I.3, I.5]
class: L3
pic: Pengguna
ask_to: Tim / Pembimbing
status: TERBUKA
updated: 2026-11-08
refs: [F-A11-0015, F-A05-0026, D-29, D-58, D-56, D-21, Q-B1-bg, Q-B1-y]
note: Butir baru dari QA siklus 2 DRAF 13 (TSK-082). Opsi a-d adalah usulan a11, bukan opsi yang ditawarkan ke pengguna; bukan keputusan. Siklus otomatis D-06 habis, sehingga tidak ada revisi otomatis atas butir ini.
```

```yaml
id: Q-B1-bk
question: Bagaimana D-59 ("tanpa pencarian literatur hibrida") ditafsirkan terhadap penanda #13 [PERLU VERIFIKASI SUMBER hibrida] di I.1 p16: keterbatasan permanen atau tugas tertunda?
affected: [Bab I, I.1 p16]
class: L3
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-08
refs: [D-59, F-A07-0062]
note: Butir baru dari QA siklus 1 DRAF 15 (TSK-087..090, dicatat TSK-092). Tafsir D-59 menunggu pengguna; bukan keputusan.
```

```yaml
id: Q-B1-bl
question: Apakah justifikasi kombinasi pemeriksaan LLM dan deterministik hanya keputusan tim/penulis (D-22, D-29) atau harus didukung literatur? Atribusi "pilihan rancangan capstone" ke dokumen tim belum dapat diverifikasi (a08 memeriksa Penyelarasan:55: dua komponen disebut, kata "kombinasi" tidak).
affected: [Bab I, I.1 p16, Penyelarasan]
class: L3
pic: Pengguna
ask_to: Tim
status: TERBUKA
updated: 2026-11-08
refs: [F-A05-0102, F-A05-0112, F-A05-0115, F-A05-0116, F-A07-0063, D-22, D-29, D-59, D-61, D-62]
note: Butir baru dari TSK-090 siklus 1 (dicatat TSK-092). Bukan keputusan. Pembaruan TSK-093 (siklus 2 DRAF 16): a05 menemukan F-A05-0116 (dasar kombinasi "rancangan capstone dan rumusan I.2" melingkar dan mendahului butir ini; F-A05-0112 dan 0115 RESOLVED menurut a05); a07 menemukan F-A07-0063 (persetujuan pembimbing tertunda, Q-TEAM butir 9). F-A05-0102 RESOLVED bila pengguna mengesahkan rumusan dasar kombinasi. a07 dan a05 berbeda menilai paragraf 18; tidak diselesaikan. Pembaruan TSK-094: DIPUTUSKAN sebagian → D-61 (dasar dan kriteria kombinasi di I.1 p18: ketetapan rumusan capstone Penyelarasan:35 + penalaran penulis berlabel). Bersyarat: a08 memeriksa dukungan literatur Bab II lebih dulu (TSK-095); revisi p18 belum dijalankan; persetujuan pembimbing tetap tertunda (Q-TEAM butir 9). Status temuan F-A05-0102, F-A05-0116, F-A07-0063 tidak diubah (hanya auditor penemu). Status butir tetap TERBUKA (sebagian). Pembaruan TSK-096 (DRAF 17): a03 menerapkan D-61 (TSK-086 terarah, p18-p19, penanda 47); a08 (TSK-095, TSK-087 terarah) PASS_WITH_NOTES: P1 parsial (Zeba), P2 parsial dan tidak searah, P3 kekosongan; menurut auditor penemu RESOLVED: F-A05-0102, F-A05-0116, F-A07-0063. Persetujuan pembimbing tetap tertunda (Q-TEAM butir 9). Tantangan baru atas D-61: Q-B1-bp, Q-B1-bq. Status butir tetap TERBUKA (sebagian). Pembaruan TSK-097: D-62 mengubah sebagian D-61 (klaim "diuji" dibatasi pada keunggulan menurut D-29; lihat Q-B1-bp); Q-B1-bq belum diputuskan.
```

```yaml
id: Q-B1-bm
question: Pembanding pemeriksaan manual di I.1 (:79) terhadap D-22: Skrabic dkk. (II.5:152) membandingkan dengan dokter. Apakah D-22 ditinjau ulang atau dipertahankan?
affected: [Bab I, I.1, D-22]
class: L3
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-08
refs: [F-A05-0109, D-22, D-60]
note: F-A05-0109 menantang D-22 (diperkuat II.5:152). D-60 tidak memutuskan butir ini. Bukan keputusan.
```

```yaml
id: Q-B1-bn
question: Bagaimana II.5/II.6 diselaraskan dengan fakta yang dipakai di Bab I DRAF 16 tetapi belum ada di Bab II (Zeba Tabel 9/kosinus hlm. 8, Skrabic skala 1-4 hlm. 3 dan rincian "mutu rekomendasi", Li Tabel 1 hlm. 5, metode ekstraksi proposisi Zeba hlm. 7)?
affected: [Bab II II.5, Bab II II.6, Bab I I.1]
class: L3
pic: Pengguna
ask_to: Penulis Bab II (a03)
status: TERBUKA
updated: 2026-11-08
refs: [F-A07-0061, F-A05-0117, F-A05-0120]
note: Butir baru dari QA siklus 2 DRAF 16 (TSK-087..090, dicatat TSK-093). Bukan keputusan. Siklus otomatis D-06 habis.
```

```yaml
id: Q-B1-bo
question: Singkatan LLM di I.5 p4 (F-A09-0126) di luar write scope a03 pada TSK-086; siapa dan kapan memperbaikinya?
affected: [Bab I, I.5 p4]
class: L2
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-08
refs: [F-A09-0126]
note: Butir baru dari TSK-089 siklus 2 (dicatat TSK-093). LOW. Bukan keputusan.
```

```yaml
id: Q-B1-bp
question: Apakah klaim "potensi saling melengkapi diuji" di I.1 p18 dipertahankan, dibatasi pada keunggulan menurut D-29, atau diberi ukuran tambahan (uji D-29 tidak mengoperasionalkan saling melengkapi; union dapat menaikkan recall tetapi menurunkan presisi)?
affected: [Bab I, I.1 p18, I.2, I.5]
class: L3
pic: Pengguna
ask_to: Pengguna
status: DIPUTUSKAN → D-62
updated: 2026-11-09
refs: [F-A05-0121, F-A07-0065, D-29, D-61, D-62]
note: Butir baru dari TSK-090 terarah DRAF 17 (dicatat TSK-096). F-A05-0121 menantang D-61 (requires_decision). Pembaruan TSK-097: pengguna memilih "Batasi ke keunggulan menurut D-29" → D-62 (mengubah sebagian D-61). Revisi p18-19 dikerjakan TSK-098 (a03, DRAF 18, COMPLETE; pembaruan TSK-099: F-A05-0121 dan F-A07-0065 RESOLVED menurut auditor penemu; tantangan baru F-A05-0127 lihat Q-B1-bs). Status F-A05-0121 dan F-A07-0065 tidak diubah (hanya auditor penemu).
```

```yaml
id: Q-B1-bq
question: Apa satu makna "konteks informasi dalam dokumen" di I.1 p18 dan bagaimana hubungannya dengan RAG yang mengambil dokumen acuan (makna bergeser tiga kali menurut a05)?
affected: [Bab I, I.1 p18]
class: L3
pic: Pengguna
ask_to: Pengguna
status: DIPUTUSKAN → D-63
updated: 2026-11-09
refs: [F-A05-0122, F-A05-0128, D-61, D-63]
note: Butir baru dari TSK-090 terarah DRAF 17 (dicatat TSK-096). F-A05-0122 menantang D-61 (requires_decision). Bukan keputusan. Pembaruan TSK-099 (DRAF 18): ditambah F-A05-0128 ("eksplisit" menurut Dietrich = kesalahan jelas vs "kondisi yang dapat dirumuskan secara eksplisit" pada kriteria D-61; MEDIUM, requires_decision, sejenis 0122). Pertanyaan diperluas: satu makna "konteks" (F-A05-0122) dan satu makna "eksplisit" (F-A05-0128) dipakai dan dinyatakan menurut pengguna. Pembaruan TSK-100: pengguna memilih "Nyatakan istilah sumber berbeda" → D-63 (kriteria D-61 tidak diubah). Revisi di TSK-101 (a03, berjalan, hasil belum ada). Status F-A05-0122 dan F-A05-0128 tidak diubah (hanya auditor penemu).
```

```yaml
id: Q-B1-br
question: Apakah a03 diberi izin menulis I.2 p2 dan I.5 p4 untuk menyelaraskan singkatan AI, NLP, RAG, LLM dengan I.1 p18 (a03 tanpa izin menulis I.2; I.5 p4 juga menyangkut Q-B1-bo)?
affected: [Bab I, I.2 p2, I.5 p4]
class: L2
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-09
refs: [F-A09-0154, F-A09-0126, Q-B1-bo]
note: Butir baru dari TSK-089 terarah DRAF 17 (dicatat TSK-096). LOW, lintas bagian. Bukan keputusan.
```

```yaml
id: Q-B1-bs
question: Apakah kata "secara langsung" di kalimat I.1 p18 (menurut D-62, potensi saling melengkapi tidak diukur langsung) dihapus atau dipertahankan, mengingat a05 menilai kata itu menyiratkan potensi saling melengkapi diukur secara tidak langsung?
affected: [Bab I, I.1 p18]
class: L3
pic: Pengguna
ask_to: Pengguna
status: DIPUTUSKAN → D-64
updated: 2026-11-09
refs: [F-A05-0127, D-62, D-64]
note: Butir baru dari TSK-090 terarah ketiga DRAF 18 (dicatat TSK-099). F-A05-0127 (LOW, requires_decision) menantang D-62. Pembaruan TSK-100: pengguna memilih "Hapus 'secara langsung'" → D-64 (mengubah sebagian D-62). Revisi di TSK-101 (berjalan). Status F-A05-0127 tidak diubah (hanya auditor penemu).
```

```yaml
id: Q-B1-bt
question: Apakah alasan jawaban "tidak" yang tidak informatif di I.1 p18 dilengkapi dengan struktur syarat D-29 (a05 menilai alasan itu ditempatkan pada mekanisme yang belum ditetapkan, padahal sumbernya struktur syarat D-29)?
affected: [Bab I, I.1 p18]
class: L3
pic: Pengguna
ask_to: Pengguna
status: DIPUTUSKAN → D-65
updated: 2026-11-09
refs: [F-A05-0129, F-A07-0065, D-29, D-62, D-65]
note: Butir baru dari TSK-090 terarah ketiga DRAF 18 (dicatat TSK-099). Kalimat tentang alasan jawaban "tidak" adalah penalaran a03 atas permintaan A01 (berdasar rekomendasi a07 F-A07-0065), BUKAN isi D-62 (koreksi A01 atas brief ke a05). Pembaruan TSK-100: pengguna memilih "Lengkapi dengan struktur syarat D-29" → D-65. Revisi di TSK-101 (berjalan). Status F-A05-0129 tidak diubah (hanya auditor penemu). Pembaruan TSK-102: a03 menyelesaikan DRAF 19 (COMPLETE); F-A05-0129 RESOLVED menurut a05; F-A05-0127, 0128 juga RESOLVED menurut a05 (Q-B1-bs, Q-B1-bq).
```

```yaml
id: Q-B1-bu
question: Bagaimana menangani F-A05-0130 di I.1 p18-p19 (istilah Dietrich "penafsiran kontekstual" hlm. 100 tidak dibedakan; "perbandingan hati-hati" diumumkan tetapi tidak dijalankan; menantang D-63)?
affected: [Bab I, I.1 p18-p19]
class: L3
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-09
refs: [F-A05-0130, D-63]
note: Butir baru dari TSK-090 terarah keempat DRAF 19 (dicatat TSK-102). requires_decision true. Bukan keputusan.
```

```yaml
id: Q-B1-bv
question: Bagaimana menangani F-A05-0131 di I.1 p18 (keadaan ketiga berjawab "tidak": saling melengkapi tetapi kenaikan presisi atau recall di bawah selisih minimum D-29; makna "saling melengkapi" bergeser dari jenis pemeriksaan ke hasil presisi dan recall; menantang D-65)?
affected: [Bab I, I.1 p18]
class: L3
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-09
refs: [F-A05-0131, D-65, D-29]
note: Butir baru dari TSK-090 terarah keempat DRAF 19 (dicatat TSK-102). requires_decision true. Bukan keputusan.
```

```yaml
id: Q-B1-bw
question: Kriteria pemilihan kombinasi tidak dapat diperiksa oleh penelitian maupun literatur setelah D-62 dan D-63 (F-A05-0132); apa konsekuensinya bagi simpulan Bab V, dan apakah hal itu dinyatakan terbuka sebagai motivasi rancangan?
affected: [Bab I, I.1 p18-p19, Bab V]
class: L3
pic: Pengguna
ask_to: Pembimbing
status: TERBUKA
updated: 2026-11-09
refs: [F-A05-0132, D-62, D-63]
note: Butir baru dari TSK-090 terarah keempat DRAF 19 (dicatat TSK-102). requires_decision true; pic Pengguna, ask_to Pembimbing menurut brief A01. Bukan keputusan.
```
