# Indeks Sumber Literatur

Diperbarui 3 November 2026 (versi pertama 23 Oktober 2026). Seluruh PDF di `source/` dikelompokkan menurut **lingkup pembicaraan**, diurutkan dari masalah (regulasi, klaim, rekam medis) ke pendekatan (NLP, LLM, RAG, graf) lalu ke batasan penggunaannya (rekomendasi, ketidakpastian, privasi). Analisis kebutuhan literatur terhadap notulensi revisi ada di [`bab2/Kebutuhan_Literatur_Revisi_Bab_II.md`](../bab2/Kebutuhan_Literatur_Revisi_Bab_II.md).

## Konvensi

- **Nama berkas** `1-s2.0-<ID>-main.pdf` (unduhan ScienceDirect) tidak diubah supaya kamus `PDFS` di `tools/verify_claims.py` dan peta ID di `CONTEXT_TRANSFER.md` tetap bisa ditelusuri. Path di `verify_claims.py` sudah diperbarui ke folder baru (40 path, semuanya ada).
- Prefiks asal unduhan dipertahankan: **M** = entri merah di `Sumber Literatur Bab 2.pdf` yang kini sudah diperoleh, **SD** = unduhan ScienceDirect/JMIR tambahan, **ITB** = koleksi digital Perpustakaan ITB, **TES** = prefiks dari unduhan asal (dibiarkan). Prefiks angka `NN_` pada unduhan lepas dihapus karena bertabrakan dengan nomor folder.
- `source/external/` = temuan teman capstone (Abizzar, Raihaan). **Tidak diubah**; isinya tetap seperti di indeks versi 23 Oktober (bagian B di bawah).
- Kolom **Status**: `inti` = langsung menjawab butir notulensi; `pendukung` = konteks atau pembanding; `tinjau` = relevansinya lemah setelah notulensi "sedikit tapi detail", pertimbangkan untuk tidak dipakai.

## Perubahan 3 November 2026

| Tindakan | Berkas |
| --- | --- |
| Dihapus (byte-identik, md5 sama) | `01_Permenkes_24_2022_Rekam_Medis (1).pdf` = `Permenkes_24_2022_Rekam_Medis.pdf`; `24592-115283-1-PB.pdf` = `Pertiwi_2026_SNOMED-CT_Indonesia.pdf` |
| Dipindah ke `_salah_unduh/` (isi tidak sesuai nama) | `SD07_…` berisi Jiang dkk. (2024) "Incorporating external knowledge for text matching model", *Computer Speech & Language*; `SD08_…` berisi Huang dkk. "Fact Check: Assessing the Response of ChatGPT to Alzheimer's Disease Myths"; `SD11_…` berisi Bui & Le "Fusing global attention and self-attention … tabular data", *ESWA* |
| Folder tema lama `01_…`–`12_…` | Isinya dipindah ke 17 folder baru; folder lama dihapus setelah kosong |
| Ditambahkan (unduhan resmi, untuk revisi Bab II) | `01_…/KMK_HK.01.07-MENKES-1423-2022_Variabel_dan_Metadata_RME.pdf` dan `01_…/KMK_HK.01.07-MENKES-1596-2024_Standar_Akreditasi_RS.pdf` dari JDIH Kemenkes; `04_…/SATUSEHAT_Panduan_Rawat_Inap_v6.0_diakses_2026-11-03.html` (salinan halaman web) |

Berkas yang benar untuk ketiga entri `_salah_unduh/` (semuanya *open access*):

- SD07 → Popescu, Roitero, & Della Mea (2026). Integrating Confidence, Difficulty, and Language Model Calibration for Better Explainability in Clinical Documents Coding. *JMIR AI*, 5, e78764. <https://doi.org/10.2196/78764>
- SD08 → Omar dkk. (2025). Benchmarking the Confidence of Large Language Models in Answering Clinical Questions. *JMIR Medical Informatics*, 13, e66917. <https://medinform.jmir.org/2025/1/e66917>
- SD11 → Chang & Sung (2024). Use of SNOMED CT in Large Language Models: Scoping Review. *JMIR Medical Informatics*, 12, e62924. <https://medinform.jmir.org/2024/1/e62924>

## Masalah kualitas berkas

| Berkas | Masalah | Saran |
| --- | --- | --- |
| `01_…/Permenkes_26_2021_Pedoman_INA-CBG.pdf` | Hasil pindai: hanya 891 kata dari 56 halaman, tidak bisa dicari | Pakai salinan berteks `external/01_Konteks_Indonesia_Regulasi_dan_Klaim/2021permenkes026.pdf` (10.149 kata) |
| `04_…/ITB03_Indrawan_2023_Tesis_RDB2FHIR.pdf` | 4 halaman tanpa lapisan teks (hanya tanda "Dokumen Asli") | Unduh ulang atau OCR sebelum dikutip |
| `02_…/ITB11_Khairunisa_2020_…pdf` | Lapisan teks rusak (karakter acak) | OCR atau baca visual |
| `ITB05`, `ITB08`, `ITB09`, `ITB10`, `ITB11`, `ITB04` | Hanya abstrak (4–6 halaman); isi lengkap terbatas di area kampus | Cukup untuk mengutip abstrak; isi lengkap lewat digilib ITB di kampus |
| `ITB07_…_BAB2` dan `ITB07_…_PUSTAKA` | Hanya Bab II dan daftar pustaka tesis | Cukup sebagai jalan *snowballing* |

Entri merah yang **masih belum diperoleh**: Maleki dkk. (2026, *J Health Organ Manag*), Mohanty dkk. (2027, bab buku), Lathifah dkk. (2020, *Enfermería Clínica*), Fahlevi dkk. (2021, *J Account Organ Change*). Sembilan entri merah lain sudah ada sebagai berkas M1–M9.

## Daftar isi

| Folder | Lingkup | Jumlah |
| --- | --- | --- |
| `01_Regulasi_dan_Kebijakan_Indonesia/` | Peraturan rekam medis, variabel RME, standar akreditasi, INA-CBG, pelindungan data, kebijakan AI kesehatan Indonesia | 7 |
| `02_Klaim_JKN_INA-CBG_dan_Kecurangan/` | Pembiayaan JKN, tarif INA-CBG, upcoding, deteksi kecurangan klaim | 10 |
| `03_Rekam_Medis_CPPT_dan_Catatan_Perkembangan/` | Isi dan mutu CPPT, struktur catatan SOAP, NLP pada catatan perkembangan | 7 |
| `04_Standar_Interoperabilitas_dan_Terminologi_Klinis/` | HL7 FHIR/SATUSEHAT di Indonesia, SNOMED CT | 7 |
| `05_Graf_Pengetahuan_dan_Ontologi_Medis/` | Knowledge graph dari rekam medis, ontologi klinis, GraphRAG | 10 |
| `06_NLP_dan_LLM_Teks_Klinis/` | Survei NLP/PLM/LLM klinis, temporal, singkatan, normalisasi konsep | 9 |
| `07_Audit_Dokumentasi_dan_Deteksi_Kesalahan/` | LLM sebagai pemeriksa dokumentasi, kesesuaian kode dengan catatan | 4 |
| `08_Pengodean_ICD_dan_Kelayakan_Klaim/` | Pengodean ICD otomatis, kelayakan penggantian biaya | 4 |
| `09_Ringkasan_Pulang_dengan_LLM/` | Pembuatan dan penilaian ringkasan pulang | 5 |
| `10_RAG_Retrieval-Augmented_Generation/` | RAG umum (fondasi, survei) dan RAG klinis | 9 |
| `11_Halusinasi_dan_Verifikasi_Keluaran/` | Halusinasi LLM dan pemeriksaan fakta | 3 |
| `12_Rekomendasi_Penggunaan_LLM_Klinis/` | Pedoman dan konsensus: LLM boleh/tidak untuk tugas apa | 6 |
| `13_Ketidakpastian_Kalibrasi_dan_Kepercayaan/` | Kalibrasi, metakognisi, komunikasi tingkat kepercayaan | 5 |
| `14_Deidentifikasi_dan_Anonimisasi/` | Pedoman de-identifikasi, risiko re-identifikasi, teknik anonimisasi | 15 |
| `15_Peringatan_dan_Alert_Fatigue/` | Kelelahan peringatan dan desain peringatan | 6 |
| `16_Sistem_Hibrida_Aturan_dan_AI/` | Gabungan sistem berbasis aturan dan AI | 2 |
| `17_Evaluasi_Sistem_NLP_Klinis/` | Pedoman anotasi dan validasi (ditunda sesuai notulensi) | 3 |
| `_salah_unduh/` | Berkas yang isinya tidak sesuai nama | 3 |

## A. source/

### 01. Regulasi dan Kebijakan Indonesia

| Sitasi | Judul / isi | Berkas | Status | Catatan |
| --- | --- | --- | --- | --- |
| Permenkes No. 24 (2022) | Rekam Medis | `Permenkes_24_2022_Rekam_Medis.pdf` | inti | Pasal 11 (sistem wajib mengacu variabel dan metadata Kemenkes), Pasal 16–17 (pengisian lengkap, berurutan, terintegrasi = dasar CPPT), Pasal 19 (input kode untuk klaim), Pasal 21 (wajib terhubung platform Kemenkes), Pasal 26–27 (isi rekam medis). Salinan lain: `external/01_…/2022permenkes024.pdf` (md5 berbeda, isi sama) |
| Permenkes No. 26 (2021) | Pedoman INA-CBG dalam Pelaksanaan Jaminan Kesehatan | `Permenkes_26_2021_Pedoman_INA-CBG.pdf` | inti | Menetapkan ICD-10 versi 2010 dan ICD-9-CM versi 2010 untuk koding dan verifikasi. Berkas ini pindaian; pakai salinan berteks di `external/` |
| KMK HK.01.07/MENKES/1423/2022 | Pedoman Variabel dan Meta Data pada Penyelenggaraan Rekam Medis Elektronik | `KMK_HK.01.07-MENKES-1423-2022_…pdf` | inti | 92 hlm., berteks. Dataset IGD, rawat jalan, rawat inap (hlm. 57–81), laboratorium, apotek; tiap variabel punya tipe data, format, definisi operasional, referensi. Dataset rawat inap **tidak** memuat variabel CPPT |
| KMK HK.01.07/MENKES/1596/2024 | Standar Akreditasi Rumah Sakit | `KMK_HK.01.07-MENKES-1596-2024_…pdf` | inti | 356 hlm., berteks (ada tanda air). MRMIK 7–9, 12 (hlm. 163–168: isi RM, identitas entri, kode/singkatan, pengkajian RM); AKP 3 (hlm. 215: CPPT); AKP 5.1 (hlm. 218–219: 6 butir isi ringkasan pulang); PAP 1.1–1.2 (hlm. 263, 266). Tidak menyebut SOAP |
| UU No. 27 (2022) | Pelindungan Data Pribadi | `UU_27_2022_Pelindungan_Data_Pribadi.pdf` | inti | Data kesehatan termasuk data pribadi spesifik |
| Fitriasari & Umasugi (2026) | Governing artificial intelligence in Indonesia digital health system: interoperability, equity, and policy readiness (*Health Policy and Technology*, komentar) | `SD01_…` | pendukung | Mengusulkan *regulatory sandbox* AI kesehatan yang terhubung dengan SATUSEHAT; bukti bahwa regulasi khusus belum ada |
| [cek penulis] (2026) | Indonesia's health reform: from pandemic mandate to the six pillars of transformation (*The Lancet*, Comment, 25 Juni 2026) | `SD04_…` | pendukung | Komentar dimulai di tengah halaman 1684; halaman 1 berisi komentar lain |

### 02. Klaim JKN, INA-CBG, dan Kecurangan

| Sitasi | Judul | Berkas | Status | Catatan |
| --- | --- | --- | --- | --- |
| Susilo dkk. (2025) | Can Indonesia achieve universal health coverage? Organisational and financing challenges in implementing the national health insurance system | `1-s2.0-S294985622500090X-main.pdf` | pendukung | Dipakai di draf II.1 |
| Rachmawaty dkk. (2021) | Evaluation of health care quality among insured patients in Indonesian mother & child hospital | `1-s2.0-S0213911121003071-main.pdf` | pendukung | Konteks RSIA |
| Nilasari & Soelistijanto (2026) | A Preliminary Study on Mitigating Upcoding in Indonesia's National Health Insurance using Multi-Agent Multi-Armed Bandits | `1-s2.0-S1877050926029406-main.pdf` | pendukung | |
| Barsasella dkk. (2021) | Predicting length of stay and mortality among hospitalized patients with type 2 diabetes mellitus and hypertension | `1-s2.0-S1386505621001957-main.pdf` | tinjau | Tidak menyentuh dokumentasi klinis |
| Sambodo dkk. (2023) | Effects of performance-based capitation payment on the use of public primary health care services in Indonesia | `1-s2.0-S0277953623002782-main.pdf` | tinjau | Layanan primer, bukan rawat inap |
| Septiono dkk. (2026) | Eclampsia and preeclampsia with tropical seasonality: Evidence from Indonesia's national health insurance registry | `1-s2.0-S2210778926000723-main.pdf` | tinjau | Epidemiologi, bukan klaim |
| Cahya (2024), tesis ITB | Ensemble model untuk deteksi fraud pada klaim asuransi kesehatan … LOF, iForest, dan Z-score | `ITB08_…` | tinjau | Abstrak saja; data transaksi terstruktur |
| Adiyansyah (2024), tesis ITB | Deteksi pencilan pada data klaim asuransi kesehatan menggunakan pembelajaran mesin | `ITB09_…` | tinjau | Abstrak saja |
| Jeremy (2024), TA ITB | Identifikasi kecurangan penyedia layanan kesehatan menggunakan support vector machine | `ITB10_…` | tinjau | Abstrak saja |
| Khairunisa (2020), TA ITB | Kualitas dan biaya BPJS kasus DBD di RSIA Zainab (judul dari nama berkas) | `ITB11_…` | pendukung | Lapisan teks rusak; konteks RSIA |

### 03. Rekam Medis, CPPT, dan Catatan Perkembangan

| Sitasi | Judul | Berkas | Status | Catatan |
| --- | --- | --- | --- | --- |
| Oktavia Az dkk. (2021) | Pengaruh penulisan formulir Catatan Perkembangan Pasien Terintegrasi terhadap MIRM 13.3 di Kota Bandung (*Jurnal MAKES* 4(3)) | `OktaviaAz_2021_CPPT_MIRM.pdf` | inti | Isi lembar CPPT (identitas, tanggal, jam, catatan perkembangan) dan masalah pengisiannya; acuan MIRM 13.3 = SNARS lama |
| Nadi dkk. (2024) | Optimizing Integrated Patient Progress Notes through the Application of Electronic Medical Record … : a Narrative Review (*Procedia of Engineering and Life Science* 6) | `Nadi_2024_CPPT_Elektronik.pdf` | inti | Praktik dan tantangan CPPT di RS Indonesia |
| Hakim dkk. (2026) | Evaluation of electronic medical records risk management in Kudus hospitals: A comparative qualitative study | `SD02_…` | pendukung | RME di dua RS Indonesia |
| Gao dkk. (2022), LREC | Hierarchical Annotation for Building A Suite of Clinical NLP Tasks: Progress Note Understanding | `Gao_2022_Progress_Note_Understanding_SOAP.pdf` | inti | Anotasi bagian SOAP pada catatan perkembangan |
| Socrates dkk. (2023) | Predicting relations between SOAP note sections: The value of incorporating a clinical information model (*JBI* 141) | `SD03_…` | inti | Relasi antarbagian S-O-A-P; paling dekat dengan "isi CPPT bisa distrukturkan" |
| Machado de Oliveira dkk. (2024) | SOAP classifier for free-text clinical notes with domain-specific pre-trained language models (*ESWA* 245) | `SD13_…` | pendukung | |
| Gao dkk. (2023) | Progress Note Understanding — Assessment and Plan Reasoning: Overview of the 2022 N2C2 Track 3 shared task (*JBI* 142) | `SD14_…` | pendukung | |

### 04. Standar Interoperabilitas dan Terminologi Klinis

| Sitasi | Judul | Berkas | Status | Catatan |
| --- | --- | --- | --- | --- |
| Heryawan dkk. (2025) | FHIR-Based Interoperability Design in Indonesia: Content Analysis of Developer Hub's Social Networking Service (*JMIR*) | `Heryawan_2025_…` | inti | Bukti pemakaian FHIR (SATUSEHAT) di Indonesia |
| Kementerian Kesehatan (2026) | Panduan interoperabilitas SATUSEHAT: Rawat Inap, versi 6.0 (10 Januari 2026), diakses 3 November 2026 | `SATUSEHAT_Panduan_Rawat_Inap_v6.0_diakses_2026-11-03.html` | inti | Alur 29 langkah dan *resource* FHIR; diagnosis ICD-10, tindakan ICD-9-CM, tanda vital LOINC, temuan klinis SNOMED CT, obat KFA; resume medis = Composition LOINC 34105-7, 13 bagian. Tidak ada *resource* CPPT. Halaman web dapat berubah |
| Hidayat, tesis ITB | Penerapan standar FHIR untuk interoperabilitas rekam kesehatan elektronik Indonesia | `ITB01_…` | pendukung | Lengkap (118 hlm.) |
| Sari Dewi (2024), tesis ITB | Studi komparasi komunikasi sinkron dan asinkron dalam penerapan standar FHIR … platform SATUSEHAT | `ITB02_…` | pendukung | Lengkap (219 hlm.) |
| Indrawan (2023), tesis ITB | RDB2FHIR (judul dari nama berkas) | `ITB03_…` | tinjau | Tanpa lapisan teks |
| Pertiwi dkk. (2026) | Adopsi SNOMED-CT, studi Korea Selatan dan konteks Indonesia (*Vol 15 No 1*, hlm. 76–83) | `Pertiwi_2026_SNOMED-CT_Indonesia.pdf` | inti | Menyatakan adopsi SNOMED CT di Indonesia masih tahap awal |
| Gaudet-Blavignac dkk. (2026) | Extended Grammar of SNOMED CT for Semantic Representation of Clinical Data: Methodological Study (*JMIR*) | `M1_…` | inti | Representasi semantik data klinis dengan SNOMED CT |

### 05. Graf Pengetahuan dan Ontologi Medis

| Sitasi | Judul | Berkas | Status | Catatan |
| --- | --- | --- | --- | --- |
| Xiao dkk. (2022) | FHIR-Ontop-OMOP: Building clinical knowledge graphs in FHIR RDF with the OMOP Common Data Model (*JBI*) | `Xiao_2022_…` | inti | KG klinis yang dibangun dari standar rekam medis (FHIR, OMOP) |
| Rotmensch dkk. (2017) | Learning a Health Knowledge Graph from Electronic Medical Records (*Scientific Reports*) | `Rotmensch_2017_…` | inti | KG penyakit–gejala dari rekam medis |
| Murali dkk. (2023) | Towards EHR-based medical knowledge graph construction, completion, and applications: A literature study (*JBI* 143) | `SD10_…` | inti | Survei KG berbasis rekam medis |
| Al Khatib dkk. (2024) | Patient-centric knowledge graphs: a survey of current methods, challenges, and applications | `AlKhatib_2024_…` | pendukung | |
| Ali dkk. (2026) | Ontology-grounded knowledge graphs for mitigating hallucinations in LLMs for clinical question answering (*JBI*) | `SD12_…` | pendukung | |
| Wu dkk. (2025), ACL | Medical Graph RAG: Evidence-based Medical LLM via Graph Retrieval-Augmented Generation | `Wu_2025_…` | pendukung | |
| Reinhart (2025), tesis ITB | Ekstraksi informasi berbasis pemrosesan bahasa alami untuk konstruksi graf pengetahuan medis | `ITB04_…` | pendukung | Abstrak saja; tertanggal Januari 2025 di sampul, nama berkas menulis 2024 |
| Sun dkk. (2027), KG-ACE | KG-ACE: Knowledge Graph Alignment and Consistency Enhancement for medical reasoning with LLMs | `1-s2.0-S0306457326004619-main.pdf` | pendukung | |
| Syeda & Reddy (2026) | Knowledge graphs and large language models: Construction paradigms, integration approaches, and emerging applications | `1-s2.0-S0950705126013274-main.pdf` | tinjau | Tidak spesifik medis (kritik notulensi) |
| Y. Yang dkk. (2026), CTKGR | Temporal knowledge graph enhanced prediction of in-hospital events for pneumonia patients using EHR | `1-s2.0-S1532046426000316-main.pdf` | tinjau | Prediksi kejadian, bukan struktur dokumen |

### 06. NLP dan LLM untuk Teks Klinis

| Sitasi | Judul | Berkas | Status |
| --- | --- | --- | --- |
| Kumar dkk. (2026) | Natural Language Processing in Healthcare: From Unstructured Data to Clinical Intelligence | `1-s2.0-S2667305326000724-main.pdf` | pendukung |
| Woo dkk. (2026) | The use of large language models in clinical documentation: A scoping review | `1-s2.0-S0020748925003323-main.pdf` | pendukung |
| Elvas dkk. (2025) | Natural language processing in medical text processing: A scoping literature review | `1-s2.0-S1386505625002667-main.pdf` | tinjau |
| Luo dkk. (2024) | Pre-trained language models in medicine: A survey | `1-s2.0-S0933365724001465-main.pdf` | tinjau |
| Kayira dkk. (2026) | NLP of Clinical Notes for Cancer Research and Patient Care Prior to Widespread Adoption of Generative AI: Scoping Review (*JMIR AI*) | `M9_…` | tinjau |
| Olex & McInnes (2021) | Review of Temporal Reasoning in the Clinical Domain for Timeline Extraction | `1-s2.0-S1532046421001131-main.pdf` | pendukung |
| Jafarpour dkk. (2025) | Preprocessing narrative texts in electronic medical records to identify hospital adverse events | `1-s2.0-S0933365725002167-main.pdf` | pendukung |
| Wei dkk. (2026) | Selection-based prompting … clinical abbreviation disambiguation via open-source LLMs | `1-s2.0-S1532046426001097-main.pdf` | pendukung |
| Chen dkk. (2026) | A comprehensive survey on medical concept normalization | `1-s2.0-S1532046426000298-main.pdf` | pendukung |

### 07. Audit Dokumentasi dan Deteksi Kesalahan

| Sitasi | Judul | Berkas | Status | Catatan |
| --- | --- | --- | --- | --- |
| Skrabic dkk. (2026) | Large language models as second reviewers for medical errors in real-world internal medicine reports | `1-s2.0-S1386505626000560-main.pdf` | inti | |
| Kim dkk. (2026) | Improving Radiology Report Error Detection Using a Multipass Large Language Model (*JMIR Med Inform*) | `M6_…` | inti | Menekan positif palsu pada prevalensi kesalahan rendah; relevan untuk peringatan per kategori |
| Du dkk. (2026) | Information systems auditing of psychiatric diagnoses using context-enriched QA-based language models | `1-s2.0-S266676492600007X-main.pdf` | pendukung | |
| Mwogosi & Mambile (2026) | Concordance of EHR data with ICD classification and evidence-based treatment guidelines | `1-s2.0-S2211883726000614-main.pdf` | pendukung | |

Dietrich & Stubbert (2026), rujukan utama audit IGD, ada di `external/02_Audit_dan_Pengodean_Klinis_Berbantuan_AI/`.

### 08. Pengodean ICD dan Kelayakan Klaim

| Sitasi | Judul | Berkas | Status |
| --- | --- | --- | --- |
| Hou dkk. (2024) | Modelling long medical documents and code associations for explainable automatic ICD coding | `1-s2.0-S0957417424003841-main.pdf` | pendukung |
| Jaganathan dkk. (2025) | Metamorphic Testing for Robustness and Fairness Evaluation of LLM-based Automated ICD Coding Applications | `1-s2.0-S235264832500025X-main.pdf` | pendukung |
| Lebeña dkk. (2025) | Large language models aided patient progression documentation according to the ICD standard | `1-s2.0-S2352914825000255-main.pdf` | pendukung |
| Seo dkk. (2026) | Assessing Eligibility for Anticancer Drug Health Insurance Reimbursement Using LLMs (*JMIR*) | `M2_…` | inti — analog terdekat: LLM menalar kriteria asuransi nasional, kerangka tiga keadaan (layak/tidak layak/belum dapat ditentukan) |

### 09. Ringkasan Pulang dengan LLM

| Sitasi | Judul | Berkas | Status |
| --- | --- | --- | --- |
| Schwieger dkk. (2024) | LLMs can support generation of standardized discharge summaries | `1-s2.0-S1386505624003174-main.pdf` | pendukung |
| Kleebayoon & Wiwanitkit (2025) | Correspondence atas Schwieger dkk. (1 hlm.) | `1-s2.0-S1386505624004192-main.pdf` | tinjau |
| Grazhdanski dkk. (2025) | SynthMedic: synthetic discharge summary generation, correction and validation | `1-s2.0-S1532046425001352-main.pdf` | tinjau |
| Mehri dkk. (2026) | Assessing the quality of AI-generated and physician-written discharge summaries | `1-s2.0-S2352396426001295-main.pdf` | pendukung |
| Tung dkk. (2024) | Comparison of the Quality of Discharge Letters Written by LLMs and Junior Clinicians (*JMIR*) | `M3_…` | pendukung |

### 10. RAG (Retrieval-Augmented Generation)

| Sitasi | Judul | Berkas | Status | Catatan |
| --- | --- | --- | --- | --- |
| Lewis dkk. (2020), NeurIPS | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | `TES_26_Lewis_2020_RAG.pdf` | inti | Makalah asal RAG; sumber diagram arsitektur |
| Gao dkk. (2023) | Retrieval-Augmented Generation for Large Language Models: A Survey | `Gao_2023_RAG_for_LLMs_Survey.pdf` | inti | Taksonomi naive/advanced/modular RAG; preprint arXiv, cek status terbit |
| R. Yang dkk. (2026) | RAG in medicine: A scoping review | `1-s2.0-S2666379126003447-main.pdf` | pendukung | |
| Landolsi dkk. (2026) | Recent trends of RAG in healthcare: A systematic review | `1-s2.0-S0952197626021962-main.pdf` | pendukung | |
| Zhang dkk. (2026) | Optimising clinical information extraction: RAG techniques in clinical notes | `1-s2.0-S1532046426000778-main.pdf` | inti | Satu-satunya RAG pada catatan klinis harian |
| Jia dkk. (2026) | Agentic memory-augmented retrieval and evidence grounding for medical QA | `1-s2.0-S1386505626000791-main.pdf` | tinjau | Soal ujian |
| Li dkk. (2026) | Evidence-linked recommendations for spine surgery via a retrieval-augmented LLM agent | `1-s2.0-S0720048X26000823-main.pdf` | pendukung | |
| Tu dkk. (2026) | Ethical Imperatives for RAG in Clinical Nursing: Viewpoint (*JMIR Med Inform*) | `M7_…` | pendukung | |
| Wijaya (2026), TA ITB | Mitigasi halusinasi pada RAG-LLM dengan ekspansi akronim, query rewriting, dan context reranking pada dataset biomedis | `ITB05_…` | pendukung | Abstrak saja |

### 11. Halusinasi dan Verifikasi Keluaran

| Sitasi | Judul | Berkas | Status |
| --- | --- | --- | --- |
| Zeba dkk. (2026) | Mitigating hallucinations in healthcare LLMs with granular fact-checking | `1-s2.0-S0957417426018786-main.pdf` | inti |
| Sun dkk. (2025) | A scoping review of NLP in addressing medically inaccurate information | `1-s2.0-S1532046425000954-main.pdf` | pendukung |
| Waqas dkk. (2026) | Hallucination detection, verification, and correction in generative AI: A comprehensive survey | `1-s2.0-S2949719126000361-main.pdf` | pendukung |

### 12. Rekomendasi Penggunaan LLM Klinis

| Sitasi | Judul | Berkas | Status | Catatan |
| --- | --- | --- | --- | --- |
| AHIMA (2024) | Artificial Intelligence Tools for Documentation and other Non-Clinical Work in Healthcare (issue brief) | `AHIMA_2024_…` | inti | 4 hlm., berbasis wawancara terstruktur oleh Alazro Consulting; bukan artikel *peer-reviewed* |
| WHO (2024) | Ethics and governance of AI for health. Guidance on large multi-modal models | `WHO_2024_…` | inti | 98 hlm. |
| Wong dkk. (2025), ESMO ELCAP | ESMO guidance on the use of Large Language Models in Clinical Practice | `SD05_…` | inti | Tiga tipe penggunaan (pasien, tenaga kesehatan, institusi) lewat Delphi |
| Devanand dkk. (2026) | A pragmatic risk-stratified framework for using LLMs in intensive care medicine: A narrative review | `SD06_…` | inti | Stratifikasi risiko per tugas |
| Denecke dkk. (2024) | Potential of Large Language Models in Health Care: Delphi Study (*JMIR*) | `Denecke_2024_…` | pendukung | |
| Sul & Kim (2025) | Consensus on the Potential of LLMs in Healthcare: Insights from a Delphi Survey in Korea (*Healthc Inform Res* 31(2)) | `Sul_2025_…` | pendukung | |

### 13. Ketidakpastian, Kalibrasi, dan Kepercayaan

| Sitasi | Judul | Berkas | Status |
| --- | --- | --- | --- |
| Testoni & Calixto (2026), EACL | Mind the Gap: Benchmarking LLM Uncertainty and Calibration with Specialty-Aware Clinical QA | `Testoni_2026_…` | inti |
| Griot dkk. (2025) | Large Language Models lack essential metacognition for reliable medical reasoning (*Nature Communications*) | `Griot_2025_…` | inti |
| Kompa dkk. (2021) | Second opinion needed: communicating uncertainty in medical machine learning (*npj Digital Medicine*) | `Kompa_2021_…` | inti |
| Schimmelpfennig dkk. (2025) | CeRTS: certainty retrieval token search in LLM clinical information extraction (*JBI*) | `SD09_…` | pendukung |
| Rezaeian dkk. (2025) | Explainability and AI Confidence in CDSS: Effects on Trust, Diagnostic Performance, and Cognitive Load | `Rezaeian_2025_…` | pendukung |

### 14. De-identifikasi dan Anonimisasi

| Sitasi | Judul | Berkas | Status | Catatan |
| --- | --- | --- | --- | --- |
| HHS OCR (2012) | Guidance on De-identification of Protected Health Information (HIPAA Safe Harbor & Expert Determination) | `HHS_2012_…` | inti | Pedoman resmi; pembanding internasional |
| NIST SP 800-188 (2023) | De-Identifying Government Datasets: Techniques and Governance | `NIST_SP_800-188_…` | inti | Pedoman teknik + tata kelola, termasuk kuasi-identifier |
| El Emam dkk. (2011) | A systematic review of re-identification attacks on health data (*PLoS ONE*) | `ElEmam_2011_…` | inti | |
| Rocher dkk. (2019) | Estimating the success of re-identifications in incomplete datasets using generative models (*Nature Communications*) | `Rocher_2019_…` | inti | Bukti bahwa kombinasi atribut cukup untuk re-identifikasi |
| Krzyzanowski & Manson (2022) | Twenty Years of the HIPAA Safe Harbor Provision: Unsolved Challenges | `SD15_…` | pendukung | |
| Jeon dkk. (2020) | De-Identification Strategy … OMOP-CDM in a Public Cloud: k-anonymity, l-diversity, t-closeness | `SD16_…` | inti | Penerapan model privasi pada data klinis terstruktur |
| Kudlicki dkk. (2026) | Leveraging routine scheduling patterns to unshift Date-Shifted clinical data | `SD17_…` | pendukung | Pergeseran tanggal bisa dibalik |
| Chevrier dkk. (2019) | Use and Understanding of Anonymization and De-Identification in the Biomedical Literature: Scoping Review | `SD18_…` | pendukung | Definisi istilah |
| Zuo dkk. (2021) | Data Anonymization for Pervasive Health Care: Systematic Literature Mapping Study | `SD19_…` | pendukung | |
| Faustini dkk. (2026) | De-identification of clinical data: A systematic review | `1-s2.0-S1386505625004423-main.pdf` | pendukung | |
| Azzam dkk. (2026) | Agentic LLM for anonymizing healthcare data with contextual awareness | `1-s2.0-S0950705126007604-main.pdf` | pendukung | |
| Tchouka dkk. (2024) | Differentially private de-identifying textual medical document … ICD-10 code association | `1-s2.0-S2667305324000905-main.pdf` | pendukung | |
| Atikasari (2024), tesis ITB | Pengembangan kerangka kerja rekayasa privasi untuk berbagi data rekam medis elektronik | `ITB06_…` | pendukung | Lengkap (168 hlm.); konteks Indonesia |
| Ganeswara (2025), tesis ITB | Tata kelola risiko privasi SIMRS (Bab II dan daftar pustaka) | `ITB07_…_BAB2`, `ITB07_…_PUSTAKA` | pendukung | |

### 15. Peringatan dan Alert Fatigue

| Sitasi | Judul | Berkas | Status |
| --- | --- | --- | --- |
| Sangal dkk. (2023) | Clinical Decision Support: Moving Beyond Interruptive "Pop-up" Alerts | `1-s2.0-S0025619623002549-main.pdf` | pendukung |
| Cánovas-Segura dkk. (2023) | Meaningful time-related aspects of alerts in CDSS | `1-s2.0-S1532046423001181-main.pdf` | pendukung |
| Boccio dkk. (2026) | Impact of a non-interruptive EHR-based CDS tool on HEART score documentation compliance | `1-s2.0-S1386505626004752-main.pdf` | pendukung |
| Page dkk. (2017) | Effectiveness of interruptive medication prescribing alerts in hospital CPOE systems | `1-s2.0-S1386505617301600-main.pdf` | pendukung |
| Newton dkk. (2026) | Experiences of Alert Fatigue and Its Contributing Factors in Hospitals (*JMIR*) | `M4_…` | pendukung |
| Gani dkk. (2025) | Understanding "Alert Fatigue" in Primary Care (*JMIR*) | `M5_…` | pendukung |

Lingkup ini lebih dekat ke peran antarmuka (Abizzar). Dua berkas bersitasi sama juga ada di `external/03_…` (md5 berbeda).

### 16. Sistem Hibrida Aturan dan AI

| Sitasi | Judul | Berkas | Status |
| --- | --- | --- | --- |
| Domingues (2026) | A hybrid decision support system using rule-based and AI methods: the OnCATs framework | `1-s2.0-S1386505625003612-main.pdf` | pendukung |
| Ijadi Maghsoodi dkk. (2026) | AI for decision-making in healthcare: decision-maker-governed hybrid systems | `1-s2.0-S2211883726001401-main.pdf` | pendukung |

### 17. Evaluasi Sistem NLP Klinis (ditunda)

| Sitasi | Judul | Berkas |
| --- | --- | --- |
| Becker dkk. (2025) | Extending CARDIO:DE: Additional annotation guidelines and evaluation of NLP approaches | `1-s2.0-S1386505625002266-main.pdf` |
| van Koevorden dkk. (2026) | Validating large language model-assisted data extraction from clinical notes | `1-s2.0-S2949820126000378-main.pdf` |
| Singh dkk. (2025) | A Machine Learning Approach for Identifying People With Neuroinfectious Diseases in EHR (*JMIR Med Inform*) | `M8_…` |

## B. source/external/ (temuan teman capstone, tidak diubah)

| Folder | Isi |
| --- | --- |
| `01_Konteks_Indonesia_Regulasi_dan_Klaim/` | Permenkes 26/2021 (berteks), Permenkes 24/2022, Simbolon & Gani (2023), Murcittowati dkk. (2023) |
| `02_Audit_dan_Pengodean_Klinis_Berbantuan_AI/` | Dietrich & Stubbert (2026), Gao dkk. (2024) human-AI clinical coding, ACDIS & AHIMA (2022) query practice |
| `03_Alert_Fatigue_dan_Peringatan/` | Ancker dkk. (2017), Sangal dkk. (2023), Cánovas-Segura dkk. (2023) |
| `04_Reliance_Penjelasan_dan_Interaksi_Manusia-AI/` | Goddard dkk. (2012), Tonekaboni dkk. (2019), Amershi dkk. (2019), Bansal dkk. (2021), Vasconcelos dkk. (2023), Kim dkk. (2025) |
| `05_Provenance_dan_Keterlacakan/` | W3C PROV-DM (2013), HL7 FHIR R4 Provenance, Parambath dkk. (2026) |
| `06_Metodologi_Desain_dan_Evaluasi_Usability/` | Peffers dkk. (2007), Brooke (SUS), Nielsen (1994), ISO 9241-210 (2019) |
| `07_Pemodelan_Sistem_dan_Penalaran_Formal/` | Harel (1987) Statecharts, Doyle (1979) TMS |
| `08_Analisis_Statis_dan_Pelacakan_Temuan/` | Sadowski dkk. (Tricorder), Spacco dkk. (2006) |

Rincian judul, halaman, dan catatan tiap berkas `external/` tetap sama dengan indeks versi 23 Oktober (lihat riwayat git `source/INDEKS.md`).
