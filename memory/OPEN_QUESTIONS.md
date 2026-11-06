---
file: OPEN_QUESTIONS
revision: 21
status: CURRENT
updated: 2026-11-07
updated_by: a13-memory-manager
based_on_commit: b05a2e3
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
updated: 2026-11-06
refs: [D-19]
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
updated: 2026-11-06
refs: [D-21, Q-TEAM, F-A07-0019]
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
question: Bagaimana hasil rawat inap dan rawat jalan dilaporkan (terpisah atau gabungan), dan apakah pembanding berupa kondisi saat ini (tanpa sistem) dimasukkan? Sengaja tidak masuk penanda I.5; menunggu keputusan pengguna.
affected: [Bab I]
class: L3
pic: Pengguna
status: TERBUKA
updated: 2026-11-06
refs: [F-A05-0007, F-A05-0014, F-A10-0119]
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
refs: [F-A11-0012, F-A05-0017, F-A05-0020, D-29, D-33]
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
status: DIPUTUSKAN SEBAGIAN → D-38, D-39, D-40
updated: 2026-11-07
refs: [D-35, D-38, D-39, D-40, Q-B1-ao, Q-B1-ap, Q-B1-aq, Q-B1-ar]
note: D-38 (2026-11-07) menetapkan nama dan makna tiga varian serta keluaran DOCX saja (Google Docs manual oleh pengguna). Sisa terbuka pada butir Q-B1-ao..ar (a-d).
note_2: Progres 2026-11-07 - (b) PDF DIPUTUSKAN D-39 (Q-B1-ap); (d) perakitan varian Lengkap DIPUTUSKAN D-40 (Q-B1-ar). Sisa terbuka: (a) Q-B1-ao (templat dasar) dan (c) Q-B1-aq (penanda editorial).
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
```

```yaml
id: Q-B1-am
question: Bagaimana nasib D-16 (perbaikan skrip build lama untuk path /home/user/project-proposal dan outline Bab II lama II.1-II.8) setelah D-35 memusatkan build pada build_modular.py?
affected: [tools/, D-16]
class: L3
pic: Pengguna
status: TERBUKA
updated: 2026-11-07
refs: [D-35, D-16, P2-02]
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
status: TERBUKA
updated: 2026-11-07
refs: [D-38, Q-B1-ak]
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
status: TERBUKA
updated: 2026-11-07
refs: [D-38, Q-B1-ak]
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
