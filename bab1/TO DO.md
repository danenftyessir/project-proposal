# TO DO Bab I

**Status:** Bab I kini DRAF 24 (per 9 November 2026) dan **belum selesai**. Naskah masih memuat 60 penanda (dihitung ulang setelah revisi terbatas). Persetujuan tim dan pembimbing belum ada. Setelah QA atas DRAF 24, revisi terbatas menangani dua temuan HIGH: urutan penilaian syarat dan "tidak dapat dinilai", serta aturan deduplikasi penyatuan dan akibatnya pada presisi. Revisi itu juga menyelaraskan I.1 paragraf 22 dengan D-83 dan D-95. Revisi terbatas ini belum diperiksa ulang QA, dan temuan QA lainnya tetap OPEN.
Ini dokumen kerja untuk saya, anggota tim, dan pembimbing, **bukan** bagian naskah proposal.

**Tenggat:**

- Tenggat lunak ke pembimbing, 6 November 2026, sudah lewat.
- Tenggat final ke pusat: 10 November 2026.

**Istilah yang dipakai di bawah:**

- **CPPT** adalah catatan perkembangan pasien terintegrasi.
- **Resume medis** adalah ringkasan perawatan pasien yang disusun di akhir perawatan.
- **Pemeriksaan rule-based** adalah pemeriksaan dengan aturan yang ditulis secara eksplisit.
- **Pemeriksaan AI/NLP berbasis RAG** adalah pemeriksaan dengan model bahasa yang lebih dulu mengambil dokumen acuan sebelum menghasilkan jawaban. RAG adalah singkatan dari *retrieval-augmented generation*.
- **Komponen** berarti salah satu dari dua pemeriksaan di atas. **Kombinasi pemeriksaan** berarti gabungan keduanya.
- **Presisi** adalah bagian temuan sistem yang memang benar. **Recall** adalah bagian ketidaksesuaian sebenarnya yang berhasil ditemukan sistem.
- **Selisih minimum** adalah batas kenaikan presisi atau recall kombinasi atas tiap komponen. Bila dipakai, selisih ini menjadi bagian syarat kedua pertanyaan pertama.
- **Penanda** adalah catatan dalam kurung siku di naskah, misalnya [MENUNGGU KEPUTUSAN] atau [DATA BELUM TERSEDIA]. Penanda [MENUNGGU KEPUTUSAN TIM] memuat usulan saya yang belum disetujui tim.

Kode dalam kurung di akhir butir hanya untuk menelusuri catatan lengkap di folder `memory/`. Nomor D-87 sampai D-97 ditetapkan a13.

## 1. Ringkasan status per subbab

| Subbab | Status | Penanda | Keterangan singkat |
|---|---|---|---|
| I.1 Latar Belakang | DRAF | 14 | Celah dan posisi penelitian ada di paragraf 16–25. Sebutan "sumber yang ditelaah dalam proposal ini" didefinisikan di paragraf 8. Premis kedua tidak lagi mengandaikan CPPT dan resume medis sama-sama dikunci. |
| I.2 Rumusan Masalah | DRAF | 13 | Ambang, selisih minimum, satuan hitung, dan kondisi keabsahan ditetapkan tim sebelum pengujian, tetapi belum ditetapkan. Ada usulan hasil "tidak dapat dinilai". |
| I.3 Tujuan | DRAF | 9 | Ukuran keberhasilan mengikuti syarat di I.2, termasuk usulan hasil "tidak dapat dinilai". |
| I.4 Batasan | DRAF | 7 | Cakupan rawat jalan bersyarat. Batas penghitungan episode rawat inap mengikuti keterangan lisan RSIA yang belum terverifikasi. Kelengkapan empiris kedua komponen tidak diuji. |
| I.5 Metodologi | DRAF | 17 | Lima tahap. Kriteria ketersediaan dokumen rawat jalan sudah diusulkan. Jawaban pertanyaan pertama disusun di tahap kelima. |
| **Total** | | **60** | |

Catatan:

- DRAF 24 menghapus tiga penanda yang isinya kini dinyatakan dengan kalimat prosedural, lalu menambah tiga penanda: usulan kriteria ketersediaan dokumen rawat jalan, usulan aturan "tidak dapat dinilai", dan bentuk baku "benih tetap". Jumlahnya tetap 60.
- Dari 60 penanda, sebagian berisi usulan saya untuk butir tim. Usulan itu bukan keputusan tim.

## 2. Perlu diputuskan oleh saya, tim, atau pembimbing

### 2.1 Yang sudah saya putuskan, menunggu persetujuan pembimbing

Keputusan berikut berlingkup terbatas dan sudah dituangkan di naskah. Persetujuan pembimbing **belum** ada, jadi keputusan ini belum final.

- Penyusunan jawaban rumusan masalah digabung ke tahap evaluasi (tahap kelima); jumlah tahap tetap lima. (D-66)
- Penanda sumber pemeriksaan hibrida diperlakukan sebagai keterbatasan tetap, tanpa sumber hibrida. (D-67)
- Singkatan AI, NLP, dan RAG di I.2 dan I.5 diselaraskan dengan I.1. (D-68)
- Pembanding tetap hanya masing-masing komponen. Batas perbandingannya dinyatakan eksplisit: penelitian tidak menyimpulkan bahwa kombinasi lebih baik daripada pemeriksaan manual. (D-22, D-72)
- Istilah "penafsiran kontekstual" pada studi Dietrich dibedakan dari kriteria pemilihan kombinasi, tanpa menafsirkan kriteria itu. (D-73, D-83)
- Makna "saling melengkapi" dipersempit menjadi jenis pemeriksaan yang berbeda, dan kalimat lama tentang jawaban "tidak" diselaraskan dengan makna itu. (D-74, D-81)
- Kriteria pemilihan kombinasi dinyatakan terbuka sebagai motivasi rancangan. (D-75)
- Selisih minimum dimuat di I.2 sebagai bagian syarat kedua secara bersyarat, tanpa angka. (D-82)
- Kata "terbaik" dibatasi pada konfigurasi yang diuji. (D-84)
- Kalimat batas sumber menyebut cakupan "sumber yang ditelaah dalam proposal ini" dan menyatakan bahwa penelusurannya tidak sistematis. (D-85)
- Kalimat penutup I.1 paragraf 19 diperlakukan sebagai pengulangan celah pertama, bukan sebagai batas dukungan bagi kriteria. (D-86)

Dijawab penulis pada DRAF 24, menunggu persetujuan pembimbing:

- Arti "saling melengkapi" tetap seperti D-74. I.4 paragraf 7 kini menyatakan bahwa kelengkapan empiris di antara kedua komponen tidak diuji dan bergantung pada mekanisme kombinasi. Tim juga perlu menyetujui. (D-87; Q-B1-cm; F-A05-0152, F-A11-0038)
- Judul sementara diambil dari judul capstone baru di dokumen penyelarasan tim dan ditandai menunggu konfirmasi pembimbing. Persetujuan judul dan empat rumusan capstone tetap terbuka (lihat 2.3). (D-92; K2; Q-TEAM butir 9)
- Temuan Dietrich hanya menjadi latar. Temuan itu tidak dipakai sebagai pertimbangan rancangan dan tidak dipakai untuk mengualifikasi komponen capstone (I.1 paragraf 22, revisi terbatas, selaras dengan D-83). Kriteria pemilihan kombinasi bersifat umum dan tidak memasangkan kondisinya dengan komponen tertentu. I.5 menyatakan bahwa jawaban pertanyaan pertama disusun di tahap kelima setelah tahap pertama sampai keempat. Pemutus yang tercatat sebelumnya ialah saya, lalu pembimbing; pemutus ini belum dikonfirmasi. (D-95; F-A05-0142, F-A05-0144, F-A05-0148, F-A11-0032)
- Satu sebutan, "sumber yang ditelaah dalam proposal ini", didefinisikan di I.1 paragraf 8 sebagai sumber yang tercantum di daftar pustaka dan dihimpun tanpa penelusuran sistematis. Sebutan ini dipakai di I.1 paragraf 18–24. Alasan Zhang tidak dihitung sebagai dukungan sudah diperiksa pada PDF (hlm. 1 dan 5). Pemutus yang tercatat sebelumnya ialah saya, lalu pembimbing; pemutus ini belum dikonfirmasi. (D-96; Q-B1-cg; F-A07-0087, F-A09-0235)

### 2.2 Usulan saya untuk butir tim, menunggu persetujuan tim

Usulan berikut tercatat di naskah sebagai penanda [MENUNGGU KEPUTUSAN TIM] atau sebagai kalimat usulan. Persetujuan tim **belum** ada.

Dijawab penulis pada DRAF 24, menunggu persetujuan tim (dan pembimbing bila disebut):

- Ketersediaan dokumen rawat jalan dinilai saya di tahap pertama dengan kriteria tertulis dan per episode. Dokumen dinilai "ada" bila dokumen yang berperan seperti resume medis tersedia, dan "memadai" bila memuat unsur yang dapat dicocokkan dengan CPPT. Hasilnya dilaporkan ke tim. Penilaian ini bergantung pada batas rawat jalan di I.4 dan tidak independen. RSIA juga perlu memastikan bentuk dokumennya. (D-88; Q-B1-cn; F-A05-0157)
- Angka ambang, selisih minimum beserta bentuk dan operator batasnya, satuan hitung, dan kondisi keabsahan ditetapkan tim dan dicatat sebelum pengujian. Isinya belum ada (lihat 2.3). Pembimbing ikut menetapkan angka ambang. (D-89; D-19)
- Naskah tidak lagi mengandaikan CPPT dan resume medis sama-sama dikunci. Keterangan lisan RSIA lewat saya, yang belum terverifikasi, dicatat khusus untuk rawat inap: CPPT yang telah tercatat tidak dapat diubah, sedangkan resume medis masih dapat direvisi. Penghitungan per episode rawat inap berlangsung sejak pasien masuk sampai pasien keluar dan resume medis episode itu diajukan. RSIA masih perlu mengonfirmasi. (D-90; Q-B1-ba)
- Cakupan rawat jalan di I.4 bersyarat: CPPT dan dokumen yang berperan seperti resume medis, bila ada. Satuan hitung rawat jalan ditetapkan setelah bentuk dokumennya diketahui. Batas operasional rawat jalan tetap terbuka (lihat 2.3). (D-91; Q-B1-f; Q-TEAM butir 4)
- Aturan sebelum uji: syarat pertama (ambang) dinilai lebih dulu. Bila syarat pertama gagal, termasuk bila presisi kombinasi 0/0, jawabannya tetap "tidak". "Tidak dapat dinilai" hanya dipakai bila syarat pertama terpenuhi tetapi syarat kedua terhalang, yaitu bila presisi atau recall kedua komponen sudah mencapai nilai maksimum, kasus terlalu sedikit untuk perbandingan, atau penyebut recall 0. Jumlah minimum kasus ditetapkan tim setelah data agregat tersedia. Pemutus yang tercatat sebelumnya ialah tim dan pembimbing; pemutus ini belum dikonfirmasi. (D-93; F-A11-0015, F-A11-0016)
- Paket usulan untuk pertentangan antarusulan: (D-94; Q-B1-o, Q-B1-r, Q-B1-by, Q-B1-bz; F-A11-0023 sampai F-A11-0027, F-A05-0150)
  1. Satuan pengacakan dan satuan hitung ialah satu episode, tanpa mengubah pembagian data per pasien.
  2. Agregasi mikro dihitung atas episode.
  3. Nilai 0/0 "tidak terdefinisi" menghasilkan "tidak dapat dinilai".
  4. Kombinasi tetap berupa penyatuan. Temuan kedua komponen atas butir yang sama dihitung sekali, dengan aturan deduplikasi yang ditetapkan sebelum pengujian. Akibatnya, syarat presisi kombinasi hanya mungkin terpenuhi bila kedua komponen sering keliru pada butir yang sama, jadi syarat itu dapat sukar dipenuhi. Recall penyatuan tidak lebih rendah daripada recall tiap komponen hanya bila penyatuan disusun dari keluaran yang sama dan aturan pencocokan tidak membuang label yang sudah cocok. Usulan ini juga menunggu pembimbing, dan D-29 tidak berubah.
  5. Kedua komponen menyasar seluruh daftar jenis. Selisih usulan ini dari dokumen penyelarasan tim dicatat.
- Pasangan ibu dan bayi: tiap episode menjadi satu unit hitung, tetapi pasangan keduanya ditempatkan di bagian data yang sama. Usulan ini bergantung pada penautan dalam data RSIA. (D-97; Q-TEAM butir 6)

Usulan lama yang masih berlaku:

- Rawat jalan dijawab terpisah dari rawat inap secara bersyarat. Bila dokumen yang setara resume medis tidak ada atau tidak memadai, hasil rawat jalan dilaporkan "tidak dapat dinilai", bukan "tidak". Bentuk dokumen rawat jalan di RSIA belum dipastikan. (D-76; Q-B1-f; Q-TEAM butir 4)
- Kombinasi dibentuk dengan penyatuan (*union*) semua temuan kedua komponen. Catatan recall-nya ditambahkan oleh D-94. (D-77)
- "Di atas ambang" berarti paling sedikit sama dengan ambang (≥). (D-78)
- Presisi dan recall dihitung dengan agregasi mikro, dan nilai 0/0 dilaporkan "tidak terdefinisi". Rinciannya diperluas oleh D-94. (D-79)
- Data pengembangan diberi label oleh saya sendiri. Akibatnya label itu tidak independen dan menjadi keterbatasan penelitian. (D-69)
- Kasus uji dipilih secara acak dengan benih tetap yang dicatat, per jenis perawatan. Temuan komponen AI di luar daftar jenis ketidaksesuaian dihitung terpisah. Pertanyaan apakah daftar jenis wajib memuat jenis yang menuntut penelaahan konteks belum terjawab. (D-70; Q-B1-cb)
- Kedua komponen menyasar seluruh daftar jenis ketidaksesuaian. (D-71)
- Gaya sitasi yang diusulkan adalah APA, menunggu tim, pembimbing, dan pedoman prodi. Naskah masih memakai konvensi penulis-tahun sementara. (K1, D-80)

### 2.3 Masih harus diputuskan

Butir yang sudah saya jawab pada DRAF 24 dipindahkan ke 2.1 dan 2.2, yaitu saling melengkapi, ketersediaan dokumen rawat jalan, penguncian, risiko batas atas, pertentangan antarusulan, Dietrich, dan cakupan sumber. Jawaban itu belum disetujui tim atau pembimbing. Butir di bawah ini masih terbuka.

- [ ] **Berapa angka ambang dan selisih minimum, dan bagaimana menilainya?** Prosedurnya sudah ada (D-89): tim menetapkan dan mencatatnya sebelum pengujian. Yang belum ada isinya:
  - angka ambang;
  - nilai, bentuk (mutlak atau relatif), dan operator batas selisih minimum;
  - satuan hitung final;
  - aturan pencocokan temuan dengan label;
  - cara menilai "lebih tinggi" beserta ketidakpastiannya;
  - kondisi keabsahan di luar usulan "tidak dapat dinilai";
  - tafsir jawaban "tidak" bila hanya satu komponen yang mencapai nilai maksimum.

  Mengapa penting: tanpa ketetapan ini, rumusan masalah belum dapat dijawab. Angkanya masih tertahan sampai tim membahasnya (D-19), dan data agregat belum tersedia.
  Pemutus: tim dan pembimbing. (Q-B1-bg, Q-B1-q, Q-B1-r, Q-B1-cc; F-A11-0034, F-A11-0036, F-A11-0037)

- [ ] **Apa arti penguncian dan prosedur perbaikannya di RSIA?** Keterangan lisan yang dimuat di naskah (D-90) masih perlu dikonfirmasi RSIA, dan rawat jalan belum tercakup.
  Mengapa penting: premis kedua dan batas kesimpulan pada tahap sebelum penguncian bergantung pada hal ini.
  Pemutus: tim dan RSIA. (Q-B1-ba, Q-B1-bi)

- [ ] **Apa batas operasional "rawat jalan terbatas", dan seperti apa bentuk dokumen rawat jalan di RSIA?** Cakupan bersyaratnya sudah dimuat (D-91), tetapi batas operasional dan satuan hitung rawat jalan belum ada.
  Mengapa penting: batasan masalah, pembagian data, dan jawaban rawat jalan bergantung pada hal ini.
  Pemutus: tim dan RSIA. (Q-B1-f; Q-TEAM butir 4)

- [ ] **Apakah pembimbing menyetujui empat rumusan masalah capstone dan judul baru?** Judul baru dari dokumen penyelarasan tim tanggal 30 Oktober kini dipakai sementara di header naskah (D-92), tetapi persetujuan pembimbing belum ada.
  Mengapa penting: rumusan masalah menjadi dasar tujuan dan metodologi, dan judul memengaruhi seluruh naskah.
  Pemutus: pembimbing. (Q-TEAM butir 9, K2)

- [ ] **Berapa jumlah minimum kasus per jenis perawatan, dan apakah jumlah kasus cukup?** Aturan "tidak dapat dinilai" sudah diusulkan (D-93), tetapi angka minimumnya baru dapat ditetapkan tim setelah data agregat tersedia.
  Mengapa penting: kecukupan kasus menentukan apakah jawaban per jenis perawatan dapat disusun.
  Pemutus: tim. (Q-A04-c, Q-B1-ci; F-A11-0016)

- [ ] **Apakah pemeriksaan manual perlu menjadi pembanding?** Saya mempertahankan pembanding berupa masing-masing komponen dan menyatakan batas perbandingannya, tetapi persetujuan pembimbing belum ada.
  Mengapa penting: pembanding menentukan apa yang dapat disimpulkan dari hasil penelitian.
  Pemutus: pembimbing. (D-22, D-72; F-A05-0109)

## 3. Perlu dikerjakan penulis setelah ada keputusan

- [ ] Menyelaraskan Bab II dengan fakta yang sudah dipakai di Bab I tetapi belum ada di Bab II: perbandingan Zeba dengan model bahasa besar dan peran kemiripan kosinus, skala penilaian Skrabic, rubrik Li, dan kategori Dietrich. Sebelumnya perlu dipastikan berkas Bab II mana yang aktif. (Q-B1-bn; F-A08-0103)
- [x] Mengoreksi kalimat di I.1 paragraf 16 dan 17 yang menyederhanakan sumber (DRAF 24, dicek pada PDF, tetapi belum diperiksa ulang a08):
  - Skrabic: 99 dari 102 kesalahan disisipkan (hlm. 2), dan model bekerja tanpa fitur pengambilan (*retrieval*) (hlm. 3).
  - Zeba: contoh keluaran juga memuat pernyataan rekam medis acuan dan jenis pemeriksaan (hlm. 9), dan yang diukur ialah ketepatan label (hlm. 10).
- [ ] Menuliskan perlakuan pasangan ibu dan bayi pada pembagian data sebagai teks final setelah tim menyetujui usulan D-97. (Q-TEAM butir 6)
- [x] Mempersempit klaim di I.5 paragraf 7 menjadi pernyataan sumber acuan label dan penilaian. Penilaian saya yang tidak independen kini disebut. (DRAF 24; F-A05-0134, F-A07-0068)
- [x] Merapikan catatan bahasa kecil (DRAF 24): sebutan komponen di I.1 paragraf 18, "Bila selisih minimum dipakai" di kedua tempat, frasa "seperti ambang" dihapus, dan "hal itu" diganti. "Benih tetap" diberi penanda bentuk baku karena belum diverifikasi. (F-A09-0230 sampai F-A09-0244; F-A07-0088, F-A07-0089)
- [x] Membersihkan butir usang di bagian Catatan kerja (DRAF 24). Bagian itu tetap bukan bagian proposal dan perlu dihapus sebelum penyerahan.
- [ ] Setelah ada keputusan tim, mengganti penanda dengan teks final serta memperbarui tujuan dan ukuran keberhasilan.
- [ ] Menyelaraskan Bab I dengan proposal Raihaan dan Abizzar. Kesesuaian lintas proposal belum dapat diverifikasi.

## 4. Perlu diverifikasi

- [ ] Rujukan Permenkes 26/2021 halaman 48 sampai 54 di I.4 belum dicocokkan dengan dokumennya. (Q-B1-bf)
- [ ] Jumlah episode per jenis perawatan dan bentuk dokumen rawat jalan belum diketahui karena data agregat belum tersedia. Akibatnya, kecukupan jumlah kasus belum dapat dinilai. (Q-A04-c, Q-B1-ci)
- [ ] Format akhir sitasi dan pedoman prodi belum dikonfirmasi. Templat individu tidak menetapkan gaya sitasi, dan header serta footer templat belum diperiksa.
- [ ] Sitasi di I.1 paragraf 16–22 sudah dicek ke halaman PDF (Dietrich, Zeba, Li, Zhang, Skrabic, dan Jaganathan). Halaman yang ditambahkan pada DRAF 24 (Skrabic hlm. 2–3, Zeba hlm. 9–10, dan Zhang hlm. 1 dan 5 untuk kalimat alasan) belum diperiksa ulang a08. Klaim kekosongan literatur hanya berlaku bagi sumber yang ditelaah dalam proposal ini, bukan hasil penelusuran sistematis.
- [ ] Keterangan lisan RSIA tentang penguncian, yaitu bahwa CPPT yang tercatat tidak dapat diubah dan resume medis dapat direvisi, belum dikonfirmasi. (D-90; Q-B1-ba)

## 5. Administratif

- [ ] Commit berkas `bab1/Bab_I_Draft.md` (DRAF 24) dan catatan di `memory/` setelah disetujui. Push belum terverifikasi. (G3)
- [ ] Menelusuri asal perubahan pada beberapa berkas yang sudah lama diperingatkan: CLAUDE.md, indeks sumber, `verify_claims.py`, dokumen migrasi Bab I dan Bab II, serta dua modul Bab II.
- [ ] Menyesuaikan build modular Bab I (folder `modular/`) dengan DRAF 23. Modul Bab I dan Bab II di folder itu belum mencerminkan DRAF 24.
- [ ] Membuat manifest integritas data RSIA.
- [ ] Membetulkan indeks sumber yang menyebut folder sumber hibrida secara keliru (09, seharusnya 16).

## Penutup

Yang sudah baik:

- Struktur subbab sudah lengkap.
- Paragraf celah penelitian (*research gap*) di I.1 sudah ditulis dan dipecah per fokus.
- I.5 terdiri atas lima tahap yang khusus untuk penelitian ini, tanpa tahap kajian pustaka.
- Rumusan masalah masih dapat dijawab "tidak".
- Klaim dari sumber utama sudah dicek ke halaman PDF.

Dokumen ini hanya ringkasan. Rincian lengkap ada di folder `memory/`. Jangan mengubah catatan di `memory/` dari dokumen ini.
