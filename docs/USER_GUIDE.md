# User Guide — Orkestrasi 13 Agent untuk Proposal TA Capstone IF4091

Panduan pemakaian sehari-hari. Rancangan lengkap: `docs/ORCHESTRATION_ARCHITECTURE.md`; peran agent: `docs/AGENT_SPECIFICATIONS.md`.

## 1. Dua cara bekerja

| Cara | Kapan | Perintah |
|---|---|---|
| **Sesi orkestrasi** | Menulis/merevisi bab, menilai *research gap*, wawancara kesiapan, QA, konsistensi tim | Di terminal terintegrasi VS Code pada root repo: `claude --agent a01-orchestrator` |
| **Sesi biasa** | Pekerjaan kecil di luar alur proposal | `claude` atau panel ekstensi VS Code seperti biasa |

Sesi biasa tetap terkena perlindungan global: berkas asli `RSIA-source/` tidak dapat diubah, Git berbahaya ditolak, dan staging harus eksplisit.

Bila `--agent` tidak berjalan di lingkungan Anda (uji T-01), pakai fallback `/orkestrasi`. Skill ini belum dibuat dan baru dibuat bila T-01 gagal.

## 2. Awal sesi

1. Buka sesi orkestrasi. Hook `SessionStart` menjalankan `check_memory.py` otomatis.
2. Ketik `/sesi-mulai`. A01 melaporkan readiness (`READY` · `READY_WITH_WARNINGS` · `NOT_READY`), tugas berjalan, dan isu yang menunggu Anda.
3. Bila `NOT_READY`, A13 menyusun usulan rekonsiliasi. Tidak ada yang ditimpa tanpa persetujuan Anda.

## 3. Meminta pekerjaan

Tulis permintaan seperti biasa, misalnya "revisi II.3 agar celahnya lebih spesifik". A01 akan:

1. Mengklasifikasi tugas (R1–R9) dan memilih agent minimum.
2. Menghentikan proses dan bertanya bila ada keputusan substantif (gate **G1**). Anda akan melihat konteks, 2–4 opsi, konsekuensi, rekomendasi berlabel, dan satu pertanyaan.
3. Menjalankan QA, lalu menyajikan hasil untuk Anda terima atau tolak (gate **G2**).

**Cara menjawab persetujuan:**

- Jawab dengan menyebut opsi yang dipilih.
- "Lanjutkan" hanya dihitung sebagai persetujuan bila pertanyaannya menawarkan satu tindakan saja.
- Diam tidak pernah dihitung sebagai persetujuan.
- Jawaban Anda dicatat verbatim di `memory/DECISION_LOG.md`.

**Supervisor (A04):**

- Pertanyaan diajukan satu per giliran, maksimal tiga per sesi wawancara, tanpa jawaban yang disarankan.
- Klarifikasi tidak dihitung dalam batas tiga, dan pertanyaan berikutnya memerlukan sesi wawancara baru. Keduanya masih penafsiran sementara (I-1, I-2), jadi koreksi bila tidak sesuai.

**Kritik adversarial (A05):** dipanggil otomatis hanya untuk klaim utama yang baru atau berubah. Minta eksplisit ("kritik secara adversarial") bila Anda menginginkannya untuk hal lain.

## 4. Tindakan yang selalu meminta izin Anda

| Tindakan | Mekanisme |
|---|---|
| `git commit`, `git push` | Prompt Claude Code (aturan `ask`) + gate G3 dari A01 |
| `python -I tools/build_modular.py` (menimpa docx di `modular/`) | Prompt + Approval Request yang menyebut berkas yang ditimpa |
| `WebSearch`/`WebFetch` (A02/A08, metadata saja) | Prompt per panggilan + izin per tugas |
| Membaca data `RSIA-source/` | Hanya bila tugas memerlukannya; A01 mencantumkan scope dan alasan di brief. Akses tercatat (hash) di `.scratch/agent_runs.jsonl` |

`tools/build_docx.py` dan `tools/build_with_toc.py` diblokir untuk semua agent sampai path dan outline-nya diperbaiki (P2-02).

## 5. Data RSIA

- Agent boleh membaca data RSIA bila relevan (D-17), tetapi tidak pernah mengubah berkas aslinya.
- Data turunan disimpan di `.scratch/rsia/`, yang tidak pernah di-commit.
- Laporan, memory, dan naskah tidak memuat pengenal pasien atau kunjungan. Nama berkas di arsip RSIA juga termasuk pengenal.
- Angka klaim pending (D-19):
  - Angka yang tercantum di PDF Breakdown menunggu pembahasan tim.
  - Angka hasil hitung dari data RSIA boleh dilaporkan kepada Anda dalam agregat.
  - Bila angka hasil hitung itu sama dengan angka di PDF Breakdown atau Penyelarasan, angka tersebut belum dimasukkan ke naskah sampai dibahas tim.

## 6. Akhir sesi

1. Ketik `/sesi-tutup`. A13 memperbarui memory dan menjalankan pemeriksaan.
2. A01 menampilkan gate **G3**: daftar path yang akan di-commit, pesan commit, dan branch. Commit hanya terjadi setelah Anda menyetujui, dan push juga memerlukan persetujuan sendiri.
3. Bila tidak ingin commit, katakan saja. Memory tetap tersimpan di working tree, dan sesi berikutnya akan memberi peringatan S7.

## 7. Pemeriksaan manual kapan saja

```bash
python scripts/check_memory.py              # readiness memory
python scripts/check_memory.py --metrics    # ringkasan efisiensi dari Run Log
python scripts/check_agents.py              # 13 agent valid
python scripts/selftest.py                  # uji regresi deterministik
python scripts/check_staged.py              # periksa staging sebelum commit manual
```

## 8. Mengubah sistem

Semua berkas di `.claude/`, `scripts/`, `docs/`, `CLAUDE.md`, dan `RULES.md` adalah konfigurasi (kelas P2). Agent tidak mengubahnya.

Saat Anda mengubahnya, perbarui juga:

- `docs/AGENT_SPECIFICATIONS.md` §4 bila mengubah `.claude/policy/write_scopes.json`, karena keduanya harus identik.
- Changelog dokumen.

Setelah perubahan, jalankan `python scripts/selftest.py` dan `python scripts/check_agents.py`.
