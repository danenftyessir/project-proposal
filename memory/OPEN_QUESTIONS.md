---
file: OPEN_QUESTIONS
revision: 1
status: CURRENT
updated: 2026-11-05
updated_by: setup Phase 3 (sesi utama; A13 belum aktif)
based_on_commit: 7d59b85
---

# Open Questions

Isu terbuka dan permintaan persetujuan. Status: `TERBUKA` · `MENUNGGU DATA` · `MENUNGGU ANGGOTA` · `MENUNGGU PEMBIMBING` · `DIPUTUSKAN → D-xx` · `DITUTUP DENGAN ALASAN`. Tidak ada butir yang diselesaikan sistem tanpa keputusan pengguna (S-3).

## K1–K7 (konflik antardokumen, docs/ORCHESTRATION_ARCHITECTURE.md Lampiran A)

```yaml
id: K1
question: Gaya sitasi akhir — penulis-tahun sementara dengan hlm. (CONTEXT_TRANSFER kep. 1, header DRAFT 6) atau APA (keputusan tim 30 Oktober di Penyelarasan)?
why: A03 dan A08 memerlukan konvensi tetap; sampai diputuskan, A08 tidak menilai format terhadap salah satu gaya (S-14)
affected: [A03, A08, bab2/Bab_II_Revisi_Notulensi.md]
class: L3
pic: Pengguna
ask_to: Tim / pembimbing
status: TERBUKA
updated: 2026-11-05
refs: [D-11]
```

```yaml
id: K2
question: Judul capstone mana yang berlaku — judul lama di CONTEXT_TRANSFER kep. 18 atau judul baru di Penyelarasan (menunggu persetujuan pembimbing, isu tim 9)?
why: Menentukan keselarasan Bab I dan kontribusi individu
affected: [Bab I, sampul docx]
class: L3
pic: Abizzar (menurut Penyelarasan)
ask_to: Pembimbing
status: MENUNGGU PEMBIMBING
updated: 2026-11-05
refs: []
```

```yaml
id: K3
question: Peran Abizzar — frontend/antarmuka (CONTEXT_TRANSFER §1) atau ketua tim, Claim Review & Resolution Engineering (Penyelarasan)?
why: A06 memerlukan pembagian peran yang benar untuk memeriksa tumpang tindih kontribusi
affected: [A06]
class: L3
pic: Pengguna
ask_to: Tim
status: TERBUKA
updated: 2026-11-05
refs: []
```

```yaml
id: K4
question: Branch kerja proposal — CONTEXT_TRANSFER menyebut claude/determined-davinci-ueb8i9, sedangkan kerja aktual di main
why: A13 perlu tahu branch target commit proposal
affected: [A13]
class: L4
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-05
refs: []
```

```yaml
id: K5
question: Cakupan perawatan — rawat inap saja (CONTEXT_TRANSFER) atau rawat inap dan rawat jalan terbatas (Penyelarasan)?
why: Menentukan ruang lingkup Bab I
affected: [Bab I, A07, A11]
class: L3
pic: Pengguna
ask_to: Tim
status: TERBUKA
updated: 2026-11-05
refs: []
```

```yaml
id: K6
question: Lingkup kerja agent — CONTEXT_TRANSFER membatasi pada Bab II satu subbab per chat, sedangkan pekerjaan berjalan sudah Bab I
why: A01 memerlukan batas lingkup tugas
affected: [A01, A03]
class: L2
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-05
refs: [D-05]
```

```yaml
id: K7
question: CLAUDE.md induk IF4071 termuat di sesi proyek
why: Instruksi tidak relevan masuk konteks
affected: [semua sesi di checkout utama]
class: L4
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
note: Mitigasi teknis D-03 (claudeMdExcludes, omitClaudeMd) tanpa mengubah berkas induk; diuji T-02 setelah merge
updated: 2026-11-05
refs: [D-03]
```

## Penafsiran yang menunggu konfirmasi

```yaml
id: I-1
question: Apakah pertanyaan klarifikasi Supervisor tidak dihitung dalam batas tiga pertanyaan per sesi wawancara?
why: Penafsiran P2-04 yang berlaku sementara di prompt A04
affected: [A04, A01]
class: L4
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-05
refs: [P2-04]
```

```yaml
id: I-2
question: Apakah satu sesi wawancara berarti satu tugas wawancara A04 dari awal sampai ringkasan?
why: Penafsiran P2-04 yang berlaku sementara di prompt A04
affected: [A04, A01]
class: L4
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-05
refs: [P2-04]
```

## Dokumen tim dan data

```yaml
id: Q-P2-a
question: Siapa pemilik capstone-teammate-propose/Draft Bab 1 (1).docx/.pdf?
why: A06 tidak menebak pemilik dokumen
affected: [A06, PROJECT_STATE Team Docs Manifest]
class: L3
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-05
refs: []
```

```yaml
id: Q-P2-b
question: Siapa penulis Penyelarasan Pemahaman Capstone.md, dan adakah versi yang lebih baru di luar repo?
why: Penyelarasan adalah acuan kelompok untuk A06
affected: [A06]
class: L3
pic: Pengguna
ask_to: Tim
status: TERBUKA
updated: 2026-11-05
refs: []
```

```yaml
id: Q-P2-c
question: Dokumen Bab Abizzar — Bab II tersedia sejak 2026-11-05 (menurut nama berkas); apakah Bab I juga akan tersedia?
why: Pemeriksaan tiga arah A06
affected: [A06]
class: L3
pic: Pengguna
ask_to: Tim
status: MENUNGGU ANGGOTA
updated: 2026-11-05
refs: []
```

```yaml
id: Q-TEAM
question: Sembilan hal yang belum ditetapkan di Penyelarasan (bagian "Yang Masih Perlu Ditetapkan")
why: Berdampak pada ketiga anggota; dicatat sebagai rujukan, bukan disalin
affected: [Bab I, A06, A11]
class: L3
pic: Abizzar (menurut Penyelarasan)
ask_to: Tim / RSIA mitra / pembimbing
status: MENUNGGU ANGGOTA
updated: 2026-11-05
refs: []
```

```yaml
id: Q-RSIA-1
question: Apakah penyimpanan data pasien RSIA di folder OneDrive organisasi sesuai perjanjian data dengan RSIA?
why: Data asli dan turunan (.scratch/rsia/) tersinkron ke OneDrive (§A-8.3 risiko sisa 4)
affected: [D-17]
class: L3
pic: Pengguna
ask_to: Tim / RSIA mitra
status: TERBUKA
updated: 2026-11-05
refs: [D-17]
```

```yaml
id: Q-08
question: Tenggat Bab I 10 November 2026 hanya tercatat di work-state claude-mem; apakah benar?
why: claude-mem hanya alat recall; fakta wajib diverifikasi ke pengguna atau artefak
affected: [A01, TASK_TRACKER]
class: L4
pic: Pengguna
ask_to: Pengguna
status: TERBUKA
updated: 2026-11-05
refs: []
```
