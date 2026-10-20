# CONTEXT TRANSFER

> Berkas ini diperbarui di akhir setiap chat yang mengubah keputusan, progres, atau daftar referensi (instruksi pengguna). Pembaruan terakhir: sesi 1, 20 Oktober 2026 (draf II.3, II.1, II.2, II.4, II.5, dan II.6, semuanya dimasukkan ke `.docx` Utama). Letakkan isi berkas ini sebagai konteks awal chat berikutnya, bersama `CLAUDE.md` dan `RULES.md`.

## 1. PROJECT / CONVERSATION OVERVIEW

- Pengguna: **Danendra Shafi Athallah, NIM 13523136**, mahasiswa Teknik Informatika ITB. Proposal TA **individual** untuk capstone IF4091.
- Topik: **audit dokumentasi klaim BPJS pra-submit, kasus kebidanan dan anak rawat inap**. **Judul belum didapatkan, hanya topik.**
- Peran pengguna dalam tim (Breakdown, bagian 14): **AI/NLP Semantic Claim Intelligence** (analisis semantik, integrasi layanan AI eksternal, implementasi dan evaluasi RAG, pembentukan temuan dan bukti). Rekan: Abizzar (frontend/antarmuka), Raihaan (backend/database).
- Tugas agent: menulis **hanya Bab II (Kajian Pustaka)**, **satu subbab per chat**, maksimal **19 halaman** untuk seluruh Bab II.
- "Project knowledge" = **repository GitHub `danenftyessir/project-proposal`** (klarifikasi pengguna). Branch kerja: `claude/determined-davinci-ueb8i9`. Jangan membuat PR kecuali diminta.
- Bab I belum ada di repo (hanya panduan Bab I dan Breakdown). Rumusan RQ1–RQ4 diambil dari Breakdown, bukan dari Bab I final.

## 2. PRIMARY GOAL

Menulis Bab II proposal TA (konfirmasi pengguna) dalam bahasa Indonesia akademik sesuai `CLAUDE.md` dan `RULES.md`, berbasis PDF sumber yang benar-benar dibaca, dengan nomor halaman pada klaim tentang isi artikel.

## 3. SECONDARY GOALS

- (Confirmed) Memperbarui berkas ini di akhir setiap chat yang mengubah keputusan/progres/daftar referensi.
- (Confirmed) Menandai sumber yang PDF-nya belum ada di repo agar pengguna dapat mengunggahnya.
- (Inferred) Menyiapkan tabel perbandingan karya terdahulu (subbab penutup Bab II) dari matriks catatan literatur per subbab.

## 4. USER REQUIREMENTS & CONSTRAINTS

Kutipan kata-kata pengguna (aturan yang berlaku untuk semua chat):

- "Setiap klaim tentang isi paper harus diambil dari PDF di project knowledge, bukan dari ingatan atau ringkasan AI lain. Sertakan nomor halaman."
- "Jangan melebih-lebihkan temuan paper agar cocok dengan desain saya. Jika paper tidak mendukung klaim, katakan terus terang."
- "Jika PDF yang dibutuhkan tidak ada di project, katakan sumber mana yang perlu saya unggah."
- "Gaya sitasi sementara penulis-tahun (mis. Ancker dkk., 2025) sampai pedoman prodi diketahui."
- "Kerjakan satu subbab per chat ... dan maksimal total page halaman BAB 2 itu adalah 19 halaman."
- "Utamakan prosa, bukan daftar poin, kecuali untuk tabel perbandingan karya terdahulu."
- "Jika ada yang ambigu atau belum diputuskan, tanyakan satu hal paling penting, jangan menebak."
- "Daftar referensi yang berlaku adalah yang tercantum di sana; jangan menambah sumber baru tanpa saya minta."
- "Di akhir setiap chat yang mengubah keputusan, progres, atau daftar referensi, perbarui file dengan Context Transfer sebelum menutup chat."

Aturan sumber (klarifikasi pengguna, chat 1):
- `source/` (langsung di bawahnya) = dokumen yang disebut di `Sumber Literatur Bab 2.pdf`.
- `source/external/` = sumber yang ditemukan **teman capstone** pengguna. **Tidak dipakai** kecuali artikelnya sama dengan yang tercantum di `Sumber Literatur Bab 2.pdf` atau di rujukan Breakdown bagian 15.

Aturan tulis dari `CLAUDE.md`/`RULES.md` yang paling sering berlaku: baca ulang `RULES.md` bagian 4 (studi literatur), 6 (bahasa), 8 (argumen ilmiah, 10 prinsip), 8.5 (50 ciri AI slop sebagai diagnostik). Jangan mengarang referensi; tandai `[PERLU VERIFIKASI SUMBER]`, `[PERLU VERIFIKASI BENTUK BAKU]`, `[DATA BELUM TERSEDIA]`; sitasi parafrasa tetap wajib; jangan menyalin keluaran parafrasa AI; kutipan langsung maksimal satu paragraf; istilah asing yang belum baku ditulis miring; hindari penggantian massal; periksa koma, kata depan `di`/`ke`/`dari`, imbuhan.

**Templat yang dipakai untuk naskah final = `Template-Proposal-IF4091-Capstone-Utama-2026.docx`** (kata pengguna: berkas itu ada di `C:\Users\HYPE R Series\OneDrive - Institut Teknologi Bandung\Documents\ITB\Semester 7\IF4091 Penyusunan Proposal\`; sesi agent berjalan di kontainer cloud sehingga **tidak dapat membaca atau menulis ke jalur itu**, hanya salinan di repo yang kebetulan identik secara bita dengan `... - Copy.docx`). Templat Utama punya Bab I (Pendahuluan), **Bab II Kajian Pustaka**, Bab III (Analisis Domain, Kebutuhan, Gambaran Umum Solusi, Pembagian Peran Tim), Bab IV (Jadwal, Risiko). Intro Bab II pada templat Utama menyebut kajian untuk "seluruh anggota tim", jadi Bab II dapat digabung dengan bagian rekan. Pada sesi 1 agent awalnya memakai struktur templat Individu dan keliru menyebut templat Utama "bukan untuk berkas ini"; itu sudah dikoreksi. Gaya dan margin templat Utama sama dengan Individu. Format (dibaca dari `styles.xml`/`sectPr` templat): Times New Roman 12 pt; spasi 1,5 (line 360); spasi sebelum/sesudah paragraf 6 pt; rata kiri-kanan; A4; margin kiri-kanan 1800 twips (± 3,17 cm), atas-bawah 1440 twips (2,54 cm). Judul bab huruf kapital tebal 14 pt, mulai halaman baru. Penomoran heading "II.1", gambar/tabel "Gambar II.1"/"Tabel II.1". Fungsi Bab II menurut templat: pemahaman teori/pekerjaan terkait, informasi pekerjaan pihak lain, dan **gap** terhadap rumusan masalah. Slide panduan: "Fokuskan pada siapa, menggunakan metode apa, dan hasilnya bagaimana", sebutkan kelebihan/kekurangan, bab cukup singkat tetapi padat.

Tenggat: slide "Tanggal-Tanggal Penting" (halaman 17 berkas `7_IF4091_PenulisanStudiLiteratur_2026_Okt.pdf`) menyebut **20 Oktober 2026 = pengumpulan hasil studi literatur (Bab II)**; Bab I 10 November 2026; Bab III (maks. 3 halaman) 1 Desember 2026; proposal lengkap 16 Desember 2026; seminar 28 Desember 2026 – 15 Januari 2027.

## 5. KEY DECISIONS

1. **Konvensi sitasi sementara**: penulis-tahun, `dkk.` untuk tiga penulis atau lebih, nomor halaman `hlm.` pada klaim isi artikel. Untuk artikel Elsevier bernomor artikel, `hlm.` = halaman berkas PDF (halaman 1 = halaman pertama PDF). Untuk Dietrich dan Stubbert (2026), `hlm.` = nomor cetak jurnal (95–101). *Alasan:* artikel bernomor artikel tidak punya nomor halaman cetak. *Status:* sementara sampai pedoman prodi diketahui. Daftar pustaka memakai pola contoh templat dan ditandai `[FORMAT AKHIR PERLU DIKONFIRMASI]`.
2. **Kebijakan sumber** (lihat bagian 4): hanya `source/` + artikel `external/` yang identik dengan yang tercantum di daftar atau Breakdown. *Final* (dari pengguna).
3. **Urutan penulisan sesi 1: II.3 lebih dulu, lalu II.1.** II.3 dijalankan dari usulan agent tanpa persetujuan pengguna (menyalahi aturan "jangan menebak"); pengguna mempertanyakannya, agent mengusulkan II.1 (urut), dan pengguna menjawab "lanjutkan" sehingga II.1 ditulis **di chat yang sama** (melonggarkan aturan satu subbab per chat atas kehendak pengguna). *Status:* kerangka II.1–II.8 tetap usulan agent, belum dikonfirmasi.
4. **Kerangka Bab II (usulan agent, belum dikonfirmasi pengguna)**, total ≤ 19 halaman:
   - II.1 Dokumentasi klinis dan klaim JKN (1,5 hlm)
   - II.2 NLP/LLM pada teks klinis, singkatan lokal, penalaran temporal (3)  ← **ditulis (judul subbab: II.2.1 Tugas dan Model Bahasa untuk Teks Klinis; II.2.2 Singkatan, Normalisasi Istilah, dan Penalaran Temporal; II.2.3 Sintesis dan Celah)**
   - II.3 Audit otomatis dokumentasi dan pengodean (3,5)  ← **ditulis**
   - II.4 Pendekatan hibrida berbasis aturan dan AI/NLP (2)  ← **ditulis (II.4.1 Kekuatan dan Batas Sistem Berbasis Aturan; II.4.2 Pola Hibrida dan Bukti yang Tersedia; II.4.3 Sintesis dan Celah)**
   - II.5 RAG, penjangkaran bukti, halusinasi (4)  ← **ditulis, hanya ± 2,6 halaman (II.5.1 RAG pada Teks Klinis; II.5.2 Penjangkaran Bukti dan Pengecekan Keluaran; II.5.3 Sintesis dan Celah)**
   - II.6 De-identifikasi untuk layanan AI eksternal (1,5)  ← **ditulis, ± 1,72 halaman (II.6.1 Pendekatan De-identifikasi dan Bukti yang Tersedia; II.6.2 Sintesis dan Celah)**
   - II.7 Evaluasi sistem NLP klinis (1,5)
   - II.8 Tabel perbandingan karya terdahulu dan celah penelitian (2) — dikerjakan terakhir
   Literatur *alert fatigue* dan *knowledge graph* sengaja dikeluarkan (lebih dekat ke antarmuka Abizzar atau eksploratif); dapat dibalik oleh pengguna. Penomoran heading memakai angka Romawi mengikuti templat (pengguna menulis "2.1" secara kasual). Judul II.1–II.3 sudah terisi di `.docx`; judulnya usulan dan belum dikonfirmasi.
5. **Posisi sumber di II.3**: Lebeña dkk. (2025) hanya diberi porsi kecil dan disebut apa adanya (prediksi diagnosis berikutnya, bukan audit), karena klaim relevansi di `Sumber Literatur Bab 2.pdf` ("paling dekat dengan skenario CPPT→kode") tidak terdukung isi artikel.
6. **Alur kerja (instruksi pengguna, chat 1 lanjutan): tulis dulu di Markdown, naskah final di `.docx` templat Utama.** Naskah ada di `bab2/*.md`; tabel verifikasi dan catatan peringatan dipisah di "Lampiran kerja" dan tidak ikut dihitung dalam 19 halaman. `.docx` dibangun otomatis dari Markdown ke salinan templat Utama di repo (gaya Heading 2/3, Normal, daftar pustaka, penomoran otomatis), disimpan sebagai berkas baru **tanpa menimpa templat**: `bab2/Proposal-IF4091-Capstone-Utama-2026_Draft-Bab2.docx`. Pengguna menyalin/menimpa ke berkas OneDrive-nya sendiri.
7. **Sumber II.1 (keputusan agent, dalam batas aturan pengguna):** hanya Susilo dkk. 2025, Rachmawaty dkk. 2021, Nilasari & Soelistijanto 2026 (dari `source/`) dan Simbolon & Gani 2023 (dari `source/external/`, karena dirujuk Breakdown bagian 15). Septiono dkk. 2026, Sambodo dkk. 2023, dan Barsasella dkk. 2021 tidak dipakai (tidak relevan dengan dokumentasi/klaim; dua yang terakhir tidak dibaca). Permenkes di `external/` tidak dipakai tanpa persetujuan. Muroli dkk. (2020) hanya disebut sebagai kutipan sekunder dari Simbolon & Gani (PDF aslinya tidak ada) dan tidak masuk daftar pustaka.

8. **Sumber II.2 (keputusan agent, dalam batas aturan pengguna):** delapan PDF dari `source/` yang dibaca: Luo dkk. 2024, Elvas dkk. 2025, Kumar dkk. 2026, Woo dkk. 2026 (tugas dan model), Wei dkk. 2026 dan Chen dkk. 2026 (singkatan, normalisasi), Olex & McInnes 2021 dan Jafarpour dkk. 2025 (temporal, teks panjang). Kayira dkk. tidak tersedia. Tidak ada sumber dari `external/`. Bagian 6.1 Kumar dkk. (sistem berbasis aturan, hlm. 12) sengaja dicadangkan untuk II.4. Definisi *large language model* (LLM) kini di II.2.1; II.3 diubah menjadi "empat LLM" tanpa mendefinisikan ulang.

9. **Pengguna menjawab "lanjutkan" tanpa memilih opsi anggaran halaman.** Agent menafsirkannya sebagai lanjut ke subbab berikutnya dalam urutan (II.4) dan **menunda pemangkasan II.3 dan penggantian teks panduan templat sampai semua subbab selesai ditulis**, karena panjang akhir II.5 belum diketahui; tidak ada isi yang dihapus. *Status:* pengguna belum memutuskan.
10. **Sumber II.4 (keputusan agent, dalam batas aturan pengguna):** Domingues 2026 dan Ijadi Maghsoodi dkk. 2026 (dibaca penuh), ditambah Kumar dkk. bagian 6.1 (hlm. 12) dan Chen dkk. hlm. 13 yang sudah ada di daftar II.2. **Maleki dkk. (analog terdekat menurut daftar sumber) tidak ada di repo**; naskah hanya menyebut keberadaan artikel berdasarkan judul di daftar, tanpa nama penulis dan isi, ditandai `[PERLU VERIFIKASI SUMBER]`. Tidak ada sumber dari `external/`.

11. **Pengguna menjawab "lanjutkan" lagi tanpa memilih opsi anggaran.** Agent melanjutkan ke II.5 (urut) dan menjaganya mendekati 3 halaman. Hasilnya ± 2,6 halaman (alokasi 4), sehingga selisih anggaran praktis tertutup tanpa memangkas II.3 (sisa ± 4,9 halaman untuk II.6–II.8 yang dialokasikan 5,0). Pemangkasan II.3 dan penggantian teks panduan templat tetap opsi untuk memberi ruang.
12. **Sumber II.5 (keputusan agent, dalam batas aturan pengguna):** delapan PDF dari `source/` yang dibaca penuh/terarah: Yang dkk. 2026, Landolsi dkk. 2026, Zhang dkk. 2026, Jia dkk. 2026, Li dkk. 2026 (RAG), Zeba dkk. 2026, Sun dkk. 2025, Waqas dkk. 2026 (halusinasi dan pengecekan). Tidak ada sumber dari `external/`. Tu dkk. (JMIR 2026), Xiong dkk. 2024, Soroush dkk. 2024, dan Ben Abacha dkk. 2025 tidak ada di repo.

13. **Pengguna menjawab "lanjut" lagi tanpa memilih opsi anggaran.** Agent melanjutkan ke II.6 (urut). **Sumber II.6:** Faustini dkk. 2026, Azzam dkk. 2026, Tchouka dkk. 2024 (semuanya dari `source/`, dibaca terarah dari PDF). Tidak ada sumber dari `external/`.

## 6. PROGRESS STATUS

### Completed
- Membaca `CLAUDE.md`, `RULES.md` (seluruhnya), Breakdown (11 hlm), `Sumber Literatur Bab 2.pdf` (12 hlm), templat individu, panduan studi literatur, informasi umum TA, panduan Bab I.
- Memetakan 46 PDF di `source/` ke daftar literatur (lihat bagian 8) dan memeriksa bahwa semuanya berteks penuh (bukan hanya abstrak).
- **Draf 1 subbab II.3** (1.365 kata isi naskah; **terukur ± 4,3 halaman** pada templat Utama dari render LibreOffice dengan Liberation Serif yang metrik-kompatibel dengan Times New Roman, melebihi alokasi 3,5; bukan ukuran Word) ditulis dari tujuh PDF yang dibaca penuh; 100 klaim/halaman dicek otomatis ke teks halaman PDF (empat awalnya gagal karena pemenggalan kata hasil ekstraksi, lalu dicek manual dan benar).
- **Draf 1 subbab II.1 Dokumentasi Klinis dan Klaim JKN** (514 kata; **terukur ± 1,54 halaman**, sesuai alokasi 1,5) ditulis dari empat PDF yang dibaca penuh (Simbolon & Gani dibaca juga dari gambar halaman karena teks PDF tercampur dua kolom); 27 klaim/halaman dicek otomatis ke teks halaman PDF (lima awalnya gagal karena offset halaman dan pemenggalan kata; halaman dikoreksi dan dicek ulang, semuanya cocok). `.docx` dibangun ulang dengan II.1 dan II.3 (II.2 penampung), lolos validasi, render 25 halaman. Bab II terisi ± 6,38 halaman termasuk judul bab, teks panduan templat, dan penampung II.2; isi II.1 + II.3 = ± 5,84 halaman.
- **Draf 1 subbab II.2 NLP dan LLM pada Teks Klinis** (1.005 kata isi naskah; **terukur ± 3,08 halaman**, sesuai alokasi 3) ditulis dari delapan PDF yang dibaca penuh; 57 klaim/halaman dicek otomatis ke teks halaman PDF (semua cocok setelah `norm()` pada pemeriksa diperbaiki untuk tanda pisah lunak + jeda baris, dan dua frasa uji lama diluruskan). Ketiga berkas klaim dijalankan ulang: II.1 27/27, II.2 57/57, II.3 83/83. `.docx` dibangun ulang dengan II.1, II.2, II.3 (19 entri pustaka), lolos validasi, render 28 halaman. Bab II terisi ± 9,3 halaman (halaman 13–22 render, halaman terakhir ± sepertiga) termasuk judul bab dan teks panduan templat (± 0,45 halaman); isi II.1 + II.2 + II.3 = ± 8,92 halaman.
- **Draf 1 subbab II.4 Pendekatan Hibrida Berbasis Aturan dan AI/NLP** (676 kata isi naskah; **terukur ± 2,18 halaman**, alokasi 2) ditulis dari dua PDF baru (Domingues; Ijadi Maghsoodi dkk.) ditambah dua bagian dari Kumar dan Chen; 35 klaim/halaman dicek otomatis (semua cocok; satu klaim Domingues melintasi halaman 3 dan 5 karena halaman 4 hanya gambar). Ketiga berkas klaim sebelumnya tetap lolos (27/27, 57/57, 83/83). `.docx` dibangun ulang dengan II.1–II.4 (21 entri pustaka), lolos validasi, render 30 halaman. **Bab II kini ± 11,5 halaman** (halaman 13–24 render) termasuk teks panduan templat ± 0,45 halaman.
- **Draf 1 subbab II.5 RAG, Penjangkaran Bukti, dan Halusinasi** (867 kata isi naskah; **terukur ± 2,61 halaman**, alokasi 4) ditulis dari delapan PDF; 64 klaim/halaman dicek otomatis (semua cocok). Semua lima berkas klaim lolos penuh (27/27, 57/57, 83/83, 35/35, 64/64). `.docx` dibangun ulang dengan II.1–II.5 (29 entri pustaka), lolos validasi, render 34 halaman. **Bab II kini ± 14,1 halaman** (termasuk teks panduan templat ± 0,45 halaman); sisa ± 4,9 halaman untuk II.6–II.8 (alokasi 1,5 + 1,5 + 2).
- **Draf 1 subbab II.6 De-identifikasi untuk Layanan AI Eksternal** (564 kata isi naskah; **terukur ± 1,72 halaman**, alokasi 1,5) ditulis dari tiga PDF; 37 klaim/halaman dicek otomatis (semua cocok). Enam berkas klaim lolos penuh (27, 57, 83, 35, 64, 37). `.docx` dibangun ulang dengan II.1–II.6 (32 entri pustaka), lolos validasi, render 35 halaman. **Bab II kini ± 15,9 halaman**; sisa ± 3,1 halaman untuk II.7 (1,5) dan II.8 (2,0) = 3,5, jadi kurang ± 0,4 halaman.

### In Progress
- Tidak ada. II.1–II.6 menunggu tinjauan pengguna.

### Not Started
- II.7, II.8; paragraf pembuka Bab II (tujuan bab menurut templat); penyatuan daftar pustaka Bab II (sementara 32 entri hasil gabungan II.1–II.6); pemformatan akhir di Word (daftar isi, halaman).

### Blocked
- Subbab yang membutuhkan PDF yang belum ada (lihat bagian 12).
- Gaya sitasi final dan struktur Bab II final menunggu pembimbing/pedoman prodi.

### Rejected / Abandoned
- Menjadikan klaim relevansi Lebeña dkk. di daftar literatur sebagai dasar naskah (ditolak karena tidak terdukung artikel).
- Memasukkan perhitungan presisi hipotetis (presisi ≈ 0,57 bila ketidaksesuaian hanya 10% dokumen) ke naskah; hanya ada di Lampiran C sebagai catatan penulis.

## 7. IMPORTANT CONVERSATION HISTORY

1. Pesan awal pengguna memuat konteks, aturan sitasi, cara kerja, tetapi **nama berkas rujukan kosong** ("Baca file  di project knowledge") dan **subbab yang dikerjakan tidak disebut**.
2. Balasan agent: belum menulis; melaporkan temuan (tidak ada berkas progres, 13 PDF daftar tanpa PDF, 6 rujukan Breakdown tanpa PDF, tenggat 20 Oktober), mengusulkan kerangka, dan menanyakan satu hal: subbab mana.
3. Pengguna mengoreksi: project knowledge = repo GitHub; `source/` = dokumen di Sumber Literatur Bab 2; `external/` = temuan teman capstone. Pengguna **tidak** menjawab pertanyaan subbab.
4. Agent memeriksa semua branch (hanya `main`; tidak ada berkas progres/Context Transfer di repo), lalu menjalankan usulan II.3.
5. Temuan penting saat membaca: lihat bagian 12 (Lebeña; arah akronim Jaganathan; kriteria kegagalan Jaganathan; angka per kategori Skrabic tidak konsisten antarbagian; Skrabic menyebut "five categories" tetapi hanya mendaftar empat).

## 8. FILES & RESOURCES

Berkas di repo (semua di root kecuali dicatat):
- `CLAUDE.md`, `RULES.md` — aturan penulisan wajib (dibaca penuh).
- `[REVISI] Breakdown Proposal (2).pdf` — rancangan TA (bukan proposal formal): RQ1–RQ4, ruang lingkup, rule-based vs AI/NLP, alur RAG, data/evaluasi, tim, pijakan literatur awal (bagian 15), daftar hal yang perlu dikonfirmasi (bagian 17–18).
- `Sumber Literatur Bab 2.pdf` — daftar awal ± 60 sumber (hasil penelusuran ScienceDirect), 9 tema + kerangka 7 kelompok; belum diverifikasi penuh. Tanda "bold merah" pada daftar tidak terbawa ke PDF.
- `Template-Proposal-IF4091-Capstone-Utama-2026.docx` (root repo; salinan identik `... - Copy.docx`) — **templat yang dipakai untuk naskah final**. `template/Template-Proposal-IF4091-Capstone-Individu-2026.docx` — templat individu (struktur Bab III–IV berbeda); tidak dipakai.
- **`bab2/Proposal-IF4091-Capstone-Utama-2026_Draft-Bab2.docx`** — templat Utama berisi II.1–II.6, daftar pustaka Bab II (32 entri); bagian lain templat tidak diubah kecuali dua paragraf pemisah halaman ganda di akhir Bab II yang dihapus (menyebabkan halaman kosong) dan contoh gambar/tabel/pustaka yang diganti. Lolos validasi skema; render 35 halaman. **Daftar isi, daftar gambar, dan daftar tabel masih berisi hasil lama** sampai diperbarui di Word (berkas diatur agar Word menawarkan pembaruan saat dibuka; atau Ctrl+A lalu F9).
- `7_IF4091_PenulisanStudiLiteratur_2026_Okt.pdf`, `3_IF4091_Informasi Umum TA_2026 Sept.pdf`, `9_IF4091_ProposalTA_Bab1_2026_Okt.pdf`, `5_...EfficientReading...`, `12_...Bahasa Indonesia...`, `1_...Pengantar Kuliah...` — materi kuliah.
- **`bab2/II.1_Dokumentasi_Klinis_dan_Klaim_JKN.md`** — draf 1 II.1 (naskah, daftar pustaka sementara, Lampiran A tabel verifikasi, B matriks catatan literatur, C catatan peringatan).
- **`bab2/II.2_NLP_dan_LLM_pada_Teks_Klinis.md`** — draf 1 II.2 (naskah, daftar pustaka sementara 8 entri, Lampiran A tabel verifikasi, B matriks catatan literatur, C 16 catatan peringatan).
- **`bab2/II.6_Deidentifikasi_untuk_Layanan_AI_Eksternal.md`** — draf 1 II.6 (naskah, daftar pustaka sementara 3 entri, Lampiran A tabel verifikasi, B matriks, C 8 catatan peringatan).
- **`bab2/II.5_RAG_Penjangkaran_Bukti_dan_Halusinasi.md`** — draf 1 II.5 (naskah, daftar pustaka sementara 8 entri, Lampiran A tabel verifikasi, B matriks, C 12 catatan peringatan).
- **`bab2/II.4_Pendekatan_Hibrida_Berbasis_Aturan_dan_AI-NLP.md`** — draf 1 II.4 (naskah, daftar pustaka sementara 2 entri baru, Lampiran A tabel verifikasi, B matriks, C 10 catatan peringatan).
- **`bab2/II.3_Audit_Otomatis_Dokumentasi_dan_Kode_Diagnosis.md`** — draf 1 II.3 (naskah + daftar pustaka sementara + Lampiran A tabel verifikasi klaim, B matriks catatan literatur untuk II.8, C catatan peringatan).
- `tools/` — `build_docx.py` (Markdown subbab → `.docx` templat Utama), `verify_claims.py` + `claims_II1.json`/`claims_II2.json`/`claims_II3.json`/`claims_II4.json`/`claims_II5.json`/`claims_II6.json` (cek frasa kutipan ke halaman PDF; kamus PDFS kini memuat 32 sumber). Setelah perbaikan `norm()` dan frasa U3b, berkas lolos penuh (27/27, 57/57, 83/83, 35/35, 64/64, 37/37); catatan lama tentang empat entri FAIL di `claims_II3.json` tidak berlaku lagi bila dijalankan ulang (nama yang dulu dicek manual: S2, U3b, U14, M2).
- `CONTEXT_TRANSFER.md` — berkas ini.

Peta 46 PDF `source/` (`1-s2.0-<ID>-main.pdf`; judul dan tim dari metadata PDF, **tahun dari daftar kecuali tujuh artikel II.3 yang sudah diperiksa**):
S2667305326000724 Kumar dkk. 2026 · S0020748925003323 Woo dkk. 2026 · S1386505625002667 Elvas dkk. 2025 · S0933365724001465 Luo dkk. 2024 · **S1386505626000560 Skrabic dkk. 2026** · **S266676492600007X Du dkk. 2026** · **S2211883726000614 Mwogosi & Mambile 2026** · **S235264832500025X Jaganathan dkk. 2025** · **S2352914825000255 Lebeña dkk. 2025** · **S0957417424003841 Hou dkk. 2024** · S1532046425001352 SynthMedic (Grazhdanski dkk. 2025) · S2352396426001295 Mehri dkk. 2026 · S1386505624003174 Schwieger dkk. 2024 · S1386505624004192 Kleebayoon & Wiwanitkit 2025 (1 halaman) · S0952197626021962 Landolsi dkk. 2026 · S2666379126003447 Yang dkk. 2026 (RAG in medicine) · S1532046426000778 Zhang dkk. 2026 · S1386505626000791 Jia dkk. 2026 · S0720048X26000823 Li dkk. 2026 · S0957417426018786 Zeba dkk. 2026 · S1532046425000954 Sun dkk. 2025 · S2949719126000361 Waqas dkk. 2026 · S1532046421001131 Olex & McInnes 2021 · S0933365725002167 Jafarpour dkk. 2025 · S0025619623002549 Sangal dkk. 2023 · S1532046423001181 Cánovas-Segura dkk. 2023 · S1386505626004752 Boccio dkk. 2026 · S1386505617301600 Page dkk. 2017 · S1386505625004423 Faustini dkk. 2026 · S0950705126007604 Azzam dkk. 2026 · S2667305324000905 Tchouka dkk. 2024 · S1532046426001097 Wei dkk. 2026 · S1532046426000298 Chen dkk. 2026 · S1386505625003612 Domingues 2026 · S2211883726001401 Ijadi Maghsoodi dkk. 2026 · S294985622500090X Susilo dkk. 2025 · S2210778926000723 Septiono dkk. 2026 · S0277953623002782 Sambodo dkk. 2023 · S0306457326004619 KG-ACE (Sun dkk., daftar menyebut Januari 2027) · S0950705126013274 Syeda & Reddy 2026 · S1532046426000316 CTKGR (Yang dkk. 2026) · S1386505625002266 Becker dkk. 2025 (CARDIO:DE) · S2949820126000378 van Koevorden dkk. 2026 · S1877050926029406 Nilasari & Soelistijanto 2026 · S0213911121003071 Rachmawaty dkk. 2021 · S1386505621001957 Barsasella dkk. 2021.
(Cetak tebal = sudah dibaca penuh dan dipakai di II.3.)

`source/external/` (temuan teman; **jangan dipakai tanpa persetujuan**, kecuali tiga yang identik dengan rujukan tim): *Automated auditing of emergency department documentation using* = **Dietrich & Stubbert 2026 (dipakai di II.3, tercantum di daftar)**; *faktor-faktor yang mempengaruhi pending rawat inap* = Simbolon & Gani 2023 (rujukan Breakdown bag. 15); *Effects of workload ... alert fatigue* = Ancker dkk. 2017 (rujukan Breakdown bag. 15). Duplikat dari daftar: *Clinical Decision Support Moving Beyond* (= Sangal dkk.), *Meaningful time-related aspects* (= Cánovas-Segura dkk.). Lainnya milik rekan: Permenkes 26/2021 (INA-CBG), Permenkes 24/2022 (rekam medis), Gao dkk. (npj Digit Med, pengodean kolaboratif manusia-AI), Parambath dkk. (JMIR Hum Factors), Vasconcelos dkk., Kim dkk. (reliance LLM), Goddard dkk. (automation bias), SUS (Brooke), Tricorder, W3C PROV-DM, HL7 FHIR Provenance, Statecharts (Harel), Truth maintenance system (Doyle), ISO 9241-210, ACDIS/AHIMA query practice, Peffers dkk. (DSR), Nielsen (heuristik), Tonekaboni dkk., Spacco dkk. (defect warnings), Amershi dkk., Bansal dkk., rekam medis RS Denpasar.

PDF yang **perlu diunggah pengguna** bila subbab terkait dikerjakan (belum ada di repo):
- Dari daftar (13): Kayira dkk. (JMIR AI 2026); Kim, Lee, Yoon (JMIR Med Inform 2026, radiologi); Seo, Kim, Kim (JMIR 2026); Tung, Gill, Chong (JMIR 2024); Tu, Shi, Wang (JMIR Med Inform 2026); Newton dkk. (JMIR 2026); Gani dkk. (JMIR 2025); **Maleki dkk. (J Health Organ Manag 2026; analog terdekat hibrida rule-based + ML untuk klaim asuransi)**; Gaudet-Blavignac dkk. (JMIR 2026); Mohanty dkk. (bab buku 2027); Singh dkk. (JMIR Med Inform 2025); Lathifah dkk. (Enfermería Clínica 2020); Fahlevi dkk. (J Account Organ Change 2021).
- Dari Breakdown bagian 15 (6): Roy dkk. 2005; Soroush dkk. 2024; Ben Abacha dkk. 2025; Williams dkk. 2025; Xiong dkk. 2024; Saputra & Galih 2026.
Pengguna harus mengunggah ulang berkas yang tidak ada di repo; agent tidak boleh menyebut isinya sebelum itu.

## 9. IMPORTANT PEOPLE / ENTITIES

- Danendra Shafi Athallah (pengguna); Abizzar (frontend); Raihaan (backend/database).
- Dosen/pembimbing materi: Satrio Adi Rukmono, S.T., M.T. (materi bimbingan 15 Oktober 2026 di `RULES.md` bagian 8.4). Pembimbing TA pengguna: belum disebut.
- Objek studi: RSIA (rumah sakit ibu dan anak) sumber data; BPJS Kesehatan/JKN; INA-CBG; CPPT; resume medis akhir.
- Istilah tim: temuan, "bukti belum cukup", "belum dapat dinilai", label acuan, hold-out per pasien.

## 10. IMPORTANT FACTS / NUMBERS / SPECIFICATIONS

Dari Breakdown (rujukan konteks, bukan hasil proyek): data pending Mei 2026: 49 klaim pending senilai Rp 89.928.800 (18 rawat inap Rp 81.626.000; 31 rawat jalan Rp 8.302.800); target awal 150–300 kasus; metrik precision, recall, F1, confusion matrix; konfigurasi dibandingkan: rule-based saja vs rule-based + AI/NLP berbasis RAG.

RQ (Breakdown bagian 2):
- RQ1 Jenis ketidaksesuaian CPPT, resume, dokumen pendukung yang relevan; mana rule-based, mana AI/NLP.
- RQ2 Rancangan pemeriksaan gabungan rule-based dan AI/NLP berbasis RAG, penyajian temuan berbukti yang tidak mengganggu pencatatan.
- RQ3 Akurasi sistem dibanding label tenaga ahli; perbedaan rule-based saja vs gabungan.
- RQ4 Penilaian tenaga ahli terhadap kejelasan alasan, bukti, relevansi temuan, referensi RAG.

Angka kunci tujuh sumber II.3 (semua sudah dicek ke halaman; rincian di Lampiran A berkas II.3):
- Dietrich & Stubbert 2026 (hlm. 95–100): 600 catatan, 500 bersisipan, 100 tanpa kesalahan; akurasi 93,2–94,2%; presisi 98,3–99,1%; spesifisitas 92,0–96,0%; F1 temuan klinis 0,75–0,84.
- Skrabic dkk. 2026: 102 laporan; lokasi benar 65,7–79,2% (o3 79,2%; DeepSeek 72,5%; GPT-OSS 65,7%); dokter 48,0% (49/102).
- Du dkk. 2026: 48.492 rekam, 7.000 pasien; sum-F1 0,7417; BERT dengan penjelasan 0,7287; Llama 3.3 0,3785; risiko rendah/sedang/tinggi 36,99%/45,9%/17,11%.
- Mwogosi & Mambile 2026: 17 studi; sensitivitas rata-rata 64,5% (sebagian proksi); metastasis tulang 76,5% vs 89,2%.
- Hou dkk. 2024: F1 makro 0,688; F1 mikro 0,727 (50 kode teratas MIMIC-III).
- Lebeña dkk. 2025: P@5 72,34%; P@20 77,49%; hingga 2% lebih baik daripada model terpisah; 46% muat 512 token; >95% tanpa pemotongan pada 1.024 token.
- Jaganathan dkk. 2025: 3.372 catatan uji; kegagalan 70–81%; akronim 20 teratas 80,7%; hapus istilah gender 55,7%.
DOI ketujuh artikel ada di Lampiran C berkas II.3.

Angka kunci sumber II.6 (semua sudah dicek ke halaman; rincian di Lampiran A berkas II.6; bahasa Indonesia tidak muncul pada ketiga PDF):
- Faustini dkk. 2026: 83 dari 734 artikel (2015–2024); mayoritas bahasa Inggris; campur kode dan kelangkaan dataset; Presidio kesulitan nama Asia Tenggara dan F1 LLM 0,33 vs 0,98 adalah laporan studi lain (hlm. 1, 5, 6).
- Azzam dkk. 2026: LLM lokal (Qwen2.5-7B) + LLM publik; sintetis presisi 1,000/recall 0,936 vs spaCy 0,329/0,893 dan Presidio 0,405/0,896; 98,6% bersih pada 100 catatan MIMIC-III memakai penanda redaksi sebagai label acuan; dosis terjaga 0,769; hanya bahasa Inggris (hlm. 1, 10, 12, 15, 19).
- Tchouka dkk. 2024: dokumen Prancis, on-site; privasi diferensial lokal metrik; penurunan utilitas ICD-10 ± 12% (label) vs 6,8%; dataset tidak kebal serangan (hlm. 2, 12, 13).

Angka kunci sumber II.5 (semua sudah dicek ke halaman; rincian di Lampiran A berkas II.5):
- Yang dkk. 2026: 251 studi RAG medis; 188 retrieval padat, hanya 24 memakai *embedding* multibahasa; masih tahap awal (hlm. 2–4). Nomor cetak = halaman PDF − 1.
- Landolsi dkk. 2026: 57 studi/10 bidang; 6 memakai sumber nonbarat/nonbahasa Inggris; 4 validasi lintas institusi (hlm. 6, 19). Persentase arsitektur (35,41% dasar) tidak konsisten dengan klaim "sebagian besar"; tidak dipakai.
- Zhang dkk. 2026: catatan perawatan lansia Australia; Llama 3.1 8B; 2 tugas × 208 rekaman; tanpa RAG F1 jawaban 0,702/0,722 vs *dense reranking* 0,946/0,953 (BERTScore); fabrikasi intrinsik terbanyak (hlm. 1, 5, 6, 8, 9, 11).
- Jia dkk. 2026: 82,98% USMLE Step 1 vs 80,67% GPT-4 (soal ujian) (hlm. 2, 8).
- Li dkk. 2026: 200 kasus, 5 ahli, rubrik 11 dimensi; pangkalan berversi dengan ID dan tingkat bukti; satu pusat; tanpa pembanding tanpa-RAG (hlm. 1, 3–5, 9).
- Zeba dkk. 2026: pemeriksa fakta tanpa LLM; 104 ringkasan/3.786 proposisi; presisi 0,8904, recall 0,8234, F1 0,8556; MIMIC-III (ICU); kurang andal pada bidang kurang terwakili (hlm. 1, 6, 7, 10, 14, 15).
- Sun dkk. 2025: 55 artikel (15 halusinasi); mitigasi terutama pada QA; standar evaluasi tidak ada (hlm. 4, 15, 18). Waqas dkk. 2026: 90 publikasi; empat jenis halusinasi (hlm. 4, 10, 18).

Angka kunci sumber baru II.4 (semua sudah dicek ke halaman; rincian di Lampiran A berkas II.4):
- Domingues 2026: 23 pedoman, 1.236 aturan JSON, 10 laporan kasus; sistem berbasis aturan murni, "hybrid-ready" (hlm. 1, 2, 3, 5). Angka kinerja jalur terapi tidak konsisten (0,80 pada hlm. 1 dan 7 vs lulus 4 dari 10 pada hlm. 5), jadi tidak dipakai.
- Ijadi Maghsoodi dkk. 2026: tinjauan naratif kritis, 3.892 rekaman menjadi 101 sumber; lima pola hibrida (termasuk ekstraksi saraf + validasi simbolik); bukti prospektif jarang (hlm. 1, 4–7, 9).

Angka kunci delapan sumber II.2 (semua sudah dicek ke halaman; rincian di Lampiran A berkas II.2; bahasa Indonesia tidak muncul pada teks kedelapan PDF):
- Luo dkk. 2024: survei PLM pada tugas NLP medis (hlm. 1).
- Elvas dkk. 2025: 31 studi NER 2019–2024; korpus Inggris 17, Tionghoa 9, Italia 2, Jerman 2, Spanyol 1 (hlm. 4); persentase di artikel memakai penyebut 33, bukan 31; LLM dikecualikan, tanpa penilaian mutu (hlm. 2).
- Kumar dkk. 2026: 153 studi (hlm. 3); kemajuan terpusat pada bahasa Inggris (hlm. 21).
- Woo dkk. 2026: 41 studi; 17 dari AS; hingga 40% hemat waktu; 36% dan 61% (sekunder); LLM sebagai penulis dokumen (hlm. 1, 4, 9, 11).
- Wei dkk. 2026: Gemma-2-9B-IT akurasi 0,9228 dan Macro-F1 0,9279 (CASI bersih), 0,7585 (CASI asli), 0,6304 (tahap 1 saja); satu tolok ukur Inggris (hlm. 1, 5, 7, 9).
- Chen dkk. 2026: MCN; UMLS memuat ICD; korpus Inggris mendominasi (hlm. 1, 4, 6, 8, 13).
- Olex & McInnes 2021: lima jenis informasi temporal (menurut Lim dkk.); sistem belum siap praktik klinis (hlm. 1, 2).
- Jafarpour dkk. 2025: 48 studi; batas 512 kata BERT; informasi temporal (hlm. 1, 4, 9).

## 11. USER PREFERENCES & FEEDBACK

- Bahasa Indonesia akademik baku; prosa, bukan daftar poin (tabel hanya untuk perbandingan karya terdahulu).
- Kejujuran terhadap isi paper lebih penting daripada kesesuaian dengan rancangan; sampaikan terus terang bila paper tidak mendukung klaim.
- Satu pertanyaan klarifikasi saja bila ambigu; jangan menebak.
- Pengguna memperhatikan asal sumber (`source/` vs `external/`) dan tidak ingin sumber baru ditambahkan tanpa permintaan.
- Sapa pengguna dengan "Anda"; jangan menduga pronomina.

## 12. OPEN QUESTIONS / UNCERTAINTIES / CONFLICTS

- **Open question:** subbab mana yang dikerjakan di chat berikutnya, dan apakah kerangka II.1–II.8 dipakai atau diganti? (pengguna belum menjawab)
- **Missing information:** nama berkas rujukan di pesan awal ("Baca file  di project knowledge") kosong; tidak ada berkas progres/Context Transfer sebelumnya di repo; berkas ini dibuat dari nol.
- **Missing information:** gaya sitasi final dan struktur Bab II final dari prodi/pembimbing (Breakdown bagian 17 menandainya "perlu dikonfirmasi"). Pembimbing belum disebut.
- **Contradiction (dilaporkan):** `Sumber Literatur Bab 2.pdf` menyebut Lebeña dkk. (2025) "paling dekat dengan skenario CPPT→kode", sedangkan artikelnya memprediksi diagnosis berikutnya (hlm. 1). Naskah mengikuti artikel.
- **Unverified information:** metadata ± 39 sumber lain di `source/` (tahun, penulis lengkap) hanya dari daftar dan judul PDF; belum diverifikasi sampai artikelnya dibaca.
- **Unverified information:** bentuk baku `ansambel`, `penyandi`, `derau`, `metaanalisis` belum diverifikasi ke KBBI/pedoman resmi [PERLU VERIFIKASI BENTUK BAKU]; `de-identifikasi` vs `deidentifikasi` (Breakdown memakai tanda hubung) belum diputuskan, dihindari di II.3.
- **Open question (anggaran halaman):** II.1 ± 1,54, II.2 ± 3,08, II.3 ± 4,28, II.4 ± 2,21, II.5 ± 2,64, II.6 ± 1,72 halaman. Bab II kini ± 15,9 halaman (termasuk teks panduan templat ± 0,45). Sisa untuk II.7 dan II.8 ≈ 19 − 15,9 ≈ 3,1 halaman, alokasi usulan 3,5 (1,5 + 2,0): kurang ± 0,4. Opsi: (a) pangkas II.3 sekitar 0,8 halaman (kandidat: paragraf Lebeña dkk. dan Jaganathan dkk.), (b) ganti teks panduan templat dengan paragraf pembuka singkat (hemat ± 0,2), (c) pangkas II.6 ± 0,2, atau (d) tulis II.7 dan II.8 lebih singkat (II.8 hampir seluruhnya tabel). Pengguna belum memutuskan; ukuran dari render LibreOffice, bukan Word.
- **Contradiction (dilaporkan, II.1):** `Sumber Literatur Bab 2.pdf` menyebut Nilasari & Soelistijanto "konteks persis TA" dan Rachmawaty dkk. "konteks ... sama persis". Setelah dibaca: Nilasari & Soelistijanto adalah rancangan tanpa hasil yang menangani kecurangan di sisi BPJS (hlm. 855, 857), dan Rachmawaty dkk. meneliti mutu layanan dan biaya satu RS ibu dan anak (hanya menyinggung audit rekam medis pada hlm. S617). Naskah mengikuti artikel.
- **Unverified information:** Tabel 1 Simbolon & Gani memuat ketidakkonsistenan (baris 4 mencantumkan sampel primigravida untuk studi administrasi klaim, hlm. 75); angka Muroli dkk. bersifat sekunder. "RSAB" tidak diuraikan di artikelnya; naskah tidak mengklaim itu RS ibu dan anak [PERLU VERIFIKASI SUMBER].
- **Unverified information:** berkas OneDrive pengguna belum tentu versi yang sama dengan salinan di repo (hanya diketahui sama dengan `... - Copy.docx` di repo).
- **Assistant assumption:** penanda `[SESUAIKAN DENGAN BAB I]` di II.3.4 (pembagian jalur AI/NLP) harus disamakan dengan rumusan Bab I final.
- **Unverified information:** arah penggantian akronim pada Jaganathan dkk. tidak jelas dalam artikelnya (hlm. 2, 4, 5), sehingga naskah tidak menyebut arah. Kriteria kegagalan mereka ketat (setiap perbedaan pada lima kode teratas, hlm. 4), jadi 70–81% adalah ketidakstabilan, bukan akurasi.
- **Unverified information:** Skrabic dkk. memberi jumlah kasus per kategori yang tidak konsisten antarbagian (31, 36, 41); naskah hanya memakai angka agregat.
- **Unverified information (II.2):** Lampiran C berkas II.2 memuat 16 catatan. Yang paling penting: (1) "tidak ada sumber yang menguji teks Indonesia" hanya berlaku pada delapan sumber yang dibaca; (2) Woo dkk. menelaah LLM sebagai penulis dokumen, bukan pemeriksa, dan kalimat peringatan keandalan adalah inferensi penulis naskah; (3) angka 36%, 61%, dan GPT-4o temporal bersifat sekunder (dikutip Woo dkk. dari studi lain); (4) pada Elvas dkk. jumlah Tabel 1 dan persentase tidak konsisten, jadi naskah memakai jumlah; (5) bahasa korpus pada Olex & McInnes tidak dinyatakan pada teks yang dibaca; (6) batas "512 kata" pada Jafarpour dkk. dikutip apa adanya [PERLU VERIFIKASI SUMBER]; (7) bentuk baku `pralatih`, `derau`, `alih kode`, `tokenisasi`, `ortografi`, `inventori makna` [PERLU VERIFIKASI BENTUK BAKU].
- **Assistant assumption:** penanda `[SESUAIKAN DENGAN BAB I]` di II.2.3 (kalimat penutup tentang pembanding dan ambang sebelum eksperimen) harus disamakan dengan rumusan Bab I final.
- **Unverified information (II.4):** Lampiran C berkas II.4 memuat 10 catatan. Yang terpenting: (1) Maleki dkk. tidak ada di repo, jadi analog terdekat belum dibaca; (2) Domingues tidak membuktikan sistem hibrida (hanya lapisan aturan, onkologi prostat, 10 kasus) dan angka kinerjanya tidak konsisten; (3) Ijadi Maghsoodi dkk. adalah tinjauan naratif dan argumen validasi dokumentasinya konseptual dan menyangkut dokumentasi buatan model generatif; (4) keputusan rancangan "pemeriksaan kode tidak bergantung pada keluaran LLM" belum diberi dasar komparatif di II.4 (dasar ada di II.3 dan pada Soroush dkk., PDF belum ada); (5) tahun rujukan Domingues dan Ijadi Maghsoodi mengikuti volume [PERLU VERIFIKASI SUMBER].
- **Assistant assumption:** penanda `[SESUAIKAN DENGAN BAB I]` di II.4.3 harus disamakan dengan rumusan Bab I final.
- **Unverified information (II.5):** Lampiran C berkas II.5 memuat 12 catatan. Yang terpenting: (1) tidak ada sumber yang menguji RAG untuk audit atau pemeriksaan konsistensi antardokumen, dan tidak ada yang menguji teks Indonesia (hanya delapan sumber); (2) pada Zhang dkk. baseline "tanpa retrieval" tidak dirinci dan F1 jawaban memakai BERTScore; (3) angka arsitektur pada Landolsi dkk. dan penyebut persentase pada Yang dkk. tidak konsisten, jadi naskah memakai jumlah; (4) Li dkk. tanpa pembanding tanpa-RAG, dengan kutipan dinilai ahli; (5) Jia dkk. adalah soal ujian dan angka GPT-4 dilaporkan penulisnya sendiri; (6) daftar penulis lengkap Yang dkk. terpotong pada PDF [PERLU VERIFIKASI SUMBER]; (7) Tu dkk., Xiong dkk., Soroush dkk., Ben Abacha dkk. tidak ada di repo.
- **Assistant assumption:** penanda `[SESUAIKAN DENGAN BAB I]` di II.5.3 harus disamakan dengan rumusan Bab I final.
- **Unverified information (II.6):** Lampiran C berkas II.6 memuat 8 catatan. Yang terpenting: (1) tidak ada sumber yang menguji teks Indonesia atau pengenal khas Indonesia; NIK dan nomor rekam medis adalah contoh penulis naskah; (2) temuan nama Asia Tenggara dan F1 0,33 vs 0,98 pada Faustini dkk. adalah laporan studi lain (sekunder); (3) Azzam dkk. memakai dataset sintetis buatan sendiri dan baseline perkakas NER umum, dan "98,6% bersih" bukan ukuran kebocoran PHI karena catatan MIMIC-III sudah dide-identifikasi; abstrak (recall 93,6%) dan Tabel 4 (0,971) tidak sama; (4) abstrak Tchouka dkk. menyebut jaminan matematis privasi tetapi kesimpulannya menyatakan dataset tidak kebal serangan; (5) bentuk baku `de-identifikasi`/`deidentifikasi` belum diputuskan [PERLU VERIFIKASI BENTUK BAKU].
- **Assistant assumption:** penanda `[SESUAIKAN DENGAN BAB I]` di II.6.2 harus disamakan dengan rumusan Bab I final.
- **Open question:** apakah subbab yang butuh PDF yang belum ada (mis. II.4 sudah ditulis tanpa Maleki; bisa diperbarui bila PDF diunggah) ditunda atau dikerjakan tanpa sumber itu?

## 13. CURRENT STATE — WHERE WE LEFT OFF

- Aksi terakhir yang selesai: pengguna menjawab "lanjut" (tanpa memilih opsi anggaran halaman); agent menulis dan memverifikasi draf 1 II.6 (37 klaim cocok), membangun ulang `.docx` (II.1–II.6), mengukur halaman (II.6 ± 1,72; Bab II ± 15,9), dan memperbarui berkas ini (dikomit ke branch `claude/determined-davinci-ueb8i9`, tanpa PR).
- Permintaan pengguna terakhir: "lanjut" (kelima kali secara total). Agent tidak memangkas apa pun karena pengguna belum memilih.
- Respons agent terakhir: melaporkan II.6 selesai sebagai draf (sedikit di atas alokasi; anggaran kurang ± 0,4 halaman untuk II.7 dan II.8) dan menanyakan satu keputusan.
- Belum ada tinjauan pengguna terhadap II.1–II.6.

## 14. NEXT STEPS

### Immediate Next Step
Ikuti pilihan pengguna untuk **cara menutup selisih anggaran halaman** (lihat bagian 12) dan **subbab berikutnya**. Jika pengguna tidak menentukan, kerjakan **II.7 (evaluasi sistem NLP klinis; alokasi 1,5; sumber: Becker dkk. 2025 CARDIO:DE, van Koevorden dkk. 2026; periksa juga Sun dkk. dan Zeba dkk. yang sudah dipakai di II.5)**, lalu II.8 paling akhir (tabel perbandingan karya terdahulu dari Lampiran B semua subbab dan celah penelitian; hampir seluruhnya tabel). Jaga II.7 ≤ 1,5 halaman dan II.8 ≤ 2 halaman; anggaran sisa ± 3,1 halaman. Baca penuh PDF, jalankan pemeriksaan halaman otomatis, tulis naskah, bangun ulang `.docx` dari Markdown (skrip `tools/build_docx.py`; tambahkan berkas subbab baru pada daftar OUTLINE di dalamnya; pemeriksa halaman: `tools/verify_claims.py` dengan contoh klaim `tools/claims_II1.json`, `tools/claims_II2.json`, dan `tools/claims_II3.json`, offset halaman per sumber ada di kamus PDFS; butuh skrip skill docx, atur `DOCX_SKILL_DIR` bila lokasinya berbeda), dan ukur halaman.

### Follow-up Steps
- Setiap subbab: baca penuh PDF sumber, catat halaman, jalankan pemeriksaan halaman otomatis, tulis naskah ≤ alokasi halaman, tambah Lampiran A/B/C, perbarui berkas ini, komit dan dorong ke branch.
- Kerjakan II.8 (tabel perbandingan dan celah penelitian) paling akhir dari matriks Lampiran B tiap subbab.
- Tulis paragraf pembuka Bab II sesuai fungsi bab menurut templat (di `.docx` masih teks panduan templat); satukan daftar pustaka; perbarui daftar isi di Word; ukur halaman Bab II secara keseluruhan di Word (bukan hanya render LibreOffice).

### Waiting for User
- Pilihan subbab berikutnya dan konfirmasi kerangka (atau kerangka milik pengguna).
- Unggahan PDF yang belum ada (bagian 8) sesuai subbab yang dipilih.
- Konfirmasi gaya sitasi final dan struktur Bab II dari prodi/pembimbing bila sudah ada.
- Tinjauan terhadap draf II.3, termasuk penanda `[SESUAIKAN DENGAN BAB I]`.
- Keputusan tentang panjang II.3 (± 4,30 halaman vs alokasi 3,5) dan penyesuaian alokasi subbab sisa: pangkas atau sesuaikan.
- Salinan `.docx` hasil harus diambil dari repo dan ditempatkan sendiri ke folder OneDrive (agent tidak dapat menulis ke `C:\`).

## 15. CONTINUATION INSTRUCTION

Anda melanjutkan sesi yang sama: bertindaklah seolah hadir sejak awal. Jangan memulai proyek dari awal dan jangan meminta pengguna mengulang informasi yang sudah ada di berkas ini. Ajukan pertanyaan klarifikasi hanya untuk hal yang di sini ditandai missing, ambigu, atau kontradiktif, dan **hanya satu hal terpenting per chat**. Mulai dari langkah pada "Immediate Next Step" (menentukan atau mengerjakan subbab berikutnya, atau merevisi II.3 bila diminta). Ikuti seluruh aturan di bagian 4 dan 11, baca `CLAUDE.md` dan `RULES.md` sebelum menulis, ambil klaim isi paper hanya dari PDF di repo dengan nomor halaman, jangan memakai `source/external/` tanpa persetujuan, dan perbarui berkas ini sebelum menutup chat yang mengubah keputusan, progres, atau daftar referensi.
