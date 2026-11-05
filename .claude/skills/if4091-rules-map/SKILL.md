---
name: if4091-rules-map
description: Peta bagian RULES.md dan CLAUDE.md yang wajib dibaca per agent dan jenis tugas pada Proposal TA Capstone IF4091. Berisi rujukan heading saja, bukan salinan aturan. Dipreload ke agent yang tidak memuat CLAUDE.md (omitClaudeMd).
user-invocable: false
---

# Peta aturan IF4091

Agent a02–a13 tidak memuat `CLAUDE.md` secara otomatis. Aturan penulisan tetap berlaku dan dibaca **dari berkas aslinya**. Peta ini hanya menunjuk bagian yang wajib dibaca, dan isi aturannya tidak disalin di sini.

## Cara membaca satu bagian

1. `Grep` heading di berkas sumber. Contoh: pola `^### 6\.5 ` di `RULES.md` mencari "§6.5"; pola `^## 8\. ` mencari bagian tingkat dua.
2. `Read` dari baris heading itu sampai heading setingkat berikutnya (pakai `offset` dan `limit`).
3. Jangan membaca `RULES.md` (≈1.700 baris) atau `CLAUDE.md` (≈660 baris) secara utuh.

Bila bagian yang dirujuk tidak ditemukan, laporkan di `open_questions`; jangan mengganti dengan ingatan.

## Peta per agent

| Agent | Wajib dibaca (sesuai jenis tugas) |
|---|---|
| a01-orchestrator | CLAUDE.md §11.3, §11.9, §11.10; RULES.md §12.8 |
| a02-research-evidence | RULES.md §4.2, §4.3, §4.4, §5, §10.1, §12.1; CLAUDE.md §3, §11.1, §11.2 |
| a03-academic-writer | CLAUDE.md §2, §3, §5; bagian CLAUDE.md §4 untuk bagian yang ditulis; RULES.md §3 (bagian terkait), §4.4, §11.7, §11.8, §11.9, §11.10; RULES.md §6.1–§6.10 sesuai jenis perubahan; Bab I: RULES.md §13 dan CLAUDE.md §12 |
| a04-supervisor | RULES.md §3, §8.2, §8.3, §11.7, §13; CLAUDE.md §12.6 |
| a05-critical-reviewer | RULES.md §4.2, §8.1, §8.2, §8.4, §12.1 |
| a06-cross-proposal | RULES.md §12.4; CLAUDE.md §11.4, §11.5 |
| a07-qa-academic | RULES.md §3, §7, §8.2, §13.6; CLAUDE.md §12.6 |
| a08-qa-citation | RULES.md §4.4, §11.9, §12.1; CLAUDE.md §3, §5.10, §11.2 |
| a09-qa-editorial | RULES.md §6.1, §6.2, §6.3, §6.4, §6.5, §6.6, §6.7, §6.8, §6.9, §6.10, §7, §8.5; CLAUDE.md §5.1, §5.2, §5.3, §5.4, §5.5, §5.11, §5.12 |
| a10-qa-structure | RULES.md §2, §11.3, §11.5, §11.6, §11.7, §11.8, §11.10, §11.11; CLAUDE.md §5.7, §5.8 |
| a11-qa-technical | RULES.md §3.5, §3.6, §8.2, §9, §10.3, §13.5; CLAUDE.md §12.5 |
| a12-qa-integrity | RULES.md §11.10, §11.11; CLAUDE.md §5.10 |
| a13-memory-manager | RULES.md §12.5, §12.8; CLAUDE.md §11.6, §11.7, §11.9 |

Catatan penomoran `CLAUDE.md`: subbagian §5.6–§5.10 berada di bawah bagian 4 (urutan di berkas tidak berurutan). Cari dengan pola heading `^### 5\.10 `, bukan dengan menghitung posisi.

## Aturan pengguna yang selalu berlaku

Aturan berikut berasal dari keputusan dan instruksi pengguna (bukan RULES.md). Ringkasannya dimuat di sini karena berlaku untuk semua agent:

- Klaim tentang isi paper diambil dari PDF di repo dengan nomor halaman, bukan dari ingatan atau ringkasan AI.
- Jangan melebih-lebihkan temuan paper agar cocok dengan desain.
- Jangan menambah sumber baru ke daftar referensi tanpa diminta (usulan masuk `open_questions`).
- Utamakan prosa; daftar poin hanya untuk tabel perbandingan karya terdahulu.
- Gaya sitasi akhir belum diputuskan (K1). Ikuti konvensi yang sudah ada di naskah dan jangan menilai format terhadap gaya lain.
- Data RSIA dan angka klaim pending: D-11, D-17, D-19 (`memory/DECISION_LOG.md`).
