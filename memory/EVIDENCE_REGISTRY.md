---
file: EVIDENCE_REGISTRY
revision: 2
status: PENDING_VERIFICATION
updated: 2026-11-06
updated_by: a13-memory-manager
based_on_commit: fee9a61
---

# Evidence Registry

Claim–Evidence Log tingkat klaim (CLAUDE.md §11.2). Indeks tingkat berkas sumber tetap di `source/INDEKS.md` dan tidak diduplikasi di sini.

Status klaim: `TERVERIFIKASI` · `DIDUKUNG SEBAGIAN` · `TIDAK DIDUKUNG` · `BERTENTANGAN` · `BELUM DIVERIFIKASI`.

Klaim dari data RSIA dicatat dengan sumber berupa **kategori data** (mis. `RSIA: data pending Mei 2026`), bukan nama berkas, dan selalu dalam bentuk agregat (R-4, R-8). Angka yang sama dengan PDF Breakdown atau Penyelarasan diberi catatan "menunggu pembahasan tim" (D-19).

**Belum diisi.** Klaim Bab II DRAFT 6 dan berkas `tools/claims_II*.json` (struktur Bab II lama) belum dimigrasikan. Migrasi dilakukan A02 dan A13 pada tugas tersendiri, dan setiap klaim diperiksa ulang ke PDF, bukan disalin dari catatan lama.

**Isi sesi 2026-11-06.** Bagian "Klaim Bab I" di bawah bersumber dari paket bukti a02 (TSK-023, `.scratch/bab1_evidence.md`, tidak di-commit) dan verifikasi halaman a08 (TSK-026). Kolom Catatan membedakan "diperiksa a08" (verifikasi sitasi kedua) dari "a02 saja" (belum diuji ulang). Halaman cetak = halaman PDF kecuali dicatat. Status bukan persetujuan Supervisor/pengguna. Lokasi di naskah Bab I belum dipetakan per paragraf (`bab1/Bab_I_Draft.md`, DRAF 4).

Catatan berkas sumber: `Permenkes_26_2021_Pedoman_INA-CBG.pdf` di `source/01_…` tidak punya lapisan teks isi; bunyi pasal dibaca dari salinan JDIH `source/external/2021permenkes026.pdf` dan halamannya dicek visual terhadap salinan resmi oleh a08 (hlm. 7, 23, 53, 54). Paginasi `Permenkes_24_2022` berbeda antara salinan Berita Negara dan salinan JDIH; acuan halaman di bawah mengikuti salinan Berita Negara (usulan agent, keputusan bentuk acuan menunggu K1).

## Klaim Bab I

| ID | Lokasi | Klaim | Sumber (path) | Halaman | Status | Catatan |
|---|---|---|---|---|---|---|
| E-01 | Bab I, I.1 | Rumah sakit wajib menyelenggarakan RME (PMK 24/2022 Ps. 3 ay. 1–2) | `source/01_Regulasi_dan_Kebijakan_Indonesia/Permenkes_24_2022_Rekam_Medis.pdf` | 3–4 | TERVERIFIKASI | a02 saja. Hanya kewajiban, bukan keadaan implementasi di RSIA |
| E-02 | Bab I, I.1 | Penyelenggaraan RME mencakup pengisian informasi klinis dan penginputan data untuk klaim pembiayaan (Ps. 13 ay. 1–3) | `…/Permenkes_24_2022_Rekam_Medis.pdf` | 6 | TERVERIFIKASI | a02 saja |
| E-03 | Bab I, I.1 | Pencatatan klinis lengkap, berurutan waktu, terintegrasi dalam satu dokumen (Ps. 16, 17) | `…/Permenkes_24_2022_Rekam_Medis.pdf` | 7–8 | TERVERIFIKASI | Ps. 16 ay. 4 hlm. 7 diperiksa a08 (salinan Berita Negara). PMK 24 tidak memakai istilah "CPPT" (istilah dari KMK 1596) |
| E-04 | Bab I, I.1 | Perkembangan pasien dicatat PPA di CPPT; DPJP reviu berkala dan verifikasi harian (KMK 1596 AKP 3 EP d; PAP 1.2) | `…/KMK_HK.01.07-MENKES-1596-2024_Standar_Akreditasi_RS.pdf` | 215; 266–267 | TERVERIFIKASI | Diperiksa a08. Standar akreditasi, bukan bukti praktik RSIA; format SOAP tidak ditetapkan |
| E-05 | Bab I, I.1 | Ringkasan pasien pulang wajib untuk semua pasien rawat inap; enam butir isi (AKP 5.1) | `…/KMK_HK.01.07-MENKES-1596-2024_Standar_Akreditasi_RS.pdf` | 218–219 | TERVERIFIKASI | Diperiksa a08. Hanya rawat inap |
| E-06 | Bab I, I.1 | Rekam medis saat pulang wajib untuk rawat inap dan rawat darurat; rawat jalan bila dibutuhkan (Ps. 26 ay. 6–9) | `…/Permenkes_24_2022_Rekam_Medis.pdf` | 11–12 | DIDUKUNG SEBAGIAN | a02 saja. Pasal tidak memakai istilah "resume medis"; penyamaan dengan resume adalah tafsiran |
| E-07 | Bab I, I.1 | Pada rawat jalan, ringkasan (PRMRJ) hanya untuk asuhan/diagnosis kompleks (AKP 5.7) | `…/KMK_HK.01.07-MENKES-1596-2024_Standar_Akreditasi_RS.pdf` | 225–226 | TERVERIFIKASI | Diperiksa a08. Relevan D-21; bentuk dokumen rawat jalan di RSIA belum dipastikan (Q-B1-f) |
| E-08 | Bab I, I.1 | Pengkajian rekam medis berkala oleh komite/tim (MRMIK 12) | `…/KMK_HK.01.07-MENKES-1596-2024_Standar_Akreditasi_RS.pdf` | 167–168 | TERVERIFIKASI | Diperiksa a08. Bukan pemeriksaan per klaim; tidak menyebut kesesuaian CPPT–resume |
| E-09 | Bab I, I.1 | Dalam JKN, rumah sakit dibayar per kasus dengan INA-CBG untuk rawat inap dan rawat jalan | `source/02_Klaim_JKN_INA-CBG_dan_Kecurangan/1-s2.0-S294985622500090X-main.pdf` (Susilo, 2025) | 2 | TERVERIFIKASI | Diperiksa a08. Gambaran umum sistem, bukan RSIA |
| E-10 | Bab I, I.1 | Resume medis sumber data pengodean; ketepatan kode memengaruhi grouper dan biaya (PMK 26/2021 Bab III) | `source/01_…/Permenkes_26_2021_Pedoman_INA-CBG.pdf` (bunyi dari `source/external/2021permenkes026.pdf`) | 23 | TERVERIFIKASI | Hlm. 23 diperiksa visual a08 terhadap salinan resmi. Salinan repo tanpa lapisan teks |
| E-11 | Bab I, I.1 | Koder wajib klarifikasi ke dokter bila ada ketidaksesuaian terhadap aturan pengodean; verifikator BPJS memeriksa kelengkapan (Bab I C) | sama dengan E-10 | 8–9 | TERVERIFIKASI | a02 saja. "Ketidaksesuaian" di sini terhadap aturan pengodean, bukan antara CPPT dan resume |
| E-12 | Bab I, I.1 | Penginputan data klaim berdasarkan diagnosis/tindakan sesuai rekam medis (Ps. 19) | `…/Permenkes_24_2022_Rekam_Medis.pdf` | 9 | TERVERIFIKASI | a02 saja |
| E-13 | Bab I, I.4 | Satu episode = satu klaim; dua jenis episode (rawat jalan, rawat inap) | sama dengan E-10 | 48 | TERVERIFIKASI | a02 saja |
| E-14 | Bab I, I.4 | Ketentuan episode rawat jalan/IGD < 6 jam/rawat inap (PMK 26/2021 Bab III) | sama dengan E-10 | 48; 52–54 | TERVERIFIKASI | Hlm. 53 dan 54 diperiksa visual a08. Cocok dengan Penyelarasan |
| E-15 | Bab I, I.4 | Bayi sehat dengan layanan neonatal esensial dibayar dalam paket persalinan ibu; bayi sakit diklaim terpisah | sama dengan E-10 | 44 | TERVERIFIKASI | a02 saja. Dasar penautan ibu–bayi; pemilik di tim terbuka (Q-B1-c) |
| E-16 | Bab I, I.4 | Lingkup dan di luar lingkup kajian (CPPT dan resume dalam satu episode; kebidanan dan anak; satu RSIA) | `Penyelarasan Pemahaman Capstone.md`; D-21; D-25 | — | TERVERIFIKASI | Keputusan tim, bukan bukti eksternal |
| E-17 | Bab I, I.4 | Sistem tidak memutuskan kelayakan klaim; "siap diajukan" ditetapkan pengguna | `Penyelarasan Pemahaman Capstone.md` | — | TERVERIFIKASI | Keputusan tim |
| E-18 | Bab I, I.4 | Tidak ada klaim penurunan *pending* atau percepatan koder; tidak digeneralisasi | `Penyelarasan Pemahaman Capstone.md` | — | TERVERIFIKASI | Keputusan tim |
| E-19 | Bab I, I.5 | Struktur Bab II (draf 6) untuk sistematika | `bab2/Bab_II_Revisi_Notulensi.md` | — | TERVERIFIKASI | Struktur draf 6; judul dan pembuka Bab II menunggu penyelarasan D-21 dan Q-B1-e |
| E-20 | Bab I, I.5 | Bab III dan seterusnya | `bab3/Bahan_Pindahan_dari_Bab_II.md` (bahan mentah) | — | BELUM DIVERIFIKASI | Belum ada naskah Bab III |

## Premis penghubung (dilaporkan terpisah, CLAUDE.md §8 no. 8)

| ID | Lokasi | Premis | Sumber (path) | Halaman | Status | Catatan |
|---|---|---|---|---|---|---|
| P-1 | Bab I, I.1 | Resume sumber pengodean; kode menentukan grouper dan biaya | = E-10 | 23 | TERVERIFIKASI | Diperiksa a08 |
| P-2 | Bab I, I.1 | Masalah pengodean menimbulkan *dispute* dan *pending* sehingga pembayaran tertunda | `source/01_…/Permenkes_26_2021_Pedoman_INA-CBG.pdf` (Bab I A) | 7 | TERVERIFIKASI (sebagai pernyataan regulator) | Hlm. 7 diperiksa visual a08. Pernyataan regulator tanpa data |
| P-3 | Bab I, I.1 | *Pending* rawat inap dipengaruhi koding tidak sesuai, kelengkapan berkas, beda diagnosis DPJP–verifikator; *pending* dapat merugikan RS | `source/external/faktor-faktor yang mempengaruhi pending rawat inap.pdf` (Simbolon & Gani) | PDF 2 dan 6; cetak 73 dan 77 (juga 72, 75) | DIDUKUNG SEBAGIAN | Diperiksa a08 (hlm. 72–73, 75, 77). Tinjauan 5 artikel 2020–2022 tanpa penilaian mutu; kalimat kerugian mengutip Muroli dkk. 2020 (sekunder; bentuk sitasi menunggu K1); rawat inap saja |
| P-4 | Bab I, I.1 | Kondisi RSIA mitra: resume disusun ulang manual, CPPT dan resume dikunci, pemeriksaan kesiapan manual | `Penyelarasan Pemahaman Capstone.md` (keterangan tim atas wawancara Direktur RSIA, September 2026) | — | DIDUKUNG SEBAGIAN | Atribusi ke dokumen tim (D-24, D-27); catatan wawancara asli tidak diperiksa. Angka pada paragraf yang sama ditahan (D-19) |
| P-5 | Bab I, I.1 | Sebagian alasan *pending* yang dicatat tim dapat dibaca dari CPPT dan resume dalam satu episode | `Penyelarasan Pemahaman Capstone.md` | — | DIDUKUNG SEBAGIAN | Klasifikasi tim tentang lokasi bukti, bukan bukti sebab-akibat. Semua jumlah ditahan (D-19) |
| P-6 | Bab I, I.1 | Premis penghubung: ketidaksesuaian CPPT–resume menyebabkan kode/klaim bermasalah dan karena itu kerugian | tidak ada di `source/` | — | BELUM DIVERIFIKASI | Hanya rantai P-1 + P-2 dan klasifikasi P-5 yang tersedia. Wajib ditulis sebagai premis/asumsi kerja; terkait F-A07-0001 dan Q-B1-b. Tidak boleh ada klaim penurunan *pending* atau percepatan koder (D-24) |
| P-7 | Bab I, I.1 | Konteks "dikunci": perbaikan data RME dibatasi 2×24 jam (Ps. 30 ay. 5–7) | `…/Permenkes_24_2022_Rekam_Medis.pdf` | 13–14 | DIDUKUNG SEBAGIAN (sebagai konteks) | Ps. 30 ay. 5–6 hlm. 13–14 diperiksa a08 (salinan Berita Negara). Tidak membuktikan bahwa penguncian di RSIA berasal dari pasal ini |
