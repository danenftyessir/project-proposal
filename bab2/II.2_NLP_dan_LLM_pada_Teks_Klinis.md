# Bab II — Subbab II.2 (DRAFT 3: sub-subbab II.2.1–II.2.4; Schwieger dkk. dan Mehri dkk. ditambahkan)

> **Status:** draf kerja, belum ditinjau pembimbing. Hanya bagian "Naskah" dan "Daftar Pustaka (sementara)" yang masuk ke proposal. Bagian "Lampiran kerja" adalah alat bantu pemeriksaan dan tidak dihitung dalam batas 19 halaman.
>
> **Konvensi sitasi sementara:** penulis-tahun dengan nomor halaman (`hlm.`). Kesepuluh sumber adalah artikel bernomor artikel (nomor halaman cetak sama dengan halaman berkas PDF), sehingga `hlm.` = halaman berkas PDF. Format akhir menunggu pedoman program studi.
>
> **Sumber:** sepuluh artikel di `source/` (Luo; Elvas; Kumar; Woo; Schwieger; Mehri; Wei; Chen; Olex & McInnes; Jafarpour), semuanya dibaca dari PDF. Setiap angka dan klaim isi dicek otomatis ke teks halaman (Lampiran A). Tidak ada sumber dari `source/external/`.
>
> **Penanda yang perlu dijawab pengguna:** satu `[SESUAIKAN DENGAN BAB I]` pada subbab penutup.

---

## Naskah

## II.2 NLP dan LLM pada Teks Klinis

### II.2.1 Tugas dan Model Bahasa untuk Teks Klinis

Pemrosesan bahasa alami (*natural language processing*, NLP) klinis bertujuan mengekstraksi informasi medis yang relevan dari teks klinis tidak terstruktur (Olex & McInnes, 2021, hlm. 1). Luo dkk. (2024) mensurvei penerapan model bahasa pralatih (*pre-trained language model*, PLM) seperti BERT, BioBERT, dan ChatGPT pada tugas NLP medis, antara lain peringkasan teks, tanya jawab, pengenalan entitas bernama (*named entity recognition*, NER), dan ekstraksi informasi (hlm. 1). Elvas dkk. (2025) meninjau 31 studi tahun 2019–2024 yang berfokus pada NER dan melaporkan bahwa pendekatan berbasis BERT, jaringan saraf, serta CRF/LSTM mendominasi dengan F1 di atas 85% (hlm. 1). Kajian itu tidak menilai mutu studi secara formal dan sengaja mengecualikan model bahasa besar (*large language model*, LLM) (hlm. 2), sehingga tidak menggambarkan penggunaan model generatif.

Bukti tersebut berasal terutama dari bahasa Inggris. Dari 31 studi dalam kajian Elvas dkk., 17 memakai teks berbahasa Inggris (hlm. 4). Kumar dkk. (2026), yang menelaah 153 studi secara sistematis (hlm. 3), menyatakan bahwa kemajuan NLP klinis terpusat pada bahasa Inggris dan bahasa bersumber daya tinggi lainnya, serta bahwa alih kode, transliterasi, dan ortografi tidak baku mempersulit tokenisasi dan *parsing* (hlm. 21).

### II.2.2 LLM untuk Dokumentasi Klinis dan Ringkasan Pulang

Woo dkk. (2026) menelaah 41 studi penggunaan LLM untuk dokumentasi klinis, terutama pembuatan catatan klinis, ringkasan pulang, dan dokumentasi pertemuan tenaga kesehatan dan pasien (hlm. 1). Sebagian studi melaporkan penghematan waktu hingga 40%, tetapi ketidakakuratan faktual, halusinasi, dan penurunan kinerja pada kasus kompleks sering ditemukan (hlm. 1). Cakupan kajian ini terbatas: 17 dari 41 studi berasal dari Amerika Serikat (hlm. 4), studi nonbahasa Inggris dikecualikan, dan menurut penulisnya sebagian besar studi dilakukan pada lingkungan terkendali atau simulasi (hlm. 11).

Dua studi primer membandingkan ringkasan pulang buatan LLM dengan tulisan dokter, dan hasilnya berbeda. Schwieger dkk. (2024) membandingkan 20 ringkasan pulang rawat inap psikiatri tulisan dokter residen dengan ringkasan buatan ChatGPT-4 dari catatan residen yang telah dipseudonimkan (hlm. 1). Delapan spesialis psikiatri yang tidak mengetahui sumbernya memberi skor rata-rata 3,78 untuk tulisan residen dan 3,12 untuk ChatGPT-4, dan halusinasi ditemukan pada 40% ringkasan ChatGPT-4 (hlm. 1). Mehri dkk. (2026) menilai 292 pasang ringkasan pulang dari 16 departemen di satu rumah sakit akademik Belanda, dengan versi LLM dibuat otomatis oleh sistem yang terintegrasi dengan rekam medis elektronik (hlm. 1, 5). Kelengkapan versi LLM lebih rendah (median 4,5 terhadap 5,0), ketepatannya serupa, dan skor total tidak berbeda; kedua penilai mempercayai 249 ringkasan LLM (85,3%), dibandingkan 279 ringkasan dokter (95,5%) (hlm. 6). Penilai menyatakan tidak menemukan halusinasi atau informasi yang tidak masuk akal secara klinis, tetapi halusinasi tidak dinilai sebagai domain tersendiri (hlm. 9).

Schwieger dkk. menyebut sampel kecil dan kesepakatan antarpenilai yang rendah sampai sedang sebagai batasan (hlm. 8). Mehri dkk. membatasi diri pada satu rumah sakit dan ringkasan berbahasa Belanda (hlm. 9); dari 292 pasang, 12 berasal dari kebidanan dan kandungan serta 29 dari pediatri (hlm. 6). Penilaian pada kedua studi dilakukan oleh manusia dengan tulisan dokter sebagai pembanding, bukan melalui pemeriksaan otomatis kesesuaian ringkasan dengan catatan sumbernya, dan keduanya tidak memakai data berbahasa Indonesia.

### II.2.3 Singkatan, Normalisasi Istilah, dan Penalaran Temporal

Jafarpour dkk. (2025) menyebut kalimat tidak gramatikal, singkatan, akronim, karakter khusus yang bermakna, negasi, dan salah ketik sesekali sebagai ciri catatan rekam medis elektronik naratif (hlm. 1). Ambiguitas singkatan menjadi salah satu persoalan praktisnya. Wei dkk. (2026) mengubah disambiguasi singkatan klinis dari pembangkitan terbuka menjadi pemilihan terbatas dari sejumlah kandidat ekspansi (hlm. 1). Pada dataset CASI berbahasa Inggris versi bersih buatan Adams, Gemma-2-9B-IT mencapai akurasi 0,9228 dan macro-F1 0,9279, sedangkan pada versi asli yang memuat lebih banyak derau (*noise*) akurasinya 0,7585 (hlm. 1, 5). Penulisnya menyatakan tiga keterbatasan: akurasi bergantung pada inventori makna sehingga istilah di luar inventori dan istilah baru sulit ditangani, seleksi peka terhadap mutu konteks, dan evaluasi hanya memakai satu tolok ukur sehingga korpus klinis nonbahasa Inggris belum diuji (hlm. 9).

Normalisasi istilah ke konsep baku berkaitan erat dengan persoalan itu. Chen dkk. (2026) mensurvei *medical concept normalization* (MCN), yaitu pemetaan frasa medis informal ke konsep baku dalam basis terstandar seperti UMLS, SNOMED CT, atau MeSH (hlm. 1, 4); UMLS memuat ICD (hlm. 6). Survei itu menilai korpus berbahasa Inggris mendominasi penelitian MCN, sedangkan penggabungan sumber multibahasa terhambat oleh pedoman anotasi yang berbeda antarbahasa, granularitas ontologi yang berbeda, dan terjemahan harfiah yang menghilangkan nuansa (hlm. 8).

Penalaran temporal merupakan komponen kunci NLP klinis karena pemahaman riwayat pasien sangat bergantung pada kemampuan mengidentifikasi dan menalar informasi temporal (Olex & McInnes, 2021, hlm. 1). Olex dan McInnes mencontohkan bahwa ungkapan “3 hari lalu” bergantung pada waktu pembuatan dokumen, sedangkan “2 jam setelah minum obat” bergantung pada kejadian lain (hlm. 2). Mereka menyimpulkan bahwa sistem ekstraksi lini masa belum cukup baik untuk praktik klinis; penanganan ungkapan temporal relatif dan implisit termasuk bidang yang memerlukan solusi baru (hlm. 1). Pada tugas bersama (*shared task*) yang mereka tinjau, sistem berbasis aturan terbaik untuk mengenali dan menormalkan ekspresi temporal, sedangkan metode pembelajaran mesin statistik unggul untuk mengenali kejadian dan mengklasifikasi relasi temporal (hlm. 2). Tinjauan itu terbit tahun 2021 dan tidak menyebut LLM. Untuk LLM, Woo dkk. (2026) melaporkan bahwa GPT-4o dalam salah satu studi yang mereka rangkum andal pada konsultasi neurovaskular tetapi kesulitan pada lintasan pasien yang kompleks secara temporal (hlm. 9). Menurut Jafarpour dkk. (2025), yang menelaah deteksi kejadian tidak diharapkan di rumah sakit dengan teks berbahasa Inggris (hlm. 1, 4), ketiadaan informasi temporal dapat membuat model keliru membedakan kejadian sebelum dan selama rawat inap (hlm. 9).

### II.2.4 Sintesis dan Celah

Kesepuluh sumber menunjukkan bahwa PLM dan LLM telah luas dipakai pada teks klinis, tetapi bukti yang tersedia memiliki tiga keterbatasan bagi penelitian ini. Pertama, tidak ada sumber yang mengevaluasi teks klinis berbahasa Indonesia, dan sebagian menyebut dominasi bahasa Inggris pada penelitian di bidangnya (Chen dkk., 2026, hlm. 8; Kumar dkk., 2026, hlm. 21). Kedua, bukti tentang LLM pada dokumentasi klinis berpusat pada pembuatan dokumen, bukan pemeriksaan kesesuaian antardokumen (Woo dkk., 2026, hlm. 1), dan hasilnya tidak seragam: halusinasi ditemukan pada 40% ringkasan pulang dalam satu studi (Schwieger dkk., 2024, hlm. 1), sedangkan penilai pada studi lain tidak menemukannya (Mehri dkk., 2026, hlm. 9). Ketiga, hasil disambiguasi singkatan yang dikaji di sini berasal dari satu dataset berbahasa Inggris dan turun dari akurasi 0,9228 menjadi 0,7585 pada versi yang memuat lebih banyak derau (Wei dkk., 2026, hlm. 1, 5, 9). Karena itu, kinerja teknik-teknik ini pada rekam medis rawat inap kebidanan dan anak berbahasa Indonesia tidak dapat diasumsikan dan harus diukur langsung pada data tersebut [SESUAIKAN DENGAN BAB I: rumusan pertanyaan dan ukuran keberhasilan].

---

## Daftar Pustaka (sementara)

> **[FORMAT AKHIR PERLU DIKONFIRMASI]** Pola mengikuti contoh pada templat (gaya mirip APA). Metadata diambil dari halaman pertama masing-masing PDF; DOI tidak dicantumkan karena belum diperiksa satu per satu.

Chen, H., Zhou, Y., Li, R., Illa, A. M., Cleveland, A., & Ding, J. (2026). A comprehensive survey on medical concept normalization: Datasets, techniques, applications, and future directions. *Journal of Biomedical Informatics, 178*, 105005.

Elvas, L. B., Almeida, A., & Ferreira, J. C. (2025). Natural language processing in medical text processing: A scoping literature review. *International Journal of Medical Informatics, 204*, 106049.

Jafarpour, H., Wu, G., Cheligeer, C., Yan, J., Xu, Y., Southern, D. A., Eastwood, C. A., Zeng, Y., & Quan, H. (2025). Preprocessing narrative texts in electronic medical records to identify hospital adverse events: A scoping review. *Artificial Intelligence in Medicine, 170*, 103281.

Kumar, D., Choudhary, N., Gupta, V., Tanwar, R., Behmani, K., Antal, S., Jarora, S., Gupta, S., Shaikh, M. S., Webster, T. J., & Faiyazuddin, M. (2026). Natural language processing in healthcare: From unstructured data to clinical intelligence. *Intelligent Systems with Applications, 31*, 200698.

Luo, X., Deng, Z., Yang, B., & Luo, M. Y. (2024). Pre-trained language models in medicine: A survey. *Artificial Intelligence in Medicine, 154*, 102904.

Mehri, T., Nadalini, T., Hoekman, A. H., van der Laan, T. P., Kagialari, K., Wagner, R. K., Doornberg, J. N., Schoonbeek, R. C., & Bootsma-Robroeks, C. M. H. H. T. (2026). Assessing the quality of AI-generated and physician-written discharge summaries: Evaluation of an EHR-integrated tool in a Dutch academic hospital. *eBioMedicine, 127*, 106247.

Olex, A. L., & McInnes, B. T. (2021). Review of temporal reasoning in the clinical domain for timeline extraction: Where we are and where we need to be. *Journal of Biomedical Informatics, 118*, 103784.

Schwieger, A., Angst, K., de Bardeci, M., Burrer, A., Cathomas, F., Ferrea, S., Grätz, F., Knorr, M., Kronenberg, G., Spiller, T., Troi, D., Seifritz, E., Weber, S., & Olbrich, S. (2024). Large language models can support generation of standardized discharge summaries: A retrospective study utilizing ChatGPT-4 and electronic health records. *International Journal of Medical Informatics, 192*, 105654.

Wei, S., Liu, X., & Shi, Y. (2026). Selection-based prompting with synthesized candidates unlocks high-performance clinical abbreviation disambiguation via open-source LLMs. *Journal of Biomedical Informatics, 181*, 105085.

Woo, B. F. Y., Cato, K., Cho, H., You, S. B., & Song, J. (2026). The use of large language models in clinical documentation: A scoping review. *International Journal of Nursing Studies, 176*, 105322.

---

## Lampiran kerja (bukan bagian naskah)

### Lampiran A. Tabel verifikasi klaim ke halaman PDF

Setiap baris dicocokkan otomatis ke teks halaman yang disebut (`tools/verify_claims.py` dengan `tools/claims_II2.json`; hasil: 57 dari 57 cocok). Nomor halaman = halaman berkas PDF = nomor cetak. Khusus angka tabel (Elvas dkk., hlm. 4), jumlah per bahasa dibaca dari teks tabel hasil ekstraksi.

| Sumber | Klaim di naskah | Hlm. | Kutipan asli (pendek) |
|---|---|---|---|
| Olex & McInnes | NLP klinis mengekstraksi informasi medis dari teks tidak terstruktur | 1 | "automatically extract medically relevant information from unstructured clinical texts" |
| Luo dkk. | PLM (BERT, BioBERT, ChatGPT) pada tugas NLP medis: peringkasan, tanya jawab, NER, ekstraksi informasi | 1 | "text summarisation, question-answering, machine translation, sentiment analysis, named entity recognition, information extraction" |
| Elvas dkk. | 31 studi, 2019–2024, fokus NER | 1, 2 | "Of 67 initial records, 31 studies were ultimately included" |
| Elvas dkk. | BERT, jaringan saraf, CRF/LSTM mendominasi; F1 di atas 85% | 1 | "consistently achieving F1-scores above 85 %" |
| Elvas dkk. | Tanpa penilaian mutu formal; LLM dikecualikan | 2 | "we did not perform a formal quality appraisal"; "We decided to exclude large language models (LLMs)" |
| Elvas dkk. | Korpus: Inggris 17, Tionghoa 9, Italia 2, Jerman 2, Spanyol 1 | 4 | Tabel 1 "Reviewed articles by their data languages" (kolom Count: 17, 9, 2, 2, 1) |
| Kumar dkk. | 153 studi, tinjauan sistematis (PRISMA) | 3 | "153 studies were eligible" |
| Kumar dkk. | Kemajuan terpusat pada bahasa Inggris dan bahasa bersumber daya tinggi; alih kode, transliterasi, ortografi tidak baku mempersulit tokenisasi dan *parsing* | 21 | "concentrated primarily in English and other high-resource languages"; "code-switching, transliteration, and non-standard orthography further complicate tokenization and parsing" |
| Woo dkk. | 41 studi; pembuatan catatan, ringkasan pulang, dokumentasi pertemuan | 1 | "Forty-one studies met inclusion criteria"; "clinical note generation, discharge summaries, and provider-patient encounter documentation" |
| Woo dkk. | Penghematan waktu hingga 40%; ketidakakuratan, halusinasi, penurunan kinerja pada kasus kompleks umum | 1 | "up to 40 % time savings"; "factual inaccuracies, hallucinations, and reduced performance in complex cases were common" |
| Woo dkk. | 17 dari 41 studi dari AS | 4 | "originated from the United States (US) (n = 17)" |
| Woo dkk. | Sebagian besar studi di lingkungan terkendali/simulasi (menurut penulis); studi nonbahasa Inggris dikecualikan | 11 | "most studies were conducted in controlled or simulated environments"; "non-English studies were excluded" |
| Woo dkk. | GPT-4o andal pada konsultasi neurovaskular, kesulitan pada lintasan pasien kompleks secara temporal (sekunder: Indrakanti dkk. 2025) | 9 | "GPT-4o performed reliably for neurovascular consultations but struggled with temporally complex patient trajectories" |
| Schwieger dkk. | 20 ringkasan pulang rawat inap psikiatri tulisan residen vs ChatGPT-4 dari catatan yang dipseudonimkan; 8 spesialis tersamar; skor rata-rata 3,78 vs 3,12; halusinasi pada 40% ringkasan ChatGPT-4 | 1 | "compared 20 inpatient DS, written by residents"; "8 blinded psychiatry specialists"; "mean ratings: human 3.78, AI 3.12"; "Hallucinations were present in 40 % of AI-DS" |
| Schwieger dkk. | Pemeriksaan halusinasi oleh peneliti: telaah kasus tanpa penyamaran, kedua versi dibandingkan dengan rekam medis elektronik masing-masing | 2 | "unblinded case-based review, comparing both DS versions qualitatively with their respective EHRs" |
| Schwieger dkk. | Batasan: sampel kecil; kesepakatan antarpenilai rendah sampai sedang (tiga batasan lain pada kalimat yang sama, pembatasan token, LLM tidak dikhususkan, dan tanpa evaluasi formal kelengkapan, tidak dipakai di naskah) | 8 | "the small sample size, the token restriction, the low to moderate inter-rater agreement, the use of a non-specialized LLM, and no formal evaluation of information" |
| Mehri dkk. | 292 pasang ringkasan pulang; sistem LLM terintegrasi rekam medis elektronik; rumah sakit akademik Belanda | 1 | "A total of 292 paired discharge summaries"; "EHR-integrated"; "Dutch academic hospital" |
| Mehri dkk. | 16 departemen | 5 | "Discharge summaries originated from 16 clinical departments" |
| Mehri dkk. | Kelengkapan median 4,5 vs 5,0; ketepatan serupa; skor total tidak berbeda; kepercayaan oleh kedua penilai 249 (85,3%) vs 279 (95,5%); ditolak kedua penilai 9 (3,1%) | 6 | "median completeness score of 4.5 (4.0–5.0), compared to 5.0"; "p = 0.14"; "trusted by both reviewers in 249 (85.3%) cases"; "rejected by both in 9"; "trusted by both reviewers in 279 (95.5%) of 292 cases" |
| Mehri dkk. | Obstetri dan ginekologi n=12; pediatri n=29 | 6 | Gambar 2: "Pediatrics (n=29)"; "Obstetrics and Gynecology (n=12)" |
| Mehri dkk. | Halusinasi tidak dinilai sebagai domain tersendiri; penilai tidak menemukan informasi berhalusinasi atau tidak masuk akal secara klinis | 9 | "no hallucinated or clinically implausible information was identified by the clinician raters"; "not scored as a separate domain" |
| Mehri dkk. | Satu rumah sakit akademik Belanda; ringkasan berbahasa Belanda | 9 | "single Dutch academic hospital and limited to Dutch-language summaries" |
| Mehri dkk. | (Tidak dipakai di naskah draf 3, dicatat sebagai bahan) skor menumpuk di ujung atas skala (efek langit-langit) | 10 | "clustered near the upper end of the Likert scale, indicating a ceiling effect" |
| Jafarpour dkk. | Ciri catatan EMR naratif | 1 | "grammatically incorrect sentences, abbreviations, frequent acronyms, specialized characters with particular meanings, negation expressions, and sporadic misspellings" |
| Jafarpour dkk. | Topik deteksi kejadian tidak diharapkan di rumah sakit; teks klinis berbahasa Inggris | 1, 4 | "hospital adverse events"; "composed in the English language" |
| Jafarpour dkk. | Informasi temporal membedakan kejadian sebelum dan selama rawat inap | 9 | "differentiate between past events and current occurrences"; "events occurring during hospitalization or events that transpired prior to hospitalization" |
| Wei dkk. | Seleksi terbatas (bukan pembangkitan terbuka); kumpulan tujuh opsi; dua jalur | 1 | "shifts the paradigm from generation to constrained selection"; "Discriminative selection from the resulting 7-option pool" |
| Wei dkk. | Gemma-2-9B-IT: akurasi 0,9228, Macro-F1 0,9279 (CASI bersih); akurasi 0,7585 (CASI asli) | 1 | "accuracy: 0.9228, Macro-F1: 0.9279"; "accuracy: 0.7585" |
| Wei dkk. | Dataset CASI berbahasa Inggris; versi asli mengandung derau | 5 | "two versions of the English CASI dataset"; "While the original dataset contains noise" |
| Wei dkk. | Pembangkitan langsung (tahap 1 saja) 0,6304 pada Gemma-2-9B-IT | 7 | "the baseline using only Stage 1 direct generation performs substantially lower at 0.6304" |
| Wei dkk. | Definisi singkatan berhuruf kapital | 5 | "defined as a shortened form consisting of capital letters" |
| Wei dkk. | Tiga keterbatasan: inventori makna, mutu konteks, satu tolok ukur; korpus nonbahasa Inggris belum diuji | 9 | "intrinsically tied to the retrieval inventory"; "out-of-vocabulary terms or evolving medical neologisms"; "sensitive to context quality"; "anchored to the CASI benchmark"; "non-English clinical corpora" |
| Chen dkk. | Definisi MCN; target UMLS, SNOMED CT, MeSH | 1, 4 | "mapping informal medical terms or phrases to standardized medical concepts"; "the target medical databases include the Unified Medical Language System" |
| Chen dkk. | UMLS memuat ICD | 6 | "over 200 source vocabularies across 29 languages, including ICD, SNOMED-CT, and MeSH" |
| Chen dkk. | Aturan dan leksikon eksplisit andal untuk disambiguasi singkatan | 13 | "where explicit rules and lexicons are reliable" |
| Chen dkk. | Korpus Inggris mendominasi MCN; pedoman anotasi, granularitas ontologi, terjemahan harfiah | 8 | "English corpora currently dominate MCN research"; "Annotation guidelines diverge across languages, ontologies differ in conceptual granularity"; "literal term translations often lose language-specific" |
| Olex & McInnes | Penalaran temporal sebagai komponen kunci NLP klinis | 1 | "understanding a patient's medical history relies heavily on the ability to identify, assimilate, and reason over temporal information" |
| Olex & McInnes | Lima cara informasi temporal (menurut Lim dkk.) | 2 | "five ways temporal information can be conveyed in text: explicit, implicit, relative, vague, and non-consuming" |
| Olex & McInnes | "3 days ago" relatif terhadap waktu dokumen; "2 h after taking medication" relatif terhadap kejadian | 2 | "may be relative to the document creation time"; "are relative to when the event" |
| Olex & McInnes | Keadaan mutakhir belum siap praktik klinis; ungkapan relatif dan implisit sebagai bidang yang memerlukan solusi | 1 | "the current state-of-the-art still has a ways to go before practical application in the clinical setting will be possible"; "handling relative and implicit temporal expressions" |
| Olex & McInnes | Tugas bersama: aturan terbaik untuk ekspresi temporal; ML statistik unggul untuk kejadian dan relasi | 2 | "rule-based systems that expanded the top general-domain temporal taggers"; "statistical machine learning methods outperformed rule-based methods for event" |

Pemeriksaan ketiadaan (bukan pencocokan frasa): pencarian `indonesia|malay|bahasa` pada teks delapan PDF pertama hanya menemukan satu kecocokan, yaitu nama "University Malaya Medical Centre" pada daftar pustaka Elvas dkk.; pada teks Schwieger dkk. dan Mehri dkk. pencarian yang sama tidak menemukan kecocokan sama sekali; frasa "large language model" tidak ada dalam teks Olex & McInnes.

### Lampiran B. Matriks catatan literatur (bahan untuk subbab II.8)

| Penulis, tahun | Data | Metode | Hasil utama | Celah terhadap penelitian ini |
|---|---|---|---|---|
| Luo dkk., 2024 | Survei PLM pada tugas NLP medis | Survei naratif, banyak tugas | PLM dipakai luas untuk peringkasan, tanya jawab, NER, ekstraksi informasi | Bahasa Indonesia tidak muncul; bukan tentang audit dokumentasi |
| Elvas dkk., 2025 | 31 studi NER, 2019–2024 | *Scoping review* (Scopus, PubMed) | BERT, jaringan saraf, CRF/LSTM mendominasi, F1 di atas 85% | LLM dikecualikan; tanpa penilaian mutu; tanpa studi berbahasa Indonesia |
| Kumar dkk., 2026 | 153 studi | Tinjauan sistematis | Kemajuan terpusat pada bahasa Inggris; korpus klinis beranotasi terbatas | Tinjauan luas; tidak menguji teks Indonesia |
| Woo dkk., 2026 | 41 studi LLM untuk dokumentasi klinis | *Scoping review* (JBI) | Penghematan waktu hingga 40%; halusinasi dan ketidakakuratan umum | LLM sebagai penulis, bukan pemeriksa; studi nonbahasa Inggris dikecualikan |
| Schwieger dkk., 2024 | 20 ringkasan pulang rawat inap psikiatri, satu rumah sakit di Zurich | Studi retrospektif; ChatGPT-4 dengan perintah standar; 8 penilai tersamar | Skor rata-rata 3,78 (residen) vs 3,12 (LLM); halusinasi 40% | Sampel kecil; satu bidang; menilai mutu ringkasan, bukan kesesuaian dengan catatan sumber secara otomatis; tanpa teks Indonesia |
| Mehri dkk., 2026 | 292 pasang ringkasan pulang, 16 departemen, satu rumah sakit akademik Belanda | Evaluasi LLM terintegrasi rekam medis elektronik; 8 penilai tersamar | Kelengkapan lebih rendah; ketepatan serupa; skor total sama; ditolak kedua penilai 3,1% | Satu rumah sakit dan satu bahasa (Belanda); efek langit-langit; tanpa teks Indonesia |
| Jafarpour dkk., 2025 | 48 studi prapemrosesan EMR naratif untuk deteksi kejadian tidak diharapkan | *Scoping review* (PRISMA-ScR) | Tantangan: panjang teks, tokenisasi, normalisasi, informasi temporal | Hanya teks Inggris; topiknya kejadian tidak diharapkan |
| Wei dkk., 2026 | CASI asli dan versi bersih (Inggris), enam LLM 7–9B | S-ACAD: seleksi terbatas dari tujuh kandidat | Gemma-2-9B-IT 0,9228 (bersih), 0,7585 (asli); pembangkitan langsung 0,6304 | Satu tolok ukur Inggris; bergantung pada inventori makna |
| Chen dkk., 2026 | Survei MCN | Survei metodologis | Korpus Inggris mendominasi; aturan masih andal untuk subtugas sempit | Sumber informal terutama media sosial, literatur, EHR; tidak memuat bahasa Indonesia |
| Olex & McInnes, 2021 | Tinjauan ekstraksi lini masa klinis | Tinjauan naratif | Sistem belum siap praktik; ungkapan relatif dan implisit sulit | Terbit 2021, tanpa LLM; bahasa korpus tidak dinyatakan pada teks yang dibaca |

### Lampiran C. Catatan peringatan dan penandaan

1. **Tidak ada sumber yang menguji teks klinis berbahasa Indonesia.** Pernyataan ini dibatasi pada sepuluh sumber yang dibaca (lihat pemeriksaan ketiadaan pada Lampiran A). Ini bukan klaim tentang seluruh literatur.
2. **Woo dkk., Schwieger dkk., dan Mehri dkk. menelaah LLM sebagai penulis dokumen, bukan sebagai pemeriksa.** Kalimat "bukan melalui pemeriksaan otomatis kesesuaian ringkasan dengan catatan sumbernya" pada II.2.2 adalah pemeriksaan ketiadaan atas cara kedua studi itu bekerja (penilaian oleh manusia; halusinasi pada Schwieger diperiksa peneliti secara kualitatif terhadap rekam medis, hlm. 2). Kalimat penafsiran lama tentang "peringatan keandalan" dikeluarkan pada draf 3 karena Schwieger dan Mehri sudah memberi bukti langsung yang saling berlawanan.
3. **Angka sekunder.** GPT-4o pada lintasan temporal (Indrakanti dkk., 2025) dikutip dari ulasan Woo dkk. pada II.2.3; studi aslinya tidak ada di repo dan tidak masuk daftar pustaka. Angka 36% (Baker dkk., 2024) dan 61% (Ando dkk., 2022) dikeluarkan dari naskah pada draf 3 demi ruang karena Schwieger dan Mehri memberi angka primer.
4. **Ketegangan internal pada Woo dkk.** Hlm. 4 menyebut 30 dari 41 studi memakai data dunia nyata dan 9 data simulasi, sedangkan keterbatasan pada hlm. 11 menyatakan sebagian besar studi dilakukan pada lingkungan terkendali atau simulasi. Naskah mengutip pernyataan terakhir dengan atribusi "menurut penulisnya"; kedua pernyataan dapat benar bersama (data nyata yang dievaluasi di lingkungan terkendali), tetapi artikelnya tidak merinci.
5. **Ketidakkonsistenan angka pada Elvas dkk.** Jumlah pada Tabel 1 (17, 9, 2, 2, 1) berjumlah 31, tetapi persentase di abstrak dan teks (51,5%; 27,3%; 6,1%; 3,0%) sesuai dengan penyebut 33. Naskah memakai jumlah dan tidak memakai persentase (termasuk persentase metode, 36,4%; 33,3%; 30,3%). Pernyataan "F1 di atas 85%" adalah klaim penulis dalam abstrak, bukan hasil gabungan yang diperiksa ke studi primer.
6. **Atribusi pada Olex & McInnes.** Lima kategori informasi temporal adalah rumusan Lim dkk. yang dilaporkan di sana (hlm. 2); hasil tugas bersama bersandar pada Sun dkk. [18] dalam daftar pustaka mereka. Tinjauan ini terbit 2021 dan tidak menyebut LLM. Bahasa korpus yang ditinjau tidak dinyatakan pada teks yang dibaca, sehingga naskah tidak menyebutnya berbahasa Inggris.
7. **Wei dkk.:** angka 0,6304 adalah ablasi "tahap 1 saja" pada Gemma-2-9B-IT; penulis membandingkannya dengan 0,9228 (dataset bersih). Klaim tentang privasi dan biaya pada abstrak mereka tidak dipakai. Kinerja pada teks Indonesia tidak diuji dan tidak diklaim.
8. **Chen dkk.:** sumber frasa informal dalam survei terutama media sosial, literatur biomedis, dan EHR (hlm. 4); kalimat "aturan dan leksikon eksplisit dinilai masih andal" bersandar pada karya lain yang disurvei (Mowery dkk.; Kate), jadi bersifat sekunder.
9. **Kumar dkk. hlm. 12 (bagian 6.1: sistem berbasis aturan dapat diprediksi dan mudah divalidasi tetapi tidak skalabel lintas institusi)** sengaja dicadangkan untuk II.4 (hibrida). Angka pada studi kasus ilustratif Kumar dkk. tidak dipakai karena dikutip dari karya lain.
10. **Jafarpour dkk.** hanya dipakai untuk tantangan prapemrosesan umum (ciri teks, informasi temporal); topiknya deteksi kejadian tidak diharapkan, bukan audit klaim. Kalimat tentang batas masukan 512 "kata" pada BERT dikeluarkan pada draf 3 (demi ruang, dan karena BERT lazimnya membatasi token subkata, bukan kata [PERLU VERIFIKASI SUMBER]); klaimnya masih ada pada `claims_II2.json` dan tidak dipakai naskah.
11. **Luo dkk.:** bahasa Indonesia tidak muncul di bagian PLM nonbahasa Inggris (Persia, Korea, Prancis, Rusia, Vietnam, Tionghoa; hlm. 35). Kalimat ini dikeluarkan dari naskah demi ruang dan dapat dikembalikan bila perlu.
12. **Tidak tersedia:** Kayira dkk. (JMIR AI 2026) pada daftar untuk II.2; PDF-nya belum diunggah. Tidak dipakai.
13. **Definisi LLM** ada di II.2.1 (kemunculan pertama dalam bab, pada kalimat tentang Elvas dkk.). II.3 diubah agar tidak mendefinisikannya ulang (`LLM` langsung dipakai pada kalimat pembuka II.3.1).
14. **Istilah yang perlu diverifikasi bentuk bakunya:** `pralatih` (untuk *pre-trained*), `derau` (untuk *noise*), `alih kode`, `tokenisasi`, `ortografi`, `inventori makna`, `dipseudonimkan` (untuk *pseudonymized*; alternatif `dianonimkan` tidak dipakai karena maknanya berbeda) [PERLU VERIFIKASI BENTUK BAKU]. `dataset` ditulis tanpa miring mengikuti pemakaian pada `RULES.md`.
15. **Penanda `[SESUAIKAN DENGAN BAB I]`:** kalimat penutup II.2.4 menyatakan perlunya mengukur kinerja terhadap pembanding dan ambang yang ditetapkan sebelum eksperimen. Rumusan pertanyaan dan ukuran keberhasilan akhir harus mengikuti Bab I yang belum ditulis.
16. **Perbaikan alat bantu pemeriksa:** fungsi `norm()` pada `tools/verify_claims.py` kini membuang tanda pisah lunak beserta jeda baris yang mengikutinya; dua frasa uji lama (`WE8`, `U3b`) adalah salah ketik frasa, bukan salah halaman. Ketiga berkas klaim dijalankan ulang: II.1 27/27, II.2 57/57, II.3 83/83.
17. **Schwieger dkk. (2024).** Studi retrospektif satu rumah sakit psikiatri di Zurich dengan 20 kasus; ringkasan dibuat ChatGPT-4 dari catatan yang dipseudonimkan secara manual (hlm. 3) dan perintah yang disetel peneliti pada 10 kasus lain (hlm. 2). Angka 40% halusinasi dan 37,5% yang dinilai sangat relevan secara klinis berasal dari abstrak; naskah hanya memakai 40%. Skor 3,78 vs 3,12 adalah rata-rata atas 15 subkategori skala Likert 1–5. Kesimpulan penulis bahwa ringkasan LLM berpotensi menjadi templat yang disempurnakan dokter (hlm. 1) tidak dipakai di naskah karena merupakan harapan penulis, bukan hasil yang diuji. Studi ini bukan tentang kebidanan, anak, klaim, atau teks Indonesia.
18. **Mehri dkk. (2026).** Model yang dipakai pada studi ini ialah GPT-4o, dan keluarannya hanya bagian perjalanan perawatan (*hospital course*) dari ringkasan pulang, dengan sistem yang dikelola vendor (hlm. 3, 10); angka kinerja karena itu tidak dapat disamakan dengan pembuatan seluruh ringkasan. Setiap pasang dinilai oleh dua dari delapan penilai (hlm. 4), sehingga "kedua penilai" pada naskah berarti kedua penilai pada pasang itu. Nama penulis kedua pada berkas ialah "Tun Nadalini", ditulis "Nadalini, T." pada daftar pustaka [PERLU VERIFIKASI SUMBER: bentuk nama]. Hasil Mehri dkk. (tanpa halusinasi yang teridentifikasi) bertentangan arah dengan Schwieger dkk. (halusinasi 40%); naskah memaparkan keduanya dan tidak memilih salah satu, dengan perbedaan desain (satu rumah sakit psikiatri vs banyak departemen, ChatGPT-4 vs GPT-4o, penilaian skala vs telaah kasus) sebagai penjelas yang mungkin, bukan sebagai penjelasan yang terbukti.
19. **Perubahan struktur (draf 3).** Woo dkk. dipindahkan dari II.2.1 ke II.2.2 bersama Schwieger dkk. dan Mehri dkk.; bagian singkatan, normalisasi, dan penalaran temporal menjadi II.2.3; sintesis menjadi II.2.4. Alasan: subbab II.2 memuat dua topik yang berbeda (alat dan model; tugas khusus teks klinis), dan topik dokumentasi dan ringkasan pulang berkaitan dengan fitur resume medis, sehingga pantas berdiri sendiri.
20. **Draf 4: kalimat Chen dkk. hlm. 13 (aturan dan leksikon eksplisit masih andal untuk disambiguasi singkatan) dihapus dari II.2.3 karena sudah dipakai pada II.4.1; kalimat Wei dkk. hlm. 5 tentang definisi singkatan berhuruf kapital juga dikeluarkan.** Klaimnya tetap lolos pada `claims_II2.json`.
