# Laporan Audit dan Revisi Bab III

Tanggal: 16 November 2026. Dikerjakan oleh sesi biasa (bukan agent a01–a13). `memory/**` tidak diubah.

**STATUS: SIAP DITINJAU.** Bab III memenuhi batas 3 halaman dan seluruh butir isi yang diminta. Atas persetujuan pengguna, Bab I Markdown dan Bab IV kemudian diselaraskan ke dua pertanyaan penelitian (butir 6). Keputusan tim dan pembimbing pada butir 7 masih terbuka.

## 1. Ringkasan revisi

- Isi Bab III turun dari sekitar 5,4 halaman menjadi 3 halaman pada render Microsoft Word.
- Semua rujukan pertanyaan penelitian diselaraskan ke dua pertanyaan pada Bab I resmi (`modular/TA1 bab 1.docx`).
- III.2.1 menjadi tabel empat keputusan rancangan teknis; sepuluh langkah menjadi lima langkah dalam tabel aktivitas dan keluaran.
- Diagram blok digambar ulang secara mendatar dan memuat nama anggota tiap bagian.
- Daftar pustaka docx kini hanya memuat lima sumber yang dikutip (sebelumnya 18, padahal 6 yang dikutip).

## 2. Perubahan struktur dan substansi

| Bagian | Perubahan |
| --- | --- |
| III.1 | Dua paragraf: kondisi saat ini dan kondisi yang diharapkan; celah penelitian. |
| III.2 | Satu paragraf pernyataan solusi dan status sementara seluruh pilihan. |
| III.2.1 | Tabel III.1 (keputusan, alternatif, pilihan sementara beserta alasan dan *trade-off*); kolom pertama menyebut modul yang menangani tiap keputusan. |
| III.2.2 | Modul, Gambar III.1, batas tanggung jawab, dan kontrak antarblok. |
| III.2.3 | Langkah pengembangan (Tabel III.2) dan kakas. Sebelumnya bernomor III.2.4. |

Keputusan pengguna yang tetap termuat: D-122 (M1 dipakai bersama dan memakai LLM), D-123 (leksikon dan pola di M2a), D-124 (pemeriksaan informal penulis, bias dinyatakan), D-125, D-126 (Ijadi Maghsoodi dkk.), D-127 (perbandingan RAG dengan LLM tanpa *retrieval* tidak dijawab). D-128 (daftar sepuluh langkah) digantikan arahan lima kelompok langkah.

## 3. Bagian yang dipangkas atau digabung

| Yang dipangkas atau digabung | Alasan |
| --- | --- |
| Subbab Kontrak Antarblok digabung ke III.2.2 | Menghemat satu heading dan membuat teks mengisi halaman 2 sebelum gambar; tanpa ini isi bab menjadi 3,1 halaman. |
| Kalimat regulasi beserta sitasi Kemenkes 2021 dan 2024 | Sudah diuraikan pada subbab I.1 dan II.1; diganti rujukan silang. |
| Kalimat tangkapan layar SIMRS dan data klaim *pending* Mei 2026 | Pengulangan Bab I; data *pending* tidak dipakai sama sekali sehingga tidak ada simpulan sebab-akibat. |
| Uraian tiap modul dalam paragraf | Dipindah ke Gambar III.1 dan Tabel III.2. |
| Paragraf alternatif (satuan, RAG, *union*, pengukuran) | Dipindah ke Tabel III.1. |
| Alternatif model NLI, nama korpus MIMIC, nama keempat kategori | Tidak diwajibkan arahan; kategori sudah didefinisikan pada subbab I.1. |
| Kepanjangan AI/NLP, LLM, SIMRS, SOAP, API | Sudah ada pada Bab I/II; lihat butir 7. |

## 4. Verifikasi jumlah halaman

| Perender | Isi Bab III | Catatan |
| --- | --- | --- |
| Microsoft Word (COM, ekspor PDF) | 3 halaman | Halaman 3 berakhir pada Tabel III.2; sisa ruang sekitar 1,5 cm. Halaman 1 dan 2 masing-masing menyisakan 0,6–1,4 cm. |
| LibreOffice | 3 halaman | Tidak dipakai sebagai acuan: badan teks dirender spasi tunggal, bukan 1,5. |

Temuan pengukuran: ukuran "3 halaman" pada versi sebelumnya berasal dari LibreOffice. Versi itu sekitar 3,5 halaman di LibreOffice dan lebih panjang lagi di Word. Ukuran huruf, margin, dan spasi tidak diubah. Ruang cadangan tipis; penambahan dua baris pada halaman mana pun dapat mendorong baris terakhir Tabel III.2 ke halaman 4.

## 5. Diagram dan pembagian tanggung jawab

Kesembilan unsur yang diminta ada pada Gambar III.1: SIMRS, bagian *Health Data & Cross-Episode Reconciliation* (Muhammad Raihaan Perdana), M1, M2a dan M2b yang terpisah, M3, M4 untuk ketiga konfigurasi, bagian *Claim Review & Resolution Engineering* (M. Abizzar Gamadrian), masukan dari luar sistem, dan hasil evaluasi untuk pertanyaan penelitian 1 dan 2.

M2a diberi tanda bintang: dibangun penulis menurut subbab I.5, tetapi pemiliknya dalam pembagian bidang tim belum ditetapkan. Dasarnya: `Penyelarasan Pemahaman Capstone.md` (baris 55 dan 169) menyebut aturan *rule-based* disusun Danen, sedangkan butir Q-B3-e di `memory/OPEN_QUESTIONS.md` masih terbuka. Rekomendasi: bila pengguna menegaskan dokumen penyelarasan itu final, tanda bintang dan penanda dihapus.

## 6. Konsistensi Bab I–IV

Sesuai di dalam Bab III: hanya pertanyaan penelitian 1 yang disebut di teks; diagram menyebut 1 dan 2; tidak ada "persoalan turunan" atau "1–3"; empat keputusan teknis tidak disebut pertanyaan penelitian.

Ditangani setelah persetujuan pengguna ("Ya, selaraskan", 16 November 2026):

1. `bab1/Bab_I_Draft.md` disinkronkan dengan `modular/TA1 bab 1.docx`: dua pertanyaan penelitian, paragraf komponen pemeriksaan menggantikan empat persoalan turunan, tujuan khusus ke-6 dihapus, pengantar ukuran keberhasilan dan langkah 4–5 I.5 mengikuti docx. Perbandingan baris demi baris menunjukkan tidak ada sisa perbedaan teks. Docx Bab I tidak diubah. Ini menggeser D-119 (Markdown sebagai sumber kebenaran) karena isi Markdown kini mengikuti docx; perlu dicatat di `memory/`.
2. `bab4/Bab_IV_Draft.md` disesuaikan seperti tabel berikut, dan `modular/TA1 bab 4.docx` dibangun ulang (nomor halaman dari render Word). Daftar pembekuan pada gerbang minggu 13 juga ditambah model *embedding* dan aturan pemecahan kalimat M1 agar sama dengan langkah 5 Bab III.

| Lokasi Bab IV | Sebelum | Sesudah |
| --- | --- | --- |
| T1 | subbab III.2.3 (kontrak); langkah 2, 3, dan awal langkah 1 subbab III.2.4 | subbab III.2.2; langkah 1 subbab III.2.3 |
| T2 | sisa langkah 1 dan langkah 4 | langkah 2 |
| T3 | langkah 5–7 | langkah 3 |
| T4 | langkah 8 dan 9 | langkah 4 |
| Gerbang minggu 13 | subbab III.2.4 | langkah 5 subbab III.2.3 |
| T6 | menjawab pertanyaan penelitian 1 dan 2 | pertanyaan penelitian 1 |
| T7 dan R2 | pertanyaan penelitian 3; "ketiga pertanyaan"; "1 dan 3" | pertanyaan penelitian 2; "kedua pertanyaan"; "1 dan 2" |

3. Konsistensi dengan proposal dua anggota lain: BELUM DAPAT DIVERIFIKASI (Bab III mereka tidak tersedia di repository).

## 7. Keputusan yang masih menunggu

| No. | Butir | Pihak |
| --- | --- | --- |
| 1 | Pemilik M2a (Q-B3-e) | Tim |
| 2 | Skema temuan dan kontrak antarblok (butir terbuka 1 dokumen penyelarasan) | Tim |
| 3 | Kebijakan LLM *cloud* atau lokal untuk teks klinis terdeidentifikasi | Pembimbing, RSIA mitra |
| 4 | Format ekspor CPPT dan resume medis dari SIMRS | RSIA mitra |
| 5 | Persetujuan penggabungan Kontrak Antarblok ke III.2.2 | Pengguna |
| 6 | T6 Bab IV masih menabulasikan hasil per kategori dan per komponen asal, padahal pertanyaan analisis per kategori sudah tidak ada di Bab I; dipertahankan sebagai bahan pembahasan atau dihapus | Pengguna |
| 7 | "Sistem" atau "komponen" analisis semantik (Q-B3-q); judul proposal memakai "komponen" | Pengguna |
| 8 | SIMRS dan SOAP belum ada di Daftar Singkatan; kepanjangan AI/NLP dan LLM tidak diulang di Bab III | Pengguna |
| 9 | Pencatatan revisi ini di `memory/**` (teks penanda berubah, D-128 digantikan, temuan perender) | Pengguna |

Teks penanda dipendekkan: "pemilik komponen *rule-based*" menjadi "pemilik M2a"; "skema temuan dan kontrak antarblok" menjadi "kontrak antarblok"; "format ekspor CPPT dan resume dari SIMRS" menjadi "format ekspor SIMRS"; "kebijakan LLM cloud vs model lokal untuk teks klinis terdeidentifikasi" menjadi "kebijakan LLM".

## 8. Berkas keluaran

- `modular/TA1 bab 3.docx` — naskah Bab III (menimpa versi commit c0df307).
- `modular/TA1 bab 3.pdf` — hasil ekspor Word, dipakai untuk menghitung halaman.
- `bab1/Bab_I_Draft.md` — disinkronkan dengan docx Bab I (dua pertanyaan penelitian).
- `bab4/Bab_IV_Draft.md` dan `modular/TA1 bab 4.docx` — rujukan langkah, subbab, dan pertanyaan penelitian diselaraskan.
- `bab3/Bab_III_Draft.md` — sumber Markdown, sinkron dengan docx.
- `bab3/gambar/gambar-III-1.png` dan `.svg` — diagram final.
- `tools/render_gambar_III_1.py` dan blok Mermaid di Markdown — sumber diagram yang dapat disunting.
- `tools/build_bab34_docx.py` — ditambah `--figure-width`, `--renderer word`, daftar pustaka Bab III, lebar tabel, dan pemisah halaman sebelum daftar pustaka.

Perintah bangun ulang:

```bash
python tools/render_gambar_III_1.py bab3/gambar/gambar-III-1.png
```

```bash
python tools/build_bab34_docx.py 3 --figure bab3/gambar/gambar-III-1.png --figure-width 14.6 --renderer word
```

## 9. Pengujian dan validasi

| Pemeriksaan | Hasil |
| --- | --- |
| Jumlah halaman isi (Word) | 3 |
| Seluruh baris Markdown ada di docx | Ya |
| Heading docx | III.1, III.2, III.2.1, III.2.2, III.2.3 |
| Sitasi dan daftar pustaka | 5 sumber dikutip, 5 entri, cocok dua arah |
| Rujukan silang | Gambar III.1, Tabel III.1, Tabel III.2, subbab I.1, I.3, I.4, I.5, II.1, II.1–II.4; semuanya ada |
| Daftar isi, gambar, tabel | Sesuai; nomor halaman dari render Word |
| `scripts/lint_prose.py` | MEDIUM 0, LOW 0, INFO 0 |
| Penanda | 4 (dua tim, satu pembimbing, satu data) |
| Tabel dan diagram | Diperiksa pada gambar halaman hasil Word; terbaca, huruf diagram 7–7,5 pt |

Batas pemeriksaan: nomor halaman sitasi diambil dari versi lengkap yang sudah diaudit sebelumnya dan tidak dibuka ulang ke PDF sumber pada sesi ini. Audit bahasa dilakukan dengan linter dan pembacaan sendiri, tanpa audit a09.
