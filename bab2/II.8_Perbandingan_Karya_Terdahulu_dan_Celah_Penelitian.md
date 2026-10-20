# Bab II — Subbab II.8 (DRAFT 1)

> **Status:** draf kerja, belum ditinjau pembimbing. Hanya bagian "Naskah" dan "Daftar Pustaka (sementara)" yang masuk ke proposal. Bagian "Lampiran kerja" adalah alat bantu pemeriksaan dan tidak dihitung dalam batas 19 halaman.
>
> **Sifat subbab ini:** II.8 tidak memuat klaim baru dari PDF. Semua baris tabel dan semua celah dirangkum dari subbab II.1–II.7 yang klaimnya sudah dicek ke halaman PDF (`tools/claims_II1.json` sampai `tools/claims_II7.json`). Halaman sumber asli tidak dicantumkan dalam tabel demi ruang; rujukan halamannya ada pada subbab asal (Lampiran A tiap subbab) dan dipetakan di Lampiran A berkas ini.
>
> **Penanda yang perlu dijawab pengguna:** satu `[SESUAIKAN DENGAN BAB I]` pada subbab penutup.

---

## Naskah

## II.8 Perbandingan Karya Terdahulu dan Celah Penelitian

### II.8.1 Perbandingan Karya Terdahulu

Karya yang paling dekat dengan masalah penelitian ini pada tiap tema subbab sebelumnya dirangkum pada Tabel II.1. Perbandingan memakai data dan metode, hasil utama, dan keterbatasan karya itu bagi penelitian ini. Rincian dan halaman sumber ada pada subbab asal.

Tabel II.1. Perbandingan karya terdahulu yang terdekat dengan penelitian ini

| Karya | Data dan metode | Hasil utama | Keterbatasan bagi penelitian ini |
|---|---|---|---|
| Simbolon & Gani (2023) | Ulasan lima artikel tentang klaim rawat inap JKN yang *pending* | Pengodean tidak sesuai, berkas tidak lengkap, dan beda diagnosis DPJP–verifikator | Ringkasan sekunder; jenis ketidaksesuaian antardokumen tidak dirinci |
| Dietrich & Stubbert (2026) | 600 catatan pemulangan IGD (MIMIC-IV-ED); empat LLM | Akurasi 93,2–94,2%; temuan klinis tersulit | 500 dari 600 catatan bersisipan kesalahan; satu dokumen; tanpa pedoman |
| Skrabic dkk. (2026) | 102 laporan IGD; tiga model penalaran vs tiga dokter | Lokasi benar 65,7–79,2% vs dokter 48,0% | Tanpa catatan bebas kesalahan, sehingga positif palsu tidak terukur |
| Jaganathan dkk. (2025) | 3.372 catatan MIMIC-III; pengujian metamorfik pada model pengodean ICD | Lima kode teratas berubah pada 70–81% catatan | Satu model; mengukur stabilitas, bukan kebenaran |
| Wei dkk. (2026) | Disambiguasi singkatan; dataset CASI berbahasa Inggris | Akurasi 0,9228 (bersih) dan 0,7585 (asli) | Satu tolok ukur Inggris; bergantung pada inventori makna |
| Ijadi Maghsoodi dkk. (2026); Domingues (2026) | Tinjauan naratif hibrida; sistem berbasis aturan untuk onkologi prostat | Hibrida paling kredibel pada validasi dokumentasi; bukti prospektif jarang | Konseptual; yang diuji hanya aturan; tanpa perbandingan aturan vs aturan + AI |
| Zhang dkk. (2026) | RAG pada catatan perawatan lansia; Llama 3.1 8B | F1 jawaban 0,702/0,722 menjadi 0,946/0,953 | Dua tugas ekstraksi berbasis skema; tanpa penalaran temporal |
| Zeba dkk. (2026) | Pemeriksa fakta tanpa LLM; 3.786 proposisi MIMIC-III | Presisi 0,8904; *recall* 0,8234; F1 0,8556 | Bahasa Inggris, ICU; vonis biner |
| Azzam dkk. (2026) | Anonimisasi oleh LLM lokal; data sintetis dan MIMIC-III | Presisi 1,000 dan *recall* 0,936 (sintetis) | Hanya bahasa Inggris; data sintetis atau sudah diredaksi |
| van Koevorden dkk. (2026) | Ekstraksi LLM vs konsensus dua dokter; 60 pasien | Akurasi 74–90%; beda dokter–dokter 29,0% | Ekstraksi nilai; bahasa Belanda; satu pusat |

### II.8.2 Celah Penelitian

Dari 34 sumber yang dirujuk dalam bab ini, empat celah berulang. Pertama, tidak ada studi NLP atau AI yang menguji teks klinis berbahasa Indonesia, termasuk singkatan dan pengenal lokalnya (subbab II.2, II.3, II.6). Kedua, tidak ada yang memeriksa kesesuaian antardokumen dalam satu episode rawat inap sebelum klaim diajukan, misalnya membandingkan catatan perkembangan harian dengan ringkasan akhir atau memakai pedoman sebagai dasar temuan (II.1, II.3, II.5). Ketiga, di antara sumber yang dibaca, tidak ada yang membandingkan konfigurasi aturan saja dengan aturan ditambah AI/NLP berbasis RAG pada tugas ini, dan ketepatan kutipan bukti belum diperiksa secara otomatis (II.4, II.5). Keempat, acuan penilaian untuk audit, yaitu unit temuan, perlakuan kasus ambigu, dan ukuran kesepakatan penilai, belum dirancang pada sumber mana pun, padahal ketidaksepakatan antarpenilai dapat mencapai 29,0% pada ekstraksi klinis (II.7). Pernyataan "tidak ada" ini berlaku pada 34 sumber tersebut, bukan pada seluruh literatur. Penelitian ini mengisi celah itu dengan menguji audit dokumentasi rawat inap kebidanan dan anak berbahasa Indonesia terhadap pembanding, ukuran, dan ambang kegagalan yang ditetapkan sebelum eksperimen [SESUAIKAN DENGAN BAB I: rumusan pertanyaan dan ukuran keberhasilan].

---

## Daftar Pustaka (sementara)

> Tidak ada entri baru. Semua rujukan pada subbab ini sudah tercantum pada daftar pustaka II.1–II.7.

---

## Lampiran kerja (bukan bagian naskah)

### Lampiran A. Pemetaan baris tabel dan celah ke subbab asal

II.8 tidak memuat klaim baru dari PDF, jadi tidak ada berkas klaim sendiri (`claims_II8.json`). Setiap angka pada Tabel II.1 sudah diverifikasi ke halaman PDF pada subbab asalnya; tabel di bawah menunjuk lokasinya. Semua berkas klaim terkait lolos penuh (II.1 27/27, II.2 57/57, II.3 83/83, II.4 35/35, II.5 64/64, II.6 37/37, II.7 33/33).

| Baris Tabel II.1 | Subbab asal | Berkas klaim | Lokasi angka/klaim |
|---|---|---|---|
| Simbolon & Gani (2023) | II.1 | `claims_II1.json` | Lampiran A II.1, baris Simbolon & Gani (hlm. 72, 77) |
| Dietrich & Stubbert (2026) | II.3 | `claims_II3.json` | Naskah II.3.2 (hlm. 95, 97, 98); Lampiran B II.3 |
| Skrabic dkk. (2026) | II.3 | `claims_II3.json` | Naskah II.3.1 (hlm. 3, 4, 6); Lampiran B II.3 |
| Jaganathan dkk. (2025) | II.3 | `claims_II3.json` | Naskah II.3.3 (hlm. 4–5); Lampiran B II.3 |
| Wei dkk. (2026) | II.2 | `claims_II2.json` | Lampiran A II.2, baris Wei dkk. (hlm. 1, 5, 7, 9) |
| Ijadi Maghsoodi dkk. (2026); Domingues (2026) | II.4 | `claims_II4.json` | Lampiran A II.4 (hlm. 1, 2, 5–7, 9) |
| Zhang dkk. (2026) | II.5 | `claims_II5.json` | Lampiran A II.5, baris Zhang dkk. (hlm. 1, 5, 6, 11) |
| Zeba dkk. (2026) | II.5 | `claims_II5.json` | Lampiran A II.5, baris Zeba dkk. (hlm. 1, 10, 14, 15) |
| Azzam dkk. (2026) | II.6 | `claims_II6.json` | Lampiran A II.6, baris Azzam dkk. (hlm. 1, 12, 15) |
| van Koevorden dkk. (2026) | II.7 | `claims_II7.json` | Lampiran A II.7 (hlm. 1, 4, 7, 8) |

| Celah (II.8.2) | Subbab asal | Dasar |
|---|---|---|
| 1. Tidak ada studi NLP/AI pada teks Indonesia, termasuk singkatan dan pengenal lokal | II.2, II.3, II.6 | Kesimpulan tiap subbab; pemeriksaan ketiadaan `indonesia\|malay\|bahasa` pada teks PDF (II.2, II.5, II.6, II.7) |
| 2. Tidak ada pemeriksaan kesesuaian antardokumen dalam satu episode sebelum klaim diajukan | II.1, II.3, II.5 | II.1 (paragraf penutup), II.3.4, II.5.3 |
| 3. Tidak ada perbandingan aturan saja vs aturan + AI/NLP berbasis RAG pada tugas ini; ketepatan kutipan tidak diperiksa otomatis | II.4, II.5 | II.4.3, II.5.2–II.5.3 |
| 4. Acuan penilaian audit belum dirancang; disagreement 29,0% | II.7 | II.7.2; van Koevorden dkk. hlm. 4 |

### Lampiran B. Matriks ringkas untuk pemeriksaan konsistensi

Matriks per sumber ada pada Lampiran B tiap subbab (II.1–II.7); II.8 hanya memilih baris yang paling dekat dengan masalah penelitian.

### Lampiran C. Catatan peringatan dan penandaan

1. **Pemilihan baris tabel.** Kriteria: satu karya terdekat per tema, dengan angka yang sudah diverifikasi. Baris yang tidak dimasukkan demi ruang: Susilo dkk. 2025; Rachmawaty dkk. 2021; Nilasari & Soelistijanto 2026 (karya JKN/upcoding terdekat, tetapi tanpa data atau hasil); Du dkk. 2026; Mwogosi & Mambile 2026; Hou dkk. 2024; Lebeña dkk. 2025; Kumar, Woo, Elvas, Luo, Chen, Olex & McInnes, Jafarpour; Landolsi, Yang, Jia, Li, Sun, Waqas; Faustini, Tchouka; Becker. Bila pembimbing meminta tabel yang lebih lengkap, baris tambahan dapat diambil dari Lampiran B tiap subbab, dengan konsekuensi tambahan halaman.
2. **"34 sumber yang dirujuk".** Angka ini adalah jumlah entri unik pada daftar pustaka gabungan II.1–II.7. Beberapa sumber dibaca terarah, bukan seluruh isi (mis. bagian tertentu Kumar dkk., Chen dkk., Landolsi dkk., dan Waqas dkk.). Pernyataan "tidak ada" pada II.8.2 berlaku pada sumber-sumber ini, bukan seluruh literatur.
3. **Anggaran halaman:** render LibreOffice menghasilkan Bab II ± 19,03 halaman, termasuk teks panduan templat ± 0,45 halaman dan halaman terakhir yang hanya berisi tiga baris. Ini tepat di batas 19 halaman dan belum ada paragraf pembuka Bab II. Ukuran Word dapat berbeda sedikit. Opsi pemangkasan: (a) II.3 ± 0,8 halaman (paragraf Lebeña dkk. dan Jaganathan dkk.), (b) ganti teks panduan templat dengan paragraf pembuka singkat, (c) II.6 ± 0,2 halaman.
4. **Format tabel:** keterangan "Tabel II.1." diketik manual (bukan bidang SEQ), sehingga daftar tabel di Word tidak otomatis memuatnya dan perlu diperbarui manual. Tabel memakai huruf 10 pt, spasi tunggal, dan baris judul yang berulang. Ukuran dan format tabel mengikuti penilaian agent, bukan templat.
5. **Hak klaim "mengisi celah".** Kalimat terakhir II.8.2 menyatakan apa yang akan diuji penelitian ini, bukan hasil. Rumusan akhirnya harus disamakan dengan Bab I [SESUAIKAN DENGAN BAB I].
