# Indeks Sumber Literatur

Dibuat 23 Oktober 2026. Mengelompokkan seluruh PDF di `source/` dan `source/external/` ke folder tema, supaya referensi mudah dicari tanpa membuka berkas satu per satu.

- **`source/<tema>/`**: 46 PDF yang disebut di `Sumber Literatur Bab 2.pdf`. Nomor dan urutan tema mengikuti heading di PDF itu (tema 10-12 berasal dari tab "Kerangka Pencarian Literatur").
- **`source/external/<tema>/`**: 27 PDF temuan teman capstone. Temanya berbeda karena isinya tidak ada di `Sumber Literatur Bab 2.pdf`. Menurut `CONTEXT_TRANSFER.md`, berkas di sini hanya dipakai bila identik dengan artikel yang tercantum di daftar atau di Breakdown bagian 15; selebihnya perlu persetujuan Anda.
- **Nama berkas tidak diubah** (`1-s2.0-<ID>-main.pdf` tetap dipakai) supaya peta ID di `CONTEXT_TRANSFER.md` dan kamus `PDFS` di `tools/verify_claims.py` tetap bisa ditelusuri.
- Kolom **Hal** = jumlah halaman PDF. Tanda **†** = tahun tidak tertera di teks berkas; isi dari pengetahuan umum, cek sebelum dikutip.
- Judul dibaca dari metadata PDF. Tahun dan nama jurnal untuk `source/` mengikuti daftar Anda dan header halaman 1 tiap artikel.

## Daftar isi

| Folder | Tema | Jumlah |
| --- | --- | --- |
| `source/01_NLP_dan_LLM_Dokumentasi_Klinis/` | NLP dan LLM untuk Dokumentasi Klinis (gambaran umum) | 4 |
| `source/02_Audit_dan_Deteksi_Ketidaksesuaian_Dokumentasi/` | Deteksi Ketidaksesuaian dan Audit Dokumentasi Klinis Otomatis | 3 |
| `source/03_Pengodean_ICD_dan_Ekstraksi_Informasi/` | LLM untuk Pengodean ICD dan Ekstraksi Informasi Klinis | 3 |
| `source/04_Resume_Medis_dan_Ringkasan_Pulang/` | Resume Medis dan Ringkasan Pulang dengan LLM | 4 |
| `source/05_RAG_di_Ranah_Klinis/` | Retrieval-Augmented Generation (RAG) di Ranah Klinis | 5 |
| `source/06_Halusinasi_Verifikasi_dan_Konsistensi_Temporal/` | Keterbatasan AI/NLP: Halusinasi, Verifikasi Bukti, dan Konsistensi Temporal | 5 |
| `source/07_Alert_Fatigue_dan_Peringatan_Non-Interruptive/` | Alert Fatigue dan Desain Peringatan Non-Interruptive | 4 |
| `source/08_Deidentifikasi_Privasi_dan_Singkatan_Klinis/` | De-identifikasi, Privasi, dan Normalisasi Singkatan Klinis | 5 |
| `source/09_Hibrida_Rule-Based_dan_AI/` | Sistem Hibrida Rule-Based + AI | 2 |
| `source/10_Representasi_Pengetahuan_Graf/` | Representasi Pengetahuan: Knowledge Graph (kelompok 5, eksploratif) | 3 |
| `source/11_Metodologi_Evaluasi_NLP_Klinis/` | Metodologi Evaluasi Sistem NLP Klinis (kelompok 6) | 2 |
| `source/12_Konteks_Indonesia_JKN_INA-CBG/` | Konteks Indonesia: JKN, INA-CBG, Upcoding, RSIA (kelompok 7) | 6 |
| `source/external/01_Konteks_Indonesia_Regulasi_dan_Klaim/` | Konteks Indonesia: Regulasi, Rekam Medis, dan Klaim Pending | 4 |
| `source/external/02_Audit_dan_Pengodean_Klinis_Berbantuan_AI/` | Audit dan Pengodean Klinis Berbantuan AI | 3 |
| `source/external/03_Alert_Fatigue_dan_Peringatan/` | Alert Fatigue dan Desain Peringatan | 3 |
| `source/external/04_Reliance_Penjelasan_dan_Interaksi_Manusia-AI/` | Reliance, Penjelasan AI, dan Interaksi Manusia-AI | 6 |
| `source/external/05_Provenance_dan_Keterlacakan/` | Provenance dan Keterlacakan | 3 |
| `source/external/06_Metodologi_Desain_dan_Evaluasi_Usability/` | Metodologi Desain dan Evaluasi Usability | 4 |
| `source/external/07_Pemodelan_Sistem_dan_Penalaran_Formal/` | Pemodelan Sistem dan Penalaran Formal | 2 |
| `source/external/08_Analisis_Statis_dan_Pelacakan_Temuan/` | Analisis Statis dan Pelacakan Temuan antar Versi | 2 |

## A. source/ (sesuai Sumber Literatur Bab 2.pdf)

### 01. NLP dan LLM untuk Dokumentasi Klinis (gambaran umum)

Folder: `source/01_NLP_dan_LLM_Dokumentasi_Klinis/`. Definisi dan taksonomi tugas NLP klinis (ekstraksi informasi, tanya-jawab, ringkasan). Daftar mengaitkannya dengan RQ1.

| Sitasi | Judul | Terbit | Hal | Berkas |
| --- | --- | --- | --- | --- |
| Kumar dkk. (2026) | Natural Language Processing in Healthcare: From Unstructured Data to Clinical Intelligence | Intelligent Systems with Applications 31 | 30 | [S2667305326000724](01_NLP_dan_LLM_Dokumentasi_Klinis/1-s2.0-S2667305326000724-main.pdf) |
| Woo dkk. (2026) | The use of large language models in clinical documentation: A scoping review | International Journal of Nursing Studies 176 | 14 | [S0020748925003323](01_NLP_dan_LLM_Dokumentasi_Klinis/1-s2.0-S0020748925003323-main.pdf) |
| Elvas dkk. (2025) | Natural language processing in medical text processing: A scoping literature review | International Journal of Medical Informatics 204 | 9 | [S1386505625002667](01_NLP_dan_LLM_Dokumentasi_Klinis/1-s2.0-S1386505625002667-main.pdf) |
| Luo dkk. (2024) | Pre-trained language models in medicine: A survey | Artificial Intelligence in Medicine 154 | 43 | [S0933365724001465](01_NLP_dan_LLM_Dokumentasi_Klinis/1-s2.0-S0933365724001465-main.pdf) |

Tercantum di daftar tetapi belum ada di repo: Kayira dkk. (JMIR AI 2026).

### 02. Deteksi Ketidaksesuaian dan Audit Dokumentasi Klinis Otomatis

Folder: `source/02_Audit_dan_Deteksi_Ketidaksesuaian_Dokumentasi/`. Audit dokumentasi sebelum klaim, LLM sebagai pemeriksa kedua, kesesuaian kode terhadap catatan. Daftar mengaitkannya dengan RQ1 dan RQ3.

| Sitasi | Judul | Terbit | Hal | Berkas |
| --- | --- | --- | --- | --- |
| Skrabic dkk. (2026) | Large language models as second reviewers for medical errors in real-world internal medicine reports: a prospective comparative study of open- and closed-source models | International Journal of Medical Informatics 211 | 6 | [S1386505626000560](02_Audit_dan_Deteksi_Ketidaksesuaian_Dokumentasi/1-s2.0-S1386505626000560-main.pdf) |
| Du dkk. (2026) | Information systems auditing of psychiatric diagnoses using context-enriched QA-based language models | Data Science and Management 9 | 15 | [S266676492600007X](02_Audit_dan_Deteksi_Ketidaksesuaian_Dokumentasi/1-s2.0-S266676492600007X-main.pdf) |
| Mwogosi & Mambile (2026) | Concordance of electronic health record data with ICD classification and evidence-based treatment guidelines: A systematic review and meta-analysis | Health Policy and Technology 15 | 13 | [S2211883726000614](02_Audit_dan_Deteksi_Ketidaksesuaian_Dokumentasi/1-s2.0-S2211883726000614-main.pdf) |

Tercantum di daftar tetapi belum ada di repo: Kim, Lee, Yoon (JMIR Med Inform 2026, radiologi). Dietrich & Stubbert (2026) ada di source/external/02_....

### 03. LLM untuk Pengodean ICD dan Ekstraksi Informasi Klinis

Folder: `source/03_Pengodean_ICD_dan_Ekstraksi_Informasi/`. Pengodean ICD otomatis, dokumentasi perkembangan pasien menurut standar ICD, ekstraksi informasi klinis.

| Sitasi | Judul | Terbit | Hal | Berkas |
| --- | --- | --- | --- | --- |
| Jaganathan dkk. (2025) | Metamorphic Testing for Robustness and Fairness Evaluation of LLM-based Automated ICD Coding Applications | Smart Health 36 | 7 | [S235264832500025X](03_Pengodean_ICD_dan_Ekstraksi_Informasi/1-s2.0-S235264832500025X-main.pdf) |
| Lebeña dkk. (2025) | Large language models aided patient progression documentation according to the ICD standard | Informatics in Medicine Unlocked 55 | 10 | [S2352914825000255](03_Pengodean_ICD_dan_Ekstraksi_Informasi/1-s2.0-S2352914825000255-main.pdf) |
| Hou dkk. (2024) | Modelling long medical documents and code associations for explainable automatic ICD coding | Expert Systems with Applications 249 | 12 | [S0957417424003841](03_Pengodean_ICD_dan_Ekstraksi_Informasi/1-s2.0-S0957417424003841-main.pdf) |

Tercantum di daftar tetapi belum ada di repo: Seo, Kim, Kim (JMIR 2026, kelayakan klaim obat kanker).

### 04. Resume Medis dan Ringkasan Pulang dengan LLM

Folder: `source/04_Resume_Medis_dan_Ringkasan_Pulang/`. Pembuatan dan evaluasi ringkasan pulang oleh LLM. Berkas Kleebayoon & Wiwanitkit adalah korespondensi 1 halaman atas Schwieger dkk.

| Sitasi | Judul | Terbit | Hal | Berkas |
| --- | --- | --- | --- | --- |
| Grazhdanski dkk. (2025), SynthMedic | SynthMedic: Utilizing large language models for synthetic discharge summary generation, correction and validation | Journal of Biomedical Informatics 170 | 13 | [S1532046425001352](04_Resume_Medis_dan_Ringkasan_Pulang/1-s2.0-S1532046425001352-main.pdf) |
| Mehri dkk. (2026) | Assessing the quality of AI-generated and physician-written discharge summaries: evaluation of an EHR-integrated tool in a Dutch academic hospital | eBioMedicine | 11 | [S2352396426001295](04_Resume_Medis_dan_Ringkasan_Pulang/1-s2.0-S2352396426001295-main.pdf) |
| Schwieger dkk. (2024) | Large language models can support generation of standardized discharge summaries – A retrospective study utilizing ChatGPT-4 and electronic health records | International Journal of Medical Informatics 192 | 10 | [S1386505624003174](04_Resume_Medis_dan_Ringkasan_Pulang/1-s2.0-S1386505624003174-main.pdf) |
| Kleebayoon & Wiwanitkit (2025) | Correspondence on “Large language models can support generation of standardized discharge summaries − A retrospective study utilizing ChatGPT-4 and electronic health records” | International Journal of Medical Informatics 195 | 1 | [S1386505624004192](04_Resume_Medis_dan_Ringkasan_Pulang/1-s2.0-S1386505624004192-main.pdf) |

Tercantum di daftar tetapi belum ada di repo: Tung, Gill, Chong (JMIR 2024).

### 05. Retrieval-Augmented Generation (RAG) di Ranah Klinis

Folder: `source/05_RAG_di_Ranah_Klinis/`. RAG untuk dokumen dan pedoman klinis, penjangkaran bukti, rekomendasi yang tertaut ke sumber. Daftar mengaitkannya dengan RQ2 dan RQ4.

| Sitasi | Judul | Terbit | Hal | Berkas |
| --- | --- | --- | --- | --- |
| Landolsi dkk. (2026) | Recent trends of retrieval-augmented generation in healthcare: A systematic review | Engineering Applications of Artificial Intelligence 182 | 30 | [S0952197626021962](05_RAG_di_Ranah_Klinis/1-s2.0-S0952197626021962-main.pdf) |
| R. Yang dkk. (2026), RAG in medicine | Retrieval-augmented generation in medicine: A scoping review of technical implementations, clinical applications, and ethical considerations | Cell Reports Medicine | 12 | [S2666379126003447](05_RAG_di_Ranah_Klinis/1-s2.0-S2666379126003447-main.pdf) |
| Zhang dkk. (2026) | Optimising clinical information extraction: a comparative study of retrieval-augmented generation techniques in clinical notes | Journal of Biomedical Informatics 180 | 13 | [S1532046426000778](05_RAG_di_Ranah_Klinis/1-s2.0-S1532046426000778-main.pdf) |
| Jia dkk. (2026) | Agentic memory-augmented retrieval and evidence grounding for medical question-answering tasks | International Journal of Medical Informatics 212 | 9 | [S1386505626000791](05_RAG_di_Ranah_Klinis/1-s2.0-S1386505626000791-main.pdf) |
| Li dkk. (2026) | Explainable and evidence-linked recommendations for spine surgery via a retrieval-augmented LLM agent | European Journal of Radiology 197 | 11 | [S0720048X26000823](05_RAG_di_Ranah_Klinis/1-s2.0-S0720048X26000823-main.pdf) |

Tercantum di daftar tetapi belum ada di repo: Tu, Shi, Wang (JMIR Med Inform 2026, etika RAG).

### 06. Keterbatasan AI/NLP: Halusinasi, Verifikasi Bukti, dan Konsistensi Temporal

Folder: `source/06_Halusinasi_Verifikasi_dan_Konsistensi_Temporal/`. Halusinasi LLM, pengecekan fakta, penalaran temporal pada catatan klinis, praproses teks naratif. Daftar mengaitkannya dengan RQ4.

| Sitasi | Judul | Terbit | Hal | Berkas |
| --- | --- | --- | --- | --- |
| Zeba dkk. (2026) | Mitigating hallucinations in healthcare LLMs with granular fact-checking and domain-specific adaptation | Expert Systems with Applications 329 | 19 | [S0957417426018786](06_Halusinasi_Verifikasi_dan_Konsistensi_Temporal/1-s2.0-S0957417426018786-main.pdf) |
| Sun dkk. (2025), halusinasi | A scoping review of natural language processing in addressing medically inaccurate information: Errors, misinformation, and hallucination | Journal of Biomedical Informatics 169 | 22 | [S1532046425000954](06_Halusinasi_Verifikasi_dan_Konsistensi_Temporal/1-s2.0-S1532046425000954-main.pdf) |
| Waqas dkk. (2026) | Hallucination detection, verification, and correction in generative AI: A comprehensive survey | Natural Language Processing Journal 16 | 20 | [S2949719126000361](06_Halusinasi_Verifikasi_dan_Konsistensi_Temporal/1-s2.0-S2949719126000361-main.pdf) |
| Olex & McInnes (2021) | Review of Temporal Reasoning in the Clinical Domain for Timeline Extraction: Where we are and where we need to be | Journal of Biomedical Informatics 118 | 16 | [S1532046421001131](06_Halusinasi_Verifikasi_dan_Konsistensi_Temporal/1-s2.0-S1532046421001131-main.pdf) |
| Jafarpour dkk. (2025) | Preprocessing narrative texts in electronic medical records to identify hospital adverse events: A scoping review | Artificial Intelligence in Medicine 170 | 19 | [S0933365725002167](06_Halusinasi_Verifikasi_dan_Konsistensi_Temporal/1-s2.0-S0933365725002167-main.pdf) |

Tercantum di daftar tetapi belum ada di repo: -.

### 07. Alert Fatigue dan Desain Peringatan Non-Interruptive

Folder: `source/07_Alert_Fatigue_dan_Peringatan_Non-Interruptive/`. Peringatan yang diabaikan bila berulang atau memblokir, serta contoh desain peringatan yang tidak memotong alur kerja.

| Sitasi | Judul | Terbit | Hal | Berkas |
| --- | --- | --- | --- | --- |
| Sangal dkk. (2023) | Clinical Decision Support: Moving Beyond Interruptive “Pop-up” Alerts | Mayo Clinic Proceedings | 5 | [S0025619623002549](07_Alert_Fatigue_dan_Peringatan_Non-Interruptive/1-s2.0-S0025619623002549-main.pdf) |
| Cánovas-Segura dkk. (2023) | Meaningful time-related aspects of alerts in Clinical Decision Support Systems. A unified framework | Journal of Biomedical Informatics 143 | 10 | [S1532046423001181](07_Alert_Fatigue_dan_Peringatan_Non-Interruptive/1-s2.0-S1532046423001181-main.pdf) |
| Boccio dkk. (2026) | Impact of a non-interruptive electronic health record-based clinical decision support tool on HEART score documentation compliance in the emergency department | International Journal of Medical Informatics 222 | 7 | [S1386505626004752](07_Alert_Fatigue_dan_Peringatan_Non-Interruptive/1-s2.0-S1386505626004752-main.pdf) |
| Page dkk. (2017) | A systematic review of the effectiveness of interruptive medication prescribing alerts in hospital CPOE systems to change prescriber behavior and improve patient safety | International Journal of Medical Informatics 105 | 9 | [S1386505617301600](07_Alert_Fatigue_dan_Peringatan_Non-Interruptive/1-s2.0-S1386505617301600-main.pdf) |

Tercantum di daftar tetapi belum ada di repo: Newton dkk. (JMIR 2026); Gani dkk. (JMIR 2025).

### 08. De-identifikasi, Privasi, dan Normalisasi Singkatan Klinis

Folder: `source/08_Deidentifikasi_Privasi_dan_Singkatan_Klinis/`. De-identifikasi sebelum data dikirim ke layanan AI eksternal; disambiguasi singkatan dan normalisasi konsep klinis.

| Sitasi | Judul | Terbit | Hal | Berkas |
| --- | --- | --- | --- | --- |
| Faustini dkk. (2026) | De-identification of clinical data: A systematic review of free text, image and tabular data approaches | International Journal of Medical Informatics 208 | 14 | [S1386505625004423](08_Deidentifikasi_Privasi_dan_Singkatan_Klinis/1-s2.0-S1386505625004423-main.pdf) |
| Azzam dkk. (2026) | Agentic LLM for anonymizing healthcare data with contextual awareness | Knowledge-Based Systems 343 | 21 | [S0950705126007604](08_Deidentifikasi_Privasi_dan_Singkatan_Klinis/1-s2.0-S0950705126007604-main.pdf) |
| Tchouka dkk. (2024) | Differentially private de-identifying textual medical document is compliant with challenging NLP analyses: Example of privacy-preserving ICD-10 code association | Intelligent Systems with Applications 23 | 15 | [S2667305324000905](08_Deidentifikasi_Privasi_dan_Singkatan_Klinis/1-s2.0-S2667305324000905-main.pdf) |
| Wei dkk. (2026) | Selection-based prompting with synthesized candidates unlocks high-performance clinical abbreviation disambiguation via open-source LLMs | Journal of Biomedical Informatics 181 | 11 | [S1532046426001097](08_Deidentifikasi_Privasi_dan_Singkatan_Klinis/1-s2.0-S1532046426001097-main.pdf) |
| Chen dkk. (2026) | A comprehensive survey on medical concept normalization: Datasets, techniques, applications, and future directions | Journal of Biomedical Informatics 178 | 26 | [S1532046426000298](08_Deidentifikasi_Privasi_dan_Singkatan_Klinis/1-s2.0-S1532046426000298-main.pdf) |

Tercantum di daftar tetapi belum ada di repo: -.

### 09. Sistem Hibrida Rule-Based + AI

Folder: `source/09_Hibrida_Rule-Based_dan_AI/`. Gabungan aturan eksplisit dan AI/NLP pada sistem pendukung keputusan dan audit klaim.

| Sitasi | Judul | Terbit | Hal | Berkas |
| --- | --- | --- | --- | --- |
| Domingues (2026) | A hybrid decision support system using rule-based and AI methods: the OnCATs knowledge-based framework | International Journal of Medical Informatics 206 | 11 | [S1386505625003612](09_Hibrida_Rule-Based_dan_AI/1-s2.0-S1386505625003612-main.pdf) |
| Ijadi Maghsoodi dkk. (2026) | Artificial intelligence for decision-making in healthcare: A critical review of decision-maker-governed hybrid systems across clinical, operational, and policy settings | Health Policy and Technology 15 | 12 | [S2211883726001401](09_Hibrida_Rule-Based_dan_AI/1-s2.0-S2211883726001401-main.pdf) |

Tercantum di daftar tetapi belum ada di repo: Maleki dkk. (J Health Organ Manag 2026; deteksi deduksi klaim asuransi dengan ML + sistem pakar).

### 10. Representasi Pengetahuan: Knowledge Graph (kelompok 5, eksploratif)

Folder: `source/10_Representasi_Pengetahuan_Graf/`. Knowledge graph dan LLM, graph-based retrieval, konsistensi penalaran lewat graf, graf temporal dari EHR.

| Sitasi | Judul | Terbit | Hal | Berkas |
| --- | --- | --- | --- | --- |
| Sun dkk. (2027), KG-ACE | KG-ACE: Knowledge Graph Alignment and Consistency Enhancement for medical reasoning with large language models | Information Processing & Management 64 | 19 | [S0306457326004619](10_Representasi_Pengetahuan_Graf/1-s2.0-S0306457326004619-main.pdf) |
| Syeda & Reddy (2026) | Knowledge graphs and large language models: Construction paradigms, integration approaches, and emerging applications | Knowledge-Based Systems 351 | 31 | [S0950705126013274](10_Representasi_Pengetahuan_Graf/1-s2.0-S0950705126013274-main.pdf) |
| Y. Yang dkk. (2026), CTKGR | CTKGR: temporal knowledge graph enhanced prediction of in-hospital events for pneumonia patients using electronic health records | Journal of Biomedical Informatics 177 | 9 | [S1532046426000316](10_Representasi_Pengetahuan_Graf/1-s2.0-S1532046426000316-main.pdf) |

Tercantum di daftar tetapi belum ada di repo: Gaudet-Blavignac dkk. (JMIR 2026); Mohanty dkk. (bab buku 2027).

### 11. Metodologi Evaluasi Sistem NLP Klinis (kelompok 6)

Folder: `source/11_Metodologi_Evaluasi_NLP_Klinis/`. Pedoman anotasi, label tenaga ahli, skema pengembangan dan validasi algoritma.

| Sitasi | Judul | Terbit | Hal | Berkas |
| --- | --- | --- | --- | --- |
| Becker dkk. (2025) | Extending CARDIO:DE: Additional annotation guidelines and evaluation of NLP approaches for clinical applications | International Journal of Medical Informatics 203 | 7 | [S1386505625002266](11_Metodologi_Evaluasi_NLP_Klinis/1-s2.0-S1386505625002266-main.pdf) |
| van Koevorden dkk. (2026) | Validating large language model-assisted data extraction from clinical notes | ESMO Real World Data and Digital Oncology | 9 | [S2949820126000378](11_Metodologi_Evaluasi_NLP_Klinis/1-s2.0-S2949820126000378-main.pdf) |

Tercantum di daftar tetapi belum ada di repo: Singh dkk. (JMIR Med Inform 2025).

### 12. Konteks Indonesia: JKN, INA-CBG, Upcoding, RSIA (kelompok 7)

Folder: `source/12_Konteks_Indonesia_JKN_INA-CBG/`. Sistem JKN, pembayaran INA-CBG, upcoding, kualitas layanan di rumah sakit ibu dan anak.

| Sitasi | Judul | Terbit | Hal | Berkas |
| --- | --- | --- | --- | --- |
| Susilo dkk. (2025) | Can Indonesia achieve universal health coverage? Organisational and financing challenges in implementing the national health insurance system | SSM - Health Systems 5 | 9 | [S294985622500090X](12_Konteks_Indonesia_JKN_INA-CBG/1-s2.0-S294985622500090X-main.pdf) |
| Septiono dkk. (2026) | Eclampsia and preeclampsia with tropical seasonality: Evidence from Indonesia's national health insurance registry (2015–2022) | Pregnancy Hypertension 44 | 7 | [S2210778926000723](12_Konteks_Indonesia_JKN_INA-CBG/1-s2.0-S2210778926000723-main.pdf) |
| Sambodo dkk. (2023) | Effects of performance-based capitation payment on the use of public primary health care services in Indonesia | Social Science & Medicine 327 | 10 | [S0277953623002782](12_Konteks_Indonesia_JKN_INA-CBG/1-s2.0-S0277953623002782-main.pdf) |
| Nilasari & Soelistijanto (2026) | A Preliminary Study on Mitigating Upcoding in Indonesia's National Health Insurance using Multi-Agent Multi-Armed Bandits | Procedia Computer Science 289 | 8 | [S1877050926029406](12_Konteks_Indonesia_JKN_INA-CBG/1-s2.0-S1877050926029406-main.pdf) |
| Rachmawaty dkk. (2021) | Evaluation of health care quality among insured patients in Indonesian mother & child hospital: A secondary data analysis | Gaceta Sanitaria 35(S2) | 6 | [S0213911121003071](12_Konteks_Indonesia_JKN_INA-CBG/1-s2.0-S0213911121003071-main.pdf) |
| Barsasella dkk. (2021) | Predicting length of stay and mortality among hospitalized patients with type 2 diabetes mellitus and hypertension | International Journal of Medical Informatics 154 | 11 | [S1386505621001957](12_Konteks_Indonesia_JKN_INA-CBG/1-s2.0-S1386505621001957-main.pdf) |

Tercantum di daftar tetapi belum ada di repo: Lathifah dkk. (Enfermería Clínica 2020); Fahlevi dkk. (J Account Organ Change 2021).

## B. source/external/ (temuan teman capstone)

### 01. Konteks Indonesia: Regulasi, Rekam Medis, dan Klaim Pending

Folder: `source/external/01_Konteks_Indonesia_Regulasi_dan_Klaim/`. Peraturan INA-CBG dan rekam medis, literatur lokal tentang klaim pending dan rekam medis elektronik.

| Sitasi | Judul | Terbit | Hal | Berkas | Catatan |
| --- | --- | --- | --- | --- | --- |
| Permenkes No. 26 (2021) | Peraturan Menteri Kesehatan RI Nomor 26 Tahun 2021 tentang Pedoman Indonesian Case Base Groups (INA-CBG) dalam Pelaksanaan Jaminan Kesehatan | Peraturan Menteri Kesehatan RI | 56 | [2021permenkes026.pdf](external/01_Konteks_Indonesia_Regulasi_dan_Klaim/2021permenkes026.pdf) |  |
| Permenkes No. 24 (2022) | Peraturan Menteri Kesehatan RI Nomor 24 Tahun 2022 tentang Rekam Medis | Peraturan Menteri Kesehatan RI | 20 | [2022permenkes024.pdf](external/01_Konteks_Indonesia_Regulasi_dan_Klaim/2022permenkes024.pdf) |  |
| Simbolon & Gani (2023) | Faktor-Faktor yang Mempengaruhi Terjadinya Pending Klaim Rawat Inap: Literatur Review | Jurnal Keperawatan dan Kesehatan 14(1) | 7 | [faktor-faktor yang mempengaruhi pen...](external/01_Konteks_Indonesia_Regulasi_dan_Klaim/faktor-faktor%20yang%20mempengaruhi%20pending%20rawat%20inap.pdf) | Rujukan Breakdown bagian 15 |
| Murcittowati dkk. (2023) | Pengaturan Pengaktifan Kembali Rekam Medis Elektronik pada Rumah Sakit X Kota Denpasar | Jurnal Kesehatan Vokasional 8(4) | 11 | [Pengaturan Pengaktifan Kembali Reka...](external/01_Konteks_Indonesia_Regulasi_dan_Klaim/Pengaturan%20Pengaktifan%20Kembali%20Rekam%20Medis%20Elektronik%20pada%20Rumah%20Sakit%20X%20Kota%20Denpasar.pdf) |  |

### 02. Audit dan Pengodean Klinis Berbantuan AI

Folder: `source/external/02_Audit_dan_Pengodean_Klinis_Berbantuan_AI/`. Audit dokumentasi UGD dengan LLM, pengodean klinis kolaboratif manusia-AI, dan pedoman praktik query pengodean.

| Sitasi | Judul | Terbit | Hal | Berkas | Catatan |
| --- | --- | --- | --- | --- | --- |
| Dietrich & Stubbert (2026) | Automated auditing of emergency department documentation using large language models | American Journal of Emergency Medicine 104 | 7 | [Automated auditing of emergency dep...](external/02_Audit_dan_Pengodean_Klinis_Berbantuan_AI/Automated%20auditing%20of%20emergency%20department%20documentation%20using.pdf) | Tercantum di Sumber Literatur Bab 2.pdf (tema 02) |
| Gao dkk. (2024) | Optimising the paradigms of human AI collaborative clinical coding | npj Digital Medicine 7:368 | 15 | [Optimising the paradigms of human A...](external/02_Audit_dan_Pengodean_Klinis_Berbantuan_AI/Optimising%20the%20paradigms%20of%20human%20AI%20collaborative%20clinical%20coding.pdf) |  |
| ACDIS & AHIMA (2022) | Guidelines for Achieving a Compliant Query Practice (2022 Update) | Pedoman praktik (2022 Update) | 27 | [Guidelines for Achieving a Complian...](external/02_Audit_dan_Pengodean_Klinis_Berbantuan_AI/Guidelines%20for%20Achieving%20a%20Compliant%20Query%20Practice.pdf) |  |

### 03. Alert Fatigue dan Desain Peringatan

Folder: `source/external/03_Alert_Fatigue_dan_Peringatan/`. Kelelahan peringatan pada CDS dan alternatif selain peringatan interruptive.

| Sitasi | Judul | Terbit | Hal | Berkas | Catatan |
| --- | --- | --- | --- | --- | --- |
| Ancker dkk. (2017) | Effects of workload, work complexity, and repeated alerts on alert fatigue in a clinical decision support system | BMC Medical Informatics and Decision Making 17:36 | 9 | [Effects of workload work complexity...](external/03_Alert_Fatigue_dan_Peringatan/Effects%20of%20workload%20work%20complexity%20and%20repeated%20alerts%20on%20alert%20fatigue%20in%20a%20clinical%20decision%20support%20system.pdf) | Rujukan Breakdown bagian 15 |
| Sangal dkk. (2023) | Clinical Decision Support: Moving Beyond Interruptive "Pop-up" Alerts | Mayo Clinic Proceedings | 5 | [Clinical Decision Support Moving Be...](external/03_Alert_Fatigue_dan_Peringatan/Clinical%20Decision%20Support%20Moving%20Beyond.pdf) | Judul sama dengan source/07 (berkas berbeda, md5 tidak sama) |
| Cánovas-Segura dkk. (2023) | Meaningful time-related aspects of alerts in Clinical Decision Support Systems. A unified framework | Journal of Biomedical Informatics 143 | 10 | [Meaningful time-related aspects of ...](external/03_Alert_Fatigue_dan_Peringatan/Meaningful%20time-related%20aspects%20of%20alerts%20in%20Clinical%20Decision%20Support.pdf) | Judul sama dengan source/07 (berkas berbeda, md5 tidak sama) |

### 04. Reliance, Penjelasan AI, dan Interaksi Manusia-AI

Folder: `source/external/04_Reliance_Penjelasan_dan_Interaksi_Manusia-AI/`. Automation bias, overreliance, efek penjelasan AI, kebutuhan klinisi, dan pedoman interaksi manusia-AI.

| Sitasi | Judul | Terbit | Hal | Berkas | Catatan |
| --- | --- | --- | --- | --- | --- |
| Goddard dkk. (2012) | Automation bias: a systematic review of frequency, effect mediators, and mitigators | JAMIA 19:121-127 | 7 | [Automation bias a systematic review...](external/04_Reliance_Penjelasan_dan_Interaksi_Manusia-AI/Automation%20bias%20a%20systematic%20review%20of%20frequency%20effect%20mediators%20and%20mitigators.pdf) |  |
| Tonekaboni dkk. (2019) | What Clinicians Want: Contextualizing Explainable Machine Learning for Clinical End Use | Machine Learning for Healthcare (PMLR) | 21 | [What Clinicians Want Contextualizin...](external/04_Reliance_Penjelasan_dan_Interaksi_Manusia-AI/What%20Clinicians%20Want%20Contextualizing%20Explainable%20Machin.pdf) |  |
| Amershi dkk. (2019) | Guidelines for Human-AI Interaction | CHI 2019 | 13 | [Guidelines for Human-AI Interaction...](external/04_Reliance_Penjelasan_dan_Interaksi_Manusia-AI/Guidelines%20for%20Human-AI%20Interaction.pdf) |  |
| Bansal dkk. (2021) | Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance | CHI '21 | 16 | [Does the Whole Exceed its Parts The...](external/04_Reliance_Penjelasan_dan_Interaksi_Manusia-AI/Does%20the%20Whole%20Exceed%20its%20Parts%20The%20Efect%20of%20AI%20Explanations.pdf) |  |
| Vasconcelos dkk. (2023) | Explanations Can Reduce Overreliance on AI Systems During Decision-Making | PACM HCI 7(CSCW1), Art. 129 | 38 | [Explanations Can Reduce Overrelianc...](external/04_Reliance_Penjelasan_dan_Interaksi_Manusia-AI/Explanations%20Can%20Reduce%20Overreliance%20on%20AI%20Systems%20During.pdf) |  |
| Kim dkk. (2025) | Fostering Appropriate Reliance on Large Language Models: The Role of Explanations, Sources, and Inconsistencies | CHI '25 | 19 | [Fostering Appropriate Reliance on L...](external/04_Reliance_Penjelasan_dan_Interaksi_Manusia-AI/Fostering%20Appropriate%20Reliance%20on%20Large%20Language%20Models.pdf) |  |

### 05. Provenance dan Keterlacakan

Folder: `source/external/05_Provenance_dan_Keterlacakan/`. Standar provenance (W3C PROV-DM, HL7 FHIR) dan studi antarmuka provenance tingkat kalimat pada ringkasan rekam medis.

| Sitasi | Judul | Terbit | Hal | Berkas | Catatan |
| --- | --- | --- | --- | --- | --- |
| W3C (2013), PROV-DM | PROV-DM: The PROV Data Model — W3C Recommendation 30 April 2013 | W3C Recommendation, 30 April 2013 | 6 | [W3C PROV-DM Specification REC-prov-...](external/05_Provenance_dan_Keterlacakan/W3C%20PROV-DM%20Specification%20REC-prov-dm-20130430.pdf) |  |
| HL7 (FHIR R4 v4.0.1), Provenance | HL7 FHIR R4 - Resource Provenance (6.3) | HL7 FHIR Release 4 | 10 | [hl7_fhir_r4_provenance.pdf](external/05_Provenance_dan_Keterlacakan/hl7_fhir_r4_provenance.pdf) |  |
| Parambath dkk. (2026) | Sentence-Level Provenance for AI Medical Record Summarization in a Click-to-Inspect Interface: Formative Usability Evaluation | JMIR Human Factors 13:e95644 | 10 | [Sentence-Level Provenance for AI Me...](external/05_Provenance_dan_Keterlacakan/Sentence-Level%20Provenance%20for%20AI%20Medical%20Record.pdf) |  |

### 06. Metodologi Desain dan Evaluasi Usability

Folder: `source/external/06_Metodologi_Desain_dan_Evaluasi_Usability/`. Design Science Research, SUS, heuristik usability Nielsen, dan ISO 9241-210 (human-centred design).

| Sitasi | Judul | Terbit | Hal | Berkas | Catatan |
| --- | --- | --- | --- | --- | --- |
| Peffers dkk. (2007/2008) | A Design Science Research Methodology for Information Systems Research | Journal of Management Information Systems 24(3):45-77 | 34 | [Unlocked A Design Science Research ...](external/06_Metodologi_Desain_dan_Evaluasi_Usability/Unlocked%20A%20Design%20Science%20Research%20Methodology%20for%20Information%20Systems%20Research.pdf) | Terbitan Winter 2007-8 |
| Brooke (1996†) | SUS - A quick and dirty usability scale | Tidak tertera di teks berkas | 7 | [SUS - A quick and dirty usability s...](external/06_Metodologi_Desain_dan_Evaluasi_Usability/SUS%20-%20A%20quick%20and%20dirty%20usability%20scale.pdf) | † tahun diisi dari pengetahuan umum, bukan dari berkas; cek sebelum dikutip |
| Nielsen (1994) | Enhancing the Explanatory Power of Usability Heuristics | CHI '94 | 7 | [Enhancing the Explanatory Power of ...](external/06_Metodologi_Desain_dan_Evaluasi_Usability/Enhancing%20the%20Explanatory%20Power%20of%20Usability%20Heuristics.pd.pdf) |  |
| ISO 9241-210 (2019) | ISO 9241-210:2019 Ergonomics of human-system interaction - Part 210: Human-centred design for interactive systems | Standar internasional, edisi ke-2 | 13 | [ISO-9241-210-2019.pdf](external/06_Metodologi_Desain_dan_Evaluasi_Usability/ISO-9241-210-2019.pdf) |  |

### 07. Pemodelan Sistem dan Penalaran Formal

Folder: `source/external/07_Pemodelan_Sistem_dan_Penalaran_Formal/`. Statecharts (pemodelan perilaku sistem) dan truth maintenance system (revisi keyakinan saat ada kontradiksi).

| Sitasi | Judul | Terbit | Hal | Berkas | Catatan |
| --- | --- | --- | --- | --- | --- |
| Harel (1987) | Statecharts: A Visual Formalism for Complex Systems | Science of Computer Programming 8:231-274 | 44 | [Statecharts a visual formalism for ...](external/07_Pemodelan_Sistem_dan_Penalaran_Formal/Statecharts%20a%20visual%20formalism%20for%20complex%20systems.pdf) |  |
| Doyle (1979) | A Truth Maintenance System | Artificial Intelligence 12:231-272 | 42 | [A truth maintenance system.pdf](external/07_Pemodelan_Sistem_dan_Penalaran_Formal/A%20truth%20maintenance%20system.pdf) | PDF pindai dengan teks OCR berkualitas rendah; pencarian kata bisa meleset |

### 08. Analisis Statis dan Pelacakan Temuan antar Versi

Folder: `source/external/08_Analisis_Statis_dan_Pelacakan_Temuan/`. Platform analisis program (Tricorder) dan pelacakan peringatan cacat antar versi (analogi untuk pelacakan temuan audit).

| Sitasi | Judul | Terbit | Hal | Berkas | Catatan |
| --- | --- | --- | --- | --- | --- |
| Sadowski dkk. (2015†) | Tricorder: Building a Program Analysis Ecosystem | Tidak tertera di teks berkas | 11 | [Tricorder Building a Program Analys...](external/08_Analisis_Statis_dan_Pelacakan_Temuan/Tricorder%20Building%20a%20Program%20Analysis%20Ecosystem.pdf) | † tahun diisi dari pengetahuan umum, bukan dari berkas; cek sebelum dikutip |
| Spacco dkk. (2006) | Tracking Defect Warnings Across Versions | MSR '06 | 4 | [Tracking Defect Warnings Across Ver...](external/08_Analisis_Statis_dan_Pelacakan_Temuan/Tracking%20Defect%20Warnings%20Across%20Versions.pdf) |  |

## C. Cari menurut penulis

| Sitasi | Lokasi |
| --- | --- |
| ACDIS & AHIMA (2022) | `source/external/02_Audit_dan_Pengodean_Klinis_Berbantuan_AI/` |
| Amershi dkk. (2019) | `source/external/04_Reliance_Penjelasan_dan_Interaksi_Manusia-AI/` |
| Ancker dkk. (2017) | `source/external/03_Alert_Fatigue_dan_Peringatan/` |
| Azzam dkk. (2026) | `source/08_Deidentifikasi_Privasi_dan_Singkatan_Klinis/` |
| Bansal dkk. (2021) | `source/external/04_Reliance_Penjelasan_dan_Interaksi_Manusia-AI/` |
| Barsasella dkk. (2021) | `source/12_Konteks_Indonesia_JKN_INA-CBG/` |
| Becker dkk. (2025) | `source/11_Metodologi_Evaluasi_NLP_Klinis/` |
| Boccio dkk. (2026) | `source/07_Alert_Fatigue_dan_Peringatan_Non-Interruptive/` |
| Brooke (1996†) | `source/external/06_Metodologi_Desain_dan_Evaluasi_Usability/` |
| Cánovas-Segura dkk. (2023) | `source/07_Alert_Fatigue_dan_Peringatan_Non-Interruptive/` |
| Cánovas-Segura dkk. (2023) | `source/external/03_Alert_Fatigue_dan_Peringatan/` |
| Chen dkk. (2026) | `source/08_Deidentifikasi_Privasi_dan_Singkatan_Klinis/` |
| Dietrich & Stubbert (2026) | `source/external/02_Audit_dan_Pengodean_Klinis_Berbantuan_AI/` |
| Domingues (2026) | `source/09_Hibrida_Rule-Based_dan_AI/` |
| Doyle (1979) | `source/external/07_Pemodelan_Sistem_dan_Penalaran_Formal/` |
| Du dkk. (2026) | `source/02_Audit_dan_Deteksi_Ketidaksesuaian_Dokumentasi/` |
| Elvas dkk. (2025) | `source/01_NLP_dan_LLM_Dokumentasi_Klinis/` |
| Faustini dkk. (2026) | `source/08_Deidentifikasi_Privasi_dan_Singkatan_Klinis/` |
| Gao dkk. (2024) | `source/external/02_Audit_dan_Pengodean_Klinis_Berbantuan_AI/` |
| Goddard dkk. (2012) | `source/external/04_Reliance_Penjelasan_dan_Interaksi_Manusia-AI/` |
| Grazhdanski dkk. (2025), SynthMedic | `source/04_Resume_Medis_dan_Ringkasan_Pulang/` |
| Harel (1987) | `source/external/07_Pemodelan_Sistem_dan_Penalaran_Formal/` |
| HL7 (FHIR R4 v4.0.1), Provenance | `source/external/05_Provenance_dan_Keterlacakan/` |
| Hou dkk. (2024) | `source/03_Pengodean_ICD_dan_Ekstraksi_Informasi/` |
| Ijadi Maghsoodi dkk. (2026) | `source/09_Hibrida_Rule-Based_dan_AI/` |
| ISO 9241-210 (2019) | `source/external/06_Metodologi_Desain_dan_Evaluasi_Usability/` |
| Jafarpour dkk. (2025) | `source/06_Halusinasi_Verifikasi_dan_Konsistensi_Temporal/` |
| Jaganathan dkk. (2025) | `source/03_Pengodean_ICD_dan_Ekstraksi_Informasi/` |
| Jia dkk. (2026) | `source/05_RAG_di_Ranah_Klinis/` |
| Kim dkk. (2025) | `source/external/04_Reliance_Penjelasan_dan_Interaksi_Manusia-AI/` |
| Kleebayoon & Wiwanitkit (2025) | `source/04_Resume_Medis_dan_Ringkasan_Pulang/` |
| Kumar dkk. (2026) | `source/01_NLP_dan_LLM_Dokumentasi_Klinis/` |
| Landolsi dkk. (2026) | `source/05_RAG_di_Ranah_Klinis/` |
| Lebeña dkk. (2025) | `source/03_Pengodean_ICD_dan_Ekstraksi_Informasi/` |
| Li dkk. (2026) | `source/05_RAG_di_Ranah_Klinis/` |
| Luo dkk. (2024) | `source/01_NLP_dan_LLM_Dokumentasi_Klinis/` |
| Mehri dkk. (2026) | `source/04_Resume_Medis_dan_Ringkasan_Pulang/` |
| Murcittowati dkk. (2023) | `source/external/01_Konteks_Indonesia_Regulasi_dan_Klaim/` |
| Mwogosi & Mambile (2026) | `source/02_Audit_dan_Deteksi_Ketidaksesuaian_Dokumentasi/` |
| Nielsen (1994) | `source/external/06_Metodologi_Desain_dan_Evaluasi_Usability/` |
| Nilasari & Soelistijanto (2026) | `source/12_Konteks_Indonesia_JKN_INA-CBG/` |
| Olex & McInnes (2021) | `source/06_Halusinasi_Verifikasi_dan_Konsistensi_Temporal/` |
| Page dkk. (2017) | `source/07_Alert_Fatigue_dan_Peringatan_Non-Interruptive/` |
| Parambath dkk. (2026) | `source/external/05_Provenance_dan_Keterlacakan/` |
| Peffers dkk. (2007/2008) | `source/external/06_Metodologi_Desain_dan_Evaluasi_Usability/` |
| Permenkes No. 24 (2022) | `source/external/01_Konteks_Indonesia_Regulasi_dan_Klaim/` |
| Permenkes No. 26 (2021) | `source/external/01_Konteks_Indonesia_Regulasi_dan_Klaim/` |
| R. Yang dkk. (2026), RAG in medicine | `source/05_RAG_di_Ranah_Klinis/` |
| Rachmawaty dkk. (2021) | `source/12_Konteks_Indonesia_JKN_INA-CBG/` |
| Sadowski dkk. (2015†) | `source/external/08_Analisis_Statis_dan_Pelacakan_Temuan/` |
| Sambodo dkk. (2023) | `source/12_Konteks_Indonesia_JKN_INA-CBG/` |
| Sangal dkk. (2023) | `source/07_Alert_Fatigue_dan_Peringatan_Non-Interruptive/` |
| Sangal dkk. (2023) | `source/external/03_Alert_Fatigue_dan_Peringatan/` |
| Schwieger dkk. (2024) | `source/04_Resume_Medis_dan_Ringkasan_Pulang/` |
| Septiono dkk. (2026) | `source/12_Konteks_Indonesia_JKN_INA-CBG/` |
| Simbolon & Gani (2023) | `source/external/01_Konteks_Indonesia_Regulasi_dan_Klaim/` |
| Skrabic dkk. (2026) | `source/02_Audit_dan_Deteksi_Ketidaksesuaian_Dokumentasi/` |
| Spacco dkk. (2006) | `source/external/08_Analisis_Statis_dan_Pelacakan_Temuan/` |
| Sun dkk. (2025), halusinasi | `source/06_Halusinasi_Verifikasi_dan_Konsistensi_Temporal/` |
| Sun dkk. (2027), KG-ACE | `source/10_Representasi_Pengetahuan_Graf/` |
| Susilo dkk. (2025) | `source/12_Konteks_Indonesia_JKN_INA-CBG/` |
| Syeda & Reddy (2026) | `source/10_Representasi_Pengetahuan_Graf/` |
| Tchouka dkk. (2024) | `source/08_Deidentifikasi_Privasi_dan_Singkatan_Klinis/` |
| Tonekaboni dkk. (2019) | `source/external/04_Reliance_Penjelasan_dan_Interaksi_Manusia-AI/` |
| van Koevorden dkk. (2026) | `source/11_Metodologi_Evaluasi_NLP_Klinis/` |
| Vasconcelos dkk. (2023) | `source/external/04_Reliance_Penjelasan_dan_Interaksi_Manusia-AI/` |
| W3C (2013), PROV-DM | `source/external/05_Provenance_dan_Keterlacakan/` |
| Waqas dkk. (2026) | `source/06_Halusinasi_Verifikasi_dan_Konsistensi_Temporal/` |
| Wei dkk. (2026) | `source/08_Deidentifikasi_Privasi_dan_Singkatan_Klinis/` |
| Woo dkk. (2026) | `source/01_NLP_dan_LLM_Dokumentasi_Klinis/` |
| Y. Yang dkk. (2026), CTKGR | `source/10_Representasi_Pengetahuan_Graf/` |
| Zeba dkk. (2026) | `source/06_Halusinasi_Verifikasi_dan_Konsistensi_Temporal/` |
| Zhang dkk. (2026) | `source/05_RAG_di_Ranah_Klinis/` |

Dua pasang berkas bersitasi sama ada di kedua pohon: Sangal dkk. (2023) dan Cánovas-Segura dkk. (2023) muncul di `source/07_...` dan `source/external/03_...`. Keduanya bukan salinan byte-identik (md5 berbeda), jadi dua-duanya dipertahankan.
