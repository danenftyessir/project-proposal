# TO DO Bab I

**Status:** Bab I kini DRAF 23 (per 9 November 2026) dan **belum selesai**. Naskah masih memuat 60 penanda.
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

Kode dalam kurung di akhir butir hanya untuk menelusuri catatan lengkap di folder `memory/`.

## 1. Ringkasan status per subbab

| Subbab | Status | Penanda | Keterangan singkat |
|---|---|---|---|
| I.1 Latar Belakang | DRAF | 14 | Celah penelitian dan posisi penelitian sudah ditulis dan dipecah menjadi paragraf per fokus (paragraf 16–25). Banyak penanda menunggu data RSIA dan persetujuan pembimbing. |
| I.2 Rumusan Masalah | DRAF | 15 | Dua pertanyaan, masing-masing dijawab terpisah untuk rawat inap dan rawat jalan. Ambang, selisih minimum, satuan hitung, dan cara kombinasi belum ditetapkan. |
| I.3 Tujuan | DRAF | 9 | Ukuran keberhasilan mengikuti syarat di I.2. Kondisi keabsahan jawaban akan ditetapkan sebelum pengujian, tetapi isinya belum ada. |
| I.4 Batasan | DRAF | 7 | Batas rawat jalan, jumlah kasus, susunan penilai, dan arti penguncian belum ditetapkan. |
| I.5 Metodologi | DRAF | 15 | Lima tahap. Tahap kelima mencakup penyusunan jawaban. Banyak penanda memuat usulan saya untuk butir tim. |
| **Total** | | **60** | |

Catatan:

- Pemeriksaan terarah terakhir atas I.2 paragraf 6 dan I.3 paragraf 2 tidak menemukan masalah berat atau sedang. Yang tersisa hanya catatan ringan.
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

### 2.2 Usulan saya untuk butir tim, menunggu persetujuan tim

Usulan berikut tercatat di naskah sebagai penanda [MENUNGGU KEPUTUSAN TIM]. Persetujuan tim **belum** ada.

- Rawat jalan dijawab terpisah dari rawat inap secara bersyarat. Bila dokumen yang setara resume medis tidak ada atau tidak memadai, hasil rawat jalan dilaporkan "tidak dapat dinilai", bukan "tidak". Bentuk dokumen rawat jalan di RSIA belum dipastikan. (D-76; Q-B1-f; Q-TEAM butir 4)
- Kombinasi dibentuk dengan penyatuan (*union*) semua temuan kedua komponen. (D-77)
- "Di atas ambang" berarti paling sedikit sama dengan ambang (≥). (D-78)
- Presisi dan recall dihitung dengan agregasi mikro, dan nilai 0/0 dilaporkan "tidak terdefinisi". (D-79)
- Data pengembangan diberi label oleh saya sendiri. Akibatnya label itu tidak independen dan menjadi keterbatasan penelitian. (D-69)
- Kasus uji dipilih secara acak dengan benih tetap yang dicatat, per jenis perawatan. Temuan komponen AI di luar daftar jenis ketidaksesuaian dihitung terpisah. Pertanyaan apakah daftar jenis wajib memuat jenis yang menuntut penelaahan konteks belum terjawab. (D-70; Q-B1-cb)
- Kedua komponen menyasar seluruh daftar jenis ketidaksesuaian. (D-71)
- Gaya sitasi yang diusulkan adalah APA, menunggu tim, pembimbing, dan pedoman prodi. Naskah masih memakai konvensi penulis-tahun sementara. (K1, D-80)

### 2.3 Masih harus diputuskan

- [ ] **Apa arti "saling melengkapi", dan benarkah jawaban uji "tidak memberi informasi" tentangnya?** Naskah memperlakukannya sebagai sifat rancangan yang tidak diukur. Ada keberatan bahwa istilah itu juga memuat bagian empiris, dan hasilnya bergantung pada mekanisme kombinasi.
  Mengapa penting: keberatan ini menantang keputusan yang sudah saya ambil tentang makna istilah dan tentang tafsir jawaban "tidak".
  Pemutus: pembimbing dan tim. (Q-B1-cm; F-A05-0152, F-A11-0038; D-74, D-81)

- [ ] **Bagaimana ketersediaan dokumen rawat jalan dinilai di tahap pertama?** Yang belum ditetapkan: kriteria "ada dan memadai", satuan penilaian, dan siapa yang menilai.
  Mengapa penting: penilaian ini menentukan apakah jawaban rawat jalan dapat disusun, dan penilaian ini bergantung pada batas operasional rawat jalan di I.4.
  Pemutus: tim dan RSIA. (Q-B1-cn; F-A05-0157)

- [ ] **Berapa ambang dan selisih minimum, dan bagaimana menghitungnya?** Yang belum ditetapkan: angka ambang; selisih minimum (ditetapkan tim, tetapi bentuknya, mutlak atau relatif, dan operator batasnya belum ditetapkan); satuan hitung; cara menilai "lebih tinggi" beserta ketidakpastiannya; kondisi keabsahan jawaban per jenis perawatan; dan perlakuan hasil di luar "ya" atau "tidak".
  Mengapa penting: tanpa ketetapan ini, rumusan masalah belum dapat dijawab. Angkanya masih tertahan sampai tim membahasnya, dan data agregat belum tersedia.
  Pemutus: tim dan pembimbing. (D-19; Q-B1-bg, Q-B1-q, Q-B1-cc; F-A11-0034, F-A11-0036, F-A11-0037)

- [ ] **Apa arti "penguncian" CPPT dan resume medis?** Dokumen tim mengandaikan keduanya dikunci setelah pelayanan selesai. Keterangan lisan dari RSIA, yang disampaikan lewat saya dan belum terverifikasi, berbeda.
  Mengapa penting: batas kesimpulan Bab I bergantung pada arti penguncian ini.
  Pemutus: tim dan RSIA. (Q-B1-ba)

- [ ] **Apa batas "rawat jalan terbatas", dan seperti apa bentuk dokumen rawat jalan di RSIA?**
  Mengapa penting: batasan masalah, pembagian data, dan jawaban rawat jalan bergantung pada hal ini.
  Pemutus: tim dan RSIA. (Q-B1-f; Q-TEAM butir 4)

- [ ] **Apakah pembimbing menyetujui empat rumusan masalah capstone dan judul baru?** Judul baru yang tercatat di dokumen penyelarasan tim tanggal 30 Oktober masih menunggu persetujuan pembimbing.
  Mengapa penting: rumusan masalah menjadi dasar tujuan dan metodologi, dan judul memengaruhi seluruh naskah.
  Pemutus: pembimbing. (Q-TEAM butir 9, K2)

- [ ] **Bagaimana menangani risiko pada rawat jalan bila hanya ada satu jenis ketidaksesuaian, dan apakah jumlah kasus per jenis perawatan cukup?**
  Mengapa penting: bila jenis ketidaksesuaian di rawat jalan sangat sedikit, presisi atau recall dapat mencapai batas atas sehingga uji "lebih tinggi" kehilangan makna. Kecukupan kasus per jenis perawatan juga belum dapat dinilai.
  Pemutus: tim dan pembimbing. (F-A11-0015, F-A11-0016)

- [ ] **Bagaimana menyelesaikan pertentangan antarusulan untuk butir tim?**
  1. Penyatuan semua temuan membuat uji recall condong ke "ya", sedangkan presisi kombinasi sulit melampaui kedua komponen. (F-A11-0023)
  2. Satuan pengacakan belum seragam: per pasien atau per episode. (F-A11-0025)
  3. Usulan agar kedua komponen menyasar seluruh jenis ketidaksesuaian berbeda dari pembagian yang tersirat di dokumen penyelarasan tim. (F-A11-0026)
  4. Agregasi mikro sudah diusulkan, padahal satuan hitungnya belum diputuskan. (F-A11-0027)
  5. Nilai 0/0 belum dipetakan ke jawaban "ya" atau "tidak". (F-A11-0024, F-A05-0150)

  Mengapa penting: usulan-usulan ini saling memengaruhi hasil uji, sehingga perlu dibahas bersama sebelum ditetapkan.
  Pemutus: tim. (Q-B1-o, Q-B1-r, Q-B1-by, Q-B1-bz)

- [ ] **Bagaimana temuan Dietrich dipakai sebagai "pertimbangan", dan apakah kriteria pemilihan kombinasi perlu membedakan pasangan komponen?** Ada pula risiko bahwa jawaban pertanyaan pertama bergantung pada tahap kelima.
  Mengapa penting: ketiganya menyangkut ketepatan argumen di latar belakang dan urutan metodologi.
  Pemutus: saya, lalu pembimbing. (F-A05-0142, F-A05-0144, F-A05-0148, F-A11-0032)

- [ ] **Apa cakupan "sumber yang ditelaah", dan mengapa studi Zhang tidak dihitung sebagai dukungan?** Naskah memakai "studi yang ditelaah pada Bab II" untuk I.1 paragraf 18–24 dan "sumber yang ditelaah dalam proposal ini" untuk kalimat batas sumber.
  Mengapa penting: klaim kekosongan literatur hanya sah dalam cakupan yang dinyatakan.
  Pemutus: saya, lalu pembimbing. (Q-B1-cg; F-A07-0087, F-A09-0235)

- [ ] **Apakah pemeriksaan manual perlu menjadi pembanding?** Saya mempertahankan pembanding berupa masing-masing komponen dan menyatakan batas perbandingannya, tetapi persetujuan pembimbing belum ada.
  Mengapa penting: pembanding menentukan apa yang dapat disimpulkan dari hasil penelitian.
  Pemutus: pembimbing. (D-22, D-72; F-A05-0109)

## 3. Perlu dikerjakan penulis setelah ada keputusan

- [ ] Menyelaraskan Bab II dengan fakta yang sudah dipakai di Bab I tetapi belum ada di Bab II: perbandingan Zeba dengan model bahasa besar dan peran kemiripan kosinus, skala penilaian Skrabic, rubrik Li, dan kategori Dietrich. Sebelumnya perlu dipastikan berkas Bab II mana yang aktif. (Q-B1-bn; F-A08-0103)
- [ ] Mengoreksi kalimat di I.1 paragraf 16 dan 17 yang menyederhanakan sumber:
  - Skrabic: perlu disebut bahwa 99 dari 102 kesalahan disisipkan, dan frasa "tanpa rujukan" seharusnya "tanpa retrieval".
  - Zeba: perlu disebut bahwa keluaran juga memuat pernyataan rujukan dan jenis pemeriksaan.
- [ ] Menuliskan perlakuan pasangan ibu dan bayi pada pembagian data setelah ada keputusan tim. (Q-TEAM butir 6)
- [ ] Mempersempit klaim di I.5 bahwa ukuran tidak berasal dari penilaian saya. Klaimnya cukup menyatakan sumber acuan label dan penilaian. (F-A05-0134, F-A07-0068)
- [ ] Merapikan sisa catatan bahasa kecil, antara lain:
  - sebutan "pemeriksaan berbasis aturan" di I.1 paragraf 18;
  - pasangan frasa "Bila selisih minimum dipakai" dan "Dalam hal selisih minimum dipakai" di I.2 paragraf 6;
  - frasa "seperti ambang" dan anteseden "hal itu";
  - bentuk baku "benih tetap", yang belum diverifikasi.
  (F-A09-0230 sampai F-A09-0244; F-A07-0088, F-A07-0089)
- [ ] Membersihkan bagian Catatan kerja di berkas naskah dari butir yang sudah usang sebelum penyerahan. Bagian itu bukan bagian proposal.
- [ ] Setelah ada keputusan tim, mengganti penanda dengan teks final serta memperbarui tujuan dan ukuran keberhasilan.
- [ ] Menyelaraskan Bab I dengan proposal Raihaan dan Abizzar. Kesesuaian lintas proposal belum dapat diverifikasi.

## 4. Perlu diverifikasi

- [ ] Rujukan Permenkes 26/2021 halaman 48 sampai 54 di I.4 belum dicocokkan dengan dokumennya. (Q-B1-bf)
- [ ] Jumlah episode per jenis perawatan dan bentuk dokumen rawat jalan belum diketahui karena data agregat belum tersedia. Akibatnya, kecukupan jumlah kasus belum dapat dinilai. (Q-A04-c, Q-B1-ci)
- [ ] Format akhir sitasi dan pedoman prodi belum dikonfirmasi. Templat individu tidak menetapkan gaya sitasi, dan header serta footer templat belum diperiksa.
- [ ] Sitasi di I.1 paragraf 16–22 sudah dicek ke halaman PDF (Dietrich, Zeba, Li, Zhang, Skrabic, dan Jaganathan). Namun, klaim kekosongan literatur hanya berlaku bagi sumber yang ditelaah, bukan hasil penelusuran sistematis.

## 5. Administratif

- [ ] Commit berkas `bab1/Bab_I_Draft.md` (DRAF 23) dan catatan di `memory/` setelah disetujui. Push belum terverifikasi. (G3)
- [ ] Menelusuri asal perubahan pada beberapa berkas yang sudah lama diperingatkan: CLAUDE.md, indeks sumber, `verify_claims.py`, dokumen migrasi Bab I dan Bab II, serta dua modul Bab II.
- [ ] Menyesuaikan build modular Bab I (folder `modular/`) dengan DRAF 23. Modul Bab I dan Bab II di folder itu belum mencerminkan DRAF 23.
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
