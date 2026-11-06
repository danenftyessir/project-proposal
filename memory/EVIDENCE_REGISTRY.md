---
file: EVIDENCE_REGISTRY
revision: 3
status: PENDING_VERIFICATION
updated: 2026-11-06
updated_by: a13-memory-manager
based_on_commit: f3cb6ba
---

# Evidence Registry

Claim–Evidence Log tingkat klaim (CLAUDE.md §11.2). Indeks tingkat berkas sumber tetap di `source/INDEKS.md` dan tidak diduplikasi di sini.

Status klaim: `TERVERIFIKASI` · `DIDUKUNG SEBAGIAN` · `TIDAK DIDUKUNG` · `BERTENTANGAN` · `BELUM DIVERIFIKASI`.

Klaim dari data RSIA dicatat dengan sumber berupa **kategori data** (mis. `RSIA: data pending Mei 2026`), bukan nama berkas, dan selalu dalam bentuk agregat (R-4, R-8). Angka yang sama dengan PDF Breakdown atau Penyelarasan diberi catatan "menunggu pembahasan tim" (D-19).

**Klaim Bab II DRAFT 6 (rev 3, TSK-058).** 47 klaim hasil pemeriksaan a02 (TSK-055, PARTIAL) dimigrasikan dari `.scratch/bab2_evidence.md` (tidak di-commit) ke bagian "Klaim Bab II" di bawah, setia pada berkas itu; A13 tidak membuka ulang PDF. Berkas `tools/claims_II*.json` (struktur Bab II lama) tidak dimigrasikan. Sisa scope a02 yang belum diperiksa (II.3.2, II.4.1 Gao, II.4.2, II.6, II.7.1 Fitriasari, II.7.2 dan Tabel II.2, II.8, II.9, halaman Skrabic/Zeba/Jaganathan/n2c2, metadata Daftar Pustaka) belum ada barisnya.

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

## Klaim Bab II (DRAFT 6; a02, TSK-055, PARTIAL; hanya a02, belum diuji ulang a08)

Sumber: `.scratch/bab2_evidence.md`. "Lokasi" mengacu ke `bab2/Bab_II_Revisi_Notulensi.md` (nomor baris). Halaman = halaman cetak; offset (cetak − PDF) per sumber menurut a02. Singkatan sumber (path di bawah `source/`): PMK24 = `01_Regulasi_dan_Kebijakan_Indonesia/Permenkes_24_2022_Rekam_Medis.pdf` (19 hlm., offset 0); PMK26 = `external/2021permenkes026.pdf` (56 hlm., offset 0); KMK1596 = `01_…/KMK_HK.01.07-MENKES-1596-2024_Standar_Akreditasi_RS.pdf` (356 hlm., offset 0); KMK1423 = `01_…/KMK_HK.01.07-MENKES-1423-2022_Variabel_dan_Metadata_RME.pdf` (92 hlm., offset 0); SIMBOLON = `external/faktor-faktor yang mempengaruhi pending rawat inap.pdf` (offset +71); OKTAVIA = `03_Rekam_Medis_CPPT_dan_Catatan_Perkembangan/OktaviaAz_2021_CPPT_MIRM.pdf` (offset +424); NADI = `03_…/Nadi_2024_CPPT_Elektronik.pdf` (offset +83); HERYAWAN = `04_Standar_Interoperabilitas_dan_Terminologi_Klinis/Heryawan_2025_FHIR_Interoperability_Indonesia.pdf` (hlm. = PDF); SATUSEHAT = `04_…/SATUSEHAT_Panduan_Rawat_Inap_v6.0_diakses_2026-11-03.html` (HTML, tanpa halaman); DIETRICH = `external/Automated auditing of emergency department documentation using.pdf` (offset +94). Ringkasan: 47 klaim; 39 TERVERIFIKASI (3 di antaranya hanya angka, halaman belum dicek), 5 DIDUKUNG SEBAGIAN, 1 BERTENTANGAN, 2 BELUM DIVERIFIKASI, 0 TIDAK DIDUKUNG.

| ID | Lokasi | Klaim | Sumber | Halaman | Status | Catatan (tindakan menurut a02) |
|---|---|---|---|---|---|---|
| B2-01 | II.1.1 :21 | RME wajib (Ps. 3) | PMK24 | 3–4 | TERVERIFIKASI | = E-01. Pertahankan |
| B2-02 | :21 | 8 kegiatan RME; pembagian pengisi (Ps. 13 ay. 1–3) | PMK24 | 6 | TERVERIFIKASI | = E-02. Pertahankan |
| B2-03 | :21 | Isi RME: dokumentasi administratif dan klinis (Ps. 27 ay. 1–3) | PMK24 | 12 | TERVERIFIKASI | Pertahankan |
| B2-04 | :21 | Sistem RME mengacu ke variabel dan metadata Kemenkes; metadata = definisi, format, kodifikasi (Ps. 11) | PMK24 | 5 | TERVERIFIKASI | Pertahankan |
| B2-05 | :23 | MRMIK 7, isi informasi a–f | KMK1596 | 163 | TERVERIFIKASI | Berlaku untuk pasien rawat jalan, rawat inap, dan gawat darurat; relevan D-21 |
| B2-06 | :23 | MRMIK 8: tanggal, jam, nama, paraf; prosedur koreksi | KMK1596 | 163–164 | TERVERIFIKASI | Pertahankan |
| B2-07 | :23 | MRMIK 9: daftar kode/simbol/singkatan; ICD-10 dan ICD-9-CM | KMK1596 | 164–165 | TERVERIFIKASI | Pertahankan |
| B2-08 | :23 | Kegagalan komunikasi akibat tulisan tidak terbaca dan singkatan tidak seragam | KMK1596 | 148 | TERVERIFIKASI | Pertahankan |
| B2-09 | :23 | MRMIK 12: pengkajian "setidaknya setiap tahun", sampel dirawat dan pulang, empat fokus | KMK1596 | 167–168 | DIDUKUNG SEBAGIAN | EP b berbunyi "secara berkala setiap tahun"; sumber tidak memakai "setidaknya". Lunakkan |
| B2-10 | II.1.2 :27 | Ps. 16 ay. 2–3 dan Ps. 17 ay. 1–2 | PMK24 | 7–8 | TERVERIFIKASI | = E-03. Pertahankan |
| B2-11 | :29 | AKP 3 EP d dan e (CPPT; unit intensif) | KMK1596 | 215 | TERVERIFIKASI | = E-04. Pertahankan |
| B2-12 | :29 | PAP 1.1: instruksi dapat dituliskan di CPPT | KMK1596 | 263 | TERVERIFIKASI | Pertahankan |
| B2-13 | :29 | PAP 1.2: instruksi di CPPT; DPJP reviu berkala dan verifikasi harian | KMK1596 | 266–267 | TERVERIFIKASI | Perbaiki sitasi menjadi hlm. 266–267 |
| B2-14 | :29 | KMK 1596 tidak menetapkan format isi CPPT | KMK1596 | seluruh teks | TERVERIFIKASI (berdasarkan pencarian teks) | "SOAP" 0 kali; "SBAR" 2 kali untuk pelaporan kondisi pasien kepada DPJP, bukan format CPPT. Pertahankan frasa "dalam teks yang ditelaah" |
| B2-15 | II.1.3 :37 | AKP 5.1: wajib untuk semua pasien rawat inap; isi a–f; dibuat DPJP; salinan untuk penjamin | KMK1596 | 218–219 | TERVERIFIKASI | = E-05. Pertahankan |
| B2-16 | :37 | PMK24 Ps. 26 ay. 6–8: isi minimum rekam medis rawat inap saat pulang | PMK24 | 11–12 | DIDUKUNG SEBAGIAN | = E-06. Ay. 8 mencakup rawat darurat; ay. 9 rawat jalan "apabila dibutuhkan"; pasal tidak memakai "resume medis" (pengaitan = tafsiran). Sebutkan bila cakupan rawat jalan dipertahankan (D-21) |
| B2-17 | :37 | PMK26 menyebut dokumen ini "resume medis" | PMK26 | 8 | TERVERIFIKASI (istilah) | Penyamaan resume medis = ringkasan pulang adalah tafsiran penulis |
| B2-18 | :37, :87 | SATUSEHAT: resume rawat inap memakai Composition LOINC 34105-7; v6.0 bertanggal 10 Januari 2026 | SATUSEHAT | — (HTML) | TERVERIFIKASI | Pertahankan |
| B2-19 | II.1.4 :41 | KMK1423: standar elemen data; lima dataset; kolom tipe, format, DO, referensi | KMK1423 | 3, 5, 6 | TERVERIFIKASI | Pertahankan |
| B2-20 | Tabel II.1 :45–55 | Kelompok I–V dan halamannya | KMK1423 | 57–81 | TERVERIFIKASI | Ubah halaman kelompok V menjadi 68–69 |
| B2-21 | :57 | Definisi diagnosis awal dan akhir; rencana rawat berupa teks bebas | KMK1423 | 69, 76–77 | TERVERIFIKASI | Pertahankan |
| B2-22 | :57, Catatan B.1 | KMK1423 tidak memuat variabel CPPT atau catatan perkembangan | KMK1423 | seluruh teks | TERVERIFIKASI (berdasarkan pencarian teks) | "CPPT", "perkembangan", "terintegrasi", "SOAP": 0 hasil |
| B2-23 | II.2 :75 | INA-CBG berdasarkan ICD-10 2010 dan ICD-9-CM 2010; 1.075 = 786 rawat inap + 289 rawat jalan | PMK26 | 10 | TERVERIFIKASI | Pertahankan |
| B2-24 | :75 | Resume medis sebagai sumber pengodean; ketepatan kode memengaruhi grouper; definisi diagnosis utama | PMK26 | 23 | TERVERIFIKASI | = E-10 |
| B2-25 | :77 | Pembagian tugas dokter, koder, verifikator | PMK26 | 8–9 | TERVERIFIKASI | = E-11. Kewajiban koder klarifikasi ke dokter (hlm. 9) dapat ditambahkan |
| B2-26 | :77 | Pengodean termasuk pengolahan informasi (Ps. 18); penginputan klaim (Ps. 19) | PMK24 | 8; 9 | TERVERIFIKASI | = E-12 |
| B2-27 | :75 | JKN: BPJS memproses klaim; pembayaran per kasus INA-CBG | Susilo (`02_Klaim_JKN_INA-CBG_dan_Kecurangan/1-s2.0-S294985622500090X-main.pdf`) | 2 | TERVERIFIKASI | = E-09 |
| B2-28 | II.3.1 :85 | RME harus terhubung dengan platform interoperabilitas Kemenkes (Ps. 21) | PMK24 | 10 | DIDUKUNG SEBAGIAN | Pasal tidak menyebut nama "SATUSEHAT"; rujuk pernyataan itu ke Heryawan hlm. 1–3 |
| B2-29 | II.7.1 :184 | Kewajiban kerahasiaan berlaku bagi pihak pembiayaan dan badan hukum (Ps. 32) | PMK24 | 14–15 | TERVERIFIKASI | Sumber memakai "pihak yang terlibat", bukan "pihak yang memiliki akses" |
| B2-30 | II.7.1 :184 | UU 27/2022 Ps. 4 ay. 2 (hlm. 5) dan Penjelasan (hlm. 38) | `01_…/UU_27_2022_Pelindungan_Data_Pribadi.pdf` | — | BELUM DIVERIFIKASI | Tidak dibaca; sisa scope |
| B2-31 | II.7.1 :184 | Berita CNBC 30 Oktober 2026 tentang perpres etika AI | tidak ada di `source/` | — | BELUM DIVERIFIKASI | Hanya URL; tidak ada salinan di repo. Arsipkan atau keputusan pengguna (external lookup off) |
| B2-40 | II.1.2 :31 | Oktavia: CPPT memakai SOAP, mengacu MIRM 13.3 "SNARS Edisi 1.1" | OKTAVIA | 426 | BERTENTANGAN (detail edisi) | Sumber menyebut "SNARS Edisi 1" (hlm. 426, 430–431, daftar pustaka). Perbaiki menjadi "Edisi 1" |
| B2-41 | :33 | 200 berkas acak; wawancara bidan, perawat, apoteker | OKTAVIA | 427 | TERVERIFIKASI | Pertahankan |
| B2-42 | :33 | Identitas 87,5%; no. RM 78%; tanggal 51%; jam 48%; TTD 80%; SOAP 100% | OKTAVIA | 427, 432 | TERVERIFIKASI | Butir berlabel "SBAR/SOAP" di tabel (hlm. 432); ganti "bagian SOAP" dengan "SBAR/SOAP". Survei awal 330 berkas (hlm. 426) tidak dipakai naskah |
| B2-43 | :33 | Penyebab: keterbatasan waktu, miskomunikasi, disiplin, pengetahuan; belum ada SOP | OKTAVIA | 425 (abstrak), 427, 429–431 | TERVERIFIKASI | Tambahkan sitasi hlm. 430–431 agar tidak hanya bertumpu pada abstrak |
| B2-44 | :31 | Nadi: S/O/A/P = keluhan, pemeriksaan fisik, diagnosis, rencana (sitasi naskah "hlm. 1") | NADI | 84 | TERVERIFIKASI (isi) | Sitasi halaman di naskah salah (hlm. 84, bukan 1); Daftar Pustaka hlm. 84–91 |
| B2-45 | :33 | Nadi mengelompokkan hambatan menjadi tiga kategori; mengusulkan digitalisasi dengan PDSA (sitasi naskah "hlm. 1") | NADI | 84; 85–86; 87–89 | DIDUKUNG SEBAGIAN | Tiga kategori hanya di abstrak; Tabel 1 Ishikawa (hlm. 85–86) memuat enam kategori. Lunakkan atau rujuk enam kategori; perbaiki halaman |
| B2-46 | II.2 :79 | Simbolon: 5 artikel 2020–2022; tiga faktor; Muroli 38 (41,8%), 44 (48,4%), 27 (29,7%) | SIMBOLON | 72, 75, 77 | TERVERIFIKASI (sebagai ringkasan sekunder) | Data Muroli dkk. berasal dari RSAB Harapan Kita 2019. Lihat P-3 |
| B2-47 | II.3.1 :85 | Heryawan: empat komponen SATUSEHAT (hlm. 3); 61/37/9 persoalan (hlm. 1) | HERYAWAN | 1, 3 | TERVERIFIKASI | Pertahankan |
| B2-48 | II.3.1 :87; Catatan B.2 | Panduan SATUSEHAT tidak memuat *resource* atau bagian khusus untuk CPPT | SATUSEHAT | — (HTML) | DIDUKUNG SEBAGIAN | "CPPT", "catatan perkembangan", "SOAP" tidak ditemukan, tetapi Bab 6 "Riwayat Perjalanan Penyakit" (narasi perkembangan penyakit, `ClinicalImpression`), Bab 12 "Rasional Klinis", Bab 7 Tujuan Perawatan (`Goal`). Daftar *resource* di :87 belum lengkap. Butuh keputusan A03/pengguna karena Catatan B.2 dipakai untuk Bab I/III |
| B2-49 | Gambar II.2 | 13 bagian Composition | SATUSEHAT | — (HTML) | TERVERIFIKASI (13 judul) | *Resource* acuan bagian 9–13 tetap BELUM DIVERIFIKASI |
| B2-50 | II.5 :150 | Dietrich: 600 kunjungan (500 + 100); akurasi 93,2–94,2%, presisi 98,3–99,1%, spesifisitas 92,0–96,0%; F1 0,75–0,84 untuk temuan klinis | DIETRICH | 98 | TERVERIFIKASI | NPV 72,5–77,3% tidak disebut naskah; pertimbangkan menyebut (relevan II.8) |
| B2-51 | :150 | Dietrich: satu institusi; kerangka audit agentik dengan pengambilan pedoman dan pemeriksaan konsistensi lintas dokumen sebagai arah lanjutan | DIETRICH | 100 | TERVERIFIKASI | Pertahankan |
| B2-52 | :152 | Skrabic: 102 laporan; 65,7–79,2% vs 48,0% | Skrabic (path tidak dicatat di berkas bukti) | 1–6 belum dicocokkan | TERVERIFIKASI (angka); halaman BELUM DIVERIFIKASI | 79,2% = 80/101 (penyebut 101, bukan 102). Cek halaman |
| B2-53 | :154 | Zeba: 104 ringkasan, 3.786 proposisi; P 0,8904, R 0,8234, F1 0,8556 | Zeba (path tidak dicatat di berkas bukti) | 1 | TERVERIFIKASI (hlm. 1) | LLM dilatih pada MIMIC-III. Klaim hlm. 6, 7, 10, 14, 15 belum dicek |
| B2-54 | :156 | Jaganathan: 3.372 catatan uji; 80,7% pada top-20 akronim | Jaganathan (path tidak dicatat di berkas bukti) | 4/5 belum dicocokkan | TERVERIFIKASI (angka); halaman BELUM DIVERIFIKASI | Cek halaman |
| B2-55 | II.4.1 :116 | n2c2 Track 3: delapan tim; Macro-F1 terbaik 0,8212; Indirect rata-rata 0,6713 | SD14 (path tidak dicatat di berkas bukti) | — | TERVERIFIKASI (angka); halaman BELUM DIVERIFIKASI | Cek hlm. 4–5 dan ukuran sampel (hlm. 7) |

Bahan paragraf *research gap* Bab I (a02, TSK-055; hanya sumber yang diperiksa a02). Didukung: (1) pemeriksaan konsistensi lintas dokumen disebut Dietrich & Stubbert (hlm. 100) sebagai arah lanjutan, bukan hasil yang ada; (2) pemeriksaan ringkasan terhadap rekam medis sumber sudah ada untuk ringkasan buatan LLM (Zeba dkk., hlm. 1), tidak untuk resume dokter terhadap catatan perkembangan; (3) kinerja tidak seragam antarkategori (Dietrich hlm. 98; NPV 72,5–77,3%); (4) KMK1596 tidak menetapkan format CPPT (B2-14), KMK1423 tidak memuat variabel CPPT (B2-22), SATUSEHAT tidak punya *resource* bernama CPPT tetapi punya Riwayat Perjalanan Penyakit lewat ClinicalImpression (B2-48, wajib dinuansakan); (5) pengkajian rekam medis menurut MRMIK 12 berkala dan berbasis sampel, tidak menyebut kesesuaian CPPT–resume (= E-08). Tidak didukung sumber yang diperiksa: tidak ada sumber yang memeriksa kesesuaian CPPT dengan resume sebelum klaim (jangan ditulis "belum pernah diteliti"); tidak ada sumber yang menyatakan satu komponen tidak cukup; sumber hibrida (Domingues; Ijadi Maghsoodi) tidak dibaca; P-6 tetap BELUM DIVERIFIKASI.
