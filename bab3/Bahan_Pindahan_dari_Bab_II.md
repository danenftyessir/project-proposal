# Bahan yang dipindahkan dari Bab II (draf 5) ke Bab I dan Bab III

> **Status:** `DRAF`, bahan mentah. Disalin apa adanya dari `bab2/II.1`–`II.8_*.md` pada 3 November 2026, ketika Bab II direvisi sesuai notulensi bimbingan ("Bab II hanya berisi karya orang lain; sintesis, celah, dan posisi penelitian dipindahkan ke Bab I; analisis kecocokan dan perbandingan ke Bab III").
>
> **Perhatian sebelum dipakai:**
> - Nomor subbab di dalam teks (II.1, II.3, dst.) merujuk ke struktur **lama**. Sesuaikan dengan `bab2/Bab_II_Revisi_Notulensi.md`.
> - Sebagian sumber yang dirujuk di sini tidak lagi dibahas di Bab II revisi (daftar di bagian C catatan revisi Bab II). Sumber yang dipakai di Bab I atau Bab III tetap harus ada di Daftar Pustaka.
> - Klaim "tidak ada sumber yang..." hanya berlaku untuk 39 sumber draf lama, bukan seluruh literatur.
> - Penanda `[SESUAIKAN DENGAN BAB I]` dan `{{...}}` berasal dari draf lama.
>
> **Saran penempatan:** paragraf celah (bagian A) ke Bab I (latar belakang atau rumusan masalah); Tabel perbandingan (bagian B) ke Bab III (analisis solusi), dengan rujukan ke subbab Bab II yang membahas tiap karya.

---

## A. Paragraf sintesis, celah, dan posisi penelitian

### Dari II.1_Dokumentasi_Klinis_dan_Klaim_JKN.md — II.1.2 Sintesis dan Celah

Dokumentasi medis, kode diagnosis, dan keputusan klaim saling terkait dalam JKN, tetapi tidak satu pun sumber di atas mengukur ketidaksesuaian di dalam dokumen klinis sebelum klaim diajukan. Ulasan Simbolon dan Gani (2023) merangkum faktor penyebab dari artikel lain, Rachmawaty dkk. (2021) menganalisis biaya dan mutu layanan, Barsasella dkk. (2021) memodelkan luaran pasien dari variabel klaim terstruktur, dan Nilasari dan Soelistijanto (2026) merancang audit di sisi BPJS tanpa evaluasi. Ringkasan Muroli dkk. (2020) dalam ulasan itu memberi proporsi berkas yang tidak lengkap atau tidak tepat, tetapi tidak merinci jenis ketidaksesuaian antardokumen, misalnya diagnosis pada resume yang tidak sejalan dengan catatan harian.


### Dari II.2_NLP_dan_LLM_pada_Teks_Klinis.md — II.2.4 Sintesis dan Celah

Kesepuluh sumber menunjukkan bahwa PLM dan LLM telah luas dipakai pada teks klinis, tetapi bukti yang tersedia memiliki tiga keterbatasan bagi penelitian ini. Pertama, tidak ada sumber yang mengevaluasi teks klinis berbahasa Indonesia, dan sebagian menyebut dominasi bahasa Inggris pada penelitian di bidangnya (Chen dkk., 2026, hlm. 8; Kumar dkk., 2026, hlm. 21). Kedua, bukti tentang LLM pada dokumentasi klinis berpusat pada pembuatan dokumen, bukan pemeriksaan kesesuaian antardokumen (Woo dkk., 2026, hlm. 1), dan hasilnya tidak seragam: halusinasi ditemukan pada 40% ringkasan pulang dalam satu studi (Schwieger dkk., 2024, hlm. 1), sedangkan penilai pada studi lain tidak menemukannya (Mehri dkk., 2026, hlm. 9). Ketiga, hasil disambiguasi singkatan yang dikaji di sini berasal dari satu dataset berbahasa Inggris dan turun dari akurasi 0,9228 menjadi 0,7585 pada versi yang memuat lebih banyak derau (Wei dkk., 2026, hlm. 1, 5, 9). Karena itu, kinerja teknik-teknik ini pada rekam medis rawat inap kebidanan dan anak berbahasa Indonesia tidak dapat diasumsikan dan harus diukur langsung pada data tersebut [SESUAIKAN DENGAN BAB I: rumusan pertanyaan dan ukuran keberhasilan].


### Dari II.3_Audit_Otomatis_Dokumentasi_dan_Kode_Diagnosis.md — II.3.4 Sintesis dan Posisi Penelitian

Dua studi yang membedakan kategori kesalahan menunjukkan pola yang sama: pemeriksaan otomatis lebih baik pada kesalahan eksplisit dalam satu dokumen daripada pada kesalahan yang menuntut penilaian klinis. Pada Dietrich dan Stubbert (2026, hlm. 98), ketidaksesuaian temuan klinis memiliki *recall* terendah, dan pada Skrabic dkk. (2026, hlm. 4), kategori diagnostik dan pemeriksaan penunjang paling sulit.

Seluruh kategori yang diuji berada di dalam satu dokumen. Dietrich dan Stubbert (2026, hlm. 96–97) menguji lima kategori pada satu catatan pemulangan, antara lain ketidaksesuaian waktu kunjungan dan hasil pemeriksaan penunjang abnormal yang diabaikan atau dikontradiksi pada penilaian atau rencana. Ketidaksesuaian diagnosis atau kode diuji terhadap label klinisi (Du dkk., 2026) dan terhadap penelusuran rekam medis (Mwogosi & Mambile, 2026), bukan antara dua dokumen klinis dalam satu episode rawat inap. Perbedaan diagnosis antara catatan perkembangan harian dan resume medis, ketidaksesuaian temporal antardokumen, serta hasil pemeriksaan yang tidak ditindaklanjuti pada dokumen lain termasuk jenis yang direncanakan ditangani komponen AI/NLP dalam penelitian ini [SESUAIKAN DENGAN BAB I]. Jenis-jenis itu perlu didefinisikan dan dievaluasi terpisah, karena kinerja pada satu jenis tidak mewakili jenis lain.

Bukti tentang positif palsu (*false positive*) belum seragam. Hanya Dietrich dan Stubbert (2026, hlm. 95) menyertakan catatan tanpa kesalahan, sebanyak 100 catatan. Skrabic dkk. (2026, hlm. 6) tidak menyertakannya, dan Du dkk. (2026, hlm. 7, 12) menilai selisih terhadap label klinisi yang sendiri dapat mengandung derau, sehingga angka presisi ketiga studi tidak sebanding. Ketidakstabilan satu model klasifikasi kode terhadap akronim dan salah ketik (Jaganathan dkk., 2025, hlm. 4–5) menunjukkan bahwa ketahanan terhadap variasi penulisan, termasuk singkatan lokal, perlu diuji secara khusus, meskipun hasilnya belum tentu berlaku bagi LLM.

Di antara keenam studi, tidak ada yang melaporkan data dari Indonesia, membandingkan catatan perkembangan harian dengan ringkasan akhir dalam satu episode rawat inap, atau mengambil pedoman sesuai kasus sebagai dasar temuan. Karena itu, angka kinerja yang dilaporkan tidak dapat dipindahkan begitu saja ke dokumentasi rawat inap kebidanan dan anak di Indonesia, dan kinerja harus diukur ulang dengan menyertakan dokumen tanpa ketidaksesuaian agar positif palsu dapat dihitung.


### Dari II.4_Pendekatan_Hibrida_Berbasis_Aturan_dan_AI-NLP.md — II.4.3 Sintesis dan Celah

Dukungan literatur berbeda menurut tiga pernyataan. Pertama, aturan eksplisit menghasilkan pemeriksaan yang dapat diprediksi dan ditelusuri, tetapi mahal dipelihara (Kumar dkk., 2026, hlm. 12; Domingues, 2026, hlm. 2, 7). Kedua, komponen AI/NLP dapat menemukan sebagian ketidaksesuaian yang tidak berbentuk aturan eksplisit, dengan kinerja lebih rendah pada kategori yang menuntut penilaian klinis (II.3). Ketiga, kombinasi keduanya dinilai paling kredibel untuk validasi dokumentasi, tetapi hanya sebagai argumen konseptual pada satu tinjauan naratif (Ijadi Maghsoodi dkk., 2026, hlm. 1, 7), sehingga peningkatan mutu audit oleh kombinasi itu masih berupa hipotesis. Hipotesis ini belum teruji pada tugas yang dikerjakan: di antara sumber yang dibaca, tidak ada yang membandingkan aturan saja dengan aturan ditambah AI/NLP pada audit dokumentasi klinis, dan satu-satunya sistem yang diuji (Domingues, 2026) hanya berbasis aturan, di bidang onkologi, pada sepuluh kasus. Selain itu, tidak ada sumber yang menyangkut aturan atau dokumen klaim berbahasa Indonesia.{{ Satu artikel pada daftar sumber, yang judulnya menyebut model hibrida pembelajaran mesin dan sistem pakar untuk identifikasi pemotongan klaim asuransi, belum dapat dibaca karena berkasnya tidak tersedia [PERLU VERIFIKASI SUMBER].}} Pembagian kerja antara aturan dan AI/NLP pada penelitian ini karenanya merupakan pilihan rancangan yang perlu dibenarkan lewat perbandingan konfigurasi aturan saja dengan aturan ditambah AI/NLP [SESUAIKAN DENGAN BAB I: rumusan pertanyaan dan ukuran keberhasilan].


### Dari II.5_RAG_Penjangkaran_Bukti_dan_Halusinasi.md — II.5.4 Sintesis dan Celah

Manfaat *retrieval* baru ditunjukkan untuk ekstraksi pada catatan klinis, dan keterlacakan keluaran terhadap sumbernya baru didemonstrasikan pada contoh yang terbatas, sehingga ada lima celah bagi penelitian ini. Pertama, aplikasi RAG terkonsentrasi pada tanya jawab, pembuatan laporan, peringkasan, dan ekstraksi (R. Yang dkk., 2026, hlm. 2), dan bukti kinerja yang paling mencolok berasal dari soal ujian (Jia dkk., 2026, hlm. 2); di antara sumber yang dibaca, tidak ada yang menguji RAG untuk memeriksa kesesuaian antardokumen dalam satu episode rawat. Kedua, tidak ada sumber yang menguji teks klinis berbahasa Indonesia, dan *retrieval* umumnya memakai model berpusat pada bahasa Inggris (R. Yang dkk., 2026, hlm. 4; Landolsi dkk., 2026, hlm. 19). Ketiga, pemeriksaan keluaran terhadap sumber baru didemonstrasikan pada ringkasan LLM atas rekam medis berbahasa Inggris (Zeba dkk., 2026), sedangkan ketepatan kutipan pada Li dkk. (2026) dinilai ahli. Keempat, kontribusi *retrieval* dibandingkan dengan kondisi tanpa *retrieval* hanya pada dua tugas ekstraksi berbasis skema (Zhang dkk., 2026, hlm. 6, 11); pada audit, kontribusinya terhadap mutu temuan dan biaya positif palsunya belum diukur. Kelima, KG dipakai untuk memverifikasi penalaran pada soal medis (Sun dkk., 2027, hlm. 1, 15) dan memprediksi kejadian pada satu penyakit (Y. Yang dkk., 2026, hlm. 1, 2), bukan memeriksa kesesuaian antardokumen, dan manfaatnya tidak dibandingkan dengan *retrieval* tanpa graf. Karena itu, manfaat RAG pada audit dokumentasi rawat inap kebidanan dan anak perlu diuji terhadap pembanding yang ditetapkan sebelum eksperimen [SESUAIKAN DENGAN BAB I: rumusan pertanyaan dan ukuran keberhasilan; celah keempat hanya terjawab bila konfigurasi aturan + LLM tanpa *retrieval* ikut dijalankan, padahal Breakdown menjadikannya opsional]. Dalam penelitian ini, KG berkedudukan sebagai calon pendekatan pendukung, bukan komponen inti, karena manfaatnya untuk pemeriksaan antardokumen belum ditunjukkan pada sumber yang ditelaah, penyelesaian KG oleh LLM di bidang kesehatan memerlukan validasi pakar klinis (Syeda & Reddy, 2026, hlm. 18), dan cakupan graf yang kurang dapat membuat penalaran yang berisiko lolos tanpa ditandai (Sun dkk., 2027, hlm. 15). Pemakaian KG diputuskan melalui uji kelayakan, dan manfaatnya baru diklaim bila konfigurasi dengan graf telah dibandingkan dengan konfigurasi tanpa graf.


### Dari II.6_Deidentifikasi_untuk_Layanan_AI_Eksternal.md — II.6.2 Sintesis dan Celah

Dua hal didukung secara terbatas: de-identifikasi oleh LLM lokal dapat memisahkan data sensitif dari LLM publik pada pengujian awal, dan penggantian yang memperhatikan utilitas mengurangi kehilangan kinerja pada tugas hilir berbasis kode. Bukti itu memiliki tiga keterbatasan. Pertama, tidak ada sumber yang menguji teks klinis berbahasa Indonesia atau pengenal khas Indonesia seperti NIK dan nomor rekam medis; temuan tentang nama Asia Tenggara bersifat sekunder dan menyangkut perkakas yang diuji pada data lain (Faustini dkk., 2026, hlm. 5). Kedua, bukti untuk pendekatan berbasis LLM lokal berasal dari data sintetis dan catatan berbahasa Inggris yang sudah dide-identifikasi (Azzam dkk., 2026, hlm. 15), sehingga kebocoran PHI pada catatan baru yang belum diredaksi belum terukur. Ketiga, kehilangan utilitas baru diukur pada asosiasi kode ICD-10 (Tchouka dkk., 2024, hlm. 13) atau pada sebutan obat dan dosis (Azzam dkk., 2026, hlm. 12); dampak de-identifikasi terhadap temuan audit yang bergantung pada tanggal, dosis, dan urutan waktu belum diukur. De-identifikasi pada penelitian ini perlu diuji pada data berbahasa Indonesia, dengan ukuran kebocoran pengenal dan dampaknya pada mutu temuan [SESUAIKAN DENGAN BAB I: rumusan pertanyaan dan ukuran keberhasilan].


### Dari II.7_Evaluasi_Sistem_NLP_Klinis.md — II.7.2 Sintesis dan Celah

Kedua sumber menunjukkan bahwa acuan penilaian perlu dirancang dan diukur, bukan diasumsikan: kesepakatan antarpenilai dapat diukur dengan ambang yang ditetapkan sebelumnya (Becker dkk., 2025, hlm. 2), dan ketidaksepakatan antarmanusia dapat mencapai 29,0% pada ekstraksi klinis (van Koevorden dkk., 2026, hlm. 4). Namun, ada tiga keterbatasan. Pertama, keduanya mengevaluasi ekstraksi entitas atau nilai dari satu dokumen, bukan temuan ketidaksesuaian antardokumen. Kedua, teks yang dievaluasi berbahasa Jerman dan Belanda (Becker dkk., 2025, hlm. 2; van Koevorden dkk., 2026, hlm. 7), bukan Indonesia, dan van Koevorden dkk. membatasi generalisasi pada satu pusat rujukan tersier (hlm. 8). Ketiga, hanya Becker dkk. yang mengukur kesepakatan antarpenilai secara formal; pada van Koevorden dkk. jumlah penilai manusia terlalu kecil untuk estimasi itu. Akibatnya, evaluasi audit dokumentasi perlu menetapkan unit temuan, perlakuan kasus ambigu, ukuran kesepakatan penilai, serta ukuran dan ambang kegagalan sebelum eksperimen; acuan yang ditetapkan satu penilai tidak dapat memperkirakan variabilitas antarpenilai. Metrik ekstraksi juga tidak dapat dipindahkan langsung sebagai ukuran keberhasilan audit, karena temuan yang masuk akal secara semantik harus didukung bukti dari episode pasien yang tepat, dan ketepatan menemukan satu masalah perlu dibaca bersama jumlah temuan yang bukan masalah [SESUAIKAN DENGAN BAB I: rumusan pertanyaan dan ukuran keberhasilan].

Ketepatan dan kelengkapan temuan audit diukur dengan presisi (P), *recall* (R), dan F1 (Domingues, 2026, hlm. 3):

$$P=\frac{TP}{TP+FP},\qquad R=\frac{TP}{TP+FN},\qquad F_1=\frac{2PR}{P+R}\qquad\text{(II.2)}$$

dengan TP temuan yang dinilai benar oleh tenaga ahli, FP temuan yang dinilai tidak benar atau tidak relevan, dan FN ketidaksesuaian pada acuan yang tidak ditemukan sistem; keluaran “bukti belum cukup” dan temuan yang belum dapat dinilai dilaporkan terpisah [SESUAIKAN DENGAN BAB I/III: definisi operasional unit temuan dan label tenaga ahli mengikuti Breakdown bagian Evaluasi]. Bila jumlah temuan antarkategori timpang, macro-F1, yaitu rata-rata sederhana F1 per kategori, lebih mencerminkan kinerja pada kategori yang jarang (Hou dkk., 2024, hlm. 6). Untuk C kategori ketidaksesuaian, ukuran itu dihitung sebagai

$$\text{macro-}F_1=\frac{1}{C}\sum_{c=1}^{C}F_{1,c}\qquad\text{(II.3)}$$



## B. Tabel perbandingan dan celah penelitian (II.8 lama)



### Perbandingan Karya Terdahulu

Karya yang paling dekat dengan masalah penelitian ini pada tiap tema subbab sebelumnya dirangkum pada Tabel II.1, lengkap dengan halaman sumber pada kolom pertama.

Tabel II.1. Perbandingan karya terdahulu yang terdekat dengan penelitian ini

| Karya | Data dan metode | Hasil utama | Keterbatasan bagi penelitian ini |
| --- | --- | --- | --- |
| Simbolon & Gani (2023, hlm. 72, 77) | Ulasan lima artikel tentang klaim rawat inap JKN yang *pending* | Pengodean tidak sesuai, berkas tidak lengkap, dan beda diagnosis DPJP–verifikator | Ringkasan sekunder; jenis ketidaksesuaian antardokumen tidak dirinci |
| Dietrich & Stubbert (2026, hlm. 95–98, 100) | 600 catatan pemulangan IGD (MIMIC-IV-ED); empat LLM | Akurasi 93,2–94,2%; temuan klinis tersulit | 500 dari 600 catatan bersisipan kesalahan; satu dokumen; tanpa pedoman |
| Skrabic dkk. (2026, hlm. 1–2, 4, 6) | 102 laporan IGD; tiga model penalaran vs tiga dokter | Lokasi benar 65,7–79,2% vs dokter 48,0% | Tanpa catatan bebas kesalahan, sehingga positif palsu tidak terukur |
| Jaganathan dkk. (2025, hlm. 3–4) | 3.372 catatan MIMIC-III; pengujian metamorfik pada model pengodean ICD | Lima kode teratas berubah pada 70–81% catatan | Satu model; mengukur stabilitas, bukan kebenaran |
| Wei dkk. (2026, hlm. 1, 5, 9) | Disambiguasi singkatan; dataset CASI berbahasa Inggris | Akurasi 0,9228 (bersih) dan 0,7585 (asli) | Satu tolok ukur Inggris; bergantung pada inventori makna |
| Ijadi Maghsoodi dkk. (2026, hlm. 1, 4, 7); Domingues (2026, hlm. 1–2) | Tinjauan naratif hibrida; sistem berbasis aturan untuk onkologi prostat | Hibrida paling kredibel pada validasi dokumentasi; bukti prospektif jarang | Konseptual; yang diuji hanya aturan; tanpa perbandingan aturan vs aturan + AI |
| Zhang dkk. (2026, hlm. 1, 5–6, 11) | RAG pada catatan perawatan lansia; Llama 3.1 8B | F1 jawaban 0,702/0,722 menjadi 0,946/0,953 | Dua tugas ekstraksi berbasis skema; tanpa penalaran temporal |
| Zeba dkk. (2026, hlm. 1, 10, 15) | Pemeriksa fakta tanpa LLM; 3.786 proposisi MIMIC-III | Presisi 0,8904; *recall* 0,8234; F1 0,8556 | Bahasa Inggris, ICU; vonis biner |
| Azzam dkk. (2026, hlm. 1, 12, 15, 19) | Anonimisasi oleh LLM lokal; data sintetis dan MIMIC-III | Presisi 1,000 dan *recall* 0,936 (sintetis) | Hanya bahasa Inggris; data sintetis atau sudah diredaksi |
| van Koevorden dkk. (2026, hlm. 1, 4, 7–8) | Ekstraksi LLM vs konsensus dua dokter; 60 pasien | Akurasi 74–90%; beda dokter–dokter 29,0% | Ekstraksi nilai; bahasa Belanda; satu pusat |

### Celah Penelitian

Dari 39 sumber yang dirujuk dalam bab ini, empat celah berulang. Pertama, tidak ada studi NLP atau AI yang menguji teks klinis berbahasa Indonesia, termasuk singkatan dan pengenal lokalnya (subbab II.2, II.3, II.6); studi pembelajaran mesin pada data Indonesia dalam sumber ini, yaitu Barsasella dkk. (2021), memakai variabel klaim terstruktur (II.1). Kedua, tidak ada yang memeriksa kesesuaian antardokumen dalam satu episode rawat inap sebelum klaim diajukan, misalnya membandingkan catatan perkembangan harian dengan ringkasan akhir atau memakai pedoman sebagai dasar temuan (II.1, II.3, II.5); pemeriksaan ringkasan terhadap rekam medis sumber baru ada pada ringkasan buatan LLM berbahasa Inggris (Zeba dkk., 2026), bukan pada resume yang ditulis dokter (II.5.2). Ketiga, di antara sumber yang dibaca, tidak ada yang membandingkan konfigurasi aturan saja dengan aturan ditambah AI/NLP berbasis RAG pada tugas ini, dan ketepatan kutipan bukti belum diperiksa secara otomatis (II.4, II.5); manfaat graf pengetahuan untuk audit antardokumen juga belum diuji (II.5.3). Keempat, acuan penilaian untuk audit, yaitu unit temuan, perlakuan kasus ambigu, dan ukuran kesepakatan penilai, belum dirancang pada sumber mana pun, padahal ketidaksepakatan antarpenilai dapat mencapai 29,0% pada ekstraksi klinis (II.7). Pernyataan "tidak ada" ini berlaku pada 39 sumber tersebut, bukan pada seluruh literatur. Penelitian ini mengisi celah itu dengan menguji audit dokumentasi rawat inap kebidanan dan anak berbahasa Indonesia terhadap pembanding, ukuran, dan ambang kegagalan yang ditetapkan sebelum eksperimen [SESUAIKAN DENGAN BAB I: rumusan pertanyaan dan ukuran keberhasilan].


