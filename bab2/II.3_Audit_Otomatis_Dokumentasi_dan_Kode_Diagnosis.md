# Bab II — Subbab II.3 (DRAFT 1)

> **Status:** draf kerja, belum ditinjau pembimbing. Hanya bagian "Naskah" dan "Daftar Pustaka (sementara)" yang masuk ke proposal. Seluruh bagian "Lampiran kerja" adalah alat bantu pemeriksaan dan tidak ikut dihitung dalam batas 19 halaman.
>
> **Konvensi sitasi sementara:** penulis-tahun, dengan nomor halaman (`hlm.`) untuk setiap klaim tentang isi artikel. Untuk artikel bernomor artikel (Elsevier), `hlm.` merujuk pada halaman berkas PDF (halaman 1 = halaman pertama PDF). Untuk Dietrich dan Stubbert (2026), `hlm.` merujuk pada nomor halaman cetak jurnal (95–101). Format akhir menunggu pedoman program studi.
>
> **Sumber:** enam artikel, lima di `source/` dan satu di `source/external/` (judulnya tercantum di *Sumber Literatur Bab 2*). Lebeña dkk. (2025) dikeluarkan pada draf 2 (lihat Lampiran C butir 1). Semua angka dibaca dari PDF dan dicek ulang ke halaman (lihat Lampiran A).

---

## Naskah

## II.3 Audit Otomatis Dokumentasi Klinis dan Kode Diagnosis

Subbab ini menelaah enam studi yang memeriksa dokumentasi klinis atau kode diagnosis secara otomatis.

### II.3.1 Model Bahasa Besar sebagai Pemeriksa Dokumentasi

Dietrich dan Stubbert (2026) mengevaluasi empat LLM sebagai pemeriksa catatan pemulangan instalasi gawat darurat (IGD). Data berasal dari 600 kunjungan pada basis data MIMIC-IV-ED. Sebanyak 500 catatan masing-masing disisipi satu kesalahan dari lima kategori, dan 100 catatan lain tidak memuat kesalahan (hlm. 95–96). Akurasi deteksi kesalahan apa pun berkisar 93,2–94,2%, presisi 98,3–99,1%, dan spesifisitas 92,0–96,0% (hlm. 98). Kinerja berbeda menurut kategori. Ketidaksesuaian identitas atau waktu kunjungan serta kesalahan obat dan alergi terdeteksi dengan F1 ≥0,96, sedangkan ketidaksesuaian antara tanda vital atau pemeriksaan fisik dan interpretasi naratif paling sulit, dengan F1 0,75–0,84 yang terutama disebabkan oleh rendahnya *recall* (hlm. 98).

Rancangan itu membatasi cakupan kesimpulannya. Kesalahan disisipkan oleh peneliti, bukan muncul secara alami, dan seluruh data berasal dari satu institusi (hlm. 100). Setiap catatan hanya memuat satu kesalahan, dan catatan yang dinilai adalah satu dokumen yang disusun dari elemen data terstruktur kunjungan (hlm. 96). Karena 500 dari 600 catatan memuat kesalahan (hlm. 95), presisi yang tinggi itu tidak dapat langsung dipindahkan ke populasi dengan proporsi ketidaksesuaian yang lebih rendah. Penulis sendiri menyebut kerangka audit berbasis agen yang mengambil pedoman dan memeriksa konsistensi lintas dokumen sebagai arah penelitian lanjutan (hlm. 100).

Skrabic dkk. (2026) menguji tiga model penalaran sebagai pemeriksa kedua (*second reviewer*) pada 102 laporan unit gawat darurat penyakit dalam yang identitasnya telah dihapus (hlm. 1–2). Dua dokter spesialis menyisipkan 99 kesalahan yang realistis dan menandai tiga kesalahan yang sudah ada dalam laporan asli (hlm. 2). Model menerima satu perintah seragam tanpa pengambilan referensi atau pemanggilan fungsi (hlm. 3). Model menemukan lokasi kesalahan dengan benar pada 65,7–79,2% laporan, sedangkan tiga dokter pembanding, yang masing-masing meninjau sepertiga kasus, menemukan 48,0% (hlm. 4). Studi ini tidak menyertakan catatan tanpa kesalahan sehingga perilaku positif palsu belum dapat dipastikan, dan datanya berasal dari satu pusat layanan (hlm. 6).

### II.3.2 Audit Label Diagnosis dan Kesesuaian Kode dengan Catatan Klinis

Du dkk. (2026) memeriksa label diagnosis, bukan kesalahan yang disisipkan. Penelitian itu mengubah klasifikasi multilabel kode diagnosis psikiatri menjadi tugas tanya jawab dengan deskripsi dan penjelasan kode pada masukan (hlm. 1, 4), memakai 48.492 rekam dari 7.000 pasien di satu klinik psikiatri (hlm. 3, 12). Model terbaik memperoleh sum-F1 0,7417 (ukuran F1 berbasis ROUGE rancangan penulis, hlm. 6), hanya 0,013 di atas BERT dengan penjelasan kode (hlm. 8), dan selisih antara kode klinisi dan keluaran model dikelompokkan menjadi tiga tingkat risiko untuk menentukan kasus yang perlu ditinjau manusia (hlm. 7).

Acuan penilaiannya adalah diagnosis yang dicatat klinisi, yang menurut penulis dapat mengandung derau (*label noise*), tidak stabil dari waktu ke waktu, dan dipengaruhi tuntutan penagihan serta dokumentasi, tanpa pemodelan derau itu (hlm. 12). Mutu penjelasan model tidak dinilai klinisi (hlm. 13), dan pengetahuan acuan yang dimasukkan bersifat statis, yaitu deskripsi sepuluh kelompok kode dalam urutan tetap (hlm. 5), bukan referensi yang diambil sesuai kasus.

Mwogosi dan Mambile (2026) menelaah dari sisi lain, yaitu kesesuaian kode ICD dalam rekam medis elektronik dengan acuan klinis. Tinjauan sistematis dan metaanalisis ini merangkum 17 studi validasi (hlm. 1). Spesifisitas dan nilai prediktif positif kode konsisten tinggi, sering melebihi 90%, tetapi sensitivitas rata-rata hanya 64,5%, dengan catatan sebagian estimasi memakai prevalensi pengodean sebagai proksi sensitivitas (hlm. 1). Penulis menyimpulkan bahwa pendekatan hibrida yang menggabungkan kode, data klinis, dan narasi diperlukan (hlm. 1), tetapi acuan validasinya, yaitu penelusuran rekam medis, juga dapat bias akibat penyalinan teks dan terbawanya diagnosis usang (hlm. 11). Seluruh studi yang ditinjau berasal dari negara berpenghasilan tinggi (hlm. 4–5).

### II.3.3 Pengodean ICD Otomatis dan Ketahanannya terhadap Variasi Teks

Hou dkk. (2024) menyatakan bahwa pengodean otomatis umumnya diperlakukan sebagai klasifikasi teks multilabel, yaitu menetapkan kode ICD pada dokumen klinis (hlm. 1). Mereka memakai Clinical-Longformer untuk dokumen panjang dan mekanisme perhatian per label agar prediksi dapat diinterpretasi (hlm. 1–2). Pada 50 kode ICD-9 teratas di MIMIC-III, model memperoleh macro-F1 0,688 dan micro-F1 0,727 (hlm. 2). Mereka menilai pendekatan berbasis aturan kurang fleksibel dan sulit diperluas karena aturan dapat saling bertentangan seiring bertambahnya kode (hlm. 2).

Jaganathan dkk. (2025) menguji ketahanan model pengode ICD, yaitu PLM-ICD, dengan pengujian metamorfik (*metamorphic testing*). Catatan diubah secara sederhana, lalu daftar kode keluarannya dibandingkan dengan keluaran catatan asli. Pada 3.372 catatan uji MIMIC-III, penggantian akronim, penghapusan kata, dan salah ketik menyebabkan perbedaan pada lima kode teratas di 70–81% catatan (hlm. 4); penggantian dua puluh akronim yang paling sering muncul mencapai 80,7% (hlm. 5). Kriteria kegagalannya ketat, yaitu setiap perbedaan pada himpunan lima kode teratas (hlm. 4), sehingga angka itu menunjukkan ketidakstabilan keluaran, bukan persentase kode yang salah. Hanya satu aplikasi yang dapat diuji (hlm. 3).

### II.3.4 Sintesis dan Posisi Penelitian

Dua studi yang membedakan kategori kesalahan menunjukkan pola yang sama: pemeriksaan otomatis lebih baik pada kesalahan eksplisit dalam satu dokumen daripada pada kesalahan yang menuntut penilaian klinis. Pada Dietrich dan Stubbert (2026, hlm. 98), ketidaksesuaian temuan klinis memiliki *recall* terendah, dan pada Skrabic dkk. (2026, hlm. 4), kategori diagnostik dan pemeriksaan penunjang paling sulit.

Seluruh kategori yang diuji berada di dalam satu dokumen. Dietrich dan Stubbert (2026, hlm. 96–97) menguji lima kategori pada satu catatan pemulangan, antara lain ketidaksesuaian waktu kunjungan dan hasil pemeriksaan penunjang abnormal yang diabaikan atau dikontradiksi pada penilaian atau rencana. Ketidaksesuaian diagnosis atau kode diuji terhadap label klinisi (Du dkk., 2026) dan terhadap penelusuran rekam medis (Mwogosi & Mambile, 2026), bukan antara dua dokumen klinis dalam satu episode rawat inap. Perbedaan diagnosis antara catatan perkembangan harian dan resume medis, ketidaksesuaian temporal antardokumen, serta hasil pemeriksaan yang tidak ditindaklanjuti pada dokumen lain termasuk jenis yang direncanakan ditangani komponen AI/NLP dalam penelitian ini [SESUAIKAN DENGAN BAB I]. Jenis-jenis itu perlu didefinisikan dan dievaluasi terpisah, karena kinerja pada satu jenis tidak mewakili jenis lain.

Bukti tentang positif palsu (*false positive*) belum seragam. Hanya Dietrich dan Stubbert (2026, hlm. 95) menyertakan catatan tanpa kesalahan, sebanyak 100 catatan. Skrabic dkk. (2026, hlm. 6) tidak menyertakannya, dan Du dkk. (2026, hlm. 7, 12) menilai selisih terhadap label klinisi yang sendiri dapat mengandung derau, sehingga angka presisi ketiga studi tidak sebanding. Ketidakstabilan satu model klasifikasi kode terhadap akronim dan salah ketik (Jaganathan dkk., 2025, hlm. 4–5) menunjukkan bahwa ketahanan terhadap variasi penulisan, termasuk singkatan lokal, perlu diuji secara khusus, meskipun hasilnya belum tentu berlaku bagi LLM.

Di antara keenam studi, tidak ada yang melaporkan data dari Indonesia, membandingkan catatan perkembangan harian dengan ringkasan akhir dalam satu episode rawat inap, atau mengambil pedoman sesuai kasus sebagai dasar temuan. Karena itu, angka kinerja yang dilaporkan tidak dapat dipindahkan begitu saja ke dokumentasi rawat inap kebidanan dan anak di Indonesia, dan kinerja harus diukur ulang dengan menyertakan dokumen tanpa ketidaksesuaian agar positif palsu dapat dihitung.

---

## Daftar Pustaka (sementara)

> **[FORMAT AKHIR PERLU DIKONFIRMASI]** Entri di bawah mengikuti pola contoh pada templat proposal (nama, tahun, judul, jurnal, volume, nomor artikel atau halaman). Metadata diambil dari berkas PDF. DOI belum dicantumkan di naskah karena gaya sitasi belum ditetapkan, tetapi tersedia di Lampiran C.

Dietrich, N., & Stubbert, B. (2026). Automated auditing of emergency department documentation using large language models. *American Journal of Emergency Medicine, 104*, 95–101.

Du, W. (H.), Wang, G., Xu, J. (N.), & Vasarhelyi, M. A. (2026). Information systems auditing of psychiatric diagnoses using context-enriched QA-based language models. *Data Science and Management, 9*, 100177.

Hou, W.-h., Wang, X.-k., Wang, Y.-n., Wang, J.-q., & Xiao, F. (2024). Modelling long medical documents and code associations for explainable automatic ICD coding. *Expert Systems with Applications, 249*, 123519.

Jaganathan, G. S., Kahanda, I., & Kanewala, U. (2025). Metamorphic testing for robustness and fairness evaluation of LLM-based automated ICD coding applications. *Smart Health, 36*, 100564.

Mwogosi, A., & Mambile, C. (2026). Concordance of electronic health record data with ICD classification and evidence-based treatment guidelines: A systematic review and meta-analysis. *Health Policy and Technology, 15*, 101213.

Skrabic, R., Viculin, I., Boban, Z., Kumric, M., Vilovic, M., Vrdoljak, J., & Bozic, J. (2026). Large language models as second reviewers for medical errors in real-world internal medicine reports: A prospective comparative study of open- and closed-source models. *International Journal of Medical Informatics, 211*, 106316.

---

## Lampiran kerja (bukan bagian naskah)

### Lampiran A. Tabel verifikasi klaim ke halaman PDF

Setiap baris sudah dicocokkan otomatis ke teks halaman yang disebut (skrip pemeriksa di sesi kerja). `P` = halaman yang dikutip di naskah. Kutipan asli singkat dicantumkan agar Anda dapat memeriksa tanpa membaca ulang seluruh artikel.

| Sumber | Klaim di naskah | P | Kutipan asli (pendek) |
|---|---|---|---|
| Dietrich & Stubbert | 600 catatan; 500 dengan satu kesalahan sisipan; 100 tanpa kesalahan | 95–96 | "600 ED discharge notes … 500 notes with a single injected documentation error … 100 error-free reference notes" |
| Dietrich & Stubbert | Perintah sistem sama berisi definisi kategori dan kriteria | 97 | "All models received an identical system prompt that defined the five predefined documentation error categories" |
| Dietrich & Stubbert | Akurasi 93,2–94,2%; presisi 98,3–99,1%; spesifisitas 92,0–96,0% | 98 | "ranged from 93.2% to 94.2% across models"; "ranging from 98.3% to 99.1%"; "Specificity ranged from 92.0% to 96.0%" |
| Dietrich & Stubbert | F1 ≥0,96 untuk identitas/kunjungan dan obat/alergi; F1 0,75–0,84 untuk temuan klinis, terutama karena recall | 98 | "F1 scores ≥0.96"; "F1 scores ranging from 0.75 to 0.84 … driven primarily by reduced recall" |
| Dietrich & Stubbert | Satu kesalahan per catatan; catatan diturunkan dari elemen data terstruktur | 96 | "each note containing only one error"; "used to derive standardized ED documentation" |
| Dietrich & Stubbert | Kesalahan disisipkan, bukan alami; satu institusi | 100 | "systematically injected into discharge notes rather than occurring naturally"; "derived from a single institution" |
| Dietrich & Stubbert | Arah lanjutan: kerangka agen dengan pengambilan pedoman dan pemeriksaan lintas dokumen | 100 | "agentic auditing frameworks incorporating guideline retrieval and cross document consistency checks" |
| Skrabic dkk. | 102 laporan; 99 disisipkan, 3 sudah ada | 1–2 | "102 real-world Emergency Internal Medicine reports"; "99 (97.1%) were deliberately inserted" |
| Skrabic dkk. | Tanpa pengambilan referensi atau pemanggilan fungsi | 3 | "No tool-calling, retrieval, or function-calling features were enabled" |
| Skrabic dkk. | Lokasi benar 65,7–79,2%; dokter 48,0%; tiga dokter masing-masing sepertiga kasus | 4 | "72.5% (74/102"; "79.2% (80/101"; "65.7% (67/102"; "overall human detection rate of 48.0% (49/102"; "Three clinicians each reviewed one-third" |
| Skrabic dkk. | Diagnostik/pemeriksaan penunjang paling sulit; median 7 isu, maksimum 17 | 4 | "diagnostic/investigation-related omissions were the most difficult class"; "median = 7"; "up to 17 issues in a single report" |
| Skrabic dkk. | Risiko kelelahan terhadap peringatan | 5 | "raises the risk of alert fatigue" |
| Skrabic dkk. | Tanpa catatan bebas kesalahan; satu pusat | 6 | "we did not include error-free notes"; "the study was single-center" |
| Du dkk. | Reformulasi tanya jawab dan pengayaan konteks; klaim aplikasi validasi klaim asuransi | 1, 4 | "insurance claim validation" (abstrak, hlm. 1); bagian 3.3 (hlm. 4) |
| Du dkk. | 48.492 rekam dari 7.000 pasien; OCR untuk sumber PDF; satu klinik psikiatri | 3, 12 | "48,492 patient records from 7,000 unique patients"; "using OCR for PDF sources" (hlm. 3); "The dataset comes from a single psychiatric clinic" (hlm. 12) |
| Du dkk. | Deskripsi sepuluh kelompok kode, urutan tetap | 5 | "fixed-order inventory F0 → F9" |
| Du dkk. | Model BART; Llama 3.3 zero-shot | 5–6 | "implemented using a BART-based sequence-to-sequence model"; "evaluated in a zero-shot setting" |
| Du dkk. | Risiko rendah 36,99%; sedang 45,9%; tinggi 17,11%; acuan = diagnosis awal klinisi | 7 | "Low-risk cases (36.99%)"; "Medium-risk cases (45.9%)"; "High-risk cases (17.11%)"; "ground truth diagnostic codes were derived from clinicians' initial assessments" |
| Du dkk. | sum-F1 0,7417 (terbaik); BERT dengan penjelasan 0,7287 (Tabel 3); Llama 3.3 0,3785 | 8 | "emerged as the top-performing model"; "sum-F1-score of only 0.3785"; nilai 0.7287 dan 0.7417 pada Tabel 3 |
| Du dkk. | sum-F1 = ukuran F1 berbasis ROUGE rancangan penulis | 6 | "we introduced a multi-label recall-oriented understudy for gisting evaluation (ROUGE) metric" |
| Du dkk. | Diagnosis klinisi berderau, tidak stabil, dipengaruhi penagihan; satu klinik | 12 | "Clinician-entered diagnoses can be noisy, temporally unstable, and influenced by billing/documentation constraints" |
| Du dkk. | Tingkat risiko heuristik tanpa psikiater; penjelasan tidak dinilai klinisi | 13 | "tuned on a development split without psychiatrist co-design"; "we did not test explanation faithfulness" |
| Mwogosi & Mambile | 17 studi; spesifisitas/PPV sering >90%; sensitivitas rata-rata 64,5% (sebagian proksi); kode saja melebih-lebihkan kepatuhan; perlu pendekatan hibrida | 1 | "Seventeen validation studies"; "mean sensitivity of ICD-coded diagnoses was 64.5%"; "coding prevalence was used as a proxy for sensitivity"; "narrative documentation are necessary" |
| Mwogosi & Mambile | Seluruh studi dari negara berpenghasilan tinggi; belum ada studi LMIC | 4–5 | "all conducted in high-income countries" (hlm. 4); "in low- and middle-income countries" (hlm. 5) |
| Mwogosi & Mambile | Metastasis tulang 76,5% vs 89,2% | 10 | "76.5% of patients received appropriate bone-targeting agents"; "falsely inflated this to 89.2%" |
| Mwogosi & Mambile | Bias acuan penelusuran rekam medis | 11 | "copy-and-paste practices" |
| Hou dkk. | Klasifikasi teks multilabel; penyandi; perhatian per label | 1–2 | "label-wise attention mechanism provides the interpretability of prediction" (hlm. 1) |
| Hou dkk. | F1 makro 0,688; F1 mikro 0,727 (50 kode teratas); alat bantu pemberi kode; aturan kurang fleksibel; pemotongan 512 token menghilangkan informasi; 4.096 token | 2 | "macro-F1 and micro-F1 of 0.688 and 0.727"; "auxiliary tool to help coders"; "less flexible or portable"; "usually lead to information loss"; "up to 4,096 tokens" |
| Jaganathan dkk. | Hanya PLM-ICD yang dapat diuji | 3 | "we could only use PLM-ICD" |
| Jaganathan dkk. | 3.372 catatan uji; kegagalan 70–81%; kriteria `I_MR < 5` | 4 | "3372 clinical notes"; "ranging from 70% to 81%"; "an MR is failed if the I_MR < 5" |
| Jaganathan dkk. | Akronim 20 teratas 80,7% | 5 | "peak of 80.7%" |

### Lampiran B. Matriks catatan literatur (bahan untuk subbab II.8)

| Penulis, tahun | Data | Metode | Hasil utama | Celah terhadap penelitian ini |
|---|---|---|---|---|
| Dietrich & Stubbert, 2026 | 600 catatan pemulangan IGD (MIMIC-IV-ED), 500 bersisipan | 4 LLM, perintah sistem seragam, 5 kategori | Akurasi 93,2–94,2%; temuan klinis paling sulit | Kesalahan sisipan, satu dokumen, satu institusi, tanpa pengambilan pedoman, tanpa lintas dokumen |
| Skrabic dkk., 2026 | 102 laporan penyakit dalam IGD | 3 model penalaran vs 3 dokter | Lokasi benar 65,7–79,2% vs dokter 48,0% | Tanpa catatan bebas kesalahan (positif palsu tidak terukur); tanpa pengambilan referensi |
| Du dkk., 2026 | 48.492 rekam psikiatri, satu klinik | Reformulasi tanya jawab + pengayaan konteks statis | sum-F1 0,7417 | Acuan = diagnosis klinisi berderau; domain psikiatri; konteks statis |
| Mwogosi & Mambile, 2026 | 17 studi validasi, negara berpenghasilan tinggi | Tinjauan sistematis dan metaanalisis | Sensitivitas rata-rata kode 64,5%; PPV tinggi | Tentang akurasi kode, bukan audit lintas dokumen atau LLM |
| Hou dkk., 2024 | MIMIC-III | Clinical-Longformer + perhatian per label | F1 makro 0,688; F1 mikro 0,727 (50 kode) | Menetapkan kode dari dokumen, bukan memeriksa kode yang sudah ada |
| Jaganathan dkk., 2025 | 3.372 catatan uji MIMIC-III | Pengujian metamorfik pada PLM-ICD | Perbedaan 5 kode teratas pada 70–81% catatan | Satu model; mengukur stabilitas, bukan kebenaran |

### Lampiran C. Catatan peringatan dan penandaan

1. **Lebeña dkk. (2025) dikeluarkan dari naskah pada draf 2 untuk menghemat ± 0,4 halaman.** *Sumber Literatur Bab 2* menyebutnya "paling dekat dengan skenario CPPT→kode", tetapi setelah dibaca artikel itu memprediksi diagnosis berikutnya dari riwayat kode dan teks (hlm. 1), bukan memeriksa konsistensi catatan dengan kode. Angka yang pernah diverifikasi (P@5 72,34%; P@20 77,49%; peningkatan hingga 2%; 46% muat 512 token) dan frasa uji `L1`–`L8` dihapus dari `claims_II3.json`; riwayat git menyimpannya bila ingin dikembalikan. Studi pembanding yang lebih dekat untuk "kode vs catatan" adalah Du dkk. (2026) dan Mwogosi dan Mambile (2026), tetapi keduanya juga bukan studi LLM pada dokumen lintas hari.
2. **Arah penggantian akronim pada Jaganathan dkk. tidak jelas di artikelnya.** Definisi parameter menyebut "acronyms with their respective abbreviations" (hlm. 2), hasil menyebut "acronyms were replaced with abbreviated words" (hlm. 4), dan paragraf akronim (hlm. 5) menyebut kedua arah ("replacing phrases with acronyms" dan "acronyms … replaced with their respective words"). Naskah hanya menyebut "penggantian akronim" tanpa arah.
3. **Kriteria kegagalan Jaganathan dkk. ketat.** Satu kode berbeda pada himpunan lima kode teratas sudah dihitung gagal, sehingga 70–81% adalah angka ketidakstabilan, bukan akurasi. Naskah menyatakannya.
4. **Pernyataan "presisi tidak dapat dipindahkan ke populasi dengan proporsi ketidaksesuaian lebih rendah"** adalah penalaran penulis dari fakta bahwa 500 dari 600 catatan bersisipan (hlm. 95) dan sifat presisi yang bergantung pada prevalensi. Pernyataan itu bukan klaim Dietrich dan Stubbert. Sebagai pemeriksaan, dengan sensitivitas 0,946 dan spesifisitas 0,920 (model yang presisinya 0,983, hlm. 98), presisi hanya sekitar 0,57 bila ketidaksesuaian ada pada 10% dokumen (hitungan penulis dengan rumus presisi dan prevalensi 10% yang bersifat hipotetis). Angka hipotetis itu sengaja tidak dimasukkan ke naskah.
5. **Klaim ketiadaan pada paragraf penutup II.3.4** ("tidak ada yang melaporkan data dari Indonesia, …") dibatasi pada keenam studi ini. Dasarnya: keenam PDF dibaca penuh, dan kata "Indonesia" tidak muncul sama sekali di satu pun. Klaim bahwa tidak ada yang membandingkan catatan harian dengan ringkasan akhir atau memakai pengambilan pedoman bertumpu pada pembacaan penuh; untuk Skrabic dkk. dikuatkan oleh pernyataan eksplisit tanpa *retrieval* (hlm. 3).
6. **Satu PDF berada di `source/external/`** (Dietrich & Stubbert). Artikelnya tercantum di *Sumber Literatur Bab 2*, sehingga dipakai. Tidak ada sumber dari `source/external/` lain yang dipakai.
7. **Angka per kategori pada Skrabic dkk. tidak konsisten antarbagian** (misalnya jumlah kasus diagnostik 31, 36, dan 41 pada bagian berbeda). Naskah hanya memakai angka agregat dan pernyataan kualitatif tentang kategori tersulit.
8. **Istilah yang perlu diperiksa bentuk bakunya:** `ansambel` (untuk *ensemble*), `penyandi` (untuk *encoder*), `derau` (untuk *noise*), `metaanalisis`. Keempatnya belum diverifikasi ke KBBI/pedoman resmi dalam sesi ini [PERLU VERIFIKASI BENTUK BAKU].
9. **Penanda yang harus diselesaikan:** `[SESUAIKAN DENGAN BAB I]` pada II.3.4 (pembagian jalur AI/NLP perlu disamakan dengan rumusan final Bab I). Definisi LLM pada II.3.1 dipindahkan ke II.2 bila subbab itu sudah ditulis lebih dahulu.
10. **DOI artikel (dari berkas PDF):** Dietrich & Stubbert 10.1016/j.ajem.2026.03.007; Skrabic dkk. 10.1016/j.ijmedinf.2026.106316; Du dkk. 10.1016/j.dsm.2026.01.002; Mwogosi & Mambile 10.1016/j.hlpt.2026.101213; Lebeña dkk. 10.1016/j.imu.2025.101637; Jaganathan dkk. 10.1016/j.smhl.2025.100564; Hou dkk. 10.1016/j.eswa.2024.123519.
11. **Draf 4 (tanggapan atas tinjauan kualitas): II.3.4 ditulis ulang agar memuat peta jenis ketidaksesuaian.** Kalimat "seluruh kategori yang diuji berada di dalam satu dokumen" bersandar pada Dietrich & Stubbert (lima kategori pada satu catatan pemulangan, hlm. 96–97; klaim DC1–DC3 pada `claims_II3.json`) dan pada Du dkk. serta Mwogosi & Mambile (label klinisi dan penelusuran rekam medis, bukan antardokumen). **Koreksi penting:** kategori "kegagalan pemeriksaan penunjang" Dietrich & Stubbert (hasil abnormal yang diabaikan, diremehkan, atau dikontradiksi pada penilaian atau rencana) dan "ketidaksesuaian identitas/waktu kunjungan" memang sudah diuji, tetapi di dalam satu catatan, sehingga naskah tidak menyatakan bahwa jenis tersebut belum pernah diuji; yang belum diuji adalah versi antardokumennya. Skrabic dkk. menyebut empat kategori pada abstrak dan metode tetapi "lima kategori" pada hasil (hanya empat terdaftar), jadi kategorinya tidak dipakai untuk peta. Tiga detail kecil dikeluarkan demi ruang (OCR pada Du dkk.; ukuran 4.096 token pada Hou dkk.; kalimat "kategori diagnostik paling sulit" pada II.3.1 karena sudah ada di II.3.4); klaimnya tetap lolos pada `claims_II3.json`.
