# Bab II — Subbab II.6 (DRAFT 1)

> **Status:** draf kerja, belum ditinjau pembimbing. Hanya bagian "Naskah" dan "Daftar Pustaka (sementara)" yang masuk ke proposal. Bagian "Lampiran kerja" adalah alat bantu pemeriksaan dan tidak dihitung dalam batas 19 halaman.
>
> **Konvensi sitasi sementara:** penulis-tahun dengan nomor halaman (`hlm.`). Semua sumber adalah artikel Elsevier bernomor artikel, sehingga `hlm.` = halaman berkas PDF. Format akhir menunggu pedoman program studi.
>
> **Sumber:** tiga artikel di `source/` (Faustini dkk.; Azzam dkk.; Tchouka dkk.), semuanya dibaca dari PDF. Setiap angka dan klaim isi dicek otomatis ke teks halaman (Lampiran A). Tidak ada sumber dari `source/external/`.
>
> **Penanda yang perlu dijawab pengguna:** satu `[SESUAIKAN DENGAN BAB I]` pada subbab penutup.

---

## Naskah

## II.6 De-identifikasi untuk Layanan AI Eksternal

### II.6.1 Pendekatan De-identifikasi dan Bukti yang Tersedia

Faustini dkk. (2026) menelaah 83 artikel yang dipilih dari 734 tentang de-identifikasi data klinis berbasis NLP pada tahun 2015–2024, dengan de-identifikasi didefinisikan sebagai pendeteksian, penggantian, atau penghapusan informasi kesehatan yang dilindungi (*protected health information*, PHI) (hlm. 1, 2). Sebagian besar studi menggarap konten berbahasa Inggris karena dataset yang tersedia berbahasa Inggris, metode berbasis aturan tetap umum di luar bahasa Inggris (hlm. 1, 6), dan tantangan utamanya ialah campur kode serta kelangkaan dataset yang dapat direproduksi (hlm. 1). Faustini dkk. juga melaporkan temuan studi lain bahwa Presidio kesulitan mengenali nama Slavia serta nama Asia Tengah dan Asia Tenggara dibandingkan nama Inggris (hlm. 5).

Azzam dkk. (2026) mengusulkan sistem agentik tempat LLM yang dihosting lokal menangani semua langkah sensitif, sedangkan LLM publik hanya menalar atas masukan yang sudah dianonimkan (hlm. 1), dengan pemetaan lokal untuk mengembalikan identitas pada jawaban (hlm. 10). Pada dataset rekam medis sintetis, sistem itu mencapai presisi 1,000 dan *recall* 0,936, sedangkan spaCy dan Presidio berpresisi 0,329 dan 0,405 dengan *recall* sekitar 0,89 (hlm. 12). Pengujian pada 100 catatan MIMIC-III memakai penanda redaksi bawaan sebagai pengganti label acuan karena catatannya sudah dide-identifikasi (hlm. 15). Sebutan obat terjaga 0,974, tetapi dosis hanya 0,769 (hlm. 12), dan sistem baru mendukung masukan berbahasa Inggris (hlm. 19).

Tchouka dkk. (2024) menguji de-identifikasi pada dokumen medis berbahasa Prancis di sebuah rumah sakit publik, dengan seluruh eksperimen di lokasi rumah sakit (hlm. 2). Tanggal, usia, dan lokasi diganti dengan privasi diferensial lokal agar aspek kronologis dan geografisnya tidak hilang (hlm. 1, 7). Pada tugas asosiasi kode ICD-10, skor F1 turun 6,8% terhadap korpus asli dengan pendekatan itu, dibandingkan sekitar 12% bila setiap entitas diganti dengan labelnya (hlm. 2, 12, 13). Dataset hasil de-identifikasi tetap tidak kebal terhadap serangan re-identifikasi dan keanggotaan sehingga tidak dapat disebarluaskan (hlm. 13).

### II.6.2 Sintesis dan Celah

Dua hal didukung secara terbatas: de-identifikasi oleh LLM lokal dapat memisahkan data sensitif dari LLM publik pada pengujian awal, dan penggantian yang memperhatikan utilitas mengurangi kehilangan kinerja pada tugas hilir berbasis kode. Bukti itu memiliki tiga keterbatasan. Pertama, tidak ada sumber yang menguji teks klinis berbahasa Indonesia atau pengenal khas Indonesia seperti NIK dan nomor rekam medis; temuan tentang nama Asia Tenggara bersifat sekunder dan menyangkut perkakas yang diuji pada data lain (Faustini dkk., 2026, hlm. 5). Kedua, bukti untuk pendekatan berbasis LLM lokal berasal dari data sintetis dan catatan berbahasa Inggris yang sudah dide-identifikasi (Azzam dkk., 2026, hlm. 15), sehingga kebocoran PHI pada catatan baru yang belum diredaksi belum terukur. Ketiga, kehilangan utilitas baru diukur pada asosiasi kode ICD-10 (Tchouka dkk., 2024, hlm. 13) atau pada sebutan obat dan dosis (Azzam dkk., 2026, hlm. 12); dampak de-identifikasi terhadap temuan audit yang bergantung pada tanggal, dosis, dan urutan waktu belum diukur. De-identifikasi pada penelitian ini perlu diuji pada data berbahasa Indonesia, dengan ukuran kebocoran pengenal dan dampaknya pada mutu temuan [SESUAIKAN DENGAN BAB I: rumusan pertanyaan dan ukuran keberhasilan].

---

## Daftar Pustaka (sementara)

> **[FORMAT AKHIR PERLU DIKONFIRMASI]** Pola mengikuti contoh pada templat (gaya mirip APA). Metadata dari halaman pertama masing-masing PDF.

Azzam, R., Musamih, A., Gebreab, S., Salah, K., & Omar, M. (2026). Agentic LLM for anonymizing healthcare data with contextual awareness. *Knowledge-Based Systems, 343*, 116034.

Faustini, P., McIver, A., Sullivan, R., & Dras, M. (2026). De-identification of clinical data: A systematic review of free text, image and tabular data approaches. *International Journal of Medical Informatics, 208*, 106225.

Tchouka, Y., Couchot, J.-F., Laiymani, D., Selles, P., & Rahmani, A. (2024). Differentially private de-identifying textual medical document is compliant with challenging NLP analyses: Example of privacy-preserving ICD-10 code association. *Intelligent Systems with Applications, 23*, 200416.

---

## Lampiran kerja (bukan bagian naskah)

### Lampiran A. Tabel verifikasi klaim ke halaman PDF

Setiap baris dicocokkan otomatis ke teks halaman yang disebut (`tools/verify_claims.py` dengan `tools/claims_II6.json`; hasil: 37 dari 37 cocok). Nomor halaman = halaman berkas PDF = nomor cetak.

| Sumber | Klaim di naskah | Hlm. | Kutipan asli (pendek) |
|---|---|---|---|
| Faustini dkk. | 83 dari 734 artikel; periode 2015–2024 | 1 | "From a set of 734 papers, 83 articles were deemed relevant"; "articles published from January 2015 to December 2024" |
| Faustini dkk. | Definisi de-identifikasi (deteksi, penggantian, penghapusan PHI) | 2 | "adopt de-identification for detection, replacement or removal of Protected Health Information" |
| Faustini dkk. | Penggunaan model bahasa meningkat; perkakas siap pakai perlu disesuaikan; mayoritas bahasa Inggris | 1 | "increased use of Language Models"; "Off-the-shelf tools often require customisation for optimal performance"; "Most studies de-identify English content, supported by the prevalence of English datasets" |
| Faustini dkk. | Aturan umum di luar bahasa Inggris; tantangan campur kode dan kelangkaan dataset | 1, 6 | "Rule-based methods remain common outside of English"; "the phenomenon of code-mixing"; "the scarcity of available datasets for reproducibility" |
| Faustini dkk. | Presidio kesulitan nama Slavia, Asia Tengah, Asia Tenggara (studi lain, sekunder) | 5 | "struggled to identify Slavic, as well as Central and Southeast Asian names, compared to English names" |
| Faustini dkk. | F1 LLM serendah 0,33 tanpa contoh/instruksi rinci vs 0,98 dengan perintah rinci (studi lain, sekunder) | 6 | "goes as low as.33"; "compared to.98 with a detailed prompt" |
| Azzam dkk. | LLM lokal menangani langkah sensitif; LLM publik hanya menalar masukan teranonimkan | 1 | "Locally hosted LLMs handle all privacy-sensitive steps"; "public LLMs are used exclusively for reasoning on pre-anonymized inputs" |
| Azzam dkk. | Pemetaan lokal untuk de-anonimisasi | 10 | "secure local mapping" |
| Azzam dkk. | Dataset sintetis; presisi 1,000 dan recall 0,936; spaCy 0,329/0,893 dan Presidio 0,405/0,896 | 1, 12 | "We evaluate our system on a synthetic clinical dataset"; Tabel 3 "0.329 0.342 0.515 0.350 0.405 1.000"; "0.893 0.893 0.397 0.495 0.896 0.936" |
| Azzam dkk. | 98,6% bersih pada 100 catatan MIMIC-III; penanda redaksi sebagai pengganti label acuan; dataset sudah dide-identifikasi | 1, 15 | "achieving a clean transformation rate of 98.6%"; "These placeholders were treated as proxy ground"; "since the dataset is already de-identified" |
| Azzam dkk. | Sebutan obat 0,974; dosis 0,769 | 12 | "medication mentions remain largely intact (0.974"; "Dosage information shows a lower preservation rate (0.769" |
| Azzam dkk. | Hanya masukan berbahasa Inggris | 19 | "Currently, the system supports only English-language inputs" |
| Tchouka dkk. | Dokumen medis Prancis; rumah sakit publik; eksperimen di lokasi tanpa data keluar | 1, 2 | "sensitive entities in French medical data"; "a French public health center"; "all experiments were conducted on-site, and no data was extracted from" |
| Tchouka dkk. | Privasi diferensial lokal berbasis metrik; penggantian tanggal/lokasi acak menghilangkan aspek kronologis/geografis | 1, 7 | "Local differential privacy"; "replacing location and date entities with random ones may lead to"; "loss of geographic epidemiological data for the former and chronological aspect for the latter" |
| Tchouka dkk. | Penurunan utilitas ± 12% (label) vs 6,8% (pendekatan penulis); penggantian label paling tahan serangan tetapi membuang nilai | 2, 12, 13 | "helps reduce the loss of utility (6.8%) compared to a traditional de-identification method (12%"; "The percentage gap between the original corpus ICD-10-HNFC and the de-identified corpus ICD-10-TAG-HNFC is approximately 12%"; "This de-identification approach is the most robust against potential re-identification attacks"; "by removing the values of the entities, they cannot be exploited for classification" |
| Tchouka dkk. | Dataset hasil de-identifikasi tidak kebal re-identifikasi/serangan keanggotaan; tidak dapat disebarluaskan | 13 | "not immune from a re-identification or membership attack"; "even de-identified datasets cannot be disseminated" |

Pemeriksaan ketiadaan (bukan pencocokan frasa): pencarian `indonesia|malay|bahasa` pada teks ketiga PDF tidak menemukan satu pun kecocokan.

### Lampiran B. Matriks catatan literatur (bahan untuk subbab II.8)

| Penulis, tahun | Data | Metode | Hasil utama | Celah terhadap penelitian ini |
|---|---|---|---|---|
| Faustini dkk., 2026 | 83 artikel (dari 734), 2015–2024 | Tinjauan sistematis | Beralih ke model bahasa; perkakas perlu disesuaikan; mayoritas bahasa Inggris; campur kode dan kelangkaan dataset | Survei; temuan nama Asia Tenggara dan LLM adalah laporan studi lain |
| Azzam dkk., 2026 | Dataset EMR sintetis; 100 catatan MIMIC-III (sudah dide-identifikasi) | Sistem agentik LLM lokal + LLM publik, bandingan 5 perkakas NER | Presisi 1,000, recall 0,936 (sintetis); dosis terjaga 0,769 | Hanya bahasa Inggris; data sintetis/sudah redaksi; baseline perkakas umum |
| Tchouka dkk., 2024 | Dokumen medis Prancis (HNFC), 375 berlabel → 46.000+ dokumen | NER CamemBERT + privasi diferensial lokal metrik; utilitas via asosiasi ICD-10 | Penurunan utilitas 6,8% vs 12% (label) | Bahasa Prancis; dataset tidak boleh disebarluaskan; serangan belum dianalisis |

### Lampiran C. Catatan peringatan dan penandaan

1. **Tidak ada sumber yang menguji teks Indonesia atau pengenal khas Indonesia (NIK, nomor rekam medis, SEP).** Pernyataan ini dibatasi pada ketiga sumber yang dibaca. Penyebutan NIK dan nomor rekam medis di naskah adalah contoh penulis naskah (selaras dengan Breakdown bagian 11), bukan dari sumber.
2. **Dua temuan Faustini dkk. adalah laporan studi lain (sekunder):** Presidio dan nama Asia Tenggara (Kotevski dkk.) serta F1 0,33 vs 0,98 (Yashwanth & Shettar; kalimat ini dikeluarkan dari naskah pada draf 3 demi ruang, klaimnya tetap ada pada `claims_II6.json`). Studi aslinya tidak ada di repo. Angka kinerja tabular dan citra pada Faustini dkk. tidak dipakai.
3. **Azzam dkk., evaluasi sintetis.** Dataset dibuat penulis dengan PHI sisipan sehingga label acuan lengkap; baseline adalah perkakas NER umum yang tidak disetel pada skema itu (spaCy, Stanza, Flair, bert-base-NER, Presidio), jadi selisih tidak membuktikan LLM lebih baik daripada perkakas yang disetel. Presisi 1,000 bergantung pada cara penulis menilai keluaran yang diparafrasa. Abstrak melaporkan recall 93,6% sedangkan Tabel 4 (rata-rata beberapa putaran) melaporkan 0,971; naskah memakai 0,936 dari Tabel 3 dan abstrak.
4. **Azzam dkk., "98,6% bersih" bukan ukuran kebocoran PHI.** Angka itu mengukur penanda redaksi bawaan MIMIC-III yang hilang dari keluaran, dan catatannya sudah dide-identifikasi (hlm. 15). Uji serangan re-identifikasi oleh LLM publik pada 100 catatan yang sama (hlm. 16) tidak dipakai di naskah karena tidak ada identitas asli sebagai label acuan. Pemilihan LLM lokal (Qwen2.5-7B-Instruct) dilakukan pada 100 pertanyaan sintetis (hlm. 11) dan tidak dipakai.
5. **Tchouka dkk.:** abstrak menyebut strategi pengganti "secara matematis menjamin perlindungan privasi", tetapi kesimpulan menyatakan dataset hasilnya tidak kebal terhadap serangan dan tidak dapat disebarluaskan; naskah mengikuti kesimpulan. Penurunan 12% dan 6,8% adalah selisih persentase F1 terhadap korpus asli (hlm. 12). Rasio privasi yang dipakai (b = 1) adalah satu titik pada spektrum yang belum dievaluasi penuh (hlm. 13).
6. **Titik hubung yang tidak diklaim.** Breakdown menyatakan de-identifikasi diperiksa manual pada sampel dan kebijakan retensi penyedia AI diperiksa sebelum dipilih. Kesesuaian dengan pemisahan lingkungan lokal dan publik pada Azzam dkk. tidak dinyatakan di naskah karena menyangkut rancangan yang belum tertulis di Bab III.
7. **Istilah yang perlu diverifikasi bentuk bakunya:** `de-identifikasi` (Breakdown memakai tanda hubung; belum diputuskan antara `de-identifikasi` dan `deidentifikasi`), `dide-identifikasi`, `anonimkan`, `redaksi`, `privasi diferensial`, `campur kode` [PERLU VERIFIKASI BENTUK BAKU]. `protected health information`, `recall`, `prompt` ditulis miring pada kemunculan pertama sebagai istilah asing.
8. **Penanda `[SESUAIKAN DENGAN BAB I]`** pada kalimat penutup II.6.2 harus disamakan dengan rumusan pertanyaan dan ukuran keberhasilan Bab I.
