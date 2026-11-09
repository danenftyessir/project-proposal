# TO DO Bab I

**Status:** Bab I masih DRAF 19 (per 9 November 2026) dan **belum selesai**.
Ini dokumen kerja untuk saya dan anggota tim, **bukan** bagian naskah proposal.

**Tenggat:**

- Tenggat lunak ke pembimbing, 6 November 2026, sudah lewat.
- Tenggat final ke pusat: 10 November 2026.

**Istilah yang dipakai di bawah:**

- **CPPT** adalah catatan perkembangan pasien terintegrasi.
- **Resume medis** adalah ringkasan perawatan pasien yang disusun di akhir perawatan.
- **Pemeriksaan rule-based** adalah pemeriksaan dengan aturan yang ditulis secara eksplisit.
- **Pemeriksaan AI berbasis RAG** adalah pemeriksaan dengan model bahasa yang lebih dulu mengambil dokumen acuan sebelum menghasilkan jawaban. RAG adalah singkatan dari *retrieval-augmented generation*.
- **Komponen** berarti salah satu dari dua pemeriksaan di atas. **Kombinasi** berarti gabungan keduanya.
- **Presisi** adalah bagian temuan sistem yang memang benar. **Recall** adalah bagian ketidaksesuaian sebenarnya yang berhasil ditemukan sistem.
- **Penanda** adalah catatan dalam kurung siku di naskah, misalnya [MENUNGGU KEPUTUSAN] atau [DATA BELUM TERSEDIA].

Kode dalam kurung di akhir butir hanya untuk menelusuri catatan lengkap di folder `memory/`.

## 1. Ringkasan status per subbab

| Subbab | Status | Penanda | Keterangan singkat |
|---|---|---|---|
| I.1 Latar Belakang | DRAF | 15 | Latar belakang dan celah penelitian sudah ditulis; banyak penanda menunggu data RSIA dan keputusan tim. |
| I.2 Rumusan Masalah | DRAF | 11 | Rumusan menunggu persetujuan pembimbing; ambang, selisih minimum, dan cara kombinasi belum ditetapkan. |
| I.3 Tujuan | DRAF | 7 | Ukuran keberhasilan bergantung pada ambang dan cara kombinasi yang belum ditetapkan. |
| I.4 Batasan | DRAF | 6 | Batas rawat jalan, jumlah kasus, dan susunan penilai belum ditetapkan. |
| I.5 Metodologi | DRAF | 8 | Lima tahap sudah ada; sengaja dibawa ke pembimbing dan tim tanpa revisi. |
| **Total** | | **47** | |

Catatan:

- I.2 sampai I.4 belum diperiksa ulang pada 9 November.
- I.5 sudah diperiksa, tetapi sengaja tidak direvisi.

## 2. Perlu diputuskan oleh saya, tim, atau pembimbing

- [ ] **Apakah rawat jalan tetap dijawab terpisah?** Dokumen yang berperan seperti resume medis belum pasti ada di rawat jalan. Bila tidak ada, cara melaporkan jawabannya juga perlu ditentukan.
  Mengapa penting: jawaban untuk rawat jalan bisa sudah pasti "tidak" sebelum diuji.
  Pemutus: tim dan RSIA. (Q-B1-bj, F-A11-0015)

- [ ] **Bagaimana kombinasi pemeriksaan dibentuk?** Pilihannya antara lain gabungan semua temuan, hanya temuan yang disepakati kedua komponen, atau cara lain.
  Mengapa penting: hasil pengujian kombinasi bergantung pada cara ini, dan caranya belum ditetapkan.
  Pemutus: tim. (Q-B1-o)

- [ ] **Berapa ambang presisi dan recall, dan bagaimana cara menghitungnya?** Yang belum ditetapkan: angka ambang, selisih minimum, satuan hitung, dan cara menilai "lebih tinggi".
  Mengapa penting: tanpa angka dan cara hitung, rumusan masalah belum dapat dijawab. Angkanya masih menunggu pembahasan tim.
  Pemutus: tim dan pembimbing. (D-19; Q-B1-q, Q-B1-r, Q-B1-bg)

- [ ] **Apakah pembimbing menyetujui empat rumusan masalah capstone?**
  Mengapa penting: rumusan masalah menjadi dasar tujuan dan metodologi.
  Pemutus: pembimbing. (Q-TEAM butir 9)

- [ ] **Apa arti "penguncian" CPPT dan resume medis?** Bab I dan dokumen tim mengandaikan keduanya dikunci. Keterangan lisan dari RSIA, yang disampaikan lewat saya dan belum terverifikasi, berbeda.
  Mengapa penting: batas kesimpulan Bab I bergantung pada arti penguncian ini.
  Pemutus: tim dan RSIA. (Q-B1-ba)

- [ ] **Apakah data pengembangan perlu diberi label?** Pilihannya: tanpa label, diberi label oleh penulis, atau sebagian diberi label oleh pakar.
  Mengapa penting: saat ini hanya data uji yang diberi label, sehingga tahap pengembangan belum punya acuan.
  Pemutus: saya dan tim. (Q-B1-bx)

- [ ] **Bagaimana kasus uji dipilih, dan bagaimana temuan komponen AI di luar daftar jenis diperlakukan?** Cara memilih bisa acak, berurutan, atau cara lain.
  Mengapa penting: cara memilih kasus dan cara menghitung temuan di luar daftar memengaruhi hasil uji.
  Pemutus: saya dan tim. (Q-B1-by)

- [ ] **Apakah tiap komponen menyasar semua jenis ketidaksesuaian, atau jenisnya dibagi antarkomponen?**
  Mengapa penting: pembagian ini dapat membuat hasil uji kombinasi mudah ditebak sebelum diuji.
  Pemutus: saya dan tim. (Q-B1-bz; Q-TEAM butir 1)

- [ ] **Apakah penyusunan jawaban dijadikan tahap tersendiri di metodologi?**
  Mengapa penting: tahap ini menentukan bagaimana hasil uji diubah menjadi jawaban rumusan masalah.
  Pemutus: saya. (Q-B1-ca)

- [ ] **Apa batas "rawat jalan terbatas", dan seperti apa bentuk dokumen rawat jalan di RSIA?**
  Mengapa penting: batasan masalah dan pembagian data bergantung pada hal ini.
  Pemutus: tim dan RSIA. (Q-B1-f; Q-TEAM butir 4)

- [ ] **Bagaimana menanggapi tiga keberatan penelaah kritis terhadap keputusan yang sudah diambil?**
  1. Istilah "penafsiran kontekstual" pada studi Dietrich belum dibedakan dari kriteria yang dipakai Bab I.
  2. Ada keadaan ketiga yang juga berjawab "tidak": komponen saling melengkapi, tetapi kenaikan presisi atau recall di bawah syarat.
  3. Kriteria pemilihan kombinasi tidak dapat diperiksa oleh penelitian maupun literatur, dan konsekuensinya bagi simpulan belum dinyatakan.

  Mengapa penting: ketiganya menyangkut ketepatan argumen di latar belakang.
  Pemutus: saya, lalu pembimbing. (Q-B1-bu, Q-B1-bv, Q-B1-bw)

- [ ] **Apakah pemeriksaan manual (kondisi saat ini) perlu menjadi pembanding?** Masalah di latar belakang adalah pemeriksaan manual, sedangkan pembanding yang dipilih hanya masing-masing komponen.
  Mengapa penting: pembanding menentukan apa yang dapat disimpulkan dari hasil penelitian.
  Pemutus: saya dan pembimbing. (D-22; Q-B1-bm)

- [ ] **Bagaimana penanda tentang sumber pemeriksaan hibrida diperlakukan?** Pilihannya: dianggap keterbatasan tetap, atau dianggap tugas yang belum dikerjakan.
  Mengapa penting: jawabannya menentukan apakah penanda itu tetap ada di naskah akhir.
  Pemutus: saya. (Q-B1-bk)

- [ ] **Apakah penulis diberi izin menyunting I.2 paragraf 2 dan I.5 paragraf 4?** Tujuannya menyelaraskan singkatan AI, NLP, RAG, dan LLM dengan I.1.
  Mengapa penting: tanpa izin, singkatan di ketiga subbab tetap tidak seragam.
  Pemutus: saya. (Q-B1-br)

- [ ] **Gaya sitasi akhir apa yang dipakai, dan judul capstone mana yang berlaku?** Gaya sitasi saat ini masih penulis-tahun sementara; pilihan lainnya APA.
  Mengapa penting: keduanya memengaruhi seluruh naskah, bukan hanya Bab I.
  Pemutus: tim dan pembimbing. (K1, K2)

## 3. Perlu dikerjakan penulis setelah ada keputusan

- [ ] Menyelaraskan Bab II dengan fakta yang sudah dipakai di Bab I tetapi belum ada di Bab II: perbandingan Zeba dengan model bahasa besar dan peran kemiripan kosinus, skala penilaian Skrabic, rubrik Li, dan kategori Dietrich. (Q-B1-bn)
- [ ] Menambah penanda yang belum tertulis di Subbab I.5 untuk: syarat rawat jalan, label data pengembangan, cara memilih kasus, perlakuan temuan komponen AI di luar daftar, dan pasangan ibu dan bayi pada pembagian data.
- [ ] Memperluas kondisi keabsahan jawaban di I.3 dan I.5 agar mencakup jawaban "ya" dan "tidak", per jenis perawatan.
- [ ] Mempersempit klaim di I.5 bahwa ukuran tidak berasal dari penilaian penulis. Klaimnya cukup menyatakan sumber acuan label dan penilaian.
- [ ] Merapikan hal kecil berikut:
  - istilah "rujukan", "konfigurasi", dan "penilai" di I.5;
  - dua penanda di I.5 yang menunjuk nomor temuan, padahal seharusnya nomor pertanyaan;
  - sisa catatan bahasa kecil di I.1.
- [ ] Mengoreksi kalimat di I.1 paragraf 16 dan 17 yang menyederhanakan sumber:
  - Skrabic: perlu disebut bahwa 99 dari 102 kesalahan disisipkan, dan frasa "tanpa rujukan" seharusnya "tanpa retrieval".
  - Zeba: perlu disebut bahwa keluaran juga memuat pernyataan rujukan dan jenis pemeriksaan.

## 4. Perlu diverifikasi

- [ ] Rujukan Permenkes 26/2021 halaman 48 sampai 54 di I.4 belum dicocokkan dengan dokumennya. (Q-B1-bf)
- [ ] Jumlah episode per jenis perawatan dan bentuk dokumen rawat jalan belum diketahui karena data agregat belum tersedia. Akibatnya, kecukupan jumlah kasus belum dapat dinilai. (Q-A04-c)

## 5. Administratif

- [ ] Commit berkas `bab1/Bab_I_Draft.md` (DRAF 19) dan catatan di `memory/` setelah disetujui. Commit terakhir dari saya: "fix: bab 1.4". Push belum terverifikasi. (G3)
- [ ] Menelusuri asal perubahan pada beberapa berkas yang sudah lama diperingatkan: CLAUDE.md, indeks sumber, dokumen migrasi, dan dua modul Bab II.
- [ ] Menyesuaikan build modular Bab I (folder `modular/`) dengan DRAF 19.

## Penutup

Yang sudah baik:

- Struktur subbab sudah lengkap.
- Paragraf celah penelitian (*research gap*) di I.1 sudah ditulis.
- I.5 memenuhi kriteria inti: ada lima tahap yang khusus untuk penelitian ini, dan tidak ada tahap kajian pustaka.

Dokumen ini hanya ringkasan. Rincian lengkap ada di folder `memory/`. Jangan mengubah catatan di `memory/` dari dokumen ini.
