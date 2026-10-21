# Bab II — Subbab II.5 (DRAFT 1)

> **Status:** draf kerja, belum ditinjau pembimbing. Hanya bagian "Naskah" dan "Daftar Pustaka (sementara)" yang masuk ke proposal. Bagian "Lampiran kerja" adalah alat bantu pemeriksaan dan tidak dihitung dalam batas 19 halaman.
>
> **Konvensi sitasi sementara:** penulis-tahun dengan nomor halaman (`hlm.`). Semua sumber adalah artikel Elsevier atau Cell Press bernomor artikel, sehingga `hlm.` = halaman berkas PDF. **Pada Yang dkk. (2026) halaman cetak "1" berada di halaman PDF 2** (halaman PDF 1 memuat abstrak grafis), jadi nomor cetak = halaman PDF − 1. Format akhir menunggu pedoman program studi.
>
> **Sumber:** delapan artikel di `source/` (Yang; Landolsi; Zhang; Jia; Li; Zeba; Sun; Waqas), semuanya dibaca dari PDF. Setiap angka dan klaim isi dicek otomatis ke teks halaman (Lampiran A). Tidak ada sumber dari `source/external/`. Tidak tersedia di repo: Tu dkk. (JMIR Med Inform 2026), Xiong dkk. 2024, dan Soroush dkk. 2024 (lihat Lampiran C).
>
> **Penanda yang perlu dijawab pengguna:** satu `[SESUAIKAN DENGAN BAB I]` pada subbab penutup.

---

## Naskah

## II.5 RAG, Graf Pengetahuan, Penjangkaran Bukti, dan Halusinasi

### II.5.1 RAG pada Teks Klinis

*Retrieval-augmented generation* (RAG) menyisipkan bukti yang diambil dari sumber luar ke dalam masukan LLM sebelum model membangkitkan jawaban. R. Yang dkk. (2026) menelaah 251 studi RAG di bidang medis dan menemukan bahwa aplikasinya terkonsentrasi pada tanya jawab, pembuatan laporan, peringkasan teks, dan ekstraksi informasi (hlm. 2). Dari 188 studi yang memakai *retrieval* padat, hanya 24 yang secara eksplisit memakai model *embedding* multibahasa; sisanya memakai model yang berpusat pada bahasa Inggris (hlm. 4). Penulisnya menilai RAG medis masih berada pada tahap awal dan memerlukan validasi klinis serta adaptasi lintas bahasa (hlm. 2). Landolsi dkk. (2026) menelaah 57 studi pada sepuluh bidang medis; hanya enam di antaranya yang memakai sumber nonbarat atau nonbahasa Inggris, dan hanya empat yang divalidasi lintas institusi (hlm. 6, 19).

Zhang dkk. (2026) memberi bukti yang paling dekat dengan catatan klinis sehari-hari. Mereka membandingkan enam strategi *retrieval* pada catatan keperawatan fasilitas perawatan lansia di Australia, dengan Llama 3.1 8B sebagai pembangkit dan indeks yang dibangun dari segmen catatan itu sendiri, untuk dua tugas ekstraksi entitas yang masing-masing diuji pada 208 rekaman (hlm. 1, 5). Tanpa *retrieval*, F1 jawaban ialah 0,702 untuk gejala agitasi pada demensia dan 0,722 untuk faktor risiko malnutrisi; dengan *dense reranking*, angkanya 0,946 dan 0,953 (hlm. 6). F1 jawaban itu dihitung dengan BERTScore, yaitu kemiripan semantik terhadap anotasi acuan (hlm. 3), bukan kecocokan label persis. Penulisnya membatasi kesimpulan pada dua tugas berbasis skema; ekstraksi relasi, penalaran temporal, dan tanya jawab terbuka tidak dievaluasi (hlm. 11). Jia dkk. (2026) melaporkan akurasi 82,98% pada soal ujian USMLE Step 1 untuk agen dengan *retrieval*, *reranking*, dan penjangkaran bukti, di atas 80,67% untuk GPT-4 (hlm. 2).

### II.5.2 Penjangkaran Bukti dan Pengecekan Keluaran

Waqas dkk. (2026) membedakan halusinasi faktual, *faithful* (tidak sesuai dengan masukan), logis, dan temporal (hlm. 4). Survei atas 90 publikasi itu mengutip RAGTruth bahwa halusinasi tetap terjadi ketika konteks ambigu atau *retrieval* gagal menemukan semua bukti yang relevan (hlm. 10), dan menyatakan bahwa bidang kesehatan membutuhkan laju positif palsu yang sangat rendah (hlm. 18). Sun dkk. (2025) menelaah 55 artikel, 15 di antaranya tentang halusinasi, dan menemukan bahwa mitigasi halusinasi sebagian besar dikaji pada tugas tanya jawab, dataset deteksi halusinasi langka, serta evaluasinya bergantung pada penilaian pakar tanpa kerangka baku (hlm. 15, 18).

Li dkk. (2026) mencontohkan penjangkaran bukti pada pendukung keputusan bedah tulang belakang. Pangkalan pengetahuannya memuat pedoman dan literatur yang masing-masing diberi ID, sumber, tahun, dan tingkat bukti (hlm. 3). Empat paragraf teratas disisipkan ke masukan model, keluaran berformat “rekomendasi + paragraf kutipan”, dan model diinstruksikan menjawab *“no clear conclusions available”* bila literatur tidak memberi jawaban pasti (hlm. 4). Lima ahli bedah menilai 200 kasus dengan rubrik 11 dimensi, termasuk ketepatan bukti yang dikutip (hlm. 1, 5). Namun yang dibandingkan ialah empat agen LLM dalam satu kerangka RAG di satu pusat, bukan RAG terhadap tanpa RAG (hlm. 9), dan artikelnya tidak menguraikan pemeriksaan kutipan otomatis.

Zeba dkk. (2026) menempuh cara lain: modul pemeriksa fakta tanpa LLM yang memeriksa keluaran LLM terhadap rekam medis sumber (hlm. 1). Ringkasan dan rekam medis dipecah menjadi proposisi atomik (hlm. 7), lalu setiap proposisi diberi vonis Didukung atau Tidak Didukung melalui pemeriksaan negasi, implikasi, konsistensi temporal, eksklusivitas bersama, kecocokan numerik, dan keberadaan (hlm. 6, 14). Pada 104 ringkasan yang diekstrak menjadi 3.786 proposisi dan divalidasi dokter, modul itu mencapai presisi 0,8904, *recall* 0,8234, dan F1 0,8556 (hlm. 1). Datanya berasal dari MIMIC-III, rekam medis unit perawatan intensif (hlm. 10), dan penulisnya menyatakan sistem kurang andal pada bidang yang kurang terwakili, termasuk gangguan metabolik anak, serta hanya memberi vonis biner tanpa usul perbaikan (hlm. 15).

### II.5.3 Representasi Pengetahuan Berbasis Graf

Graf pengetahuan (*knowledge graph*, KG) menyimpan pengetahuan sebagai entitas dan relasi. Syeda dan Reddy (2026) mensurvei integrasinya dengan LLM dalam tiga bentuk, yaitu KG yang memperkuat LLM, LLM yang membantu membangun KG, dan gabungan keduanya, serta mencatat GraphRAG dan HybridRAG sebagai RAG berbasis graf (hlm. 1). Mereka menilai penyelesaian KG oleh LLM di bidang kesehatan lebih berisiko sehingga memerlukan validasi pakar klinis (hlm. 18), dan menyatakan belum ada tolok ukur untuk seluruh alur KG–LLM (hlm. 27).

Dua studi primer memakai KG untuk fungsi yang berbeda. KG-ACE memverifikasi penalaran medis yang sudah dibangkitkan LLM dengan dua graf, satu untuk konsep baku dan satu untuk aturan klinis, termasuk urutan waktu, dan menerima revisi hanya bila skor kesesuaian membaik (Sun dkk., 2027, hlm. 1, 4). Dua dari empat tolok ukurnya sintetis atau semisintetis, tidak ada yang memuat catatan klinis nyata, dan cakupan graf yang kurang dapat meloloskan penalaran tanpa tantangan (hlm. 15). CTKGR membangun KG temporal dari rekam medis 3.214 pasien pneumonia di satu rumah sakit untuk memprediksi gejala dan merekomendasikan obat, dengan AUC 0,745 dan 0,798 (Y. Yang dkk., 2026, hlm. 1, 2); penulisnya mencatat cakupan graf yang terbatas (hlm. 8).

### II.5.4 Sintesis dan Celah

Manfaat *retrieval* baru ditunjukkan untuk ekstraksi pada catatan klinis, dan keterlacakan keluaran terhadap sumbernya baru didemonstrasikan pada contoh yang terbatas, sehingga ada lima celah bagi penelitian ini. Pertama, aplikasi RAG terkonsentrasi pada tanya jawab, pembuatan laporan, peringkasan, dan ekstraksi (R. Yang dkk., 2026, hlm. 2), dan bukti kinerja yang paling mencolok berasal dari soal ujian (Jia dkk., 2026, hlm. 2); di antara sumber yang dibaca, tidak ada yang menguji RAG untuk memeriksa kesesuaian antardokumen dalam satu episode rawat. Kedua, tidak ada sumber yang menguji teks klinis berbahasa Indonesia, dan *retrieval* umumnya memakai model berpusat pada bahasa Inggris (R. Yang dkk., 2026, hlm. 4; Landolsi dkk., 2026, hlm. 19). Ketiga, pemeriksaan keluaran terhadap sumber baru didemonstrasikan pada ringkasan LLM atas rekam medis berbahasa Inggris (Zeba dkk., 2026), sedangkan ketepatan kutipan pada Li dkk. (2026) dinilai ahli. Keempat, kontribusi *retrieval* dibandingkan dengan kondisi tanpa *retrieval* hanya pada dua tugas ekstraksi berbasis skema (Zhang dkk., 2026, hlm. 6, 11); pada audit, kontribusinya terhadap mutu temuan dan biaya positif palsunya belum diukur. Kelima, KG dipakai untuk memverifikasi penalaran pada soal medis (Sun dkk., 2027, hlm. 1, 15) dan memprediksi kejadian pada satu penyakit (Y. Yang dkk., 2026, hlm. 1, 2), bukan memeriksa kesesuaian antardokumen, dan manfaatnya tidak dibandingkan dengan *retrieval* tanpa graf. Karena itu, manfaat RAG pada audit dokumentasi rawat inap kebidanan dan anak perlu diuji terhadap pembanding yang ditetapkan sebelum eksperimen [SESUAIKAN DENGAN BAB I: rumusan pertanyaan dan ukuran keberhasilan; celah keempat hanya terjawab bila konfigurasi aturan + LLM tanpa *retrieval* ikut dijalankan, padahal Breakdown menjadikannya opsional]. Dalam penelitian ini, KG berkedudukan sebagai calon pendekatan pendukung, bukan komponen inti, karena manfaatnya untuk pemeriksaan antardokumen belum ditunjukkan, penyelesaian KG oleh LLM di bidang kesehatan memerlukan validasi pakar klinis (Syeda & Reddy, 2026, hlm. 18), dan cakupan graf yang kurang dapat membuat penalaran yang berisiko lolos tanpa ditandai (Sun dkk., 2027, hlm. 15). Pemakaian KG diputuskan melalui uji kelayakan, dan manfaatnya baru diklaim bila konfigurasi dengan graf telah dibandingkan dengan konfigurasi tanpa graf.

---

## Daftar Pustaka (sementara)

> **[FORMAT AKHIR PERLU DIKONFIRMASI]** Pola mengikuti contoh pada templat (gaya mirip APA). Metadata dari halaman pertama masing-masing PDF.

Jia, S., Bit, S., Jasodanand, V. H., Liu, Y., & Kolachalama, V. B. (2026). Agentic memory-augmented retrieval and evidence grounding for medical question-answering tasks. *International Journal of Medical Informatics, 212*, 106339.

Landolsi, M. Y., Fadhli, I., Boufaied, A., & Ben Romdhane, L. (2026). Recent trends of retrieval-augmented generation in healthcare: A systematic review. *Engineering Applications of Artificial Intelligence, 182*, 115912.

Li, Y., Lv, M., Cheng, L., Xie, Y., Gu, Q., He, H., Chen, Z., Fang, D., & Zhou, X. (2026). Explainable and evidence-linked recommendations for spine surgery via a retrieval-augmented LLM agent. *European Journal of Radiology, 197*, 112734.

Sun, Z., Yim, W.-W., Uzuner, Ö., Xia, F., & Yetisgen, M. (2025). A scoping review of natural language processing in addressing medically inaccurate information: Errors, misinformation, and hallucination. *Journal of Biomedical Informatics, 169*, 104866.

Sun, C., Fang, J., Ni, L., Yu, K., Lu, Y., & Lu, Y. (2027). KG-ACE: Knowledge Graph Alignment and Consistency Enhancement for medical reasoning with large language models. *Information Processing & Management, 64*, 105071. {{ed:[PERLU VERIFIKASI SUMBER: tahun mengikuti volume 64 (2027); terbit daring 29 Juli 2026]}}

Syeda, Q. A., & Reddy B., R. (2026). Knowledge graphs and large language models: Construction paradigms, integration approaches, and emerging applications. *Knowledge-Based Systems, 351*, 116601. {{ed:[PERLU VERIFIKASI SUMBER: bentuk nama penulis kedua pada berkas, "Ravinder Reddy B."]}}

Waqas, S. M., Umer, Z., Alim, A., Arham, M., Su'ud, M. M., Kazmi, S. J. A., & Alam, M. M. (2026). Hallucination detection, verification, and correction in generative AI: A comprehensive survey. *Natural Language Processing Journal, 16*, 100231.

{{ed:Yang, R., [PERLU VERIFIKASI SUMBER: penulis lain; daftar pada halaman judul PDF terpotong], & Liu, N.||cl:Yang, R., dkk.}} (2026). Retrieval-augmented generation in medicine: A scoping review of technical implementations, clinical applications, and ethical considerations. *Cell Reports Medicine, 7*, 102927.

Zeba, M., Al Mamun, A., Tithee, K. J., Sutradhar, D., Raiaan, M. A. K., Mukta, S., Mohamed, R. E., Islam, M. R., Sebastian, Y., Hussain, M., & Azam, S. (2026). Mitigating hallucinations in healthcare LLMs with granular fact-checking and domain-specific adaptation. *Expert Systems with Applications, 329*, 132966.

Zhang, H., Vithanage, D., Deng, C., & Yu, P. (2026). Optimising clinical information extraction: A comparative study of retrieval-augmented generation techniques in clinical notes. *Journal of Biomedical Informatics, 180*, 105053.

Yang, Y., Gao, B., Tan, C., Zhu, C., Yuan, P., Xie, P., Gu, Y., & Liu, H. (2026). CTKGR: Temporal knowledge graph enhanced prediction of in-hospital events for pneumonia patients using electronic health records. *Journal of Biomedical Informatics, 177*, 105007.

---

## Lampiran kerja (bukan bagian naskah)

### Lampiran A. Tabel verifikasi klaim ke halaman PDF

Setiap baris dicocokkan otomatis ke teks halaman yang disebut (`tools/verify_claims.py` dengan `tools/claims_II5.json`; hasil: 64 dari 64 cocok). Nomor halaman = halaman berkas PDF (pada Yang dkk., nomor cetak = halaman PDF − 1).

| Sumber | Klaim di naskah | Hlm. | Kutipan asli (pendek) |
|---|---|---|---|
| Yang dkk. | 251 studi RAG medis (244 + 7 manual) | 1, 3 | "review 251 studies"; "a total of 251 studies being analyzed" |
| Yang dkk. | Aplikasi terkonsentrasi pada tanya jawab, pembuatan laporan, peringkasan, ekstraksi informasi | 2 | "RAG applications are concentrated on question answering, report generation, text summarization, and information extraction" |
| Yang dkk. | Sumber: korpus biomedis 88, pedoman 67, EHR 33 studi | 3 | "biomedical scientific corpora constitute the main data source"; "Clinical guidelines follow closely, adopted in 67 studies"; "electronic health records (EHRs) (33 studies)" |
| Yang dkk. | 188 studi retrieval padat, hanya 24 memakai *embedding* multibahasa | 3, 4 | "188 studies (83.93%) adopting this approach"; "only 24 explicitly employed multilingual embed…"; "remaining studies relied on English-centric embedding models" |
| Yang dkk. | RAG medis masih tahap awal; perlu validasi klinis dan adaptasi lintas bahasa | 2 | "medical RAG remains at an early stage, requiring advances in clinical validation, cross-linguistic adaptation" |
| Landolsi dkk. | 57 studi pada sepuluh bidang | 6 | "57 papers across 10 medical fields" |
| Landolsi dkk. | 6 dari 57 memakai sumber nonbarat/nonbahasa Inggris; 4 divalidasi lintas institusi | 19 | "only 6 of the 57 studies draw on explicitly non-Western or non-English-language"; "only 4 studies explicitly validate across more than one institution" |
| Zhang dkk. | Catatan perawatan lansia di Australia; enam strategi retrieval | 1 | "Australian aged care facilities"; "we systematically compare six retrieval methods" |
| Zhang dkk. | Dua tugas, masing-masing 208 rekaman; Llama 3.1 8B; indeks dari segmen catatan | 1, 4, 5 | "agitation symptoms in dementia (n = 208) and identifying malnutrition risk factors (n = 208)"; "Llama3.1.8 B to generate responses"; "transform unstructured clinical notes into machine-readable knowledge representations" |
| Zhang dkk. | Tanpa RAG 0,702 dan 0,722; *dense reranking* 0,946 dan 0,953 | 6 | "Without RAG, the LLM achieved Answer F1 scores of 0.702 for agitation symptom extraction and 0.722 for malnutrition risk factor extraction"; "achieving F1 scores of 0.946 and 0.953, respectively" |
| Zhang dkk. | F1 jawaban memakai BERTScore | 3 | "BERTScore, which embeds both texts into contextualised vector representations" |
| Zhang dkk. | Galat: fabrikasi intrinsik terbanyak, lalu ekstrinsik, negatif palsu | 8, 9 | "Intrinsic fabrications occur when the model misrepresents information that is present in the source text"; "intrinsic fabrications were the most prevalent error type across all retrieval methods, followed by extrinsic fabrications, whereas false negatives occurred less frequently" |
| Zhang dkk. | Tidak mengevaluasi ekstraksi relasi, penalaran temporal, tanya jawab terbuka | 11 | "did not evaluate tasks involving relation extraction, temporal reasoning, or open-ended clinical question" |
| Jia dkk. | Akurasi 82,98% USMLE Step 1 vs 80,67% GPT-4; retrieval + reranking + penjangkaran bukti | 2 | "82.98% on the United States Medical Licensing Examination"; "surpassing GPT-4's 80.67%" |
| Waqas dkk. | Empat jenis halusinasi: faktual, faithful, logis, temporal | 4 | "factual hallucination, where an assertion is contradicted by world…"; "faithful hallucination, where an assertion is inconsistent with the…"; "temporal hallucination, where date information is inaccurate" |
| Waqas dkk. | 90 publikasi; tanpa penilaian risiko bias formal | 4 | "90 retained publications"; "No formal meta-analysis or risk-of-bias score" |
| Waqas dkk. | Halusinasi tetap terjadi bila konteks ambigu atau retrieval gagal (RAGTruth, sekunder) | 10 | "proved that the hallucinations still happen when the context is ambiguous or retrieval fails to identify all relevant evidence" |
| Waqas dkk. | Kesehatan memerlukan laju positif palsu sangat rendah | 18 | "very low false positives rates are needed" |
| Sun dkk. | 55 artikel, 15 tentang halusinasi | 4, 15 | "55 articles were included in our final review"; "Fifteen articles about hallucination detection and mitigation" |
| Sun dkk. | Mitigasi terutama pada tanya jawab; dataset deteksi halusinasi langka | 15 | "Current research on hallucination mitigation mainly focuses on QA tasks"; "there were few datasets and studies directly related to hallucination detection" |
| Sun dkk. | Evaluasi bergantung penilaian pakar; tidak ada kerangka baku | 18 | "Evaluation of hallucination often relies heavily on expert judgment"; "The absence of standardized, objective, and scalable evaluation frameworks" |
| Li dkk. | Pangkalan pengetahuan dengan ID, sumber, tahun, tingkat bukti; empat paragraf teratas | 4 | "unique literature ID, source (e.g., NASS guidelines), publication year, and evidence level"; "top-4 most relevant" |
| Li dkk. | Pembaruan tiap enam bulan | 3 | "Cron Job every six months" |
| Li dkk. | Keluaran "rekomendasi + paragraf kutipan"; jawaban "no clear conclusions available" | 4 | "recommendation + cited paragraph"; "no clear conclusions available" |
| Li dkk. | 200 kasus; lima ahli bedah; rubrik 11 dimensi termasuk ketepatan bukti kutipan | 1, 5 | "200 real-world spinal cases"; "Five spine surgeons independently evaluated model outputs using an 11-dimen…"; "Accuracy and precision of cited" |
| Li dkk. | Satu pusat; membandingkan agen LLM dalam satu kerangka RAG | 9 | "single-center context"; "relative performance of different LLM agents within a unified RAG framework" |
| Zeba dkk. | Modul pemeriksa fakta tanpa LLM terhadap rekam medis | 1 | "fact-checking module that operates independently of any LLM" |
| Zeba dkk. | Proposisi atomik; vonis Supported / Not Supported; enam pemeriksaan | 6, 7, 14 | "atomic propositions"; "Supported or Not Supported"; "negation, implication, temporal, mutual exclusiveness, numerical, and presence checks" |
| Zeba dkk. | 104 ringkasan, 3.786 proposisi; presisi 0,8904, *recall* 0,8234, F1 0,8556; divalidasi dokter | 1, 10 | "we sampled 104 summaries, extracted them into 3786 propositions"; "precision of 0.8904, a recall of 0.8234, and an F1-score of 0.8556"; "proposition-level annotation by clinicians" |
| Zeba dkk. | Tanpa negasi dan numerik presisi turun > 8% | 14 | "drop exceeding 8% in precision" |
| Zeba dkk. | MIMIC-III dari ICU; kurang andal pada bidang kurang terwakili (gangguan metabolik anak); vonis biner | 10, 15 | "collected from intensive care units"; "pediatric metabolic"; "binary gate" |

Pemeriksaan ketiadaan (bukan pencocokan frasa): pencarian `indonesia|malay|bahasa` pada teks kedelapan PDF hanya menemukan satu kecocokan, yaitu "Malaysia" pada afiliasi penulis Waqas dkk.

### Lampiran B. Matriks catatan literatur (bahan untuk subbab II.8)

| Penulis, tahun | Data | Metode | Hasil utama | Celah terhadap penelitian ini |
|---|---|---|---|---|
| Yang dkk., 2026 | 251 studi RAG medis | *Scoping review* (4 basis data) | Terkonsentrasi pada QA, laporan, peringkasan, ekstraksi; 24 dari 188 studi retrieval padat memakai *embedding* multibahasa; masih tahap awal | Bukan tentang audit; tidak ada bahasa Indonesia |
| Landolsi dkk., 2026 | 57 studi, 10 bidang | Tinjauan sistematis | 6 dari 57 memakai sumber nonbarat/nonbahasa Inggris; 4 validasi lintas institusi; evaluasi tidak seragam | Persentase arsitektur tidak konsisten (lihat Lampiran C); bukan audit |
| Zhang dkk., 2026 | Catatan perawatan lansia (Australia), 2 tugas × 208 rekaman | Perbandingan 6 strategi retrieval, Llama 3.1 8B, ANOVA ukuran berulang | Tanpa RAG 0,702/0,722; *dense reranking* 0,946/0,953 | Dua tugas ekstraksi berbasis skema; tanpa penalaran temporal; bahasa Inggris |
| Jia dkk., 2026 | 5 tolok ukur QA medis (USMLE dll.) | Agen LLM dengan retrieval, reranking, memori | 82,98% USMLE Step 1 vs GPT-4 80,67% | Soal ujian, bukan dokumentasi |
| Li dkk., 2026 | 200 kasus bedah tulang belakang (satu pusat) | RAG dengan kutipan terikat ID; 4 agen LLM; lima penilai ahli | Gemini 2.5 Flash tertinggi (49,25 ± 2,88) | Tanpa pembanding tanpa-RAG; kutipan dinilai manusia |
| Zeba dkk., 2026 | MIMIC-III; 104 ringkasan, 3.786 proposisi | Pemeriksa fakta tanpa LLM, enam pemeriksaan logika | Presisi 0,8904, *recall* 0,8234, F1 0,8556 | Bahasa Inggris, ICU; vonis biner; kurang andal pada bidang kurang terwakili |
| Sun dkk., 2025 | 55 artikel (15 halusinasi) | *Scoping review* PRISMA-ScR | Mitigasi halusinasi terutama pada QA; dataset dan standar evaluasi langka | Bukan audit dokumentasi |
| Waqas dkk., 2026 | 90 publikasi | Survei (tanpa penilaian risiko bias) | Taksonomi empat jenis halusinasi; kesehatan perlu positif palsu rendah | Survei lintas domain; kajian multibahasa terbatas |

### Lampiran C. Catatan peringatan dan penandaan

1. **PDF yang disebut daftar atau Breakdown tetapi tidak ada di repo, sehingga tidak dipakai:** Tu, Shi, & Wang (JMIR Med Inform 2026, etika RAG di keperawatan), Xiong dkk. 2024 (RAG meningkatkan akurasi QA medis; rujukan Breakdown bagian 15), Soroush dkk. 2024 dan Ben Abacha dkk. 2025 (rujukan Breakdown bagian 15). Pernyataan Breakdown tentang "RAG meningkatkan akurasi pada tanya-jawab medis" belum dapat diperiksa ke sumber aslinya.
2. **Tidak ada sumber yang menguji RAG untuk audit atau pemeriksaan konsistensi antardokumen.** Pernyataan ini dibatasi pada delapan sumber yang dibaca. Zhang dkk. adalah yang paling dekat (RAG pada catatan klinis harian), tetapi tugasnya ekstraksi entitas berbasis skema.
3. **Zhang dkk., baseline "tanpa retrieval" tidak sepenuhnya jelas.** Artikel menyebut baseline memakai "prompting alone, without any retrieved context" (hlm. 5, 6), tanpa merinci apakah catatan utuh tetap diberikan. Naskah memakai angka 0,702/0,722 sebagai "tanpa retrieval" persis seperti artikel. F1 jawaban memakai BERTScore (kemiripan semantik), bukan kecocokan label.
4. **Landolsi dkk. memuat angka yang tidak konsisten, jadi klaim "sebagian besar memakai arsitektur dasar" dikeluarkan dari naskah.** Abstrak menyebut sebagian besar implementasi memakai arsitektur dasar, tetapi hlm. 13 melaporkan 35,41% studi memakai arsitektur dasar dan 18,75% modular, dengan penyebut yang tidak cocok dengan 57 studi. Naskah hanya memakai jumlah (6 dari 57; 4 studi).
5. **Yang dkk. memuat penyebut persentase yang bervariasi** (184/229, 188 = 83,93%, 100 = 41,15% dari jumlah berbeda) padahal total yang dianalisis 251. Naskah memakai jumlah studi, bukan persentase. Daftar penulis lengkap Yang dkk. terpotong pada halaman judul PDF; daftar pustaka memuat penanda `[PERLU VERIFIKASI SUMBER]`.
6. **Jia dkk. adalah tolok ukur soal ujian (USMLE dkk.)**; angka 80,67% untuk GPT-4 dilaporkan penulisnya sendiri dan tidak diperiksa ke sumber aslinya. Pemakaiannya di naskah dibatasi pada menunjukkan jenis bukti kinerja RAG.
7. **Waqas dkk. mengutip RAGTruth (Niu dkk., 2024)** untuk halusinasi yang tetap terjadi pada RAG; ini sekunder. Pernyataan "laju positif palsu sangat rendah" adalah sikap penulis survei (hlm. 18), bukan hasil empiris. Survei hanya menyertakan artikel berbahasa Inggris (hlm. 3).
8. **Li dkk.:** rubrik "Search Relevance" (ketepatan bukti kutipan) dinilai lima ahli bedah; artikel tidak menguraikan pemeriksaan kutipan otomatis, sehingga naskah menyatakannya sebagai tidak diuraikan, bukan sebagai tidak ada. Pernyataan di pendahuluannya tentang halusinasi 28,3% dan peningkatan galat 12% pada bahasa nonbahasa Inggris dikutip dari studi lain dan tidak dipakai.
9. **Zeba dkk.:** tabel perbandingan akurasi dengan Claude-2/DOSSIER dan lainnya (hlm. 14) tidak dipakai karena tidak jelas apakah tugas dan data sebanding. Evaluasi manusia bergantung pada dua dokter (hlm. 15).
10. **Titik hubung yang tidak diklaim.** Rancangan Breakdown (sumber tervalidasi dan berversi, kutipan bukti dicek otomatis ke sumber, temuan tanpa bukti valid tidak ditampilkan) paralel dengan pangkalan berversi dan penanda "no clear conclusions available" pada Li dkk. serta pemeriksa terpisah pada Zeba dkk., tetapi kesamaan itu tidak dinyatakan di naskah karena menyangkut rancangan yang belum tertulis di Bab III.
11. **Istilah yang perlu diverifikasi bentuk bakunya:** `penjangkaran`, `fabrikasi`, `positif palsu`/`negatif palsu`, `proposisi atomik`, `pembangkit` [PERLU VERIFIKASI BENTUK BAKU]. `retrieval`, `embedding`, `reranking`, `recall`, `dense reranking`, dan `faithful` ditulis miring sebagai istilah asing yang belum baku; `dataset` tidak dimiringkan mengikuti pemakaian di `RULES.md`.
12. **Penanda `[SESUAIKAN DENGAN BAB I]`** pada kalimat penutup II.5.3 harus disamakan dengan rumusan pertanyaan dan ukuran keberhasilan Bab I.
13. **Kalimat yang dikeluarkan pada draf 3 demi ruang** (klaimnya tetap lolos pada `claims_II5.json` dan dapat dikembalikan): sumber pengetahuan RAG tersering (Yang dkk., hlm. 3); galat tersering pada Zhang dkk. (fabrikasi intrinsik, hlm. 8, 9); pembaruan pangkalan Li dkk. tiap enam bulan (hlm. 4); penurunan presisi Zeba dkk. tanpa pemeriksaan negasi dan numerik (hlm. 14).

### Lampiran D. Sumber graf pengetahuan (draf 5; sub-subbab II.5.3)

Ketiga sumber ada di `source/` dan tercantum pada `Sumber Literatur Bab 2.pdf` (Kelompok 5, "Representasi Pengetahuan", berstatus Eksploratif), jadi tidak melanggar aturan sumber pengguna. Dua sumber lain pada kelompok itu (Gaudet-Blavignac dkk., JMIR 2026; Mohanty dkk., bab buku 2027) tidak ada di repo dan tidak dipakai. Semua klaim dicek ke halaman PDF (`claims_II5.json`, KG1–KG17; semua lolos).

| Sumber | Klaim di naskah | Hlm. | Kutipan asli (pendek) |
|---|---|---|---|
| Syeda & Reddy | Survei; tiga bentuk integrasi KG–LLM; GraphRAG dan HybridRAG sebagai RAG berbasis graf | 1 | "KG enhanced LLMs, 2) LLMs-augmented KGs and 3) Synergized LLMs+KGs"; "GraphRAG based on graph-based retrieval-augmented generation" |
| Syeda & Reddy | Penyelesaian KG kesehatan lebih berisiko; perlu validasi pakar klinis | 18 | "KG completion for healthcare is riskier than general domains"; "requires clinical expert validation of LLM-generated completions" |
| Syeda & Reddy | Belum ada tolok ukur untuk seluruh alur KG–LLM | 27 | "There is no unified benchmark to evaluate the whole KG-LLM pipeline" |
| Sun dkk. (KG-ACE) | Kerangka pascapembangkitan untuk memverifikasi dan merevisi penalaran medis LLM; dua graf (konsep baku; aturan klinis); revisi diterima hanya bila skor kesesuaian membaik | 1 | "a post-generation framework for verifying and revising medical reasoning produced by LLMs"; "separates standardized medical concepts in the Ontology Knowledge Graph from clinical rules in the Consistency Knowledge Graph"; "accepts a revision only when the recomputed alignment score improves by a specified margin" |
| Sun dkk. (KG-ACE) | Aturan klinis mencakup interaksi obat, kontraindikasi, relasi sebab, eksklusi timbal balik, dan urutan waktu | 4 | "drug interactions, contraindications, causal relations, mutual exclusions, and temporal orderings" |
| Sun dkk. (KG-ACE) | Empat tolok ukur; dua sintetis atau semisintetis; tidak ada catatan klinis nyata; cakupan graf kurang dapat meloloskan penalaran | 1, 15 | "MedQA, MedMCQA, GenMedGPT-5k, and DDXPlus"; "two of the four evaluation datasets (GenMedGPT-5k and DDXPlus) are synthetic or semi-synthetic, and none contains real unstructured clinical notes"; "constraint edges may be absent, causing the framework to pass potentially unsafe reasoning unchallenged" |
| Y. Yang dkk. (CTKGR) | KG temporal dari EHR; 3.214 pasien pneumonia, satu rumah sakit tersier di Beijing; AUC 0,745 (gejala) dan 0,798 (obat) | 1, 2 | "constructed a temporal knowledge graph (TKG) by systematically extracting clinical information"; "AUC of 0.745 for symptom prediction and 0.798 for medication recommendation"; "3,214 patients diagnosed with community-acquired pneumonia admitted to the respiratory department of a tertiary hospital in Beijing" |
| Y. Yang dkk. (CTKGR) | Cakupan graf terbatas | 8 | "the knowledge graph constructed may lack comprehensive coverage" |

Catatan peringatan:

1. **Kedudukan KG diputuskan pengguna pada 21 Oktober 2026: calon pendekatan pendukung yang dipastikan melalui uji kelayakan** (opsi "c"; opsi lain: komponen yang manfaatnya diuji, atau pendukung RAG tanpa klaim peningkatan). Alasannya: fokus penelitian tetap pada aturan + AI/NLP berbasis RAG sesuai Breakdown, dan beban eksperimen tidak bertambah. Kalimat penutup II.5.4 menuliskan kedudukan ini beserta tiga alasan yang dapat dipertahankan saat sidang ("mengapa bukan KG?"); kedua rujukannya (Syeda & Reddy hlm. 18; KG-ACE hlm. 15) sudah lolos pada `claims_II5.json`. Bila pembimbing meminta KG menjadi kontribusi, kalimat itu harus diganti dan konfigurasi dengan/tanpa graf masuk rancangan eksperimen Bab I/III.
2. **Tidak ada satu pun dari ketiga sumber yang menguji dokumentasi klinis Indonesia atau kesesuaian antardokumen.** KG-ACE menguji soal medis berbahasa Inggris; CTKGR memprediksi kejadian pada satu penyakit; Syeda & Reddy adalah survei lintas bidang. Pencarian `indonesia|bahasa|malay` pada ketiga teks PDF tidak menemukan kecocokan; klaim ketiadaan pada II.8.2 tetap dibatasi pada "sumber yang dibaca".
3. **KG-ACE: tahun.** Volume 64 bertahun 2027, tetapi artikel tersedia daring 29 Juli 2026 (diterima 20 Juli 2026). Naskah memakai 2027 mengikuti volume [PERLU VERIFIKASI SUMBER bila prodi mengikuti tahun daring].
4. **Syeda & Reddy: nama penulis kedua.** Berkas menulis "Ravinder Reddy B․"; judul berjalan memakai "R.R. B․". Daftar pustaka memakai "Reddy B., R." [PERLU VERIFIKASI SUMBER: bentuk nama].
5. **Bentrok nama penulis pertama.** Dua sumber II.5 berpenulis pertama "Yang" dan bertahun 2026 (RAG dalam kedokteran; CTKGR). Naskah memakai "R. Yang dkk." dan "Y. Yang dkk." (aturan APA untuk nama belakang kembar).
6. **Survei bersifat sekunder.** Pernyataan Syeda & Reddy tentang risiko penyelesaian KG kesehatan dan ketiadaan tolok ukur adalah penilaian penulis survei, bukan hasil uji.
7. **Pembatasan klaim.** KG-ACE dan CTKGR tidak menunjukkan bahwa KG meningkatkan audit dokumentasi; naskah tidak menyiratkannya. KG-ACE menyebut dirinya "bounded verification aid" (hlm. 15).
8. **Tiga detail kecil dikeluarkan demi ruang** pada draf 5: kalimat Jia dkk. diringkas; teks II.6 dipadatkan; paragraf Du dkk. pada II.3.2 dipadatkan (klaim tetap lolos pada berkas klaim masing-masing).
