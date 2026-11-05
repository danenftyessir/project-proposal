---
file: DECISION_LOG
revision: 2
status: CURRENT
updated: 2026-11-05
updated_by: a13-memory-manager
based_on_commit: 7d59b85
---

# Decision Log

Keputusan yang sudah diambil pengguna. Hanya A13 yang menulis berkas ini, dan hanya dengan `approval_evidence` berisi kutipan verbatim (§A-9.6). Sumber kutipan: docs/ORCHESTRATION_ARCHITECTURE.md Lampiran C. Jam persetujuan tidak tercatat di sesi, sehingga `answered_at` hanya berisi tanggal.

Status: `APPROVED` · `DEFERRED` · `SUPERSEDED by D-xx` · `REJECTED` · `WAIVED`.

## D-01

```yaml
id: D-01
decision: Agent 01 sebagai main-thread agent (claude --agent a01-orchestrator), fallback skill /orkestrasi bila tidak didukung di VS Code
class: L4
status: APPROVED (bersyarat uji T-01)
date: '2026-11-05'
approval_evidence:
  question: Register keputusan §19 docs/ORCHESTRATION_ARCHITECTURE.md v0.1, baris D-01
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - 'D-01: Setuju bersyarat. Agent 01 menjadi main-thread agent, dengan fallback apabila tidak didukung di VS Code.'
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-2 (atas ORCHESTRATION_ARCHITECTURE.md v0.1)
  scope: Agent 01 sebagai main-thread agent (claude --agent a01-orchestrator), fallback skill /orkestrasi bila tidak didukung di VS Code
```

## D-02

```yaml
id: D-02
decision: Nesting subagent dimatikan (hub-and-spoke)
class: L4
status: APPROVED
date: '2026-11-05'
approval_evidence:
  question: Register keputusan §19 docs/ORCHESTRATION_ARCHITECTURE.md v0.1, baris D-02
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - 'D-02: Setuju.'
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-2 (atas ORCHESTRATION_ARCHITECTURE.md v0.1)
  scope: Nesting subagent dimatikan (hub-and-spoke)
```

## D-03

```yaml
id: D-03
decision: 'Isolasi konteks: claudeMdExcludes lokal + omitClaudeMd di subagent + skill if4091-rules-map'
class: L4
status: APPROVED (dengan uji T-02, T-03)
date: '2026-11-05'
approval_evidence:
  question: Register keputusan §19 docs/ORCHESTRATION_ARCHITECTURE.md v0.1, baris D-03
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - 'D-03: Setuju, dengan pengujian isolasi konteks.'
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-2 (atas ORCHESTRATION_ARCHITECTURE.md v0.1)
  scope: 'Isolasi konteks: claudeMdExcludes lokal + omitClaudeMd di subagent + skill if4091-rules-map'
```

## D-04

```yaml
id: D-04
decision: Struktur memory 7 berkas tanpa CHANGELOG dan AGENT_LOG
class: L4
status: APPROVED
date: '2026-11-05'
approval_evidence:
  question: Register keputusan §19 docs/ORCHESTRATION_ARCHITECTURE.md v0.1, baris D-04
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - 'D-04: Setuju.'
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-2 (atas ORCHESTRATION_ARCHITECTURE.md v0.1)
  scope: Struktur memory 7 berkas tanpa CHANGELOG dan AGENT_LOG
```

## D-05

```yaml
id: D-05
decision: Root CONTEXT_TRANSFER.md dibiarkan dan ditandai SUPERSEDED di memory
class: L4
status: APPROVED
date: '2026-11-05'
approval_evidence:
  question: Register keputusan §19 docs/ORCHESTRATION_ARCHITECTURE.md v0.1, baris D-05
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - 'D-05: Pilih opsi (a), root CONTEXT_TRANSFER dibiarkan dan ditandai SUPERSEDED di memory.'
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-2 (atas ORCHESTRATION_ARCHITECTURE.md v0.1)
  scope: Root CONTEXT_TRANSFER.md dibiarkan dan ditandai SUPERSEDED di memory
```

## D-06

```yaml
id: D-06
decision: Maksimal dua siklus revisi otomatis
class: L4
status: APPROVED
date: '2026-11-05'
approval_evidence:
  question: Register keputusan §19 docs/ORCHESTRATION_ARCHITECTURE.md v0.1, baris D-06
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - 'D-06: Setuju, maksimal dua siklus revisi otomatis.'
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-2 (atas ORCHESTRATION_ARCHITECTURE.md v0.1)
  scope: Maksimal dua siklus revisi otomatis
```

## D-07

```yaml
id: D-07
decision: Model per agent sesuai AGENT_SPECIFICATIONS.md §2.1, dievaluasi ulang setelah dipakai
class: L4
status: APPROVED (bersyarat evaluasi)
date: '2026-11-05'
approval_evidence:
  question: Register keputusan §19 docs/ORCHESTRATION_ARCHITECTURE.md v0.1, baris D-07
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - 'D-07: Setuju bersyarat, evaluasi kembali penggunaan model setelah sistem digunakan.'
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-2 (atas ORCHESTRATION_ARCHITECTURE.md v0.1)
  scope: Model per agent sesuai AGENT_SPECIFICATIONS.md §2.1, dievaluasi ulang setelah dipakai
```

## D-08

```yaml
id: D-08
decision: Auto memory hanya untuk preferensi umum, bukan fakta, data, atau keputusan proyek
class: L4
status: APPROVED
date: '2026-11-05'
approval_evidence:
  question: Register keputusan §19 docs/ORCHESTRATION_ARCHITECTURE.md v0.1, baris D-08
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - 'D-08: Pilih opsi (a). Auto memory hanya untuk preferensi umum, bukan fakta, data, atau keputusan proyek.'
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-2 (atas ORCHESTRATION_ARCHITECTURE.md v0.1)
  scope: Auto memory hanya untuk preferensi umum, bukan fakta, data, atau keputusan proyek
```

## D-09

```yaml
id: D-09
decision: Pemangkasan CLAUDE.md proyek dan pemindahan ke .claude/rules/
class: L4
status: DEFERRED
date: '2026-11-05'
approval_evidence:
  question: Register keputusan §19 docs/ORCHESTRATION_ARCHITECTURE.md v0.1, baris D-09
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - 'D-09: DEFERRED sampai pekerjaan Bab I selesai.'
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-2 (atas ORCHESTRATION_ARCHITECTURE.md v0.1)
  scope: Pemangkasan CLAUDE.md proyek dan pemindahan ke .claude/rules/
```

## D-10

```yaml
id: D-10
decision: Agent dilarang mengakses RSIA-source/
class: L4
status: SUPERSEDED by D-17
date: '2026-11-05'
approval_evidence:
  question: Register keputusan §19 docs/ORCHESTRATION_ARCHITECTURE.md v0.1, baris D-10
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - 'D-10: Pilih opsi (a), deny total akses agent ke RSIA-source.'
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-2 (atas ORCHESTRATION_ARCHITECTURE.md v0.1)
  scope: Agent dilarang mengakses RSIA-source/
```

## D-11

```yaml
id: D-11
decision: Penyelarasan tidak di-commit sebelum diperiksa; angka PDF Breakdown dibahas tim sebelum dipakai atau dibagikan
class: L3
status: APPROVED
date: '2026-11-05'
approval_evidence:
  question: Register keputusan §19 docs/ORCHESTRATION_ARCHITECTURE.md v0.1, baris D-11
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - 'D-11: Pilih opsi (b). Penyelarasan tidak boleh di-commit sebelum diperiksa. PDF Breakdown dibahas dengan tim sebelum angka di dalamnya digunakan atau dibagikan lebih lanjut.'
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-2 (atas ORCHESTRATION_ARCHITECTURE.md v0.1)
  scope: Penyelarasan tidak di-commit sebelum diperiksa; angka PDF Breakdown dibahas tim sebelum dipakai atau dibagikan
```

## D-12

```yaml
id: D-12
decision: Git pre-commit hook lokal (core.hooksPath --local); syarat pemeriksaan hook lama sudah dipenuhi
class: L4
status: APPROVED (bersyarat; syarat diperiksa)
date: '2026-11-05'
approval_evidence:
  question: Register keputusan §19 docs/ORCHESTRATION_ARCHITECTURE.md v0.1, baris D-12
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - 'D-12: Setuju bersyarat. Periksa core.hooksPath yang sudah ada dan pastikan konfigurasi dapat dikembalikan tanpa mengganggu hook lain.'
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-2 (atas ORCHESTRATION_ARCHITECTURE.md v0.1)
  scope: Git pre-commit hook lokal (core.hooksPath --local); syarat pemeriksaan hook lama sudah dipenuhi
```

## D-13

```yaml
id: D-13
decision: Branch setup/orchestration di Git worktree terpisah dari commit bersih
class: L4
status: APPROVED
date: '2026-11-05'
approval_evidence:
  question: Register keputusan §19 docs/ORCHESTRATION_ARCHITECTURE.md v0.1, baris D-13
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - 'D-13: Setuju, tetapi gunakan mekanisme branch/worktree yang benar-benar mengisolasi perubahan setup dari working tree pekerjaan proposal.'
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-2 (atas ORCHESTRATION_ARCHITECTURE.md v0.1)
  scope: Branch setup/orchestration di Git worktree terpisah dari commit bersih
```

## D-14

```yaml
id: D-14
decision: Dokumen sistem digabung (tanpa WORKFLOW/MEMORY_ARCHITECTURE/PERMISSION_POLICY/SKILLS_INTEGRATION terpisah)
class: L4
status: APPROVED
date: '2026-11-05'
approval_evidence:
  question: Register keputusan §19 docs/ORCHESTRATION_ARCHITECTURE.md v0.1, baris D-14
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - 'D-14: Setuju.'
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-2 (atas ORCHESTRATION_ARCHITECTURE.md v0.1)
  scope: Dokumen sistem digabung (tanpa WORKFLOW/MEMORY_ARCHITECTURE/PERMISSION_POLICY/SKILLS_INTEGRATION terpisah)
```

## D-15

```yaml
id: D-15
decision: Skill eksternal opsional dan diperiksa sebelum mapping final
class: L4
status: APPROVED
date: '2026-11-05'
approval_evidence:
  question: Register keputusan §19 docs/ORCHESTRATION_ARCHITECTURE.md v0.1, baris D-15
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - 'D-15: Setuju. Skill eksternal tetap opsional dan harus diperiksa sebelum mapping final.'
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-2 (atas ORCHESTRATION_ARCHITECTURE.md v0.1)
  scope: Skill eksternal opsional dan diperiksa sebelum mapping final
```

## D-16

```yaml
id: D-16
decision: Perbaikan ROOT tools/verify_claims.py ditunda; tidak ada commit atas berkas sensitif atau belum disetujui
class: L4
status: DEFERRED
date: '2026-11-05'
approval_evidence:
  question: Register keputusan §19 docs/ORCHESTRATION_ARCHITECTURE.md v0.1, baris D-16
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - 'D-16: Tunda sampai perubahan pengguna diamankan. Jangan melakukan commit terhadap file sensitif atau file yang belum disetujui.'
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-2 (atas ORCHESTRATION_ARCHITECTURE.md v0.1)
  scope: Perbaikan ROOT tools/verify_claims.py ditunda; tidak ada commit atas berkas sensitif atau belum disetujui
```

## D-17

```yaml
id: D-17
decision: Agent boleh membaca dan memakai RSIA-source/ sesuai kebutuhan dan Task Brief; berkas asli tidak diubah; turunan di .scratch/rsia/; tanpa pengenal di keluaran; tidak pernah di-stage; data tidak dipindah/dienkripsi
class: L3
status: APPROVED (menggantikan D-10)
date: '2026-11-05'
approval_evidence:
  question: Register keputusan docs/ORCHESTRATION_ARCHITECTURE.md v0.3 §19 dan docs/AGENT_SPECIFICATIONS.md v0.1 §7, baris D-17
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - Saya memutuskan bahwa agent **DIIZINKAN membaca dan menggunakan data di `RSIA-source/`** karena data tersebut memang diperlukan untuk mendukung analisis dan penyusunan proposal.
  - Saya menerima risiko bahwa agent dapat membaca data tersebut selama bekerja dalam repository ini.
  - Jangan memindahkan, mengenkripsi, menghapus, atau mengubah lokasi data RSIA.
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-3 (atas ORCHESTRATION_ARCHITECTURE.md v0.3 dan AGENT_SPECIFICATIONS.md v0.1)
  scope: Agent boleh membaca dan memakai RSIA-source/ sesuai kebutuhan dan Task Brief; berkas asli tidak diubah; turunan di .scratch/rsia/; tanpa pengenal di keluaran; tidak pernah di-stage; data tidak dipindah/dienkripsi
```

## D-18

```yaml
id: D-18
decision: Satu repository utama; worktree setup di luar OneDrive dari 7d59b85, branch setup/orchestration; merge tahap terpisah
class: L4
status: APPROVED
date: '2026-11-05'
approval_evidence:
  question: Register keputusan docs/ORCHESTRATION_ARCHITECTURE.md v0.3 §19 dan docs/AGENT_SPECIFICATIONS.md v0.1 §7, baris D-18
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - Saya menginginkan **satu repository utama untuk seluruh proyek IF4091 Penyusunan Proposal**.
  - 'Untuk Git worktree setup, saya menyetujui lokasi berikut:'
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-3 (atas ORCHESTRATION_ARCHITECTURE.md v0.3 dan AGENT_SPECIFICATIONS.md v0.1)
  scope: Satu repository utama; worktree setup di luar OneDrive dari 7d59b85, branch setup/orchestration; merge tahap terpisah
```

## P2-01

```yaml
id: P2-01
decision: Web A02/A08 hanya untuk metadata/bibliografi; mati secara bawaan; diaktifkan eksplisit per tugas; bukan izin menambah referensi
class: L4
status: APPROVED
date: '2026-11-05'
approval_evidence:
  question: Register keputusan docs/ORCHESTRATION_ARCHITECTURE.md v0.3 §19 dan docs/AGENT_SPECIFICATIONS.md v0.1 §7, baris P2-01
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - Setujui penelusuran web hanya untuk verifikasi metadata dan informasi bibliografi.
  - Nonaktif secara default.
  - Harus diaktifkan secara eksplisit melalui Task Brief dan izin saya untuk tugas terkait.
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-3 (atas ORCHESTRATION_ARCHITECTURE.md v0.3 dan AGENT_SPECIFICATIONS.md v0.1)
  scope: Web A02/A08 hanya untuk metadata/bibliografi; mati secara bawaan; diaktifkan eksplisit per tugas; bukan izin menambah referensi
```

## P2-02

```yaml
id: P2-02
decision: Hanya tools/build_modular.py dengan persetujuan per eksekusi; build_docx.py dan build_with_toc.py dilarang
class: L4
status: APPROVED
date: '2026-11-05'
approval_evidence:
  question: Register keputusan docs/ORCHESTRATION_ARCHITECTURE.md v0.3 §19 dan docs/AGENT_SPECIFICATIONS.md v0.1 §7, baris P2-02
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - Setujui hanya penggunaan `tools/build_modular.py`.
  - Setiap eksekusi wajib meminta persetujuan saya.
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-3 (atas ORCHESTRATION_ARCHITECTURE.md v0.3 dan AGENT_SPECIFICATIONS.md v0.1)
  scope: Hanya tools/build_modular.py dengan persetujuan per eksekusi; build_docx.py dan build_with_toc.py dilarang
```

## P2-03

```yaml
id: P2-03
decision: material/ hanya untuk A10 bila diperlukan
class: L4
status: APPROVED
date: '2026-11-05'
approval_evidence:
  question: Register keputusan docs/ORCHESTRATION_ARCHITECTURE.md v0.3 §19 dan docs/AGENT_SPECIFICATIONS.md v0.1 §7, baris P2-03
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - Setujui akses hanya untuk A10 (QA Structure) jika diperlukan untuk memeriksa struktur, format, atau kepatuhan terhadap materi/pedoman.
  - Agent lain tidak memperoleh akses otomatis.
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-3 (atas ORCHESTRATION_ARCHITECTURE.md v0.3 dan AGENT_SPECIFICATIONS.md v0.1)
  scope: material/ hanya untuk A10 bila diperlukan
```

## P2-04

```yaml
id: P2-04
decision: 'Supervisor: satu pertanyaan per giliran, antrean maksimal tiga per sesi wawancara, tanpa recommended answer'
class: L4
status: APPROVED
date: '2026-11-05'
approval_evidence:
  question: Register keputusan docs/ORCHESTRATION_ARCHITECTURE.md v0.3 §19 dan docs/AGENT_SPECIFICATIONS.md v0.1 §7, baris P2-04
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - Setujui satu pertanyaan per giliran kepada saya.
  - Maksimal tiga pertanyaan dalam antrean untuk satu sesi wawancara.
  - Jangan memberikan recommended answer yang seolah-olah menjadi keputusan saya.
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-3 (atas ORCHESTRATION_ARCHITECTURE.md v0.3 dan AGENT_SPECIFICATIONS.md v0.1)
  scope: 'Supervisor: satu pertanyaan per giliran, antrean maksimal tiga per sesi wawancara, tanpa recommended answer'
```

## P2-05

```yaml
id: P2-05
decision: A05 hanya untuk klaim utama baru/berubah atau atas permintaan eksplisit
class: L4
status: APPROVED
date: '2026-11-05'
approval_evidence:
  question: Register keputusan docs/ORCHESTRATION_ARCHITECTURE.md v0.3 §19 dan docs/AGENT_SPECIFICATIONS.md v0.1 §7, baris P2-05
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - Setujui A05 dipanggil hanya ketika terdapat klaim utama baru atau berubah.
  - A05 tetap dapat dipanggil jika saya secara eksplisit meminta kritik adversarial.
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-3 (atas ORCHESTRATION_ARCHITECTURE.md v0.3 dan AGENT_SPECIFICATIONS.md v0.1)
  scope: A05 hanya untuk klaim utama baru/berubah atau atas permintaan eksplisit
```

## P2-06

```yaml
id: P2-06
decision: Nilai awal effort/maxTurns sesuai §2.1; tidak dinaikkan otomatis
class: L4
status: APPROVED
date: '2026-11-05'
approval_evidence:
  question: Register keputusan docs/ORCHESTRATION_ARCHITECTURE.md v0.3 §19 dan docs/AGENT_SPECIFICATIONS.md v0.1 §7, baris P2-06
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - Setujui nilai awal berdasarkan tabel `docs/AGENT_SPECIFICATIONS.md` §2.1.
  - Jangan menaikkan batas secara otomatis tanpa alasan dan evaluasi.
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-3 (atas ORCHESTRATION_ARCHITECTURE.md v0.3 dan AGENT_SPECIFICATIONS.md v0.1)
  scope: Nilai awal effort/maxTurns sesuai §2.1; tidak dinaikkan otomatis
```

## D-19

```yaml
id: D-19
decision: 'Penyelesaian C-1: angka di PDF Breakdown menunggu pembahasan tim; angka independen dari data RSIA boleh dilaporkan dalam agregat, tetapi bila sama dengan angka PDF Breakdown atau Penyelarasan belum masuk naskah sampai dibahas tim; angka agregat lain melalui G1'
class: L3
status: APPROVED
date: '2026-11-05'
approval_evidence:
  question: Klarifikasi C-1, docs/ORCHESTRATION_ARCHITECTURE.md v0.4 Lampiran A
  options_offered: lihat dokumen pada session_ref
  user_answer:
  - 1. Angka yang memang tercantum dalam PDF Breakdown. Tetap menunggu pembahasan tim sebelum digunakan atau dibagikan, sesuai D-11.
  - 2. Angka yang dihitung secara independen dari data RSIA. Boleh dianalisis dan dilaporkan kepada Anda dalam bentuk agregat. Namun, jika hasilnya sama dengan angka dalam PDF Breakdown atau dokumen Penyelarasan, saya menyarankan angka tersebut belum dimasukkan ke naskah sampai dibahas dengan tim. Penggunaan angka agregat lainnya tetap melalui G1 sesuai R-8.
  - Jadi saya setujuin dan lanjut ke fase berikutnya
  answered_at: '2026-11-05'
  session_ref: Sesi Claude Code 2026-11-05, pesan tinjauan pengguna ke-4 (klarifikasi C-1 atas v0.4)
  scope: 'Penyelesaian C-1: angka di PDF Breakdown menunggu pembahasan tim; angka independen dari data RSIA boleh dilaporkan dalam agregat, tetapi bila sama dengan angka PDF Breakdown atau Penyelarasan belum masuk naskah sampai dibahas tim; angka agregat lain melalui G1'
```

## D-20

```yaml
id: D-20
decision: 'Perluas allowlist Bash secara sempit: a13 + git ls-tree dan git hash-object (read-only); a12 + mkdir/cp terbatas ke .scratch/**; perbaiki injeksi placeholder <SKILL_DIR:...> di prompt a12. Diimplementasikan di sesi setup (bukan agent), lalu T-19 dan init_reconcile diulang; selftest diberi kasus baru.'
class: L3
status: APPROVED
date: '2026-11-05'
related: [D-08, P2-02]
basis: 'Uji runtime TSK-005: F-A12-0001 (MEDIUM, placeholder tidak terisi), F-A12-0002 (find ditolak), F-A12-0003 (mkdir ditolak); a13 TSK-012 PARTIAL karena git ls-tree / python -c ditolak guard.'
alternatives_considered: ['Tanpa perluasan (A01 memberi path absolut, .scratch/ disiapkan pihak lain)', 'Tunda sampai setelah merge']
consequences: 'Permukaan Bash a12/a13 bertambah sedikit; selftest perlu kasus baru; T-19 tetap BLOCKED sampai implementasi.'
approval_evidence:
  question: 'Uji runtime menemukan allowlist Bash yang memblokir tugas sah. Contohnya, a13 tidak dapat menjalankan `git ls-tree` untuk init_reconcile; a12 tidak dapat menjalankan `find`, `mkdir`, atau `cp` untuk .scratch/; dan placeholder <SKILL_DIR:...> tidak terisi di prompt a12. Bagaimana menanganinya?'
  options_offered: ['Perluas sempit (Rekomendasi)', 'Tanpa perluasan', 'Tunda']
  user_answer: 'Perluas sempit (Rekomendasi)'
  answered_at: '2026-11-05'
  session_ref: 'Sesi Claude Code 2026-11-05, AskUserQuestion (channel); rujukan pesan tidak diberikan dalam brief TSK-013'
  scope: 'Perluasan sempit allowlist Bash a12/a13 dan perbaikan placeholder <SKILL_DIR:...> sebagaimana pada decision; bukan perluasan lain'
```
