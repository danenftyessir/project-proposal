# Laporan Audit dan Revisi Bab IV

Tanggal: 16 November 2026. Dikerjakan oleh sesi biasa (bukan agent a01–a13). `memory/**`, Bab I, Bab II, dan Bab III tidak diubah.

**STATUS: PARTIAL.** Bab IV memenuhi seluruh butir tugas: tahapan, jadwal, dan lima risiko konsisten satu sama lain. Atas persetujuan pengguna, subbab I.5 kini menyatakan bahwa tahap 2 dan tahap 3 dapat berjalan bersamaan (butir 8). Satu hal yang masih terbuka: pihak penyimpan label acuan sebelum gerbang belum dikonfirmasi (butir 7).

## Temuan audit sebelum revisi

| No. | Temuan pada draf sebelumnya | Penanganan |
| --- | --- | --- |
| A1 | Tujuan, ketergantungan, dan keluaran setiap tahap tidak dinyatakan secara seragam; T2–T4 digabung dalam satu paragraf | Tabel IV.1 dengan kolom tujuan, aktivitas teknis, ketergantungan, dan keluaran |
| A2 | Paralelisme T5 hanya dibenarkan dengan "label siap saat gerbang"; tidak ada aturan yang mencegah penulis membaca label atau isi data uji | Empat syarat pemisahan data uji (IV.1) |
| A3 | T1 memeriksa kelengkapan dokumen tanpa membedakan data pengembangan dan data uji, sehingga isi data uji dapat terbaca sebelum gerbang | Pemeriksaan isi hanya pada data pengembangan; data uji hanya diperiksa keberadaan dokumen dan cap waktunya |
| A4 | Daftar pembekuan tidak memuat versi kode dan syarat label acuan siap | Ditambahkan, beserta pernyataan bahwa pembekuan tidak berarti valid secara klinis |
| A5 | T6 menabulasikan hasil per kategori dan per komponen asal, padahal pertanyaan analisis per kategori sudah tidak ada di Bab I | Dihapus dari T6; T6 kini mengikuti I.5 langkah 4 (lihat butir 7) |
| A6 | Jadwal berupa tabel 21 kolom tanpa ketergantungan, tanpa pembeda data pengembangan dan data uji, dan tanpa persiapan T5/T7 | Gambar IV.1 (Gantt chart) |
| A7 | Fungsi minggu cadangan hanya "cadangan" | Diberi fungsi konkret |
| A8 | Tabel risiko tanpa indikator awal; R3 tidak menjelaskan perlakuan episode tanpa bukti waktu; R4 menyiratkan deidentifikasi cukup; R5 hanya berisi persiapan permintaan data | Kolom indikator awal; R3, R4, R5 ditulis ulang |
| A9 | Istilah "pengaturan sistem" berbeda dari "konfigurasi" pada Bab I dan Bab III | Diseragamkan menjadi "gerbang pembekuan konfigurasi" |

## 1. Ringkasan hasil revisi

Struktur IV.1–IV.3, tujuh tahap, dan baseline minggu tidak berubah. Yang berubah adalah cara penyajian, aturan pemisahan data uji, Gantt chart, dan isi tabel risiko.

## 2. Perubahan IV.1

- **Tabel IV.1 (tujuh baris):** setiap tahap memuat tujuan, aktivitas teknis, ketergantungan, dan keluaran. T1–T4 dipetakan ke langkah 1–4 subbab III.2.3, sedangkan langkah 5 dipetakan ke gerbang.
- **T1:** memuat izin RSIA mitra (sebagai rencana bersama tim), format ekspor, format berkas dan skema temuan bersama dua bagian lain, definisi kategori, panduan, jumlah minimum, serta pembagian data tingkat pasien dengan *fixed seed* dan pasangan ibu–bayi.
- **T3:** memisahkan pekerjaan M2a dan M2b dan menegaskan bahwa keduanya memakai proposisi M1 yang sama.
- **T4:** mencakup uji pasangan temuan yang mirip tetapi berbeda serta uji M4 dengan kasus buatan.
- **T5 dan T7:** diberi masa persiapan (minggu 4–5 dan 13–14) tanpa menggeser baseline.
- **Paragraf pemisahan data uji (empat syarat):**
  1. Data dipisahkan sebelum isinya dibaca.
  2. T2–T4 hanya memakai data pengembangan.
  3. Label tidak dibuka sebelum gerbang.
  4. Data uji tidak dipakai menyetel, dan konfigurasi tidak diubah setelah hasil T6 terlihat.
- **Paragraf gerbang:** memuat syarat label teradjudikasi, sepuluh unsur yang dibekukan, dan batas makna pembekuan.

## 3. Perubahan IV.2 dan validasi Gantt chart

- Gambar IV.1 menampilkan minggu 1–20, tujuh tahap, persiapan T5/T7, minggu cadangan 12, gerbang di awal minggu 13, empat panah ketergantungan, serta pembeda data pengembangan dan data uji.
- Minggu pada Tabel IV.1, blok teks Markdown, dan skrip gambar dicocokkan secara otomatis; ketiganya sama.
- Lima tumpang tindih dijelaskan beserta prasyaratnya:

| Minggu | Tahap | Alasan teknis |
| --- | --- | --- |
| 3 | T1–T2 | Format ekspor dan contoh berkas sudah dikonfirmasi pada minggu 1–2 |
| 5 | T2–T3 | Kontrak proposisi sudah tetap |
| 10 | T3–T4 | Temuan sudah sesuai skema |
| 6–12 | T5 | Pelabelan memakai partisi data yang berbeda |
| 15 | T6–T7 | Temuan kombinasi sudah ada sejak minggu 13–14 |

- Panah T1→T5 dihapus dari gambar karena memotong tiga baris; ketergantungan itu tetap tercantum di Tabel IV.1.
- Tanggal kalender tidak dikarang: [DATA BELUM TERSEDIA: kalender resmi TA 2].

## 4. Perubahan IV.3 dan kelima risiko

Tabel IV.2 kini memiliki kolom No., Risiko, Jenis, Dampak, Indikator awal, dan Tindakan. Seluruh indikator awal dinyatakan sebagai rencana penulis.

| Risiko | Jenis | Perubahan utama |
| --- | --- | --- |
| R1 Akses, ekspor, format, dan pasokan berkas | Negatif | Indikator minggu 1–3; data buatan hanya untuk menguji jalannya kode |
| R2 Pelabel, adjudikator, dan penilai | Negatif | Indikator laju pelabelan (kurang dari separuh target pada minggu 9) |
| R3 Versi prapengajuan | Negatif | Episode tanpa bukti waktu ditandai. Evaluasi utama memakai versi yang sama dengan yang dilabeli, sehingga ketepatan deteksi tetap terukur, tetapi episode itu tidak dianggap mewakili kondisi prapengajuan. Penyajian terpisah dijadikan analisis tambahan yang menunggu persetujuan pembimbing |
| R4 Privasi, biaya, dan model lokal | Negatif | Model ditetapkan sebelum T2; bila berubah sebelum gerbang, M1–M3 diulang; deidentifikasi tidak menghilangkan risiko (subbab II.5.3) |
| R5 Persetujuan atau data lebih cepat | Positif | Pemicu, peluang, pemanfaatan, dan batas: gerbang tidak dimajukan, dan pembagian data tetap dilakukan sebelum isi data uji dibaca |

Kelima risiko adalah risiko selama pengerjaan TA; tidak ada risiko penggunaan produk.

## 5. Konsistensi Bab I dan Bab III

| Butir | Hasil |
| --- | --- |
| Dua pertanyaan penelitian; tidak ada rujukan pertanyaan 3 | Sesuai |
| T6 menjawab pertanyaan 1, T7 menjawab pertanyaan 2 | Sesuai |
| M1–M4 dan langkah 1–5 subbab III.2.3 | Sesuai; subbab III.2.2 dan III.2.3 ada di Bab III |
| Pekerjaan anggota lain | Format berkas, deidentifikasi, dan penyatuan episode dinyatakan sebagai pasokan bagian *Health Data & Cross-Episode Reconciliation*; skema temuan disepakati dengan bagian *Claim Review & Resolution Engineering*; rekonsiliasi tidak dimasukkan ke Bab IV |
| Gerbang pembekuan | Daftar Bab IV mencakup daftar langkah 5 Bab III, ditambah aturan kecocokan dan versi kode |
| Rawat inap dan rawat jalan | Dilaporkan terpisah; rawat jalan hanya bila dokumen memadai (I.2, I.4) |
| Unit klaster *bootstrap* | Pasien, sesuai I.5 |

## 6. Potensi kebocoran data dan masalah metodologis

1. **Pelabelan paralel:** ditangani dengan empat syarat di IV.1. Pemisahan bersifat prosedural. Penulis tetap menjalankan seluruh pipeline, sehingga kepatuhannya bergantung pada penyimpanan label oleh pihak lain.
2. **Pemeriksaan kelengkapan data uji:** dibatasi pada metadata.
3. **Nilai kesepakatan sebelum gerbang:** penulis hanya menerima nilai agregat, tidak membaca isi label.
4. **Ukuran data uji:** ditetapkan pada T1 sebelum pelabelan, tidak disesuaikan setelah melihat hasil.

## 7. Keputusan yang masih menunggu

| No. | Butir | Pihak |
| --- | --- | --- |
| 1 | Pihak penyimpan label acuan sebelum gerbang (usulan: tenaga ahli ketiga atau pembimbing); penanda di IV.1 | Pembimbing |
| 2 | Penyajian terpisah episode tanpa bukti waktu (R3) sebagai analisis tambahan | Pembimbing |
| 3 | Tabulasi per kategori dan per komponen asal: dihapus dari T6 agar sesuai Bab I; bisa dikembalikan sebagai bahan pembahasan | Pengguna |
| 4 | Indikator awal R1–R5 (misalnya ambang separuh target pada minggu 9) | Pengguna |
| 5 | Kalender resmi TA 2 | Prodi |
| 6 | Q-B3-o (R5 risiko positif) kini dijawab oleh arahan tugas ini (dipertahankan); perlu dicatat di `memory/` | Pengguna |

## 8. Rekomendasi lintas bab (tidak dikerjakan)

- **Bab I, subbab I.5 (dikerjakan atas persetujuan pengguna):** butir 3 kini diakhiri kalimat "Tahap ini dapat berjalan bersamaan dengan tahap 2 karena kedua tahap memakai partisi data yang berbeda, dan isi label acuan tidak dibuka penulis sebelum konfigurasi dibekukan." Perubahan diterapkan pada `bab1/Bab_I_Draft.md`, `modular/TA1 bab 1.docx`, dan `…-Draft-Bab1-Bab2.docx`. Kalimat IV.1 yang semula menyebut perbedaan dengan I.5 diganti menjadi "Sesuai subbab I.5, pelabelan pada T5 berjalan bersamaan dengan pembangunan pada T3–T4."
- **Bab III, Tabel III.2 langkah 5:** tambahkan aturan kecocokan temuan dan versi kode agar daftar pembekuan sama persis dengan Bab IV.
- **Daftar Singkatan:** belum memuat SIMRS, SOAP, dan TA 2.
- **Dokumen gabungan:** `…-Draft-Bab1-Bab2-Bab3` (51 hlm.) dan `…-Draft-Bab1-Bab2-Bab3-Bab4` (55 hlm.) dibangun ulang setelah perubahan I.5; nomor daftar isi berkas dasar `…-Draft-Bab1-Bab2` ikut disegarkan (II.1.4 27→26, II.5.3 41→40).

## 9. Berkas keluaran

- `bab4/Bab_IV_Draft.md` — sumber Markdown.
- `modular/TA1 bab 4.docx` dan `modular/TA1 bab 4.pdf` — naskah Bab IV (nomor halaman dan daftar disegarkan dari render Word).
- `bab4/gambar/gambar-IV-1.png` dan `.svg`, `tools/render_gambar_IV_1.py` — Gantt chart dan sumbernya.
- `13523136-Proposal-IF4091-Capstone-Individu-2026-Draft-Bab1-Bab2-Bab3-Bab4.docx` dan `.pdf` — gabungan yang dibangun ulang.
- `tools/build_bab34_docx.py` — lebar tabel Bab IV; tabel Bab IV boleh terpotong halaman.
- `tools/build_gabungan.py` — opsi `--figure4` untuk gambar Bab IV.

Perintah bangun ulang:

```bash
python tools/render_gambar_IV_1.py bab4/gambar/gambar-IV-1.png
```

```bash
python tools/build_bab34_docx.py 4 --figure bab4/gambar/gambar-IV-1.png --figure-width 14.6 --renderer word
```

```bash
python tools/refresh_daftar.py "modular/TA1 bab 4.docx"
```

```bash
python tools/build_gabungan.py 4 --figure bab3/gambar/gambar-III-1.png --figure4 bab4/gambar/gambar-IV-1.png
```

## 10. Validasi akhir

| Pemeriksaan | Hasil |
| --- | --- |
| Baris Markdown ada di docx | Semua ada |
| Jumlah risiko | 5 (4 negatif, 1 positif) |
| Minggu tabel, teks, dan gambar | Sama |
| Rujukan silang | subbab I.3, I.4, I.5, II.5.3, III.2.2, III.2.3; langkah 1–4 dan 5; semuanya ada |
| Rujukan pertanyaan penelitian | Hanya 1 dan 2 |
| `scripts/lint_prose.py` | MEDIUM 0, LOW 0, INFO 0 |
| Render Word | TA1 bab 4: isi bab hlm. 1–6; gabungan Bab 1–4: 55 hlm, Bab IV hlm. 46–51 |
| Tata letak | Diperiksa pada gambar halaman. Kolom tabel diperlebar setelah pemeriksaan pertama memotong kata ("Ketergantung-an", "Negati-f", "No."); Gantt chart terbaca pada lebar 14,6 cm |

Batas pemeriksaan: tanpa audit a07, a09, atau a10. Isi docx Bab I tidak dibandingkan ulang karena tidak berubah sejak sinkronisasi sebelumnya.
