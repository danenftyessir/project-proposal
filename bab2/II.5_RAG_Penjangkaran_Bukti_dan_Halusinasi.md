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

## II.5 RAG, Penjangkaran Bukti, dan Halusinasi

### II.5.1 RAG pada Teks Klinis

*Retrieval-augmented generation* (RAG) menyisipkan bukti yang diambil dari sumber luar ke dalam masukan LLM sebelum model membangkitkan jawaban. Yang dkk. (2026) menelaah 251 studi RAG di bidang medis dan menemukan bahwa aplikasinya terkonsentrasi pada tanya jawab, pembuatan laporan, peringkasan teks, dan ekstraksi informasi (hlm. 2). Sumber pengetahuan yang paling sering dipakai ialah korpus ilmiah biomedis (88 studi), pedoman klinis (67 studi), dan rekam medis elektronik (33 studi) (hlm. 3). Dari 188 studi yang memakai *retrieval* padat, hanya 24 yang secara eksplisit memakai model *embedding* multibahasa; sisanya memakai model yang berpusat pada bahasa Inggris (hlm. 4). Penulisnya menilai RAG medis masih berada pada tahap awal dan memerlukan validasi klinis serta adaptasi lintas bahasa (hlm. 2). Landolsi dkk. (2026) menelaah 57 studi pada sepuluh bidang medis; hanya enam di antaranya yang memakai sumber nonbarat atau nonbahasa Inggris, dan hanya empat yang divalidasi lintas institusi (hlm. 6, 19).

Zhang dkk. (2026) memberi bukti yang paling dekat dengan catatan klinis sehari-hari. Mereka membandingkan enam strategi *retrieval* pada catatan keperawatan fasilitas perawatan lansia di Australia, dengan Llama 3.1 8B sebagai pembangkit dan indeks yang dibangun dari segmen catatan itu sendiri, untuk dua tugas ekstraksi entitas yang masing-masing diuji pada 208 rekaman (hlm. 1, 5). Tanpa *retrieval*, F1 jawaban ialah 0,702 untuk gejala agitasi pada demensia dan 0,722 untuk faktor risiko malnutrisi; dengan *dense reranking*, angkanya 0,946 dan 0,953 (hlm. 6). F1 jawaban itu dihitung dengan BERTScore, yaitu kemiripan semantik terhadap anotasi acuan (hlm. 3), bukan kecocokan label persis. Galat yang paling sering ialah fabrikasi intrinsik, yaitu model memutarbalikkan informasi yang ada di teks sumber, disusul fabrikasi ekstrinsik dan negatif palsu (hlm. 8, 9). Penulisnya membatasi kesimpulan pada dua tugas berbasis skema; ekstraksi relasi, penalaran temporal, dan tanya jawab terbuka tidak dievaluasi (hlm. 11). Jia dkk. (2026) menguji agen dengan *retrieval*, *reranking*, dan penjangkaran bukti pada tolok ukur tanya jawab berformat ujian dan melaporkan akurasi 82,98% pada USMLE Step 1, di atas 80,67% untuk GPT-4 (hlm. 2).

### II.5.2 Penjangkaran Bukti dan Pengecekan Keluaran

Waqas dkk. (2026) membedakan halusinasi faktual, *faithful* (tidak sesuai dengan masukan), logis, dan temporal (hlm. 4). Survei atas 90 publikasi itu, yang tidak memakai penilaian risiko bias formal (hlm. 4), mengutip RAGTruth bahwa halusinasi tetap terjadi ketika konteks ambigu atau *retrieval* gagal menemukan semua bukti yang relevan (hlm. 10), dan menyatakan bahwa bidang kesehatan membutuhkan laju positif palsu yang sangat rendah (hlm. 18). Sun dkk. (2025) menelaah 55 artikel, 15 di antaranya tentang halusinasi, dan menemukan bahwa mitigasi halusinasi sebagian besar dikaji pada tugas tanya jawab, dataset deteksi halusinasi langka, serta evaluasinya bergantung pada penilaian pakar tanpa kerangka baku (hlm. 15, 18).

Li dkk. (2026) mencontohkan penjangkaran bukti pada pendukung keputusan bedah tulang belakang. Pangkalan pengetahuannya memuat pedoman dan literatur yang masing-masing diberi ID, sumber, tahun, dan tingkat bukti, dan diperbarui tiap enam bulan dengan penanda versi (hlm. 3, 4). Empat paragraf teratas disisipkan ke masukan model, keluaran berformat “rekomendasi + paragraf kutipan”, dan model diinstruksikan menjawab *“no clear conclusions available”* bila literatur tidak memberi jawaban pasti (hlm. 4). Lima ahli bedah menilai 200 kasus dengan rubrik 11 dimensi, termasuk ketepatan bukti yang dikutip (hlm. 1, 5). Namun yang dibandingkan ialah empat agen LLM dalam satu kerangka RAG di satu pusat, bukan RAG terhadap tanpa RAG (hlm. 9), dan artikelnya tidak menguraikan pemeriksaan kutipan otomatis.

Zeba dkk. (2026) menempuh cara lain: modul pemeriksa fakta tanpa LLM yang memeriksa keluaran LLM terhadap rekam medis sumber (hlm. 1). Ringkasan dan rekam medis dipecah menjadi proposisi atomik (hlm. 7), lalu setiap proposisi diberi vonis Didukung atau Tidak Didukung melalui pemeriksaan negasi, implikasi, konsistensi temporal, eksklusivitas bersama, kecocokan numerik, dan keberadaan (hlm. 6, 14). Pada 104 ringkasan yang diekstrak menjadi 3.786 proposisi dan divalidasi dokter, modul itu mencapai presisi 0,8904, *recall* 0,8234, dan F1 0,8556 (hlm. 1). Tanpa pemeriksaan negasi dan numerik, presisinya turun lebih dari 8% (hlm. 14). Datanya berasal dari MIMIC-III, rekam medis unit perawatan intensif (hlm. 10), dan penulisnya menyatakan sistem kurang andal pada bidang yang kurang terwakili, termasuk gangguan metabolik anak, serta hanya memberi vonis biner tanpa usul perbaikan (hlm. 15).

### II.5.3 Sintesis dan Celah

Sumber-sumber di atas menunjukkan bahwa *retrieval* menaikkan kinerja ekstraksi pada catatan klinis dan bahwa keluaran dapat ditautkan serta diperiksa terhadap sumbernya, tetapi ada empat celah bagi penelitian ini. Pertama, aplikasi RAG terkonsentrasi pada tanya jawab, pembuatan laporan, peringkasan, dan ekstraksi (Yang dkk., 2026, hlm. 2), dan bukti kinerja yang paling mencolok berasal dari soal ujian (Jia dkk., 2026, hlm. 2); di antara sumber yang dibaca, tidak ada yang menguji RAG untuk memeriksa kesesuaian antardokumen dalam satu episode rawat. Kedua, tidak ada sumber yang menguji teks klinis berbahasa Indonesia, dan *retrieval* umumnya memakai model berpusat pada bahasa Inggris (Yang dkk., 2026, hlm. 4; Landolsi dkk., 2026, hlm. 19). Ketiga, pemeriksaan keluaran terhadap sumber baru didemonstrasikan pada ringkasan LLM atas rekam medis berbahasa Inggris (Zeba dkk., 2026), sedangkan ketepatan kutipan pada Li dkk. (2026) dinilai ahli. Keempat, kontribusi *retrieval* dibandingkan dengan kondisi tanpa *retrieval* hanya pada dua tugas ekstraksi berbasis skema (Zhang dkk., 2026, hlm. 6, 11); pada audit, kontribusinya terhadap mutu temuan dan biaya positif palsunya belum diukur. Manfaat RAG pada audit dokumentasi rawat inap kebidanan dan anak karena itu perlu diuji dengan membandingkan konfigurasi dengan dan tanpa *retrieval* [SESUAIKAN DENGAN BAB I: rumusan pertanyaan dan ukuran keberhasilan].

---

## Daftar Pustaka (sementara)

> **[FORMAT AKHIR PERLU DIKONFIRMASI]** Pola mengikuti contoh pada templat (gaya mirip APA). Metadata dari halaman pertama masing-masing PDF.

Jia, S., Bit, S., Jasodanand, V. H., Liu, Y., & Kolachalama, V. B. (2026). Agentic memory-augmented retrieval and evidence grounding for medical question-answering tasks. *International Journal of Medical Informatics, 212*, 106339.

Landolsi, M. Y., Fadhli, I., Boufaied, A., & Ben Romdhane, L. (2026). Recent trends of retrieval-augmented generation in healthcare: A systematic review. *Engineering Applications of Artificial Intelligence, 182*, 115912.

Li, Y., Lv, M., Cheng, L., Xie, Y., Gu, Q., He, H., Chen, Z., Fang, D., & Zhou, X. (2026). Explainable and evidence-linked recommendations for spine surgery via a retrieval-augmented LLM agent. *European Journal of Radiology, 197*, 112734.

Sun, Z., Yim, W.-W., Uzuner, Ö., Xia, F., & Yetisgen, M. (2025). A scoping review of natural language processing in addressing medically inaccurate information: Errors, misinformation, and hallucination. *Journal of Biomedical Informatics, 169*, 104866.

Waqas, S. M., Umer, Z., Alim, A., Arham, M., Su'ud, M. M., Kazmi, S. J. A., & Alam, M. M. (2026). Hallucination detection, verification, and correction in generative AI: A comprehensive survey. *Natural Language Processing Journal, 16*, 100231.

Yang, R., [PERLU VERIFIKASI SUMBER: penulis lain; daftar pada halaman judul PDF terpotong], & Liu, N. (2026). Retrieval-augmented generation in medicine: A scoping review of technical implementations, clinical applications, and ethical considerations. *Cell Reports Medicine, 7*, 102927.

Zeba, M., Al Mamun, A., Tithee, K. J., Sutradhar, D., Raiaan, M. A. K., Mukta, S., Mohamed, R. E., Islam, M. R., Sebastian, Y., Hussain, M., & Azam, S. (2026). Mitigating hallucinations in healthcare LLMs with granular fact-checking and domain-specific adaptation. *Expert Systems with Applications, 329*, 132966.

Zhang, H., Vithanage, D., Deng, C., & Yu, P. (2026). Optimising clinical information extraction: A comparative study of retrieval-augmented generation techniques in clinical notes. *Journal of Biomedical Informatics, 180*, 105053.

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
