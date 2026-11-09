---
file: DECISION_LOG
revision: 36
status: CURRENT
updated: 2026-11-09
updated_by: a13-memory-manager
based_on_commit: c056d20
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
catatan_rujukan: '[Ditambahkan A13 2026-11-07; teks dan status D-16 di atas tidak diubah] D-35 dan Q-B1-am menyebut D-16 sebagai perbaikan skrip build lama; teks asli D-16 hanya menyebut tools/verify_claims.py. Pilihan A01 atas delegasi pengguna D-44 (build_docx.py dan build_with_toc.py tidak diperbaiki, tetap dilarang) merujuk D-16 hanya sebatas catatan ini. Perbedaan cakupan dilaporkan ke A01 sebagai konflik, tidak diselesaikan.'
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

## D-21

```yaml
id: D-21
decision: 'Cakupan perawatan Bab I individu Danendra (K5): rawat inap dan rawat jalan terbatas, sesuai keputusan tim 30 Oktober 2026'
class: L3
status: APPROVED
date: '2026-11-06'
related: [D-19, K5]
basis: 'K5 (konflik CONTEXT_TRANSFER vs Penyelarasan, docs/ORCHESTRATION_ARCHITECTURE.md Lampiran A); P1 antrean wawancara a04 TSK-018'
alternatives_considered: ['Rawat inap saja']
consequences: 'Tindak lanjut TERBUKA (tidak ada naskah diubah): (1) pembuka Bab II (bab2/Bab_II_Revisi_Notulensi.md:15, "klaim rawat inap") dan II.1 "Rekam Medis Rawat Inap" perlu diselaraskan; (2) bentuk dokumen rawat jalan di RSIA belum dipastikan (Q-TEAM butir 4); (3) dasar kuantitatif tertahan D-19. Keputusan ini tidak menyentuh angka, ambang, atau cakupan lain.'
approval_evidence:
  question: 'Cakupan perawatan (K5): Apakah Bab I Anda mencakup rawat inap saja, atau rawat inap dan rawat jalan terbatas seperti keputusan tim 30 Oktober?'
  options_offered: ['Rawat inap dan rawat jalan terbatas', 'Rawat inap saja']
  user_answer: 'Rawat inap dan rawat jalan terbatas'
  answered_at: '2026-11-06'
  session_ref: 'sesi /sesi-mulai 2026-11-06, AskUserQuestion Cakupan (P1 antrean a04 TSK-018)'
  scope: 'Cakupan perawatan Bab I individu: rawat inap dan rawat jalan terbatas'
```

## D-22

```yaml
id: D-22
decision: 'Pembanding kombinasi pada rumusan masalah 1 Bab I individu Danendra (P2): kombinasi rule-based dan AI/NLP dibandingkan dengan tiap komponen sendiri-sendiri (rule-based saja dan AI/NLP saja) pada data dan label yang sama'
class: L3
status: APPROVED
date: '2026-11-06'
related: [D-19, D-21, F-A04-0003]
basis: 'P2 antrean wawancara a04 TSK-018; F-A04-0003 (rumusan 1 menguji kombinasi tanpa pembanding)'
alternatives_considered: ['Pemeriksaan manual koder', 'Tanpa pembanding, hanya ambang']
consequences: 'Keputusan ini tidak menetapkan metrik, ambang, angka, atau metodologi rinci. Konsekuensi: (1) diperlukan label tenaga ahli per jenis ketidaksesuaian dan rancangan uji di metodologi; (2) Penyelarasan Pemahaman Capstone.md:35 saat ini tanpa pembanding sehingga perlu diselaraskan dengan tim (dampak lintas proposal, belum dikonfirmasi tim). Naskah belum diubah.'
approval_evidence:
  question: 'Pembanding untuk "kombinasi" (rumusan masalah 1): Kalau rumusan Anda menyebut kombinasi rule-based dan AI/NLP, dengan apa kombinasi itu dibandingkan?'
  options_offered: ['Tiap komponen sendiri-sendiri', 'Pemeriksaan manual koder', 'Tanpa pembanding, hanya ambang']
  user_answer: 'Tiap komponen sendiri-sendiri'
  answered_at: '2026-11-06'
  session_ref: 'sesi /sesi-mulai 2026-11-06, AskUserQuestion Pembanding (P2 antrean a04 TSK-018)'
  scope: 'Pembanding kombinasi rule-based dan AI/NLP pada rumusan masalah 1 Bab I individu: tiap komponen sendiri-sendiri'
```

## D-23

```yaml
id: D-23
decision: 'Dasar bukti kerugian dan premis penghubung pada latar belakang Bab I individu Danendra (P3): hubungan antara ketidaksesuaian CPPT-resume dan kerugian ditunjukkan dari wawancara pihak RSIA (keterangan kualitatif narasumber). Klaim dibatasi pada apa yang dinyatakan narasumber'
class: L3
status: SUPERSEDED by D-24
date: '2026-11-06'
superseded_scope: 'Sebagian: hanya bagian sumber ("wawancara pihak RSIA") dan atribusinya, digantikan D-24. Pembatasan klaim (tanpa klaim penurunan pending/percepatan koder, angka tertahan D-19) tetap berlaku dan diteruskan D-24'
related: [D-19, D-21, D-22, F-A04-0006]
basis: 'P3 antrean wawancara a04 TSK-018; F-A04-0006 (premis tersembunyi bahwa ketidaksesuaian CPPT-resume menyebabkan pending)'
alternatives_considered: ['Dari data/alasan pending RSIA', 'Asumsi kerja yang ditandai']
consequences: 'Keputusan ini tidak membolehkan klaim penurunan pending atau percepatan kerja koder (Penyelarasan Pemahaman Capstone.md:98); angka tetap tertahan D-19. Tindak lanjut TERBUKA: (1) belum dikonfirmasi apakah isi kualitatif wawancara boleh diparafrasakan di naskah (Q-A04-e); (2) narasumber dan lokasi catatan wawancara belum diidentifikasi; (3) premis tetap ditulis eksplisit dengan status buktinya (CLAUDE.md sec. 8 no. 8). Naskah belum diubah.'
approval_evidence:
  question: 'Siapa yang dirugikan dan premis penghubungnya: Kerugian apa yang Anda tunjukkan di latar belakang, dan bukti apa yang menghubungkan ketidaksesuaian CPPT-resume dengan kerugian itu?'
  options_offered: ['Dari data/alasan pending RSIA', 'Dari wawancara pihak RSIA', 'Asumsi kerja yang ditandai']
  user_answer: 'Dari wawancara pihak RSIA'
  answered_at: '2026-11-06'
  session_ref: 'sesi /sesi-mulai 2026-11-06, AskUserQuestion Premis (P3 antrean a04 TSK-018)'
  scope: 'Dasar bukti kerugian dan premis penghubung pada latar belakang Bab I individu: wawancara pihak RSIA'
```

## D-24

```yaml
id: D-24
decision: 'Sumber dan atribusi keterangan kerugian pada latar belakang Bab I individu Danendra: bersandar pada dokumen Penyelarasan Pemahaman Capstone.md (keputusan tim), dengan atribusi ke dokumen itu, bukan wawancara langsung. Menggantikan sebagian D-23 (bagian sumber wawancara)'
class: L3
status: APPROVED
date: '2026-11-06'
supersedes_partially: D-23
related: [D-17, D-19, D-21, D-22, D-23, Q-A04-e, F-A04-0006]
basis: 'Lanjutan P3 antrean wawancara a04 TSK-018; pengguna menyatakan konteks: klien mengajukan topik ke salah satu anggota tim, lalu anggota itu mengajak pengguna untuk capstone (konteks, bukan keputusan; identitas anggota tidak dicatat)'
alternatives_considered: ['Wawancara, boleh diparafrasakan tanpa angka', 'Belum, bahas dulu dengan tim']
consequences: 'Klaim dibatasi pada isi Penyelarasan Pemahaman Capstone.md; angka tetap tertahan D-19; tidak ada klaim penurunan pending atau percepatan kerja koder (Penyelarasan:98); pengenal kunjungan/pasien dari Penyelarasan tidak boleh masuk naskah (D-17 R-4). Isi wawancara langsung tidak dipakai kecuali lewat Penyelarasan. Premis tetap ditulis eksplisit dengan status buktinya. Naskah belum diubah.'
approval_evidence:
  question: 'Dari mana keterangan tentang kerugian di latar belakang Bab I boleh diambil, dan dengan atribusi apa?'
  options_offered: ['Wawancara, boleh diparafrasakan tanpa angka', 'Lewat Penyelarasan tim saja', 'Belum, bahas dulu dengan tim']
  user_answer: 'Lewat Penyelarasan tim saja (pilihan ini menyebut bahwa D-23 ''kerugian dari wawancara'' perlu disesuaikan; didahului pernyataan pengguna: ''Jadi intinya client mengajukan ke salah satu anggota kami, lalu anggota tersebut mengajak saya untuk capstone proposal tugas akhir'')'
  answered_at: '2026-11-06'
  session_ref: 'sesi /sesi-mulai 2026-11-06, AskUserQuestion Sumber (lanjutan P3, antrean a04 TSK-018)'
  scope: 'Sumber dan atribusi keterangan kerugian pada latar belakang Bab I individu: Penyelarasan tim'
```

## D-25

```yaml
id: D-25
decision: 'Lingkup kajian individu Bab I (I.4) hanya CPPT lawan resume dalam satu episode; konsistensi antar-entri CPPT dan penautan ibu-bayi berada di luar kajian individu'
class: L3
status: APPROVED
date: '2026-11-06'
related: [D-19, D-21, F-A07-0004, F-A07-0005]
basis: 'Jawaban pengguna atas pertanyaan lingkup I.4 pada sesi 2026-11-06'
alternatives_considered: ['Antar-CPPT masuk, ibu-bayi di luar', 'Ibu-bayi masuk terbatas, antar-CPPT di luar', 'Keduanya masuk']
consequences: 'Penautan ibu-bayi tetap bagian tim (Penyelarasan:43); pemiliknya perlu dipastikan agar tidak ada celah antarproposal (tindak lanjut A06/A01). Naskah belum diubah.'
approval_evidence:
  question: 'Ruang lingkup I.4 (F-A07-0004, F-A07-0005): Apakah konsistensi antar-entri CPPT dan penautan ibu–bayi termasuk dalam kajian individu Anda, atau hanya dalam capstone?'
  options_offered: ['Keduanya di luar kajian individu', 'Antar-CPPT masuk, ibu–bayi di luar', 'Ibu–bayi masuk terbatas, antar-CPPT di luar', 'Keduanya masuk']
  user_answer: 'Keduanya di luar kajian individu'
  answered_at: '2026-11-06'
  session_ref: 'sesi /sesi-mulai 2026-11-06, AskUserQuestion Lingkup I.4'
  scope: 'Lingkup kajian individu Bab I: hanya CPPT lawan resume dalam satu episode'
```

## D-26

```yaml
id: D-26
decision: 'Subbab I.6 Sistematika Penulisan dihapus dari Bab I individu (mengikuti templat Individu I.1-I.5)'
class: L3
status: APPROVED
date: '2026-11-06'
related: [F-A10-0001, F-A10-0002]
basis: 'Jawaban pengguna atas pertanyaan nasib I.6 pada sesi 2026-11-06'
alternatives_considered: ['Pertahankan, konfirmasi pembimbing']
consequences: 'Kriteria CLAUDE.md soal sistematika tidak terpenuhi; kalimat risiko Bab IV yang berada di I.6 hilang. Naskah belum diubah.'
approval_evidence:
  question: 'Nasib I.6 Sistematika Penulisan (F-A10-0001, F-A10-0002): Templat Individu hanya punya I.1–I.5 dan tidak mengatur sistematika. Apakah I.6 dipertahankan atau dihapus?'
  options_offered: ['Hapus I.6', 'Pertahankan, konfirmasi pembimbing']
  user_answer: 'Hapus I.6'
  answered_at: '2026-11-06'
  session_ref: 'sesi /sesi-mulai 2026-11-06, AskUserQuestion I.6'
  scope: 'Struktur Bab I individu: tanpa subbab I.6'
```

## D-27

```yaml
id: D-27
decision: 'Atribusi kondisi RSIA di I.1 Bab I individu ke dokumen Penyelarasan saja, tanpa menyebut wawancara. Dicatat sebagai entri tersendiri karena memperjelas bentuk atribusi di I.1; selaras dengan D-24, tidak menggantikannya'
class: L3
status: APPROVED
date: '2026-11-06'
related: [D-17, D-19, D-24, F-A07-0010]
basis: 'Jawaban pengguna atas pertanyaan atribusi I.1 pada sesi 2026-11-06'
alternatives_considered: ['Boleh, sebut sebagai catatan wawancara']
consequences: 'Naskah tidak boleh menyebut bahwa dokumen tim merekam wawancara; atribusi hanya ke dokumen Penyelarasan. Naskah belum diubah.'
approval_evidence:
  question: 'Atribusi di I.1 (F-A07-0010): Dokumen Penyelarasan mencatat kondisi RSIA berdasarkan wawancara Direktur RSIA (September 2026). Bolehkah naskah menyebut bahwa dokumen tim itu merekam suatu wawancara?'
  options_offered: ['Boleh, sebut sebagai catatan wawancara', 'Tidak, atribusi ke dokumen saja']
  user_answer: 'Tidak, atribusi ke dokumen saja'
  answered_at: '2026-11-06'
  session_ref: 'sesi /sesi-mulai 2026-11-06, AskUserQuestion Atribusi'
  scope: 'Bentuk atribusi kondisi RSIA di I.1: dokumen Penyelarasan saja'
```

## D-28

```yaml
id: D-28
decision: 'Rumusan masalah individual Bab I (I.2) Danendra terdiri atas rumusan 1 capstone (pembentukan temuan; presisi dan recall) dan bagian rumusan 4 capstone yang menjadi bagiannya (kejelasan alasan dan rujukan temuan), sesuai Penyelarasan Pemahaman Capstone.md:176'
class: L3
status: APPROVED
date: '2026-11-06'
related: [D-19, D-21, D-22, D-25, Q-A04-b, F-A04-0004]
basis: 'Jawaban pengguna atas pertanyaan komposisi rumusan I.2 pada sesi 2026-11-06'
alternatives_considered: ['Hanya rumusan 1', 'Tunda I.2, bahas dengan tim dulu']
consequences: 'Tidak menetapkan angka ambang (D-19; Q-TEAM butir 8), satuan presisi/recall (Q-A04-d), atau jumlah kasus (Q-A04-c). Konsekuensi: I.3, I.5, dan paragraf research gap harus memuat ukuran kejelasan alasan dan rujukan; irisan dengan rumusan 4 Abizzar perlu diperiksa A06 (dampak lintas proposal, belum dikonfirmasi tim).'
approval_evidence:
  question: 'Untuk menulis I.2 (Rumusan Masalah), bagian mana dari rumusan capstone yang menjadi rumusan masalah individual Anda? Penyelarasan:176 menyebut Anda mengukur rumusan 1 serta bagian kejelasan alasan dan rujukan pada rumusan 4 (Q-A04-b masih terbuka). Pembanding sudah diputuskan di D-22; ambang tetap berupa "di atas ambang yang ditetapkan sebelum pengujian" tanpa angka (D-19, Q-TEAM butir 8).'
  options_offered: ['Rumusan 1 + bagian rumusan 4 (Recommended)', 'Hanya rumusan 1', 'Tunda I.2, bahas dengan tim dulu']
  user_answer: 'Rumusan 1 + bagian rumusan 4 (Recommended)'
  answered_at: '2026-11-06'
  session_ref: 'sesi /sesi-mulai 2026-11-06, AskUserQuestion Rumusan I.2'
  scope: 'Komposisi rumusan masalah individual I.2: rumusan 1 + bagian kejelasan alasan dan rujukan dari rumusan 4'
```

## D-29

```yaml
id: D-29
decision: 'Kriteria keunggulan kombinasi pada rumusan 1 Bab I individu (I.2): presisi dan recall kombinasi rule-based + AI/NLP sama-sama harus lebih tinggi daripada presisi dan recall masing-masing komponen (rule-based saja dan AI/NLP saja) pada data dan label yang sama; jawaban "tidak" bila salah satu metrik tidak lebih tinggi daripada salah satu komponen. Selisih minimum, ambang numerik, dan satuan hitung tetap belum ditetapkan'
class: L3
status: APPROVED
date: '2026-11-06'
related: [D-19, D-22, D-28, F-A07-0021, F-A09-0041]
basis: 'Jawaban pengguna atas pertanyaan kriteria keunggulan kombinasi pada sesi 2026-11-06'
alternatives_considered: ['Belum ditetapkan, netralkan teks', 'Recall lebih tinggi, presisi tidak turun di bawah ambang']
consequences: 'Penanda "kriteria keunggulan" di I.2 dihapus; selisih minimum tetap bermarker (Q-TEAM butir 8). Kriteria ketat sehingga kelayakannya perlu dinilai a11. Penyelarasan:35 belum memuat pembanding atau kriteria ini (dampak lintas proposal, belum dikonfirmasi tim; perlu a06). Tidak menetapkan metrik lain, ambang, angka. Naskah belum diubah.'
approval_evidence:
  question: 'a07 menilai I.2 FAIL (0 HIGH, 5 MEDIUM) karena rumusan 1 sudah memuat aturan "tidak" (kombinasi harus lebih tinggi daripada tiap komponen), sementara penanda di dekatnya mengatakan kriteria itu belum diputuskan (F-A07-0021). D-22 hanya menetapkan pembanding, bukan cara kombinasi dinyatakan lebih baik. Bagaimana kriteria keunggulan kombinasi atas rule-based saja dan AI/NLP saja ditetapkan?'
  options_offered: ['Presisi dan recall sama-sama lebih tinggi (Recommended)', 'Belum ditetapkan, netralkan teks', 'Recall lebih tinggi, presisi tidak turun di bawah ambang']
  user_answer: 'Presisi dan recall sama-sama lebih tinggi (Recommended)'
  answered_at: '2026-11-06'
  session_ref: 'sesi /sesi-mulai 2026-11-06, AskUserQuestion Kriteria Q1'
  scope: 'Kriteria keunggulan kombinasi atas tiap komponen pada rumusan 1 (I.2): presisi dan recall sama-sama lebih tinggi'
```

## D-30

```yaml
id: D-30
decision: 'Lingkup I.4 Bab I individu diselaraskan dengan rumusan 2 I.2: I.4 memuat satu paragraf bahwa kajian juga menilai kejelasan alasan dan rujukan temuan oleh tenaga ahli dan pengguna proksi, tanpa mencakup alur penilaian, skor SUS, atau tingkat penyelesaian tugas (bagian rumusan 4 milik Abizzar)'
class: L3
status: APPROVED
date: '2026-11-06'
related: [D-25, D-28, F-A07-0022]
basis: 'Jawaban pengguna atas pertanyaan lingkup I.4 pada sesi 2026-11-06'
alternatives_considered: ['Ubah klaim di I.2, I.4 tetap']
consequences: 'I.4 (yang sudah lolos QA siklus 2) berubah dan perlu QA ulang; siapa penilainya menunggu Q-TEAM butir 7; irisan dengan rumusan 4 Abizzar perlu dicek a06. Tidak menetapkan angka, ambang, atau skala penilaian. Naskah belum diubah saat keputusan dicatat.'
approval_evidence:
  question: 'Kedua QA menilai I.2 FAIL (a07: 5 MEDIUM; a09: 3 MEDIUM). Satu butir lagi perlu keputusan Anda (F-A07-0022): rumusan 2 I.2 mengukur kejelasan alasan dan rujukan temuan oleh tenaga ahli dan pengguna proksi, tetapi I.4 hanya menyebut sumber data CPPT dan resume medis, sedangkan I.2 mengklaim kedua pertanyaan berada dalam batas I.4. Bagaimana menyelaraskannya?'
  options_offered: ['Tambah satu paragraf di I.4 (Recommended)', 'Ubah klaim di I.2, I.4 tetap']
  user_answer: 'Tambah satu paragraf di I.4 (Recommended)'
  answered_at: '2026-11-06'
  session_ref: 'sesi /sesi-mulai 2026-11-06, AskUserQuestion Lingkup I.4'
  scope: 'Penambahan satu paragraf di I.4 tentang penilaian kejelasan alasan dan rujukan temuan oleh tenaga ahli dan pengguna proksi'
```

## D-31

```yaml
id: D-31
decision: 'Redaksi tujuan utama I.3 Bab I individu tetap berupa "mengevaluasi kombinasi pemeriksaan rule-based dan AI/NLP berbasis RAG dari dua sisi: ketepatan deteksi ketidaksesuaian CPPT-resume medis dalam satu episode, dan kejelasan alasan dan rujukan pada temuan", sepadan 1:1 dengan dua rumusan I.2; pengembangan komponen oleh penulis tidak dimasukkan ke tujuan'
class: L3
status: APPROVED
date: '2026-11-06'
related: [D-28, D-29, D-30, F-A10-0105]
basis: 'Jawaban pengguna atas pertanyaan redaksi tujuan utama I.3 pada sesi 2026-11-06'
alternatives_considered: ['Mengembangkan dan mengevaluasi']
consequences: 'Pengembangan aturan rule-based dan pemeriksaan AI/NLP berbasis RAG oleh penulis (Penyelarasan:55, :169) harus dijelaskan di paragraf research gap I.1 atau I.5 (Q-B1-n); kontribusi individual tidak tampak di tujuan. Tidak menetapkan angka, ambang, atau skala.'
approval_evidence:
  question: 'a03 sudah menulis I.3 (DRAF 7), sepadan dengan dua rumusan I.2 dan tanpa angka. Tujuan utamanya berbunyi: "Tujuan utama penelitian ini ialah mengevaluasi kombinasi pemeriksaan rule-based dan AI/NLP berbasis RAG dari dua sisi: ketepatannya dalam mendeteksi ketidaksesuaian antara CPPT dan resume medis dalam satu episode serta kejelasan alasan dan rujukan pada temuannya." Penyelarasan:55 dan :169 mencatat bahwa Anda menyusun aturan rule-based dan membangun pemeriksaan AI/NLP berbasis RAG, tetapi tujuan ini hanya menyebut "mengevaluasi". Bagaimana redaksi tujuan utamanya?'
  options_offered: ['Mengembangkan dan mengevaluasi (Recommended)', 'Mengevaluasi saja (teks sekarang)']
  user_answer: 'Mengevaluasi saja (teks sekarang)'
  answered_at: '2026-11-06'
  session_ref: 'sesi /sesi-mulai 2026-11-06, AskUserQuestion Tujuan I.3'
  scope: 'Redaksi tujuan utama I.3: mengevaluasi saja'
```

## D-32

```yaml
id: D-32
decision: 'Kriteria D-29 dipertahankan. Mekanisme kombinasi rule-based dan AI/NLP berbasis RAG belum ditetapkan dan ditandai di I.2 dan I.3 sebagai keputusan yang harus ditetapkan sebelum pengujian, dengan syarat mekanisme itu memungkinkan kedua arah hasil (kombinasi dapat lebih tinggi maupun tidak lebih tinggi daripada komponen). Dibawa ke tim sebagai butir terbuka, bersama titik ukur kombinasi terhadap rekonsiliasi antarpemeriksaan milik Abizzar'
class: L3
status: APPROVED
date: '2026-11-06'
related: [D-22, D-29, F-A05-0001, F-A05-0002, F-A11-0001, F-A11-0002, F-A11-0003]
basis: 'Jawaban pengguna atas pertanyaan kriteria D-29 pada sesi 2026-11-06'
alternatives_considered: ['Tinjau D-29: recall lebih tinggi, presisi tidak turun di bawah ambang', 'Tunda ke tim dan pembimbing']
consequences: 'Penanda baru di I.2 dan I.3 (jumlah penanda Bab I bertambah). Risiko jawaban "tidak" tak informatif karena aritmetika tetap terbuka sampai tim menetapkan mekanisme (union, irisan, penyaringan, atau pembentukan bertahap; menurut a11, irisan tidak pernah menaikkan recall dan union atas komponen dengan cakupan jenis terpisah tidak pernah menaikkan presisi di atas keduanya). D-29 tidak diubah. Perlu dicek A06 untuk dampak ke Abizzar (rekonsiliasi, Penyelarasan:183). Naskah belum diubah saat keputusan dicatat.'
approval_evidence:
  question: 'Dua auditor independen (a05 kritis, a11 teknis) sepakat bahwa kriteria D-29 (presisi dan recall kombinasi sama-sama lebih tinggi daripada tiap komponen) tidak layak diuji bila mekanisme kombinasi tidak ditetapkan. Naskah hanya menyebut "gabungan kedua komponen" (I.2 baris 83). Menurut a11, irisan tidak pernah dapat menaikkan recall di atas komponen, dan union atas komponen dengan cakupan jenis terpisah (Penyelarasan:69, :76) tidak pernah dapat menaikkan presisi di atas keduanya, sehingga jawaban "tidak" sudah pasti. Hanya penyaringan atas union atau irisan cakupan yang besar yang mungkin lolos. Mekanisme kombinasi belum ada di daftar tim, dan ini tidak menyatakan D-29 salah. Bagaimana menanganinya?'
  options_offered: ['Pertahankan D-29, tandai mekanismenya (Recommended)', 'Tinjau D-29: recall lebih tinggi, presisi tidak turun di bawah ambang', 'Tunda ke tim dan pembimbing']
  user_answer: 'Pertahankan D-29, tandai mekanismenya (Recommended)'
  answered_at: '2026-11-06'
  session_ref: 'sesi /sesi-mulai 2026-11-06, AskUserQuestion Kriteria D-29'
  scope: 'Mekanisme kombinasi dan status D-29: D-29 dipertahankan, mekanisme ditandai dan dibawa ke tim'
```

## D-33

```yaml
id: D-33
decision: 'Syarat keberhasilan I.3 Bab I individu dirumuskan sebagai hasil yang dituju = jawaban atas dua pertanyaan I.2 (bukan "tujuan tercapai/tidak tercapai"); tujuan tetap "mengevaluasi" (D-31 utuh). I.3 menyatakan kapan kombinasi pemeriksaan dinyatakan memenuhi atau tidak memenuhi syarat pada tiap sisi dengan merujuk I.2; jawaban "tidak" adalah hasil yang sah; tidak ada aturan status gabungan antarsisi'
class: L3
status: APPROVED
date: '2026-11-06'
related: [D-28, D-29, D-31, F-A07-0038, F-A10-0112, F-A05-0008]
basis: 'Jawaban pengguna atas pertanyaan rumusan syarat paragraf 2-3 I.3 pada sesi 2026-11-06'
alternatives_considered: ['Tujuan sebagai hasil yang dituju (menunjukkan kombinasi memenuhi kedua syarat)']
consequences: 'Kalimat "tujuan tercapai/tidak tercapai" dihapus dari I.3; kebutuhan templat "tercapai atau tidak" dipenuhi lewat jawaban pertanyaan. Tidak menetapkan angka, ambang, atau skala. D-31 dan D-29 tidak diubah.'
approval_evidence:
  question: 'Tiga auditor (a07, a10, a05) menemukan hal yang sama pada I.3: tujuan utama berbunyi "mengevaluasi" (D-31), tetapi paragraf 2-3 menyatakan "Tujuan tidak tercapai pada sisi itu bila jawaban pertanyaan ... ''tidak''". Akibatnya, jawaban "tidak" yang sah terbaca sebagai penelitian yang gagal, dan tidak ada aturan status tujuan bila hanya satu sisi terpenuhi. Redaksi "mengevaluasi" sendiri tidak dipersoalkan. Bagaimana syarat di paragraf 2-3 dirumuskan?'
  options_offered: ['Hasil = jawaban pertanyaan, bukan tercapai/tidak (Recommended)', 'Tujuan sebagai hasil yang dituju']
  user_answer: 'Hasil = jawaban pertanyaan, bukan tercapai/tidak (Recommended)'
  answered_at: '2026-11-06'
  session_ref: 'sesi /sesi-mulai 2026-11-06, AskUserQuestion Tujuan vs ukuran'
  scope: 'Rumusan syarat keberhasilan I.3: hasil = jawaban pertanyaan'
```

## D-34

```yaml
id: D-34
decision: 'I.5 Metodologi Bab I individu disusun tanpa kerangka metodologi bernama: tahapan khusus penelitian ini (masukan, kegiatan, keluaran), bersumber dari keputusan APPROVED dan bagian Data dan Evaluasi Penyelarasan, dengan pernyataan bahwa tidak ada kerangka baku yang diklaim diikuti; hal yang menunggu tim tetap berupa penanda'
class: L3
status: APPROVED
date: '2026-11-06'
related: [D-19, D-22, D-29, D-31, D-32, D-33]
basis: 'Jawaban pengguna atas pertanyaan kerangka I.5 pada sesi 2026-11-06 (lanjutan)'
alternatives_considered: ['Pengguna menyebutkan kerangka metodologi', 'Tunda I.5 sampai keputusan tim']
consequences: 'Pembimbing mungkin menuntut kerangka bernama; dapat ditambahkan kemudian. Tidak menetapkan mekanisme kombinasi, angka, ambang, atau satuan. Tidak memasukkan kajian pustaka sebagai tahap.'
approval_evidence:
  question: 'Sebelum menulis I.5 (Metodologi), perlu satu keputusan Anda: Penyelarasan tidak menyebut kerangka metodologi dan belum ada keputusan APPROVED soal itu. Penyelarasan hanya menetapkan prinsip evaluasi (label tenaga ahli buta terhadap keluaran sistem, pembagian data per pasien, pembandingan tiga konfigurasi, penilaian kejelasan oleh tenaga ahli dan pengguna proksi). Aturan proposal juga melarang sekadar menyebut nama kerangka tanpa menjelaskan penerapannya. Bagaimana I.5 disusun?'
  options_offered: ['Tanpa kerangka bernama (Recommended)', 'Saya sebutkan kerangkanya', 'Tunda I.5 sampai keputusan tim']
  user_answer: 'Tanpa kerangka bernama, tapi kan current session sudah 82%, Silahkan segera buat versi modularnya di C:\Users\HYPE R Series\worktrees\project-proposal-setup\modular\13523136-Proposal-IF4091-Capstone-Individu-2026-Modular-Bab-I_Editorial.docx (dan tiga berkas modular lain: Bab-I.docx, Bab-II_Editorial.docx, Bab-II.docx di folder yang sama)'
  answered_at: '2026-11-06'
  session_ref: 'sesi /sesi-mulai 2026-11-06 (lanjutan), AskUserQuestion Kerangka I.5'
  scope: 'Hanya bentuk I.5: tanpa kerangka bernama. Permintaan membuat versi modular dalam jawaban yang sama BUKAN bagian keputusan ini dan belum disetujui (menunggu Approval Request build_modular per P2-02)'
```

## D-35

```yaml
id: D-35
decision: 'Peran migrasi Markdown final ke Docs/DOCX (varian modular editorial, formal, dan lengkap) ditempatkan pada a03 dengan memperbaiki tools/build_modular.py agar mendukung tiga varian dan jalur Google Docs; tidak ada agent baru; a03 menjalankannya dengan persetujuan per eksekusi seperti sekarang (P2-02). Lingkup terbatas pada penempatan peran ini'
class: L3
status: APPROVED
date: '2026-11-07'
related: [D-16, Q-B1-ai, Q-B1-ah, Q-A04-a]
basis: 'Jawaban pengguna atas pertanyaan penempatan peran migrasi Markdown final ke Docs'
alternatives_considered: ['Agent ke-14 khusus', 'Skrip deterministik tanpa agent', 'Rancang dulu']
consequences: 'a03 menjadi penulis sekaligus penerbit. Keputusan ini TIDAK menetapkan: (a) siapa yang boleh mengedit tools/build_modular.py (a03 hanya berwenang menulis bab*/ dan .scratch/**), (b) definisi tiga varian dan format keluaran Google Docs, (c) perubahan AGENT_SPECIFICATIONS/ORCHESTRATION, hook guard dan check_agents, (d) nasib D-16. Semua itu terbuka (Q-B1-aj..am). Tidak memberi persetujuan build apa pun; P2-02 tetap berlaku (skrip build lama tetap dilarang). Perbaikan build_modular belum dilakukan saat keputusan dicatat. [Catatan rujukan 2026-11-07, ditambahkan A13: bagian jalur Google Docs pada keputusan ini dipersempit oleh D-38; teks keputusan asli tidak diubah.]'
approval_evidence:
  question: 'Bagaimana peran migrasi Markdown final ke Docs (versi modular editorial, formal, dan lengkap) ditempatkan di sistem agent?'
  options_offered: ['Perluas a03 + perbaiki build_modular', 'Agent ke-14 khusus', 'Skrip deterministik tanpa agent', 'Rancang dulu']
  user_answer: 'Perluas a03 + perbaiki build_modular'
  answered_at: '2026-11-07'
  session_ref: 'Brief A01 memory_op (pertanyaan penempatan peran migrasi); tanggal = hari pencatatan, tidak tercantum di brief'
  scope: 'Hanya penempatan peran migrasi: a03 diperluas dan build_modular.py diperbaiki untuk tiga varian dan jalur Google Docs; tidak ada agent baru; persetujuan per eksekusi (P2-02) tetap'
```

## D-36

```yaml
id: D-36
decision: 'a03 diberi wewenang edit khusus atas satu berkas, tools/build_modular.py, dengan persetujuan pengguna per perubahan dan audit hasil oleh a12. Lingkup terbatas pada siapa yang berwenang mengedit berkas itu'
class: L3
status: APPROVED
date: '2026-11-07'
related: [D-35, D-16, Q-B1-aj, Q-B1-al, Q-B1-an, P2-02]
basis: 'Jawaban pengguna atas pertanyaan Q-B1-aj (siapa mengedit tools/build_modular.py)'
alternatives_considered: ['Pengguna atau sesi terpisah di luar agent mengedit skrip', 'Tunda; putuskan definisi varian dulu']
consequences: 'Wewenang ini mensyaratkan perubahan AGENT_SPECIFICATIONS, hook guard, dan check_agents (konsekuensi wajib, dicatat di Q-B1-al) serta audit a12 atas hasil. Keputusan ini TIDAK menetapkan: (a) definisi tiga varian dan format Google Docs (Q-B1-ak tetap terbuka), (b) isi perubahan skrip, (c) nasib D-16 (Q-B1-am tetap terbuka), (d) pelaksanaan perubahan pada docs/, hook, dan konfigurasi agent, (e) jalur atau agent yang mengedit berkas-berkas itu (Q-B1-an terbuka). Sebelum perubahan tersebut dilaksanakan, a03 tetap TIDAK berwenang menulis di tools/. Tidak memberi persetujuan build apa pun; P2-02 tetap berlaku (skrip build lama tetap dilarang).'
approval_evidence:
  question: 'Siapa yang mengedit tools/build_modular.py untuk mendukung tiga varian (editorial, formal, lengkap) dan jalur Google Docs? a03 saat ini hanya berwenang menulis di bab1/–bab4/ dan .scratch/**, jadi tidak bisa mengedit skrip di tools/.'
  options_offered: ['Anda/sesi terpisah di luar agent', 'Beri a03 wewenang edit khusus tools/build_modular.py, dengan approval per perubahan, memerlukan perubahan AGENT_SPECIFICATIONS, hook guard, dan check_agents, serta a12 mengaudit hasilnya', 'Tunda, putuskan definisi varian dulu']
  user_answer: 'Beri a03 wewenang edit khusus tools/build_modular.py'
  answered_at: '2026-11-07'
  session_ref: 'Brief A01 memory_op R9 (pertanyaan Q-B1-aj), sesi 2026-11-07'
  scope: 'HANYA siapa yang berwenang mengedit tools/build_modular.py (a03, satu berkas itu). Tidak mencakup definisi tiga varian/format Google Docs (Q-B1-ak), isi perubahan skrip, nasib D-16 (Q-B1-am), maupun pelaksanaan perubahan pada docs/, hook, dan konfigurasi agent'
```

## D-37

```yaml
id: D-37
decision: 'Perubahan AGENT_SPECIFICATIONS, ORCHESTRATION_ARCHITECTURE, scripts/guard.py, scripts/check_agents.py, dan definisi agent a03 (konsekuensi wajib D-36) dikerjakan oleh pengguna atau sesi Claude Code biasa di luar agent. Lingkup terbatas pada jalur pelaksanaan perubahan itu'
class: L3
status: APPROVED
date: '2026-11-07'
related: [D-36, D-35, Q-B1-al, Q-B1-an, P2-02]
basis: 'Jawaban pengguna atas pertanyaan Q-B1-an (siapa mengerjakan perubahan spesifikasi/hook)'
alternatives_considered: ['Susun draf perubahan di .scratch/ untuk ditinjau dan diterapkan pengguna', 'Tunda sampai definisi varian jelas']
consequences: 'Q-B1-an ditutup (DIPUTUSKAN). Q-B1-al tetap TERBUKA sampai perubahan benar-benar diterapkan dan check_agents lolos; sebelum itu wewenang a03 menurut D-36 belum operasional dan a03 tetap TIDAK berwenang menulis di tools/. Daftar lokasi perubahan yang disampaikan A01 ke pengguna: AGENT_SPECIFICATIONS (tabel agent baris A03; blok write_scopes dan daftar skrip terlarang; tes T-26 dan T-29; P2-02), ORCHESTRATION_ARCHITECTURE (R5), scripts/guard.py, scripts/check_agents.py, .claude/agents/a03-academic-writer.md. Keputusan ini TIDAK menetapkan isi perubahan, tidak memberi persetujuan build apa pun, dan tidak mengubah D-36. A13 tidak berwenang menulis berkas-berkas itu.'
approval_evidence:
  question: 'Wewenang edit a03 atas tools/build_modular.py hanya efektif bila spesifikasi dan kebijakan hook diubah (AGENT_SPECIFICATIONS, ORCHESTRATION_ARCHITECTURE, scripts/guard.py, scripts/check_agents.py, definisi agent a03). Tidak ada agent yang berwenang menulis berkas-berkas itu, dan saya sendiri tidak punya akses tulis. Siapa yang mengerjakan perubahan tersebut?'
  options_offered: ['Anda/sesi Claude Code biasa', 'Susun draf perubahan di .scratch/ untuk ditinjau dan diterapkan pengguna', 'Tunda sampai definisi varian jelas']
  user_answer: 'Anda/sesi Claude Code biasa (Recommended)'
  answered_at: '2026-11-07'
  session_ref: 'Brief A01 memory_op R9 (pertanyaan Q-B1-an), sesi 2026-11-07'
  scope: 'HANYA jalur pelaksanaan perubahan spesifikasi/hook/check_agents/definisi a03: dikerjakan pengguna atau sesi Claude Code biasa di luar agent. Tidak mencakup isi perubahan, definisi varian, maupun penutupan Q-B1-al'
```

## D-38

```yaml
id: D-38
decision: 'Tiga varian keluaran build_modular didefinisikan: (i) Editorial = satu docx per bab memuat catatan editorial, pola nama ...-Modular-Bab-{I-IV}_Editorial.docx; (ii) Formal = satu docx per bab, siap kumpul meski masih ada celah, pola ...-Modular-Bab-{I-IV}.docx; (iii) Lengkap = proposal utuh mengikuti templat Individu IF4091, acuan berkas "Template-Proposal-IF4091-Capstone-Individu-2026 - Copy.docx" di root repo. Keluaran skrip hanya DOCX; pengguna mengunggah ke Google Docs secara manual; tidak ada jalur Google Docs otomatis dan tidak ada agent yang memakai konektor Google Docs'
class: L3
status: APPROVED
date: '2026-11-07'
related: [D-35, D-36, D-37, Q-B1-ak, P2-02]
basis: 'Pesan pengguna yang mendefinisikan varian (contoh pada folder modular/ dan templat di root) dan jawaban pengguna atas pertanyaan jalur Google Docs'
alternatives_considered: ['DOCX dulu, Google Docs lewat sesi terpisah', 'DOCX dan PDF saja, Google Docs tidak diperlukan']
consequences: 'MENYEMPITKAN lingkup D-35 (yang menyebut jalur Google Docs): jalur Google Docs otomatis tidak ada; D-35 tidak diubah selain catatan rujukan. Q-B1-ak ditandai DIPUTUSKAN SEBAGIAN. Keputusan ini TIDAK menetapkan dan tidak boleh dianggap disetujui: (a) apakah "Template-... Individu-2026 - Copy.docx" di root identik dengan template/Template-Proposal-IF4091-Capstone-Individu-2026.docx dan mana yang menjadi dasar skrip; (b) apakah PDF termasuk keluaran skrip; (c) isi tepat penanda/catatan editorial yang dibawa varian Editorial dan yang harus hilang dari Formal; (d) cara varian Lengkap menggabungkan Bab I-IV dan komponen pelengkap (halaman judul, abstrak, daftar isi, daftar pustaka) sesuai templat. Tidak memberi persetujuan build apa pun; P2-02 tetap berlaku (skrip build lama tetap dilarang). Q-B1-am (nasib skrip lama) tidak diubah. [Catatan rujukan 2026-11-07, ditambahkan A13: butir (b) dijawab D-39 (PDF untuk Formal dan Lengkap; D-38 diperluas untuk dua varian itu) dan butir (d) dijawab D-40 (sumber isi varian Lengkap); teks keputusan asli tidak diubah. Butir (a) dijawab D-42: penunjukan berkas "- Copy" di root pada poin (iii) digantikan oleh template/ sebatas penunjukan berkas templat.]'
approval_evidence:
  question: 'Bagaimana jalur ke Google Docs ditangani setelah Markdown final dibuat menjadi DOCX oleh build_modular.py?'
  options_offered: ['DOCX saja, unggah ke Google Docs manual', 'DOCX dulu, Google Docs lewat sesi terpisah', 'DOCX dan PDF saja, Google Docs tidak diperlukan']
  user_answer: 'DOCX saja, unggah ke Google Docs manual (Recommended)'
  user_message_definisi_varian: 'bedanya bisa dilihat di C:\Users\HYPE R Series\worktrees\project-proposal-setup\modular untuk modular yang tiap bab ada 2 jenis yaitu editorial (ada catatannya) dan formal (siap kumpul walau masih ada celah/kekurangan) dan C:\Users\HYPE R Series\worktrees\project-proposal-setup\Template-Proposal-IF4091-Capstone-Individu-2026 - Copy.docx untuk lengkap'
  answered_at: '2026-11-07'
  session_ref: 'Brief A01 memory_op R9 (definisi varian dan pertanyaan Google Docs), sesi 2026-11-07'
  scope: 'Definisi tiga varian (nama, pola nama berkas, makna) dan keluaran hanya DOCX tanpa jalur Google Docs otomatis. Tidak mencakup butir (a)-(d) pada consequences'
```

## D-39

```yaml
id: D-39
decision: 'Keluaran build_modular.py: varian Editorial = DOCX saja; varian Formal dan Lengkap = DOCX dan PDF. Lingkup terbatas pada format keluaran per varian'
class: L3
status: APPROVED
date: '2026-11-07'
related: [D-38, D-35, D-36, D-37, Q-B1-ap, Q-B1-ak, Q-B1-al, P2-02]
basis: 'Jawaban pengguna atas pertanyaan Q-B1-ap (apakah PDF termasuk keluaran skrip)'
alternatives_considered: ['DOCX saja untuk skrip', 'DOCX dan PDF otomatis (semua varian)']
consequences: 'MEMPERLUAS D-38 untuk varian Formal dan Lengkap (D-38 menyebut keluaran DOCX saja; teks D-38 tidak diubah). Q-B1-ap ditutup (DIPUTUSKAN). Konsekuensi yang diketahui A01 dari deskripsi opsi: konversi PDF memerlukan LibreOffice/soffice di mesin, skrip lebih kompleks, dan a03 memerlukan izin Bash baru. Keputusan ini TIDAK menetapkan dan tidak boleh dianggap disetujui: (a) cara konversi PDF; (b) perubahan izin Bash a03 (bagian Q-B1-al/D-37, dikerjakan pengguna atau sesi biasa); (c) kriteria audit a12 untuk PDF. Tidak memberi persetujuan build apa pun; P2-02 tetap berlaku (skrip build lama tetap dilarang).'
approval_evidence:
  question: 'Apakah PDF termasuk keluaran build_modular.py, selain DOCX (tiga varian: Editorial, Formal, Lengkap)? Bab I dan II saat ini sudah punya PDF hasil migrasi di luar sistem.'
  options_offered: ['DOCX saja untuk skrip', 'DOCX dan PDF otomatis', 'PDF hanya untuk varian Formal dan Lengkap']
  user_answer: 'PDF hanya untuk varian Formal dan Lengkap'
  answered_at: '2026-11-07'
  session_ref: 'Brief A01 memory_op R9 (pertanyaan Q-B1-ap), sesi 2026-11-07'
  scope: 'HANYA format keluaran per varian: Editorial DOCX saja; Formal dan Lengkap DOCX dan PDF. Tidak mencakup cara konversi PDF, perubahan izin Bash a03, kriteria audit a12 untuk PDF, maupun persetujuan build'
```

## D-40

```yaml
id: D-40
decision: 'Varian Lengkap mengisi templat Individu dengan teks Bab I-IV langsung dari Markdown bab1/-bab4/ (bukan dari docx Formal); komponen pelengkap yang datanya belum ada diberi placeholder yang jelas (mis. [DATA BELUM TERSEDIA]) sesuai aturan CLAUDE.md; daftar isi berupa field Word yang diperbarui saat dibuka (bagian dari opsi yang dipilih, menurut deskripsi opsi). Lingkup terbatas pada sumber isi dan penanganan komponen pelengkap'
class: L3
status: APPROVED
date: '2026-11-07'
related: [D-38, D-39, D-35, Q-B1-ar, Q-B1-ak, Q-B1-ao, P2-02]
basis: 'Jawaban pengguna atas pertanyaan Q-B1-ar (perakitan varian Lengkap)'
alternatives_considered: ['Isi dari docx Formal per bab', 'Kerangka templat saja dulu']
consequences: 'Q-B1-ar ditutup (DIPUTUSKAN). Konsekuensi: a12 harus memastikan tidak ada placeholder yang lolos ke berkas yang dikumpulkan. Keputusan ini TIDAK menetapkan dan tidak boleh dianggap disetujui: (a) isi tiap komponen pelengkap (halaman judul, abstrak, daftar isi, daftar pustaka); (b) templat acuan (Q-B1-ao tetap terbuka; fakta hash identik antara templat di template/ dan templat root "- Copy" sudah tercatat, bukan keputusan). Tidak memberi persetujuan build apa pun; P2-02 tetap berlaku (skrip build lama tetap dilarang).'
approval_evidence:
  question: 'Bagaimana varian Lengkap dirakit dari Markdown final: dari mana isi Bab I–IV diambil, dan bagaimana komponen pelengkap (halaman judul, abstrak, daftar isi, daftar pustaka) yang datanya belum ada ditangani?'
  options_offered: ['Isi dari Markdown bab, pelengkap placeholder', 'Isi dari docx Formal per bab', 'Kerangka templat saja dulu']
  user_answer: 'Isi dari Markdown bab, pelengkap placeholder (Recommended)'
  answered_at: '2026-11-07'
  session_ref: 'Brief A01 memory_op R9 (pertanyaan Q-B1-ar), sesi 2026-11-07'
  scope: 'HANYA sumber isi varian Lengkap (Markdown bab1/-bab4/) dan penanganan komponen pelengkap dengan placeholder jelas. Tidak mencakup isi tiap komponen pelengkap, templat acuan (Q-B1-ao), maupun persetujuan build'
```

## D-41

```yaml
id: D-41
decision: 'Varian Formal diturunkan dari Editorial dengan menghapus teks tersorot dan penanda berkurung, tanpa teks pengganti. Tidak ada sintaks penanda baru di Markdown dan tidak ada dua sumber Markdown. Lingkup terbatas pada cara skrip membedakan Editorial dan Formal dari satu sumber'
class: L3
status: SUPERSEDED by D-43
superseded_scope: 'Sebagian: hanya bagian "tanpa teks pengganti" (penanda dihapus tanpa pengganti), digantikan D-43 (Formal memakai teks pengganti Y dari sintaks {{ed:X||cl:Y}} bila ditulis). Bagian lain tetap berlaku: Formal diturunkan dari Editorial, teks tersorot dan penanda berkurung tanpa pengganti dihapus, satu sumber Markdown. Teks keputusan asli di bawah tidak diubah. Rujukan: D-43, D-38'
date: '2026-11-07'
related: [D-38, D-40, D-35, Q-B1-aq, Q-B1-ak, Q-B1-ao, P2-02]
basis: 'Jawaban pengguna atas pertanyaan Q-B1-aq (pembedaan Editorial dan Formal dari satu sumber Markdown)'
alternatives_considered: ['Satu sumber + sintaks penanda baku', 'Dua Markdown terpisah per bab']
consequences: 'Q-B1-aq ditutup (DIPUTUSKAN). Konsekuensi yang diketahui (dari deskripsi opsi dan temuan a12 TSK R5-Q-B1-aq; dicatat sebagai konsekuensi, BUKAN persetujuan atas hal-hal ini): kasus seperti entri Yang et al. (Formal sekarang "Yang, R., dkk. (2026)..." vs Editorial "Yang, R., [PERLU VERIFIKASI SUMBER: ...], & Liu, N. (2026)...") akan terhapus tanpa pengganti sehingga entri dapat tidak lengkap di Formal; teks Formal hasil skrip akan berbeda dari Formal yang ada sekarang di modular/. Keputusan ini TIDAK menetapkan dan tidak boleh dianggap disetujui: (a) apakah penghapusan tanpa pengganti dapat menyisakan kalimat tidak utuh atau entri daftar pustaka tidak lengkap di Formal, dan siapa/bagaimana memeriksanya (usul belum disetujui: a12 memeriksa hasil Formal, a09 bila teks berubah) - Q-B1-as; (b) apakah placeholder templat di Formal (tanggal sampul, "<jika diperlukan>", lampiran contoh, teks panduan templat) termasuk "siap kumpul" (terkait D-40) - Q-B1-at; (c) aturan deteksi catatan tak berkurung seperti "Format sitasi sementara" agar ikut terhapus - Q-B1-au; (d) apakah Formal yang ada sekarang di modular/ dibangun ulang atau dibiarkan - Q-B1-av. Tidak memberi persetujuan build apa pun; P2-02 tetap berlaku (skrip build lama tetap dilarang).'
approval_evidence:
  question: 'Bagaimana skrip membedakan Editorial dan Formal dari satu sumber Markdown, khususnya untuk bagian bertanda seperti entri Yang et al. yang isinya berbeda di Formal ("dkk.") dan Editorial (penulis lengkap + penanda)?'
  options_offered: ['Satu sumber + sintaks penanda baku', 'Dua Markdown terpisah per bab', 'Formal = Editorial tanpa sorotan (hapus penanda saja)']
  user_answer: 'Formal = Editorial tanpa sorotan (hapus penanda saja)'
  answered_at: '2026-11-07'
  session_ref: 'Brief A01 memory_op R9 (pertanyaan Q-B1-aq), sesi 2026-11-07'
  scope: 'HANYA cara pembedaan Editorial dan Formal: Formal diturunkan dari Editorial dengan menghapus teks tersorot dan penanda berkurung tanpa teks pengganti; tanpa sintaks penanda baru dan tanpa dua sumber. Tidak mencakup pemeriksaan kelengkapan hasil Formal, status placeholder templat, deteksi catatan tak berkurung, nasib Formal yang ada, maupun persetujuan build'
```

## D-42

```yaml
id: D-42
decision: 'Varian Lengkap merujuk template/Template-Proposal-IF4091-Capstone-Individu-2026.docx sebagai dasar templat. Berkas "Template-Proposal-IF4091-Capstone-Individu-2026 - Copy.docx" di root tidak dirujuk skrip. Lingkup terbatas pada penunjukan berkas templat dasar varian Lengkap'
class: L3
status: APPROVED
date: '2026-11-07'
related: [D-38, D-40, Q-B1-ao, Q-B1-ak, P2-02]
basis: 'Jawaban pengguna atas pertanyaan Q-B1-ao (berkas templat yang dirujuk skrip untuk varian Lengkap)'
alternatives_considered: ['Berkas "- Copy" di root', 'Salin templat ke lokasi tetap baru']
consequences: 'Q-B1-ao ditutup (DIPUTUSKAN). Penunjukan awal pengguna atas berkas "- Copy" di root (pesan definisi varian yang dikutip pada D-38) DIGANTIKAN, sebatas penunjukan berkas templat, oleh pilihan ini; bagian lain D-38 tidak berubah. Fakta (dari catatan sebelumnya di Q-B1-ao, bukan keputusan): sha256 kedua berkas identik (awalan a76030913c40). Keputusan ini TIDAK menetapkan dan tidak boleh dianggap disetujui: penghapusan atau pembiaran berkas "- Copy" di root (pengguna memutuskan di luar sistem; bukan bagian persetujuan ini), isi komponen pelengkap, maupun persetujuan build. P2-02 tetap berlaku (skrip build lama tetap dilarang).'
approval_evidence:
  question: 'Berkas templat mana yang dirujuk skrip untuk varian Lengkap? Kedua berkas identik menurut hash sha256 (awalan a76030913c40).'
  options_offered: ['template/', 'Berkas "- Copy" di root', 'Salin templat ke lokasi tetap baru']
  user_answer: 'template/ (Recommended)'
  answered_at: '2026-11-07'
  session_ref: 'Brief A01 memory_op R9 (pertanyaan Q-B1-ao), sesi 2026-11-07'
  scope: 'HANYA berkas templat dasar varian Lengkap = template/Template-Proposal-IF4091-Capstone-Individu-2026.docx; berkas "- Copy" di root tidak dirujuk skrip. Tidak mencakup nasib berkas "- Copy", isi komponen pelengkap, maupun persetujuan build'
```

## D-43

```yaml
id: D-43
decision: 'Varian Formal memakai teks pengganti Y dari sintaks {{ed:X||cl:Y}} di Markdown bila ditulis penulis (Editorial menampilkan X, Formal menampilkan Y, mis. "dkk."), dan menghapus penanda berkurung serta teks tersorot yang tidak punya pengganti. Lingkup terbatas pada perlakuan Formal terhadap sintaks pengganti di sumber Markdown Bab II'
class: L3
status: APPROVED
date: '2026-11-07'
related: [D-41, D-38, D-40, Q-B1-aq, Q-B1-as, Q-B1-au, P2-02]
basis: 'Sumber Markdown Bab II sudah memakai sintaks {{ed:X||cl:Y}} dan perilaku tools/build_modular.py yang ada memakai Y; D-41 mengasumsikan sintaks pengganti tidak ada (menurut brief A01)'
alternatives_considered: ['Tetap D-41: hapus penanda saja dan abaikan Y', 'Tunda sampai hasil pemeriksaan a12']
consequences: 'MENGUBAH keputusan APPROVED D-41 sebagian: D-41 ditandai SUPERSEDED by D-43 (sebagian, hanya bagian "tanpa teks pengganti"); teks D-41 tidak dihapus dan tidak diubah. Rujukan: D-41, D-38 (butir (c) D-38, isi penanda yang dibawa Editorial dan yang hilang dari Formal, tidak berubah selain yang dinyatakan di sini). Keputusan ini TIDAK menetapkan: cakupan sintaks di Bab I, III, IV (menurut brief A01 belum ada sintaks itu di bab-bab tersebut), dan tidak memberi persetujuan build apa pun; P2-02 tetap berlaku (skrip build lama tetap dilarang).'
approval_evidence:
  question: 'Sumber Markdown Bab II sudah memakai sintaks {{ed:X||cl:Y}}: Editorial menampilkan X dan Formal menampilkan teks pengganti Y yang ditulis penulis (mis. "dkk."). D-41 menetapkan Formal = Editorial tanpa sorotan, hapus penanda tanpa pengganti. Mana yang berlaku untuk Formal?'
  options_offered: ['Pakai Y bila ada, hapus penanda bila tidak (Recommended)', 'Tetap D-41, hapus penanda saja dan abaikan Y', 'Tunda sampai hasil pemeriksaan a12']
  user_answer: 'Pakai Y bila ada, hapus penanda bila tidak (Recommended)'
  answered_at: '2026-11-07'
  session_ref: 'Brief A01 memory_op R9 (perubahan D-41), sesi 2026-11-07'
  scope: 'HANYA perlakuan Formal: pakai Y dari {{ed:X||cl:Y}} bila ada; hapus penanda berkurung dan teks tersorot tanpa pengganti. Tidak mencakup cakupan sintaks di Bab I/III/IV maupun persetujuan build'
```

## D-44

```yaml
id: D-44
decision: 'Skrip tools/build_docx.py dan tools/build_with_toc.py tidak diperbaiki dan tetap dilarang (P2-02); tools/build_modular.py adalah satu-satunya jalur build; penghapusan kedua berkas dilakukan pengguna di luar sistem. Lingkup terbatas pada nasib dua skrip build lama (Q-B1-am)'
class: L3
status: APPROVED (lingkup terbatas; pilihan A01 atas delegasi pengguna, dapat dibatalkan pengguna kapan saja)
date: '2026-11-07'
related: [D-35, D-16, Q-B1-am, P2-02]
basis: 'Pesan delegasi pengguna (lihat approval_evidence) dan pilihan A01; Q-B1-am dijawab'
alternatives_considered: ['Memperbaiki build_docx.py dan build_with_toc.py (path Linux, outline Bab II lama)']
consequences: 'Q-B1-am DIPUTUSKAN → D-44. Teks asli D-16 TIDAK diubah; D-16 hanya diberi catatan rujukan (lihat catatan_rujukan pada D-16). Ketidaksesuaian dicatat, tidak diselesaikan: teks D-16 mengenai tools/verify_claims.py, bukan skrip build lama. Keputusan ini bukan jawaban pengguna atas opsi spesifik: pengguna mendelegasikan dan tidak menyebut opsi. Tidak memberi persetujuan build apa pun; P2-02 tetap berlaku.'
approval_evidence:
  question: 'Tidak diajukan per butir. Pertanyaan terbuka yang dijawab (OPEN_QUESTIONS Q-B1-am): Bagaimana nasib D-16 (perbaikan skrip build lama untuk path /home/user/project-proposal dan outline Bab II lama II.1-II.8) setelah D-35 memusatkan build pada build_modular.py?'
  options_offered: []
  user_answer: '2-4. lakukan sesuai preferensi anda'
  answered_at: '2026-11-07'
  session_ref: 'Brief A01 memory_op R9; pesan delegasi pengguna sesi 2026-11-07. Konteks menurut A01: pengguna merujuk daftar yang menunggu mereka, butir 2 Q-B1-al, butir 3 Q-B1-am, butir 4 Q-B1-as..av; butir "5." (dua docx bab2) ditanggapi terpisah'
  scope: 'Penafsiran A01 atas delegasi (pengguna tidak menyebut opsi spesifik): HANYA pilihan A01 untuk Q-B1-am, build_docx.py dan build_with_toc.py tidak diperbaiki dan tetap dilarang, build_modular.py satu-satunya jalur, penghapusan dilakukan pengguna di luar sistem. Q-B1-al TIDAK tercakup'
```

## D-45

```yaml
id: D-45
decision: 'Hasil build Formal diperiksa a12 (kalimat dan entri daftar pustaka utuh, tidak ada penanda tersisa); a09 ikut memeriksa bila teks berubah. Lingkup terbatas pada siapa dan apa yang diperiksa pada Formal (Q-B1-as)'
class: L3
status: APPROVED (lingkup terbatas; pilihan A01 atas delegasi pengguna, dapat dibatalkan pengguna kapan saja)
date: '2026-11-07'
related: [D-41, D-43, Q-B1-as, Q-B1-aq]
basis: 'Pesan delegasi pengguna (lihat approval_evidence) dan pilihan A01; Q-B1-as dijawab'
alternatives_considered: []
consequences: 'Q-B1-as DIPUTUSKAN → D-45. Pengguna tidak menyebut opsi spesifik. Tidak memberi persetujuan build apa pun; P2-02 tetap berlaku.'
approval_evidence:
  question: 'Tidak diajukan per butir. Pertanyaan terbuka yang dijawab (OPEN_QUESTIONS Q-B1-as): Apakah penghapusan penanda tanpa pengganti (D-41) dapat menyisakan kalimat tidak utuh atau entri daftar pustaka tidak lengkap di Formal (mis. entri Yang et al., Formal sekarang "dkk." vs Editorial penulis lengkap + penanda), dan siapa serta bagaimana memeriksanya?'
  options_offered: []
  user_answer: '2-4. lakukan sesuai preferensi anda'
  answered_at: '2026-11-07'
  session_ref: 'Brief A01 memory_op R9; pesan delegasi pengguna sesi 2026-11-07 (konteks menurut A01: butir 4 = Q-B1-as..av)'
  scope: 'Penafsiran A01 atas delegasi: HANYA pilihan A01 untuk Q-B1-as, a12 memeriksa Formal hasil build (kalimat/entri pustaka utuh, tak ada penanda tersisa), a09 ikut bila teks berubah'
```

## D-46

```yaml
id: D-46
decision: 'Placeholder templat di Formal (tanggal sampul, "<jika diperlukan>", lampiran contoh, teks panduan templat) dilaporkan a12 sebagai temuan ringan dan tidak memblokir; hanya varian Lengkap dinyatakan gagal bila placeholder tersisa (D-40). Lingkup terbatas pada perlakuan placeholder templat di Formal (Q-B1-at)'
class: L3
status: APPROVED (lingkup terbatas; pilihan A01 atas delegasi pengguna, dapat dibatalkan pengguna kapan saja)
date: '2026-11-07'
related: [D-38, D-40, D-41, Q-B1-at]
basis: 'Pesan delegasi pengguna (lihat approval_evidence) dan pilihan A01; Q-B1-at dijawab'
alternatives_considered: []
consequences: 'Q-B1-at DIPUTUSKAN → D-46. Pengguna tidak menyebut opsi spesifik. Tidak memberi persetujuan build apa pun; P2-02 tetap berlaku.'
approval_evidence:
  question: 'Tidak diajukan per butir. Pertanyaan terbuka yang dijawab (OPEN_QUESTIONS Q-B1-at): Apakah placeholder templat yang ada di Formal (tanggal sampul "Bandung, <tanggal>", "<jika diperlukan>", "<diisi sesuai sumber yang dirujuk pada bab ini>", "Lampiran A. Contoh Judul Lampiran", teks panduan templat di Bab I dan III) termasuk "siap kumpul" menurut D-38 dan D-40?'
  options_offered: []
  user_answer: '2-4. lakukan sesuai preferensi anda'
  answered_at: '2026-11-07'
  session_ref: 'Brief A01 memory_op R9; pesan delegasi pengguna sesi 2026-11-07 (konteks menurut A01: butir 4 = Q-B1-as..av)'
  scope: 'Penafsiran A01 atas delegasi: HANYA pilihan A01 untuk Q-B1-at, placeholder templat di Formal = temuan ringan a12 tanpa memblokir; Lengkap gagal bila placeholder tersisa'
```

## D-47

```yaml
id: D-47
decision: 'Skrip menghapus teks tersorot dan catatan "Format sitasi sementara" secara eksplisit; a12 memeriksa tidak ada sorotan atau kata kunci itu di Formal. Lingkup terbatas pada deteksi catatan editorial tak berkurung (Q-B1-au)'
class: L3
status: APPROVED (lingkup terbatas; pilihan A01 atas delegasi pengguna, dapat dibatalkan pengguna kapan saja)
date: '2026-11-07'
related: [D-41, D-43, Q-B1-au, Q-B1-aq]
basis: 'Pesan delegasi pengguna (lihat approval_evidence) dan pilihan A01; Q-B1-au dijawab'
alternatives_considered: []
consequences: 'Q-B1-au DIPUTUSKAN → D-47. Pengguna tidak menyebut opsi spesifik. Tidak memberi persetujuan build apa pun; P2-02 tetap berlaku.'
approval_evidence:
  question: 'Tidak diajukan per butir. Pertanyaan terbuka yang dijawab (OPEN_QUESTIONS Q-B1-au): Apa aturan deteksi catatan editorial tak berkurung seperti "Format sitasi sementara" agar ikut terhapus dari Formal (pencarian penanda berpola tidak menjaringnya)?'
  options_offered: []
  user_answer: '2-4. lakukan sesuai preferensi anda'
  answered_at: '2026-11-07'
  session_ref: 'Brief A01 memory_op R9; pesan delegasi pengguna sesi 2026-11-07 (konteks menurut A01: butir 4 = Q-B1-as..av)'
  scope: 'Penafsiran A01 atas delegasi: HANYA pilihan A01 untuk Q-B1-au, penghapusan eksplisit teks tersorot dan catatan "Format sitasi sementara"; a12 memeriksa tak ada sorotan/kata kunci itu di Formal'
```

## D-48

```yaml
id: D-48
decision: 'Berkas Formal yang ada di modular/ dibangun ulang bila skrip siap, dengan Approval Request P2-02 per eksekusi yang menyebut berkas modular/ yang ditimpa. Lingkup terbatas pada nasib Formal yang ada (Q-B1-av)'
class: L3
status: APPROVED (lingkup terbatas; pilihan A01 atas delegasi pengguna, dapat dibatalkan pengguna kapan saja)
date: '2026-11-07'
related: [D-41, D-43, Q-B1-av, Q-B1-aw, P2-02]
basis: 'Pesan delegasi pengguna (lihat approval_evidence) dan pilihan A01; Q-B1-av dijawab'
alternatives_considered: ['Dibiarkan']
consequences: 'Q-B1-av DIPUTUSKAN → D-48. Skrip belum siap menurut pengamatan A01 (Q-B1-aw), sehingga pembangunan ulang belum dapat dilakukan. Pengguna tidak menyebut opsi spesifik. Tidak memberi persetujuan build apa pun; persetujuan P2-02 tetap per eksekusi.'
approval_evidence:
  question: 'Tidak diajukan per butir. Pertanyaan terbuka yang dijawab (OPEN_QUESTIONS Q-B1-av): Apakah berkas Formal yang ada sekarang di modular/ dibangun ulang dengan skrip (D-41) atau dibiarkan?'
  options_offered: []
  user_answer: '2-4. lakukan sesuai preferensi anda'
  answered_at: '2026-11-07'
  session_ref: 'Brief A01 memory_op R9; pesan delegasi pengguna sesi 2026-11-07 (konteks menurut A01: butir 4 = Q-B1-as..av)'
  scope: 'Penafsiran A01 atas delegasi: HANYA pilihan A01 untuk Q-B1-av, Formal yang ada dibangun ulang bila skrip siap dengan Approval Request P2-02 per eksekusi'
```

## D-49

```yaml
id: D-49
decision: 'Markdown bab1/Bab_I_Draft.md (DRAF 10) adalah sumber kebenaran Bab I untuk modular/. Docx/pdf sementara bab1/Bab1_Revisi1_IF4091.* (hasil migrasi LLM lain) tidak dipakai sebagai sumber; modular/ Bab I dibangun dari Markdown lewat skrip (setelah Q-B1-aw/al). Lingkup: hanya penentuan sumber Bab I; tidak mencakup isi naskah, penghapusan berkas sementara, atau Bab II'
class: L3
status: APPROVED
date: '2026-11-07'
related: [D-29, D-30, Q-B1-ax, Q-B1-aw]
basis: 'Jawaban pengguna (approval_evidence) atas pertanyaan sumber Bab I (bagian dari Q-B1-ax); audit a12 TSK R5-migrasi-docx-vs-md (F-A12-0001..0004)'
alternatives_considered: ['Docx sementara', 'Sebagian diubah pengguna sendiri di docx']
consequences: 'Q-B1-ax: bagian sumber Bab I diputuskan; butir tetap TERBUKA (Bab II dan waktu pemindahan). Pengamatan a12 (bukan keputusan): sekitar 25-30 kalimat Bab I ditulis ulang di docx; atribusi "dokumen penyelarasan tim" dihapus atau diganti "informasi awal"; tanggal 29-30 Oktober hilang; paragraf diubah menjadi daftar bernomor; 38 penanda editorial (hitungan perlu diverifikasi) bocor sebagai teks biasa; Bab II docx setia pada Markdown (0 paragraf berbeda) tetapi 12 penanda editorial tercetak, plus backtick literal dan satu baris sampul tambahan; front matter docx memuat placeholder templat dan glosarium tak sesuai. Audit a12 itu PARTIAL (pembandingan dengan modular/, sitasi, sebagian docx-vs-pdf belum diperiksa). Bukti kerja: .scratch/a12/.'
approval_evidence:
  question: 'Untuk Bab I, versi mana yang otoritatif untuk dipindahkan ke modular/? Docx sementara menulis ulang puluhan kalimat dan menghapus atribusi "dokumen penyelarasan tim", sedangkan bab1/Bab_I_Draft.md (DRAF 10) mengikuti aturan atribusi D-29–D-30.'
  options_offered: ['Bab_I_Draft.md', 'Docx sementara', 'Ada sebagian yang saya ubah sendiri di docx']
  user_answer: 'Bab_I_Draft.md (Recommended)'
  answered_at: '2026-11-07'
  session_ref: 'Brief A01 memory_op R9, sesi 2026-11-07'
  scope: 'Hanya penentuan sumber Bab I untuk modular/'
```

## D-50

```yaml
id: D-50
decision: 'PDF varian Formal dan Lengkap dibuat di dalam tools/build_modular.py (skrip sudah memanggil soffice), tanpa izin Bash baru untuk a03 dan tanpa perubahan allowlist guard; satu persetujuan per eksekusi P2-02 mencakup DOCX dan PDF. Syarat yang diketahui: LibreOffice terpasang di mesin pengguna'
class: L3
status: APPROVED
date: '2026-11-07'
related: [D-39, Q-B1-al, Q-B1-aw, P2-02]
basis: 'Jawaban pengguna atas bagian [PERLU KEPUTUSAN PENGGUNA] di draf patch a03'
alternatives_considered: ['P-B perintah soffice terpisah untuk a03', 'P-C pengguna mengonversi sendiri']
consequences: 'Melengkapi D-39. Menutup bagian jalur PDF dari Q-B1-al; Q-B1-al sendiri tetap TERBUKA.'
approval_evidence:
  question: 'Lewat jalur mana PDF untuk varian Formal dan Lengkap (D-39) dibuat?'
  options_offered: ['P-A di dalam build_modular.py', 'P-B perintah soffice terpisah untuk a03', 'P-C pengguna mengonversi sendiri']
  user_answer: 'P-A: di dalam build_modular.py (Recommended)'
  answered_at: '2026-11-07'
  session_ref: 'Brief A01 memory_op R9, sesi 2026-11-07'
  scope: 'Hanya jalur pembuatan PDF Formal dan Lengkap'
```

## D-51

```yaml
id: D-51
decision: 'Draf patch boleh memuat aturan ask untuk Edit(./tools/build_modular.py) di .claude/settings.json; pelaksana tetap pengguna/sesi biasa (D-37). Memperluas daftar berkas D-37 dengan satu berkas konfigurasi tersebut saja'
class: L3
status: APPROVED
date: '2026-11-07'
related: [D-36, D-37, Q-B1-al]
basis: 'Jawaban pengguna atas pertanyaan perluasan daftar berkas D-37'
alternatives_considered: ['Tidak, hanya berkas daftar D-37', 'Tidak, dan batalkan izin edit a03']
consequences: 'Efektivitas prompt bergantung pada hasil uji T-14 (ask di auto mode). Tidak diputuskan: perubahan scripts/selftest.py (usulan a03 di luar daftar D-37; butir terbuka Q-B1-ay) dan cakupan audit a12 atas D-36 terhadap diff skrip (kartu A12 tidak memuat tools/ dalam akses bacanya; butir terbuka Q-B1-az). Pengamatan a03: DECISION_LOG hanya memuat satu entri D-41 dan revisinya lewat D-43 (D-41 SUPERSEDED sebagian), sehingga patch tidak bergantung pada D-41.'
approval_evidence:
  question: 'Apakah patch juga boleh menambah aturan ask untuk Edit(./tools/build_modular.py) di .claude/settings.json (berkas ini tidak ada di daftar D-37)? Tanpa aturan ini, guard hanya bisa menolak sehingga persetujuan per perubahan (D-36) tidak ditegakkan oleh sistem.'
  options_offered: ['Ya, tambah aturan ask', 'Tidak, hanya berkas daftar D-37', 'Tidak, dan batalkan izin edit a03']
  user_answer: 'Ya, tambah aturan ask (Recommended)'
  answered_at: '2026-11-07'
  session_ref: 'Brief A01 memory_op R9, sesi 2026-11-07'
  scope: 'Hanya aturan ask Edit(./tools/build_modular.py) di .claude/settings.json'
```

## D-52

```yaml
id: D-52
decision: 'scripts/selftest.py tidak diubah sekarang; cukup uji manual T-14 dan T-30 setelah patch diterapkan. Kasus uji tiruan dapat menyusul bila pengguna meminta. Lingkup terbatas pada Q-B1-ay'
class: L3
status: APPROVED (lingkup terbatas; pilihan A01 atas delegasi pengguna, dapat dibatalkan pengguna kapan saja)
date: '2026-11-07'
related: [D-37, D-51, Q-B1-ay, Q-B1-al]
basis: 'Pesan delegasi pengguna (lihat approval_evidence) dan pilihan A01; Q-B1-ay dijawab'
alternatives_considered: []
consequences: 'Q-B1-ay DIPUTUSKAN → D-52. Pengguna tidak menyebut opsi spesifik. Tidak menerapkan patch Q-B1-al dan tidak menyetujui butir OPSIONAL di patch. Q-B1-al tetap TERBUKA.'
approval_evidence:
  question: 'Tidak diajukan per butir. Pertanyaan terbuka yang dijawab (OPEN_QUESTIONS Q-B1-ay): Apakah scripts/selftest.py boleh diubah sebagai bagian patch a03 (usulan a03, di luar daftar berkas D-37)?'
  options_offered: []
  user_answer: 'lakukan sesuai preferensi anda'
  answered_at: '2026-11-07'
  session_ref: 'Brief A01 memory_op R9, sesi 2026-11-07 (konteks menurut A01: A01 baru menyerahkan patch final .scratch/patch_Q-B1-al.md dan mendaftar butir terbuka; pengguna tidak menyebut opsi spesifik)'
  scope: 'Penafsiran A01 atas delegasi: HANYA pilihan A01 untuk Q-B1-ay (selftest.py tidak diubah sekarang). BUKAN penerapan patch dan BUKAN persetujuan butir OPSIONAL di patch'
```

## D-53

```yaml
id: D-53
decision: 'Audit a12 atas perubahan D-36 hanya mencakup berkas hasil build. Diff tools/build_modular.py ditinjau pengguna melalui prompt ask per edit (D-51). Akses baca a12 tidak diperluas ke tools/. Lingkup terbatas pada Q-B1-az'
class: L3
status: APPROVED (lingkup terbatas; pilihan A01 atas delegasi pengguna, dapat dibatalkan pengguna kapan saja)
date: '2026-11-07'
related: [D-36, D-51, Q-B1-az, Q-B1-al]
basis: 'Pesan delegasi pengguna (lihat approval_evidence) dan pilihan A01; Q-B1-az dijawab'
alternatives_considered: []
consequences: 'Q-B1-az DIPUTUSKAN → D-53. Pengguna tidak menyebut opsi spesifik. Pengamatan A01 (bukan keputusan): tinjauan diff skrip bergantung pada prompt ask D-51 yang efektivitasnya diuji T-14. Q-B1-al tetap TERBUKA.'
approval_evidence:
  question: 'Tidak diajukan per butir. Pertanyaan terbuka yang dijawab (OPEN_QUESTIONS Q-B1-az): Apakah audit a12 atas perubahan D-36 mencakup diff tools/build_modular.py (kartu A12 tidak memuat tools/ dalam akses bacanya)?'
  options_offered: []
  user_answer: 'lakukan sesuai preferensi anda'
  answered_at: '2026-11-07'
  session_ref: 'Brief A01 memory_op R9, sesi 2026-11-07 (konteks menurut A01: patch final .scratch/patch_Q-B1-al.md diserahkan; pengguna tidak menyebut opsi spesifik)'
  scope: 'Penafsiran A01 atas delegasi: HANYA pilihan A01 untuk Q-B1-az. BUKAN penerapan patch dan BUKAN persetujuan butir OPSIONAL di patch'
```

## D-54

```yaml
id: D-54
decision: 'Kriteria audit PDF oleh a12 (D-39 butir c): a12 membandingkan teks dan jumlah halaman PDF terhadap DOCX dengan pdftotext dan pdfinfo (sudah di allowlist), tanpa izin baru. Lingkup terbatas pada kriteria audit PDF'
class: L3
status: APPROVED (lingkup terbatas; pilihan A01 atas delegasi pengguna, dapat dibatalkan pengguna kapan saja)
date: '2026-11-07'
related: [D-39, D-50, D-36, Q-B1-ap]
basis: 'Pesan delegasi pengguna (lihat approval_evidence) dan pilihan A01; melengkapi D-39 yang menyisakan kriteria audit a12 untuk PDF'
alternatives_considered: []
consequences: 'Tidak ada butir OPEN_QUESTIONS terbuka khusus untuk hal ini (Q-B1-ap sudah DIPUTUSKAN D-39), sehingga dicatat langsung sebagai keputusan tanpa butir baru. Pengguna tidak menyebut opsi spesifik. Tidak ada perubahan allowlist.'
approval_evidence:
  question: 'Tidak diajukan per butir. Hal yang dijawab: kriteria audit a12 untuk PDF (sisa D-39 butir c, catatan pada OPEN_QUESTIONS Q-B1-ap).'
  options_offered: []
  user_answer: 'lakukan sesuai preferensi anda'
  answered_at: '2026-11-07'
  session_ref: 'Brief A01 memory_op R9, sesi 2026-11-07 (konteks menurut A01: patch final .scratch/patch_Q-B1-al.md diserahkan; pengguna tidak menyebut opsi spesifik)'
  scope: 'Penafsiran A01 atas delegasi: HANYA pilihan A01 untuk kriteria audit PDF a12. BUKAN penerapan patch dan BUKAN persetujuan butir OPSIONAL di patch'
```

## D-55

```yaml
id: D-55
decision: 'Batas kesimpulan penelitian pada I.4 (paragraf 6) = tahap dokumen SEBELUM penguncian CPPT dan resume medis. Lingkup terbatas pada tahap dokumen sebagai batas kesimpulan di I.4'
class: L3
status: APPROVED (lingkup terbatas)
date: '2026-11-08'
related: [D-30, D-25, D-56, Q-B1-f, F-A04-0012, F-A11-0004]
basis: 'Jawaban pengguna atas pertanyaan a04 P2 (dari 3), diteruskan A01 verbatim'
alternatives_considered: ['Sesudah penguncian', 'Keduanya']
consequences: 'Menurut A01 (bukan keputusan tambahan): data uji harus berisi dokumen pada tahap sebelum penguncian; F-A11-0004 di I.5 tetap terbuka; I.4 paragraf 6 perlu diselaraskan (belum dilakukan, naskah tidak diubah A13). Tidak memutuskan versi dokumen pada data uji (F-A11-0004) maupun penyelesaian premis kedua I.1 paragraf 14. F-A04-0012 IN_PROGRESS.'
approval_evidence:
  question: 'Pertanyaan a04 (P2 dari 3), diteruskan verbatim. Konteks (ringkas): I.4 paragraf 6 menyatakan rentang yang dikaji "mencakup masa sebelum dan sesudah CPPT dan resume medis dikunci"; I.1 paragraf 14 (premis kedua) menyatakan ketidaksesuaian perlu diperiksa sebelum dokumen dikunci; I.5 masih memuat penanda tentang versi dan tahap dokumen pada data uji (F-A11-0004). Bila data uji hanya berisi dokumen versi akhir, hasilnya tidak dapat menjadi dasar kesimpulan tentang deteksi sebelum penguncian. Pertanyaan: Tahap dokumen mana yang Anda maksud sebagai batas kesimpulan penelitian: sebelum penguncian, sesudah penguncian, atau keduanya?'
  options_offered: ['Sebelum penguncian', 'Sesudah penguncian', 'Keduanya']
  user_answer: 'Sebelum penguncian'
  answered_at: '2026-11-08'
  session_ref: 'sesi /sesi-mulai 2026-11-08, AskUserQuestion P2 penguncian (a04, F-A04-0012)'
  scope: 'Hanya tahap dokumen sebagai batas kesimpulan di I.4; tidak memutuskan versi dokumen pada data uji (F-A11-0004) maupun penyelesaian premis kedua I.1 paragraf 14'
```

## D-56

```yaml
id: D-56
decision: 'Kesimpulan atas kedua pertanyaan penelitian dinyatakan TERPISAH untuk rawat inap dan rawat jalan. Lingkup terbatas pada cara pelaporan kesimpulan'
class: L3
status: APPROVED (lingkup terbatas)
date: '2026-11-08'
related: [D-21, D-22, D-29, D-55, Q-B1-t, Q-B1-f, F-A04-0013]
basis: 'Jawaban pengguna atas pertanyaan a04 P3 (dari 3), diteruskan A01 verbatim'
alternatives_considered: ['Gabungan', 'Belum diputuskan']
consequences: 'Q-B1-t bagian pelaporan (terpisah atau gabungan) DIPUTUSKAN → D-56. Catatan (bukan keputusan): D-29 per jenis perawatan berimplikasi pada I.2, I.3, dan I.5; belum diperiksa. Tidak memutuskan perlu tidaknya pembanding kondisi saat ini (sudah D-22), angka ambang, atau mekanisme kombinasi. Naskah tidak diubah A13.'
approval_evidence:
  question: 'Pertanyaan a04 (P3 dari 3), diteruskan verbatim. Konteks (ringkas): I.4 paragraf 7 menyatakan kesimpulan berlaku untuk "kasus kebidanan dan anak di satu RSIA mitra" tanpa membedakan rawat inap dan rawat jalan; paragraf 4 menyebut cakupan rawat jalan terbatas; menurut Penyelarasan:279 rawat jalan cukup diperiksa dengan satu aturan; Q-B1-t belum dijawab. Bila cakupan jenis ketidaksesuaian rawat jalan jauh lebih sempit, presisi dan recall gabungan dapat menutupi perbedaan antarperawatan. Pertanyaan: Apakah kesimpulan atas kedua pertanyaan dinyatakan terpisah untuk rawat inap dan rawat jalan, atau gabungan?'
  options_offered: ['Terpisah', 'Gabungan', 'Belum diputuskan']
  user_answer: 'Terpisah'
  answered_at: '2026-11-08'
  session_ref: 'sesi /sesi-mulai 2026-11-08, AskUserQuestion P3 pelaporan (a04, F-A04-0013 terkait)'
  scope: 'Hanya cara pelaporan kesimpulan (terpisah per jenis perawatan). Tidak memutuskan perlu tidaknya pembanding kondisi saat ini (sudah D-22), angka ambang, atau mekanisme kombinasi'
```

## D-57

```yaml
id: D-57
decision: 'I.4 paragraf 6 dirumuskan sebagai batas KESIMPULAN saja sesuai D-55 (kesimpulan berlaku bagi dokumen pada tahap sebelum penguncian). Pengecualian dokumen terkunci dari "kajian" dan pengandaian bahwa CPPT dan resume sama-sama terkunci dihapus dari paragraf 6. Data uji tetap terbuka (F-A11-0004)'
class: L3
status: APPROVED (lingkup terbatas)
date: '2026-11-08'
related: [D-55, D-56, D-24, D-27, Q-B1-bc, Q-B1-ba, Q-B1-ae, F-A07-0050, F-A05-0023, F-A05-0024, F-A11-0004]
basis: 'Jawaban pengguna atas AskUserQuestion I.4 paragraf 6 (kedua), diteruskan A01'
alternatives_considered: ['Pertahankan batas kajian', 'Tunda dengan penanda keputusan']
consequences: 'Menjelaskan dan menegaskan D-55 (tidak membatalkannya). Catatan A01 (bukan keputusan tambahan): F-A07-0050 dan F-A05-0023/0024 sebagian tertangani oleh pembatasan teks; tetap OPEN sampai auditor penemu menyatakan lain. Q-B1-bc DIPUTUSKAN → D-57 hanya untuk rumusan paragraf 6. Arti penguncian (Q-B1-ba), data uji (F-A11-0004, Q-B1-ae), dan penyelarasan I.2/I.3/I.5 dengan D-56 (Q-B1-bd) tetap terbuka. Naskah belum diubah A13.'
approval_evidence:
  question: 'a13 sudah mencatat semuanya (Q-B1-ba..bf), dan klarifikasi RSIA dari Anda dicatat sebagai pernyataan, bukan keputusan. Satu keputusan tersisa untuk I.4 paragraf 6 (F-A07-0050, F-A05-0023, F-A05-0024). Konteks: D-55 hanya memutuskan batas KESIMPULAN pada tahap sebelum penguncian. DRAF 11 menulis lebih jauh ("kajian terbatas pada tahap sebelum ... dikunci"; dokumen terkunci "tidak termasuk kajian") dan menyebut keduanya dikunci, sedangkan klarifikasi RSIA menyatakan CPPT tidak dapat diubah tetapi resume masih dapat diubah, dan melarang asumsi keduanya terkunci permanen. Klarifikasi itu belum ada di Penyelarasan, jadi tidak boleh dikutip di naskah (D-24, D-27). Anda juga meminta agar keputusan dan ruang lingkup tidak diperluas. Bagaimana paragraf 6 dirumuskan?'
  options_offered: ['Batas kesimpulan saja (Rekomendasi)', 'Pertahankan batas kajian', 'Tunda dengan penanda keputusan']
  user_answer: 'Batas kesimpulan saja (Rekomendasi)'
  answered_at: '2026-11-08'
  session_ref: 'sesi /sesi-mulai 2026-11-08, AskUserQuestion I.4 paragraf 6 (kedua)'
  scope: 'Hanya rumusan I.4 paragraf 6 sebagai batas kesimpulan (tidak memutuskan versi dokumen pada data uji F-A11-0004, arti penguncian, atau penyelarasan I.2/I.3/I.5 dengan D-56)'
```

## D-58

```yaml
id: D-58
decision: 'Aturan jawaban untuk D-56: tiap pertanyaan penelitian (I.2) dijawab SENDIRI untuk rawat inap dan untuk rawat jalan, tanpa aturan penggabungan; kriteria D-29 serta ambang berlaku per jenis perawatan. I.2, I.3, dan I.5 diselaraskan dengan rumusan ini. Tidak memutuskan angka ambang, kondisi keabsahan jawaban per stratum, atau selisih minimum'
class: L3
status: APPROVED (lingkup terbatas)
date: '2026-11-08'
related: [D-56, D-29, D-55, D-57, D-21, Q-B1-bd, Q-B1-bg, Q-B1-bh, Q-B1-bi, F-A07-0049, F-A05-0025, F-A05-0032, Q-TEAM butir 8, Q-B1-y, Q-B1-ad]
basis: 'Jawaban pengguna atas AskUserQuestion Aturan D-56, diteruskan A01'
alternatives_considered: ['Tandai saja, belum selaraskan (Rekomendasi)', 'Jawaban terpisah plus keseluruhan']
consequences: 'Menindaklanjuti D-56. Catatan A01 (bukan keputusan tambahan): opsi yang dipilih memuat catatan bahwa ambang dan kondisi keabsahan per stratum membutuhkan Approval Request lanjutan dan pembahasan tim (Q-TEAM butir 8, Q-B1-y, Q-B1-ad). F-A05-0032 (cakupan pertanyaan I.2 vs batas kesimpulan I.4) TIDAK diputuskan oleh D-58 dan tetap OPEN; F-A07-0049 dan F-A05-0025 tetap OPEN sampai auditor penemu menyatakan lain. Q-B1-bd DIPUTUSKAN → D-58 hanya untuk bentuk jawaban. Perlu pembahasan dengan tim karena mengubah arti jawaban rumusan capstone (Penyelarasan:35, satu jawaban ya/tidak per rumusan): Q-B1-bh. Naskah belum diubah A13.'
approval_evidence:
  question: 'QA siklus 1 untuk I.4 selesai. Paragraf 6 sudah mengikuti D-57. Sisa yang menentukan adalah D-56 (kesimpulan terpisah rawat inap dan rawat jalan): paragraf 7 I.4 sudah menyatakannya, tetapi aturan jawaban "tidak" di I.2 (paragraf 6 dan 7) dan ukuran di I.3 masih satu jawaban ya/tidak per pertanyaan (F-A07-0049, F-A05-0025). Akibatnya jawaban tidak terdefinisi bila rawat inap "ya" dan rawat jalan "tidak". a05 juga mencatat (F-A05-0032) bahwa cakupan pertanyaan I.2 (seluruh masa prapengajuan) kini lebih luas daripada batas kesimpulan I.4 (sebelum penguncian). Ini menyentuh I.2, I.3, dan I.5, di luar I.4 yang Anda minta ditinjau, dan memakai sisa siklus otomatis (maksimal 2; siklus 1 sudah terpakai). Bagaimana Anda ingin menangani aturan jawaban untuk D-56?'
  options_offered: ['Tandai saja, belum selaraskan (Rekomendasi)', 'Dua jawaban terpisah', 'Jawaban terpisah plus keseluruhan']
  user_answer: 'Dua jawaban terpisah'
  answered_at: '2026-11-08'
  session_ref: 'sesi /sesi-mulai 2026-11-08, AskUserQuestion Aturan D-56'
  scope: 'Hanya bentuk jawaban per pertanyaan (dua jawaban terpisah per jenis perawatan, tanpa penggabungan) dan penyelarasan I.2, I.3, I.5 dengan bentuk itu'
```

## D-59

```yaml
id: D-59
decision: 'Celah (b) di I.1 paragraf 16 dikeluarkan dari daftar celah literatur dan dinyatakan sebagai PILIHAN RANCANGAN capstone (menguji gabungan pemeriksaan berbasis model bahasa besar dan pemeriksaan deterministik), lengkap dengan alasan dan trade-off. Celah (a) dan (c) tetap. Tanpa pencarian literatur hibrida. D-22, D-29, D-31, D-58 tidak berubah'
class: L3
status: APPROVED (lingkup terbatas)
date: '2026-11-08'
related: [D-22, D-29, D-31, D-58, F-A05-0101, F-A07-0056, F-A08-0001..0007]
basis: 'Jawaban pengguna atas AskUserQuestion Celah (b), diteruskan A01 (brief TSK-091)'
alternatives_considered: ['Pertahankan bersyarat + telusuri hibrida', 'Pertahankan, batasi klaim pada dua studi']
consequences: 'Catatan A13 (bukan keputusan tambahan): F-A05-0101 dan F-A07-0056 dicatat IN_PROGRESS dengan rujukan D-59; RESOLVED hanya oleh a05/a07 setelah pemeriksaan ulang. F-A05-0102..0105 (requires_decision) tetap OPEN. Naskah (I.1 p16, DRAF 14/15) belum diselaraskan menurut catatan A13; revisi siklus 1 (DRAF 15) sedang berjalan saat dicatat.'
approval_evidence:
  question: 'Di I.1 paragraf 16 (DRAF 14), celah (b) berbunyi: kedua studi (Dietrich dan Stubbert; Zeba dkk.) "tidak membandingkan gabungan pemeriksaan berbasis model bahasa besar dan pemeriksaan deterministik dengan masing-masing jenis pemeriksaan". a05 (F-A05-0101) menilai celah ini benar dengan sendirinya, karena studi non-hibrida otomatis tidak membandingkan gabungan, jadi ia diturunkan dari rancangan Anda, bukan dari masalah. a07 (F-A07-0056) menilai celah ini belum memenuhi syarat bukti komparatif, karena naskah sendiri menyatakan literatur hibrida belum ditelusuri. a08 mengonfirmasi bahwa Zeba membandingkan modul deterministik dengan verifier LLM (Tabel 9), tetapi bukan gabungannya. Bagaimana celah (b) diperlakukan? Pilihan ini menyentuh klaim utama dan rancangan, sehingga hanya Anda yang dapat memutuskannya.'
  options_offered: ['Jadikan pilihan rancangan (Recommended)', 'Pertahankan bersyarat + telusuri hibrida', 'Pertahankan, batasi klaim pada dua studi']
  user_answer: 'Jadikan pilihan rancangan (Recommended)'
  answered_at: '2026-11-08'
  session_ref: 'sesi /sesi-mulai 2026-11-08 (lanjutan), AskUserQuestion Celah (b)'
  scope: 'Hanya perlakuan celah (b) di I.1 paragraf 16: dikeluarkan dari celah literatur dan dinyatakan sebagai pilihan rancangan capstone dengan alasan dan trade-off; celah (a) dan (c) tetap; tanpa pencarian hibrida; D-22, D-29, D-31, D-58 tidak berubah'
```

## D-60

```yaml
id: D-60
decision: 'Rumusan celah (a) dan (c) di I.1 paragraf 16 diperbaiki: paragraf membahas keempat studi Subbab II.5 dan Li dkk. (II.6:178). Celah (a) dirumuskan sebagai belum adanya studi yang memeriksa dua dokumen tulisan tenaga kesehatan dalam satu episode. Celah (c) dipersempit pada pemeriksaan dokumentasi klinis dan menyatakan posisinya terhadap Li dkk. Rumusan masalah, tujuan, I.2-I.5 tidak berubah; D-59 tetap'
class: L3
status: APPROVED (lingkup terbatas)
date: '2026-11-08'
related: [D-59, D-22, F-A07-0060, F-A05-0110, F-A05-0111, F-A05-0106, F-A05-0109]
basis: 'Jawaban pengguna atas AskUserQuestion Celah (a),(c), diteruskan A01 (brief TSK-092)'
alternatives_considered: ['Nyatakan kriteria seleksi saja', 'Pertahankan, catat sebagai keterbatasan']
consequences: 'Deskripsi opsi (dari brief A01): celah lebih sulit dibantah penguji karena kontra-contoh di Bab II ikut dibahas, tetapi paragraf bertambah rincian dan perlu pengecekan sitasi a08 untuk Skrabic dan Li. Dampak ke I.2, I.3, dan proposal anggota kecil. Catatan A13 (bukan keputusan tambahan): F-A07-0060, F-A05-0110, F-A05-0111, F-A05-0106 dicatat IN_PROGRESS dengan rujukan D-60; RESOLVED hanya oleh auditor penemu. F-A05-0109 (menantang D-22) tidak diputuskan D-60 dan tetap OPEN. Naskah belum diselaraskan menurut catatan A13; revisi siklus 2 (DRAF 16) sedang berjalan saat dicatat.'
approval_evidence:
  question: 'Setelah D-59, celah literatur yang tersisa di I.1 paragraf 16 adalah (a) tidak ada studi yang memeriksa kesesuaian dua dokumen tulisan tenaga kesehatan dalam satu episode, dan (c) tidak ada studi yang menjadikan kejelasan alasan dan rujukan temuan sebagai ukuran. Paragraf itu menyebut "dua di antara empat studi pada Subbab II.5" (Dietrich dan Stubbert; Zeba dkk.). Tiga auditor menemukan hal yang sama: a07 (F-A07-0060) dan a05 (F-A05-0110) menemukan Skrabic dkk. (II.5:152) juga memeriksa dokumentasi klinis secara otomatis pada 102 laporan IGD tulisan dokter dan memakai pembanding dokter, tetapi tidak disebut dan tidak dinilai terhadap celah. a05 (F-A05-0111) menemukan Li dkk. (II.6:178) menilai ketepatan bukti kutipan dengan rubrik ahli, sehingga celah (c) bertahan hanya karena dibatasi pada dua studi. a05 dan a08 menemukan celah (a) dan (c) tetap bertahan terhadap seluruh empat studi II.5. Bagaimana rumusan celah diperbaiki? Pilihan ini menyentuh klaim utama (research gap), sehingga hanya Anda yang dapat memutuskannya.'
  options_offered: ['Libatkan Skrabic dan Li, sempitkan (Recommended)', 'Nyatakan kriteria seleksi saja', 'Pertahankan, catat sebagai keterbatasan']
  user_answer: 'Libatkan Skrabic dan Li, sempitkan (Recommended)'
  answered_at: '2026-11-08'
  session_ref: 'sesi /sesi-mulai 2026-11-08 (lanjutan), AskUserQuestion Celah (a),(c)'
  scope: 'Hanya rumusan celah (a) dan (c) di I.1 paragraf 16: membahas keempat studi II.5 dan Li dkk.; celah (a) = belum ada studi yang memeriksa dua dokumen tulisan tenaga kesehatan dalam satu episode; celah (c) dipersempit pada pemeriksaan dokumentasi klinis dan menyatakan posisinya terhadap Li dkk.; rumusan masalah, tujuan, I.2-I.5 tidak berubah; D-59 tetap'
```

## D-61

```yaml
id: D-61
decision: 'Dasar kombinasi pemeriksaan (rule-based dan AI/NLP berbasis RAG) di I.1 paragraf 18 dinyatakan sebagai ketetapan rumusan capstone (Penyelarasan:35), dengan kriteria berupa penalaran penulis berlabel: pemeriksaan konsistensi CPPT dan resume medis berpotensi membutuhkan pemeriksaan terhadap kondisi yang dapat dirumuskan secara eksplisit serta penelaahan konteks informasi dalam dokumen; kombinasi dipilih untuk menguji potensi saling melengkapi, tanpa mengasumsikan kombinasi pasti lebih unggul daripada masing-masing komponen'
class: L3
status: APPROVED (lingkup terbatas; bersyarat, revisi paragraf 18 belum dijalankan)
date: '2026-11-08'
related: [Q-B1-bl, F-A05-0102, F-A05-0116, F-A07-0063, F-A05-0119, D-06, D-22, D-29, D-59, D-60, TSK-095]
basis: 'Tiga jawaban pengguna berantai (lihat approval_evidence), diteruskan A01 (brief TSK-094)'
alternatives_considered: ['Nyatakan sebagai keputusan tim (Recommended)', 'Biarkan, bawa ke tim', 'Kelemahan berbeda per komponen (Recommended)', 'Cakupan jenis ketidaksesuaian']
consequences: 'SYARAT dari pengguna: (1) sebelum merevisi paragraf 18, a08 memeriksa apakah literatur yang sudah tercantum di Bab II mendukung karakteristik masing-masing pendekatan (TSK-095); (2) hanya dukungan yang benar-benar relevan dipakai, temuan literatur dibedakan dari penalaran penulis, hasil studi terdahulu tidak digeneralisasi ke kasus CPPT-resume; (3) bila literatur belum mendukung suatu premis, kekosongan dilaporkan lebih dulu; (4) tanpa referensi baru, tanpa klaim keunggulan, tanpa pembagian jenis ketidaksesuaian tanpa persetujuan pengguna; (5) status persetujuan pembimbing tetap ditandai tertunda (Q-TEAM butir 9). Revisi paragraf 18 BELUM terjadi dan menunggu laporan a08. Q-B1-bl DIPUTUSKAN sebagian (dasar dan kriteria). Catatan A13 (bukan keputusan tambahan): status F-A05-0102, F-A05-0116, F-A07-0063 tidak diubah; hanya auditor penemu yang dapat menetapkan RESOLVED. Revisi atas pilihan ini berjalan sebagai satu perbaikan terarah atas izin pengguna karena siklus otomatis D-06 habis. Jawaban kedua pengguna hanya berupa label opsi tanpa isi kriteria; isi kriteria berasal dari jawaban ketiga.'
approval_evidence:
  steps:
  - question: 'Di Bab I DRAF 16 paragraf 18, dasar penelitian memakai kombinasi pemeriksaan (rule-based dan AI/NLP berbasis RAG) ditulis sebagai "rancangan capstone dan rumusan masalah pada Subbab I.2, bukan kelemahan studi terdahulu". Rumusan pertama capstone di Penyelarasan:35 memang menanyakan kombinasi, tanpa menetapkan mekanismenya (diverifikasi a08 dan a05). Penilaian kedua auditor berbeda. a07 menilai rumusan itu koheren dengan I.2 dan tidak mendahului keputusan. a05 (F-A05-0116) menilainya melingkar, karena rumusan I.2 menanyakan kombinasi sebab rancangan memilih kombinasi, sehingga tidak dapat menjadi alasan rancangan. a05 juga menilai kalimat itu sama dengan menjawab butir terbuka Q-B1-bl (apakah justifikasi kombinasi hanya keputusan tim, atau didukung literatur) sebelum Anda memutuskannya. a07 (F-A07-0063) menambahkan bahwa persetujuan pembimbing atas rumusan capstone masih tertunda (Q-TEAM butir 9) dan statusnya hanya ditandai di I.2. Bagaimana dasar kombinasi dinyatakan di I.1? Ini menyangkut klaim utama dan rancangan, sehingga hanya Anda yang dapat memutuskannya. Siklus revisi otomatis sudah habis (D-06), jadi revisi atas pilihan Anda berjalan sebagai satu perbaikan terarah atas izin Anda.'
    options_offered: ['Nyatakan sebagai keputusan tim (Recommended)', 'Tambahkan kriteria pilihan', 'Biarkan, bawa ke tim']
    user_answer: &a1 'Tambahkan kriteria pilihan'
  - question: 'Anda memilih menambahkan kriteria pilihan kombinasi di Bab I paragraf 18, di samping pernyataan bahwa kombinasi adalah ketetapan rumusan capstone (Penyelarasan:35). Isi kriteria itu belum ditentukan. Agar a03 tidak menciptakan kriteria sendiri, kriteria mana yang boleh ditulis sebagai penalaran penulis berlabel? Catatan dari a05 (F-A05-0119): setiap kriteria memuat premis tersembunyi. Pembagian jenis ketidaksesuaian per komponen belum ditetapkan tim (Q-TEAM butir 1), dan kelemahan Dietrich, Zeba, serta Skrabic berasal dari tugas dan data yang berbeda dari kasus CPPT-resume. Premis itu akan dinyatakan sebagai asumsi.'
    options_offered: ['Kelemahan berbeda per komponen (Recommended)', 'Cakupan jenis ketidaksesuaian', 'Saya tulis sendiri kriterianya']
    user_answer: &a2 'Saya tulis sendiri kriterianya'
  - question: 'Anda memilih menulis kriterianya sendiri, tetapi jawaban yang masuk hanya label opsi dan belum memuat isi kriteria. Saya tidak menebaknya. Yang saya butuhkan: satu atau dua kalimat dari Anda tentang mengapa pemeriksaan penelitian ini memakai kombinasi rule-based dan AI/NLP berbasis RAG. Contoh bentuknya: "Komponen X dipilih untuk Y karena Z".'
    options_offered: []
    user_answer: &a3 'Saya menetapkan kriteria pemilihan kombinasi sebagai penalaran penulis bahwa pemeriksaan konsistensi CPPT dan resume medis berpotensi membutuhkan pemeriksaan terhadap kondisi yang dapat dirumuskan secara eksplisit serta penelaahan konteks informasi dalam dokumen. Kombinasi rule-based dan AI/NLP berbasis RAG dipilih untuk menguji potensi saling melengkapi tersebut, tanpa mengasumsikan bahwa kombinasi pasti lebih unggul daripada masing-masing komponen. Sebelum merevisi paragraf 18, minta a08 memeriksa apakah literatur yang sudah tercantum dalam Bab II mendukung karakteristik masing-masing pendekatan tersebut. Gunakan hanya dukungan yang benar-benar relevan, bedakan temuan literatur dari penalaran penulis, dan jangan menggeneralisasi hasil studi terdahulu ke kasus CPPT-resume. Jika literatur yang tersedia belum mendukung suatu premis, laporkan kekosongannya terlebih dahulu. Jangan menambahkan referensi, klaim keunggulan, atau pembagian jenis ketidaksesuaian tanpa persetujuan saya. Status persetujuan pembimbing tetap ditandai sebagai tertunda.'
  user_answer: [*a1, *a2, *a3]
  answered_at: '2026-11-08'
  session_ref: 'sesi /sesi-mulai 2026-11-08 (lanjutan), AskUserQuestion "Dasar kombinasi" dan "Isi kriteria" lalu pesan teks pengguna'
  scope: 'Dasar kombinasi di I.1 paragraf 18 dinyatakan sebagai ketetapan rumusan capstone (Penyelarasan:35) dengan kriteria penalaran penulis: pemeriksaan konsistensi CPPT-resume berpotensi membutuhkan pemeriksaan kondisi yang dapat dirumuskan eksplisit serta penelaahan konteks informasi dalam dokumen; kombinasi dipilih untuk menguji potensi saling melengkapi, tanpa mengasumsikan keunggulan. SYARAT: sebelum revisi paragraf 18, a08 memeriksa dukungan literatur Bab II dan melaporkan kekosongan lebih dulu; tanpa referensi baru, tanpa klaim keunggulan, tanpa pembagian jenis ketidaksesuaian tanpa persetujuan pengguna; persetujuan pembimbing tetap ditandai tertunda; revisi paragraf 18 belum dijalankan'
```

## D-62

```yaml
id: D-62
decision: 'Klaim "diuji" di I.1 paragraf 18-19 dibatasi pada keunggulan menurut uji D-29: kalimat kriteria D-61 dipertahankan sebagai motivasi pemilihan kombinasi, tetapi yang diuji dalam penelitian ini ialah apakah presisi dan recall kombinasi lebih tinggi daripada tiap komponen; potensi saling melengkapi tidak diukur langsung; tanpa ukuran tumpang tindih atau kontribusi unik'
class: L3
status: APPROVED (lingkup terbatas)
date: '2026-11-09'
amends: 'D-61 (sebagian: bagian "menguji potensi saling melengkapi")'
related: [D-61, D-29, D-32, D-33, Q-B1-bp, F-A05-0121, F-A07-0065]
basis: 'Jawaban pengguna atas AskUserQuestion Klaim "diuji", diteruskan A01 (brief TSK-097)'
alternatives_considered: ['Tambah ukuran kontribusi unik', 'Pertahankan kata-kata D-61']
consequences: 'Deskripsi opsi (dari brief A01): klaim jujur terhadap rancangan uji dan menjawab F-A05-0121 dan F-A07-0065 tanpa menambah ukuran baru. Kata-kata D-61 berubah sedikit pada bagian "menguji potensi saling melengkapi". I.2, I.3, I.5, dan proposal anggota tidak berubah; D-29, D-32, D-33 tidak berubah. Revisi berjalan sebagai perbaikan terarah kedua (TSK-098, a03) di luar siklus D-06 atas izin pengguna. Catatan A13 (bukan keputusan tambahan): status F-A05-0121 dan F-A07-0065 tidak diubah; hanya auditor penemu yang dapat menetapkan RESOLVED. Syarat D-61 lain (tanpa referensi baru, tanpa klaim keunggulan, tanpa pembagian jenis ketidaksesuaian, persetujuan pembimbing tertunda) tetap berlaku.'
approval_evidence:
  question: 'Kriteria D-61 yang Anda tetapkan menyebut kombinasi rule-based dan AI/NLP berbasis RAG "dipilih untuk menguji potensi saling melengkapi". a05 (F-A05-0121) menilai klaim "diuji" itu tidak dioperasionalkan oleh uji D-29. Uji D-29 hanya menanyakan apakah presisi dan recall kombinasi lebih tinggi daripada masing-masing komponen. Kombinasi yang saling melengkapi tetap bisa gagal D-29, misalnya gabungan menaikkan recall tetapi menurunkan presisi. Jadi jawaban "tidak" tidak membedakan "tidak saling melengkapi" dari "saling melengkapi tetapi presisi terencerkan", dan tumpang tindih temuan per komponen tidak direncanakan di I.5. Bagaimana klaim "diuji" diperlakukan? Ini menyentuh kata-kata D-61 dan klaim utama, sehingga hanya Anda yang dapat memutuskannya. Revisi apa pun berjalan sebagai perbaikan terarah atas izin Anda.'
  options_offered: ['Batasi ke keunggulan menurut D-29 (Recommended)', 'Tambah ukuran kontribusi unik', 'Pertahankan kata-kata D-61']
  user_answer: 'Batasi ke keunggulan menurut D-29 (Recommended)'
  answered_at: '2026-11-09'
  session_ref: 'sesi /sesi-mulai 2026-11-08 (lanjutan, berlanjut 2026-11-09), AskUserQuestion Klaim "diuji"'
  scope: 'Hanya klaim "diuji" di I.1 paragraf 18-19: kalimat kriteria D-61 dipertahankan sebagai motivasi pemilihan kombinasi, tetapi frasa "diuji dalam penelitian ini" dibatasi: yang diuji ialah apakah presisi dan recall kombinasi lebih tinggi daripada tiap komponen (D-29); potensi saling melengkapi tidak diukur langsung; tanpa ukuran tumpang tindih atau kontribusi unik; kata-kata D-61 berubah sedikit pada bagian "menguji potensi saling melengkapi"; mengubah sebagian D-61, D-29/D-32/D-33 tidak berubah'
```

## D-63

```yaml
id: D-63
decision: 'Istilah kriteria D-61 ("konteks" dan "eksplisit") di I.1 paragraf 18 ditangani dengan menyatakan bahwa istilah sumber berbeda: a03 menambah satu kalimat bahwa "eksplisit" menurut Dietrich dan "konteks" menurut Li tidak identik dengan istilah kriteria, dan mengganti "tidak sejalan dengan kriteria itu" menjadi pernyataan bahwa arah temuan perlu dibandingkan hati-hati karena maknanya berbeda; kata-kata kriteria D-61 tidak diubah dan tidak ditafsirkan'
class: L3
status: APPROVED (lingkup terbatas)
date: '2026-11-09'
amends: 'D-61 (klarifikasi uraian literatur; kriteria tetap)'
related: [D-61, Q-B1-bq, F-A05-0122, F-A05-0128]
basis: 'Jawaban pengguna atas AskUserQuestion Istilah kriteria, diteruskan A01 (brief TSK-100)'
alternatives_considered: ['Hapus penilaian kesejajaran', 'Saya tetapkan maknanya sendiri']
consequences: 'Deskripsi opsi (dari brief A01): jujur terhadap perbedaan makna dan menjawab F-A05-0122 dan 0128 tanpa menetapkan definisi baru. Dampak ke I.2, I.3, dan proposal anggota tidak ada. Revisi berjalan sebagai perbaikan terarah ketiga (TSK-101, a03) di luar siklus D-06 atas izin pengguna; revisi BELUM terjadi saat dicatat. Catatan A13 (bukan keputusan tambahan): status F-A05-0122 dan F-A05-0128 tidak diubah; hanya auditor penemu yang dapat menetapkan RESOLVED. Syarat D-61 lain tetap berlaku.'
approval_evidence:
  question: 'Kriteria D-61 Anda memakai dua istilah: "kondisi yang dapat dirumuskan secara eksplisit" dan "penelaahan konteks informasi dalam dokumen". a05 menemukan (F-A05-0122 dan 0128) bahwa uraian literatur di paragraf 18 memakai kata yang sama dengan makna berbeda. Menurut Dietrich, "eksplisit" berarti kesalahan yang jelas dan mudah terlihat, sedangkan kriteria Anda berarti kondisi yang dapat dirumuskan sebagai aturan. Menurut Li, "konteks" berarti pengetahuan yang diambil dari basis eksternal, sedangkan kriteria Anda berarti informasi di dalam dokumen. Penilaian bahwa arah temuan Dietrich "tidak sejalan dengan kriteria itu" bergantung pada penyamaan itu, dan penyamaannya tidak dinyatakan. Bagaimana istilah ini ditangani? Pilihan ini menyangkut kesetiaan terhadap kriteria D-61 yang Anda tetapkan, sehingga hanya Anda yang dapat memutuskannya.'
  options_offered: ['Nyatakan istilah sumber berbeda (Recommended)', 'Hapus penilaian kesejajaran', 'Saya tetapkan maknanya sendiri']
  user_answer: 'Nyatakan istilah sumber berbeda (Recommended)'
  answered_at: '2026-11-09'
  session_ref: 'sesi /sesi-mulai 2026-11-08 (lanjutan, 2026-11-09), AskUserQuestion Istilah kriteria'
  scope: 'Hanya penanganan istilah "konteks" dan "eksplisit" di uraian literatur I.1 paragraf 18: satu kalimat bahwa istilah sumber berbeda; "tidak sejalan dengan kriteria itu" diganti pernyataan bahwa arah temuan perlu dibandingkan hati-hati karena maknanya berbeda; kata-kata kriteria D-61 tidak diubah dan tidak ditafsirkan; I.2, I.3, proposal anggota tidak berubah'
```

## D-64

```yaml
id: D-64
decision: 'Kata "secara langsung" dihapus dari kalimat D-62 di I.1 paragraf 18: "Penelitian ini tidak mengukur potensi itu secara langsung; yang diuji ialah ..." menjadi "Penelitian ini tidak mengukur potensi itu; yang diuji ialah apakah presisi dan recall kombinasi lebih tinggi ..."'
class: L3
status: APPROVED (lingkup terbatas)
date: '2026-11-09'
amends: 'D-62 (sebagian: kata "secara langsung"; perubahan kata minimum)'
related: [D-62, D-29, Q-B1-bs, F-A05-0127]
basis: 'Jawaban pengguna atas AskUserQuestion Kata D-62, diteruskan A01 (brief TSK-100)'
alternatives_considered: ['Pertahankan kata D-62', 'Tambah arti jawaban "ya"']
consequences: 'Deskripsi opsi (dari brief A01): klaim lebih akurat terhadap uji D-29 dan menjawab F-A05-0127, dengan perubahan kata minimum pada D-62. Dampak ke I.2, I.3, I.5, dan proposal anggota tidak ada. Revisi berjalan di TSK-101 (a03); BELUM terjadi saat dicatat. Catatan A13 (bukan keputusan tambahan): status F-A05-0127 tidak diubah; hanya auditor penemu.'
approval_evidence:
  question: 'Kalimat yang diputuskan lewat D-62 di paragraf 18 berbunyi "Penelitian ini tidak mengukur potensi itu secara langsung; yang diuji ialah apakah presisi dan recall kombinasi lebih tinggi daripada ...". a05 (F-A05-0127) menilai kata "secara langsung" menyiratkan bahwa potensi saling melengkapi diukur secara tidak langsung oleh uji D-29. Padahal uji itu tidak mengukurnya, baik langsung maupun tidak: jawaban "ya" hanya menunjukkan keunggulan presisi dan recall, bukan saling melengkapi. Pilihan ini mengubah kata-kata yang Anda putuskan di D-62, sehingga hanya Anda yang dapat memutuskannya. Bagaimana kalimat ini diperlakukan?'
  options_offered: ['Hapus ''secara langsung'' (Recommended)', 'Pertahankan kata D-62', 'Tambah arti jawaban "ya"']
  user_answer: 'Hapus ''secara langsung'' (Recommended)'
  answered_at: '2026-11-09'
  session_ref: 'sesi /sesi-mulai 2026-11-08 (lanjutan, 2026-11-09), AskUserQuestion Kata D-62'
  scope: 'Hanya kata "secara langsung" pada kalimat D-62 di I.1 paragraf 18; kalimat menjadi "Penelitian ini tidak mengukur potensi itu; yang diuji ialah apakah presisi dan recall kombinasi lebih tinggi ..."; I.2, I.3, I.5, proposal anggota tidak berubah'
```

## D-65

```yaml
id: D-65
decision: 'Kalimat jawaban "tidak" di I.1 paragraf 18 dilengkapi dengan struktur syarat D-29: jawaban "tidak" tidak membedakan "tidak saling melengkapi" dari "saling melengkapi tetapi hanya salah satu dari presisi atau recall yang naik"; hasil juga bergantung pada mekanisme kombinasi (D-32), tanpa memilih mekanisme'
class: L3
status: APPROVED (lingkup terbatas)
date: '2026-11-09'
related: [D-29, D-32, D-33, D-62, Q-B1-bt, F-A05-0129, F-A07-0065]
basis: 'Jawaban pengguna atas AskUserQuestion Jawaban "tidak", diteruskan A01 (brief TSK-100)'
alternatives_considered: ['Hapus kalimat itu', 'Pertahankan apa adanya']
consequences: 'Catatan: kalimat itu semula penalaran a03 atas permintaan A01 (bukan isi D-62); kini dilengkapi atas persetujuan pengguna. Deskripsi opsi (dari brief A01): akurat dan menjawab F-A05-0129, tetapi menambah satu alasan penalaran penulis yang harus diperiksa a07 dan a05 lagi. Tidak mengubah D-29, D-32, atau D-33; tanpa memilih mekanisme kombinasi. Revisi di TSK-101 (a03); BELUM terjadi saat dicatat. Catatan A13: status F-A05-0129 tidak diubah; hanya auditor penemu.'
approval_evidence:
  question: 'Di paragraf 18 ada kalimat "Jawaban ''tidak'' ... tidak serta-merta berarti kedua komponen tidak saling melengkapi karena hasilnya bergantung pula pada mekanisme kombinasi yang belum ditetapkan". Kalimat ini bukan isi keputusan Anda. Saya meminta a03 menulisnya berdasarkan rekomendasi a07. a05 (F-A05-0129) menilai alasannya salah tempat: ketidakjelasan jawaban "tidak" tetap ada walau mekanisme sudah ditetapkan, karena uji D-29 menuntut presisi dan recall sama-sama naik. Kombinasi yang menaikkan recall tetapi menurunkan presisi gagal uji itu padahal saling melengkapi. Bagaimana kalimat ini diperlakukan?'
  options_offered: ['Lengkapi dengan struktur syarat D-29 (Recommended)', 'Hapus kalimat itu', 'Pertahankan apa adanya']
  user_answer: 'Lengkapi dengan struktur syarat D-29 (Recommended)'
  answered_at: '2026-11-09'
  session_ref: 'sesi /sesi-mulai 2026-11-08 (lanjutan, 2026-11-09), AskUserQuestion Jawaban "tidak"'
  scope: 'Hanya kalimat alasan jawaban "tidak" di I.1 paragraf 18: diperluas dengan struktur syarat D-29 dan ketergantungan pada mekanisme kombinasi (D-32) tanpa memilih mekanisme; D-29, D-32, D-33 tidak berubah'
```

Catatan A13 untuk D-66 sampai D-75 (brief TSK-114, jawaban pengguna 2026-11-09 lewat AskUserQuestion): (1) [Diperbarui TSK-116: A01 melengkapi `options_offered` D-66..D-75 dengan opsi penuh; frasa "opsi lain tidak diterima A13" pada `alternatives_considered` dan `consequences` kini usang untuk daftar opsi.] (2) Keputusan yang pemutusnya "Anda dan tim" atau "Anda dan pembimbing" dicatat sebagai keputusan PENGGUNA; persetujuan tim atau pembimbing BELUM ada dan tidak dicatat sebagai telah diberikan. (3) Revisi naskah atas keputusan ini BELUM dilakukan; naskah tidak diubah pada pencatatan ini. (4) Status temuan terkait tidak diubah oleh A13; RESOLVED hanya oleh auditor penemu, REJECTED dan WAIVED hanya oleh pengguna.

## D-66

```yaml
id: D-66
decision: 'Penyusunan jawaban rumusan masalah (mengubah hasil uji menjadi jawaban "ya"/"tidak" per jenis perawatan) di I.5 digabung ke tahap evaluasi; bukan tahap tersendiri; kelima tahap I.5 tetap'
class: L3
status: APPROVED (lingkup terbatas)
date: '2026-11-09'
related: [Q-B1-ca, F-A07-0070, D-33, D-29]
basis: 'Jawaban pengguna atas AskUserQuestion Q-B1-ca, diteruskan A01 (brief TSK-114)'
alternatives_considered: ['Tahap tersendiri (tidak dipilih; daftar opsi lengkap tidak diterima A13)']
consequences: 'KOREKSI A01 atas label opsi: label "(Rekomendasi agent a07)" pada opsi yang dipilih SALAH; F-A07-0070 tidak merekomendasikan opsi apa pun (hanya requires_decision). Pilihan pengguna ditetapkan menurut isinya (digabung ke tahap evaluasi), bukan menurut label itu. Dampak yang disebut dalam pertanyaan: I.3 (syarat keberhasilan = jawaban, D-33) dan penanda di I.5 ikut terpengaruh; revisi I.5 BELUM dilakukan. Status F-A07-0070 tidak diubah (hanya auditor penemu).'
approval_evidence:
  question: 'Q-B1-ca (L3, pemutus: Anda): Apakah penyusunan jawaban rumusan masalah dijadikan tahap tersendiri di metodologi I.5? Tahap itu mengubah hasil uji menjadi jawaban ''ya''/''tidak'' per jenis perawatan (F-A07-0070). Dampak: I.3 (syarat keberhasilan = jawaban, D-33) dan penanda di I.5 ikut terpengaruh.'
  options_offered: ['Jadikan tahap tersendiri', 'Gabung ke tahap evaluasi (Rekomendasi agent a07) [opsi terpilih; label rekomendasi dikoreksi A01 sebagai salah, lihat consequences]', 'Tidak diubah, bawa ke pembimbing']
  user_answer: 'Gabung ke tahap evaluasi (Rekomendasi agent a07)'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion Q-B1-ca, diteruskan A01 (brief TSK-114)'
  scope: 'Hanya penempatan penyusunan jawaban di I.5: digabung ke tahap evaluasi (lima tahap tetap), bukan tahap tersendiri; tanpa perubahan rumusan masalah, D-29, D-33'
```

## D-67

```yaml
id: D-67
decision: 'Penanda hibrida di I.1 paragraf 20 diperlakukan sebagai keterbatasan tetap tanpa sumber hibrida: penanda diganti kalimat batas oleh penulis (BELUM dilakukan); Ijadi Maghsoodi dkk. tidak dimasukkan ke telaah; kalimat "tidak satu pun sumber yang ditelaah menyatakan bahwa satu komponen saja tidak cukup" dipertahankan'
class: L3
status: APPROVED (lingkup terbatas)
date: '2026-11-09'
related: [Q-B1-bk, D-59, F-A07-0062, F-A02-0201, F-A02-0202, F-A02-0203]
basis: 'Jawaban pengguna atas dua AskUserQuestion Q-B1-bk, diteruskan A01 (brief TSK-114)'
alternatives_considered: ['Pertanyaan 1: opsi lain tidak diterima A13', 'Pertanyaan 2: opsi lain tidak diterima A13']
consequences: 'Pertanyaan 1 ("Panggil a02 baca kedua PDF dulu (Recommended)") adalah izin tugas a02 (TSK-113), BUKAN keputusan substantif. Pertanyaan 2 memutuskan Q-B1-bk. Hasil a02 (TSK-113): tidak ada sumber yang menguji kombinasi aturan+LLM; Ijadi Maghsoodi dkk. (tinjauan naratif) hanya memberi argumen konseptual dan trade-off dengan rumusan "might" (hlm. 2, 7, 9, 10). F-A02-0201 ditangani keputusan ini (status mengikuti jawaban pengguna; tidak ditandai RESOLVED tanpa a07/a08). Rekonsiliasi referensi: penanda hibrida di naskah ada di I.1 p20 (penanda 14 dalam daftar penanda), sedangkan Q-B1-bk dan F-A07-0062 menyebut #13 di p16 (DRAF 15, lama). Penggantian penanda belum dilakukan. Menjawab tafsir D-59 untuk penanda ini (keterbatasan permanen, bukan tugas tertunda).'
approval_evidence:
  question: 'Pertanyaan 2 (pemutus: Anda): Q-B1-bk (pemutus: Anda): Setelah a02 membaca kedua PDF, tidak ada sumber yang menguji kombinasi aturan+LLM; Ijadi Maghsoodi dkk. (tinjauan naratif, hlm. 2, 7, 9, 10) hanya memberi argumen konseptual dan trade-off, dengan rumusan ''might''. Bagaimana penanda hibrida di I.1 p20 diperlakukan? | Pertanyaan 1 (izin tugas a02): Q-B1-bk: kedua PDF hibrida ada di source/16_Sistem_Hibrida_Aturan_dan_AI/ tetapi belum pernah dibaca. Bagaimana kita lanjut?'
  options_offered: ['Pertanyaan 2 (Q-B1-bk): "Keterbatasan tetap, tanpa sumber hibrida" [terpilih] | "Pakai Ijadi sebagai alasan konseptual berlabel" | "Bawa ke pembimbing, penanda tetap"', 'Pertanyaan 1 (izin a02): "Panggil a02 baca kedua PDF dulu (Recommended)" [terpilih] | "Putuskan sekarang: keterbatasan tetap" | "Putuskan sekarang: tugas belum dikerjakan"']
  user_answer: 'Pertanyaan 2: "Keterbatasan tetap, tanpa sumber hibrida". Pertanyaan 1 (izin tugas): "Panggil a02 baca kedua PDF dulu (Recommended)"'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion Q-B1-bk (dua pertanyaan berurutan), diteruskan A01 (brief TSK-114)'
  scope: 'Hanya perlakuan penanda hibrida di I.1 p20: keterbatasan tetap tanpa sumber hibrida; penanda diganti kalimat batas oleh penulis; Ijadi Maghsoodi dkk. tidak masuk telaah; kalimat "tidak satu pun sumber ..." dipertahankan; tanpa sumber baru di daftar referensi'
```

## D-68

```yaml
id: D-68
decision: 'a03 diberi izin menyunting I.2 paragraf 2 dan I.5 paragraf 4 hanya untuk menyelaraskan singkatan AI, NLP, RAG, dan LLM dengan cara I.1 memperkenalkannya; tidak ada perubahan klaim atau keputusan'
class: L2
status: APPROVED (lingkup terbatas)
date: '2026-11-09'
related: [Q-B1-br, F-A09-0154, F-A09-0126, Q-B1-bo]
basis: 'Jawaban pengguna atas AskUserQuestion Q-B1-br, diteruskan A01 (brief TSK-114)'
alternatives_considered: ['Opsi lain tidak diterima A13']
consequences: 'Izin write a03 terbatas pada singkatan di dua paragraf itu; perubahan BELUM dilakukan. I.5 paragraf 4 juga menyangkut Q-B1-bo (tetap TERBUKA; D-68 tidak memutuskannya). Status F-A09-0154 dan F-A09-0126 tidak diubah (hanya auditor penemu).'
approval_evidence:
  question: 'Q-B1-br (L2, pemutus: Anda): Apakah a03 (penulis) diberi izin menyunting I.2 paragraf 2 dan I.5 paragraf 4 untuk menyelaraskan singkatan AI, NLP, RAG, dan LLM dengan cara I.1 memperkenalkannya? Perubahan terbatas pada singkatan; tidak ada perubahan klaim atau keputusan. Catatan: I.5 paragraf 4 juga menyangkut Q-B1-bo.'
  options_offered: ['Izinkan, hanya singkatan [terpilih]', 'Jangan izinkan sekarang']
  user_answer: 'Izinkan, hanya singkatan'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion Q-B1-br, diteruskan A01 (brief TSK-114)'
  scope: 'Hanya penyelarasan singkatan AI, NLP, RAG, LLM di I.2 paragraf 2 dan I.5 paragraf 4 oleh a03; tanpa perubahan klaim atau keputusan'
```

## D-69

```yaml
id: D-69
decision: 'Data pengembangan di I.5 diberi label oleh penulis'
class: L3
status: APPROVED (keputusan pengguna; persetujuan tim BELUM ada)
date: '2026-11-09'
related: [Q-B1-bx, F-A11-0021]
basis: 'Jawaban pengguna atas AskUserQuestion Q-B1-bx, diteruskan A01 (brief TSK-114)'
alternatives_considered: ['Opsi lain tidak diterima A13 (usulan a11: tanpa label; label sebagian oleh pakar)']
consequences: 'Pemutus yang tertulis: pengguna dan tim. Pilihan ini dicatat sebagai keputusan PENGGUNA/penulis; persetujuan tim BELUM ada dan tidak boleh dianggap ada. Menjawab arah F-A11-0021 (tahap 3 tanpa acuan), tetapi rancangan I.5 BELUM direvisi dan status F-A11-0021 tidak diubah.'
approval_evidence:
  question: 'Q-B1-bx (L3; pemutus: Anda dan tim, jadi pilihan Anda tercatat sebagai keputusan penulis dan perlu disepakati tim): Bagaimana data pengembangan diberi label di I.5? Saat ini hanya data uji yang dilabeli, sehingga tahap 3 (pengembangan) tidak punya acuan (F-A11-0021).'
  options_offered: ['Tanpa label', 'Label oleh penulis [terpilih]', 'Sebagian label oleh pakar']
  user_answer: 'Label oleh penulis'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion Q-B1-bx, diteruskan A01 (brief TSK-114)'
  scope: 'Hanya pelabelan data pengembangan di I.5 oleh penulis, sebagai keputusan pengguna; persetujuan tim tertunda'
```

## D-70

```yaml
id: D-70
decision: 'Dua bagian Q-B1-by. (1/2) Kasus uji dipilih secara acak dengan benih tetap yang dicatat, terpisah untuk rawat inap dan rawat jalan (per jenis perawatan). (2/2) Temuan komponen AI (RAG) yang berada di luar daftar jenis ketidaksesuaian dihitung terpisah dan tidak masuk presisi/recall utama'
class: L3
status: APPROVED (keputusan pengguna, sebagian; persetujuan tim BELUM ada)
date: '2026-11-09'
related: [Q-B1-by, F-A05-0136, F-A05-0138, D-29]
basis: 'Jawaban pengguna atas dua AskUserQuestion Q-B1-by (1/2) dan (2/2), diteruskan A01 (brief TSK-114)'
alternatives_considered: ['Opsi lain tidak diterima A13']
consequences: 'Pemutus yang tertulis: pengguna dan tim; pilihan dicatat sebagai keputusan PENGGUNA, persetujuan tim BELUM ada. CATATAN LINGKUP: jawaban (2/2) hanya menjawab perlakuan temuan di luar daftar; bagian "apakah daftar jenis wajib memuat jenis konteks" (F-A05-0138) BELUM terjawab dan tetap TERBUKA (butir baru Q-B1-cb). Pada (1/2), kalimat "Rekomendasi saya (bukan temuan agent)" berasal dari penanya (A01), bukan temuan agent; label "(Recommended)" bukan bukti persetujuan lebih kuat. Revisi I.5 belum dilakukan. Status F-A05-0136 dan F-A05-0138 tidak diubah.'
approval_evidence:
  question: 'Q-B1-by (1/2): Bagaimana kasus uji dipilih (F-A05-0136)? Rekomendasi saya (bukan temuan agent): acak dengan benih tetap yang dicatat, terpisah untuk rawat inap dan rawat jalan. | Q-B1-by (2/2): Bagaimana temuan komponen AI (RAG) yang berada di luar daftar jenis ketidaksesuaian diperlakukan, dan apakah daftar jenis wajib memuat jenis konteks (F-A05-0136, F-A05-0138)?'
  options_offered: ['(1/2) "Acak, benih tetap, per jenis perawatan (Recommended)" [terpilih] | "Acak berstrata per jenis ketidaksesuaian" | "Berurutan". Catatan: pertanyaan awal tanpa label rekomendasi diajukan lebih dulu; pengguna bertanya "Kalau berdasarkan keadaan saat ini ...RSIA-source anda merekomendasikan apa?" (bukan keputusan), lalu dijawab pada pertanyaan berlabel ini', '(2/2) "Dihitung terpisah, tidak masuk presisi/recall utama" [terpilih] | "Dinilai penilai; yang valid dihitung benar" | "Dihitung salah (di luar daftar = tidak sah)"']
  user_answer: '(1/2) "Acak, benih tetap, per jenis perawatan (Recommended)"; (2/2) "Dihitung terpisah, tidak masuk presisi/recall utama"'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion Q-B1-by (1/2) dan (2/2), diteruskan A01 (brief TSK-114)'
  scope: '(1/2) pemilihan kasus uji: acak, benih tetap dicatat, per jenis perawatan; (2/2) HANYA perlakuan temuan RAG di luar daftar jenis: dihitung terpisah, di luar presisi/recall utama; TIDAK mencakup apakah daftar jenis wajib memuat jenis konteks (tetap terbuka); persetujuan tim tertunda'
```

## D-71

```yaml
id: D-71
decision: 'Tiap komponen (rule-based dan RAG) menyasar seluruh daftar jenis ketidaksesuaian; jenis tidak dibagi per komponen'
class: L3
status: APPROVED (keputusan pengguna; persetujuan tim BELUM ada)
date: '2026-11-09'
related: [Q-B1-bz, F-A05-0133, D-29, Q-TEAM butir 1]
basis: 'Jawaban pengguna atas AskUserQuestion Q-B1-bz, diteruskan A01 (brief TSK-114)'
alternatives_considered: ['Dibagi per komponen (tidak dipilih; daftar opsi lengkap tidak diterima A13)']
consequences: 'Pemutus yang tertulis: pengguna dan tim (Q-TEAM butir 1). Pilihan dicatat sebagai keputusan PENGGUNA; persetujuan tim BELUM ada. Menghindari hasil uji D-29 yang mudah ditebak menurut a05 (F-A05-0133) bila jenis dibagi per komponen. Revisi I.5 dan I.2 BELUM dilakukan. Status F-A05-0133 tidak diubah.'
approval_evidence:
  question: 'Q-B1-bz (L3; Anda dan tim, Q-TEAM butir 1): Apakah tiap komponen (rule-based dan RAG) menyasar seluruh daftar jenis ketidaksesuaian, atau jenisnya dibagi per komponen? a05 (F-A05-0133) menilai bila dibagi per jenis, uji recall D-29 hampir pasti ''ya'' dan uji presisi union hampir pasti ''tidak'', jadi hasil mudah ditebak sebelum diuji.'
  options_offered: ['Keduanya menyasar seluruh daftar jenis [terpilih]', 'Dibagi per jenis (rule-based untuk jenis eksplisit, RAG untuk jenis kontekstual)', 'Bawa ke tim tanpa memilih']
  user_answer: 'Keduanya menyasar seluruh daftar jenis'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion Q-B1-bz, diteruskan A01 (brief TSK-114)'
  scope: 'Hanya cakupan jenis per komponen: keduanya menyasar seluruh daftar jenis ketidaksesuaian; keputusan pengguna, persetujuan tim tertunda'
```

## D-72

```yaml
id: D-72
decision: 'D-22 dipertahankan (pembanding hanya masing-masing komponen: rule-based dan RAG), dengan syarat tambahan bahwa batas perbandingan dinyatakan eksplisit dalam proposal: penelitian tidak menyimpulkan kombinasi lebih baik dari pemeriksaan manual'
class: L3
status: APPROVED (keputusan pengguna; persetujuan pembimbing BELUM ada)
date: '2026-11-09'
related: [Q-B1-bm, F-A05-0109, D-22, D-60]
basis: 'Jawaban pengguna atas AskUserQuestion Q-B1-bm, diteruskan A01 (brief TSK-114)'
alternatives_considered: ['Tinjau ulang D-22 (tidak dipilih; daftar opsi lengkap tidak diterima A13)']
consequences: 'D-22 TIDAK berubah. Pemutus yang tertulis: pengguna dan pembimbing; persetujuan pembimbing BELUM ada. Syarat tambahan: pernyataan eksplisit batas perbandingan (tidak menyimpulkan lebih baik dari pemeriksaan manual) belum ditulis di naskah. Status F-A05-0109 tidak diubah (hanya auditor penemu).'
approval_evidence:
  question: 'Q-B1-bm (L3; Anda dan pembimbing): Masalah di I.1 adalah pemeriksaan manual, tetapi D-22 memilih pembanding hanya masing-masing komponen (rule-based, RAG). a05 (F-A05-0109) menantang ini, dan Skrabic dkk. (II.5:152) membandingkan dengan dokter. Apakah D-22 dipertahankan atau ditinjau ulang?'
  options_offered: ['Pertahankan D-22 [pilihan 1, terpilih dengan catatan pengguna]', 'Tinjau ulang: tambah pemeriksaan manual sebagai pembanding', 'Bawa ke pembimbing tanpa memilih']
  user_answer: 'pilihan 1 — Pertahankan D-22, dengan catatan bahwa batas perbandingan harus dinyatakan secara eksplisit dalam proposal.'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion Q-B1-bm, diteruskan A01 (brief TSK-114)'
  scope: 'Hanya Q-B1-bm: D-22 dipertahankan; batas perbandingan (tidak menyimpulkan lebih baik dari pemeriksaan manual) dinyatakan eksplisit; persetujuan pembimbing tertunda'
```

## D-73

```yaml
id: D-73
decision: 'Istilah Dietrich "penafsiran kontekstual" (hlm. 100) dibedakan secara eksplisit dari kriteria yang dipakai Bab I di I.1 paragraf 18-19; D-63 dipertahankan dan diperjelas'
class: L3
status: APPROVED (keputusan pengguna; persetujuan pembimbing BELUM ada)
date: '2026-11-09'
amends: 'D-63 (klarifikasi tambahan; D-63 dipertahankan)'
related: [Q-B1-bu, F-A05-0130, D-63, D-61]
basis: 'Jawaban pengguna atas AskUserQuestion Q-B1-bu, diteruskan A01 (brief TSK-114)'
alternatives_considered: ['Opsi lain tidak diterima A13']
consequences: 'Pemutus yang tertulis: pengguna, lalu pembimbing; persetujuan pembimbing BELUM ada. Pernyataan "perbandingan hati-hati" yang diumumkan tetapi tidak dijalankan (F-A05-0130) harus ditangani oleh revisi; revisi BELUM dilakukan. Kriteria D-61 tetap tidak diubah dan tidak ditafsirkan. Status F-A05-0130 tidak diubah.'
approval_evidence:
  question: 'Q-B1-bu (L3; Anda, lalu pembimbing): a05 (F-A05-0130) menantang D-63 di I.1 p18–19. Istilah Dietrich ''penafsiran kontekstual'' (hlm. 100) tidak dibedakan dari kriteria yang dipakai Bab I, dan ''perbandingan hati-hati'' diumumkan tetapi tidak dijalankan. Bagaimana ditangani?'
  options_offered: ['Bedakan istilah secara eksplisit [terpilih]', 'Hapus janji "perbandingan hati-hati" saja', 'Tinjau ulang D-63']
  user_answer: 'Bedakan istilah secara eksplisit'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion Q-B1-bu, diteruskan A01 (brief TSK-114)'
  scope: 'Hanya perbedaan istilah "penafsiran kontekstual" (Dietrich hlm. 100) dari kriteria Bab I di I.1 p18-19; D-63 dipertahankan dan diperjelas; persetujuan pembimbing tertunda'
```

## D-74

```yaml
id: D-74
decision: 'Makna "saling melengkapi" di I.1 paragraf 18 dipersempit pada jenis pemeriksaan yang berbeda (bukan hasil presisi/recall); keadaan ketiga yang juga berjawab "tidak" (komponen saling melengkapi tetapi kenaikan presisi/recall di bawah selisih minimum D-29) harus ditangani di I.3'
class: L3
status: APPROVED (keputusan pengguna; persetujuan pembimbing BELUM ada)
date: '2026-11-09'
amends: 'D-65 (sebagian: makna "saling melengkapi"; ditandai, D-65 tidak SUPERSEDED)'
related: [Q-B1-bv, F-A05-0131, D-65, D-29, D-62]
basis: 'Jawaban pengguna atas AskUserQuestion Q-B1-bv, diteruskan A01 (brief TSK-114)'
alternatives_considered: ['Opsi lain tidak diterima A13']
consequences: 'Pemutus yang tertulis: pengguna, lalu pembimbing; persetujuan pembimbing BELUM ada. Hubungan dengan D-65: mengubah/melengkapi sebagian (makna istilah), D-65 tidak dicabut. Turunan terbuka: penanganan keadaan ketiga di I.3 belum dikerjakan (butir baru Q-B1-cc). Revisi naskah BELUM dilakukan. Status F-A05-0131 tidak diubah.'
approval_evidence:
  question: 'Q-B1-bv (L3; Anda, lalu pembimbing): a05 (F-A05-0131) menantang D-65 di I.1 p18. Ada keadaan ketiga yang juga berjawab ''tidak'': komponen saling melengkapi, tetapi kenaikan presisi/recall di bawah selisih minimum D-29. Makna ''saling melengkapi'' bergeser dari jenis pemeriksaan ke hasil presisi/recall. Bagaimana ditangani?'
  options_offered: ['Nyatakan keadaan ketiga eksplisit', 'Persempit makna ''saling melengkapi'' [terpilih]', 'Bawa ke pembimbing tanpa memilih']
  user_answer: 'Persempit makna ''saling melengkapi'''
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion Q-B1-bv, diteruskan A01 (brief TSK-114)'
  scope: 'Hanya makna "saling melengkapi" di I.1 p18: dibatasi pada jenis pemeriksaan yang berbeda; keadaan ketiga ditangani di I.3 (belum dikerjakan); persetujuan pembimbing tertunda'
```

## D-75

```yaml
id: D-75
decision: 'Kenyataan bahwa kriteria pemilihan kombinasi tidak dapat diperiksa oleh penelitian maupun literatur (setelah D-62 dan D-63) dinyatakan terbuka sebagai motivasi rancangan'
class: L3
status: APPROVED (keputusan pengguna; persetujuan pembimbing BELUM ada)
date: '2026-11-09'
related: [Q-B1-bw, F-A05-0132, D-62, D-63, D-61]
basis: 'Jawaban pengguna atas AskUserQuestion Q-B1-bw, diteruskan A01 (brief TSK-114)'
alternatives_considered: ['Opsi lain tidak diterima A13']
consequences: 'Pemutus yang tertulis: pengguna, lalu pembimbing; persetujuan pembimbing BELUM ada. Pernyataan terbuka ini mencakup konsekuensi bagi simpulan (Bab V) menurut pertanyaan; rumusan tidak ditulis A13; revisi BELUM dilakukan. Status F-A05-0132 tidak diubah.'
approval_evidence:
  question: 'Q-B1-bw (L3; Anda, lalu pembimbing): Setelah D-62 dan D-63, kriteria pemilihan kombinasi tidak dapat diperiksa oleh penelitian maupun literatur (F-A05-0132). Apa konsekuensinya bagi simpulan, dan apakah hal itu dinyatakan terbuka sebagai motivasi rancangan?'
  options_offered: ['Nyatakan terbuka sebagai motivasi rancangan [terpilih]', 'Tidak dinyatakan, bawa ke pembimbing']
  user_answer: 'Nyatakan terbuka sebagai motivasi rancangan'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion Q-B1-bw, diteruskan A01 (brief TSK-114)'
  scope: 'Hanya Q-B1-bw: ketidakterujian kriteria pemilihan kombinasi dinyatakan terbuka sebagai motivasi rancangan; persetujuan pembimbing tertunda'
```

Catatan A13 untuk D-76 sampai D-80 (brief TSK-116, jawaban pengguna 2026-11-09 lewat AskUserQuestion): pemutus resmi butir-butir ini adalah TIM (dan RSIA/pembimbing). Setiap blok dicatat sebagai USUL/keputusan PENGGUNA; persetujuan tim, RSIA, atau pembimbing BELUM ada dan tidak boleh dianggap ada. Q terkait di OPEN_QUESTIONS TIDAK ditandai DIPUTUSKAN. Naskah tidak diubah. Pertanyaan balik pengguna (bukan keputusan) dicatat di `question` sebagai konteks.

## D-76

```yaml
id: D-76
decision: 'USUL PENGGUNA: rawat jalan dijawab terpisah dari rawat inap, bersyarat: hanya bila dokumen setara resume rawat jalan terbukti ada dan memadai; bila tidak, dilaporkan "tidak dapat dinilai", bukan "tidak"'
class: L3
status: APPROVED (lingkup terbatas, hanya sebagai keputusan pengguna; menunggu tim dan RSIA)
date: '2026-11-09'
related: [Q-B1-bj, Q-B1-f, Q-TEAM butir 4, D-29]
basis: 'Jawaban pengguna atas AskUserQuestion Q-B1-bj, diteruskan A01 (brief TSK-116)'
alternatives_considered: ['Rawat inap saja', 'Tunggu info RSIA']
consequences: 'Pemutus resmi: tim dan RSIA. Ini usulan pengguna, bukan keputusan tim; persetujuan tim dan RSIA BELUM ada. Q-B1-f dan Q-TEAM butir 4 (bentuk dokumen rawat jalan RSIA, "Perlu ditanyakan") tetap TERBUKA. Konteks dari A01: Penyelarasan baris 13, 49, 279 memasukkan rawat jalan ke lingkup, terbatas pada CPPT dan resume atau padanannya; baris 51 dan 350 menyatakan bentuk dokumen rawat jalan belum dipastikan. Naskah BELUM diubah.'
approval_evidence:
  question: 'Q-B1-bj (pemutus resmi: tim dan RSIA; jawaban Anda dicatat sebagai usulan pengguna, bukan keputusan tim). Penyelarasan baris 279 memasukkan rawat jalan ke lingkup tetapi bentuk dokumen rawat jalan RSIA belum dipastikan (butir 4, ''Perlu ditanyakan''). Apakah rawat jalan tetap dijawab terpisah dari rawat inap? (Konteks: pengguna lebih dulu menanyakan apakah Penyelarasan menjawab; A01 melaporkan baris 13, 49, 279 dan baris 51, 350.)'
  options_offered: ['Tetap terpisah, bersyarat (Recommended) [terpilih]', 'Rawat inap saja', 'Tunggu info RSIA']
  user_answer: 'Tetap terpisah, bersyarat (Recommended)'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion Q-B1-bj, diteruskan A01 (brief TSK-116)'
  scope: 'Hanya usulan pengguna untuk Q-B1-bj: rawat jalan dijawab terpisah secara bersyarat (tidak dapat dinilai bila dokumen setara resume tidak terbukti ada dan memadai); menunggu tim dan RSIA'
```

## D-77

```yaml
id: D-77
decision: 'USUL PENGGUNA: kombinasi rule-based dan AI berbasis RAG dibentuk sebagai union (gabungan semua temuan kedua komponen)'
class: L3
status: APPROVED (lingkup terbatas, hanya sebagai keputusan pengguna; menunggu tim)
date: '2026-11-09'
related: [Q-B1-o, D-29, D-32, D-65, D-74]
basis: 'Jawaban pengguna atas AskUserQuestion Q-B1-o, diteruskan A01 (brief TSK-116)'
alternatives_considered: ['Irisan', 'Penyaringan bertahap', 'Bawa ke tim']
consequences: 'Pemutus resmi: tim. Usulan pengguna; persetujuan tim BELUM ada. Konsekuensi yang disampaikan A01: recall kombinasi tidak mungkin di bawah komponen terbaik (jawaban recall condong "ya"), presisi dapat turun. Perlu dicek terhadap penyataan D-65/D-32 (tanpa memilih mekanisme) dan syarat D-29 (kedua arah hasil harus mungkin); A13 tidak menyelesaikan. Naskah BELUM diubah.'
approval_evidence:
  question: 'Q-B1-o (L3; pemutus resmi: tim; jawaban Anda dicatat sebagai usulan pengguna): Bagaimana kombinasi rule-based dan AI berbasis RAG dibentuk? Harus ditetapkan sebelum pengujian dan harus memungkinkan kedua arah hasil (kombinasi lebih tinggi maupun tidak daripada komponen). Kriteria D-29 sudah menyebut uji presisi/recall untuk kombinasi, sehingga cara kombinasi menentukan angka yang diuji.'
  options_offered: ['Union [terpilih]', 'Irisan', 'Penyaringan bertahap', 'Bawa ke tim']
  user_answer: 'Union (gabungan semua temuan)'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion Q-B1-o, diteruskan A01 (brief TSK-116)'
  scope: 'Hanya usulan pengguna untuk Q-B1-o: kombinasi = union; menunggu tim'
```

## D-78

```yaml
id: D-78
decision: 'USUL PENGGUNA: operator ambang memakai ">=" (selaras dengan tabel Penyelarasan baris 327-339), bukan ">" seperti di naskah; angka ambang tidak ditetapkan di sini'
class: L3
status: APPROVED (lingkup terbatas, hanya sebagai keputusan pengguna; menunggu tim/pembimbing)
date: '2026-11-09'
related: [Q-B1-q, D-19, D-29]
basis: 'Jawaban pengguna atas AskUserQuestion Q-B1-q, diteruskan A01 (brief TSK-116)'
alternatives_considered: ['">"', 'Bawa ke tim']
consequences: 'Pemutus resmi: tim/pembimbing. Usulan pengguna; persetujuan BELUM ada. Angka ambang tetap tertahan D-19. Naskah (memakai ">") BELUM diubah; ketidaksesuaian operator naskah vs tabel Penyelarasan tetap ada sampai revisi.'
approval_evidence:
  question: 'Q-B1-q (L3; pemutus resmi: tim/pembimbing; jawaban Anda dicatat sebagai usulan): Operator ambang di naskah memakai ''>'' sedangkan tabel Penyelarasan (baris 327-339) memakai ''>=''. Operator mana yang dipakai? Angka ambangnya sendiri tidak ditetapkan di sini (tertahan D-19).'
  options_offered: ['''>='' (selaras dengan tabel Penyelarasan) [terpilih]', '''>''', 'Bawa ke tim']
  user_answer: '''>='' (selaras dengan tabel Penyelarasan)'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion Q-B1-q, diteruskan A01 (brief TSK-116)'
  scope: 'Hanya usulan pengguna untuk operator ambang (>=); angka ambang tetap tertahan D-19; menunggu tim/pembimbing'
```

## D-79

```yaml
id: D-79
decision: 'USUL PENGGUNA: presisi dan recall dihitung dengan agregasi mikro (gabung semua temuan lintas kasus); nilai 0/0 dilaporkan tidak terdefinisi'
class: L3
status: APPROVED (lingkup terbatas, hanya sebagai keputusan pengguna; menunggu tim)
date: '2026-11-09'
related: [Q-B1-r, Q-B1-bg, D-19, D-29]
basis: 'Jawaban pengguna atas AskUserQuestion Q-B1-r (pertanyaan lanjutan), diteruskan A01 (brief TSK-116)'
alternatives_considered: ['Makro per jenis ketidaksesuaian', 'Minta a02 buat ringkasan agregat dulu (izin sensitive_access)']
consequences: 'Pemutus resmi: tim. Usulan pengguna; persetujuan tim BELUM ada. Rekomendasi pada pertanyaan berasal dari A01 (bukan temuan agent), berdasar Penyelarasan baris 279 (31 klaim rawat jalan satu alasan) dan belum adanya data agregat; isi RSIA-source TIDAK dibuka dan tidak ada sensitive_access diberikan. Q-B1-bg tetap terbuka (tertahan D-19 dan data agregat). Naskah BELUM diubah.'
approval_evidence:
  question: 'Pertanyaan awal: "Q-B1-r (L3; pemutus resmi: tim; jawaban Anda dicatat sebagai usulan): Cara menghitung presisi dan recall: agregasi mikro (gabung semua temuan lintas kasus) atau makro (rata-rata per kasus/jenis), dan perlakuan nilai 0/0. Bagaimana?" Jawaban pengguna berupa pertanyaan balik (bukan keputusan): "Kalau berdasarkan data C:\Users\HYPE R Series\worktrees\project-proposal-setup\RSIA-source anda merekomendasikan apa?". Pertanyaan lanjutan: "Q-B1-r (pemutus resmi: tim; jawaban Anda dicatat sebagai usulan): Cara menghitung presisi dan recall. Rekomendasi saya (bukan temuan agent): mikro, 0/0 dilaporkan tidak terdefinisi, berdasarkan Penyelarasan baris 279 (31 klaim rawat jalan satu alasan) dan belum adanya data agregat."'
  options_offered: ['Mikro; 0/0 tidak terdefinisi (Recommended) [terpilih]', 'Makro per jenis ketidaksesuaian', 'Minta a02 buat ringkasan agregat dulu (izin sensitive_access)']
  user_answer: 'Mikro; 0/0 tidak terdefinisi (Recommended)'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion Q-B1-r (dua putaran), diteruskan A01 (brief TSK-116)'
  scope: 'Hanya usulan pengguna untuk Q-B1-r: agregasi mikro, 0/0 tidak terdefinisi; menunggu tim; tanpa sensitive_access'
```

## D-80

```yaml
id: D-80
decision: 'USUL PENGGUNA: gaya sitasi akhir (K1) adalah APA (adaptasi Indonesia), selaras dengan draf Bab II Abizzar; naskah belum diubah dan format akhir tetap "perlu dikonfirmasi"'
class: L3
status: APPROVED (lingkup terbatas, hanya sebagai keputusan pengguna; menunggu tim dan pembimbing, konfirmasi pedoman prodi tetap diperlukan)
date: '2026-11-09'
related: [K1, TSK-115, F-A10 (tidak ada temuan baru)]
basis: 'Jawaban pengguna atas AskUserQuestion K1 (putaran ketiga), diteruskan A01 (brief TSK-116)'
alternatives_considered: ['Penulis-tahun sementara, tunggu pedoman', 'Numerik (IEEE)']
consequences: 'Pemutus resmi: tim dan pembimbing. Usulan pengguna; persetujuan BELUM ada. Fakta pendukung (dari laporan A01/a10, perlu verifikasi): templat TIDAK menetapkan gaya sitasi/format Daftar Pustaka pada teks badan; hanya empat contoh entri (Balabanovic, McKusick, Mitchell, Pazzani) penulis-tahun alfabetis tanpa nomor, tidak dilabeli aturan. A01 membaca hlm. 8-9 dan 20-22 PDF draf Bab II Abizzar: APA adaptasi Indonesia (di teks (Penulis, tahun), "dkk.", "&"; daftar pustaka alfabetis, indentasi menggantung, tahun dalam kurung, jurnal dan volume miring, DOI sebagai URL, "(t.t.)", "Dalam ... (Ed.)", "hlm."). Itu hanya draf satu anggota; draf Raihaan belum diperiksa. Pedoman prodi di luar templat tidak dicari. Aturan skill if4091-rules-map ("gaya sitasi akhir belum diputuskan, ikuti konvensi naskah") tetap berlaku sampai tim/pembimbing menyetujui.'
approval_evidence:
  question: 'Putaran 1: "K1 (pemutus resmi: tim dan pembimbing; jawaban Anda dicatat sebagai usulan): Gaya sitasi akhir apa yang dipakai? ..." -> pengguna: "kalau berdasarkan ...Template-Proposal-IF4091-Capstone-Individu-2026 - Copy.docx itu apa?" (bukan keputusan). Putaran 2: "K1 (...): Templat tidak menetapkan gaya sitasi; hanya empat contoh entri penulis-tahun alfabetis. Gaya sitasi apa yang Anda usulkan?" -> pengguna: "Kalau dari teman saya pada ...capstone-teammate-propose\Draft Proposal TA BAB 2 M. Abizzar Gamadrian.pdf itu gayanya apa" (bukan keputusan). Putaran 3 (menentukan): "K1 (pemutus resmi: tim dan pembimbing; jawaban Anda dicatat sebagai usulan). Draf Bab II Abizzar memakai APA adaptasi Indonesia, dan templat hanya memberi contoh penulis-tahun alfabetis tanpa menyebut gaya. Gaya sitasi apa yang Anda usulkan?"'
  options_offered: ['APA (selaras dengan Abizzar) (Recommended) [terpilih]', 'Penulis-tahun sementara, tunggu pedoman', 'Numerik (IEEE)']
  user_answer: 'APA (selaras dengan Abizzar) (Recommended)'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion K1 (tiga putaran), diteruskan A01 (brief TSK-116)'
  scope: 'Hanya usulan pengguna untuk K1: APA; menunggu tim dan pembimbing; konfirmasi pedoman prodi tetap diperlukan; naskah tidak diubah'
```

## D-81

```yaml
id: D-81
decision: 'Kalimat D-65 di I.1 p19 ("jawaban tidak tidak membedakan dua keadaan: tidak saling melengkapi, atau saling melengkapi tetapi hanya presisi/recall yang lebih tinggi") diselaraskan dengan definisi sempit "saling melengkapi" pada p18 (D-74) dan dengan keadaan ketiga (selisih di bawah minimum, I.3 p2)'
class: L3
status: APPROVED (keputusan pengguna lingkup terbatas; persetujuan pembimbing BELUM ada)
date: '2026-11-09'
amends: 'D-65 (sebagian: kalimat p19; ditandai, D-65 tidak SUPERSEDED); D-74 tetap berlaku'
related: [F-A07-0072, F-A11-0029, F-A05-0141, D-65, D-74, D-29]
basis: 'Jawaban pengguna atas AskUserQuestion F-A07-0072/F-A11-0029/F-A05-0141, diteruskan A01 (brief TSK-124)'
alternatives_considered: ['Pulihkan makna lama dan batalkan D-74', 'Biarkan, bawa ke pembimbing']
consequences: 'Rekomendasi pada opsi berasal dari A01, bukan temuan agent. Pembimbing BELUM menyetujui D-65/D-74 maupun keputusan ini. Naskah dikerjakan a03 (TSK-123, DRAF 21; belum selesai saat dicatat). Status temuan tidak diubah A13; RESOLVED hanya oleh auditor penemu.'
approval_evidence:
  question: 'F-A07-0072 / F-A11-0029 / F-A05-0141 (HIGH menurut a05; temuan sama dari tiga auditor): Kalimat D-65 di I.1 p19 ("jawaban "tidak" tidak membedakan dua keadaan: tidak saling melengkapi, atau saling melengkapi tetapi hanya presisi/recall yang lebih tinggi") bertentangan dengan definisi sempit "saling melengkapi" pada p18 (D-74) dan tidak memuat keadaan ketiga (selisih di bawah minimum, I.3 p2). Apa yang dilakukan dengan kalimat itu?'
  options_offered: ['Selaraskan p19 dengan D-74 (Recommended) [terpilih]', 'Pulihkan makna lama dan batalkan D-74', 'Biarkan, bawa ke pembimbing']
  user_answer: 'Selaraskan p19 dengan D-74 (Recommended)'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion F-A07-0072/F-A11-0029/F-A05-0141, diteruskan A01 (brief TSK-124)'
  scope: 'Hanya penyelarasan kalimat D-65 di I.1 p19 dengan D-74; D-74 tetap; pembimbing belum menyetujui'
```

## D-82

```yaml
id: D-82
decision: 'I.2 p6 memuat selisih minimum (setelah ditetapkan tim) secara bersyarat sebagai bagian syarat kedua jawaban "tidak"; I.2 menjadi satu-satunya daftar ketentuan jawaban "tidak" yang berwenang'
class: L3
status: APPROVED (keputusan pengguna lingkup terbatas; persetujuan pembimbing/tim BELUM ada)
date: '2026-11-09'
related: [F-A07-0073, F-A11-0030, F-A05-0147, D-19, D-29, D-74]
basis: 'Jawaban pengguna atas AskUserQuestion F-A07-0073/F-A11-0030/F-A05-0147, diteruskan A01 (brief TSK-124)'
alternatives_considered: ['Ubah I.3/I.5, I.2 tidak disentuh', 'Biarkan, bawa ke pembimbing']
consequences: 'Menyentuh rumusan masalah (I.2). Selisih minimum tetap tertahan D-19 (tanpa angka). Rekomendasi pada opsi dari A01, bukan temuan agent. Naskah dikerjakan a03 (TSK-123, DRAF 21). Status temuan tidak diubah A13.'
approval_evidence:
  question: 'F-A07-0073 / F-A11-0030 / F-A05-0147 (MEDIUM): Di mana daftar ketentuan jawaban "tidak" yang berwenang berada? I.2 p6 tidak memuat "selisih di bawah minimum", sedangkan I.3 p1 menyatakan ketentuan "tidak" mengikuti I.2 dan I.3 p2/I.5 p6 menambah kondisi itu secara bersyarat ("bila ditetapkan").'
  options_offered: ['Tambahkan ke I.2 p6 secara bersyarat (Recommended) [terpilih]', 'Ubah I.3/I.5, I.2 tidak disentuh', 'Biarkan, bawa ke pembimbing']
  user_answer: 'Tambahkan ke I.2 p6 secara bersyarat (Recommended)'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion F-A07-0073/F-A11-0030/F-A05-0147, diteruskan A01 (brief TSK-124)'
  scope: 'Hanya penambahan selisih minimum bersyarat ke I.2 p6 sebagai satu-satunya daftar "tidak"; tanpa angka (D-19)'
```

## D-83

```yaml
id: D-83
decision: 'Pembedaan "penafsiran kontekstual" Dietrich di I.1 p19 ditulis tanpa menafsirkan kriteria D-61 ("dalam dokumen"); istilah sumber dan kriteria dinyatakan berbeda rumusan tanpa frasa "antara dua dokumen"'
class: L3
status: APPROVED (keputusan pengguna lingkup terbatas; persetujuan pembimbing BELUM ada)
date: '2026-11-09'
related: [F-A05-0143, D-61, D-73]
basis: 'Jawaban pengguna atas AskUserQuestion F-A05-0143, diteruskan A01 (brief TSK-124)'
alternatives_considered: ['Tetapkan tafsir: "dalam dokumen" = antara dua dokumen', 'Bawa ke pembimbing, kalimat dihapus sementara']
consequences: 'D-73 dipertahankan; kriteria D-61 tidak ditafsirkan. Rekomendasi pada opsi dari A01, bukan temuan agent. Naskah dikerjakan a03 (TSK-123, DRAF 21). Status F-A05-0143 tidak diubah A13.'
approval_evidence:
  question: 'F-A05-0143 (HIGH): Pembedaan "penafsiran kontekstual" Dietrich di I.1 p19 menafsirkan kriteria D-61 ("dalam dokumen") sebagai "antara dua dokumen", padahal D-73 menyatakan D-61 tidak ditafsirkan. Bagaimana pembedaan itu ditulis?'
  options_offered: ['Tanpa menafsirkan D-61 (Recommended) [terpilih]', 'Tetapkan tafsir: "dalam dokumen" = antara dua dokumen', 'Bawa ke pembimbing, kalimat dihapus sementara']
  user_answer: 'Tanpa menafsirkan D-61 (Recommended)'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion F-A05-0143, diteruskan A01 (brief TSK-124)'
  scope: 'Hanya cara menulis pembedaan Dietrich di I.1 p19 tanpa menafsirkan D-61'
```

## D-84

```yaml
id: D-84
decision: 'Simpulan I.1 p21 dibatasi ke konfigurasi yang diuji (tiga konfigurasi) sehingga "terbaik" memiliki pembanding yang disebut; tingkat dukungan literatur terhadap kriteria dinyatakan satu tingkat yang konsisten'
class: L3
status: APPROVED (keputusan pengguna lingkup terbatas; persetujuan pembimbing BELUM ada)
date: '2026-11-09'
related: [F-A05-0145, D-75, D-61]
basis: 'Jawaban pengguna atas AskUserQuestion F-A05-0145, diteruskan A01 (brief TSK-124)'
alternatives_considered: ['Biarkan, bawa ke pembimbing']
consequences: 'D-75 dipertahankan dan diperjelas. Rekomendasi pada opsi dari A01, bukan temuan agent. Naskah dikerjakan a03 (TSK-123, DRAF 21). Status F-A05-0145 tidak diubah A13.'
approval_evidence:
  question: 'F-A05-0145 (MEDIUM): I.1 p21 menyatakan simpulan "tidak akan menyatakan kombinasi merupakan pilihan terbaik", tetapi jawaban "ya" pertanyaan 1 berarti kombinasi lebih tinggi daripada kedua komponen, yaitu terbaik di antara tiga konfigurasi. Pembandingnya juga tidak disebut, dan tingkat dukungan literatur terhadap kriteria dinyatakan tidak konsisten ("terbatas" di p18, "tidak diperiksa/tidak didukung" di p19 dan p21). Bagaimana ditangani?'
  options_offered: ['Batasi ke konfigurasi yang diuji (Recommended) [terpilih]', 'Biarkan, bawa ke pembimbing']
  user_answer: 'Batasi ke konfigurasi yang diuji (Recommended)'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion F-A05-0145, diteruskan A01 (brief TSK-124)'
  scope: 'Hanya pembatasan simpulan p21 ke konfigurasi yang diuji dan satu tingkat dukungan literatur'
```

## D-85

```yaml
id: D-85
decision: 'Kalimat batas di I.1 p20 ("Tidak satu pun sumber yang ditelaah menguji kombinasi pemeriksaan berbasis aturan dan model bahasa besar pada pemeriksaan dokumen") dinyatakan dengan cakupan "sumber yang ditelaah" dan sifat penelusuran yang tidak sistematis'
class: L3
status: APPROVED (keputusan pengguna lingkup terbatas; persetujuan pembimbing BELUM ada)
date: '2026-11-09'
related: [F-A05-0146, F-A08-0102, D-67]
basis: 'Jawaban pengguna atas AskUserQuestion F-A05-0146, diteruskan A01 (brief TSK-124)'
alternatives_considered: ['Biarkan seperti DRAF 20']
consequences: 'Menyentuh D-67 (dipertahankan dan diperjelas). Menurut a08 klaim tidak terbantahkan oleh sumber yang dikutip, tetapi bukan negatif terverifikasi; istilah "model bahasa besar" membuat Zeba (aturan + encoder) tidak tercakup (F-A08-0101). Rekomendasi pada opsi dari A01, bukan temuan agent. Pertanyaan a05 tentang cakupan "sumber yang ditelaah" (Bab II DRAFT 6 saja, lima studi p16, atau juga II.4 lama) dicatat di Q-B1-cg. Naskah dikerjakan a03 (TSK-123, DRAF 21). Status temuan tidak diubah A13.'
approval_evidence:
  question: 'F-A05-0146 (MEDIUM; menyentuh D-67): Kalimat batas di I.1 p20 ("Tidak satu pun sumber yang ditelaah menguji kombinasi pemeriksaan berbasis aturan dan model bahasa besar pada pemeriksaan dokumen") mencerminkan cara sumber dipilih. Cakupan "sumber yang ditelaah" tidak didefinisikan, penelusurannya tidak sistematis, dan istilah "model bahasa besar" membuat Zeba (aturan + encoder) tidak tercakup. a08 menilai klaimnya tidak terbantahkan oleh sumber yang dikutip, tetapi bukan negatif yang terverifikasi. Bagaimana ditangani?'
  options_offered: ['Nyatakan cakupan dan sifat tidak sistematis (Recommended) [terpilih]', 'Biarkan seperti DRAF 20']
  user_answer: 'Nyatakan cakupan dan sifat tidak sistematis (Recommended)'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion F-A05-0146, diteruskan A01 (brief TSK-124)'
  scope: 'Hanya pernyataan cakupan dan sifat tidak sistematis pada kalimat batas I.1 p20'
```

## D-86

```yaml
id: D-86
decision: 'Kalimat penutup I.1 p19 ("Tidak satu pun studi yang ditelaah menguji model bahasa besar atau RAG untuk menelaah konteks antara dua dokumen yang ditulis tenaga kesehatan") berfungsi sebagai pengulangan celah pertama, bukan sebagai batas dukungan kriteria D-61 dan bukan dasar p21'
class: L3
status: APPROVED (keputusan pengguna lingkup terbatas; persetujuan pembimbing BELUM ada)
date: '2026-11-09'
related: [F-A07-0077, F-A05-0153, F-A09-0211, D-61, D-83]
basis: 'Jawaban pengguna atas AskUserQuestion F-A07-0077 / F-A05-0153, diteruskan A01 (brief TSK-131)'
alternatives_considered: ['Hapus kalimat itu', 'Tetapkan tafsir: dalam dokumen mencakup antara dua dokumen']
consequences: 'Kalimat berfungsi sebagai pernyataan celah pertama, tidak dipakai sebagai batas dukungan kriteria D-61 dan tidak menjadi dasar p21; D-61 tidak ditafsirkan; D-83 dipertahankan. Rekomendasi pada opsi terpilih dari A01, bukan temuan agent. Menurut a08 klaim kalimat itu benar menurut sumber. Naskah dikerjakan a03 (TSK-130, DRAF 22); status F-A07-0077, F-A05-0153, F-A09-0211 tidak diubah A13.'
approval_evidence:
  question: 'F-A07-0077 / F-A05-0153 (MEDIUM; temuan sama dari a07 dan a05): Kalimat penutup I.1 p19 ("Tidak satu pun studi yang ditelaah menguji model bahasa besar atau RAG untuk menelaah konteks antara dua dokumen yang ditulis tenaga kesehatan") berada di bawah topik "Untuk penelaahan konteks" dan menjadi dasar p21, sehingga tersirat memetakan "dalam dokumen" (D-61) ke "antara dua dokumen", tafsir yang ditolak D-83. Menurut a08, klaimnya sendiri benar menurut sumber. Apa fungsi kalimat itu?'
  options_offered: ['Pengulangan celah pertama, bukan batas dukungan (Recommended) [terpilih]', 'Hapus kalimat itu', 'Tetapkan tafsir: dalam dokumen mencakup antara dua dokumen']
  user_answer: 'Pengulangan celah pertama, bukan batas dukungan (Recommended)'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion F-A07-0077 / F-A05-0153, diteruskan A01 (brief TSK-131)'
  scope: 'Hanya fungsi kalimat penutup I.1 p19 (pengulangan celah pertama; bukan batas dukungan D-61, bukan dasar p21)'
```
