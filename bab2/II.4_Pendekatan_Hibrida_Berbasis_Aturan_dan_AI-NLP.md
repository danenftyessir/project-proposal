# Bab II — Subbab II.4 (DRAFT 1)

> **Status:** draf kerja, belum ditinjau pembimbing. Hanya bagian "Naskah" dan "Daftar Pustaka (sementara)" yang masuk ke proposal. Bagian "Lampiran kerja" adalah alat bantu pemeriksaan dan tidak dihitung dalam batas 19 halaman.
>
> **Konvensi sitasi sementara:** penulis-tahun dengan nomor halaman (`hlm.`). Semua sumber adalah artikel Elsevier bernomor artikel, sehingga `hlm.` = halaman berkas PDF. Format akhir menunggu pedoman program studi.
>
> **Sumber:** dua artikel baru dari `source/` (Domingues; Ijadi Maghsoodi dkk.) ditambah dua artikel yang sudah dipakai di II.2 (Kumar dkk., bagian 6.1; Chen dkk.), semuanya dibaca dari PDF. **Maleki dkk. (2026), analog terdekat menurut daftar sumber, tidak ada di repo sehingga subbab ini ditulis tanpanya** (lihat II.4.3 dan Lampiran C). Tidak ada sumber dari `source/external/`.
>
> **Penanda yang perlu dijawab pengguna:** satu `[SESUAIKAN DENGAN BAB I]` dan satu `[PERLU VERIFIKASI SUMBER]` pada subbab penutup.

---

## Naskah

## II.4 Pendekatan Hibrida Berbasis Aturan dan AI/NLP

### II.4.1 Kekuatan dan Batas Sistem Berbasis Aturan

Kumar dkk. (2026) menilai sistem berbasis aturan (*rule-based*) dan hibrida layak dipakai di layanan kesehatan karena transparan dan dapat ditafsirkan (hlm. 12). Keunggulan utama sistem berbasis aturan ialah hasilnya dapat diprediksi dan mudah divalidasi, terutama pada kondisi klinis yang diatur regulasi (hlm. 12). Kelemahannya, menurut Kumar dkk., sistem itu tidak dapat diskalakan lintas institusi dan spesialisasi karena perbedaan bahasa klinis harus dipelihara secara manual, dan kinerjanya umumnya buruk pada dataset baru atau kebiasaan dokumentasi yang berubah (hlm. 12). Karena itu, sistem tersebut paling cocok untuk tugas berlingkup kecil atau sebagai bagian dari *pipeline* hibrida, bukan sebagai solusi tunggal (hlm. 12). Chen dkk. (2026) sejalan dengan itu: aturan dan leksikon eksplisit masih efektif untuk subtugas sempit seperti disambiguasi singkatan (hlm. 13).

Domingues (2026) menunjukkan sisi keterlacakan sistem berbasis aturan lewat OnCATs, sistem pendukung keputusan klinis untuk kanker prostat yang mengubah 23 pedoman internasional menjadi 1.236 aturan dalam format JSON (hlm. 1, 2). Setiap rekomendasi disertai jejak pembenaran yang menyebut aturan dan sumber pedoman yang aktif (hlm. 2). Sistem itu diuji pada sepuluh laporan kasus terbitan, dan penulisnya menyebut pengujian itu sebagai uji kelayakan teknis, bukan validasi klinis (hlm. 3, 5). Penulis memperingatkan bahwa pembaruan basis pengetahuan secara manual berisiko tertinggal dari praktik klinis (hlm. 7). Meskipun judul artikelnya menyebut metode berbasis aturan dan AI, yang diuji hanya lapisan berbasis aturan; penulis sendiri menyebut sistemnya "*hybrid-ready*", dengan modul pembelajaran mesin baru direncanakan (hlm. 2). Artikel ini karenanya tidak memberi bukti tentang kinerja sistem hibrida, dan domainnya ialah pedoman terapi onkologi, bukan audit dokumentasi.

### II.4.2 Pola Hibrida dan Bukti yang Tersedia

Ijadi Maghsoodi dkk. (2026) menyusun tinjauan naratif kritis atas 101 sumber yang dipilih dari 3.892 rekaman, dengan fokus pada sistem hibrida yang lapisan simboliknya, yaitu aturan, ontologi, atau batasan, disusun atau disetujui pemangku kepentingan (hlm. 1, 4). Salah satu dari setidaknya lima pola rancangan yang mereka identifikasi ialah ekstraksi saraf disertai validasi simbolik, tempat pemeriksaan konsistensi dan aturan dokumentasi memvalidasi keluaran model NLP atau model fondasi untuk abstraksi laporan, pengodean, dan pencatatan registri (hlm. 5). Tinjauan itu menyimpulkan bahwa desain hibrida tampak paling kredibel pada situasi yang terikat aturan, peka terhadap audit, dan bergantung pada alur kerja, termasuk validasi dokumentasi (hlm. 1), serta bahwa bukti empiris lebih kuat untuk tugas terbatas seperti validasi laporan dan ekstraksi informasi daripada untuk klaim yang ambisius tentang penalaran klinis, kalibrasi kepercayaan, atau perbaikan luaran pasien (hlm. 7). Untuk dokumentasi buatan model generatif, penulisnya berargumen bahwa validasi hibrida dapat menegakkan elemen wajib dan mendeteksi inkonsistensi (hlm. 7); ini argumen konseptual, bukan hasil uji.

Penulisnya sendiri membatasi kesimpulan itu. Basis empiris masih terbatas dan bukti prospektif jarang (hlm. 1), dan klaim tentang dampak pada mutu keputusan sebaiknya dibaca sebagai pembangkit hipotesis, bukan temuan konfirmatif (hlm. 6). Lapisan simbolik menimbulkan beban akuisisi pengetahuan, ketidakselarasan ontologi, konflik aturan, dan pemeliharaan (hlm. 1, 9). Proses penyaringan tinjauan itu mengecualikan rekaman nonbahasa Inggris (hlm. 2), dan literaturnya terkonsentrasi pada sistem kesehatan berpendapatan tinggi dan matang secara digital (hlm. 9).

### II.4.3 Sintesis dan Celah

Sumber-sumber di atas mendukung dua hal yang terbatas: sistem berbasis aturan unggul dalam penelusuran dan validasi tetapi mahal dipelihara, dan kombinasi dengan komponen pembelajaran dinilai paling kredibel untuk validasi dokumentasi menurut satu tinjauan naratif. Keterbatasannya ada tiga. Pertama, di antara sumber yang dibaca, tidak ada yang membandingkan konfigurasi aturan saja dengan aturan ditambah AI/NLP pada audit dokumentasi klinis; satu-satunya sistem yang diuji (Domingues, 2026) hanya berbasis aturan, di bidang onkologi, pada sepuluh kasus. Kedua, dukungan terkuat untuk validasi dokumentasi bersifat konseptual (Ijadi Maghsoodi dkk., 2026, hlm. 7). Ketiga, tidak ada sumber yang menyangkut aturan atau dokumen klaim berbahasa Indonesia. Satu artikel pada daftar sumber, yang judulnya menyebut model hibrida pembelajaran mesin dan sistem pakar untuk identifikasi pemotongan klaim asuransi, belum dapat dibaca karena berkasnya tidak tersedia [PERLU VERIFIKASI SUMBER]. Pembagian kerja antara aturan dan AI/NLP pada penelitian ini karenanya merupakan pilihan rancangan yang perlu dibenarkan lewat perbandingan konfigurasi aturan saja dengan aturan ditambah AI/NLP [SESUAIKAN DENGAN BAB I: rumusan pertanyaan dan ukuran keberhasilan].

---

## Daftar Pustaka (sementara)

> **[FORMAT AKHIR PERLU DIKONFIRMASI]** Pola mengikuti contoh pada templat (gaya mirip APA). Hanya entri baru; Kumar dkk. (2026) dan Chen dkk. (2026) sudah ada pada daftar II.2. Metadata dari halaman pertama masing-masing PDF.

Domingues, N. S. (2026). A hybrid decision support system using rule-based and AI methods: The OnCATs knowledge-based framework. *International Journal of Medical Informatics, 206*, 106144.

Ijadi Maghsoodi, A., Kurz, J., Lawrenson, R., Parsons, M., Walker, C., O'Sullivan, M., & Rouse, P. (2026). Artificial intelligence for decision-making in healthcare: A critical review of decision-maker-governed hybrid systems across clinical, operational, and policy settings. *Health Policy and Technology, 15*, 101292.

---

## Lampiran kerja (bukan bagian naskah)

### Lampiran A. Tabel verifikasi klaim ke halaman PDF

Setiap baris dicocokkan otomatis ke teks halaman yang disebut (`tools/verify_claims.py` dengan `tools/claims_II4.json`; hasil: 35 dari 35 cocok). Nomor halaman = halaman berkas PDF = nomor cetak.

| Sumber | Klaim di naskah | Hlm. | Kutipan asli (pendek) |
|---|---|---|---|
| Kumar dkk. | Sistem berbasis aturan dan hibrida diterapkan karena transparan dan dapat ditafsirkan | 12 | "Transparency and interpretability make rule-based and hybrid NLP systems applicable" |
| Kumar dkk. | Dapat diprediksi, mudah divalidasi, terutama pada kondisi klinis yang diatur regulasi | 12 | "predictable and readily validated, especially in regulated clinical conditions" |
| Kumar dkk. | Tidak dapat diskalakan lintas institusi dan spesialisasi; kinerja buruk pada dataset baru atau kebiasaan dokumentasi berubah | 12 | "not scalable across institutions and specialties"; "poor performance when used with new data sets or changing documentation habits" |
| Kumar dkk. | Paling cocok untuk lingkup kecil atau bagian dari *pipeline* hibrida | 12 | "best suited to small scope endeavors or elements of hybrid pipelines" |
| Chen dkk. | Aturan dan leksikon eksplisit efektif untuk subtugas sempit (disambiguasi singkatan) | 13 | "Rule-oriented normalization remains effective for constrained subproblems"; "where explicit rules and lexicons are reliable" |
| Domingues | 23 pedoman menjadi basis aturan JSON; 1.236 aturan | 1, 2 | "Evidence from 23 international guidelines was formalized into a JSON-based rule base"; "The resulting rule base comprised 1,236 discrete rules" |
| Domingues | Setiap rekomendasi disertai jejak yang menyebut aturan dan sumber pedoman | 2 | "justification trace that cites the specific rules and guideline sources activated during reasoning" |
| Domingues | Sepuluh laporan kasus terbitan; uji kelayakan teknis, bukan validasi klinis | 1, 3, 5 | "Feasibility was tested using ten published case reports"; "This study is a technical feasibility evaluation using ten" (hlm. 3); "it is not a clinical validation" (hlm. 5) |
| Domingues | Ketidaksesuaian karena model harapan hidup yang disederhanakan dan data kasus tidak lengkap | 1 | "Divergences primarily reflected simplified life-expectancy modeling and incomplete case data" |
| Domingues | Imputasi dapat membiaskan rekomendasi; pembaruan manual berisiko tertinggal | 7 | "these can bias recommendations in unpredictable ways"; "manual updating risks lagging behind clinical practice" |
| Domingues | Judul menyebut aturan dan AI; yang diuji hanya lapisan berbasis aturan; "hybrid-ready" | 1, 2 | "A hybrid decision support system using rule-based and AI methods"; "hybrid-ready rather than hybrid-implemented"; "The current implementation represents the deterministic rule-based phase of a broader hybrid architecture" |
| Ijadi Maghsoodi dkk. | Tinjauan naratif kritis; 3.892 rekaman menjadi 101 sumber | 1 | "screening 3,892 de-duplicated records to 101 sources retained" |
| Ijadi Maghsoodi dkk. | Tiga syarat sistem tata-kelola pemangku kepentingan (lapisan simbolik, memengaruhi perilaku, disusun/disetujui pemangku kepentingan) | 4 | "three conditions are met" |
| Ijadi Maghsoodi dkk. | Setidaknya lima pola rancangan; ekstraksi saraf + validasi simbolik untuk abstraksi laporan, pengodean, registri | 4, 5 | "at least five recurring hybrid design patterns"; "Neural extraction plus symbolic validation"; "Report abstraction, coding, registry capture" |
| Ijadi Maghsoodi dkk. | Hibrida paling kredibel pada situasi terikat aturan, peka audit, bergantung alur kerja, termasuk validasi dokumentasi | 1 | "Hybrid designs appear most credible in rule-bound, audit-sensitive, and workflow-dependent settings, including documentation validation" |
| Ijadi Maghsoodi dkk. | Bukti lebih kuat untuk tugas terbatas daripada klaim ambisius | 7 | "The empirical base is stronger for bounded tasks such as report validation, information extraction, and constrained recommendation" |
| Ijadi Maghsoodi dkk. | Argumen: validasi hibrida pada dokumentasi buatan model generatif | 7 | "Hybrid validation is therefore especially compelling here, since it can enforce required elements, detect inconsistencies" |
| Ijadi Maghsoodi dkk. | Basis empiris terbatas, bukti prospektif jarang; klaim = pembangkit hipotesis | 1, 6 | "the empirical base remains limited; prospective evidence is sparse"; "should be read as hypothesis-generating rather than confirmatory" |
| Ijadi Maghsoodi dkk. | Beban lapisan simbolik: akuisisi pengetahuan, ontologi, konflik aturan, pemeliharaan | 1, 9 | "knowledge acquisition, ontology misalignment, rule conflict, and maintenance overhead"; "Symbolic layers require curation, versioning, adjudication, and retirement" |
| Ijadi Maghsoodi dkk. | Rekaman nonbahasa Inggris dikecualikan; literatur terkonsentrasi di sistem berpendapatan tinggi dan matang digital | 2, 9 | "non-English records"; "high-income, digitally mature health systems" |

### Lampiran B. Matriks catatan literatur (bahan untuk subbab II.8)

| Penulis, tahun | Data | Metode | Hasil utama | Celah terhadap penelitian ini |
|---|---|---|---|---|
| Kumar dkk., 2026 (bagian 6.1) | Sintesis dari tinjauan 153 studi | Tinjauan sistematis (bagian ini naratif, bersandar pada karya lain) | Aturan dapat diprediksi dan mudah divalidasi, tetapi tidak dapat diskalakan | Pernyataan sekunder; tanpa perbandingan kuantitatif aturan vs hibrida |
| Domingues, 2026 | 23 pedoman, 1.236 aturan, 10 laporan kasus | Basis aturan JSON dengan mesin inferensi *forward-chaining* | Jejak pembenaran per rekomendasi; uji kelayakan teknis | Hanya lapisan aturan (belum hibrida); onkologi prostat; bukan audit dokumentasi; sampel 10 kasus |
| Ijadi Maghsoodi dkk., 2026 | 101 sumber dari 3.892 rekaman | Tinjauan naratif kritis | Hibrida paling kredibel pada validasi dokumentasi dan tugas terbatas; bukti prospektif jarang | Konseptual; sumber nonbahasa Inggris dikecualikan; bukan perbandingan aturan vs aturan+AI |

### Lampiran C. Catatan peringatan dan penandaan

1. **Maleki dkk. (J Health Organ Manag 2026) tidak tersedia.** Daftar sumber menyebutnya analog paling dekat dengan arsitektur aturan + AI untuk klaim asuransi dan "sangat layak dibaca penuh". Naskah hanya menyebut keberadaannya tanpa nama penulis dan tanpa isi, dan menandainya `[PERLU VERIFIKASI SUMBER]`. Bila PDF diunggah, II.4.3 sebaiknya diperbarui (perkiraan tambahan ± 0,3 halaman) karena bisa jadi pembanding paling relevan.
2. **Domingues tidak membuktikan sistem hibrida.** Daftar sumber menyebutnya "hybrid decision support system using rule-based and AI", tetapi artikelnya menyatakan sistem yang diuji hanya berbasis aturan dan "hybrid-ready" (hlm. 2); modul pembelajaran mesin direncanakan. Domainnya kanker prostat, bukan klaim atau dokumentasi. Naskah mengatakannya terang-terangan.
3. **Ketidakkonsistenan angka pada Domingues, sehingga angka kinerjanya tidak dipakai.** Abstrak dan pembahasan melaporkan kecocokan jalur terapi 0,80 (hlm. 1, 7), tetapi bagian hasil menyatakan sistem lulus pada 4 dari 10 kasus dan gagal pada 6 (hlm. 5). Abstrak juga melaporkan presisi, *recall*, dan F1, sedangkan pembahasan (hlm. 7) menyebut metrik itu sebagai perbaikan yang diusulkan atas evaluasi lulus/gagal. Naskah hanya memakai desain sistem, cakupan, dan keterbatasan.
4. **Ijadi Maghsoodi dkk. adalah tinjauan naratif kritis.** Penulisnya menyebut desainnya tidak menawarkan sintesis kuantitatif sistematis (hlm. 9). Argumen "validasi hibrida pada dokumentasi" ada di bagian dokumentasi yang dibuat model generatif (hlm. 7), bukan audit dokumen yang sudah ada; naskah menandainya sebagai argumen konseptual. Klaim bahwa sistem neuro-simbolik meningkatkan keterauditan dan akurasi pengenalan entitas pada catatan onkologi dan radiologi (hlm. 4) dikutip dari studi lain (rujukan 36 dan 37) dan tidak dipakai.
5. **Titik hubung yang tidak diklaim di naskah.** Ijadi Maghsoodi dkk. mensyaratkan lapisan simbolik disusun atau disetujui pemangku kepentingan (hlm. 4); Breakdown menyatakan aturan berstatus "tervalidasi" atau "perlu validasi" dan tim tidak menetapkan aturan klinis sendiri. Kesesuaian itu tampak menarik untuk Bab I atau III, tetapi tidak disebut di II.4 karena kesimpulan itu bergantung pada rancangan yang belum tertulis.
6. **Keputusan rancangan "pemeriksaan kode tidak bergantung pada keluaran LLM" belum diberi dasar komparatif di II.4.** Dasarnya ada di II.3 (Jaganathan dkk., ketahanan pengodean ICD otomatis; Hou dkk.) dan pada Soroush dkk. 2024 (rujukan Breakdown; PDF belum ada). Prinsip 9 (pilihan rancangan juga klaim) menuntut alasan, kriteria, dan *trade-off*; ini perlu dijembatani di II.8 atau Bab III.
7. **Kutipan sekunder dalam Kumar dkk. dan Chen dkk.** Pernyataan Kumar dkk. tentang skalabilitas bersandar pada Berge dkk. (2023) dan Withers dkk. (2025); pernyataan Chen dkk. tentang aturan bersandar pada Mowery dkk. dan Kate. Keduanya tidak ada di repo.
8. **Istilah yang perlu diverifikasi bentuk bakunya:** `dapat diskalakan`, `pembangkit hipotesis`, `model fondasi`, `jejak pembenaran`, `abstraksi`, `luaran` [PERLU VERIFIKASI BENTUK BAKU]. `*pipeline*` ditulis miring sebagai istilah asing; `dataset` mengikuti pemakaian di `RULES.md`.
9. **Penanda `[SESUAIKAN DENGAN BAB I]`** pada kalimat penutup II.4.3 harus disamakan dengan rumusan pertanyaan dan ukuran keberhasilan Bab I.
10. **Tahun rujukan:** Domingues terbit daring 14 Oktober 2025 dalam volume 206 tahun 2026; Ijadi Maghsoodi dkk. terbit daring 23 Juli 2026 (daftar sumber menyebut edisi Desember 2026). Daftar pustaka memakai 2026 untuk keduanya, mengikuti volume; **[PERLU VERIFIKASI SUMBER]** untuk tahun final.
