# Kebutuhan Literatur untuk Revisi Bab II

Disusun 3 November 2026 dari notulensi bimbingan, draf `modular/13523136-Proposal-IF4091-Capstone-Individu-2026-Modular-Bab-II_Editorial.docx`, `Sumber Literatur Bab 2.pdf`, dan isi `source/` setelah dirapikan (lihat `source/INDEKS.md`).

Status dokumen: `DRAF`. Butir bertanda `[PERLU VERIFIKASI]` belum dicek ke dokumen aslinya.

## 1. Kondisi draf saat ini terhadap notulensi

| Masukan notulensi | Kondisi draf Bab II | Tindakan |
| --- | --- | --- |
| Bab II hanya berisi apa yang dibuat orang lain | Tujuh subbab punya sub-subbab "Sintesis dan Celah"; II.8 berisi Tabel II.1 perbandingan dan "Celah Penelitian" | Hapus semua "Sintesis dan Celah" dan II.8. Celah yang memotivasi TA pindah ke Bab I; tabel perbandingan dan analisis kecocokan pindah ke Bab III dengan rujukan ke subbab Bab II |
| Pengelompokan wajar, jangan dipaksakan | Setiap subbab berpola 1–3 sub-subbab + "Sintesis dan Celah" | Susun ulang mengikuti urutan masalah (bagian 3) |
| Sedikit tapi detail | 39 sumber, sebagian hanya 2–3 kalimat (mis. Jia dkk., CTKGR, Barsasella dkk.) | Pilih 1–3 sumber jangkar per subbab dan bahas mendalam; sumber berstatus `tinjau` di INDEKS dipertimbangkan untuk dibuang |
| Standar dan aturan Indonesia diutamakan | Tidak ada pembahasan Permenkes 24/2022, standar variabel RME, SATUSEHAT, atau standar akreditasi; FHIR hanya muncul di daftar singkatan | Tambah subbab regulasi dan standar Indonesia sebagai pembuka (bagian 2.1) |
| Isi CPPT/RME dijelaskan eksplisit | Belum ada sama sekali | Tambah subbab kolom/skema CPPT dan cara menstrukturkannya (bagian 2.2) |
| Gambar dan diagram | Hanya tiga persamaan; belum ada gambar | Rencanakan gambar: skema CPPT/variabel RME, resource FHIR rawat inap, arsitektur RAG, skema KG klinis |
| Singkatan lengkap pertama kali di tiap bab | INA-CBG dan JKN sudah dijabarkan; CPPT belum muncul di badan teks | Periksa ulang setelah struktur baru jadi |
| Evaluasi NLP dilewati; perbandingan ke Bab III | II.7 Evaluasi dan II.8 Perbandingan masih ada | Keluarkan II.7 dan II.8 dari Bab II |

## 2. Kebutuhan literatur per butir notulensi

Kolom **Sudah ada** merujuk folder di `source/`. Kolom **Perlu ditambah** hanya memuat dokumen yang keberadaannya sudah dicek di web pada 3 November 2026, kecuali yang ditandai.

### 2.1 Standar dan aturan Indonesia (masukan umum)

Notulensi meminta bukti bahwa standar memang dipakai di Indonesia. Rantai bukti yang tersedia:

1. **Permenkes 24/2022** (`01_…`) mewajibkan RME (Pasal 3), pengisian lengkap dan berurutan dengan nama, waktu, dan tanda tangan (Pasal 16), pengisian informasi klinis terintegrasi dalam satu dokumen bila ada lebih dari satu jenis tenaga kesehatan (Pasal 17, dasar hukum CPPT), input kode klasifikasi penyakit untuk klaim berdasarkan rekam medis (Pasal 19), keterhubungan dengan platform interoperabilitas Kemenkes (Pasal 21), dan sistem elektronik yang mengacu pada "variabel dan meta data yang ditetapkan oleh Kementerian Kesehatan" (Pasal 11).
2. Pasal 11 itu menunjuk ke **KMK HK.01.07/MENKES/1423/2022** tentang Pedoman Variabel dan Meta Data pada Penyelenggaraan RME. Lampirannya memuat dataset rawat jalan, IGD, laboratorium, **rawat inap**, dan farmasi, dengan nama variabel, tipe data, format, definisi operasional, dan rujukan per variabel. **Belum ada di repo.**
3. **Permenkes 26/2021** (`01_…`, salinan berteks di `external/01_…`) menetapkan ICD-10 versi 2010 dan ICD-9-CM versi 2010 untuk koding dan verifikasi klaim INA-CBG.
4. **SATUSEHAT** memakai HL7 FHIR untuk pertukaran data dan menetapkan ICD-10 (2010), ICD-9-CM, SNOMED CT, LOINC, dan KFA sebagai terminologi. Bukti pemakaian di lapangan: Heryawan dkk. (2025), tesis ITB01 dan ITB02 (`04_…`). Dokumentasi resmi SATUSEHAT **belum diarsipkan di repo**.
5. **SNOMED CT di Indonesia** masih tahap awal menurut Pertiwi dkk. (2026); panduan SATUSEHAT menyebut deskripsi SNOMED CT perlu diterjemahkan resmi lebih dahulu. Status keanggotaan Indonesia di SNOMED International tidak ditemukan dalam pencarian `[PERLU VERIFIKASI]`.

| Perlu ditambah | Alasan | Sumber |
| --- | --- | --- |
| KMK HK.01.07/MENKES/1423/2022, Pedoman Variabel dan Meta Data RME | Skema resmi kolom RME rawat inap; jawaban langsung untuk "kolomnya apa saja" | [JDIH Kemenkes](https://jdih.kemkes.go.id/documents/keputusan-menteri-kesehatan-nomor-hk0107menkes14232022) |
| KMK HK.01.07/MENKES/1596/2024, Standar Akreditasi Rumah Sakit | Menggantikan KMK 1128/2022; memuat standar asesmen ulang dan format/isi rekam medis (bab MRMIK). Kewajiban SOAP/CPPT dalam teks resminya belum dicek `[PERLU VERIFIKASI]` | [JDIH Kemenkes](https://jdih.kemkes.go.id/documents/keputusan-menteri-kesehatan-nomor-hk0107menkes15962024) |
| Kepdirjen Yankes HK.02.02/D/47104/2024, instrumen survei akreditasi RS | Elemen penilaian yang diturunkan dari KMK 1596/2024; tempat mencari rumusan CPPT yang dinilai surveior | [keslan.kemkes.go.id](https://keslan.kemkes.go.id/unduhan/fileunduhan_1737603973_377193.pdf) |
| Dokumentasi terminologi dan profil rawat inap SATUSEHAT | Bukti standar terminologi yang dipakai dan contoh resource FHIR rawat inap untuk gambar skema | [Terminologi](https://satusehat.kemkes.go.id/platform/docs/id/terminology/), [Rawat Inap](https://satusehat.kemkes.go.id/platform/docs/id/interoperability/rawat-inap-new/), [SNOMED CT di SATUSEHAT](https://satusehat.kemkes.go.id/platform/docs/id/terminology/snomed-ct/guide/) |

Halaman web SATUSEHAT dapat berubah; simpan sebagai PDF dengan tanggal akses.

### 2.2 Isi CPPT/RME dan cara menstrukturkannya

| Kebutuhan | Sudah ada | Perlu ditambah |
| --- | --- | --- |
| Kolom dan aturan pengisian CPPT | Permenkes 24/2022 Pasal 16–17; Oktavia Az dkk. (2021) menyebut isi lembar CPPT (identitas, tanggal, jam, catatan perkembangan/evaluasi) dan mengacu MIRM 13.3 (standar akreditasi lama); Nadi dkk. (2024) | KMK 1423/2022 (dataset rawat inap) dan KMK 1596/2024 (bagian 2.1) |
| Struktur SOAP dan relasi antarbagian | Gao dkk. (2022), Socrates dkk. (2023), Gao dkk. (2023, n2c2 Track 3), Machado de Oliveira dkk. (2024) di `03_…` | Tidak perlu tambahan |
| Pemetaan isi ke terminologi baku | Gaudet-Blavignac dkk. (2026), Pertiwi dkk. (2026) di `04_…`; Chen dkk. (2026) di `06_…` | Chang & Sung (2024), *Use of SNOMED CT in LLMs: Scoping Review* (ganti SD11 yang salah unduh) |
| Representasi sebagai knowledge graph | Lihat 2.5 | |

Gambar yang disarankan: (a) tabel atau diagram kolom CPPT menurut KMK 1423/2022; (b) pemetaan satu entri CPPT ke bagian S-O-A-P; (c) pemetaan ke resource FHIR SATUSEHAT (Encounter, Condition, Observation, dsb. `[PERLU VERIFIKASI]` terhadap profil rawat inap).

### 2.3 Rekomendasi penggunaan LLM di bidang medis

Notulensi: cari rekomendasi tentang aspek yang boleh dan tidak boleh dikerjakan LLM; karena aturan pemerintah Indonesia belum ada, rekomendasi dari penelitian atau organisasi profesi boleh dipakai asal ada buktinya.

**Bukti bahwa aturan Indonesia belum ada (per Oktober 2026):**

- SE Menkominfo No. 9 Tahun 2023 tentang Etika Kecerdasan Artifisial berlaku lintas sektor, bukan khusus kesehatan. **Belum ada di repo.**
- Perpres Peta Jalan AI dan Perpres Etika AI masih "dalam proses penandatanganan" pada 30 Oktober 2026 ([CNBC Indonesia](https://www.cnbcindonesia.com/tech/20261030162941-37-781009/ri-atur-ai-sesuai-risiko-komdigi-beberkan-isi-regulasinya)). Isi yang disampaikan: keputusan akhir tetap di tangan manusia, pendekatan berbasis risiko, dan label produk AI. Ini berita, bukan dokumen hukum; kutip hati-hati dan perbarui bila Perpres terbit.
- Kemenkes menyatakan akan menyusun regulasi AI khusus kesehatan (Juli 2025) dan mengadakan konferensi nasional tentang ekosistem AI kesehatan pada 8 Juni 2026 ([kemkes.go.id](https://kemkes.go.id/id/kemenkes-tekankan-pemanfaatan-ai-kesehatan-harus-diiringi-tata-kelola-ketat-dan-etika-yang-kuat)).
- Pedoman dan Standar Etik Penelitian dan Pengembangan Kesehatan Nasional (KEPPKN) memuat bagian aspek etik penelitian kecerdasan buatan ([repositori Kemenkes](https://repository.badankebijakan.kemkes.go.id/id/eprint/4214/1/Pedoman%20dan%20Standar%20Etik%20Penelitian%20dan%20Pengembangan%20Kesehatan%20Nasional.pdf)). Relevan untuk etika penelitian TA, bukan untuk operasional sistem. **Belum ada di repo.**
- Fitriasari & Umasugi (2026) (`01_…/SD01`) mengusulkan *regulatory sandbox* AI kesehatan yang terhubung dengan SATUSEHAT.

**Rekomendasi yang sudah ada di `12_…`:** AHIMA (2024), WHO (2024), ESMO ELCAP (Wong dkk., 2025), Devanand dkk. (2026), Denecke dkk. (2024), Sul & Kim (2025). Kandidat jangkar: ESMO ELCAP (kategori penggunaan disusun lewat Delphi 20 pakar) dan Devanand dkk. (stratifikasi risiko per tugas), karena keduanya memetakan jenis tugas ke tingkat pengawasan. AHIMA (2024) hanya 4 halaman dan berbasis wawancara; tidak *peer-reviewed*. Isi rekomendasi per tugas di keenam dokumen belum dibaca rinci; lakukan sebelum menulis.

**Perlu ditambah:** SE Menkominfo 9/2023 dan pedoman KEPPKN (lihat di atas). Tidak perlu paper rekomendasi baru selama keenam dokumen di `12_…` sudah memberi pemetaan tugas yang dibutuhkan.

### 2.4 Akurasi per kategori kesalahan dan peringatan tingkat kepercayaan

Notulensi: untuk kategori yang skornya jelek, sistem perlu memberi peringatan tingkat kepercayaan kepada pengguna.

| Kebutuhan | Sudah ada | Perlu ditambah |
| --- | --- | --- |
| Bukti bahwa kinerja berbeda per kategori | Dietrich & Stubbert (2026) (`external/02_…`): F1 ≥0,96 pada kategori identitas/obat, 0,75–0,84 pada ketidaksesuaian tanda vital/pemeriksaan fisik; Kim dkk. (2026) `M6` | |
| LLM tidak tahu kapan ia salah | Griot dkk. (2025), Testoni & Calixto (2026) | Omar dkk. (2025), *Benchmarking the Confidence of LLMs in Answering Clinical Questions* (ganti SD08) |
| Kalibrasi pada tugas pengodean dokumen klinis | | Popescu dkk. (2026), *JMIR AI* e78764 (ganti SD07). Catatan: model transformer *fine-tuned* untuk kode penyebab kematian, bukan LLM generatif |
| Cara mengomunikasikan ketidakpastian ke pengguna | Kompa dkk. (2021); Rezaeian dkk. (2025); Schimmelpfennig dkk. (2025, CeRTS) | |
| Risiko pengguna terlalu percaya | Goddard dkk. (2012), Kim dkk. (2025), Vasconcelos dkk. (2023) di `external/04_…` (milik tim) | |

Opsional: Boie dkk. (2026), *Calibration of Self-Reported Confidence and Accuracy of LLMs in Medical Question Answering*, *Journal of Medical Systems* ([Springer](https://link.springer.com/article/10.1007/s10916-026-02430-0)).

### 2.5 Knowledge graph dan ontologi khusus rekam medis

Notulensi: KG yang dipakai di draf tidak spesifik medis (Syeda & Reddy, 2026). Cari KG atau ontologi khusus rekam medis.

Sudah ada di `05_…`, semuanya spesifik rekam medis:

- **Xiao dkk. (2022)**, FHIR-Ontop-OMOP: KG klinis dibangun dari data rekam medis berstandar OMOP CDM dan diekspos sebagai FHIR RDF. Paling dekat dengan arahan "standar dulu", karena FHIR dipakai SATUSEHAT.
- **Rotmensch dkk. (2017)**: KG penyakit–gejala dipelajari dari rekam medis.
- **Murali dkk. (2023)**: survei konstruksi, pelengkapan, dan penerapan KG berbasis rekam medis.
- **Gaudet-Blavignac dkk. (2026)** dan **Pertiwi dkk. (2026)** (`04_…`): SNOMED CT sebagai ontologi klinis.

**Perlu ditambah:** Chang & Sung (2024) (ganti SD11). Kandidat opsional: *Use of SNOMED CT, 2020–2025: literature review*, *JAMIA* 33(9):1798 ([OUP](https://academic.oup.com/jamia/article/33/9/1798/8706593)); penulis belum dicek `[PERLU VERIFIKASI]`.

Syeda & Reddy (2026), KG-ACE, dan CTKGR turun menjadi pendukung atau dibuang.

### 2.6 Anonimisasi

Notulensi: menghapus kolom identitas saja tidak cukup, karena kombinasi riwayat penyakit dan tahun dapat mengungkap identitas. Pakai pedoman yang ada, jangan merancang cara sendiri.

| Kebutuhan | Sudah ada di `14_…` | Perlu ditambah |
| --- | --- | --- |
| Pedoman resmi | HHS OCR (2012): metode Safe Harbor dan Expert Determination; NIST SP 800-188 (2023): teknik dan tata kelola de-identifikasi | |
| Bukti bahwa kombinasi atribut cukup untuk re-identifikasi | Rocher dkk. (2019); El Emam dkk. (2011); Kudlicki dkk. (2026, pergeseran tanggal dapat dibalik); Krzyzanowski & Manson (2022) | Sweeney, L. (2002). k-anonymity: A model for protecting privacy. *Int. J. Uncertainty, Fuzziness and Knowledge-Based Systems*, 10(5), 557–570. Sumber asal konsep kuasi-identifier `[PERLU VERIFIKASI metadata dan akses]` |
| Penerapan model privasi pada data klinis | Jeon dkk. (2020): k-anonymity, l-diversity, t-closeness pada OMOP-CDM | |
| Definisi istilah | Chevrier dkk. (2019) | |
| Aturan Indonesia | UU 27/2022 PDP (`01_…`); Permenkes 24/2022 Pasal 29–32 (keamanan dan kerahasiaan) | **PP 28/2024** pelaksanaan UU 17/2023 tentang Kesehatan: Pasal 777–785 tentang rekam medis, serta bagian pengelolaan dan pemrosesan data kesehatan. Ada tidaknya pasal anonimisasi/pseudonimisasi belum dicek `[PERLU VERIFIKASI]` |
| Standar internasional khusus kesehatan | | ISO 25237:2017, *Health informatics — Pseudonymization*. Kemungkinan berbayar `[PERLU VERIFIKASI akses]` |
| Konteks Indonesia | Atikasari (2024), Ganeswara (2025), tesis ITB | |

### 2.7 Arsitektur RAG (untuk gambar)

Sudah cukup: Lewis dkk. (2020) sebagai makalah asal RAG dan Gao dkk. (2023) untuk taksonomi naive/advanced/modular RAG (`10_…`). Gao dkk. (2023) adalah preprint arXiv; cek status terbitnya. Statechart (Harel, 1987, `external/07_…`) relevan bila komponen Anda memakai pemodelan keadaan temuan; pembahasan ledakan jumlah state dibandingkan state diagram RPL ada di makalah Harel.

## 3. Usulan susunan Bab II berbasis masalah

Masalah di Bab I: ketidaksesuaian antara CPPT dan resume medis menyebabkan klaim JKN pending. Literatur diturunkan dari pertanyaan yang muncul dari masalah itu:

| Subbab | Pertanyaan yang dijawab | Sumber jangkar |
| --- | --- | --- |
| II.1 Rekam medis elektronik, CPPT, dan resume medis dalam regulasi Indonesia | Dokumen apa yang dibandingkan, kolomnya apa, aturannya apa? | Permenkes 24/2022, KMK 1423/2022, KMK 1596/2024, Oktavia Az dkk. (2021) |
| II.2 Klaim INA-CBG dan peran resume medis | Bagaimana isi dokumen memengaruhi klaim? | Permenkes 26/2021, Simbolon & Gani (2023) |
| II.3 Standar interoperabilitas dan terminologi klinis | Standar apa yang dipakai di Indonesia untuk menstrukturkan isi? | SATUSEHAT/FHIR (Heryawan dkk., 2025), SNOMED CT (Pertiwi dkk., 2026; Gaudet-Blavignac dkk., 2026), struktur SOAP (Socrates dkk., 2023) |
| II.4 Representasi rekam medis sebagai knowledge graph | Bagaimana isi itu dijadikan graf? | Xiao dkk. (2022), Murali dkk. (2023) |
| II.5 Pemeriksaan dokumentasi klinis dengan LLM | Apa yang sudah dilakukan orang untuk mendeteksi kesalahan dokumentasi? | Dietrich & Stubbert (2026), Kim dkk. (2026) |
| II.6 RAG dan verifikasi keluaran | Bagaimana keluaran LLM dijangkarkan ke bukti? | Lewis dkk. (2020), Zeba dkk. (2026) |
| II.7 Rekomendasi penggunaan LLM klinis dan ketidakpastian | Untuk apa LLM boleh dipakai, dan kapan pengguna harus diperingatkan? | ESMO ELCAP (2025), Devanand dkk. (2026), Griot dkk. (2025), Kompa dkk. (2021) |
| II.8 De-identifikasi dan anonimisasi | Bagaimana data dikirim ke layanan AI tanpa mengungkap identitas? | UU PDP, HHS (2012), NIST SP 800-188, Rocher dkk. (2019) |

Sub-subbab hanya dibuat bila isinya memang terbagi. Bila pembimbing meminta judul kelompok mengikuti taksonomi bidang, kandidat simpul ACM CCS 2012 yang relevan antara lain *Applied computing → Life and medical sciences → Health informatics*, *Computing methodologies → Artificial intelligence → Natural language processing*, *Computing methodologies → Artificial intelligence → Knowledge representation and reasoning*, dan *Security and privacy → Human and societal aspects of security and privacy → Privacy protections* `[PERLU VERIFIKASI ke dokumen ACM CCS 2012]`.

## 4. Daftar unduhan berikutnya (urut prioritas)

1. KMK HK.01.07/MENKES/1423/2022 (variabel dan metadata RME) → `source/01_Regulasi_dan_Kebijakan_Indonesia/`
2. KMK HK.01.07/MENKES/1596/2024 (standar akreditasi RS) dan Kepdirjen HK.02.02/D/47104/2024 → `01_…`
3. Dokumentasi SATUSEHAT: terminologi, panduan SNOMED CT, profil rawat inap (simpan PDF + tanggal akses) → `04_…`
4. Unduh ulang tiga berkas salah: Chang & Sung (2024) → `04_…`; Omar dkk. (2025) dan Popescu dkk. (2026) → `13_…`. Setelah itu `_salah_unduh/` boleh dihapus
5. PP 28/2024 → `01_…`
6. SE Menkominfo 9/2023 dan pedoman KEPPKN → `01_…` atau `12_…`
7. Sweeney (2002) → `14_…`; ISO 25237:2017 bila tersedia lewat ITB
8. Opsional: Boie dkk. (2026), JAMIA SNOMED CT 2020–2025

Belum dapat diperoleh dari daftar awal: Maleki dkk. (2026), Mohanty dkk. (2027), Lathifah dkk. (2020), Fahlevi dkk. (2021). Maleki dkk. hanya penting bila subbab hibrida dipertahankan; tiga lainnya tidak diperlukan oleh susunan di bagian 3.

## 5. Yang belum dapat diverifikasi

- Isi rekomendasi per tugas di keenam dokumen `12_…` belum dibaca rinci.
- Rumusan resmi CPPT/SOAP di KMK 1596/2024 belum dibaca; sumber sekunder (medminutes.io) menyebut format SOAP atau SBAR.
- Pasal anonimisasi di PP 28/2024 belum dicek.
- Status keanggotaan Indonesia di SNOMED International tidak ditemukan.
- Penulis komentar *The Lancet* (SD04) belum dicatat.
