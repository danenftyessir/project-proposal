
# Rangkuman Lengkap Bimbingan Tugas Akhir & Tesis: Prinsip Penulisan sebagai Argumen dan Pemodelan Perangkat Lunak

**Dosen Pembimbing:** Satrio Adi Rukmono, S.T., M.T.
**Tanggal Pertemuan:** 15 Oktober 2026 (Durasi Rekaman: 2 jam 9 menit 12 detik)
**Sumber Materi:** Rekaman Transkrip Bimbingan (Menit 00:04–28:55 untuk Materi Utama; Menit 28:55–02:09:12 untuk Sesi Asistensi) & Slide Presentasi *Penyamaan Perspektif Materi 2: Prinsip Menulis Tugas Akhir sebagai Argumen*

## 1. Paradigma Dasar: Tugas Akhir dan Tesis adalah Argumen Ilmiah, Bukan Laporan Kegiatan

Banyak dokumen Tugas Akhir (TA) maupun Tesis dinilai kurang memuaskan karena mahasiswa hanya memaparkan kronologi pembuatan perangkat lunak ("apa saja yang telah dibuat"), bukan membangun argumen yang meyakinkan pembaca. Dalam sidang (*defense*), tugas utama penulis adalah mempertahankan klaim di hadapan penguji yang bersikap skeptis.

| Dimensi Perbandingan                      | Laporan Kegiatan (Kurang Tepat)                        | Argumen Ilmiah (Seharusnya)                                            |
| :---------------------------------------- | :----------------------------------------------------- | :--------------------------------------------------------------------- |
| **Pertanyaan Pembaca / Penguji**    | "Apa saja yang kamu buat?"                             | "Mengapa saya harus percaya pada klaim Anda?"                          |
| **Contoh Kalimat Hasil**            | "Sistem berhasil diimplementasikan."                   | "X bekerja 2 kali lebih cepat daripada Y pada data Z."                 |
| **Fokus Penulisan**                 | Deskripsi aktivitas dan fitur yang selesai dibuat      | Klaim terukur yang didukung bukti (*evidence*) dan penalaran logis   |
| **Sifat saat Sidang (*Defense*)** | Mudah diserang karena klaim kabur atau tanpa dasar uji | Kokoh karena setiap klaim penting memiliki bukti dan batasan eksplisit |

### Akar Masalah dan Rekomendasi Buku Referensi

* **Kesenjangan Kemampuan Berargumentasi:** Berdasarkan pengalaman dosen saat menempuh studi S3 dan membimbing mahasiswa di Belanda, terdapat perbedaan mencolok antara mahasiswa di Belanda dan di Indonesia dalam hal mengekspresikan isi pikiran secara tertulis. Pendidikan dasar hingga menengah di Indonesia umumnya belum membiasakan siswa menyusun kerangka argumentasi, mengolah bukti atas klaim, dan menalar himpunan kebenaran secara ketat.
* **Buku Referensi Wajib Baca:** Mahasiswa disarankan membaca buku klasik karya **Prof. Dr. Gorys Keraf** berjudul ***Argumentasi dan Narasi*** (terbitan era akhir 1970-an/awal 1980-an, kisaran harga Rp50.000 di toko buku). Buku tersebut menjadi rujukan utama dalam slide presentasi dosen (ditandai sebagai *Keraf I.2, II, V.5, VI.4*) karena mengupas dasar logika berbahasa, proposisi, himpunan kebenaran, serta cara menyusun pembuktian yang tidak mudah dibantah.

## 2. Sepuluh Prinsip Penulisan Tugas Akhir sebagai Argumen

Kesepuluh prinsip berikut merupakan daftar periksa (*checklist*) utama yang digunakan dosen dan penguji untuk menilai kualitas Bab I (Latar Belakang, Rumusan Masalah, Tujuan), Bab Evaluasi/Pengujian, hingga Bab Kesimpulan.

### Ringkasan 10 Prinsip Utama

| No           | Prinsip Penulisan                                                 | Bagian Dokumen Terkait                     | Contoh yang Harus Dihindari                                                                           | Contoh Penulisan yang Tepat                                                                                      |
| :----------- | :---------------------------------------------------------------- | :----------------------------------------- | :---------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- |
| **1**  | **Mulai dari masalah pembaca, bukan dari teknologi**        | Bab I (Latar Belakang & Rumusan Masalah)   | "Penelitian ini membangun chatbot berbasis LLM untuk layanan akademik."                               | "Mahasiswa baru menunggu rata-rata dua hari untuk jawaban administrasi yang sudah ada di pedoman."               |
| **2**  | **Ajukan pertanyaan yang bisa dijawab 'tidak'**             | Bab I (Rumusan Masalah)                    | "Bagaimana merancang sistem rekomendasi pengadaan?"                                                   | "Apakah rekomendasi sistem menghasilkan profit lebih tinggi daripada kebijakan manual?"                          |
| **3**  | **Nyatakan kuantitas klaim: semua, sebagian, berapa**       | Bab Evaluasi & Kesimpulan                  | "Pengguna merasa terbantu."                                                                           | "24 dari 31 responden menyatakan terbantu; 5 netral, 2 tidak."                                                   |
| **4**  | **'Lebih' selalu lebih daripada sesuatu**                   | Bab Evaluasi & Kesimpulan                  | "Avatar terbukti mengurangi kecemasan pengguna." (1 kondisi, 31 responden)                            | "Skor kecemasan dengan avatar 1,2 poin lebih rendah daripada dengan antarmuka teks, pada 31 responden."          |
| **5**  | **Tetapkan ukuran dan tanda gagal sebelum eksperimen**      | Bab Analisis (NFR) & Rancangan Pengujian   | "Sistem mampu menekan ukuran berkas secara signifikan."                                               | "Hipotesis gagal jika ukuran berkas turun kurang dari 20% dibanding gzip pada korpus Z."                         |
| **6**  | **Jangan menyimpulkan melampaui kasus yang diuji**          | Bab Evaluasi & Kesimpulan                  | "Metode ini efektif untuk mendeteksi code smell pada perangkat lunak." (diuji pada 4 repositori Java) | "Pada 4 repositori Java berukuran sedang, metode ini mendeteksi ...; bahasa lain belum diuji."                   |
| **7**  | **Klaim sebab harus menyingkirkan penjelasan lain**         | Bab Eksperimen & Evaluasi                  | "Latensi turun setelah cache ditambahkan, jadi cache menurunkan latensi."                             | "... pada mesin, data, dan beban yang sama; satu-satunya perubahan di antara dua pengukuran adalah cache."       |
| **8**  | **Tuliskan premis yang tersembunyi**                        | Bab Pengujian & Pembahasan                 | "Semua tes lulus, jadi implementasi sudah benar."                                                     | "Semua 212 tes lulus; tes itu mencakup kasus A dan B, belum mencakup C."                                         |
| **9**  | **Celah dan pilihan rancangan juga klaim**                  | Bab II (Studi Literatur) & Bab Perancangan | "Penelitian sebelumnya masih terbatas."                                                               | Menyebutkan spesifik riset A sudah melakukan X tetapi belum Y, serta alasan memilih X beserta *trade-off*-nya. |
| **10** | **Kesimpulan menjawab pertanyaan, lengkap dengan batasnya** | Bab Kesimpulan                             | "Sistem berhasil dirancang dan diimplementasikan sesuai kebutuhan."                                   | "X 2,1 kali lebih cepat daripada Y pada data Z (Subbab 5.2); belum diuji pada data di atas 1 GB."                |

### Penjelasan Detail Tiap Prinsip

1. **Prinsip 1 — Mulai dari masalah pembaca, bukan dari teknologi (Slide 4 & Transkrip 03:30–05:15)**
   * **Inti Bahasan:** Jangan berangkat dari teknologi/solusi yang mencari-cari masalah (*solution looking for a problem*). Penelitian dan pelaporan harus berangkat dari *problem space* (masalah nyata yang dialami pengguna/organisasi), bukan langsung menyebut teknologi.
   * **Penerapan pada Bab I:** Di bagian awal laporan dan rumusan masalah, jelaskan dampak buruk atau ketidakefisienan yang terjadi saat ini. Pemilihan teknologi (seperti penggunaan LLM) hanyalah konsekuensi logis setelah masalah dianalisis, bukan tujuan yang berdiri sendiri.
   * **Pertanyaan Cek Mandiri:** *Bisakah kamu menulis masalahnya tanpa menyebut teknologi apa pun? Siapa yang dirugikan, dan apa buktinya?*
2. **Prinsip 2 — Ajukan pertanyaan yang bisa dijawab "tidak" (Slide 5 & Transkrip 05:16–06:50)**
   * **Inti Bahasan:** Kesalahan paling umum mahasiswa TA adalah menulis rumusan masalah dengan kalimat *"Bagaimana merancang sistem yang..."*. Pertanyaan semacam ini bersifat tautologis dan merupakan tugas kuliah biasa: jawabannya hanya berupa langkah-langkah perancangan sesuai buku Rekayasa Perangkat Lunak (RPL) dan tidak bisa dibantah atau diuji gagal/berhasilnya.
   * **Penerapan pada Rumusan Masalah:** Rumusan masalah harus berupa pertanyaan yang **dapat diuji (*testable/falsifiable*)**—yakni pertanyaan mengenai apakah solusi yang dibuat benar-benar menyelesaikan masalah atau mencapai target tertentu, yang jawabannya berpotensi "tidak" atau berupa angka yang belum diketahui sebelum eksperimen.
   * **Pertanyaan Cek Mandiri:** *Mungkinkah jawabannya "tidak", atau berupa angka yang belum kamu ketahui? Jika tidak, yang kamu tulis masih tugas.*
3. **Prinsip 3 — Nyatakan kuantitas klaim: semua, sebagian, berapa (Slide 6 & Transkrip 06:51–08:10)**
   * **Inti Bahasan:** Gunakan pemahaman dari mata kuliah Logika Informatika mengenai kuantifikator (*semua, sebagian, beberapa, berapa*). Hampir tidak ada pengujian perangkat lunak yang hasilnya berlaku mutlak untuk *semua* kasus di dunia (misalnya menguji teknik baru pada 200 repositori tidak otomatis membuktikan teknik itu berlaku untuk semua perangkat lunak).
   * **Penerapan pada Evaluasi:** Jika menulis kalimat klaim tanpa kuantifikator (seperti *"Pengguna merasa terbantu"*), secara logika kalimat tersebut terbaca sebagai kuantor universal (*"Semua pengguna merasa terbantu"*), sehingga cukup satu kasus tandingan (*counter-example*) dari penguji untuk menggugurkan klaim tersebut. Tuliskan angka pastinya secara jujur.
   * **Pertanyaan Cek Mandiri:** *Tanpa kuantifikator, klaimmu terbaca "semua". Apakah datamu mendukung "semua"? Satu kasus tandingan cukup untuk menggugurkannya.*
4. **Prinsip 4 — "Lebih" selalu lebih daripada sesuatu (Slide 7 & Transkrip 08:11–09:05)**
   * **Inti Bahasan:** Setiap penggunaan kata sifat komparatif (*lebih cepat, lebih akurat, mengurangi, meningkatkan*) wajib memiliki titik pembanding (*baseline*) dan angka selisih yang jelas.
   * **Penerapan pada Evaluasi:** Mengklaim bahwa *"Avatar mengurangi kecemasan pengguna"* dengan hanya menguji satu kondisi pada 31 responden adalah klaim cacat karena tidak jelas lebih rendah dibandingkan apa. Bandingkan secara eksplisit dengan kondisi pembanding (misalnya antarmuka berbasis teks) beserta selisih skornya.
   * **Pertanyaan Cek Mandiri:** *Dibandingkan dengan apa? Cara manual, alat yang ada, versi tanpa komponenmu, atau kondisi sebelum perubahan?*
5. **Prinsip 5 — Tetapkan ukuran dan tanda gagal sebelum eksperimen (Slide 8 & Transkrip 09:06–11:15)**
   * **Inti Bahasan:** Sebelum melakukan pengujian, tetapkan kriteria lulus/gagal (*pass/fail criteria*) terlebih dahulu. Sekadar mencatat waktu respons (1 detik, 2 detik) lalu menampilkannya di tabel tanpa ambang batas keberhasilan tidak memberikan makna ilmiah.
   * **Kaitan dengan *Non-Functional Requirement* (NFR):** Dalam *Software Engineering*, *Functional Requirement* mendefinisikan fitur apa yang bisa dilakukan sistem, sedangkan **Non-Functional Requirement (NFR)** mendefinisikan ukuran kualitas sistem secara terukur. Jangan menulis NFR yang kabur seperti *"Sistem harus scalable, secure, atau efisien"* tanpa angka. Tuliskan definisi terukurnya di NFR (misal: *"Scalable artinya dapat diakses oleh X pengguna secara bersamaan dalam jendela waktu Y detik"*). Angka pada NFR inilah yang menjadi acuan pengujian di bab eksperimen.
   * **Pertanyaan Cek Mandiri:** *Bisakah orang lain memeriksa keberhasilanmu tanpa bertanya kepadamu? Hasil apa yang akan membuktikan klaimmu salah?*
6. **Prinsip 6 — Jangan menyimpulkan melampaui kasus yang diuji (Slide 9 & Transkrip 11:16–14:30)**
   * **Inti Bahasan:** Ruang lingkup kesimpulan harus setara dengan ruang lingkup pengujian. Deskripsikan karakteristik sampel yang diuji secara spesifik: apakah repositori berukuran kecil/sedang/besar, apakah *toy project* (kode pura-pura) atau sistem produksi nyata yang digunakan banyak orang, serta bahasa pemrograman apa yang diuji.
   * **Aturan Komplemen / Negasi Eksplisit (*Disjoint* dan Lengkap):** Layaknya percabangan `if-else` dalam pemrograman yang harus saling lepas (*disjoint*) dan mencakup seluruh kemungkinan (lengkap), saat menulis kesimpulan jangan hanya menyebutkan kasus yang berhasil diuji, tetapi **tuliskan juga secara eksplisit bagian komplemen/negasinya** (apa yang belum diuji). Selain itu, pahami himpunan kebenaran dan jenis-jenis oposisi/kebalikan proposisi (seperti kontradiktoris, bahwa *"Semua manusia adalah makhluk berakal budi"* tidak berarti *"Semua makhluk berakal budi adalah manusia"*).
   * **Pertanyaan Cek Mandiri:** *Berapa kasusmu, seberapa bervariasi, dan apakah kasus yang hasilnya buruk ikut dilaporkan?*
7. **Prinsip 7 — Klaim sebab harus menyingkirkan penjelasan lain (Slide 10)**
   * **Inti Bahasan:** *(Tercantum pada Slide 3 & Slide 10 PDF)* Ketika mengklaim hubungan sebab-akibat (misalnya penambahan komponen X menyebabkan peningkatan performa Y), penulis harus membuktikan bahwa variabel lingkungan lainnya dikontrol tetap sama sehingga perubahan hasil murni disebabkan oleh komponen X.
   * **Penerapan pada Eksperimen:** Sebutkan bahwa mesin, dataset, dan beban kerja dijaga identik di antara dua pengukuran, dan satu-satunya variabel yang berubah hanyalah komponen yang diuji.
   * **Pertanyaan Cek Mandiri:** *Adakah penjelasan lain untuk hasilmu? Apa yang berubah selain komponen yang kamu uji?*
8. **Prinsip 8 — Tuliskan premis yang tersembunyi (Slide 11 & Transkrip 14:31–17:44)**
   * **Inti Bahasan:** Karena mahasiswa telah menjalani pelatihan *Software Engineering* selama 4 tahun, sering muncul asumsi atau pengetahuan *baseline* di kepala yang dianggap "semua orang pasti sudah tahu". Dosen mencontohkan pengalaman membuat perangkat lunak untuk klien berlatar belakang dokter: *engineer* menganggap klien bodoh karena tidak paham dasar perangkat lunak, sementara dokter menganggap *engineer* bodoh karena tidak paham dasar medis. Dalam penulisan laporan, asumsi atau premis yang menjembatani bukti menuju kesimpulan harus dituliskan secara eksplisit.
   * **Kesalahan Klasik *Software Testing*:** Menulis *"Semua tes lulus, jadi implementasi sudah benar"* menyimpan premis tersembunyi yang salah bahwa kelulusan tes membuktikan kebenaran mutlak. Dalam ilmu pengujian perangkat lunak, *testing* hanya membuktikan tidak adanya *defect* pada *subset* kasus uji yang dijalankan (lulus 100, 1.000, atau 1.000.000 *test case* tidak menjamin *test case* ke-101 atau ke-1.000.001 akan lulus). Oleh sebab itu, sebutkan jumlah kasus uji dan ruang lingkup kasus apa yang dicakup maupun yang belum dicakup.
   * **Pertanyaan Cek Mandiri:** *Premis apa yang harus benar agar kesimpulanmu berlaku? Sudahkah kamu menuliskannya, dengan rujukan?*
9. **Prinsip 9 — Celah dan pilihan rancangan juga klaim (Slide 3 & Transkrip 17:45–19:15)**
   * **Inti Bahasan:** *(Tercantum pada tabel ringkasan Slide 3 dan dijelaskan secara lisan di transkrip)* Saat merumuskan *research gap* (celah penelitian, khususnya pada Tesis dan TA riset) atau menjelaskan keputusan perancangan, hindari kalimat tumpul yang menyapu rata seperti *"Penelitian sebelumnya masih terbatas"*.
   * **Penerapan pada Studi Literatur & Perancangan:** Tuliskan klaim celah dan keputusan desain dengan "pensil yang tajam": rinci secara akurat penelitian mana yang telah melakukan bagian X tetapi belum menangani kondisi Y, lalu jelaskan alasan memilih pendekatan A dibandingkan B beserta kriteria pemilihan dan *trade-off* (kompromi kelebihan/kekurangan) dari pilihan tersebut.
10. **Prinsip 10 — Kesimpulan menjawab pertanyaan, lengkap dengan batasnya (Slide 12–13 & Transkrip 19:16–20:54)**
    * **Inti Bahasan:** Seluruh dokumen TA/Tesis harus bersifat **dapat ditelusuri (*traceable*)**. Bab Kesimpulan harus menjawab secara langsung pertanyaan yang diajukan pada Rumusan Masalah di Bab I dengan merujuk pada bukti angka di bab evaluasi serta mencantumkan batasan pengujiannya.
    * **Pertanyaan Cek Mandiri:** *Apakah kesimpulanmu menjawab pertanyaan di Bab I? Apa batasnya, dan apa yang tidak kamu klaim?*

## 3. Prinsip Pemodelan Diagram dalam Software Engineering (Menit 20:55–25:30)

Selain penulisan teks, dosen menyoroti kesalahan mendasar yang sering berulang pada pembuatan diagram UML di laporan TA maupun kuliah proyek perangkat lunak:

1. **Kesalahan Fatal pada *Sequence Diagram* (Menulis Infrastruktur, Bukan Fungsionalitas):**
   * Mahasiswa sering menggambar *Sequence Diagram* dengan menamai kotak objek (*lifeline*) sebagai `Frontend`, `Backend`, dan `Database`.
   * **Koreksi:** *Sequence Diagram* wajib merepresentasikan interaksi antar-**komponen fungsional / tanggung jawab logis**, bukan lokasi penempatan (*deployment*) kode tersebut berada di sisi *frontend* atau *backend*.
2. **Gunakan *Deployment Diagram* untuk Menunjukkan Lokasi Fisik / Server:**
   * Jika ingin menunjukkan bahwa suatu bagian berada di *Backend Server*, *Database Server*, dan saling terhubung melalui protokol internet, gunakan **Deployment Diagram** (yang digambarkan dengan notasi balok tiga dimensi).
   * Di dalam masing-masing *node* pada *Deployment Diagram* tersebut terdapat kotak-kotak komponen perangkat lunak. Komponen-komponen fungsional di dalamnya itulah yang kemudian dijabarkan interaksinya pada *Sequence Diagram*.
3. **Pisahkan secara Tegas antara *Problem Space* dan *Solution Space* dalam Diagram:**
   * Saat membuat diagram apa pun (termasuk *Use Case Diagram* dengan relasi `<<include>>` dan `<<extend>>`, *Class Diagram*, maupun *Component Diagram*), penulis harus sadar apakah diagram tersebut sedang memodelkan **masalah (*problem domain*)** atau **solusi (*solution domain*)**.
   * Setiap elemen di dalam diagram harus menggunakan terminologi yang konsisten sesuai domain dan aspeknya (apakah sedang membahas aspek ruang masalah, aspek pembagian fungsional solusi, atau aspek *deployment* solusi).
4. **Saran Evaluasi Mandiri (*Self-Check* Sebelum Mengumpulkan Draf):**
   * Dosen menyarankan mahasiswa untuk melatih kepekaan dengan mengambil contoh laporan TA/Tesis tahun lalu, lalu menilai Bab I (Rumusan Masalah) dan Bab Kesimpulannya menggunakan ke-10 prinsip di atas.
   * Sebelum menyerahkan draf laporan kepada pembimbing, mahasiswa wajib menguji tulisannya sendiri menggunakan daftar 10 prinsip tersebut.

## 4. [DITANDAI KHUSUS] Poin-Poin Umum & Penting dari Sesi Asistensi (Menit 28:55–02:09:12)

> **Catatan Penanda:** Bagian di bawah ini diekstrak dari sesi asistensi per topik/mahasiswa (setelah menit 28:55). Detail yang terlalu spesifik pada individu telah disaring, dan hanya **panduan metodologis, strategi pengerjaan, rekomendasi *tools*, serta wawasan riset umum** yang relevan bagi seluruh mahasiswa bimbingan yang dirangkum di sini.

### A. Strategi Studi Literatur (Bab II) dan Pencarian Referensi

* **Teknik *Snowballing* Dua Arah (Menit 34:15–35:30 & 1:30:10):**
  * Saat memulai studi literatur dari satu artikel rujukan awal (*seed paper* atau disertasi pembimbing), lakukan pelacakan literatur dua arah:
    1. *Backward Snowballing (Mundur):* Telusuri daftar referensi yang disitasi di dalam *paper* tersebut.
    2. *Forward Snowballing (Maju):* Gunakan Google Scholar untuk melihat daftar *paper* terbaru yang mensitasi *paper* awal tersebut.
  * Setelah terkumpul, kelompokkan literatur ke dalam kategori-kategori tematik (misalnya: kelompok paper tentang visualisasi, kelompok paper tentang evolusi arsitektur, kelompok paper tentang klasifikasi).
* **Gunakan DBLP (`dblp.org`) untuk Riset Ilmu Komputer (Menit 1:54:15–1:55:10):**
  * Selain Google Scholar yang sifatnya sangat umum lintas disiplin, gunakan **[DBLP](https://www.google.com/search?q=https%3A%2F%2Fdblp.org)** sebagai katalog bibliografi yang khusus mengindeks publikasi *Computer Science*.
* **Menyikapi Preprint di `arXiv` untuk Topik yang *Fast-Moving* (Menit 2:07:00–2:08:25):**
  * Secara akademis formal, artikel di `arXiv` adalah *preprint* yang belum melalui *peer-review* pakar sehingga normalnya bukan rujukan valid untuk disitasi sebagai literatur primer.
  * Namun, pada bidang yang bergerak sangat cepat (*fast-moving*) seperti *AI/Coding Agents* atau *LLM*, banyak inovasi terbaru yang langsung dirilis sebagai proyek *open-source* atau naskah `arXiv` sebelum sempat terbit di jurnal/konferensi. Dalam kondisi tersebut, `arXiv` tetap boleh digunakan sebagai bahan eksplorasi awal dan titik berangkat *snowballing*.
* **Pemanfaatan AI untuk *Brainstorming* Literatur (Menit 1:11:30 & 1:52:00):**
  * Mahasiswa diperbolehkan memanfaatkan AI untuk membantu merumuskan kata kunci (*keywords*) pencarian literatur, memahami langkah-langkah metodologi studi literatur, serta memetakan sub-topik dari arahan pembimbing.

### B. Manajemen Pengerjaan TA/Tesis: Pendekatan *Spiral* vs Sekuensial

* **Jangan Hanya Menulis Bab I–II Tanpa Mencoba Kode (*Spiral Approach*) (Menit 44:00–45:55):**
  * Meskipun secara kurikulum semester berjalan baru menuntut pengumpulan dokumen Bab I dan Bab II (atau pada S2: semester 1 khusus studi literatur dan semester 2 proposal), dosen **tidak menyarankan pengerjaan secara sekuensial kaku** (hanya membaca dan menulis teori selama satu semester penuh).
  * Gunakan pendekatan **spiral/iteratif**: sambil menyusun Bab I dan II, mulailah menulis prototipe kode atau mengeksekusi *source code/repository* dari *paper* rujukan.
  * **Manfaat Utama:** Eksperimen awal dengan kode akan mempertajam pemahaman masalah dan mendeteksi lebih dini apabila suatu ide ternyata tidak dapat dijalankan, sudah pernah diselesaikan orang lain, atau keliru secara konseptual—sehingga mahasiswa tidak terjebak merancang sesuatu di Bab I–II yang menjadi bumerang di semester implementasi.
* **Kebiasaan *Weekly Report* dan Berbagi Literatur Antar-Mahasiswa (Menit 42:10 & 1:53:10):**
  * Mahasiswa yang memiliki topik beririsan dianjurkan saling berbagi (*sharing*) temuan *paper* agar proses pemetaan literatur lebih cepat dan komprehensif.
  * Biasakan mengirim laporan progres mingguan (*weekly report*) yang tidak hanya mencantumkan daftar judul *paper* yang dibaca, melainkan merangkum **apa intisari yang berhasil dipahami** dari bacaan tersebut.

### C. Wawasan Metodologis & Teknis Riset Rekayasa Perangkat Lunak (Bagi Topik Terkait)

* **Paradigma *Forward Engineering* vs *Reverse Engineering* (Menit 52:00–56:30):**
  * Banyak konsep arsitektur perangkat lunak—seperti *Role Stereotypes* (Information Holder, Service Provider, Controller, dll.), *Design Patterns*, hingga *Architectural Tactics* (rujukan utama: buku ***Software Architecture in Practice***)—awalnya diciptakan untuk digunakan secara *forward* (membantu merancang sistem dari nol).
  * Namun, dalam penelitian *Software Engineering*, konsep-konsep tersebut sangat menarik bila ditarik secara *reverse/backward*: mengekstraksi dan mengidentifikasi apakah suatu *source code* eksisting menerapkan taktik/pola tertentu, lalu menilai bagian sistem mana yang sudah memenuhi atribut kualitas (seperti *maintainability*) dan bagian mana yang belum memiliki bukti.
* **Metode Validasi Taksonomi: *Dimensional Analysis* vs Evaluasi *Expert* (Menit 1:34:00–1:41:00):**
  * Ketika meneliti atau memvalidasi suatu pengelompokan/taksonomi kategori (misalnya kategori relasi antar-kelas), ada dua cara validasi:
    1. *Analisis Dimensi (Dimensional Analysis):* Menguraikan kategori-kategori yang ada ke dalam beberapa dimensi ortogonal (contoh dimensi: *"Apakah mengubah state objek atau tidak?"*, seperti membedakan `query/retrieve` vs `command/mutate`). Dengan memetakan kategori ke dalam matriks/kuadran dimensi, peneliti dapat melihat secara objektif apakah ada kuadran yang kosong (kategori yang belum teridentifikasi) atau tumpang tindih.
    2. *Melibatkan Expert Industri:* Mengumpulkan *senior/rockstar developer* untuk menilai taksonomi. Namun, pendekatan ini jauh lebih berat dari sisi *effort* karena sulit mencari waktu luang praktisi ahli, harus memvalidasi tingkat kepakaran mereka, dan harus mengukur kesepakatan antar-pakar (*inter-rater agreement*). Oleh karena itu, memulai dari *analisis dimensi* jauh lebih terukur dan *feasible*.
* **Strategi Pemanfaatan LLM dan Model Terstruktur untuk Riset Kode (Menit 56:40 & 1:20:30–1:22:30):**
  * **Masalah Biaya Inferensi LLM & Pembuatan *Ground Truth*:** Menggunakan LLM berukuran besar secara langsung untuk mengklasifikasi kode memang lebih fleksibel dibanding aturan *heuristic* kaku, tetapi biaya inferensinya mahal. Salah satu hipotesis riset yang menarik adalah menggunakan konsensus dari beberapa model LLM berbeda (misalnya 5 model) untuk melabeli dataset dan membangun *ground truth* berkualitas tinggi (jika 5 model sepakat, label dianggap valid; jika terbelah, menjadi kasus menarik untuk dianalisis), lalu menggunakan *ground truth* tersebut untuk melatih model khusus yang lebih kecil dan hemat biaya inferensi.
  * **Eksplorasi Model Generatif Terstruktur (seperti JEPA) & *Tools* Analisis Kode (Spoon):** Untuk analisis kode sumber Java, *library* **Spoon** (buatan tim riset di Prancis) direkomendasikan untuk memproses AST/struktur kode. Selain itu, model AI yang menerima input berupa struktur data/graf dan menghasilkan prediksi terstruktur (bukan sekadar teks bahasa alami) layak dieksplorasi untuk klasifikasi komponen perangkat lunak.
