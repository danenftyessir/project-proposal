# Bab IV — Rencana Pelaksanaan

> **Status:** berkas ini memuat subbab IV.1–IV.3; jadwal memakai minggu relatif terhadap awal TA 2 dan belum dipadankan dengan kalender resmi. Bab ini tidak memuat sitasi.

---

## Naskah

## BAB IV RENCANA PELAKSANAAN

## IV.1 Tahapan Pelaksanaan

Pelaksanaan pada Tugas Akhir 2 (TA 2) dibagi menjadi tujuh tahap, yaitu T1 sampai T7, yang merinci lima tahap metodologi pada subbab I.5. Penyiapan data dikerjakan pada T1; pembangunan pemeriksaan pada T2, T3, dan T4; pelabelan oleh tenaga ahli pada T5; pengujian deteksi pada T6; serta penilaian kejelasan dan penyusunan jawaban penelitian pada T7. Pembangunan pemeriksaan dipecah menjadi tiga tahap mengikuti modul pada subbab III.2.2 karena keluaran setiap modul menjadi masukan modul berikutnya. Rentang minggu setiap tahap yang disebut pada subbab ini mengikuti jadwal pada Tabel IV.1 (subbab IV.2).

T1, yaitu penyiapan data dan kontrak antarblok, berlangsung pada minggu 1–3. Kontrak antarblok adalah kesepakatan dengan tim tentang format berkas masukan dan skema temuan (subbab III.2.3). Tahap ini mencakup langkah 2 dan 3 subbab III.2.4 serta bagian awal langkah 1, yaitu penetapan format berkas masukan. Pada tahap ini, format ekspor catatan perkembangan pasien terintegrasi (CPPT), resume medis, dan dokumen ringkasan pelayanan dikonfirmasi, izin data dari rumah sakit ibu dan anak (RSIA) mitra diurus, dan skema proposisi serta skema temuan disepakati dengan tim. Definisi operasional keempat kategori ketidaksesuaian dan panduan pelabelan juga disusun pada T1 karena tenaga ahli melabeli data uji berdasarkan kategori yang telah ditetapkan sebelum T5. Dokumen terdeidentifikasi yang telah disatukan per episode oleh bagian capstone *Health Data & Cross-Episode Reconciliation* diperiksa kelengkapannya. Jumlah minimum data uji (subbab I.3) ditetapkan sebelum data dibagi menjadi data pengembangan dan data uji pada tingkat pasien sesuai dengan subbab I.5. Keluaran T1 adalah skema yang telah disepakati, definisi operasional keempat kategori, panduan pelabelan, pembagian data, dan sampel episode terdeidentifikasi untuk pengembangan.

Pembangunan pemeriksaan dikerjakan pada data pengembangan. Pada T2 (minggu 3–5), M1 dibangun melalui sisa langkah 1 dan langkah 4 subbab III.2.4. Pembangunan ini mencakup penyusunan pengurai dokumen, pemilihan versi terakhir resume medis atau dokumen ringkasan pelayanan yang dapat dibuktikan tersedia sebelum pengajuan klaim, dan segmentasi. Keluarannya adalah M1 yang berjalan pada data pengembangan. Pada T3 (minggu 5–10), langkah 5–7 dikerjakan untuk membangun kedua komponen pemeriksaan, yaitu M2a (leksikon, pola, dan aturan) dan M2b (indeks *retrieval* dan *prompt* pembentukan temuan). Keluarannya adalah temuan M2a dan M2b pada data pengembangan sesuai dengan skema temuan. Langkah 8 dan 9 dikerjakan pada T4 (minggu 10–11). M3, yaitu penggabungan (*union*) dan deduplikasi temuan, diuji dengan kasus yang sengaja dibuat tumpang tindih dan menghasilkan daftar temuan unik. Perangkat evaluasi M4 diuji dengan kasus buatan agar siap dijalankan ketika pengujian dimulai.

T5, yaitu pelabelan oleh tenaga ahli, berlangsung pada minggu 6–12. Dua tenaga ahli melabeli data uji secara independen, dan perbedaan penilaian diselesaikan oleh tenaga ahli ketiga melalui adjudikasi. Keluarannya adalah label acuan dan kesepakatan awal antarpenilai yang dihitung dengan Krippendorff’s alpha nominal. Subbab I.5 menyebut pelabelan sebelum pembangunan pemeriksaan, sedangkan pada jadwal ini pelabelan dimulai pada minggu 6, ketika pembangunan masih berjalan. Penempatan ini dipilih agar label acuan sudah siap saat pengaturan sistem dibekukan.

Gerbang pembekuan pengaturan sistem pada minggu 13 memisahkan pembangunan dari pengujian. Pada gerbang ini, seluruh pengaturan sistem dibekukan, yaitu model bahasa besar (*large language model*, LLM) beserta versi dan parameter *decoding*-nya, *prompt*, parameter *retrieval*, leksikon dan aturan M2a, serta kriteria deduplikasi (subbab III.2.4). Aturan kecocokan temuan dengan label acuan pada M4 juga ditetapkan paling lambat pada gerbang ini dan tidak diubah sesudahnya. Sebelum gerbang tersebut, data uji dipakai untuk pelabelan oleh tenaga ahli, tetapi tidak dipakai untuk membangun, menyetel, atau menjalankan pemeriksaan.

T6, yaitu pengujian deteksi, berlangsung pada minggu 13–15. Ketiga konfigurasi yang dibandingkan (subbab I.5 dan III.2.2) dijalankan pada data uji. Temuan yang diukur adalah temuan M2a, temuan M2b, dan temuan konfigurasi kombinasi yang dihasilkan M3. M4 lalu mencocokkan temuan dengan label acuan, menghitung *precision* dan *recall* beserta interval kepercayaan yang diperoleh dengan *paired cluster bootstrap*, serta menabulasikan hasil per kategori dan per komponen asal. Perhitungan tersebut dilakukan terpisah untuk rawat inap dan rawat jalan. Keluaran T6 adalah hasil pengujian yang menjawab pertanyaan penelitian 1 dan 2.

T7, yaitu penilaian kejelasan dan penyusunan jawaban penelitian, berlangsung pada minggu 15–20. Instrumen penilaian dan para penilainya disiapkan sebelum minggu 15. Tenaga ahli dan pengguna proksi menilai, dengan skala 1–5, kejelasan alasan dan rujukan pada temuan konfigurasi kombinasi yang dihasilkan M3. Kesepakatan antarpenilai dihitung dengan Krippendorff’s alpha ordinal. Hasil penilaian ini menjawab pertanyaan penelitian 3. Jawaban atas ketiga pertanyaan penelitian disusun terpisah untuk rawat inap dan rawat jalan, lalu jawaban atas pertanyaan penelitian 1 dan 3 dibandingkan dengan ukuran keberhasilan pada subbab I.3. Seluruh hasil kemudian dituangkan dalam laporan TA.

## IV.2 Jadwal

Jadwal pada Tabel IV.1 disusun dengan asumsi TA 2 berlangsung selama 20 minggu. Minggu dihitung dari awal TA 2 dan akan dipadankan dengan tanggal setelah kalender resmi diumumkan [DATA BELUM TERSEDIA: kalender resmi TA 2]. Pembangunan pemeriksaan mengisi minggu 3–11, sedangkan pelabelan mengisi minggu 6–12, sehingga keduanya selesai sebelum gerbang pembekuan pengaturan sistem pada minggu 13. Minggu 12 tidak diisi tahap pembangunan dan menjadi cadangan sebelum gerbang. Pengujian deteksi serta penilaian kejelasan dan penyusunan jawaban penelitian mengisi minggu 13–20.

Tabel IV.1. Jadwal pelaksanaan mingguan

| Tahap | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T1 Penyiapan data dan kontrak antarblok | ■ | ■ | ■ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| T2 Pembangunan M1 |  |  | ■ | ■ | ■ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| T3 Pembangunan M2a dan M2b |  |  |  |  | ■ | ■ | ■ | ■ | ■ | ■ |  |  |  |  |  |  |  |  |  |  |
| T4 Pembangunan penggabung M3 dan perangkat evaluasi M4 |  |  |  |  |  |  |  |  |  | ■ | ■ |  |  |  |  |  |  |  |  |  |
| T5 Pelabelan oleh tenaga ahli |  |  |  |  |  | ■ | ■ | ■ | ■ | ■ | ■ | ■ |  |  |  |  |  |  |  |  |
| Gerbang pembekuan pengaturan sistem |  |  |  |  |  |  |  |  |  |  |  |  | ◆ |  |  |  |  |  |  |  |
| T6 Pengujian deteksi |  |  |  |  |  |  |  |  |  |  |  |  | ■ | ■ | ■ |  |  |  |  |  |
| T7 Penilaian kejelasan dan penyusunan jawaban penelitian |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ■ | ■ | ■ | ■ | ■ | ■ |

Keterangan: ■ menandai minggu pelaksanaan tahap; ◆ menandai gerbang pembekuan pengaturan sistem.

## IV.3 Risiko Pelaksanaan

Tabel IV.2 memuat lima risiko utama pelaksanaan. R1–R4 bersifat negatif karena dapat menunda tahap atau membuat pertanyaan penelitian tidak dapat dijawab, sedangkan R5 bersifat positif karena mempercepat pelaksanaan bila terjadi. Tindakan untuk risiko negatif berupa mitigasi, sedangkan tindakan untuk R5 berupa pemanfaatan. Tindakan yang melibatkan pembimbing, RSIA mitra, atau tim merupakan rencana penulis dan belum disepakati dengan pihak tersebut.

Tabel IV.2. Risiko pelaksanaan dan tindakannya

| No. | Risiko | Jenis | Dampak | Tindakan |
| --- | --- | --- | --- | --- |
| R1 | Akses data CPPT, resume medis, dan dokumen ringkasan pelayanan dari RSIA mitra terlambat, format ekspornya tidak dapat diproses, atau pasokan berkas terdeidentifikasi per episode (termasuk kode kelompok pasien) dari bagian capstone *Health Data & Cross-Episode Reconciliation* terlambat | Negatif | T1 sampai T3 mundur, pembangunan pemeriksaan berjalan tanpa data nyata, dan pelabelan pada T5 tertunda sehingga label acuan mungkin belum siap pada gerbang minggu 13 | Mitigasi: mengajukan permintaan data segera setelah proposal disetujui; memakai data sintetis untuk membangun M1, M2a, M2b, dan M3, sedangkan penyetelan tetap memakai data pengembangan nyata; tidak memakai data uji untuk membangun, menyetel, atau menjalankan pemeriksaan sebelum gerbang; tidak melewati gerbang sebelum label acuan siap; bila data terlambat, menyerap keterlambatan dengan minggu cadangan (minggu 12) lebih dulu; bila keterlambatan melampaui minggu cadangan, menggeser gerbang beserta T6 dan T7 serta mencatat pergeserannya, dengan konsekuensi waktu T6 dan T7 berkurang atau jadwal perlu disesuaikan setelah dibahas dengan pembimbing |
| R2 | Tenaga ahli pelabel (termasuk tenaga ahli ketiga untuk adjudikasi) atau penilai kejelasan (tenaga ahli dan pengguna proksi) tidak tersedia, atau pelabelan dan penilaian berjalan lambat | Negatif | Label acuan belum siap pada minggu 13 sehingga pertanyaan penelitian 1 dan 2 tidak dapat dijawab, atau penilaian kejelasan tertunda sehingga pertanyaan penelitian 3 tidak dapat dijawab pada T7 | Mitigasi: menyepakati nama tenaga ahli dan jatah waktunya pada T1; menyesuaikan ukuran data uji dengan jatah waktu tersebut tanpa menurunkannya di bawah jumlah minimum yang ditetapkan pada T1; menyiapkan panduan pelabelan dan alat pelabelan sederhana; menjalankan pelabelan sesuai dengan jadwal T5; menyiapkan instrumen penilaian kejelasan dan menyepakati penilainya sebelum minggu 15; bila jumlah minimum tidak tercapai, menyatakan hasil ukuran keberhasilan yang terdampak sebagai tidak dapat dinilai sesuai dengan subbab I.3 |
| R3 | Versi dokumen atau *snapshot* prapengajuan tidak tersimpan di sistem informasi manajemen rumah sakit (SIMRS) | Negatif | Batasan pada subbab I.4 tentang versi terakhir sebelum pengajuan klaim tidak dapat dipenuhi | Mitigasi: mengonfirmasi ketersediaan versi pada T1; bila tidak tersedia, melaporkannya sebagai keterbatasan dan memakai versi terakhir yang tersedia dengan catatan eksplisit bahwa versi itu tidak otomatis mewakili kondisi prapengajuan |
| R4 | Kebijakan privasi melarang pengiriman teks klinis ke LLM berbasis *cloud*, atau biaya antarmuka pemrograman aplikasi (*application programming interface*, API) melampaui anggaran | Negatif | Pilihan model berubah di tengah pelaksanaan. Karena proposisi M1 dibentuk dengan LLM dan dipakai kedua komponen, perubahan itu memengaruhi ketiga konfigurasi, bukan hanya M2b | Mitigasi: menanyakan kebijakan tersebut kepada pembimbing dan RSIA mitra pada T1; menyiapkan alternatif model lokal; memastikan teks telah dideidentifikasi sebelum diproses model |
| R5 | Pembimbing dan RSIA mitra memberi persetujuan lebih cepat daripada jadwal yang direncanakan sehingga data nyata tersedia sebelum TA 2 dimulai | Positif | Data nyata tersedia lebih awal daripada jadwal T1 (minggu 1–3) sehingga pemeriksaan kelengkapan dan pembagian data pada T1 dapat dimulai lebih awal | Pemanfaatan: menyiapkan daftar permintaan data dan pertanyaan wawancara sebelum proposal disetujui agar keduanya dapat diajukan segera setelah persetujuan diperoleh |
