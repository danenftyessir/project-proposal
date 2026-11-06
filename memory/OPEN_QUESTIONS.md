---
file: OPEN_QUESTIONS
revision: 6
status: CURRENT
updated: 2026-11-06
updated_by: a13-memory-manager
based_on_commit: fee9a61
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
updated: 2026-11-05
refs: []
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
updated: 2026-11-05
refs: []
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
refs: [F-A04-0007]
```

```yaml
id: Q-A04-b
question: Apakah rumusan individual mengambil bagian rumusan 4 (kejelasan alasan dan rujukan)?
affected: [Bab I]
class: L3
pic: Pengguna
status: TERBUKA
updated: 2026-11-06
refs: []
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
