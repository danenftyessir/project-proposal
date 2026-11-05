# Penyelarasan Pemahaman Capstone

Oct 30, 2026 · @Tung Tung Tung Tung Tung ITB

## Tujuan Dokumen

Dokumen ini menetapkan judul, rumusan masalah, lingkup, pembagian bidang, dan batas kerja capstone per 30 Oktober 2026. Isinya menjadi acuan bersama saat menulis proposal individual dan merancang sistem, agar tidak ada bagian yang dikerjakan dua kali atau tidak dikerjakan siapa pun.

Setiap proposal individual mengambil rumusan masalahnya dari rumusan masalah capstone di bawah, sesuai arahan dosen. Semua bagian berisi ketetapan tim, kecuali bagian terakhir yang memuat hal yang belum ditetapkan dan berdampak pada ketiga anggota. Bila ada ketetapan yang tidak sesuai dengan rencana bidangmu, beri komentar pada kalimat yang bersangkutan.

## Gambaran Capstone

Capstone ini membangun prototipe sistem yang memeriksa kesesuaian CPPT (catatan perkembangan pasien terintegrasi) dengan resume medis sebelum klaim BPJS diajukan, untuk kasus kebidanan dan anak, rawat inap dan rawat jalan, di RSIA mitra.

**Judul capstone (baru).** "Pengembangan Sistem Pemeriksaan Kesesuaian CPPT dan Resume Medis Berbasis Aturan dan AI untuk Mendukung Kesiapan Klaim BPJS". Judul lama menonjolkan antarmuka *user-centered*, padahal tim tidak memiliki bidang antarmuka tersendiri. Judul baru menyebut objek yang diperiksa, cara memeriksanya, dan batas manfaatnya.

**Masalah yang dijawab.** Data klaim *pending* RSIA mitra pada Mei 2026 mencatat 49 klaim tertunda: 18 klaim rawat inap dan 31 klaim rawat jalan. Klaim rawat inap mencakup 90,8% nilai yang tertunda. Seluruh 31 klaim rawat jalan tertunda karena satu alasan, yaitu kode Z37 (hasil persalinan) tidak diinput pada persalinan. Wawancara dengan Direktur RSIA mitra (September 2026) menunjukkan bahwa resume medis disusun ulang secara manual pada akhir masa rawat, CPPT dan resume dikunci setelah layanan selesai, dan pemeriksaan kesiapan dokumen masih manual.

**Pengguna sasaran.** Tenaga kesehatan (DPJP, bidan, perawat) saat mencatat, serta petugas *casemix* atau koder sebelum klaim diajukan.

**Prinsip sistem.** Sistem menyajikan temuan beserta buktinya sebagai bahan klarifikasi. Sistem tidak mengubah dokumen, tidak menahan pencatatan, dan tidak memutuskan kelayakan klaim; keputusan tetap pada tenaga kesehatan dan koder.

| Peran | Nama |
| --- | --- |
| *Project Owner* | Kurnia Meity Isasari, Sp.OG. |
| Pembimbing | Satrio Adi Rukmono, S.T., M.T. |
| Ketua tim, *Claim Review & Resolution Engineering* | M. Abizzar Gamadrian (13523155) |
| *Health Data & Cross-Episode Reconciliation* | Muhammad Raihaan Perdana (13523124) |
| *AI/NLP Semantic Claim Intelligence* | Danendra Shafi Athallah (13523136) |

## Rumusan Masalah Capstone

Capstone menjawab empat rumusan masalah. Setiap anggota mengambil rumusan yang menjadi bagiannya dan menuliskan bagian yang ia ukur, karena dosen meminta rumusan masalah individual diturunkan dari rumusan masalah capstone. Setiap rumusan dapat berjawab "tidak" karena hasilnya dibandingkan dengan ambang yang ditetapkan sebelum pengujian.

1. **Pembentukan temuan.** Apakah kombinasi pemeriksaan *rule-based* dan AI/NLP berbasis RAG dapat mendeteksi ketidaksesuaian antara CPPT dan resume medis pada kasus kebidanan dan anak di RSIA mitra dengan presisi dan *recall* di atas ambang terhadap label tenaga ahli?
2. **Keterlacakan bukti.** Apakah setiap temuan, yang disimpan dalam satu skema temuan terpadu, dapat ditelusuri ke pasien, episode, versi dokumen, dan bagian sumber yang menjadi buktinya hanya dari catatan temuan, dengan ketepatan lokasi bukti dan ketepatan penautan episode di atas ambang terhadap isi sumber, serta hanya dapat dibuka oleh pengguna yang berwenang?
3. **Dokumen yang berubah.** Ketika CPPT atau resume medis berubah, apakah sistem dapat menyimpan versi baru beserta catatan perubahannya tanpa kehilangan entri, menetapkan status temuan lama (aktif, perlu diperiksa ulang, atau tidak berlaku untuk versi terbaru) dan mencocokkannya dengan temuan baru dengan ketepatan di atas ambang terhadap status acuan tenaga ahli, serta menghasilkan temuan ganda lebih sedikit daripada pemeriksaan ulang penuh tanpa pencocokan?
4. **Peninjauan temuan.** Apakah tenaga ahli dan pengguna proksi dapat menilai dan menindaklanjuti temuan melalui antarmuka peninjauan, dengan tingkat penyelesaian tugas, skor SUS, serta penilaian kejelasan alasan, bukti, relevansi, dan rujukan temuan masing-masing di atas ambang?

| Rumusan | Abizzar | Raihaan | Danen |
| --- | --- | --- | --- |
| 1. Pembentukan temuan | — | Menyediakan data per episode | **Utama:** presisi dan *recall* temuan |
| 2. Keterlacakan bukti | Skema temuan; keterlacakan dari catatan temuan | **Utama:** lokasi bukti, penautan episode termasuk ibu–bayi, kewenangan akses | Mengisi lokasi bukti pada setiap temuan |
| 3. Dokumen yang berubah | **Utama:** status temuan, pencocokan lama–baru, temuan ganda | Versi dan catatan perubahan tanpa kehilangan entri | Pemeriksaan ulang pada bagian yang terdampak |
| 4. Peninjauan temuan | **Utama:** alur penilaian dan tindak lanjut, penyelesaian tugas, SUS | Tampilan bukti sumber pada versinya | Kejelasan alasan dan rujukan temuan |

## Yang Masuk Lingkup

Sistem memeriksa CPPT dan resume medis di dalam satu episode, rawat inap maupun rawat jalan, untuk kasus kebidanan dan anak di RSIA mitra.

- **Dokumen yang diperiksa:** CPPT dan resume medis saja. Nilai yang tertulis di dalam entri CPPT, misalnya hasil Hb yang dicatat perawat, ikut diperiksa. Padanan kedua dokumen pada rawat jalan masih dipastikan ke RSIA karena resume medis wajib untuk rawat inap dan rawat darurat, tetapi tidak selalu dibuat untuk rawat jalan (Permenkes 24/2022 Pasal 26).
- **Satuan pemeriksaan:** satu episode menurut Permenkes 26/2021. Episode rawat inap berlangsung dari tanggal masuk sampai keluar rumah sakit, termasuk ruang intensif, ruang operasi, rawat jalan atau IGD yang berlanjut ke rawat inap pada hari yang sama, dan IGD lebih dari 6 jam. Episode rawat jalan adalah rangkaian pelayanan pada hari yang sama.
- **Lintas hari:** entri CPPT yang bertambah setiap hari selama rawat inap dibandingkan dengan resume medis dan dengan entri lain dalam episode yang sama.
- **Penautan ibu–bayi (terbatas):** episode ibu dan episode bayi baru lahir dari persalinan yang sama ditautkan karena bayi sehat yang mendapat pelayanan neonatal esensial dibayar dalam paket persalinan ibunya, sedangkan bayi sakit yang membutuhkan perawatan lain diklaim terpisah (Permenkes 26/2021). Pemeriksaannya terbatas pada isian yang ada di catatan keduanya: hasil persalinan (lahir hidup atau mati, tunggal atau kembar), tanggal dan cara persalinan, serta usia kehamilan.
- **Cara memeriksa:** aturan *rule-based* dan AI/NLP berbasis RAG, keduanya disusun Danen. Setiap temuan wajib menunjuk versi dokumen dan lokasi buktinya.
- **Waktu memeriksa:** aturan *rule-based* berjalan setiap entri disimpan. AI/NLP berjalan saat resume medis dibuat atau diubah, saat pengguna memintanya, dan wajib sekali sebelum episode ditandai siap diajukan.
- **Pemeriksaan ulang pada versi baru:** aturan *rule-based* dijalankan ulang penuh, sedangkan AI/NLP hanya memeriksa bagian yang berubah terhadap seluruh isi dokumen pasangannya. Pemeriksaan sebelum pengajuan menjalankan AI/NLP penuh sekali sebagai jaring pengaman.
- **Siklus hidup temuan:** penyatuan ke satu skema, rekonsiliasi antarpemeriksaan, penilaian dan tindak lanjut oleh pengguna, evaluasi ulang saat versi dokumen berubah, serta rekap per episode dengan status kesiapan klaim.
- **Pengelolaan data dan bukti:** versi per entri, catatan perubahan, lokasi bukti, *provenance* data, audit akses, dan deidentifikasi.
- **Bentuk keluaran:** prototipe aplikasi *web* yang dibuka lewat peramban di komputer.
- **Data:** data terdeidentifikasi dari RSIA mitra; izin penggunaannya sudah diperoleh dan jumlah kasusnya mencukupi.

## Klaim *Pending* dan Lingkupnya

Dari 49 klaim *pending* Mei 2026, 35 klaim dapat diperiksa dari CPPT dan resume medis, 7 klaim bergantung pada isi CPPT dan rujukan yang tersedia, dan 7 klaim berada di luar lingkup. Aturannya: klaim masuk bila buktinya dapat dibaca dari CPPT dan resume medis dalam satu episode, sedangkan klaim yang membutuhkan dokumen pendukung atau kunjungan lain tidak dimasukkan.

| Alasan *pending* | Rawat | Klaim | Lingkup | Keterangan |
| --- | --- | --- | --- | --- |
| Kode Z37 (hasil persalinan) tidak diinput pada persalinan | Jalan | 31 | Masuk | Persalinan tercatat, tetapi kode Z37 tidak ada; cocok untuk aturan *rule-based* |
| Kode repair episiotomi 73.6, bukan 75.69 | Inap | 2 | Masuk | Tindakan yang tercatat dibandingkan dengan kode di resume |
| Konfirmasi indikasi seksio sesarea | Inap | 1 | Masuk | Indikasi ditulis DPJP di CPPT dan resume |
| Rawat inap kurang dari 6 jam yang seharusnya ditagihkan sebagai RJTL | Inap | 1 | Masuk | Jam masuk dan keluar pada resume |
| Bukti *loading* cairan untuk dehidrasi | Inap | 4 | Bergantung | Masuk bila pemberian cairan ditulis di CPPT |
| Hasil lab sebelum dan sesudah transfusi | Inap | 1 | Bergantung | Masuk bila hasil lab ditulis di CPPT |
| Leukosit bayi baru lahir | Inap | 1 | Bergantung | Masuk bila hasil lab ditulis di CPPT |
| Indikasi rawat inap faringitis akut terhadap rekomendasi TKMKB | Inap | 1 | Bergantung | Masuk bila rekomendasi TKMKB tersedia sebagai rujukan RAG |
| Seksio sesarea tanpa riwayat berobat ke poli Obgyn | Inap | 6 | Tidak | Butuh kunjungan lain, yang merupakan episode tersendiri |
| Tidak ada partograf | Inap | 1 | Tidak | Butuh dokumen pendukung |

Berkas sumber memuat 50 baris karena SEP V000093 tercatat dua kali; klaim uniknya 49.

## Di Luar Lingkup dan Batasan

Dokumen pendukung di luar CPPT dan resume medis serta riwayat kunjungan sebelumnya tidak diperiksa. Keputusan ini berlaku untuk seluruh bagian tim (29–30 Oktober 2026) karena datanya belum tentu tersedia dan rancangannya jauh lebih rumit.

| Hal | Alasan | Perlakuan |
| --- | --- | --- |
| Hasil laboratorium sebagai dokumen terpisah (Hb sebelum dan sesudah transfusi, leukosit bayi baru lahir, protein urine) | Dokumen di luar CPPT dan resume; hasil dapat menyusul atau berubah | Saran penelitian lanjutan |
| Bukti pemberian cairan pada dokumen terpisah | Dokumen di luar CPPT dan resume | Saran penelitian lanjutan |
| Konfirmasi indikasi seksio sesarea dari dokumen lain | Dokumen di luar CPPT dan resume | Saran penelitian lanjutan |
| Partograf dan dokumen pendukung lain | Dokumen di luar CPPT dan resume | Saran penelitian lanjutan |
| Hasil pemeriksaan yang menyusul, misalnya kultur | Bukti baru masuk setelah pemeriksaan; menambah jenis perubahan baru | Saran penelitian lanjutan |
| Riwayat kunjungan sebelumnya, misalnya kunjungan poli sebelum seksio sesarea | Episode dan klaim tersendiri menurut Permenkes 26/2021 | Disebut di latar belakang, batasan, dan saran; tidak ditampilkan di antarmuka |
| OCR, *billing*, farmasi, pengajuan klaim ke BPJS, SIMRS lengkap | Di luar tujuan capstone | Tidak dikerjakan |

**Batas perilaku sistem.** Sistem tidak memutuskan kelayakan klaim, tidak memberi peringkat prioritas pada temuan, tidak menahan pencatatan, dan tidak mengubah dokumen. Status "siap diajukan" ditetapkan pengguna, bukan oleh sistem.

**Batas klaim penelitian.** Tidak ada anggota tim yang mengklaim penurunan klaim *pending* atau percepatan kerja koder. Hasil tidak digeneralisasi di luar kasus kebidanan dan anak di satu RSIA.

## Istilah Bersama

Ketiga proposal individual memakai istilah berikut dengan arti yang sama.

**Ketentuan penulisan yang wajib diikuti ketiga proposal:**

- Status keberlakuan temuan ditulis persis **aktif**, **perlu diperiksa ulang**, atau **tidak berlaku untuk versi terbaru**. Bentuk lain seperti "tetap berlaku", "masih berlaku", atau "valid" tidak dipakai.
- Rentang waktu sejak pencatatan sampai klaim diajukan ditulis **prapengajuan**, satu kata tanpa tanda hubung. Bentuk "pra-*submit*" dan "pra-pengajuan" tidak dipakai.
- Nilai penilaian, tindak lanjut, dan status kesiapan klaim ditulis persis seperti pada tabel di bawah.
- Keluaran pemeriksaan sistem disebut **temuan**, bukan "peringatan" atau *finding*.
- Istilah asing yang dipertahankan dicetak miring, misalnya *rule-based*, *evidence locator*, dan *provenance*.
- Singkatan ditulis lengkap pada kemunculan pertama di setiap bab, lalu cukup singkatannya sampai akhir bab.

| Istilah | Arti yang dipakai tim |
| --- | --- |
| Episode rawat inap | Rangkaian perawatan dari tanggal masuk sampai keluar rumah sakit; satu episode, satu klaim (Permenkes 26/2021) |
| Episode rawat jalan | Rangkaian pelayanan rawat jalan pada hari yang sama (Permenkes 26/2021) |
| Penautan ibu–bayi | Hubungan antara episode ibu dan episode bayi baru lahir dari persalinan yang sama |
| Prapengajuan | Rentang waktu sejak pencatatan sampai klaim diajukan ke BPJS |
| CPPT | Catatan perkembangan pasien terintegrasi; entri bertambah setiap hari dari berbagai tenaga kesehatan |
| Resume medis | Ringkasan pulang yang menjadi sumber pengodean INA-CBG (diagnosis utama, diagnosis sekunder, tindakan) |
| Entri | Satu catatan CPPT atau satu isian resume medis |
| Versi dokumen | Keadaan CPPT atau resume setelah entri ditambah, diubah, atau dihapus |
| Catatan perubahan | Rekaman perubahan tingkat entri antara dua versi, berisi keadaan lama dan baru |
| Lokasi bukti (*evidence locator*) | Rujukan ke bagian dokumen pada versi tertentu yang menjadi dasar temuan |
| Temuan | Ketidaksesuaian hasil pemeriksaan; memuat jenis, aturan atau rujukan, versi dokumen, lokasi bukti beserta kutipannya, waktu, dan pembuatnya |
| Bagian terdampak | Entri atau isian yang berubah, dibandingkan dengan seluruh isi dokumen pasangannya |
| Pemeriksaan ulang penuh | Pemeriksaan ulang seluruh dokumen tanpa pencocokan dengan temuan sebelumnya; hanya dipakai sebagai pembanding uji |
| Status keberlakuan | Apakah bukti temuan masih ada pada versi terbaru: aktif, perlu diperiksa ulang, atau tidak berlaku untuk versi terbaru |
| Penilaian | Pendapat pengguna atas temuan: benar, tidak benar atau tidak relevan, atau belum dapat dinilai |
| Tindak lanjut | Belum ditinjau, perlu klarifikasi, sudah ditindaklanjuti, atau tidak relevan |
| Status kesiapan klaim | Penanda tahap per episode: belum diperiksa, diperiksa, siap diajukan, diajukan |
| Tenaga ahli | Profesional yang membuat label dan status acuan tanpa melihat keluaran sistem |
| Pengguna proksi | Peserta di luar petugas RSIA mitra yang menjalankan tugas peninjauan mewakili pengguna sasaran |
| *Provenance* data | Asal data dan aktivitas yang menghasilkannya (bidang Raihaan) |
| Riwayat asal-usul temuan | Pemeriksaan yang membuat temuan, perubahan statusnya, penilaian, dan tindak lanjutnya (bidang Abizzar) |
| Audit akses | Catatan siapa membuka atau mengubah data (bidang Raihaan) |

## Alur Sistem dan Pemilik Tiap Langkah

&#91;embedded content: alur sistem · tiga bidang, satu putaran perbaikan dokumen\]

Pemeriksaan pertama berjalan dari dokumen di kiri atas sampai penilaian oleh pengguna. Bila pengguna meminta klarifikasi dan tenaga kesehatan memperbaiki dokumen, Raihaan menyimpan versi baru beserta catatan perubahannya. Danen lalu memeriksa ulang bagian yang terdampak, dan Abizzar menetapkan nasib temuan lama sebelum hasilnya kembali ke penilaian. Sebelum episode ditandai siap diajukan, AI/NLP memeriksa seluruh episode sekali lagi.

## Pembagian Bidang

Raihaan menyiapkan data dan bukti, Danen membentuk temuan dari data itu, dan Abizzar mengelola temuan setelah terbentuk. Antarmuka bukan bidang tersendiri; setiap anggota menyediakan bagian antarmuka yang menyajikan hasil bidangnya.

### Raihaan: data dan bukti

**Fokus.** Setiap data yang diperiksa berasal dari dokumen, pasien, episode, dan versi yang benar, dapat ditelusuri ke sumbernya, dan hanya diakses pihak yang berwenang.

- Menerima dan menyimpan CPPT dan resume medis, rawat inap maupun rawat jalan, beserta hasil representasinya, tetap tertaut ke bagian sumber.
- Menyatukan catatan ke dalam satu episode menurut Permenkes 26/2021, termasuk menetapkan arti No. RM, No. Rawat, No. SEP, dan No. SPRI.
- Menautkan episode ibu dengan episode bayi baru lahir dari persalinan yang sama.
- Menyimpan versi per entri dan catatan perubahan tingkat entri; versi lama tetap dapat dibuka.
- Menetapkan skema lokasi bukti bersama Danen, dan menjamin setiap lokasi bukti menunjuk versi tertentu.
- Mencatat *provenance* data, audit akses, kewenangan akses, dan deidentifikasi.

**Arti "lintas episode" pada judul Raihaan.** Frasa itu dipertahankan dan berarti penautan antarepisode yang berlangsung bersamaan, yaitu episode ibu dan episode bayi baru lahir, serta penyatuan catatan bernomor berbeda ke dalam satu episode. Riwayat kunjungan sebelumnya tidak termasuk.

**Tidak mengerjakan:** penautan dengan kunjungan sebelumnya; memindahkan lokasi bukti lama ke versi baru; menetapkan isi, status, penilaian, atau tindak lanjut temuan.

**Rumusan yang diukur:** rumusan 2 (lokasi bukti, penautan episode, kewenangan akses) dan bagian versi pada rumusan 3.

### Danen: pembentukan temuan

**Fokus.** Menghasilkan temuan ketidaksesuaian antara CPPT dan resume medis beserta bukti, alasan, dan rujukannya.

- Menyusun aturan *rule-based* dan membangun pemeriksaan AI/NLP berbasis RAG, termasuk rujukan yang dipakai RAG.
- Mengisi setiap temuan sesuai skema temuan terpadu, termasuk versi dokumen dan lokasi bukti.
- Menjalankan pemeriksaan sesuai pemicu yang ditetapkan, dan memeriksa ulang bagian yang terdampak ketika versi baru tersedia.
- Menyusun aturan pemeriksaan untuk pasangan ibu–bayi (hasil persalinan, tanggal dan cara persalinan, usia kehamilan) dan untuk kode Z37 pada persalinan.

**Tidak mengerjakan:** nasib temuan lama setelah versi berubah; penilaian dan tindak lanjut; penyimpanan versi.

**Rumusan yang diukur:** rumusan 1, serta bagian kejelasan alasan dan rujukan pada rumusan 4.

### Abizzar: siklus hidup temuan

**Fokus.** Mengelola temuan sejak terbentuk sampai episode dinyatakan siap diajukan, termasuk ketika dokumen berubah.

- Menetapkan skema temuan terpadu untuk temuan *rule-based* dan AI/NLP, termasuk temuan yang buktinya berada pada dua episode (ibu dan bayi).
- Merekonsiliasi temuan dari pemeriksaan yang berbeda pada versi yang sama.
- Merancang alur penilaian dan tindak lanjut, beserta antarmuka peninjauannya.
- Saat versi berubah: menentukan arti perubahan bagi temuan (status keberlakuan), mencocokkan temuan lama dengan temuan baru, dan mewariskan penilaian.
- Mencatat riwayat asal-usul setiap temuan, serta rekap per episode dan status kesiapan klaim.
- Menyusun skenario perubahan dokumen yang juga boleh dipakai Raihaan untuk menguji versi dan lokasi bukti.

**Tidak mengerjakan:** cara temuan dibentuk dan akurasinya; penyimpanan versi dan audit akses.

**Rumusan yang diukur:** bagian skema dan keterlacakan pada rumusan 2, rumusan 3, dan rumusan 4.

## Titik Temu Antarbidang

Tujuh bentuk data berpindah antarbidang; masing-masing punya satu penetap agar tidak ada dua versi aturan.

| Yang dipertukarkan | Ditetapkan oleh | Dipakai oleh | Ketentuan |
| --- | --- | --- | --- |
| Skema temuan terpadu | Abizzar | Danen mengisi; Raihaan menyimpan | Temuan boleh disimpan di basis data Raihaan, tetapi struktur, status, penilaian, dan tindak lanjutnya ditetapkan Abizzar |
| Skema lokasi bukti | Raihaan, disepakati dengan Danen | Danen mengisi; Abizzar membaca | Selalu menunjuk versi tertentu dan boleh menunjuk dua episode (ibu dan bayi). Lokasi lama tidak dipindahkan ke versi baru; temuan pada versi baru membawa lokasi baru dari pemeriksaan ulang Danen |
| Versi dokumen dan catatan perubahan tingkat entri | Raihaan | Danen menentukan bagian terdampak; Abizzar menentukan arti perubahan bagi temuan | Raihaan mencatat fakta perubahan (entri ditambah, diubah, dihapus; teks lama dan baru). Abizzar menafsirkan dampaknya pada temuan |
| Hubungan pasien–episode dan penautan ibu–bayi | Raihaan | Danen untuk aturan ibu–bayi; Abizzar untuk rekap per episode | Batas episode mengikuti Permenkes 26/2021 |
| Pemicu pemeriksaan dan bagian terdampak | Danen | Abizzar menunggu temuan baru sebelum evaluasi ulang | *Rule-based* setiap entri disimpan; AI/NLP saat resume dibuat atau diubah, atas permintaan pengguna, dan wajib sekali sebelum episode ditandai siap diajukan |
| Temuan hasil pemeriksaan | Danen | Abizzar | Wajib memuat versi dan lokasi bukti. Temuan tanpa keduanya dicatat sebagai kegagalan masukan, bukan kegagalan skema |
| Skenario perubahan dokumen | Abizzar | Raihaan untuk menguji versi dan lokasi bukti | Kebenaran setiap perubahan dalam skenario sudah diketahui sejak disusun |

**Jejak dibagi tiga.** *Provenance* data dan audit akses dicatat Raihaan. Riwayat asal-usul temuan, yaitu pemeriksaan pembuat, perubahan status, penilaian, dan tindak lanjut, dicatat Abizzar. Pembagian ini mengikuti pembedaan *Provenance* dan *AuditEvent* pada FHIR R4; SATUSEHAT belum memodelkan keduanya.

## Skema Temuan dan Lokasi Bukti

Setiap temuan, dari aturan *rule-based* maupun AI/NLP, diisi dengan bentuk yang sama, dan setiap lokasi buktinya menunjuk satu entri pada satu versi beserta kutipan persisnya. Danen mengisi skema ini, Raihaan menyimpan dan memeriksa ketepatan lokasinya, dan Abizzar memakainya untuk keterlacakan serta pencocokan antarversi.

### Kolom Temuan

| Kolom | Wajib | Isi | Dipakai untuk |
| --- | --- | --- | --- |
| Id temuan | Ya | Pengenal unik | Rujukan bagi status, penilaian, dan tindak lanjut |
| Id pemeriksaan | Ya | Pengenal satu kali pemeriksaan, yang mencatat versi setiap dokumen yang diperiksa | Riwayat asal-usul temuan; rekonsiliasi antarpemeriksaan |
| Pembuat | Ya | *Rule-based* atau AI/NLP, beserta versi aturan atau model | Riwayat asal-usul; hasil per pembuat |
| Waktu dibuat | Ya | Tanggal dan jam | Riwayat asal-usul |
| Episode pemilik | Ya | Episode yang klaimnya terdampak | Rekap per episode |
| Jenis ketidaksesuaian | Ya | Satu kode dari daftar tertutup di bawah, bukan teks bebas | Pencocokan antarversi dan rekonsiliasi |
| Aturan atau rujukan | Ya | Id aturan *rule-based*, atau dokumen rujukan RAG beserta bagiannya | Keterlacakan (rumusan 2); pencocokan |
| Objek | Bila ada | Konsep atau kode yang dipersoalkan, misalnya ICD-10 Z37.0 atau ICD-9-CM 75.69 | Pencocokan saat posisi bukti bergeser |
| Alasan | Ya | Penjelasan singkat untuk pengguna | Peninjauan (rumusan 4) |
| Lokasi bukti | Ya, minimal satu | Daftar lokasi bukti (tabel berikut) | Ketiga bidang |

Status keberlakuan, penilaian, tindak lanjut, dan hubungan antartemuan tidak diisi Danen. Keempatnya dicatat Abizzar sebagai catatan terpisah yang merujuk id temuan sehingga isi temuan asli tidak pernah diubah. Skema tidak memuat kolom prioritas karena sistem tidak memeringkat temuan.

### Kolom Lokasi Bukti

| Kolom | Wajib | Isi |
| --- | --- | --- |
| Episode | Ya | Episode tempat dokumen berada; lokasi dalam satu temuan boleh berasal dari dua episode (ibu dan bayi) |
| Jenis dokumen | Ya | CPPT, resume medis, atau padanannya pada rawat jalan |
| Dokumen dan versi | Ya | Dokumen dan versi yang diperiksa |
| Entri atau isian | Ya | Entri CPPT, atau isian resume seperti "diagnosis sekunder"; id entri tetap sama di semua versi |
| Posisi awal dan akhir | Bila ada kutipan | Posisi karakter di dalam entri, bukan di seluruh dokumen |
| Kutipan | Ya | Teks persis seperti tertulis, tanpa diubah atau diringkas; boleh kosong bila isiannya kosong |
| Peran | Ya | **Dipersoalkan** (bagian yang dinilai tidak sesuai), **pendukung** (bagian yang menunjukkan ketidaksesuaian), atau **isian kosong** (tempat sesuatu seharusnya ada) |

### Aturan Pengisian

1. **Kutipan harus persis.** Teks pada posisi awal sampai akhir di versi yang dirujuk harus sama dengan kutipan. Bila tidak sama, temuan dicatat sebagai kegagalan masukan dan tidak ditampilkan. Aturan ini sekaligus menjadi pemeriksaan otomatis ketepatan lokasi bukti.
2. **Temuan "sesuatu tidak ada" menunjuk isian tempat hal itu seharusnya ada**, dengan peran isian kosong dan kutipan berupa isi isian saat itu. Contohnya kode Z37 yang tidak diinput: bila koder menambahkannya, isian berubah dan temuan dievaluasi ulang.
3. **Temuan ibu–bayi memuat minimal satu lokasi dari setiap episode.** Temuan masuk rekap episode pemilik dan tampil sebagai rujukan pada episode pasangannya, tanpa dihitung dua kali.
4. **Id entri tidak berubah antarversi.** Entri yang diubah tetap memakai id yang sama, sedangkan entri baru mendapat id baru. Tanpa aturan ini, perubahan satu entri tidak dapat dibedakan dari penghapusan lalu penambahan.

### Contoh Pengisian

| Kolom | Contoh 1: diagnosis tidak didukung | Contoh 2: kode wajib tidak ada |
| --- | --- | --- |
| Jenis ketidaksesuaian | Diagnosis atau tindakan di resume tidak didukung CPPT | Kode wajib tidak diinput |
| Objek | ICD-10 O99.0 (anemia dalam kehamilan) | ICD-10 Z37.0 (lahir hidup tunggal) |
| Aturan atau rujukan | Aturan diagnosis anemia (contoh) | Aturan kode hasil persalinan (contoh) |
| Lokasi bukti 1 | Resume v1, isian diagnosis sekunder, "Anemia dalam kehamilan", dipersoalkan | Catatan kunjungan v1, entri persalinan, "Bayi lahir hidup tunggal", pendukung |
| Lokasi bukti 2 | CPPT v1, entri 3, "Hb 11,8 g/dL", pendukung | Resume v1, isian diagnosis sekunder, kutipan kosong, isian kosong |

Seluruh data contoh fiktif. Contoh 1 memakai pasien yang sama dengan Gambar II.1–II.2 di proposal Abizzar.

### Daftar Jenis Ketidaksesuaian (Usulan Awal)

1. Diagnosis atau tindakan di resume tidak didukung CPPT, misalnya indikasi seksio sesarea.
2. Diagnosis atau tindakan di CPPT tidak tercantum di resume.
3. Kode tidak sesuai dengan diagnosis atau tindakan yang tercatat, misalnya repair episiotomi.
4. Kode wajib tidak diinput, misalnya Z37 pada persalinan.
5. Data ibu dan bayi tidak sejalan.
6. Data administratif episode tidak sesuai dengan jenis rawat, misalnya rawat inap kurang dari 6 jam.
7. Indikasi tidak sesuai dengan rujukan, misalnya indikasi rawat inap terhadap rekomendasi TKMKB.

Daftar final ditetapkan bersama Danen sebelum aturan disusun.

## Keputusan 30 Oktober dan Alasannya

Tiga belas hal ditetapkan pada 30 Oktober 2026. Alasan setiap keputusan dicatat agar anggota yang tidak ikut membahas tahu dasar pilihannya.

| Hal | Yang ditetapkan | Alasan |
| --- | --- | --- |
| Rawat jalan | Masuk lingkup, terbatas pada CPPT dan resume medis atau padanannya | Ke-31 klaim *pending* rawat jalan berasal dari satu alasan (kode Z37) yang cukup diperiksa dengan satu aturan. Episode rawat jalan hanya satu hari sehingga dokumennya jarang berubah. Yang perlu dipastikan: bentuk dokumen rawat jalan di RSIA |
| Pemicu AI/NLP | Saat resume dibuat atau diubah, atas permintaan pengguna, dan wajib sekali sebelum episode ditandai siap diajukan | Perbandingan CPPT dengan resume baru bermakna setelah resume ada. AI/NLP pada setiap entri CPPT mahal dan memunculkan temuan berulang. Pemeriksaan wajib sebelum pengajuan memastikan tidak ada episode yang lolos |
| Cakupan pemeriksaan ulang | *Rule-based* penuh; AI/NLP hanya pada bagian terdampak; AI/NLP penuh sekali sebelum pengajuan | Memeriksa bagian yang berubah tanpa pasangannya melewatkan ketidaksesuaian baru. Memeriksa seluruh dokumen setiap kali berubah menaikkan biaya dan temuan ganda. Temuan pada bagian yang tidak tersentuh tetap aktif melalui evaluasi ulang |
| "Lintas episode" di judul Raihaan | Dipertahankan; artinya penautan ibu–bayi dan penyatuan catatan dalam satu episode | Dengan penautan ibu–bayi, memang ada dua episode yang ditautkan. Bila penautan ibu–bayi dibatalkan, frasa ini dihapus dari judul |
| Penautan ibu–bayi | Masuk, terbatas pada isian yang ada di catatan ibu dan bayi | Berpengaruh langsung ke klaim: bayi sehat dibayar dalam paket persalinan ibu, bayi sakit diklaim terpisah, dan hasil persalinan dikode Z37 pada ibu (Permenkes 26/2021) |
| Riwayat kunjungan sebelumnya | Hanya disebut di latar belakang, batasan, dan saran | Menampilkannya di antarmuka tetap menuntut penautan lintas kunjungan, pekerjaan yang sudah dikeluarkan, tanpa ada yang diuji |
| Istilah | Status keberlakuan: aktif, perlu diperiksa ulang, tidak berlaku untuk versi terbaru. Rentang sebelum klaim diajukan: prapengajuan. Ketentuan lengkap ada di bagian Istilah Bersama | Dokumen tim sebelumnya memakai dua bentuk untuk hal yang sama: "aktif" dan "tetap berlaku", serta "pra-submit" dan "prapengajuan". Satu bentuk dipilih agar ketiga proposal seragam; "aktif" sudah dipakai di daftar status entitas tim, dan "prapengajuan" adalah bentuk baku bahasa Indonesia |
| Rujukan model data kesehatan | SATUSEHAT untuk objek yang sudah dimodelkannya: pasien, kunjungan, episode perawatan, diagnosis, tindakan, dan dokumen klinis. HL7 FHIR R4 dasar untuk Provenance dan AuditEvent, yang tidak ada dalam daftar resource SATUSEHAT | Dosen meminta acuan Indonesia dipakai bila sudah ada. SATUSEHAT dibangun di atas FHIR R4, jadi keduanya tidak bertentangan. Episode perawatan di SATUSEHAT (misalnya selama kehamilan) berbeda dari episode INA-CBG; untuk klaim tetap dipakai episode menurut Permenkes 26/2021 |
| Platform | Prototipe aplikasi *web* | Cukup dibuka lewat peramban tanpa instalasi sehingga mudah dipakai saat uji. Aplikasi desktop tidak lebih mudah karena harus dipasang di setiap komputer peserta |
| Judul capstone | "Pengembangan Sistem Pemeriksaan Kesesuaian CPPT dan Resume Medis Berbasis Aturan dan AI untuk Mendukung Kesiapan Klaim BPJS" | Tidak ada bidang antarmuka tersendiri; judul baru menyebut objek, cara, dan batas manfaat |
| Rumusan masalah | Empat rumusan capstone; rumusan individual diturunkan darinya | Arahan dosen |
| Data | Data terdeidentifikasi RSIA mitra | Izin sudah diperoleh dan jumlah kasusnya mencukupi |
| Gaya sitasi | APA | Dipakai sampai ada pedoman prodi |

## Data dan Evaluasi

Setiap rumusan diuji dengan acuannya sendiri sehingga kesalahan satu bidang tidak terhitung sebagai kesalahan bidang lain.

**Sumber data.** Pengujian memakai data terdeidentifikasi dari RSIA mitra; izin sudah diperoleh dan jumlah kasusnya mencukupi. Data dibagi per pasien agar catatan satu pasien tidak muncul di data pengembangan dan data uji sekaligus. Data klaim *pending* Mei 2026, empat berkas contoh (V000094, V000099, V000162, V000163), dan wawancara September 2026 hanya menggambarkan masalah, bukan berkas uji.

| Rumusan | Yang diukur | Acuan | Pengukur |
| --- | --- | --- | --- |
| 1 | Presisi dan *recall* temuan | Label tenaga ahli | Danen |
| 2 | Keterlacakan dari catatan temuan; ketepatan lokasi bukti; ketepatan penautan episode; akses tanpa kewenangan ditolak | Isi dokumen sumber; data registrasi RSIA untuk penautan; kebijakan akses | Abizzar (keterlacakan), Raihaan (lainnya) |
| 3 | Versi tersimpan tanpa kehilangan entri; ketepatan status dan pasangan lama–baru; temuan ganda | Skenario perubahan yang kebenarannya diketahui; status acuan tenaga ahli; pemeriksaan ulang penuh sebagai pembanding temuan ganda | Raihaan (versi), Abizzar (lainnya) |
| 4 | Penyelesaian tugas; SUS; penilaian kejelasan alasan, bukti, relevansi, dan rujukan | Ambang yang ditetapkan sebelum uji | Abizzar (alur dan SUS), Danen (kejelasan dan rujukan) |

**Aturan acuan.** Label dan status acuan dibuat tenaga ahli tanpa melihat keluaran sistem. Penilaian pengguna di antarmuka tidak dipakai sebagai acuan karena pengguna cenderung menerima keluaran sistem apa adanya (*automation bias*). Angka ambang setiap ukuran ditetapkan bersama pembimbing sebelum pengujian; usulan awalnya ada di bagian berikut.

### Tenaga Ahli dan Pengguna Proksi

**Fungsi tenaga ahli.** Tenaga ahli menetapkan jawaban yang benar sebelum sistem diuji, tanpa melihat keluaran sistem. Tugasnya tiga: melabeli ketidaksesuaian pada berkas uji (rumusan 1), menetapkan status dan pasangan acuan pada skenario perubahan dokumen (rumusan 3), serta ikut uji peninjauan dan menilai kejelasan temuan (rumusan 4). Dua tugas pertama dikerjakan lebih dulu karena setelah melihat keluaran sistem penilaian mereka tidak lagi netral.

**Fungsi pengguna proksi.** Pengguna proksi menggantikan tenaga kesehatan dan koder RSIA dalam uji tugas rumusan 4 karena petugas RSIA sulit meluangkan waktu. Mereka menilai dan menindaklanjuti temuan melalui prototipe, lalu mengisi SUS.

**Usulan susunan peserta:**

- **Tenaga ahli, dua orang dengan keahlian berbeda:** satu klinisi yang biasa mengisi atau memverifikasi CPPT dan resume (dokter umum atau dokter spesialis kebidanan atau anak), dan satu koder atau petugas *casemix* yang mengodekan klaim BPJS. Sebagian alasan *pending* adalah soal kode (Z37, repair episiotomi) yang lebih tepat dinilai koder. Sebagian berkas dilabeli keduanya agar kesepakatan antarpenilai dapat dilaporkan.
- **Koas (dokter muda):** tidak disarankan sebagai tenaga ahli karena belum berwenang atas dokumentasi dan pengodean klaim, tetapi cocok sebagai pengguna proksi karena sudah pernah mengisi CPPT.
- **Mahasiswa kedokteran tahap praklinik:** tidak disarankan, baik sebagai tenaga ahli maupun pengguna proksi, karena belum pernah mengisi CPPT atau resume.
- **Pengguna proksi, sekitar 5–8 orang:** campuran koas (mewakili tenaga kesehatan) dan mahasiswa rekam medis dan informasi kesehatan atau koder magang (mewakili koder). Jumlah final ditetapkan bersama pembimbing.

## Ambang Keberhasilan (Usulan Awal)

Tiga belas ukuran perlu diberi ambang sebelum pengujian. Angka di bawah adalah usulan awal untuk dibawa ke pembimbing; angka finalnya ditetapkan bersama pembimbing.

| Ukuran | Rumusan | Usulan awal | Pertimbangan |
| --- | --- | --- | --- |
| *Recall* temuan | 1 | ≥ 0,80 | Ketidaksesuaian yang terlewat dapat berujung klaim *pending*, jadi *recall* diberi ambang lebih tinggi daripada presisi |
| Presisi temuan | 1 | ≥ 0,70 | Temuan yang salah menambah beban peninjau dan memicu kelelahan peringatan |
| Keterlacakan dari catatan temuan | 2 | 100% | Syarat mutlak: satu temuan yang tidak dapat ditelusuri sudah berarti gagal |
| Ketepatan lokasi bukti | 2 | ≥ 95% | Lokasi bukti menjadi dasar penilaian dan evaluasi ulang; kesalahannya merambat ke bidang lain |
| Ketepatan penautan episode dan ibu–bayi | 2 | ≥ 95% | Penautan di satu rumah sakit memakai nomor yang tersedia, jadi ketepatannya diharapkan tinggi |
| Akses tanpa kewenangan ditolak | 2 | 100% skenario uji | Kebocoran data pasien tidak dapat ditoleransi |
| Versi tersimpan tanpa kehilangan entri | 3 | 100% skenario uji | Versi yang hilang membuat evaluasi ulang tidak dapat diperiksa |
| Ketepatan status keberlakuan | 3 | ≥ 80% | Belum ada angka pembanding dari penelitian sebelumnya; 80% dipakai sebagai titik awal diskusi |
| Ketepatan pasangan lama–baru | 3 | ≥ 80% | Sama dengan ketepatan status |
| Pengurangan temuan ganda | 3 | Berkurang paling sedikit 50% dibanding pemeriksaan ulang penuh | Pembanding tanpa pencocokan hampir pasti menghasilkan lebih banyak temuan ganda, jadi syarat "lebih sedikit" saja terlalu mudah dipenuhi |
| Penyelesaian tugas | 4 | ≥ 80% tugas selesai tanpa bantuan | Tugas disusun dari pekerjaan sehari-hari peninjau; banyak tugas gagal berarti alurnya belum jelas |
| Skor SUS | 4 | ≥ 68 | Angka rata-rata yang sering dipakai dalam literatur kegunaan, tetapi Brooke (1996) tidak menetapkan ambang; bila dipakai, perlu sumber tambahan |
| Penilaian kejelasan alasan, bukti, relevansi, dan rujukan | 4 | Rata-rata ≥ 4 dari 5 per aspek | Skala 1–5 disusun saat perancangan rinci |

## Yang Masih Perlu Ditetapkan

Sembilan hal belum ditetapkan, dan semuanya berdampak pada ketiga anggota. Hal yang hanya menyangkut satu bidang diputuskan oleh anggota yang bersangkutan dan tidak dicantumkan di sini.

| No. | Butir | Penanggung jawab | Ditanyakan ke | Status |
| --- | --- | --- | --- | --- |
| 1 | Persetujuan Danen dan Raihaan atas skema temuan dan lokasi bukti, serta daftar final jenis ketidaksesuaian | Abizzar, Raihaan, Danen | Tim | Belum dibahas |
| 2 | Apakah hasil laboratorium dan pemberian cairan ikut ditulis di CPPT; menentukan 6 dari 7 klaim berstatus "Bergantung" | Abizzar | RSIA mitra | Sedang dicari tahu |
| 3 | Formulir kosong CPPT dan resume medis, tanpa data pasien | Abizzar | RSIA mitra | Sedang dicari tahu |
| 4 | Bentuk dokumen rawat jalan: apakah ada CPPT dan resume medis, atau catatan kunjungan dan daftar diagnosis beserta kodenya | Abizzar | RSIA mitra | Perlu ditanyakan |
| 5 | Prosedur membuka kembali CPPT dan resume yang sudah terkunci | Abizzar | RSIA mitra | Perlu ditanyakan |
| 6 | Apakah data RSIA menautkan bayi dengan ibunya, misalnya nomor rekam medis ibu pada catatan bayi | Abizzar | RSIA mitra | Perlu ditanyakan |
| 7 | Siapa tenaga ahli (usulan: satu klinisi dan satu koder) dan siapa pengguna proksi (usulan: 5–8 koas dan mahasiswa rekam medis) | Abizzar | RSIA mitra, pembimbing | Belum dibahas |
| 8 | Angka ambang setiap ukuran; usulan awalnya ada di bagian Ambang Keberhasilan | Abizzar | Pembimbing | Belum dibahas |
| 9 | Persetujuan judul capstone baru dan empat rumusan masalah capstone | Abizzar | Pembimbing | Belum dibahas |
