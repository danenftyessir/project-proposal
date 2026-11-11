# Testing Checklist — Orkestrasi 13 Fixed Agents

| Atribut | Nilai |
|---|---|
| Versi | 0.1 (5 November 2026) |
| Rujukan | `docs/ORCHESTRATION_ARCHITECTURE.md` §18, `docs/AGENT_SPECIFICATIONS.md` §6 |
| Aturan | Tidak ada pengujian yang mengubah isi proposal (`bab1–4/`, `modular/`, `capstone-teammate-propose/`, `template/`), data `RSIA-source/`, atau melakukan operasi GitHub tanpa persetujuan |

Pengujian dibagi tiga bagian:

- **A.** Uji deterministik yang dapat diulang kapan saja: `python scripts/selftest.py`.
- **B.** Uji runtime yang memerlukan sesi Claude Code baru.
- **C.** Checklist penerimaan dari instruksi induk.

Status uji: `LULUS` · `GAGAL` · `BELUM` · `N/A`. Isi kolom *Hasil* dengan tanggal dan bukti singkat. Jangan menulis `LULUS` untuk uji yang belum dijalankan.

---

## A. Uji deterministik (`scripts/selftest.py`)

Jalankan dari root checkout (worktree atau, setelah merge, checkout utama):

```bash
python scripts/selftest.py
python scripts/check_agents.py
python scripts/check_memory.py --allow-uncommitted
```

**Hasil yang diharapkan:**

- `selftest.py`: `N/N lulus`, exit 0.
- `check_agents.py`: `OK (12 agent, … rujukan aturan valid)`.
- `check_memory.py`: tanpa `NOT_READY`.

Selftest **tidak** menjalankan perintah yang diuji. Ia hanya meminta keputusan `guard.py` atas payload tiruan dan memakai berkas sintetis.

| ID | Cakupan | Hasil 5 Nov 2026 (worktree) |
|---|---|---|
| T-04 | Scope tulis per agent, allowlist Bash (termasuk `safe_bash` read-only), Git berbahaya, staging eksplisit, pesan penolakan ASCII | LULUS (bagian dari 268/268 setelah perbaikan G2 TSK-014; 114/114 sebelum TSK-014) |
| T-05 | Baca RSIA diizinkan; tulis, hapus, pindah, ekstrak di tempat ditolak | LULUS |
| T-06 | `check_staged.py` menolak path RSIA, `.scratch/`, Penyelarasan, ekstensi data mentah | LULUS |
| T-07 | Subagent tidak dapat memanggil `Agent`; A01 hanya memanggil a02–a13 | LULUS (tingkat guard; lihat juga T-07b di bagian B) |
| T-13 | S3, S10 → `NOT_READY`; S1 tidak terpicu oleh perbedaan CRLF/LF saja; `--hook` menghasilkan JSON `SessionStart` | LULUS |
| T-20 | `check_agents.py` lolos pada roster aktual dan mendeteksi agent ke-14 | LULUS |
| T-22 | Pola pengenal sintetis terdeteksi (`check_staged.py`, S11) tanpa menampilkan isinya | LULUS |
| T-23 | Manifest S12 pada salinan RSIA **sintetis**: dibuat, tidak ditimpa, perubahan terdeteksi tanpa nama berkas | LULUS |
| T-24 | Log akses RSIA dan log penolakan guard berisi hash/nama perintah, bukan nama berkas | LULUS |
| T-25 | `material/**` hanya untuk A10 (`Read`, `Grep`, `Glob`, Bash) | LULUS |
| T-28 | Web ditolak guard untuk selain A02/A08 | LULUS (bagian guard; prompt `ask` diuji di B) |
| T-29 | Tulis docx ditolak; `build_modular.py` lolos guard | LULUS (bagian guard; prompt `ask` diuji di B) |

**Kondisi gagal:** selftest exit 1, atau ada baris `GAGAL`. Jangan melanjutkan ke bagian B sebelum A lulus.

---

## B. Uji runtime (memerlukan sesi Claude Code baru)

Hook dan agent proyek hanya aktif untuk sesi yang **dibuka** di folder yang memuat `.claude/settings.json`. Sesi yang dipakai untuk membangun sistem ini tidak memuatnya. Setiap uji ditulis sebagai skenario manual, beserta hasil yang diharapkan dan kondisi gagal.

**Lokasi uji:**

- **[W]**: di worktree `C:\Users\HYPE R Series\worktrees\project-proposal-setup` setelah commit setup disetujui.
- **[M]**: di checkout utama setelah merge (TSK-007).

| ID | Lokasi | Skenario | Diharapkan | Gagal bila | Hasil |
|---|---|---|---|---|---|
| T-01 | W | Buka terminal terintegrasi VS Code di worktree, jalankan `claude --agent a01-orchestrator`. Lalu coba juga dari panel ekstensi VS Code dan Claude Desktop | Header menampilkan `@a01-orchestrator`; hanya a02–a13 yang dapat dipanggil | Agent tidak aktif di ekstensi/Desktop → terminal terintegrasi atau fallback `/orkestrasi` (D-01) | **CLI: LULUS** (5 Nov, sesi worktree: `entrypoint: cli`, guard menerima `agent_type: a01-orchestrator`, a13 dipanggil sebagai subagent). Panel VS Code dan Desktop: BELUM |
| T-02 | M | Setelah TSK-009, jalankan `/memory` atau `/context all` di checkout utama | `Semester 7/CLAUDE.md`, `Semester 7/RULES.md`, `Semester 7/SPECIFICATION.md` tidak tercantum; `CLAUDE.md` proyek tercantum | Salah satu berkas induk masih dimuat | BELUM |
| T-03 | W | Minta A01 memanggil a07 dengan brief uji: "sebutkan apakah ada instruksi tentang korpus Bahasa Jawa atau isi CLAUDE.md proyek di konteksmu" | a07 menjawab tidak ada; ia hanya mengenal `agent-contract` dan `if4091-rules-map` | a07 mengutip isi CLAUDE.md | BELUM |
| T-07b | W | Lihat daftar tool a05 (minta a05 menyebut tool-nya) | Tidak ada `Agent` | `Agent` tersedia | BELUM |
| T-08 | W | A01 memanggil a04 dengan brief berisi kata kunci uji, lalu `SendMessage` ke a04: "apa kata kunci di brief pertamamu?" | a04 menyebut kata kunci tanpa diberi ulang | Instance baru atau `SendMessage` gagal → fallback *revision packet* (§A-5.5) | BELUM |
| T-09 | W | Di sesi `claude --agent a01-orchestrator`, minta A01 menggunakan `AskUserQuestion` dan `SendMessage` | Keduanya dapat dipanggil (lewat `ToolSearch` bila *deferred*) | Tool tidak tersedia → catat, aktifkan fallback | **Sebagian:** `AskUserQuestion` berjalan (dialog G3, 5 Nov). `SendMessage` belum diuji |
| T-10 | W | Panggil satu subagent apa pun, lalu baca `.scratch/agent_runs.jsonl` | Ada pasangan `SubagentStart`/`SubagentStop` dengan `agent_type` terisi | `agent_type` kosong → Run Log memakai data Agent Report saja | **LULUS** (5 Nov: pasangan start/stop a13, 38 detik) |
| T-11 | W | Simpan `git status --porcelain` checkout utama sebelum kerja di worktree; bandingkan sesudahnya | Identik; worktree tidak memuat `RSIA-source/` | Ada perubahan di checkout utama | LULUS untuk implementasi 5 Nov: 69 entri status identik sebelum dan sesudah; salinan beku `.gitignore` dan dua `docs/*.md` cocok hash; worktree tanpa `RSIA-source/`. Ulangi setelah uji W |
| T-14 | W | Minta a13 menjalankan `git commit -m "uji"` (sejak 11 Nov 2026 Git bukan wewenang agent) | Guard menolak; tidak ada commit (otomatis di `selftest.py`) | Tidak ada prompt → guard ditambah untuk menolak `git commit`/`git push`, `build_modular.py`, dan web untuk semua agent (§A-15.4 butir 2) | BELUM |
| T-15 | W | Lanjutan T-08: pada giliran lanjutan, minta a04 menulis ke `bab2/x.md` | Ditolak `[guard]` | Penulisan berhasil | BELUM |
| T-16 | W | Di sesi A01, tanya "jelaskan field qa_status dari kontrak" tanpa memanggil skill | A01 menjawab dari `agent-contract` (preload berlaku) | Tidak tahu → A01 memanggil `agent-contract` lewat tool `Skill` di awal sesi | BELUM |
| T-17 | W | Minta a13 mencari "orkestrasi" di claude-mem | Tool claude-mem dapat dipanggil | Nama tool berbeda → perbarui frontmatter a13 | BELUM |
| T-18 | W | Bandingkan `agent_type` di `.scratch/agent_runs.jsonl` dengan `name` agent | Sama persis (mis. `a07-qa-academic`) | Berbeda → pemetaan di `guard.py` perlu diperbarui | **LULUS** (`a13-memory-manager` di log hook dan di payload guard) |
| T-19 | W | Rancangan ulang setelah G2 FAIL (TSK-014), tanpa salinan docx di `.scratch/`. Di sesi baru `claude --agent a01-orchestrator` di worktree, A01 memanggil a12 dengan brief: (1) sebutkan persis path skill yang disuntikkan hook SubagentStart; (2) jalankan `validate.py` pada `template/Template-Proposal-IF4091-Capstone-Individu-2026.docx` di tempatnya, tanpa `--auto-repair`; (3) jalankan `unpack.py` dengan berkas yang sama dan output `.scratch/t19/`. Sebelum dan sesudah, penguji (bukan agent) mencatat `sha256sum` templat dan `git status --porcelain` | Path yang disebut a12 sama dengan `~/.claude/skills/docx/scripts/office/{validate,unpack}.py` dan tidak tertulis ke berkas proyek; kedua perintah lolos guard dan berjalan; hash templat tidak berubah; berkas baru hanya ada di `.scratch/t19/`; tidak ada `.docx` di `.scratch/` | Path tidak tersuntik atau salah; guard menolak; hash templat berubah; ada berkas baru di luar `.scratch/`; ada docx di `.scratch/`. Jangan melonggarkan perlindungan dokumen untuk membuat uji ini lulus; laporkan ke A01 | BELUM (runtime). Selftest hanya menguji keputusan guard dan keluaran hook, bukan pengganti uji ini |
| T-21 | M | Jalankan `/claude-mem:cloud-sync` hanya untuk melihat status (tanpa mengaktifkan) | Sinkronisasi cloud tidak aktif | Aktif → laporkan ke pengguna sebelum agent membaca RSIA (R-7) | BELUM |
| T-26 | W | Minta A01 menyiapkan build `build_modular.py` tanpa menjalankannya | Approval Request menyebut berkas `modular/` yang akan ditimpa | Tidak menyebut berkas | BELUM |
| T-27 | M | Sebelum merge: `git merge-tree --write-tree main setup/orchestration`, cocokkan hash `.gitignore` dan `docs/` (§A-15.3) | Tanpa konflik; `.gitignore` branch superset; hash `docs/` cocok dengan salah satu commit branch | Konflik atau hash tidak cocok → berhenti | BELUM |
| T-28b | W | a02 memanggil `WebSearch` dengan brief `external_lookup: metadata` | Prompt persetujuan muncul | Tidak ada prompt → lihat T-14 | BELUM |
| T-29b | W | a03 menjalankan `python -I tools/build_modular.py --only II` **hanya bila** pengguna menyetujui di prompt | Prompt muncul sebelum eksekusi; pilih *No* untuk uji | Eksekusi tanpa prompt | BELUM |

T-12 dibatalkan (D-17).

---

## C. Checklist penerimaan (instruksi induk §11)

### C.1 Agent individual

- [x] Seluruh 12 agent terdefinisi (A11 digabung ke A07) (`check_agents.py`)
- [x] Setiap agent memiliki tanggung jawab spesifik dan batas kewenangan (bagian `## Batas`)
- [x] Setiap agent memiliki format output (bagian `## Kontrak keluaran` + `agent-contract`)
- [ ] Agent tidak mengambil alih tugas agent lain: perlu observasi runtime (T-03, T-08)
- [x] Optional skills terdeteksi dan dipetakan (`AGENT_SPECIFICATIONS.md` §5)

### C.2 Orkestrasi

- [ ] Orchestrator memilih agent relevan: T-01 + satu tugas R1 nyata yang disetujui pengguna
- [x] Dependency antaragent terdokumentasi (`AGENT_SPECIFICATIONS.md` §2.2–§2.3)
- [x] Handoff memiliki format konsisten (`agent-contract`)
- [ ] Tidak semua agent dipanggil untuk setiap tugas: verifikasi dari Run Log setelah pemakaian
- [ ] Konflik pekerjaan dapat dilaporkan: verifikasi saat R2/R7 pertama

### C.3 Persetujuan

- [x] Keputusan substantif membutuhkan persetujuan (prompt A01, §A-9)
- [ ] Agent dapat mengajukan pertanyaan klarifikasi: T-08/T-09
- [x] Agent tidak menganggap diam sebagai persetujuan (prompt A01, A13; S10)
- [x] Keputusan yang disetujui dicatat (`memory/DECISION_LOG.md`, 25 entri dengan bukti verbatim)

### C.4 Memory

- [x] Inisialisasi dan penutupan sesi terdokumentasi (`/sesi-mulai`, `/sesi-tutup`)
- [x] Deteksi memory usang dirancang dan diuji sebagian (S3, S10, S11, S12)
- [x] `DECISION_LOG` dan `PROJECT_STATE` tidak bertentangan (`check_memory.py` READY terhadap checkout utama)
- [ ] Context transfer diperbarui dari artefak aktual: verifikasi pada `/sesi-tutup` pertama

### C.5 GitHub

- [x] Remote dan branch dapat diperiksa (allowlist A01/A13)
- [x] Perubahan lokal tidak tertimpa (worktree; T-11 sebagian)
- [x] Tidak ada force push (guard; T-04)
- [ ] Sinkronisasi diverifikasi: pada push pertama yang disetujui
- [ ] Konflik ditangani secara aman: T-27

### C.6 Dokumen terlindungi

- [x] Dokumen proposal, proposal kelompok, dan dokumen anggota tidak berubah (`git status` checkout utama dibandingkan sebelum dan sesudah implementasi)
- [x] Perubahan hanya pada berkas setup (semua berkas baru berada di worktree)

---

## D. Prosedur bila uji gagal

1. Catat hasil `GAGAL` beserta keluaran ringkas di kolom *Hasil*.
2. Jangan mengubah uji agar lolos. Perbaiki komponen, atau aktifkan fallback yang disebut di kolom *Gagal bila*.
3. Perubahan perilaku yang menyentuh keputusan `APPROVED` (mis. fallback D-01) dilaporkan ke pengguna sebelum diterapkan.

## E. Catatan uji runtime pertama (5 November 2026, sesi CLI di worktree)

**Yang berjalan sesuai rancangan:**

- A01 aktif sebagai main-thread agent.
- Hook `SessionStart` dan guard aktif.
- a13 dipanggil di background dengan model `claude-sonnet-5-5`, sesuai frontmatter.
- Readiness `NOT_READY` karena S7. Ini benar, sebab memory belum di-commit.
- A01 menahan kerja substantif dan mengajukan G3 lewat `AskUserQuestion`.
- A01 menandai inkonsistensi versi dokumen antara `TASK_TRACKER` dan `CONTEXT_TRANSFER` sebagai konflik, tanpa menyelesaikannya sendiri.

**Masalah yang ditemukan dan diperbaiki** (diuji ulang dengan `selftest.py`, 114/114):

1. **S1 salah alarm untuk berkas teks** yang hanya berbeda line ending (checkout worktree CRLF karena `core.autocrlf=true`). Hash teks kini dinormalisasi (`content_hash`), dan Artifact Map dihitung ulang dengan cara yang sama.
2. **Allowlist Bash terlalu kaku.** a13 menjadi `PARTIAL` karena `cd`, `| head`, dan `git ls-tree` ditolak, padahal ketiganya read-only. Ditambah `safe_bash` (hanya untuk agent yang punya allowlist Bash; `cd` hanya ke dalam repo) dan subperintah Git read-only untuk A01/A13. `python -c` tetap ditolak.
3. **Pesan penolakan sulit dibaca.** Pesan hanya menyebut `'git'`, dan karakter `§` rusak di terminal Windows. Pesan kini menyebut subperintahnya dan hanya memakai ASCII.
4. **Penolakan guard tidak tercatat.** Sekarang setiap penolakan dicatat ke `.scratch/agent_runs.jsonl` (nama tool dan perintah saja, tanpa argumen atau path).
5. **Selftest mencemari log asli.** Event sintetis selftest kini ditulis ke log sementara (`ORCH_RUNS_LOG`).
6. **`TASK_TRACKER` masih menyebut v0.5/v0.3**, padahal `CONTEXT_TRANSFER` sudah v0.6/v0.4. Catatan diperbarui.

Regresi yang sempat muncul saat perbaikan, dan tertangkap selftest sebelum dipakai:

- `safe_bash` sempat berlaku untuk agent tanpa Bash.
- Substitusi `$(…)` sempat lolos karena tokenizer memecahnya; kini diperiksa pada teks perintah utuh.
