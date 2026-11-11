## II.5 Tata Kelola dan Privasi Penggunaan AI Klinis

### II.5.1 Pengaturan dan Tata Kelola Penggunaan AI di Indonesia

Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi menggolongkan data dan informasi kesehatan sebagai data pribadi yang bersifat spesifik (Pasal 4 ayat 2, hlm. 5). Penjelasannya menyebut bahwa pemrosesan data tersebut dapat menimbulkan dampak lebih besar bagi subjek data, antara lain diskriminasi (hlm. 38). Permenkes 24/2022 mewajibkan seluruh pihak yang memiliki akses terhadap data pasien, termasuk tenaga yang berkaitan dengan pembiayaan dan badan hukum, menjaga kerahasiaan isi rekam medis (Pasal 32, hlm. 14–15).

Dalam sumber yang ditelaah pada naskah ini, belum ditemukan peraturan yang secara khusus mengatur penggunaan AI di bidang kesehatan. Fitriasari dan Umasugi (2026) membahas risiko penerapan AI pada rumah sakit, puskesmas, penyedia telemedisin, dan asuransi sebelum tersedia pengaturan yang memadai mengenai validasi, pemantauan, dan akuntabilitas. Mereka mengusulkan klasifikasi risiko berdasarkan kasus penggunaan, validasi lokal, serta mekanisme akuntabilitas algoritmik. Pembahasan tersebut menempatkan kesiapan kebijakan dan tata kelola sebagai persoalan yang perlu diperhatikan dalam penerapan AI pada sistem kesehatan Indonesia.

Pemberitaan CNBC Indonesia pada 30 Oktober 2026 menyebut bahwa rancangan peraturan presiden mengenai etika AI masih berada dalam proses penandatanganan. Pernyataan tersebut menggambarkan status yang diberitakan pada tanggal publikasi sumber dan tidak diperlakukan sebagai status regulasi terkini tanpa pemeriksaan lebih lanjut.

### II.5.2 Rekomendasi Penggunaan LLM dalam Konteks Klinis dan Administratif

European Society for Medical Oncology (ESMO) menyusun panduan ELCAP melalui telaah literatur dan proses Delphi yang melibatkan 20 pakar pada periode November 2024 sampai Februari 2025 (Wong dkk., 2025). Setiap pernyataan dalam panduan dinilai oleh pakar menggunakan skala 1–9. Panduan tersebut membagi penggunaan LLM menjadi tiga tipe: tipe 1 untuk aplikasi bagi pasien, tipe 2 untuk aplikasi bagi tenaga kesehatan, dan tipe 3 untuk sistem institusional yang berjalan di latar belakang. Ekstraksi data dan sistem peringatan merupakan contoh penggunaan tipe 3.

Untuk penggunaan tipe 2, tenaga kesehatan diminta memverifikasi informasi yang disarankan AI terhadap pedoman, studi yang telah ditelaah sejawat, atau konsensus pakar. Pengawasan manusia tetap diperlukan untuk keputusan klinis kritis. Tenaga kesehatan tidak boleh menyerahkan tanggung jawab akhir atas diagnosis atau rencana terapi kepada LLM, menganggap keluarannya selalu benar, atau mengunggah data pasien sensitif ke platform eksternal tanpa keamanan yang ketat dan persetujuan institusi serta pasien (pernyataan 2.1–2.7, hlm. 1449).

Untuk penggunaan tipe 3, ELCAP meminta dokumentasi rekam medis dipastikan lengkap dan akurat, proses ekstraksi divalidasi, kinerja sistem dipantau secara berkelanjutan, dan staf dilatih untuk mempertanyakan temuan yang mencurigakan. Panduan tersebut juga tidak mendukung penggantian tinjauan manusia dengan keluaran otomatis untuk tugas kritis, validasi yang hanya dilakukan satu kali, atau penerapan sistem tanpa evaluasi dampak terhadap proses klinis (pernyataan 3.1–3.8, hlm. 1449). ELCAP menyebut bahwa LLM dapat membantu pengodean dan penagihan, tetapi model umum memiliki keterbatasan pengetahuan domain, kerentanan terhadap kesalahan, dan kebutuhan penyesuaian terhadap aturan penjamin (hlm. 1453).

American Health Information Management Association (AHIMA) (2024) mewawancarai sepuluh organisasi penyedia layanan, penjamin, vendor, dan konsultan hukum mengenai penggunaan alat AI untuk pekerjaan nonklinis. Penerapan yang telah digunakan atau sedang diuji mencakup pengodean berbantuan komputer, penjaminan mutu rekam medis, serta tinjauan klaim sebelum penagihan. Narasumber menekankan bahwa data dalam rekam medis tetap harus diautentikasi dan integritas dokumentasi harus diutamakan. Organisasi juga perlu membangun tata kelola yang memadai untuk penggunaan alat AI.

Dokumen AHIMA merupakan ringkasan isu berbasis wawancara dan tidak melalui proses telaah sejawat. Meskipun demikian, pembahasannya memberikan konteks mengenai penggunaan AI untuk pekerjaan administratif kesehatan, termasuk penjaminan mutu rekam medis dan tinjauan klaim. Kedua sumber tersebut dirangkum pada Tabel II.2.

Tabel II.2. Ringkasan rekomendasi penggunaan LLM di bidang klinis dan administratif

| Aspek | Wong dkk. (2025), ESMO ELCAP | AHIMA (2024) |
|---|---|---|
| Dasar penyusunan | Tinjauan literatur dan Delphi dengan 20 pakar bidang onkologi | Wawancara terhadap 10 organisasi |
| Penggunaan yang dibahas | Aplikasi untuk pasien, tenaga kesehatan, serta sistem institusional; termasuk ekstraksi data dan sistem peringatan | Pengodean berbantuan komputer, penjaminan mutu rekam medis, dan tinjauan klaim sebelum penagihan |
| Tanggung jawab dan verifikasi | Informasi AI diverifikasi; tanggung jawab akhir keputusan klinis tetap pada tenaga kesehatan | Data rekam medis tetap harus diautentikasi |
| Perlindungan data | Data sensitif tidak diunggah ke platform eksternal tanpa keamanan dan persetujuan | Kepatuhan terhadap aturan privasi |
| Pemantauan dan tata kelola | Validasi berkelanjutan, pemantauan kinerja, dan pelatihan staf | Tata kelola organisasi untuk penggunaan AI |

### II.5.3 Deidentifikasi Data Rekam Medis

Pedoman Office for Civil Rights dari Departemen Kesehatan Amerika Serikat (HHS Office for Civil Rights, 2012) menjelaskan dua metode deidentifikasi berdasarkan Health Insurance Portability and Accountability Act (HIPAA), yaitu Safe Harbor dan Expert Determination. Safe Harbor mensyaratkan penghapusan delapan belas jenis pengenal, termasuk nama, wilayah geografis yang lebih kecil daripada negara bagian, seluruh unsur tanggal selain tahun, nomor telepon, dan nomor rekam medis. Selain itu, pemegang data tidak boleh memiliki pengetahuan aktual bahwa informasi yang tersisa, baik secara sendiri maupun jika digabungkan dengan informasi lain, dapat mengidentifikasi pasien.

Metode Expert Determination menggunakan penilaian ahli terhadap risiko identifikasi dengan mempertimbangkan kemudahan data direplikasi, ketersediaannya di sumber lain, dan kemungkinan membedakan individu. Pedoman tersebut menjelaskan bahwa kedua metode tetap menyisakan risiko identifikasi yang sangat kecil, tetapi tidak nol. Ketentuan HIPAA tersebut merupakan acuan teknis dari Amerika Serikat dan tidak diposisikan sebagai dasar hukum yang berlaku di Indonesia.

NIST SP 800-188 (Garfinkel dkk., 2023) membedakan pengenal langsung dari quasi-identifier, yaitu atribut yang tidak mengidentifikasi seseorang secara langsung, tetapi dapat mengidentifikasi ketika digabungkan dengan atribut lain. Salah satu pendekatan yang dibahas adalah k-anonymity, yaitu setiap kombinasi nilai quasi-identifier harus dimiliki oleh sedikitnya \(k\) rekaman. Pedoman tersebut menjelaskan bahwa identifikasi quasi-identifier membutuhkan pengetahuan domain, sedangkan teks tidak terstruktur dalam data tabular memerlukan perhatian khusus. Untuk tanggal, pedoman membahas generalisasi ke tingkat tahun serta penggeseran seluruh tanggal dalam rekaman seorang individu menggunakan nilai acak yang sama.

Faustini dkk. (2026) menelaah 83 artikel mengenai deidentifikasi data klinis berbasis NLP yang diterbitkan pada periode 2015–2024. Sebagian besar penelitian menggunakan teks berbahasa Inggris karena keterbatasan dataset yang tersedia. Penulis juga mencatat bahwa metode berbasis aturan masih umum digunakan untuk bahasa selain Inggris. Tinjauan tersebut memberikan gambaran mengenai pendekatan deidentifikasi teks klinis dan keterbatasan ketersediaan sumber data lintas bahasa.

Pedoman HHS dan NIST memberikan acuan teknis mengenai penghapusan pengenal serta risiko identifikasi melalui kombinasi atribut, sedangkan tinjauan Faustini dkk. membahas penerapan NLP pada teks klinis. Dalam konteks penelitian ini, pembahasan tersebut berkaitan dengan perlindungan data rekam medis yang digunakan sebagai masukan. Kedua pedoman internasional tersebut tidak menggantikan kewajiban perlindungan data berdasarkan ketentuan yang berlaku di Indonesia.

Pembahasan dalam bab ini mencakup regulasi dan dokumentasi rekam medis, representasi serta standardisasi informasi klinis, penelitian mengenai pemeriksaan dokumentasi dengan model bahasa besar, mekanisme retrieval-augmented generation, serta tata kelola dan privasi penggunaan AI klinis. Analisis terhadap keterkaitan literatur tersebut dengan persoalan penelitian, identifikasi kesenjangan penelitian, dan penentuan posisi serta rancangan solusi dibahas pada Bab III.
