## II.3 Pemeriksaan Dokumentasi Klinis dengan Model Bahasa Besar

### II.3.1 Deteksi Kesalahan pada Dokumentasi Klinis

Dietrich dan Stubbert (2026) mengevaluasi empat model bahasa besar (large language model, LLM) untuk mendeteksi kesalahan dalam catatan pemulangan instalasi gawat darurat (IGD). Penelitian menggunakan 600 kunjungan dari basis data MIMIC-IV-ED. Sebanyak 500 catatan masing-masing disisipi satu kesalahan dari lima kategori, sedangkan 100 catatan lainnya tidak memuat kesalahan. Rancangan ini memungkinkan evaluasi terhadap kemampuan model mengenali catatan yang mengandung kesalahan maupun catatan tanpa kesalahan.

Hasil evaluasi menunjukkan bahwa akurasi deteksi kesalahan apa pun berkisar 93,2–94,2%, dengan presisi 98,3–99,1% dan spesifisitas 92,0–96,0%. Kinerja model berbeda menurut kategori. Ketidaksesuaian identitas atau waktu kunjungan serta kesalahan obat dan alergi dapat dideteksi dengan nilai F1 sekurang-kurangnya 0,96. Sebaliknya, ketidaksesuaian antara tanda vital atau pemeriksaan fisik dan interpretasi naratif menjadi kategori yang paling sulit dideteksi, dengan nilai F1 sebesar 0,75–0,84. Penurunan tersebut terutama disebabkan oleh rendahnya recall.

Penelitian ini menunjukkan bahwa kinerja pemeriksaan dokumentasi dapat berbeda menurut jenis kesalahan yang diperiksa. Namun, terdapat batasan pada rancangan evaluasinya. Kesalahan disisipkan oleh peneliti, data berasal dari satu institusi, dan catatan yang dinilai berupa satu dokumen yang disusun dari elemen data terstruktur pada kunjungan tersebut. Penulis menyebut kerangka audit berbasis agen yang mengambil pedoman dan memeriksa konsistensi lintas dokumen sebagai arah penelitian lanjutan (hlm. 100). Dengan demikian, penelitian tersebut memberikan contoh evaluasi deteksi kesalahan pada dokumentasi klinis, sekaligus menunjukkan bahwa hasil dari satu dokumen belum menjawab persoalan pemeriksaan konsistensi lintas dokumen.

### II.3.2 Pemeriksaan Fakta Keluaran terhadap Rekam Medis Sumber

Zeba dkk. (2026) mengembangkan modul pemeriksa fakta tanpa menggunakan LLM untuk memeriksa keluaran model terhadap rekam medis sumber. Pendekatan tersebut memecah ringkasan dan rekam medis menjadi proposisi atomik, yaitu satuan pernyataan terkecil yang dapat dinilai dukungannya secara mandiri. Setiap proposisi kemudian diberi vonis Didukung atau Tidak Didukung berdasarkan sejumlah pemeriksaan, yaitu negasi, implikasi, konsistensi temporal, eksklusivitas bersama, kecocokan numerik, dan keberadaan informasi dalam sumber.

Pada 104 ringkasan yang diekstrak menjadi 3.786 proposisi dan divalidasi oleh dokter, modul tersebut mencapai presisi 0,8904, recall 0,8234, dan F1 0,8556. Data penelitian berasal dari MIMIC-III. Penulis menyatakan bahwa sistem kurang andal pada bidang yang kurang terwakili dalam data, termasuk gangguan metabolik anak. Selain itu, keluaran modul terbatas pada vonis biner dan belum memberikan usulan perbaikan terhadap proposisi yang tidak didukung (hlm. 1, 10, 15).

Penelitian tersebut memberikan contoh pemeriksaan fakta pada tingkat proposisi dengan membandingkan informasi yang dihasilkan model terhadap sumber rekam medis. Relevansinya terhadap penelitian ini terletak pada pembahasan cara memeriksa dukungan informasi dari dokumen sumber. Namun, penelitian Zeba dkk. tidak secara langsung mengevaluasi kesesuaian antara CPPT dan resume medis dalam satu episode pelayanan.
