# CONTEXT TRANSFER

> Berkas ini diperbarui di akhir setiap chat yang mengubah keputusan, progres, atau daftar referensi (instruksi pengguna). Pembaruan terakhir: sesi 1, 20 Oktober 2026 (draf II.3 dan II.1, keduanya dimasukkan ke `.docx` Utama). Letakkan isi berkas ini sebagai konteks awal chat berikutnya, bersama `CLAUDE.md` dan `RULES.md`.

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
   - II.2 NLP/LLM pada teks klinis, singkatan lokal, penalaran temporal (3)
   - II.3 Audit otomatis dokumentasi dan pengodean (3,5)  ← **ditulis**
   - II.4 Pendekatan hibrida rule-based dan AI/NLP (2)
   - II.5 RAG, penjangkaran bukti, halusinasi (4)
   - II.6 De-identifikasi untuk layanan AI eksternal (1,5)
   - II.7 Evaluasi sistem NLP klinis (1,5)
   - II.8 Tabel perbandingan karya terdahulu dan celah penelitian (2) — dikerjakan terakhir
   Literatur *alert fatigue* dan *knowledge graph* sengaja dikeluarkan (lebih dekat ke antarmuka Abizzar atau eksploratif); dapat dibalik oleh pengguna. Penomoran heading memakai angka Romawi mengikuti templat (pengguna menulis "2.1" secara kasual). Judul II.1 dan II.2 di `.docx` adalah penampung bertanda kuning agar nomor II.3 benar; judulnya usulan dan belum dikonfirmasi.
5. **Posisi sumber di II.3**: Lebeña dkk. (2025) hanya diberi porsi kecil dan disebut apa adanya (prediksi diagnosis berikutnya, bukan audit), karena klaim relevansi di `Sumber Literatur Bab 2.pdf` ("paling dekat dengan skenario CPPT→kode") tidak terdukung isi artikel.
6. **Alur kerja (instruksi pengguna, chat 1 lanjutan): tulis dulu di Markdown, naskah final di `.docx` templat Utama.** Naskah ada di `bab2/*.md`; tabel verifikasi dan catatan peringatan dipisah di "Lampiran kerja" dan tidak ikut dihitung dalam 19 halaman. `.docx` dibangun otomatis dari Markdown ke salinan templat Utama di repo (gaya Heading 2/3, Normal, daftar pustaka, penomoran otomatis), disimpan sebagai berkas baru **tanpa menimpa templat**: `bab2/Proposal-IF4091-Capstone-Utama-2026_Draft-Bab2.docx`. Pengguna menyalin/menimpa ke berkas OneDrive-nya sendiri.
7. **Sumber II.1 (keputusan agent, dalam batas aturan pengguna):** hanya Susilo dkk. 2025, Rachmawaty dkk. 2021, Nilasari & Soelistijanto 2026 (dari `source/`) dan Simbolon & Gani 2023 (dari `source/external/`, karena dirujuk Breakdown bagian 15). Septiono dkk. 2026, Sambodo dkk. 2023, dan Barsasella dkk. 2021 tidak dipakai (tidak relevan dengan dokumentasi/klaim; dua yang terakhir tidak dibaca). Permenkes di `external/` tidak dipakai tanpa persetujuan. Muroli dkk. (2020) hanya disebut sebagai kutipan sekunder dari Simbolon & Gani (PDF aslinya tidak ada) dan tidak masuk daftar pustaka.

## 6. PROGRESS STATUS

### Completed
- Membaca `CLAUDE.md`, `RULES.md` (seluruhnya), Breakdown (11 hlm), `Sumber Literatur Bab 2.pdf` (12 hlm), templat individu, panduan studi literatur, informasi umum TA, panduan Bab I.
- Memetakan 46 PDF di `source/` ke daftar literatur (lihat bagian 8) dan memeriksa bahwa semuanya berteks penuh (bukan hanya abstrak).
- **Draf 1 subbab II.3** (1.365 kata isi naskah; **terukur ± 4,3 halaman** pada templat Utama dari render LibreOffice dengan Liberation Serif yang metrik-kompatibel dengan Times New Roman, melebihi alokasi 3,5; bukan ukuran Word) ditulis dari tujuh PDF yang dibaca penuh; 100 klaim/halaman dicek otomatis ke teks halaman PDF (empat awalnya gagal karena pemenggalan kata hasil ekstraksi, lalu dicek manual dan benar).
- **Draf 1 subbab II.1 Dokumentasi Klinis dan Klaim JKN** (514 kata; **terukur ± 1,54 halaman**, sesuai alokasi 1,5) ditulis dari empat PDF yang dibaca penuh (Simbolon & Gani dibaca juga dari gambar halaman karena teks PDF tercampur dua kolom); 27 klaim/halaman dicek otomatis ke teks halaman PDF (lima awalnya gagal karena offset halaman dan pemenggalan kata; halaman dikoreksi dan dicek ulang, semuanya cocok). `.docx` dibangun ulang dengan II.1 dan II.3 (II.2 penampung), lolos validasi, render 25 halaman. Bab II terisi ± 6,38 halaman termasuk judul bab, teks panduan templat, dan penampung II.2; isi II.1 + II.3 = ± 5,84 halaman.

### In Progress
- Tidak ada. II.1 dan II.3 menunggu tinjauan pengguna.

### Not Started
- II.2, II.4, II.5, II.6, II.7, II.8; paragraf pembuka Bab II (tujuan bab menurut templat); penyatuan daftar pustaka Bab II (sementara 11 entri hasil gabungan II.1 dan II.3); pemformatan akhir di Word (daftar isi, halaman).

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
- **`bab2/Proposal-IF4091-Capstone-Utama-2026_Draft-Bab2.docx`** — templat Utama berisi II.3 (dan penampung II.1, II.2), daftar pustaka Bab II; bagian lain templat tidak diubah kecuali dua paragraf pemisah halaman ganda di akhir Bab II yang dihapus (menyebabkan halaman kosong) dan contoh gambar/tabel/pustaka yang diganti. Lolos validasi skema; render 22 halaman. **Daftar isi, daftar gambar, dan daftar tabel masih berisi hasil lama** sampai diperbarui di Word (berkas diatur agar Word menawarkan pembaruan saat dibuka; atau Ctrl+A lalu F9).
- `7_IF4091_PenulisanStudiLiteratur_2026_Okt.pdf`, `3_IF4091_Informasi Umum TA_2026 Sept.pdf`, `9_IF4091_ProposalTA_Bab1_2026_Okt.pdf`, `5_...EfficientReading...`, `12_...Bahasa Indonesia...`, `1_...Pengantar Kuliah...` — materi kuliah.
- **`bab2/II.1_Dokumentasi_Klinis_dan_Klaim_JKN.md`** — draf 1 II.1 (naskah, daftar pustaka sementara, Lampiran A tabel verifikasi, B matriks catatan literatur, C catatan peringatan).
- **`bab2/II.3_Audit_Otomatis_Dokumentasi_dan_Kode_Diagnosis.md`** — draf 1 II.3 (naskah + daftar pustaka sementara + Lampiran A tabel verifikasi klaim, B matriks catatan literatur untuk II.8, C catatan peringatan).
- `tools/` — `build_docx.py` (Markdown subbab → `.docx` templat Utama), `verify_claims.py` + `claims_II1.json`/`claims_II3.json` (cek frasa kutipan ke halaman PDF). Catatan: pada `claims_II3.json` empat entri berstatus FAIL otomatis karena pemenggalan kata di teks PDF (sudah dicek manual dan benar: S2, U3b, U14, M2); `claims_II1.json` sudah memuat halaman/frasa yang dikoreksi (semua lolos).
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
- **Open question:** II.3 terukur ± 4,30 halaman (alokasi 3,5) dan II.1 ± 1,54 (alokasi 1,5). Sisa anggaran untuk II.2 dan II.4–II.8 = 19 − 5,84 ≈ 13,2 halaman, sedangkan alokasi usulan untuk keenamnya 14 halaman, belum termasuk paragraf pembuka Bab II. Pilihan: memangkas II.3 sekitar 0,8 halaman (kandidat: paragraf Lebeña dkk. dan Jaganathan dkk.), atau menyesuaikan alokasi subbab lain. Pengguna belum memutuskan.
- **Contradiction (dilaporkan, II.1):** `Sumber Literatur Bab 2.pdf` menyebut Nilasari & Soelistijanto "konteks persis TA" dan Rachmawaty dkk. "konteks ... sama persis". Setelah dibaca: Nilasari & Soelistijanto adalah rancangan tanpa hasil yang menangani kecurangan di sisi BPJS (hlm. 855, 857), dan Rachmawaty dkk. meneliti mutu layanan dan biaya satu RS ibu dan anak (hanya menyinggung audit rekam medis pada hlm. S617). Naskah mengikuti artikel.
- **Unverified information:** Tabel 1 Simbolon & Gani memuat ketidakkonsistenan (baris 4 mencantumkan sampel primigravida untuk studi administrasi klaim, hlm. 75); angka Muroli dkk. bersifat sekunder. "RSAB" tidak diuraikan di artikelnya; naskah tidak mengklaim itu RS ibu dan anak [PERLU VERIFIKASI SUMBER].
- **Unverified information:** berkas OneDrive pengguna belum tentu versi yang sama dengan salinan di repo (hanya diketahui sama dengan `... - Copy.docx` di repo).
- **Assistant assumption:** penanda `[SESUAIKAN DENGAN BAB I]` di II.3.4 (pembagian jalur AI/NLP) harus disamakan dengan rumusan Bab I final.
- **Unverified information:** arah penggantian akronim pada Jaganathan dkk. tidak jelas dalam artikelnya (hlm. 2, 4, 5), sehingga naskah tidak menyebut arah. Kriteria kegagalan mereka ketat (setiap perbedaan pada lima kode teratas, hlm. 4), jadi 70–81% adalah ketidakstabilan, bukan akurasi.
- **Unverified information:** Skrabic dkk. memberi jumlah kasus per kategori yang tidak konsisten antarbagian (31, 36, 41); naskah hanya memakai angka agregat.
- **Open question:** apakah subbab yang butuh PDF yang belum ada (mis. II.4 butuh Maleki) ditunda atau dikerjakan tanpa sumber itu?

## 13. CURRENT STATE — WHERE WE LEFT OFF

- Aksi terakhir yang selesai: pengguna menjawab "lanjutkan" setelah agent mengusulkan II.1; agent membaca empat PDF, menulis dan memverifikasi draf 1 II.1, membangun ulang `.docx` (II.1 + penampung II.2 + II.3), mengukur halaman, dan memperbarui berkas ini (dikomit ke branch `claude/determined-davinci-ueb8i9`, tanpa PR).
- Permintaan pengguna terakhir: "lanjutkan" (mengerjakan II.1, usulan agent). Sebelumnya: pertanyaan alasan mulai dari II.3 dan perintah memakai `.docx` templat Utama (markdown dulu, final di docx).
- Respons agent terakhir: melaporkan II.1 selesai sebagai draf (panjang, temuan peringatan, sisa anggaran halaman) dan menanyakan keputusan panjang II.3 serta subbab berikutnya.
- Belum ada tinjauan pengguna terhadap II.1 maupun II.3.

## 14. NEXT STEPS

### Immediate Next Step
Ikuti pilihan pengguna untuk **subbab berikutnya** atau revisi (mis. pemangkasan II.3). Jika pengguna tidak menentukan, usulkan **II.2 (NLP dan LLM pada teks klinis)** karena urut; PDF-nya ada (Kumar, Woo, Elvas, Luo; singkatan lokal: Wei, Chen; temporal: Olex & McInnes) kecuali Kayira dkk. (belum diunggah). Baca penuh PDF, jalankan pemeriksaan halaman otomatis, tulis naskah, bangun ulang `.docx` dari Markdown (skrip `tools/build_docx.py`; tambahkan berkas subbab baru pada daftar OUTLINE di dalamnya; pemeriksa halaman: `tools/verify_claims.py` dengan contoh klaim `tools/claims_II1.json` dan `tools/claims_II3.json`, offset halaman per sumber ada di kamus PDFS; butuh skrip skill docx, atur `DOCX_SKILL_DIR` bila lokasinya berbeda), dan ukur halaman.

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
