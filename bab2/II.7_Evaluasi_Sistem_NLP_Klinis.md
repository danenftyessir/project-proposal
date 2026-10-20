# Bab II — Subbab II.7 (DRAFT 1)

> **Status:** draf kerja, belum ditinjau pembimbing. Hanya bagian "Naskah" dan "Daftar Pustaka (sementara)" yang masuk ke proposal. Bagian "Lampiran kerja" adalah alat bantu pemeriksaan dan tidak dihitung dalam batas 19 halaman.
>
> **Konvensi sitasi sementara:** penulis-tahun dengan nomor halaman (`hlm.`). Becker dkk. (artikel Elsevier bernomor artikel) dan van Koevorden dkk. (ESMO Real World Data and Digital Oncology, tanpa nomor halaman cetak pada berkas yang dibaca): `hlm.` = halaman berkas PDF. Format akhir menunggu pedoman program studi.
>
> **Sumber:** dua artikel baru di `source/` (Becker dkk.; van Koevorden dkk.), keduanya dibaca penuh dari PDF, ditambah satu rujukan silang ke Sun dkk. (2025) yang sudah dibaca untuk II.5. Setiap angka dan klaim isi dicek otomatis ke teks halaman (Lampiran A). Tidak ada sumber dari `source/external/`. Singh dkk. (JMIR Med Inform 2025), sumber ketiga pada kelompok ini di daftar sumber, tidak ada di repo.
>
> **Penanda yang perlu dijawab pengguna:** satu `[SESUAIKAN DENGAN BAB I]` pada subbab penutup.

---

## Naskah

## II.7 Evaluasi Sistem NLP Klinis

### II.7.1 Acuan Penilaian dan Variabilitas Penilai

Becker dkk. (2025) memperluas korpus CARDIO:DE, yaitu 500 surat dokter berbahasa Jerman di bidang kardiovaskular (hlm. 2), dengan lima label entitas: diagnosis, tindakan diagnostik, obat, temuan medis, dan terapi (hlm. 1). Seorang apoteker dan seorang ekonom kesehatan mula-mula menganotasi sekitar 15% korpus secara tumpang tindih, membahas ketidaksesuaiannya, lalu menganotasi 5% tambahan secara tumpang tindih, dengan ambang kesepakatan Krippendorff's alpha *unitizing* 0,85 yang ditetapkan sebelumnya (hlm. 2). Kesepakatan mencapai 0,98 pada beberapa subset (hlm. 1), tetapi seluruh proses memakan tujuh bulan dan 10–40 menit per dokumen (hlm. 2). Empat model diuji, dan semuanya sering menukar temuan medis dengan diagnosis (hlm. 4); penulisnya menunjukkan bahwa frasa seperti "80 % main stem stenosis" dapat dilabeli keduanya bergantung pada konteks (hlm. 3).

van Koevorden dkk. (2026) memvalidasi ekstraksi data oleh LLM sumber terbuka pada 1.482 halaman dokumen klinis 60 pasien onkologi kepala dan leher untuk 29 kategori, dengan enam pakar menilai 2.555 nilai: penilaian cocok atau tidak cocok secara buta, lalu pengkategorian galat (hlm. 1). Akurasi per kategori berkisar 74% sampai 90%, dan penulis menegaskan bahwa metrik itu adalah metrik yang ditetapkan pakar karena keluaran model berupa teks bebas, bukan prediksi kategorikal (hlm. 1, 4). Dua dokter yang mengekstraksi secara independen berselisih pada 29,0% nilai, sedangkan LLM berselisih dari konsensus mereka pada 41,4% dalam pemetaan awal (hlm. 4). Setelah peninjauan, lebih dari separuh keluaran LLM yang semula dinilai berbeda dinyatakan cocok (hlm. 5), dan dari 65 keluaran yang semula dikategorikan halusinasi hanya empat yang terkonfirmasi setelah dicek ke dokumen asli (hlm. 6). Penilaian dampak galat juga tidak seragam: satu dari enam penilai menandai 61 dari 68 galat sebagai berdampak tinggi (hlm. 5). Penulisnya menyimpulkan bahwa taksonomi galat dan metrik saja tidak cukup untuk menilai konsekuensi klinis (hlm. 5), dan bahwa jumlah ekstraktor manusia yang kecil membatasi estimasi variabilitas antarpenilai (hlm. 7).

### II.7.2 Sintesis dan Celah

Kedua sumber menunjukkan bahwa acuan penilaian perlu dirancang dan diukur, bukan diasumsikan: kesepakatan antarpenilai dapat diukur dengan ambang yang ditetapkan sebelumnya (Becker dkk., 2025, hlm. 2), dan ketidaksepakatan antarmanusia dapat mencapai 29,0% pada ekstraksi klinis (van Koevorden dkk., 2026, hlm. 4). Namun, ada tiga keterbatasan. Pertama, keduanya mengevaluasi ekstraksi entitas atau nilai dari satu dokumen, bukan temuan ketidaksesuaian antardokumen. Kedua, teks yang dievaluasi berbahasa Jerman dan Belanda (Becker dkk., 2025, hlm. 2; van Koevorden dkk., 2026, hlm. 7), bukan Indonesia, dan van Koevorden dkk. membatasi generalisasi pada satu pusat rujukan tersier (hlm. 8). Ketiga, hanya Becker dkk. yang mengukur kesepakatan antarpenilai secara formal; pada van Koevorden dkk. jumlah penilai manusia terlalu kecil untuk estimasi itu. Akibatnya, evaluasi audit dokumentasi perlu menetapkan unit temuan, perlakuan kasus ambigu, ukuran kesepakatan penilai, serta ukuran dan ambang kegagalan sebelum eksperimen; acuan yang ditetapkan satu penilai tidak dapat memperkirakan variabilitas antarpenilai [SESUAIKAN DENGAN BAB I: rumusan pertanyaan dan ukuran keberhasilan].

---

## Daftar Pustaka (sementara)

> **[FORMAT AKHIR PERLU DIKONFIRMASI]** Pola mengikuti contoh pada templat (gaya mirip APA). Hanya entri baru; Sun dkk. (2025) sudah ada pada daftar II.5. Metadata dari halaman pertama masing-masing PDF.

Becker, M., Krumscheid, M., Knobelspies, A., Seydel, M., Richter-Pechanski, P., & Karl, A. (2025). Extending CARDIO:DE: Additional annotation guidelines and evaluation of NLP approaches for clinical applications. *International Journal of Medical Informatics, 203*, 106009.

van Koevorden, J. W., Aben, N., Struben, V., Rollings, A., Kurban, M., Wessels, L., van der Noort, V., Burger, A. V. M., van Dijk, S. W., Karssemakers, L., Smeele, L., Wouters, M. W. J. M., & Dirven, R. (2026). Validating large language model-assisted data extraction from clinical notes. *ESMO Real World Data and Digital Oncology, 12*, 100718.

---

## Lampiran kerja (bukan bagian naskah)

### Lampiran A. Tabel verifikasi klaim ke halaman PDF

Setiap baris dicocokkan otomatis ke teks halaman yang disebut (`tools/verify_claims.py` dengan `tools/claims_II7.json`; hasil: 33 dari 33 cocok). Nomor halaman = halaman berkas PDF.

| Sumber | Klaim di naskah | Hlm. | Kutipan asli (pendek) |
|---|---|---|---|
| Becker dkk. | CARDIO:DE: 500 surat dokter berbahasa Jerman; lima label entitas | 1, 2 | "500 clinical routine doctor’s letters"; "Diagnostic, Diagnosis, Drug, Medical_Finding, Therapy" |
| Becker dkk. | Dua anotator (apoteker, ekonom kesehatan); ± 15% tumpang tindih, lalu 5% tambahan; ambang alpha 0,85 | 2 | "about 15 % of the corpus was annotated by two experts"; "one a pharmacist with extensive clinical experience, the other a health economist"; "A threshold of 0.85 was set"; "an additional 5 % of the corpus was annotated with overlap"; "Krippendorff’s Alpha unitizing" |
| Becker dkk. | Kesepakatan hingga 0,98; tujuh bulan; 10–40 menit per dokumen | 1, 2 | "reaching up to 0.98 for certain subsets"; "The entire annotation process took seven months"; "ranged from 10 to 40 min" |
| Becker dkk. | Evaluasi menekankan batas entitas; TinyLlama F1 makro 0,845 | 1, 4 | "high emphasis on the correct recognition of entity boundaries"; "macro-average F1 score of 0.845" |
| Becker dkk. | Model sering menukar temuan medis dan diagnosis; contoh "80 % main stem stenosis" | 3, 4 | "commonly confuse MEDICAL_FINDING and DIAGNOSIS"; "80 % main stem stenosis" |
| van Koevorden dkk. | 60 pasien, 1.482 halaman, 29 kategori; dua dokter dan LLM sumber terbuka; enam pakar menilai 2.555 nilai | 1 | "Clinical documentation from 60 patients (1482 pages) was analyzed"; "Data were extracted for 29 clinically relevant categories by two physicians and a pretrained open-source LLM"; "Six clinical experts evaluated 2555 extracted values in a two-step procedure" |
| van Koevorden dkk. | Akurasi 74–90% per kategori; metrik ditetapkan pakar | 1, 4 | "accuracies between 74%"; "should therefore be interpreted as expert-assigned evaluation metrics" |
| van Koevorden dkk. | Disagreement dokter–dokter 29,0%; LLM–konsensus 41,4% (pemetaan awal) | 4 | "overall human—human disagreement rate of 29.0%"; "disagreement rate of 41.4%" |
| van Koevorden dkk. | > separuh keluaran semula berbeda dinyatakan cocok; 65 → 4 halusinasi terkonfirmasi | 5, 6 | "more than half of the LLM outputs initially scored as discrepant or partially overlapping were ultimately reclassified as valid matches"; "65 model responses were classified as hallucinations"; "only four were confirmed as genuine hallucinations" |
| van Koevorden dkk. | Satu penilai menandai 61 dari 68 galat berdampak tinggi; taksonomi dan metrik tidak cukup | 5 | "classifying errors as high-impact 61 of 68 times"; "insufficient to gauge the potential clinical consequences of extraction errors" |
| van Koevorden dkk. | Ekstraktor manusia sedikit; dokumen Belanda; generalisasi terbatas (pusat tersier) | 7, 8 | "The small number of human extractors limited our ability to statistically assess interobserver variability"; "capable of processing Dutch clinical documents effectively"; "Finally, a weakness of this study is the question of generalizability" |
| Sun dkk. | Evaluasi halusinasi bergantung penilaian pakar yang subjektif | 18 | "Evaluation of hallucination often relies heavily on expert judgment"; "these evaluations can be subjective and vary depending on the individual’s expertise" |

Pemeriksaan ketiadaan (bukan pencocokan frasa): pencarian `indonesia|malay|bahasa` pada teks kedua PDF tidak menemukan satu pun kecocokan.

### Lampiran B. Matriks catatan literatur (bahan untuk subbab II.8)

| Penulis, tahun | Data | Metode | Hasil utama | Celah terhadap penelitian ini |
|---|---|---|---|---|
| Becker dkk., 2025 | CARDIO:DE, 500 surat dokter berbahasa Jerman, 304.582 anotasi token | Anotasi iteratif dua pakar, IAA alpha unitizing (ambang 0,85); 4 model | IAA hingga 0,98; TinyLlama F1 makro 0,845 | Ekstraksi entitas dari satu dokumen; bahasa Jerman; kardiologi |
| van Koevorden dkk., 2026 | 60 pasien, 1.482 halaman, 29 kategori (onkologi kepala dan leher) | Validasi prospektif LLM vs konsensus 2 dokter; 6 penilai | Akurasi 74–90%; disagreement manusia 29,0%; halusinasi 0,16% setelah verifikasi | Ekstraksi nilai; bahasa Belanda; satu pusat tersier; penilai manusia sedikit |

### Lampiran C. Catatan peringatan dan penandaan

1. **Singh dkk. (JMIR Med Inform 2025)**, sumber ketiga pada kelompok evaluasi di daftar sumber, tidak ada di repo dan tidak dipakai. Daftar sumber menyebutnya contoh desain "algorithm development and validation".
2. **Kedua sumber mengevaluasi ekstraksi entitas atau nilai, bukan deteksi ketidaksesuaian.** Daftar sumber menyebut ketiganya sebagai "template untuk RQ3 — akurasi sistem dibanding label tenaga ahli". Secara desain (label tenaga ahli, panduan anotasi, ukuran kesepakatan) itu masuk akal, tetapi unit evaluasinya berbeda dari unit temuan pada Breakdown bagian 11; naskah menyatakannya sebagai keterbatasan.
3. **Becker dkk.:** F1 dihitung dengan pencocokan entitas yang ketat pada batas entitas, sehingga label dengan rentang panjang cenderung berskor lebih rendah (hlm. 3, 4). Ambang "0,85" adalah ambang kesepakatan yang dipilih penulis; penulis juga mencatat skor IAA tidak sebanding langsung dengan IAA berbasis F1 (hlm. 3). Tabel 2 memuat skor 0,79 sampai 0,98 pada iterasi berbeda; naskah hanya memakai nilai tertinggi yang dilaporkan abstrak. Naskah menyebut "dua pakar" dan "5%" mengikuti uraian metode, sementara angka lengkap per iterasi ada di Tabel 2.
4. **van Koevorden dkk.:** 41,4% adalah disagreement pada pemetaan awal, sebelum peninjauan yang mengubah lebih dari separuh nilai menjadi cocok (hlm. 5); jadi 41,4% tidak boleh dibaca sebagai tingkat galat LLM. Metrik presisi, recall, dan F1 diturunkan dari label pakar dengan pemetaan Match/Overcomplete sebagai benar positif dan Incorrect/Hallucination sebagai positif palsu (hlm. 4); definisi ini khas studi tersebut. Data berasal dari dokumen yang dipindai dan diproses OCR (dua pasien dikecualikan karena kualitas pindaian, hlm. 3), sedangkan Breakdown hanya memakai teks digital. Penghematan waktu (8,6 menjadi 1,9 menit; hlm. 6) hanya untuk langkah ekstraksi dan tidak dipakai di naskah.
5. **Hubungan dengan rancangan yang tidak diklaim di naskah.** Breakdown menetapkan satu tenaga ahli utama sebagai penentu label dan keterbatasan satu penilai dilaporkan. Kedua sumber menunjukkan bahwa ketidaksepakatan antarpenilai dapat besar; kalimat penutup II.7.2 menyatakan keterbatasan itu secara umum tanpa menyebut rancangan tim. Prinsip 5 (ukuran dan tanda gagal sebelum eksperimen) dan prinsip 8 (premis tersembunyi) menuntut ini dijembatani di Bab III.
6. **Rujukan silang Sun dkk. (2025, hlm. 18)** sudah diverifikasi pada berkas II.5 dan dipakai ulang di sini; entri daftar pustakanya ada pada II.5.
7. **Istilah yang perlu diverifikasi bentuk bakunya:** `penilai`, `anotator`/`anotasi`, `tumpang tindih`, `kesepakatan antarpenilai`, `acuan penilaian` [PERLU VERIFIKASI BENTUK BAKU]. `unitizing` ditulis miring sebagai istilah asing.
8. **Penanda `[SESUAIKAN DENGAN BAB I]`** pada kalimat penutup II.7.2 harus disamakan dengan rumusan pertanyaan dan ukuran keberhasilan Bab I.
