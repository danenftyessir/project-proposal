---
file: OPEN_QUESTIONS
revision: 59
status: CURRENT
updated: 2026-11-12
updated_by: a13-memory-manager
based_on_commit: 5f5d4b9
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
status: DIPUTUSKAN → D-113
closed_reason: 'APA sementara (konfirmasi tim/pembimbing/prodi belum ada). Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
refs: [D-11, F-A08-0004, F-A08-0005, F-A08-0013, D-80]
note_2026-11-09: 'USUL PENGGUNA APA (D-80, lingkup terbatas; BUKAN keputusan final): menunggu tim dan pembimbing; konfirmasi pedoman prodi tetap diperlukan; naskah belum diubah. Fakta (laporan A01/a10 TSK-115, PARTIAL, qa BLOCKED; belum diverifikasi A13 ke berkas): templat tidak menetapkan gaya sitasi/format Daftar Pustaka di teks badan, hanya empat contoh entri penulis-tahun alfabetis tanpa nomor, tidak dilabeli aturan; draf Bab II Abizzar (hlm. 8-9, 20-22, dibaca A01) memakai APA adaptasi Indonesia; draf Raihaan belum diperiksa; pedoman prodi di luar templat tidak dicari. Pengamatan a10: templat tidak konsisten internal (acuan "Gambar I.1/Tabel I.1" vs keterangan "II.1").'
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
updated: 2026-11-09
refs: []
note_2026-11-09: 'Fakta saja (tidak ditanyakan ke pengguna; pemutus resmi pembimbing, PIC Abizzar, Penyelarasan butir 9 "Belum dibahas"; dilaporkan A01, belum diverifikasi A13 ke berkas): Penyelarasan baris 15 dan 288 menetapkan judul baru "Pengembangan Sistem Pemeriksaan Kesesuaian CPPT dan Resume Medis Berbasis Aturan dan AI untuk Mendukung Kesiapan Klaim BPJS" (menunggu persetujuan pembimbing). Draf Abizzar 21 Oktober 2026 masih memakai judul capstone lama "Perancangan Antarmuka User-Centered untuk Sistem Pemeriksaan Resume Medis dalam Mendukung Kesiapan Klaim BPJS" dan judul individu Abizzar "Pengelolaan Siklus Hidup Temuan pada Sistem Pemeriksaan Resume Medis dalam Mendukung Kesiapan Klaim BPJS". Draf individu pengguna tidak diubah. Tetap MENUNGGU PEMBIMBING.'
note_D-92: 'Pembaruan 2026-11-09 (TSK-142): pengguna memilih "Pakai judul baru dari dokumen penyelarasan, ditandai usulan" → D-92 (lingkup terbatas; BUKAN persetujuan pembimbing). Bab I memakai judul baru sebagai usulan; K2 TETAP MENUNGGU PEMBIMBING (tidak diputuskan).'
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
updated: 2026-11-09
refs: []
note_D-115: '(D-115 kini SUPERSEDED sebagian oleh D-118, hanya untuk perubahan Bab I di 80a13ba; bagian D-115 yang dirujuk di sini tidak terpengaruh. Rujukan dipindah dari refs ke catatan agar S4 tidak salah menandai.) Pembaruan 2026-11-12: D-90, D-91, D-92, D-94, D-97 (rujukan lama butir ini) ditandai SUPERSEDED sebagian oleh D-115 karena teks DRAF 24 digantikan docx resmi; butir tim di Penyelarasan tetap MENUNGGU ANGGOTA.'
note_D-87_97: 'Pembaruan 2026-11-09 (TSK-142): pengguna memutuskan (lingkup terbatas; BUKAN keputusan tim/pembimbing/RSIA) pada beberapa butir yang menyentuh Q-TEAM: butir 4 → D-91 (rawat jalan terbatas = cakupan bersyarat; definisi tetap tidak ada); butir 5 → D-90 (penguncian, satuan episode rawat inap; keterangan RSIA belum terverifikasi); butir 6 → D-97 (satu episode = satu unit, pasangan ibu-bayi tidak dipisah); butir 9 → D-92 (judul baru, ditandai usulan); butir tim lain (F-A11-0023..0027, F-A05-0150) → D-94 (paket usulan penulis). Q-TEAM TETAP MENUNGGU ANGGOTA: tim belum menjawab.'
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
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
refs: [F-A09-0006, F-A09-0017, F-A09-0018]
```

```yaml
id: Q-B1-b
question: Bagaimana F-A07-0001 (masalah konkret CPPT lawan resume di RSIA belum ditunjukkan) diselesaikan, mengingat angka tertahan D-19?
affected: [Bab I]
class: L3
pic: Pengguna
ask_to: Tim
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
refs: [F-A07-0001, D-19]
```

```yaml
id: Q-B1-c
question: Siapa pemilik di tim untuk penautan ibu-bayi (Penyelarasan:43) setelah lingkup I.4 diputuskan di luar kajian individu?
affected: [Bab I, A06]
class: L3
pic: Pengguna
ask_to: Tim
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
refs: [D-25, F-A07-0005]
```

```yaml
id: Q-B1-d
question: Konfirmasi pembimbing atas urutan paragraf 1 I.1 (masalah dulu, rujukan capstone kemudian) dibanding templat
affected: [Bab I]
class: L3
pic: Pengguna
ask_to: Pembimbing
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU PEMBIMBING'
updated: 2026-11-12
refs: []
```

```yaml
id: Q-B1-e
question: Judul Bab II mana yang berlaku, "Studi Literatur" (naskah) atau "Kajian Pustaka" (templat)?
affected: [Bab II]
class: L3
pic: Pengguna
ask_to: Pembimbing
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
refs: [F-A10-0010]
```

```yaml
id: Q-B1-f
question: Apa definisi "rawat jalan terbatas" dan bentuk dokumen rawat jalan di RSIA (Q-TEAM butir 4)?
affected: [Bab I, Bab II]
class: L3
pic: Pengguna
ask_to: Tim / RSIA mitra
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
refs: [D-21, Q-TEAM, F-A07-0019, F-A04-0010, F-A04-0011, D-76]
note_2026-11-09_TSK-116: 'Tetap terbuka (fakta RSIA via Abizzar/tim). A01 melaporkan Penyelarasan baris 51 dan 350 menyatakan bentuk dokumen rawat jalan belum dipastikan; baris 13, 49, 279 memasukkan rawat jalan terbatas pada CPPT dan resume atau padanannya (belum diverifikasi A13 ke berkas). Usulan pengguna D-76 bergantung pada butir ini.'
note_D-91: 'Pembaruan 2026-11-09 (TSK-142): D-91 (pengguna, lingkup terbatas; BUKAN keputusan tim/RSIA): "rawat jalan terbatas" di I.4 dinyatakan sebagai cakupan bersyarat tanpa definisi baru; terkait D-88 (penilaian ketersediaan). Batas operasional dan bentuk dokumen rawat jalan RSIA tetap tidak diketahui; Q-TEAM butir 4 dan butir ini TETAP MENUNGGU ANGGOTA.'
note: 'Pernyataan pengguna 2026-11-08 (BUKAN keputusan; premis, belum diverifikasi ke aturan atau RSIA). Pertanyaan a04 P1 (verbatim): "Pertanyaan a04 (P1 dari 3), diteruskan verbatim. Konteks (ringkas): I.4 paragraf 2 membatasi dokumen pada \"CPPT dan resume medis\"; paragraf 4 hanya memuat penanda #28 tanpa batas rawat jalan; I.1 paragraf 4 menyebut resume medis belum tentu ada pada setiap episode rawat jalan; Penyelarasan:279 memakai frasa \"atau padanannya\" yang tidak ada di I.4; I.2 menyatakan kedua pertanyaan berlaku pada rawat inap dan rawat jalan. Pertanyaan: Dalam kajian Anda, apakah episode rawat jalan yang tidak memiliki resume medis berada di luar kajian, ataukah dokumen padanannya dikaji sebagai pengganti resume medis? Jawaban \"belum dapat diputuskan sebelum tim atau RSIA menjawab butir 4\" juga sah." Opsi: Di luar kajian | Dokumen padanan dikaji | Belum dapat diputuskan. Jawaban teks bebas pengguna (verbatim, bukan salah satu opsi): "Rawat jalan juga semua harusnya ada resume medisnya karena jika tidak tidak bisa klaim bpjs". Tidak menetapkan batas operasional rawat jalan: penanda #28 tetap [MENUNGGU KEPUTUSAN]; Q-TEAM butir 4 dan butir ini tetap terbuka.'
```

```yaml
id: Q-B1-g
question: "Laporan utama capstone" yang dirujuk Bab I tidak ada di repo; di mana berkasnya, atau rujukan diganti Penyelarasan?
affected: [Bab I]
class: L3
pic: Pengguna
ask_to: Tim
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
refs: [F-A08-0005]
```

```yaml
id: Q-B1-h
question: Apakah satuan keputusan Q2 (rumusan 2 I.2, kejelasan alasan dan rujukan) ditetapkan per kelompok penilai (tenaga ahli dan pengguna proksi terpisah) atau gabungan, dan siapa yang menilai (Q-TEAM butir 7)?
affected: [Bab I, A06, A11]
class: L3
pic: Pengguna
ask_to: Tim
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
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
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
refs: [Q-B1-e]
```

```yaml
id: Q-B1-j
question: Selisih minimum presisi dan recall kombinasi atas masing-masing komponen (D-29) belum ada di daftar Q-TEAM Penyelarasan (butir 8 hanya memuat angka ambang 13 ukuran); perlu diusulkan ke tim
affected: [Bab I, A06]
class: L3
pic: Pengguna
ask_to: Tim
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
refs: [D-29, D-22, F-A07-0032, F-A07-0037, F-A09-0075]
```

```yaml
id: Q-B1-k
question: Dampak lintas proposal yang belum diperiksa: (1) Penyelarasan:35 belum memuat pembanding D-22 maupun kriteria D-29 (A06 belum dijalankan); (2) irisan I.4 paragraf 5 / rumusan 2 dengan rumusan 4 Abizzar belum diperiksa. Perlu A06 dan konfirmasi tim
affected: [Bab I, A06]
class: L3
pic: Pengguna
ask_to: Tim
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
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
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
refs: [D-30, Q-B1-j]
marker: I.3 paragraf 3
```

```yaml
id: Q-B1-m
question: Rujukan maju I.3 paragraf 1 "prosedur pengukurannya diuraikan pada Subbab I.5" harus dipenuhi saat I.5 ditulis atau dihapus
affected: [Bab I]
class: L4
pic: Pengguna
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
refs: [D-31]
```

```yaml
id: Q-B1-n
question: Di mana pengembangan komponen (aturan rule-based dan pemeriksaan AI/NLP berbasis RAG) oleh penulis dijelaskan: paragraf research gap I.1 atau I.5?
affected: [Bab I]
class: L3
pic: Pengguna
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
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
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
refs: [D-32, D-29, F-A11-0001, F-A05-0001, F-A06-0006, D-77]
note_2026-11-09: 'USUL PENGGUNA: union (gabungan semua temuan), D-77 lingkup terbatas; BUKAN keputusan tim, tidak DIPUTUSKAN. Konsekuensi (A01): recall kombinasi tak di bawah komponen terbaik, presisi dapat turun. Menunggu tim.'
```

```yaml
id: Q-B1-p
question: Titik ukur kombinasi terhadap rekonsiliasi antarpemeriksaan milik Abizzar (Penyelarasan:183) dan perlakuan temuan ganda
affected: [Bab I, A06]
class: L3
pic: Pengguna
ask_to: Tim
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
refs: [D-32, F-A11-0003, F-A06-0006, F-A05-0018]
```

```yaml
id: Q-B1-q
question: Operator ambang ">" (naskah) atau ">=" (tabel Penyelarasan:327-339)
affected: [Bab I, I.2]
class: L3
pic: Pengguna
ask_to: Tim / pembimbing
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
refs: [F-A11-0010, F-A06-0007, D-78, F-A11-0036, F-A05-0155, F-A07-0079, F-A07-0085, F-A07-0086, F-A09-0229]
note_2026-11-09: 'USUL PENGGUNA: ">=" (selaras tabel Penyelarasan), D-78 lingkup terbatas; BUKAN keputusan tim/pembimbing. Angka ambang tetap tertahan D-19 (dan Q-B1-bg). Naskah masih memakai ">".'
note_TSK-131: 'Pembaruan 2026-11-09: butir ini kini juga memuat paket F-A11-0036 (operator batas selisih dan saat penetapan; requires_decision), F-A05-0155 (MEDIUM: selisih minimum tak terikat sebelum pengujian; penetap dan bentuk selisih), F-A07-0079 (I.2 tidak mengikat selisih minimum sebelum pengujian). Izin alur DRAF 22 (TSK-130) menyelaraskan I.2 p6 (empat selisih; selisih minimum ditetapkan sebelum pengujian, tanpa angka); itu penyelarasan teks, bukan keputusan operator. Operator dan penetap tetap menunggu tim/pembimbing. Bukan keputusan.'
note_TSK-136: 'Pembaruan 2026-11-09: QA DRAF 22 menemukan bahwa rumusan "kurang dari selisih minimum" di I.2 p6 dan I.3 p2 menetapkan operator secara tersirat (selisih sama dengan minimum lolos), padahal penanda menyatakan operator belum ditetapkan (F-A09-0229 MEDIUM, F-A07-0085 LOW; requires_decision), dan DRAF 22 menjadikan penetap selisih minimum butir terbuka padahal D-82 menulis "setelah ditetapkan tim" (F-A07-0086). Ditangani izin alur DRAF 23 (TSK-135; rumusan netral operator, penetap dikembalikan "ditetapkan tim sebelum pengujian"; tanpa angka). Itu perbaikan teks, bukan keputusan operator: operator TIDAK diputuskan, tetap menunggu tim/pembimbing (usul pengguna D-78 tetap usul). Bukan keputusan.'
note_TSK-139: 'Pembaruan 2026-11-09: DRAF 23 (TSK-135) memakai rumusan netral operator di I.2 p6 dan I.3 p2 ("tidak memenuhi selisih minimum"); penetap selisih minimum "ditetapkan tim sebelum pengujian" (sesuai D-82); penanda selisih minimum kini memuat bentuk (mutlak atau relatif) dan operator batas sebagai butir terbuka. F-A09-0229, F-A07-0085, F-A07-0086 RESOLVED menurut auditor penemu (TSK-137, TSK-138). Operator dan bentuk selisih TETAP tidak diputuskan; menunggu tim/pembimbing. Catatan a07: siapa memutuskan apakah selisih minimum dipakai tersirat pada tim. Bukan keputusan.'
note_D-89: 'Pembaruan 2026-11-09 (TSK-142): D-89 (pengguna, lingkup terbatas): ambang, selisih minimum, dan satuan hitung di I.2/I.3 dinyatakan sebagai prosedur tanpa angka, ditetapkan sebelum pengujian. Operator dan bentuk selisih tidak diputuskan; D-78 tetap usul; BUKAN keputusan tim/pembimbing.'
```

```yaml
id: Q-B1-r
question: Aturan pencocokan temuan-label, agregasi mikro atau makro, dan perlakuan nilai 0/0 pada presisi dan recall
affected: [Bab I, I.2]
class: L3
pic: Pengguna
ask_to: Tim
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
refs: [F-A11-0005, F-A05-0003, Q-A04-d, D-79]
note_2026-11-09: 'USUL PENGGUNA: agregasi mikro, 0/0 dilaporkan tidak terdefinisi (D-79, lingkup terbatas); BUKAN keputusan tim. Rekomendasi berasal dari A01 (bukan temuan agent); RSIA-source tidak dibuka, tanpa sensitive_access. Bagian "aturan pencocokan temuan-label" dalam butir ini TIDAK dijawab. Menunggu tim.'
```

```yaml
id: Q-B1-s
question: Adakah ringkasan agregat jumlah episode dan sebaran jenis di luar .scratch/rsia/agregat/ yang dapat dirujuk tanpa membuka data RSIA?
affected: [Bab I]
class: L4
pic: Pengguna
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
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
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
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
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
refs: [F-A06-0003, F-A06-0004, Q-B1-l]
```

```yaml
id: Q-B1-w
question: Siapa pemilik konsistensi antar-entri CPPT di tingkat tim (Penyelarasan:53 tanpa pemilik, rumusan, atau jenis ketidaksesuaian)?
affected: [Bab I, A06]
class: L3
pic: Pengguna
ask_to: Tim
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
refs: [F-A06-0010, F-A05-0021, D-25]
```

```yaml
id: Q-B1-x
question: Di mana batas antara penautan ibu-bayi (di luar kajian, D-25) dan aturan pemeriksaan pasangan ibu-bayi yang tercatat milik Danen? Tergantung Q-TEAM butir 1
affected: [Bab I, A06]
class: L3
pic: Pengguna
ask_to: Tim
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
refs: [F-A06-0009, D-25, Q-TEAM]
```

```yaml
id: Q-B1-y
question: Bagaimana jawaban "tidak" ditafsirkan mengingat plafon presisi/recall = 1 (D-29 menjadi pasti "tidak") dan apa kondisi keabsahan jawaban (termasuk opsi "tidak dapat disimpulkan")?
affected: [Bab I, I.2, I.3]
class: L3
pic: Pengguna
ask_to: Tim
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
refs: [F-A11-0012, F-A05-0017, F-A05-0020, D-29, D-33, F-A11-0015, Q-B1-bj]
```

```yaml
id: Q-B1-z
question: Nuansa klaim "tidak ada resource CPPT" pada SATUSEHAT di Bab II:87 (narasi perkembangan penyakit dikirim lewat ClinicalImpression, Bab 6 panduan); bagaimana dipakai di Bab I/III?
affected: [Bab I, Bab II, Bab III]
class: L3
pic: Pengguna
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
refs: [B2-48, EVIDENCE_REGISTRY]
```

```yaml
id: Q-B1-aa
question: Konfirmasi pemilik Draft Bab 1 (1) dan apakah ada versi anggota yang lebih baru (dua dokumen anggota tampak usang; tanggal manifest Raihaan Bab I "± 2026-10-20" tidak cocok isinya karena sampul memakai judul baru 30 Okt)
affected: [A06, PROJECT_STATE Team Docs Manifest]
class: L3
pic: Pengguna
ask_to: Tim
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
refs: [Q-P2-a, Q-P2-c, F-A06-0014]
```

```yaml
id: Q-B1-ab
question: source/INDEKS.md usang (menyebut folder 01-12, sedangkan struktur kini 01-17); perbarui atau abaikan?
affected: [source/INDEKS.md]
class: L4
pic: A13/Pengguna
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
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
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
refs: [F-A11-0006, F-A11-0012, F-A05-0017, Q-B1-y]
```

```yaml
id: Q-B1-ae
question: Versi dokumen mana yang dilabeli dan diuji, dan apakah mode AI/NLP penuh atau inkremental?
affected: [Bab I, I.5]
class: L3
pic: Pengguna
ask_to: Tim
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
refs: [F-A11-0004]
```

```yaml
id: Q-B1-af
question: Dua inferensi penulis baru di I.5 perlu dinilai pengguna apakah merupakan keputusan metodologi. (1) Paragraf 4, "data uji tidak dipakai menyusun/menyesuaikan pemeriksaan": turunan Penyelarasan:297 tetapi tidak eksplisit di sana. (2) Paragraf 7.
affected: [Bab I, I.5]
class: L3
pic: Pengguna
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
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
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
refs: [TSK-059, Penyelarasan:304, Penyelarasan:312, A06]
```

## Butir baru dari kegagalan build modular (TSK-061/063, 2026-11-06)

```yaml
id: Q-B1-ah
question: lxml, LibreOffice, dan pdftotext belum tersedia untuk build_modular (build gagal ModuleNotFoundError lxml, build_modular.py baris 29). Apakah pengguna akan memasangnya (lxml; LibreOffice di C:\Program Files\LibreOffice\program\soffice.exe atau env SOFFICE; pdftotext dan pdfinfo di PATH), dan apakah build diulang dengan Approval Request baru (persetujuan P2-02 untuk satu eksekusi sudah terpakai)?
affected: [modular/, tools/build_modular.py]
class: L4
pic: Pengguna
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
refs: [TSK-061, TSK-063, P2-02, Q-B1-ac]
note: Pemasangan paket dilakukan pengguna, bukan agent. Keempat berkas modular tidak tersentuh.
```

```yaml
id: Q-B1-ai
question: Jalur pembuatan docx modular dari Markdown Bab I belum ada (build_modular tidak membacanya; build_docx.py dan build_with_toc.py dilarang P2-02). Bagaimana jalur itu disediakan?
affected: [modular/, bab1, tools/]
class: L3
pic: Pengguna
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
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
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
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
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
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
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
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
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
refs: [D-55, D-56, D-57, D-21, D-24, D-27, F-A05-0024, F-A07-0051, F-A11-0004, Q-B1-ae, Q-TEAM butir 5, Q-B1-bb, Q-B1-bc]
note_2026-11-09_TSK-116: 'Tetap terbuka (fakta RSIA via Abizzar/tim); tidak ada keputusan baru pada TSK-116.'
note_D-90: 'Pembaruan 2026-11-09 (TSK-142): pengguna menjawab dengan teks bebas (bukan memilih opsi) → D-90 (lingkup terbatas; BUKAN keputusan tim/pembimbing/RSIA): naskah tidak mengasumsikan keduanya terkunci; menurut keterangan lisan RSIA via penulis (BELUM terverifikasi) CPPT tidak dapat diubah dan resume medis masih dapat direvisi; satuan hitung rawat inap = satu episode (masuk hingga keluar dan resume diajukan; resume episode sebelumnya tidak dihitung kembali). Konflik dengan dokumen tim TIDAK diselesaikan A13; konfirmasi RSIA/tim tetap diperlukan; status TETAP MENUNGGU ANGGOTA. Naskah (I.1 baris 75/89, I.4 p6) belum diselaraskan pada pencatatan ini.'
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
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
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
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
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
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
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
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
refs: [D-58, D-29, D-56, Q-TEAM butir 8, Q-B1-y, Q-B1-ad, Q-B1-j, F-A05-0026, F-A11-0015, F-A05-0034, F-A11-0016, F-A11-0017, Q-A04-c, Q-B1-bj]
note: Tidak diputuskan D-58. Menurut catatan A01, membutuhkan Approval Request lanjutan dan pembahasan tim. Butir turunan dari Q-B1-bd.
note_2026-11-09_TSK-116: 'Tetap terbuka: tertahan D-19 dan belum adanya data agregat. Usulan pengguna D-78 (operator ">=") dan D-79 (mikro, 0/0 tidak terdefinisi) tidak menetapkan angka ambang, selisih minimum, atau kondisi keabsahan stratum.'
note_D-89_D-93: 'Pembaruan 2026-11-09 (TSK-142): D-89 (pengguna: ambang, selisih minimum, satuan hitung dinyatakan sebagai prosedur tanpa angka, ditetapkan sebelum pengujian) dan D-93 (plafon → hasil "tidak dapat dinilai", aturan sebelum uji; F-A11-0015 HIGH, F-A11-0016). Keduanya keputusan pengguna lingkup terbatas, BUKAN tim/pembimbing. Angka tetap tertahan D-19; status butir TETAP MENUNGGU ANGGOTA. Konfirmasi pengguna atas isian a03 di TO DO.md (pemutus butir 7 dan 10) BELUM ada.'
```

```yaml
id: Q-B1-bh
question: Apakah tim dan pembimbing menyetujui bahwa tiap pertanyaan penelitian menghasilkan dua jawaban terpisah (rawat inap dan rawat jalan), padahal rumusan 1 di Penyelarasan:35 memuat satu jawaban ya/tidak per rumusan capstone?
affected: [Bab I, I.2, I.3, Penyelarasan]
class: L3
pic: Pengguna
ask_to: Tim / Pembimbing
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
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
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
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
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU ANGGOTA'
updated: 2026-11-12
refs: [F-A11-0015, F-A05-0026, D-29, D-58, D-56, D-21, Q-B1-bg, Q-B1-y, F-A07-0067, F-A05-0034, D-76]
note_2026-11-09_TSK-116: 'USUL PENGGUNA (D-76, lingkup terbatas; BUKAN keputusan tim/RSIA): rawat jalan tetap dijawab terpisah, bersyarat: bila dokumen setara resume terbukti ada dan memadai; bila tidak, dilaporkan "tidak dapat dinilai", bukan "tidak". Catatan A13: pertanyaan yang diajukan A01 (rawat jalan terpisah dari rawat inap) berbeda rumusan dari pertanyaan butir ini (syarat D-29 bila satu aturan); butir ini TIDAK dianggap terjawab sepenuhnya, opsi (d) a11 sebagian mirip tetapi tidak dipilih secara eksplisit. Q-B1-f dan Q-TEAM butir 4 tetap terbuka. Status diubah dari TERBUKA ke MENUNGGU ANGGOTA karena menunggu tim/RSIA.'
note: Pembaruan TSK-107 (2026-11-09): QA I.5 DRAF 19 mencatat I.2/I.3/I.5 tidak memuat penanda Q-B1-bj (F-A11-0015 tetap OPEN HIGH; F-A07-0067; F-A05-0034 diperkuat I.1 p20); belum ada keputusan. Butir asli: butir baru dari QA siklus 2 DRAF 13 (TSK-082). Opsi a-d adalah usulan a11, bukan opsi yang ditawarkan ke pengguna; bukan keputusan. Siklus otomatis D-06 habis, sehingga tidak ada revisi otomatis atas butir ini. Pembaruan TSK-109 (2026-11-09): I.5 dibawa ke pembimbing dan tim tanpa revisi (TSK-108 DROPPED); status tetap TERBUKA.
```

```yaml
id: Q-B1-bk
question: Bagaimana D-59 ("tanpa pencarian literatur hibrida") ditafsirkan terhadap penanda #13 [PERLU VERIFIKASI SUMBER hibrida] di I.1 p16: keterbatasan permanen atau tugas tertunda?
affected: [Bab I, I.1 p16]
class: L3
pic: Pengguna
ask_to: Pengguna
status: DIPUTUSKAN → D-67
updated: 2026-11-09
refs: [D-59, F-A07-0062, D-67, F-A02-0201, F-A02-0202, F-A02-0203]
note: Butir baru dari QA siklus 1 DRAF 15 (TSK-087..090, dicatat TSK-092). Pembaruan TSK-114 (2026-11-09): setelah a02 membaca kedua PDF hibrida (TSK-113), pengguna memilih "Keterbatasan tetap, tanpa sumber hibrida" → D-67. Penanda hibrida diganti kalimat batas oleh penulis (BELUM dilakukan); Ijadi Maghsoodi dkk. tidak masuk telaah; kalimat "tidak satu pun sumber ..." dipertahankan. Koreksi referensi: penanda hibrida di naskah DRAF 19 ada di I.1 p20 (penanda 14), bukan #13 di p16. F-A02-0201 ditangani keputusan ini; status F-A07-0062 dan F-A02-0201 tidak diubah (hanya auditor penemu).
```

```yaml
id: Q-B1-bl
question: Apakah justifikasi kombinasi pemeriksaan LLM dan deterministik hanya keputusan tim/penulis (D-22, D-29) atau harus didukung literatur? Atribusi "pilihan rancangan capstone" ke dokumen tim belum dapat diverifikasi (a08 memeriksa Penyelarasan:55: dua komponen disebut, kata "kombinasi" tidak).
affected: [Bab I, I.1 p16, Penyelarasan]
class: L3
pic: Pengguna
ask_to: Tim
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
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
status: DIPUTUSKAN → D-72 (menunggu pembimbing)
updated: 2026-11-09
refs: [F-A05-0109, D-22, D-60, D-72]
note: F-A05-0109 menantang D-22 (diperkuat II.5:152). D-60 tidak memutuskan butir ini. Pembaruan TSK-114 (2026-11-09): pengguna memilih mempertahankan D-22 dengan catatan batas perbandingan dinyatakan eksplisit → D-72. D-22 tidak berubah. Persetujuan pembimbing BELUM ada. Status F-A05-0109 tidak diubah.
```

```yaml
id: Q-B1-bn
question: Bagaimana II.5/II.6 diselaraskan dengan fakta yang dipakai di Bab I DRAF 16 tetapi belum ada di Bab II (Zeba Tabel 9/kosinus hlm. 8, Skrabic skala 1-4 hlm. 3 dan rincian "mutu rekomendasi", Li Tabel 1 hlm. 5, metode ekstraksi proposisi Zeba hlm. 7)?
affected: [Bab II II.5, Bab II II.6, Bab I I.1]
class: L3
pic: Pengguna
ask_to: Penulis Bab II (a03)
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
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
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
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
status: DIPUTUSKAN → D-68
updated: 2026-11-09
refs: [F-A09-0154, F-A09-0126, Q-B1-bo, D-68]
note: Butir baru dari TSK-089 terarah DRAF 17 (dicatat TSK-096). LOW, lintas bagian. Pembaruan TSK-114 (2026-11-09): pengguna memilih "Izinkan, hanya singkatan" → D-68 (izin a03 hanya untuk singkatan di I.2 p2 dan I.5 p4; belum dikerjakan). Q-B1-bo tetap TERBUKA.
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
status: DIPUTUSKAN → D-73 (menunggu pembimbing)
updated: 2026-11-09
refs: [F-A05-0130, D-63, D-73]
note: Butir baru dari TSK-090 terarah keempat DRAF 19 (dicatat TSK-102). requires_decision true. Pembaruan TSK-114 (2026-11-09): pengguna memilih "Bedakan istilah secara eksplisit" → D-73 (D-63 dipertahankan dan diperjelas). Persetujuan pembimbing BELUM ada; revisi belum dilakukan; status F-A05-0130 tidak diubah.
```

```yaml
id: Q-B1-bv
question: Bagaimana menangani F-A05-0131 di I.1 p18 (keadaan ketiga berjawab "tidak": saling melengkapi tetapi kenaikan presisi atau recall di bawah selisih minimum D-29; makna "saling melengkapi" bergeser dari jenis pemeriksaan ke hasil presisi dan recall; menantang D-65)?
affected: [Bab I, I.1 p18]
class: L3
pic: Pengguna
ask_to: Pengguna
status: DIPUTUSKAN → D-74 (menunggu pembimbing)
updated: 2026-11-09
refs: [F-A05-0131, D-65, D-29, D-74, Q-B1-cc]
note: Butir baru dari TSK-090 terarah keempat DRAF 19 (dicatat TSK-102). requires_decision true. Pembaruan TSK-114 (2026-11-09): pengguna memilih "Persempit makna 'saling melengkapi'" → D-74 (mengubah sebagian D-65; ditandai). Turunan terbuka: Q-B1-cc (keadaan ketiga di I.3). Persetujuan pembimbing BELUM ada; status F-A05-0131 tidak diubah.
```

```yaml
id: Q-B1-bw
question: Kriteria pemilihan kombinasi tidak dapat diperiksa oleh penelitian maupun literatur setelah D-62 dan D-63 (F-A05-0132); apa konsekuensinya bagi simpulan Bab V, dan apakah hal itu dinyatakan terbuka sebagai motivasi rancangan?
affected: [Bab I, I.1 p18-p19, Bab V]
class: L3
pic: Pengguna
ask_to: Pembimbing
status: DIPUTUSKAN → D-75 (menunggu pembimbing)
updated: 2026-11-09
refs: [F-A05-0132, D-62, D-63, D-75]
note: Butir baru dari TSK-090 terarah keempat DRAF 19 (dicatat TSK-102). requires_decision true; pic Pengguna, ask_to Pembimbing menurut brief A01. Pembaruan TSK-114 (2026-11-09): pengguna memilih "Nyatakan terbuka sebagai motivasi rancangan" → D-75. Persetujuan pembimbing BELUM ada; revisi belum dilakukan; status F-A05-0132 tidak diubah.
```

## Butir baru dari QA Subbab I.5 DRAF 19 (TSK-103..106, dicatat TSK-107, 2026-11-09)

```yaml
id: Q-B1-bx
question: Bagaimana data pengembangan diberi label di I.5 (F-A11-0021): tanpa label, label oleh penulis, atau label sebagian oleh pakar? Saat ini hanya data uji dilabeli dan tahap 3 tidak punya acuan pada data pengembangan.
affected: [Bab I, I.5]
class: L3
pic: Pengguna
ask_to: Pengguna / Tim
status: DIPUTUSKAN → D-69 (menunggu tim)
updated: 2026-11-09
refs: [F-A11-0021, D-69]
note: Opsi a, b, c adalah usulan a11, bukan opsi yang ditawarkan ke pengguna. Pembaruan TSK-109 (2026-11-09): I.5 dibawa ke pembimbing dan tim tanpa revisi (revisi TSK-108 DROPPED atas koreksi pengguna). Pembaruan TSK-114 (2026-11-09): pengguna memilih "Label oleh penulis" → D-69 sebagai keputusan pengguna/penulis. Persetujuan tim BELUM ada; status F-A11-0021 tidak diubah.
```

```yaml
id: Q-B1-by
question: Bagaimana kasus uji dipilih (F-A05-0136), dan bagaimana temuan RAG di luar daftar jenis diperlakukan serta apa komposisi daftar jenis, termasuk apakah wajib memuat jenis konteks (F-A05-0138)?
affected: [Bab I, I.5]
class: L3
pic: Pengguna
ask_to: Pengguna / Tim
status: DIPUTUSKAN → D-70 (sebagian; menunggu tim)
updated: 2026-11-09
refs: [F-A05-0136, F-A05-0138, D-70, Q-B1-cb]
note: Butir baru dari TSK-104 (dicatat TSK-107). requires_decision true. Pembaruan TSK-109 (2026-11-09): I.5 dibawa ke pembimbing dan tim tanpa revisi. Pembaruan TSK-114 (2026-11-09): pengguna memilih (1/2) "Acak, benih tetap, per jenis perawatan" dan (2/2) "Dihitung terpisah, tidak masuk presisi/recall utama" → D-70. Persetujuan tim BELUM ada. Bagian "apakah daftar jenis wajib memuat jenis konteks" (F-A05-0138) BELUM terjawab: dipindah ke butir baru Q-B1-cb (TERBUKA). Status F-A05-0136 dan F-A05-0138 tidak diubah.
```

```yaml
id: Q-B1-bz
question: Apakah tiap komponen menyasar seluruh daftar jenis atau dibagi per jenis (F-A05-0133)? Bila dibagi per jenis, menurut a05 uji recall D-29 hampir pasti ya dan uji presisi union hampir pasti tidak.
affected: [Bab I, I.5, I.2]
class: L3
pic: Pengguna
ask_to: Pengguna / Tim
status: DIPUTUSKAN → D-71 (menunggu tim)
updated: 2026-11-09
refs: [F-A05-0133, D-29, Q-TEAM butir 1, D-71]
note: Butir baru dari TSK-104 (dicatat TSK-107); terkait Q-TEAM butir 1. requires_decision true. Pembaruan TSK-109 (2026-11-09): I.5 dibawa ke pembimbing dan tim tanpa revisi. Pembaruan TSK-114 (2026-11-09): pengguna memilih "Keduanya menyasar seluruh daftar jenis" → D-71 sebagai keputusan pengguna. Persetujuan tim BELUM ada (Q-TEAM butir 1 tetap menunggu tim); status F-A05-0133 tidak diubah.
```

```yaml
id: Q-B1-ca
question: Apakah penyusunan jawaban dijadikan tahap tersendiri di I.5 (F-A07-0070)?
affected: [Bab I, I.5]
class: L3
pic: Pengguna
ask_to: Pengguna
status: DIPUTUSKAN → D-66
updated: 2026-11-09
refs: [F-A07-0070, D-66]
note: Butir baru dari TSK-105 (dicatat TSK-107). requires_decision true. Pembaruan TSK-109 (2026-11-09): I.5 dibawa ke pembimbing dan tim tanpa revisi. Pembaruan TSK-114 (2026-11-09): pengguna memilih "Gabung ke tahap evaluasi" → D-66 (lima tahap tetap). Koreksi A01: label "(Rekomendasi agent a07)" pada opsi itu salah; F-A07-0070 tidak merekomendasikan opsi apa pun. Dampak ke I.3 dan penanda I.5 menunggu revisi; status F-A07-0070 tidak diubah.
```

## Butir baru dari keputusan 2026-11-09 (TSK-114)

```yaml
id: Q-B1-cb
question: Apakah daftar jenis ketidaksesuaian wajib memuat jenis konteks (F-A05-0138)? Bagian ini tidak terjawab oleh D-70 (yang hanya memutuskan perlakuan temuan RAG di luar daftar).
affected: [Bab I, I.5]
class: L3
pic: Pengguna
ask_to: Pengguna / Tim
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
refs: [F-A05-0138, D-70, Q-B1-by]
note: Butir baru dari TSK-114 (turunan Q-B1-by 2/2). requires_decision true. Bukan keputusan.
```

```yaml
id: Q-B1-cc
question: Keadaan ketiga yang berjawab "tidak" (komponen saling melengkapi menurut jenis pemeriksaan, tetapi kenaikan presisi/recall di bawah selisih minimum D-29) belum ditangani di I.3 dan I.5. Bagaimana kondisi itu dinyatakan setelah D-74 mempersempit makna "saling melengkapi"?
affected: [Bab I, I.3, I.5, I.1 p18]
class: L3
pic: Pengguna
ask_to: Penulis / Pembimbing
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU DATA'
updated: 2026-11-12
refs: [F-A05-0131, D-74, D-65, D-29, D-33, Q-B1-bv, D-81, D-82, F-A07-0072, F-A07-0073, F-A07-0074, F-A07-0075, F-A11-0024, F-A05-0150]
note: Butir baru dari TSK-114 (turunan D-74). Pembaruan TSK-124 (2026-11-09): bagian teks keadaan ketiga ditangani D-81 (kalimat p19 diselaraskan dengan D-74) dan D-82 (selisih minimum bersyarat masuk I.2 p6); pengerjaan naskah oleh a03 (TSK-123, DRAF 21); persetujuan pembimbing BELUM ada. Bagian yang TETAP TERBUKA: hasil kosong atau tidak terdefinisi (0/0) dan status "tidak dapat dinilai" belum dipetakan ke jawaban (F-A11-0024 MEDIUM, hanya dipicu dokumen rawat jalan; F-A05-0150), serta keabsahan I.3 p1 vs p2 (F-A07-0074, requires_decision) dan rujukan kondisi keabsahan dari I.5 p6/I.3 p3 (F-A07-0075). Bukan keputusan. Pembaruan TSK-131 (2026-11-09): a07 menyatakan F-A07-0072..0075 RESOLVED dan a11 F-A11-0030 RESOLVED (menurut auditor), tetapi bentuk baru terbuka: F-A11-0037 (LOW, requires_decision: keabsahan hanya dinyatakan untuk jawaban "tidak" di I.3 p1), F-A05-0156 (MEDIUM: keabsahan dan kategori ketiga tak terikat sebelum pengujian), F-A11-0024 (membaik sebagian), F-A05-0150 (bentuk berubah). Izin alur DRAF 22 menyelaraskan I.3 (keabsahan sebelum pengujian untuk "ya" maupun "tidak"); itu penyelarasan teks, bukan keputusan akademik.
```

```yaml
id: Q-B1-cd
question: Cakupan revisi a03 atas DRAF 20 (penerapan D-66..D-75 dan usulan D-76..D-80 ke Bab I) belum diputuskan
affected: [Bab I]
class: L3
pic: Pengguna
ask_to: Pengguna / tim / pembimbing
status: DITUTUP DENGAN ALASAN (dijawab pengguna 2026-11-09; izin revisi terarah, bukan keputusan akademik; revisi dijalankan TSK-117 → DRAF 20)
updated: 2026-11-09
refs: [D-66, D-67, D-68, D-69, D-70, D-71, D-72, D-73, D-74, D-75, D-76, D-77, D-78, D-79, D-80, TSK-117, TSK-123]
note: Butir baru dari TSK-116. Pengguna semula menjawab "Coba tanyakan ke saya terkait yang putusannya adalah tim" (verbatim; BUKAN persetujuan). Pembaruan TSK-124 (2026-11-09): pertanyaan "Setelah a13 selesai mencatat, apakah a03 dijalankan untuk revisi Bab I menjadi DRAF 20?" (opsi: "Jalankan, butir milik Anda saja (Recommended)" | "Jalankan, termasuk usulan tim sebagai penanda" | "Jangan revisi sekarang") dijawab "Jalankan, termasuk usulan tim sebagai penanda". Ini izin revisi terarah (TSK-117) di luar siklus D-06; usulan tim hanya sebagai penanda [MENUNGGU KEPUTUSAN TIM], bukan keputusan tim. Izin lanjutan DRAF 21 (TSK-123) dicatat di TASK_TRACKER. Ditutup karena dijawab; persetujuan tim dan pembimbing atas D-69..D-80 tetap BELUM ada.
```

```yaml
id: Q-B1-ce
question: Kriteria pemilihan kombinasi (D-61) tidak membedakan pasangan aturan+RAG dari pasangan lain; bagaimana kriteria dibuat spesifik pada pasangan yang diuji?
affected: [Bab I, I.1 p18]
class: L3
pic: Pengguna
ask_to: Pengguna / pembimbing
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
refs: [F-A05-0142, D-61, D-73]
note: Butir baru dari TSK-124 (QA DRAF 20, a05 TSK-122). requires_decision true. Dalam cakupan "tidak disentuh" DRAF 21. Bukan keputusan.
note_D-95: 'Pembaruan 2026-11-09 (TSK-142): D-95 (pengguna, lingkup terbatas; BUKAN keputusan pembimbing): kriteria tetap umum, urutan dinyatakan (opsi "dibedakan per pasangan" tidak dipilih). Status butir TETAP TERBUKA sampai naskah dan auditor; D-61 tidak diubah.'
```

```yaml
id: Q-B1-cf
question: Kata "pertimbangan" Dietrich di I.1 p20 tanpa fungsi dan kategori kontradiksi tidak disebut; apa fungsi rujukan itu?
affected: [Bab I, I.1 p20]
class: L3
pic: Pengguna
ask_to: Pengguna / pembimbing
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
refs: [F-A05-0144]
note: Butir baru dari TSK-124 (a05 TSK-122). MEDIUM. Dalam cakupan "tidak disentuh" DRAF 21. Bukan keputusan.
note_D-95: 'Pembaruan 2026-11-09 (TSK-142): D-95 (pengguna, lingkup terbatas; BUKAN keputusan pembimbing): temuan Dietrich hanya latar. Status butir TETAP TERBUKA sampai naskah dan auditor.'
```

```yaml
id: Q-B1-cg
question: Apakah "sumber yang ditelaah" pada kalimat batas I.1 p20 mencakup Bab II DRAFT 6 saja, lima studi p16, atau juga II.4 lama? Dan apakah Zeba (aturan + encoder, dua tahap) perlu disebut agar tidak terbaca sebagai kontra-contoh?
affected: [Bab I, I.1 p20, Bab II]
class: L3
pic: Pengguna
ask_to: Pengguna / a05 / a08
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
refs: [F-A05-0146, F-A08-0101, F-A08-0102, D-67, D-85, F-A09-0235, F-A07-0087]
note: Butir baru dari TSK-124. Pertanyaan a05 (TSK-122); D-85 menetapkan cakupan dan sifat tidak sistematis harus dinyatakan, tetapi isi cakupan belum ditetapkan. Pembaruan TSK-131 (2026-11-09): D-85 dan kalimat batas p22 DRAF 21 sudah menyatakan cakupan (a08 TSK-127: konsisten dengan H-01..H-03, D-67, D-85), tetapi himpunan rujukan literatur belum diseragamkan (F-A05-0154 LOW; F-A07-0083 INFO: ungkapan cakupan literatur berbeda-beda; F-A08-0108 INFO: cakupan "Bab II"). Bagian itu TETAP TERBUKA; DRAF 22 (TSK-130) tidak mencakupnya. Bukan keputusan.
note_TSK-136: 'Pembaruan 2026-11-09 (QA DRAF 22): F-A09-0235 (LOW, requires_decision): "studi lain pada Bab II" di I.1 p19 vs "kelima studi"/Zhang; bentuk berasal dari keputusan pengguna D-86. F-A07-0087 (LOW): alasan Zhang tidak dihitung sebagai dukungan p21 setelah kalimat penutup p19 dikeluarkan; alasan harus ditulis tanpa menafsirkan D-61, bila tidak bisa ke pengguna. a08 TSK-134: kalimat penutup p19 DIDUKUNG sumber; F-A08-0112 (INFO): Gao dkk. dan Ali dkk. di batas klaim kekosongan dinilai dari teks Bab II. Bagian himpunan rujukan literatur tetap TERBUKA; DRAF 23 (TSK-135) tidak mencakupnya. Bukan keputusan.'
note_D-96: 'Pembaruan 2026-11-09 (TSK-142): D-96 (pengguna, lingkup terbatas; BUKAN keputusan pembimbing): satu istilah cakupan, definisi sekali di I.1, alasan Zhang satu kalimat (menjawab F-A09-0235, F-A07-0087 sebagai arah; status temuan tidak diubah A13). Isi definisi belum ditulis; naskah belum diubah. Konfirmasi pengguna atas isian a03 di TO DO.md (pemutus butir 7 dan 10) BELUM ada; butir tetap TERBUKA sampai naskah dan auditor.'
```

```yaml
id: Q-B1-ch
question: Jawaban pertanyaan 1 bergantung pada tahap 5 (pengguna proksi); apakah ketergantungan itu dinyatakan di Bab I (menantang D-66)?
affected: [Bab I, I.5]
class: L3
pic: Pengguna
ask_to: Pengguna
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
refs: [F-A05-0148, F-A11-0032, D-66]
note: Butir baru dari TSK-124 (a05 F-A05-0148 LOW, challenges D-66; a11 F-A11-0032 INFO: jawaban menunggu tahap 5, risiko ke mitigasi). Dalam cakupan "tidak disentuh" DRAF 21. Bukan keputusan.
```

```yaml
id: Q-B1-ci
question: Satuan pengacakan dan ukuran stratum untuk pengacakan per jenis perawatan: acak memilih per episode, sedangkan data dibagi per pasien. Bagaimana satuannya ditetapkan?
affected: [Bab I, I.5]
class: L3
pic: Pengguna
ask_to: Tim / pembimbing
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: MENUNGGU DATA'
updated: 2026-11-12
refs: [F-A11-0025, F-A11-0016, Q-B1-bg, Q-A04-c]
note: Butir baru dari TSK-124 (a11 TSK-121, MEDIUM). Data agregat tidak ada, sehingga ukuran stratum tidak dapat dinilai. Bukan keputusan.
```

```yaml
id: Q-B1-cj
question: D-71 bertentangan dengan pembagian jenis tersirat di Penyelarasan (:69, :76); bagaimana keduanya diselaraskan? Juga: agregasi mikro (D-79) mendahului Q-A04-d.
affected: [Bab I, I.5, Penyelarasan]
class: L3
pic: Pengguna
ask_to: Tim
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
refs: [F-A11-0026, F-A11-0027, D-71, D-79, Q-A04-d]
note: Butir baru dari TSK-124 (a11 TSK-121: F-A11-0026 MEDIUM, F-A11-0027 LOW). Terkait juga F-A11-0023 (union hanya formal memenuhi D-32; uji D-29 asimetris; bergantung aturan temuan ganda; ke tim) dan F-A07-0076 (INFO). Bukan keputusan.
```

```yaml
id: Q-B1-ck
question: Arti "memadai" pada usulan Q-B1-bj tidak terdefinisi, dan rumusan usulan Q-B1-bj ("terpisah") berbeda dari pertanyaan yang diajukan A01 serta taksa; bagaimana dirumuskan ulang?
affected: [Bab I, I.5, OPEN_QUESTIONS Q-B1-bj]
class: L3
pic: Pengguna
ask_to: Tim
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
refs: [F-A05-0149, F-A05-0151, F-A09-0184, F-A09-0194, Q-B1-bj, D-76, D-78]
note: Butir baru dari TSK-124. F-A05-0149 (MEDIUM, ke tim), F-A05-0151 (LOW; dasar usulan ">=" bertentangan dengan kalimat sebelumnya), F-A09-0184 (cakupan selisih I.5 p6 taksa), F-A09-0194 (requires_decision). Pengamatan A01: Q-B1-bj di OPEN_QUESTIONS memiliki rumusan berbeda dari pertanyaan yang diajukan A01 (belum direkonsiliasi; tidak diubah A13). Bukan keputusan.
```

```yaml
id: Q-B1-cl
question: Berkas Bab II mana yang aktif? Berkas lama II.4/II.7/II.8 masih mengutip Domingues dan Ijadi, sedangkan DRAFT 6 dan I.1 p20 tidak menelaahnya.
affected: [Bab II, I.1 p20]
class: L3
pic: Pengguna
ask_to: Pengguna
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
refs: [F-A08-0103, F-A05-0146, Q-B1-bn, D-67]
note: Butir baru dari TSK-124 (a08 TSK-120, LOW). Bukan keputusan.
```

```yaml
id: Q-B1-cm
question: Apa arti "saling melengkapi" dan "tidak memberi informasi" bagi jawaban "tidak" setelah D-74/D-81: definisi D-74 memuat bagian empiris, sikap terhadap jawaban "ya" belum dinyatakan, dan dengan union recall jawaban "tidak" memberi informasi teramati tentang kontribusi unik?
affected: [Bab I, I.1 p18-19, I.3, I.5]
class: L3
pic: Pengguna
ask_to: Pembimbing / tim
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
refs: [F-A05-0152, F-A11-0038, D-74, D-81, D-65, D-32, F-A11-0023]
note: Butir baru dari TSK-131 (a05 TSK-129: F-A05-0152 MEDIUM, menantang D-74/D-81, requires_decision; a11 TSK-128: F-A11-0038 LOW, requires_decision, ke tim). Di luar cakupan DRAF 22 (TSK-130 tidak menyentuh F-A05-0152/F-A11-0038). Bukan keputusan.
note_D-87: 'Pembaruan 2026-11-09 (TSK-142): pengguna memilih "Pertahankan D-74, nyatakan keberatan sebagai keterbatasan" → D-87 (lingkup terbatas; BUKAN keputusan tim/pembimbing). Dijawab penulis; D-74/D-81 tetap menunggu pembimbing. Status F-A05-0152 dan F-A11-0038 tidak diubah A13 (RESOLVED hanya oleh auditor penemu); naskah belum diubah.'
```

```yaml
id: Q-B1-cn
question: Bagaimana ketersediaan dokumen rawat jalan dinilai (kriteria "tersedia" vs "ada dan memadai", satuan, pelaku), mengingat ketergantungan melingkar dengan I.4?
affected: [Bab I, I.4, I.5]
class: L3
pic: Pengguna
ask_to: Tim
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
refs: [F-A05-0157, F-A11-0033, Q-B1-ba, Q-B1-bj, Q-B1-ck]
note: Butir baru dari TSK-131 (a05 F-A05-0157 MEDIUM, requires_decision, ke tim; a11 F-A11-0033 LOW). Di luar cakupan DRAF 22 (TSK-130 tidak menyentuh F-A05-0157). Bukan keputusan.
note_D-88: 'Pembaruan 2026-11-09 (TSK-142): pengguna memilih "Penulis menilai dengan kriteria tertulis, hasil ke tim" → D-88 (lingkup terbatas; BUKAN keputusan tim/RSIA). Kriteria tertulis belum dirumuskan; bentuk dokumen rawat jalan RSIA tetap tidak diketahui (Q-B1-f). Status F-A05-0157 tidak diubah A13.'
```

```yaml
id: Q-B1-co
question: Butir yang masih menunggu pengguna setelah D-98..D-100 - (1) dampak D-98 (syarat pertama dinilai lebih dulu, 0/0 = syarat pertama gagal) pada stratum tanpa label; (2) konfirmasi interpretasi A01 atas "keputusan editorial terkait D-83" (Dietrich/Stubbert hanya latar, tidak mengualifikasi komponen capstone, tanpa menafsirkan D-61); (3) jalur DOCX (build_modular.py membangun dari master docx Bab II); (4) temuan paket usulan A01 yang tidak dipilih (plafon satu komponen, satuan unit, episode tanpa dokumen, batas kesimpulan, "tidak diuji")?
affected: [Bab I, I.1, I.2, I.3, I.5, DOCX]
class: L3
pic: Pengguna
ask_to: Pengguna / tim / pembimbing
status: DITUTUP DENGAN ALASAN
closed_reason: 'D-115 (2026-11-12): teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi; Bab I dibiarkan apa adanya oleh pengguna. Status sebelumnya: TERBUKA'
updated: 2026-11-12
refs: [D-98, D-99, D-100, D-83, D-95, F-A11-0048, F-A11-0049, F-A07-0099, F-A07-0101, Q-B1-aw, Q-B1-al, Q-B1-ax, Q-B1-cj]
note: Butir baru dari TSK-152. Bukan keputusan. D-98 menjawab F-A11-0048 sebagai keputusan pengguna, tetapi status F-A11-0048 tetap OPEN sampai a11 memeriksa ulang. D-99: union tetap usulan penulis (Q-B1-cj tetap TERBUKA untuk tim); D-29 tidak berubah. Siklus otomatis D-06 habis; revisi lanjutan butuh izin pengguna.
note_TSK-153: 'Pembaruan 2026-11-10: D-101 (tiga entri Kemenkes ditambahkan ke docx resmi Bab II) menjawab sebagian butir (3) hanya soal sumber Daftar Pustaka; jalur DOCX secara keseluruhan tetap BELUM diputuskan. Build run3 FAILED di bab1_refs (menurut brief). tools/build_modular.py dimodifikasi pengguna/sesi biasa, isi belum diverifikasi. Perlu build ulang dan pemeriksaan ulang a12 untuk menyatakan F-A12-0001 (versi brief) RESOLVED. Q-B1-bf (Permenkes 26/2021 hlm. 48-54) tetap BELUM diverifikasi. D-92 (judul) tidak dipasang.'
```

## Rekonsiliasi 2026-11-12 (konflik baseline vs docx resmi vs keputusan lama)

Butir di bawah dibuat oleh rekonsiliasi atas permintaan pengguna; bukan keputusan.

```yaml
id: Q-REC-a
question: 'Judul sub-subbab Bab II pada baseline (D-103) berbeda dari docx resmi: II.2 ''Representasi dan Standardisasi Informasi Klinis'' (baseline) vs ''Standar Interoperabilitas dan Terminologi Klinis di Indonesia'' (docx); II.3.1 ''Pemeriksaan Kesalahan dan Konsistensi Dokumentasi Klinis'' vs ''Deteksi Kesalahan pada Dokumentasi Klinis''; II.3.2 ''Ketahanan Model terhadap Variasi Teks Klinis'' vs ''Pemeriksaan Fakta Keluaran terhadap Rekam Medis Sumber''. Mana yang berlaku, dan apakah isi II.3.2 perlu diubah mengikuti baseline? (Ejaan II.5.3 sudah diputuskan ''Deidentifikasi'', D-112.)'
affected:
- Bab II
- TA1 bab 2.docx
- Draft-Bab1-Bab2.docx
- bab2/II.2_*.md
- bab2/II.3_*.md
class: L3
pic: Pengguna
ask_to: Pengguna
status: DIPUTUSKAN → D-114
updated: 2026-11-12
refs:
- D-103
- D-111
- D-112
note: Dibuat oleh rekonsiliasi 2026-11-12 sesuai instruksi 'laporkan konflik sebelum melakukan perubahan'. Tidak ada judul diubah.
```

```yaml
id: Q-REC-b
question: Naskah Bab I di docx resmi menyatakan ambang 0,80 untuk precision dan recall, 80% penilaian skor 4 atau 5, serta mekanisme union dan deduplikasi, padahal baseline (D-102) melarang menentukan mekanisme kombinasi, ambang, jumlah kasus, pencocokan hasil, dan komposisi penilai tanpa keputusan tim. Apakah angka dan mekanisme itu diberi status usulan, dipertahankan karena sudah disepakati, atau diubah?
affected:
- Bab I
- I.3
- I.5
- TA1 bab 1.docx
class: L3
pic: Pengguna
ask_to: Pengguna
status: DIPUTUSKAN → D-115
updated: 2026-11-12
refs:
- D-102
- D-77
- D-78
- D-79
- Q-B1-o
- Q-B1-q
- Q-B1-r
note: D-77 (union), D-78 (>=), D-79 (agregasi mikro) tercatat sebagai usulan pengguna yang belum disetujui tim.
```

```yaml
id: Q-REC-c
question: Baseline menyebut I.3 'dua tujuan/ukuran keberhasilan', sedangkan docx I.3 memuat satu tujuan utama, lima tujuan khusus, dan tiga ukuran (dua utama dan satu pendamping, kesepakatan antarpenilai). Disesuaikan ke baseline atau docx yang berlaku?
affected:
- Bab I
- I.3
class: L3
pic: Pengguna
ask_to: Pengguna
status: DIPUTUSKAN → D-115
updated: 2026-11-12
refs:
- D-102
note: Tidak ada perubahan dilakukan.
```

```yaml
id: Q-REC-d
question: Baseline memindahkan sintesis, perbandingan penelitian, research gap, dan posisi penelitian ke Bab III, tetapi Bab III di docx resmi masih teks templat dan bab3/Bahan_Pindahan_dari_Bab_II.md belum diselaraskan. Kapan Bab III ditulis, dan apakah bab3/Bahan_Pindahan_dari_Bab_II.md diperbarui lebih dulu?
affected:
- Bab III
- bab3/Bahan_Pindahan_dari_Bab_II.md
class: L3
pic: Pengguna
ask_to: Pengguna
status: DIPUTUSKAN → D-116
updated: 2026-11-12
refs:
- D-104
- D-120
note: Naskah Bab I docx tidak memuat paragraf research gap; materi lama ada di riwayat Git. D-120 (2026-11-12): Bab III resmi dibuka, D-116 terpenuhi.
```

```yaml
id: Q-REC-e
question: Keputusan lama yang bergantung pada teks DRAF 24 yang sudah tidak ada di Bab I resmi (D-59..D-65 dan D-81..D-85, D-95 tentang paragraf research gap I.1; D-66..D-75, D-88..D-94, D-96, D-97 tentang I.2/I.3/I.5 DRAF 24; D-98..D-100) serta temuan QA terkait di FINDINGS_LOG (F-A05/F-A07/F-A09/F-A11 atas DRAF 24) tetap berstatus lama. Apakah ditandai SUPERSEDED/ditutup dengan alasan 'teks digantikan docx resmi 2026-11-12', dibawa ke Bab III, atau dibiarkan?
affected:
- DECISION_LOG
- FINDINGS_LOG
- OPEN_QUESTIONS
class: L3
pic: Pengguna
ask_to: Pengguna
status: DIPUTUSKAN → D-115
updated: 2026-11-12
refs:
- D-111
- D-104
- D-105
note: Tidak ada status diubah (instruksi D-105 butir 6). Q-B1-* yang terkait I.x DRAF 24 belum ditutup.
```

```yaml
id: Q-REC-f
question: Gaya sitasi di docx resmi tidak seragam ('et al.' dan 'dkk.', 'p.' dan 'hlm.'; K1 belum diputuskan, D-80 usul APA). Disamakan sekarang atau menunggu keputusan K1?
affected:
- Bab I
- Bab II
- K1
class: L3
pic: Pengguna
ask_to: Pengguna
status: DIPUTUSKAN → D-113
updated: 2026-11-12
refs:
- K1
- D-80
note: Pengamatan dari sinkronisasi 2026-11-12; tidak ada perubahan.
```

```yaml
id: Q-REC-g
question: Docx resmi Bab I (modular/TA1 bab 1.docx dan bagian Bab I Draft-Bab1-Bab2.docx) USANG terhadap bab1/Bab_I_Draft.md (D-119). Kapan dan bagaimana docx diperbarui (Approval Request P2-02 tersendiri; build_modular.py atau penyuntingan manual)?
affected:
- Bab I
- modular/TA1 bab 1.docx
- Draft-Bab1-Bab2.docx
class: L3
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-12
refs:
- D-119
- P2-02
note: Berkaitan dengan D-111 (SUPERSEDED sebagian oleh D-119). Tidak ada build disetujui oleh D-119. Status formal D-49 (Markdown sumber kebenaran Bab I; SUPERSEDED sebagian oleh D-111) tidak diubah; apakah dipulihkan formal diserahkan ke pengguna.
```

```yaml
id: Q-REC-h
question: Revisi Paket A (TSK-166) dan QA a09 terarah (TSK-167) tidak punya laporan agent di memory. Apakah perubahan substantif Bab I di 80a13ba (mis. I.2/I.3) selaras dengan D-102, dan apakah hasil QA a09 perlu dicatat ke FINDINGS_LOG bila laporannya ada?
affected:
- Bab I
- FINDINGS_LOG
class: L3
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-12
refs:
- D-118
- D-102
- TSK-166
- TSK-167
note: A13 tidak menilai isi substantif; tidak ada temuan dicatat tanpa laporan.
```

## Butir baru dari penulisan dan QA III.1 (TSK-168..172, dicatat TSK-174, 2026-11-12)

Dibuat dari brief A01; bukan keputusan. Batch untuk pengguna.

```yaml
id: Q-B3-a
question: Konfirmasi atau batalkan pemakaian Ijadi Maghsoodi dkk. (2026) di Bab III dan penambahannya ke bab2/Daftar_Pustaka.md (sudah dilakukan a03 atas arahan operasional A01); Domingues (2026) dan Newton dkk. (2026) tidak dipakai.
affected:
- bab3/Bab_III_Draft.md
- bab2/Daftar_Pustaka.md
class: L3
pic: Pengguna
ask_to: Pengguna
status: DIPUTUSKAN → D-126
updated: 2026-11-12
refs:
- TSK-169
- TSK-168
- TSK-181
- D-126
- TSK-187
note: Ijadi Maghsoodi dkk., Domingues, dan Newton berada di luar daftar pustaka sebelum Bab III (menurut a02). Aturan pengguna menyatakan sumber baru ke daftar referensi hanya atas permintaan. Pembaruan TSK-185 (2026-11-12) - pengguna memilih "Tunda sampai laporan QA masuk" (arahan alur; BELUM ada keputusan; pertanyaan diulang setelah QA III.2). Catatan a08 (TSK-181): III.2 tidak mengutip Ijadi Maghsoodi maupun Lewis; Ijadi hanya di III.1 baris 35. Status tetap TERBUKA (ditunda). [TSK-187: DIPUTUSKAN → D-126, "Pertahankan dan konfirmasi".] Butir terbuka kecil (bukan keputusan): koreksi A01 - frasa "belum diaudit a08" dalam pertanyaan hanya batas cakupan a08 pada TSK-181; audit sitasi III.1 (TSK-172) sudah dilakukan, tetapi apakah baris 35 (Ijadi Maghsoodi dkk.) diperiksa spesifik di TSK-172 BELUM diverifikasi A01/A13; tidak ada audit tambahan dijalankan.
```

```yaml
id: Q-B3-b
question: Lewis dkk.: daftar pustaka mengutip prosiding NeurIPS (hlm. 9459-9474) tetapi repo hanya punya arXiv v4. Kutip arXiv atau sediakan PDF prosiding?
affected:
- bab2/Daftar_Pustaka.md
- bab3/Bab_III_Draft.md
class: L3
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-12
refs:
- TSK-168
note: Menurut a02 (TSK-168).
```

```yaml
id: Q-B3-c
question: F-A07-0112 vs F-A08-0122a: frasa "paling sedikit mencakup" (KMK 1596/2024 hlm. 168 EP c menurut a08; "kata setidaknya tidak ada di sumber" menurut catatan paket bukti B3-06 yang dipakai a07). Bagaimana rumusan di bab3/Bab_III_Draft.md baris 17 diputuskan (F-A09-0304 mengusulkan "sekurang-kurangnya pada")?
affected:
- bab3/Bab_III_Draft.md
class: L3
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-12
refs:
- F-A07-0112
- F-A08-0122
- F-A09-0304
- TSK-171
- TSK-172
note: Konflik dua auditor, tidak dipilih A01 maupun A13. Perubahan di luar batas siklus otomatis D-106. Pembaruan TSK-188/189 (2026-11-12) - fakta tekstual dari a08 (read-only; cetak = PDF): KMK 1596/2024 hlm. 168 EP c berbunyi "Fokus pengkajian paling sedikit mencakup pada ketepatan waktu, keterbacaan, kelengkapan rekam medis dan isi rekam medis sesuai dengan peraturan perundangan." EP b hlm. 168: "Komite/tim secara berkala melakukan pengkajian rekam medis pasien secara berkala setiap tahun dan menggunakan sampel yang mewakili (rekam medis pasien yang masih dirawat dan pasien yang sudah pulang)." Maksud dan tujuan MRMIK 12 hlm. 167: "Pengkajian berfokus pada ketepatan waktu, kelengkapan, keterbacaan, keabsahan dan ketentuan lainnya ..." (tanpa "paling sedikit"). "setidaknya"/"sekurang-kurangnya" tidak ada di hlm. 167-168. Catatan paket bukti B3-06 yang dipakai a07 (F-A07-0112) tidak sesuai PDF; baris 17 memparafrasakan "isi rekam medis sesuai dengan peraturan perundangan" menjadi "kesesuaian isi dengan peraturan", dan "berdasarkan" berasal dari maksud dan tujuan; EP c ambigu tata bahasanya (fokus keempat atau keterangan atas kelengkapan). Ini fakta tekstual, BUKAN penilaian siapa benar. A01 mengajukan tiga opsi (pertahankan baris 17; pertahankan dan koreksi B3-06 oleh a02; sempurnakan kalimat ke bunyi sumber); pengguna TIDAK memilih (jawabannya hanya perintah /sesi-tutup). Status TETAP TERBUKA; baris 17 tidak diubah.
```

```yaml
id: Q-B3-d
question: F-A07-0107 diterapkan sementara lewat opsi A (kontras kelompok 3/RAG dinyatakan tidak dijawab penelitian ini). Opsi B (definisikan sumber retrieval di III.2) tetap terbuka; pilih A tetap atau B?
affected:
- bab3/Bab_III_Draft.md
- III.2
class: L3
pic: Pengguna
ask_to: Pengguna
status: DIPUTUSKAN → D-127
updated: 2026-11-12
refs:
- F-A07-0107
- TSK-171
- F-A07-0125
- D-127
- TSK-187
- TSK-180
note: Opsi A diterapkan atas arahan operasional A01 (jalur yang membatasi klaim); bukan keputusan D-. Pembaruan TSK-185 (2026-11-12) - a07 (F-A07-0125, INFO) mencatat bahwa III.2 kini mendefinisikan sumber retrieval = proposisi dari kedua dokumen (indeks gabungan), sehingga pertanyaan opsi A/B perlu dinilai ulang pengguna. TETAP TERBUKA; bukan keputusan. [TSK-187: DIPUTUSKAN → D-127, "Pertahankan keduanya".]
```

```yaml
id: Q-B3-e
question: Penanda [MENUNGGU KEPUTUSAN TIM: pemilik komponen rule-based] (bab3/Bab_III_Draft.md baris 49). Dokumen Penyelarasan baris 55 dan 169 menyatakan pengguna membangun rule-based dan AI/NLP; apakah itu final sehingga penanda ditutup?
affected:
- bab3/Bab_III_Draft.md
class: L3
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-12
refs:
- TSK-169
- Q-TEAM
note: Pembagian pemilik komponen belum disahkan tim menurut penanda. Pengamatan baris Penyelarasan berasal dari brief A01, tidak diverifikasi A13.
```

```yaml
id: Q-B3-f
question: Bab II II.1.1 menulis "sekurang-kurangnya setiap tahun" (KMK 1596) yang perlu diselaraskan dengan temuan a02/a08 pada Bab III. Diperbarui di Markdown dan docx resmi Bab II, atau dibiarkan?
affected:
- bab2/II.1_Rekam_Medis_dan_Dokumentasi_Klinis_dalam_Konteks_Klaim_JKN.md
- modular/TA1 bab 2.docx
- Draft-Bab1-Bab2.docx
class: L3
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-12
refs:
- Q-B3-c
note: Bergantung pada jawaban Q-B3-c. Docx adalah naskah resmi Bab II (pernyataan pengguna 2026-11-12).
```

```yaml
id: Q-B3-g
question: Keselarasan antarbab dan daftar pustaka: heading bab2/Daftar_Pustaka.md masih "(Bab I dan Bab II)"; Bab I baris 23 dan Bab III tidak mengeja ICD-10/ICD-9-CM; pasangan "presisi"/"precision" antarbab belum seragam. Diseragamkan oleh siapa dan kapan?
affected:
- bab2/Daftar_Pustaka.md
- bab1/Bab_I_Draft.md
- bab3/Bab_III_Draft.md
class: L3
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-12
refs:
- TSK-169
note: Pengamatan dari brief A01; tidak diverifikasi A13.
```

```yaml
id: Q-B3-h
question: Wong dkk. 2025 (pedoman onkologi ESMO) dipakai untuk pernyataan umum tentang keluaran AI di Bab III. Dipertahankan dengan konteks atau diganti?
affected:
- bab3/Bab_III_Draft.md
class: L3
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-12
refs:
- TSK-168
- TSK-172
note: Wong offset halaman +1446 terkonfirmasi a02.
```

```yaml
id: Q-B3-i
question: source/INDEKS.md usang (folder Domingues/Ijadi 16_, Faustini 14_, Newton 15_ tidak sesuai). Diperbaiki oleh pengguna atau sesi biasa?
affected:
- source/INDEKS.md
class: L3
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-12
refs:
- TSK-168
- F-A08-0123
note: Menurut a02. Paket bukti B3-40 (halaman 0,74 = 5490), B3-19, dan B3-22 (klaim bahasa tanpa halaman) perlu dikoreksi a02 (F-A08-0123).
```

```yaml
id: Q-B3-j
question: Jadwal pengerjaan temuan LOW/INFO Bab III (F-A07-0108..0111, F-A09-0280..0306, F-A08-0120, 0121, 0124) sekali di akhir bab; F-A07-0111 (batas blok "Cross-Episode Reconciliation") untuk a06. Disetujui?
affected:
- bab3/Bab_III_Draft.md
class: L3
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-12
refs:
- TSK-170
- TSK-171
- TSK-172
- D-106
note: Usulan A01. Pembaruan TSK-185 (2026-11-12) - cakupan diperluas ke temuan LOW/INFO III.2 (F-A07-0121, 0122, 0124, 0125, 0127; F-A08-0001..0005 versi III.2; F-A09-0403..0420 dan 14 LOW tanpa ID dari TSK-184). Pengguna memilih draf ke-3 "Tiga MEDIUM saja (Recommended)" sehingga LOW/INFO ditahan sampai akhir Bab III (arahan alur, bukan keputusan D-); pengerjaannya di luar batas D-106 memerlukan izin eksplisit pengguna. Status tetap TERBUKA.
```

```yaml
id: Q-B3-k
question: Struktur III.2.4 berupa daftar bernomor 10 langkah (9 langkah pada draf awal), sedangkan aturan pengguna mengutamakan prosa dan daftar poin hanya untuk tabel perbandingan karya terdahulu. Apakah langkah teknis III.2.4 dikecualikan, atau diubah menjadi prosa? Usulan a09: routing ke a10.
affected:
- bab3/Bab_III_Draft.md
- III.2.4
class: L3
pic: Pengguna
ask_to: Pengguna
status: DIPUTUSKAN → D-128
updated: 2026-11-12
refs:
- TSK-179
- TSK-184
- D-128
- TSK-187
note: Pertanyaan struktur dari a09 (TSK-179). Diputuskan TSK-187 - "Kecualikan, pertahankan daftar" (D-128); tanpa panggilan a10.
```

```yaml
id: Q-B3-l
question: Pengamatan a03 untuk pengguna pada III.2 (draf 3): (1) Langkah 2 tidak menyatakan siapa yang menetapkan isi definisi operasional dan kriteria kelalaian (penulis sendiri, pakar, atau pembimbing) dan tidak ditandai penanda; (2) perbandingan retrieval leksikal/embedding/hybrid (baris 76) hanya bersandar pada penalaran penulis, tanpa sumber terverifikasi untuk teks klinis berbahasa Indonesia; (3) kalimat "Keluaran LLM juga dapat berbeda antarpengulangan..." (baris 175) adalah klaim umum tanpa sumber; (4) Bab I I.4 butir 7 ("kombinasi union setelah deduplikasi") berbeda urutan dari I.5 dan III.2 (F-A07-0127). Bagaimana masing-masing ditangani?
affected:
- bab3/Bab_III_Draft.md
- bab1/Bab_I_Draft.md
class: L3
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-12
refs:
- TSK-182
- F-A07-0127
- F-A07-0128
note: Pengamatan a03 menurut brief A01; bukan keputusan. Butir (4) menyentuh Bab I yang naskah berlakunya Markdown (D-119); perubahan Bab I butuh keputusan pengguna.
```
