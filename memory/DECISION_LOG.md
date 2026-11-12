---
file: DECISION_LOG
revision: 43
status: CURRENT
updated: 2026-11-12
updated_by: a13-memory-manager
based_on_commit: 80a13ba
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
status: SUPERSEDED by D-106 (sebagian, batas siklus 2 menjadi 1, aturan lain D-06 tetap)
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
status: SUPERSEDED by D-111 (sebagian, sumber kebenaran Bab I kini docx resmi, sisa D-49 tentang modular/ tetap tercatat)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (lingkup terbatas)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (lingkup terbatas)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (lingkup terbatas; bersyarat, revisi paragraf 18 belum dijalankan)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (lingkup terbatas)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (lingkup terbatas)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (lingkup terbatas)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (lingkup terbatas)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (lingkup terbatas)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (lingkup terbatas)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (lingkup terbatas)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna; persetujuan tim BELUM ada)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna, sebagian; persetujuan tim BELUM ada)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna; persetujuan tim BELUM ada)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna; persetujuan pembimbing BELUM ada)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna; persetujuan pembimbing BELUM ada)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna; persetujuan pembimbing BELUM ada)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna; persetujuan pembimbing BELUM ada)
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
status: SUPERSEDED by D-113 (sebagian, usulan APA menjadi keputusan pengguna sementara)
status_sebelumnya: APPROVED (lingkup terbatas, hanya sebagai keputusan pengguna; menunggu tim dan pembimbing, konfirmasi pedoman prodi tetap diperlukan)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna lingkup terbatas; persetujuan pembimbing BELUM ada)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna lingkup terbatas; persetujuan pembimbing/tim BELUM ada)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna lingkup terbatas; persetujuan pembimbing BELUM ada)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna lingkup terbatas; persetujuan pembimbing BELUM ada)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna lingkup terbatas; persetujuan pembimbing BELUM ada)
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
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna lingkup terbatas; persetujuan pembimbing BELUM ada)
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

Catatan D-87..D-97 (2026-11-09, brief A01 memory_op record_decisions): semua adalah keputusan PENGGUNA berlingkup terbatas melalui AskUserQuestion, BUKAN persetujuan tim, pembimbing, atau RSIA. Pertanyaan yang di brief A01 diringkas dengan tanda "..." dicatat apa adanya (kutipan A01, bukan teks penuh). Keterangan lisan RSIA pada D-90 adalah pernyataan yang belum terverifikasi. Rekomendasi pada opsi (bila ada) berasal dari A01, bukan temuan agent.

## D-87

```yaml
id: D-87
decision: 'D-74 dipertahankan; keberatan auditor tentang istilah "saling melengkapi" (bagian empiris dan hasil bergantung pada cara kombinasi) dinyatakan di Bab I sebagai keterbatasan'
class: L3
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna lingkup terbatas; persetujuan tim/pembimbing BELUM ada)
date: '2026-11-09'
related: [Q-B1-cm, F-A05-0152, F-A11-0038, D-74, D-81, D-65]
basis: 'Jawaban pengguna atas AskUserQuestion butir 1 dari 2.3, diteruskan A01'
alternatives_considered: ['Hapus istilah "saling melengkapi" dari naskah', 'Jadikan bagian empiris yang diukur']
consequences: 'Q-B1-cm: F-A05-0152 dan F-A11-0038 dijawab penulis; D-74 dan D-81 tetap MENUNGGU PEMBIMBING. Status temuan tidak diubah A13 (RESOLVED hanya oleh auditor penemu). Naskah belum diubah pada pencatatan ini.'
approval_evidence:
  question: 'Butir 1 dari 2.3. Auditor a05 (F-A05-0152) dan a11 (F-A11-0038) keberatan: "saling melengkapi" juga punya bagian empiris dan hasilnya bergantung pada cara kombinasi, padahal naskah (D-74, D-81) menyebutnya sifat rancangan yang tidak diukur. Bagaimana istilah itu diperlakukan di Bab I?'
  options_offered: ['Pertahankan D-74, nyatakan keberatan sebagai keterbatasan [terpilih]', 'Hapus istilah "saling melengkapi" dari naskah', 'Jadikan bagian empiris yang diukur']
  user_answer: 'Pertahankan D-74, nyatakan keberatan sebagai keterbatasan'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion butir 1 dari 2.3, diteruskan A01 (brief memory_op record_decisions)'
  scope: 'Hanya perlakuan istilah "saling melengkapi" di Bab I (D-74 dipertahankan; keberatan menjadi keterbatasan)'
```

## D-88

```yaml
id: D-88
decision: 'Pada tahap pertama, ketersediaan dokumen rawat jalan yang setara resume medis dinilai "ada dan memadai" oleh penulis dengan kriteria tertulis; hasil penilaian dilaporkan ke tim'
class: L3
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna lingkup terbatas; persetujuan tim/pembimbing/RSIA BELUM ada)
date: '2026-11-09'
related: [Q-B1-cn, F-A05-0157, F-A11-0033, D-76, Q-B1-f]
basis: 'Jawaban pengguna atas AskUserQuestion butir 2 dari 2.3, diteruskan A01'
alternatives_considered: ['Tetap penanda: ditetapkan tim dan RSIA', 'Tanpa penilaian memadai; cukup "ada"']
consequences: 'Isi kriteria tertulis belum ditetapkan (harus dirumuskan penulis, tidak dikarang A13). Tidak menetapkan bentuk dokumen rawat jalan RSIA (Q-B1-f tetap terbuka). Status temuan tidak diubah A13.'
approval_evidence:
  question: 'Butir 2 dari 2.3 (Q-B1-cn, F-A05-0157). Di tahap pertama, bagaimana ketersediaan dokumen rawat jalan yang setara resume medis dinilai "ada dan memadai"?'
  options_offered: ['Penulis menilai dengan kriteria tertulis, hasil ke tim [terpilih]', 'Tetap penanda: ditetapkan tim dan RSIA', 'Tanpa penilaian memadai; cukup "ada"']
  user_answer: 'Penulis menilai dengan kriteria tertulis, hasil ke tim'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion butir 2 dari 2.3, diteruskan A01'
  scope: 'Hanya pelaku dan cara penilaian ketersediaan dokumen rawat jalan di tahap pertama'
```

## D-89

```yaml
id: D-89
decision: 'Ambang, selisih minimum, dan satuan hitung dinyatakan di I.2/I.3 sebagai prosedur tanpa angka: ditetapkan sebelum pengujian'
class: L3
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna lingkup terbatas; persetujuan tim/pembimbing BELUM ada)
date: '2026-11-09'
related: [D-19, Q-B1-bg, Q-B1-q, Q-B1-cc, D-82, D-78]
basis: 'Jawaban pengguna atas AskUserQuestion butir 3 dari 2.3, diteruskan A01'
alternatives_considered: ['Saya (pengguna) tetapkan angka sekarang', 'Pembanding relatif saja: tanpa ambang absolut']
consequences: 'Tidak ada angka ditetapkan; D-19 (angka klaim pending) tidak diubah. Operator dan bentuk selisih tidak diputuskan. Q-B1-bg dan Q-B1-q tetap menunggu tim/pembimbing untuk angka.'
approval_evidence:
  question: 'Butir 3 dari 2.3 (D-19; Q-B1-bg, q, cc). Bagaimana ambang, selisih minimum, dan satuan hitung dinyatakan di I.2/I.3 supaya rumusan masalah dapat dijawab? ... (teks diringkas pada brief A01)'
  options_offered: ['Prosedur tanpa angka: ditetapkan sebelum pengujian [terpilih]', 'Saya (pengguna) tetapkan angka sekarang', 'Pembanding relatif saja: tanpa ambang absolut']
  user_answer: 'Prosedur tanpa angka: ditetapkan sebelum pengujian'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion butir 3 dari 2.3, diteruskan A01'
  scope: 'Hanya bentuk pernyataan ambang, selisih minimum, dan satuan hitung di I.2/I.3 (prosedur tanpa angka)'
```

## D-90

```yaml
id: D-90
decision: 'Naskah tidak mengasumsikan CPPT dan resume medis sama-sama dikunci setelah pelayanan selesai; berdasarkan keterangan lisan RSIA (disampaikan lewat penulis, belum terkonfirmasi) CPPT yang tercatat tidak dapat diubah dan resume medis masih dapat direvisi; satuan hitung rawat inap adalah satu episode (masuk hingga keluar dan resume episode itu diajukan), resume episode sebelumnya tidak dihitung kembali'
class: L3
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna lingkup terbatas; persetujuan tim/pembimbing BELUM ada; keterangan RSIA belum terverifikasi)
date: '2026-11-09'
related: [Q-B1-ba, D-55, D-56, D-57, D-21, F-A05-0024, F-A11-0004, Q-TEAM butir 5]
basis: 'Jawaban teks bebas pengguna atas AskUserQuestion butir 4 dari 2.3, diteruskan A01'
alternatives_considered: ['Nyatakan dua tafsir, kesimpulan dibatasi', 'Ikuti dokumen tim', 'Ikuti keterangan RSIA']
consequences: 'Pengguna menjawab dengan teks bebas, bukan memilih salah satu opsi. Keterangan RSIA tetap pernyataan yang perlu dikonfirmasi, bukan fakta RSIA terverifikasi. Berlaku untuk rawat inap saja. Konflik sumber Q-B1-ba dengan dokumen tim tidak diselesaikan A13; naskah (I.1 baris 75/89 dan I.4 p6) perlu diselaraskan penulis. Konfirmasi RSIA tetap diperlukan.'
approval_evidence:
  question: 'Butir 4 dari 2.3 (Q-B1-ba). Dokumen tim mengandaikan CPPT dan resume medis dikunci setelah pelayanan selesai, sedangkan keterangan lisan RSIA (lewat Anda, belum terverifikasi) berbeda. Bagaimana Bab I menyatakannya?'
  options_offered: ['Nyatakan dua tafsir, kesimpulan dibatasi', 'Ikuti dokumen tim', 'Ikuti keterangan RSIA']
  user_answer: 'Naskah tidak mengasumsikan bahwa CPPT dan resume medis sama-sama dikunci setelah pelayanan selesai. Berdasarkan keterangan lisan RSIA yang disampaikan melalui penulis dan masih perlu dikonfirmasi, CPPT yang telah tercatat tidak dapat diubah, sedangkan resume medis masih dapat direvisi. Penghitungan dilakukan berdasarkan satu episode rawat inap, sejak pasien masuk hingga pasien keluar dan resume medis untuk episode tersebut diajukan. Resume dari episode sebelumnya tidak dihitung kembali sebagai bagian dari episode yang sedang dievaluasi.'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion butir 4 dari 2.3 (jawaban teks bebas), diteruskan A01'
  scope: 'Hanya cara Bab I menyatakan penguncian CPPT/resume medis dan satuan hitung episode rawat inap'
```

## D-91

```yaml
id: D-91
decision: '"Rawat jalan terbatas" di I.4 dinyatakan sebagai cakupan bersyarat, tanpa definisi baru'
class: L3
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna lingkup terbatas; persetujuan tim/RSIA BELUM ada)
date: '2026-11-09'
related: [Q-B1-f, Q-TEAM butir 4, D-21, D-76, D-88]
basis: 'Jawaban pengguna atas AskUserQuestion butir 5 dari 2.3, diteruskan A01'
alternatives_considered: ['Samakan satuan dengan rawat inap', 'Keluarkan rawat jalan dari Bab I']
consequences: 'Batas operasional dan bentuk dokumen rawat jalan RSIA tetap tidak ditetapkan; Q-B1-f dan Q-TEAM butir 4 tetap terbuka.'
approval_evidence:
  question: 'Butir 5 dari 2.3 (Q-B1-f, Q-TEAM butir 4). ... Apa batas "rawat jalan terbatas" di I.4 dan bentuk dokumen rawat jalan di RSIA? (teks diringkas pada brief A01)'
  options_offered: ['Nyatakan sebagai cakupan bersyarat, tanpa definisi baru [terpilih]', 'Samakan satuan dengan rawat inap', 'Keluarkan rawat jalan dari Bab I']
  user_answer: 'Nyatakan sebagai cakupan bersyarat, tanpa definisi baru'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion butir 5 dari 2.3, diteruskan A01'
  scope: 'Hanya cara I.4 menyatakan "rawat jalan terbatas" (cakupan bersyarat tanpa definisi baru)'
```

## D-92

```yaml
id: D-92
decision: 'Bab I memakai judul baru dari dokumen penyelarasan tim (30 Oktober), ditandai sebagai usulan; K2 tetap menunggu persetujuan pembimbing'
class: L3
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna lingkup terbatas; persetujuan pembimbing BELUM ada)
date: '2026-11-09'
related: [K2, Q-TEAM butir 9]
basis: 'Jawaban pengguna atas AskUserQuestion butir 6 dari 2.3, diteruskan A01'
alternatives_considered: ['Pakai judul yang berlaku di naskah, K2 tetap terbuka']
consequences: 'K2 tetap MENUNGGU PEMBIMBING; judul dan empat rumusan masalah capstone belum disetujui pembimbing. Draf individu pengguna tidak diubah.'
approval_evidence:
  question: 'Butir 6 dari 2.3 (K2, Q-TEAM butir 9). Judul baru di dokumen penyelarasan tim (30 Oktober) dan empat rumusan masalah capstone menunggu persetujuan pembimbing ... Apa yang dipakai Bab I sekarang? (teks diringkas pada brief A01)'
  options_offered: ['Pakai judul yang berlaku di naskah, K2 tetap terbuka', 'Pakai judul baru dari dokumen penyelarasan, ditandai usulan [terpilih]']
  user_answer: 'Pakai judul baru dari dokumen penyelarasan, ditandai usulan'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion butir 6 dari 2.3, diteruskan A01'
  scope: 'Hanya judul yang dipakai Bab I sekarang (judul baru, ditandai usulan); K2 tidak diputuskan'
```

## D-93

```yaml
id: D-93
decision: 'Aturan sebelum uji: bila plafon menghalangi pembedaan, hasil dinyatakan "tidak dapat dinilai"'
class: L3
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna lingkup terbatas; persetujuan tim/pembimbing BELUM ada); urutan penilaian DIUBAH sebagian oleh D-98 (2026-11-10)
date: '2026-11-09'
related: [F-A11-0015, F-A11-0016, Q-B1-bg, D-89]
basis: 'Jawaban pengguna atas AskUserQuestion butir 7 dari 2.3, diteruskan A01'
alternatives_considered: ['Nyatakan sebagai keterbatasan saja', 'Tetap penanda untuk tim dan pembimbing']
consequences: 'Kondisi plafon yang tepat (ambang) tidak ditetapkan; angka tetap tertahan D-19. Status F-A11-0015 (HIGH) dan F-A11-0016 tidak diubah A13. Konfirmasi pengguna atas isian a03 di TO DO.md (pemutus butir 7 dan 10) BELUM ada.'
approval_evidence:
  question: 'Butir 7 dari 2.3 (F-A11-0015 HIGH, F-A11-0016). ... Bagaimana naskah menanganinya? (teks diringkas pada brief A01)'
  options_offered: ['Aturan sebelum uji: hasil "tidak dapat dinilai" bila plafon [terpilih]', 'Nyatakan sebagai keterbatasan saja', 'Tetap penanda untuk tim dan pembimbing']
  user_answer: 'Aturan sebelum uji: hasil "tidak dapat dinilai" bila plafon'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion butir 7 dari 2.3, diteruskan A01'
  scope: 'Hanya penanganan plafon (F-A11-0015, F-A11-0016): aturan sebelum uji, hasil "tidak dapat dinilai"'
```

## D-94

```yaml
id: D-94
decision: 'Lima pertentangan antarusulan untuk butir tim diselesaikan sebagai satu paket konsisten, ditandai usulan penulis: satuan episode; agregasi mikro atas episode; 0/0 tidak terdefinisi menjadi "tidak dapat dinilai"; union dengan catatan recall; seluruh jenis ketidaksesuaian tetap usulan'
class: L3
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna lingkup terbatas, bersifat usulan penulis; persetujuan tim/pembimbing BELUM ada); butir 3 (0/0) DIUBAH oleh D-98 dan butir union DILENGKAPI oleh D-99 (2026-11-10)
date: '2026-11-09'
related: [F-A11-0023, F-A11-0024, F-A11-0025, F-A11-0026, F-A11-0027, F-A05-0150, D-72, D-79, D-81]
basis: 'Jawaban pengguna atas AskUserQuestion butir 8 dari 2.3, diteruskan A01'
alternatives_considered: ['Biarkan semua tetap penanda untuk tim']
consequences: 'Paket adalah usulan penulis, bukan keputusan tim. Pembanding manual tetap D-72 (tidak berubah); K1 tetap D-80. Isi paket menurut keterangan A01. Status temuan tidak diubah A13.'
approval_evidence:
  question: 'Butir 8 dari 2.3, lima pertentangan antarusulan untuk butir tim (F-A11-0023..0027, F-A05-0150). Bagaimana naskah menyelesaikannya?'
  options_offered: ['Satu paket konsisten, ditandai usulan penulis [terpilih]', 'Biarkan semua tetap penanda untuk tim']
  user_answer: 'Satu paket konsisten, ditandai usulan penulis'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion butir 8 dari 2.3, diteruskan A01'
  scope: 'Hanya penyelesaian lima pertentangan antarusulan sebagai satu paket usulan penulis'
```

## D-95

```yaml
id: D-95
decision: 'Temuan Dietrich hanya dipakai sebagai latar; kriteria pemilihan kombinasi tetap umum (tidak dibedakan per pasangan komponen) dengan urutan dinyatakan'
class: L3
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna lingkup terbatas; persetujuan pembimbing BELUM ada)
date: '2026-11-09'
related: [Q-B1-ce, Q-B1-cf, F-A05-0142, F-A05-0144, D-61, D-73]
basis: 'Jawaban pengguna atas AskUserQuestion butir 9 dari 2.3, diteruskan A01'
alternatives_considered: ['Kriteria dibedakan per pasangan komponen', 'Tetap penanda untuk pembimbing']
consequences: 'D-61 tidak diubah. Status temuan tidak diubah A13.'
approval_evidence:
  question: 'Butir 9 dari 2.3. Bagaimana temuan Dietrich dipakai, dan apakah kriteria pemilihan kombinasi perlu membedakan pasangan komponen? ... (teks diringkas pada brief A01)'
  options_offered: ['Dietrich hanya latar; kriteria tetap umum, urutan dinyatakan [terpilih]', 'Kriteria dibedakan per pasangan komponen', 'Tetap penanda untuk pembimbing']
  user_answer: 'Dietrich hanya latar; kriteria tetap umum, urutan dinyatakan'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion butir 9 dari 2.3, diteruskan A01'
  scope: 'Hanya fungsi rujukan Dietrich (latar) dan sifat umum kriteria pemilihan kombinasi'
```

## D-96

```yaml
id: D-96
decision: 'Cakupan literatur dirumuskan dengan satu istilah cakupan, didefinisikan sekali di I.1, dan alasan Zhang dinyatakan satu kalimat'
class: L3
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna lingkup terbatas; persetujuan pembimbing BELUM ada)
date: '2026-11-09'
related: [Q-B1-cg, F-A07-0087, F-A09-0235, F-A05-0154, D-85, D-86]
basis: 'Jawaban pengguna atas AskUserQuestion butir 10 dari 2.3, diteruskan A01'
alternatives_considered: ['Biarkan dua sebutan seperti sekarang']
consequences: 'Isi definisi cakupan tidak ditetapkan di sini (dirumuskan penulis). D-85 dan D-86 dipertahankan. Konfirmasi pengguna atas isian a03 di TO DO.md (pemutus butir 7 dan 10) BELUM ada. Status temuan tidak diubah A13.'
approval_evidence:
  question: 'Butir 10 dari 2.3 (Q-B1-cg; F-A07-0087, F-A09-0235). ... Bagaimana cakupan itu dirumuskan? (teks diringkas pada brief A01)'
  options_offered: ['Satu istilah cakupan, definisi sekali di I.1, alasan Zhang satu kalimat [terpilih]', 'Biarkan dua sebutan seperti sekarang']
  user_answer: 'Satu istilah cakupan, definisi sekali di I.1, alasan Zhang satu kalimat'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion butir 10 dari 2.3, diteruskan A01'
  scope: 'Hanya perumusan cakupan literatur (satu istilah, definisi sekali di I.1, alasan Zhang satu kalimat)'
```

## D-97

```yaml
id: D-97
decision: 'Pasangan ibu dan bayi: satu episode = satu unit; pasangan tidak dipisah antar-bagian pada pembagian data'
class: L3
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna lingkup terbatas; persetujuan tim BELUM ada)
date: '2026-11-09'
related: [Q-TEAM butir 6, D-90, D-94]
basis: 'Jawaban pengguna atas AskUserQuestion butir terakhir (bagian 3), diteruskan A01'
alternatives_considered: ['Tetap penanda untuk tim']
consequences: 'Tim belum menyetujui; pemilik penautan ibu-bayi menurut Penyelarasan belum dikonfirmasi.'
approval_evidence:
  question: 'Butir terakhir yang perlu keputusan (bagian 3, Q-TEAM butir 6): bagaimana pasangan ibu dan bayi diperlakukan pada pembagian data?'
  options_offered: ['Satu episode = satu unit; pasangan tidak dipisah antar-bagian [terpilih]', 'Tetap penanda untuk tim']
  user_answer: 'Satu episode = satu unit; pasangan tidak dipisah antar-bagian'
  answered_at: '2026-11-09'
  session_ref: 'sesi 2026-11-09, AskUserQuestion butir terakhir (bagian 3), diteruskan A01'
  scope: 'Hanya perlakuan pasangan ibu-bayi pada pembagian data (satu episode = satu unit)'
```

Catatan D-98..D-100 (2026-11-10, brief A01 memory_op record_decisions): keputusan PENGGUNA lingkup terbatas melalui AskUserQuestion, BUKAN persetujuan tim, pembimbing, atau RSIA. Pertanyaan dan deskripsi opsi yang di brief A01 diringkas dengan tanda "..." dicatat apa adanya (kutipan A01, bukan teks penuh). Rekomendasi pada opsi berasal dari A01.

## D-98

```yaml
id: D-98
decision: 'Urutan penilaian di I.2/I.3: syarat pertama dinilai lebih dulu; "tidak dapat dinilai" hanya untuk syarat kedua; 0/0 pada penyebut presisi kombinasi dihitung sebagai syarat pertama gagal'
class: L3
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna lingkup terbatas; persetujuan tim/pembimbing BELUM ada)
date: '2026-11-10'
related: [F-A07-0090, F-A07-0091, F-A11-0041, F-A11-0048, F-A11-0049, D-93, D-94, D-79]
basis: 'Jawaban pengguna atas AskUserQuestion (temuan a07 dan a11 atas paket D-94/D-93), diteruskan A01'
alternatives_considered: ['Pertahankan paket D-94 apa adanya', 'Bawa ke tim, naskah memuat penanda saja']
consequences: 'MENGUBAH D-94 butir 3 (0/0 menjadi "tidak dapat dinilai") dan sebagian D-93 (urutan penilaian). Menjawab F-A11-0048 (konflik dengan D-94 butir 3) sebagai keputusan pengguna; status F-A11-0048 tidak diubah A13 (RESOLVED hanya oleh a11). Pengguna BELUM menyebut secara eksplisit dampaknya pada stratum tanpa label (F-A11-0049); butir itu tetap terbuka. D-79 (mikro) tidak disebut pengguna. Isi turunan menurut keterangan A01.'
approval_evidence:
  question: 'Temuan a07 (F-A07-0090 HIGH, F-A07-0091) dan a11 (F-A11-0041): usulan paket D-94/D-93 membuat "tidak dapat dinilai" menyerap kegagalan yang sudah pasti. Contoh: kombinasi tanpa temuan sama sekali (presisi 0/0, recall 0) jelas gagal syarat pertama, tetapi dilaporkan "tidak dapat dinilai", bukan "tidak". Bagaimana urutan penilaian ditetapkan di I.2/I.3?'
  options_offered: ['Syarat pertama dinilai lebih dulu; "tidak dapat dinilai" hanya untuk syarat kedua [terpilih] (deskripsi opsi diringkas A01: 0/0 pada penyebut presisi kombinasi dihitung sebagai syarat pertama gagal; mengubah sebagian D-94 dan D-93)', 'Pertahankan paket D-94 apa adanya', 'Bawa ke tim, naskah memuat penanda saja']
  user_answer: 'Syarat pertama dinilai lebih dulu; "tidak dapat dinilai" hanya untuk syarat kedua'
  answered_at: '2026-11-10'
  session_ref: 'sesi 2026-11-10, AskUserQuestion urutan penilaian (temuan a07/a11), diteruskan A01'
  scope: 'Hanya urutan penilaian syarat pertama dan kedua di I.2/I.3 (mengubah D-94 butir 3 dan sebagian D-93)'
```

## D-99

```yaml
id: D-99
decision: 'Union tanpa aturan temuan ganda: naskah menyatakan aturan deduplikasi dan akibatnya (presisi kombinasi berada di antara presisi komponen), ditandai usulan penulis'
class: L3
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (keputusan pengguna lingkup terbatas, bersifat usulan penulis; persetujuan tim/pembimbing BELUM ada)
date: '2026-11-10'
related: [F-A11-0023, D-77, D-94, D-29]
basis: 'Jawaban pengguna atas AskUserQuestion F-A11-0023, diteruskan A01'
alternatives_considered: ['Tinjau bentuk syarat presisi (bawa ke tim sebagai penanda)', 'Ganti mekanisme union jadi bentuk lain (irisan/penyaringan)']
consequences: 'Union (D-77/D-94) tetap usulan penulis; D-29 tidak berubah. Bentuk syarat presisi tidak ditinjau dan mekanisme tidak diganti. Status F-A11-0023 tidak diubah A13 (RESOLVED menurut a11 pada audit ulang terarah dicatat di FINDINGS_LOG).'
approval_evidence:
  question: 'F-A11-0023 (HIGH, a11). Pada union tanpa aturan temuan ganda, presisi kombinasi selalu berada di antara presisi kedua komponen, sehingga syarat "presisi kombinasi lebih tinggi daripada masing-masing komponen" tidak mungkin terpenuhi. Bagaimana naskah menanganinya (union itu sendiri adalah usulan Anda, D-77/D-94)?'
  options_offered: ['Nyatakan aturan deduplikasi dan akibatnya, tanda usulan [terpilih]', 'Tinjau bentuk syarat presisi (bawa ke tim sebagai penanda)', 'Ganti mekanisme union jadi bentuk lain (irisan/penyaringan)']
  user_answer: 'Nyatakan aturan deduplikasi dan akibatnya, tanda usulan'
  answered_at: '2026-11-10'
  session_ref: 'sesi 2026-11-10, AskUserQuestion F-A11-0023, diteruskan A01'
  scope: 'Hanya penanganan F-A11-0023: aturan deduplikasi dan akibatnya dinyatakan, ditandai usulan penulis'
```

## D-100

```yaml
id: D-100
decision: 'Lingkup revisi terbatas atas DRAF 24 (bukan DRAF 25) yang langsung menghasilkan DOCX: terapkan keputusan pengguna yang ada (termasuk dua isu HIGH dan keputusan editorial terkait D-83), simpan Markdown hasil revisi, migrasikan ke DOCX tanpa format baru, jangan ubah klausa D-85 di p22 dan kalimat verbatim D-90, audit terarah a09/a07/a11'
class: L3
status: SUPERSEDED by D-115 (sebagian, teks Bab I DRAF 24 yang menjadi objeknya digantikan docx resmi 2026-11-12, tidak mengikat naskah baru)
status_sebelumnya: APPROVED (instruksi pengguna lingkup terbatas; persetujuan tim/pembimbing BELUM ada)
date: '2026-11-10'
related: [D-83, D-85, D-90, D-95, D-98, D-99, D-06, D-35, D-36, D-49, Q-B1-aw, Q-B1-al, Q-B1-ax]
basis: 'Jawaban teks bebas pengguna atas pertanyaan paket usulan A01 setelah empat auditor DRAF 24 selesai (siklus otomatis D-06 habis), diteruskan A01'
alternatives_considered: ['Paket usulan penulis A01 (plafon satu komponen, satuan unit, episode tanpa dokumen, batas kesimpulan, "tidak diuji"): TIDAK dipilih pengguna; teks lengkap opsi diringkas A01 (tanda "...")']
consequences: 'Pengguna TIDAK memilih paket usulan A01; temuan terkait (plafon satu komponen, satuan unit, episode tanpa dokumen, batas kesimpulan, "tidak diuji") tetap OPEN. Interpretasi A01 atas "keputusan editorial terkait D-83": Dietrich/Stubbert hanya sebagai latar, tidak dipakai mengualifikasi komponen capstone, tanpa menafsirkan D-61 (D-83/D-95); interpretasi ini BELUM dikonfirmasi pengguna. Jalur DOCX BELUM diputuskan: tools/build_modular.py membangun dari master docx Bab II, Bab I hanya penampung (Q-B1-aw, al, ax TERBUKA); tidak ada eksekusi build tercatat pada brief ini. Output wajib menurut pengguna: Markdown hasil revisi, DOCX siap diperiksa, ringkasan perubahan dan status verifikasi auditor, daftar temuan OPEN dan keputusan menunggu tim/pembimbing. Pemeriksaan di luar cakupan tidak diperbaiki tanpa persetujuan.'
approval_evidence:
  question: 'Keempat auditor selesai (a07 FAIL, a11 FAIL, a09 FAIL, a08 PASS_WITH_NOTES). Siklus otomatis D-06 sudah habis, jadi revisi ke DRAF 25 butuh izin Anda. ... setujukah paket usulan penulis berikut ...? (teks diringkas pada brief A01)'
  options_offered: ['Daftar opsi lengkap TIDAK diterima A13; brief A01 hanya menyebut paket usulan penulis (plafon satu komponen, satuan unit, episode tanpa dokumen, batas kesimpulan, "tidak diuji"); pengguna menjawab dengan teks bebas']
  user_answer: 'Saya ingin alur kerja langsung menghasilkan DOCX, bukan berhenti di Markdown.Gunakan DRAF 24 sebagai basis. Lakukan revisi terbatas sesuai keputusan yang telah saya berikan, termasuk dua isu HIGH dan keputusan editorial terkait D-83.Setelah revisi Markdown selesai:1. Simpan Markdown hasil revisi sebagai sumber yang dapat ditelusuri.2. Langsung migrasikan Markdown tersebut ke DOCX.3. Pertahankan struktur proposal, hierarki heading, penomoran, tabel, diagram, sitasi, dan format akademik sesuai dokumen sebelumnya. Jangan membuat format baru.4. Jangan mengubah klausa D-85 di p22 dan kalimat verbatim D-90.5. Jalankan pemeriksaan terarah oleh a09, a07, dan a11 pada bagian yang berubah. Jangan mengulang seluruh QA.6. Jika pemeriksaan menemukan masalah, laporkan dan jangan memperbaiki di luar cakupan tanpa persetujuan.**Output wajib:**- Markdown hasil revisi.- DOCX hasil migrasi yang siap diperiksa.- Ringkasan perubahan dan status verifikasi auditor.- Daftar temuan yang masih OPEN dan keputusan yang masih menunggu tim/pembimbing.Jangan membuat DRAF 25. Perlakukan pekerjaan ini sebagai revisi terbatas DRAF 24 yang langsung menghasilkan dokumen DOCX.'
  answered_at: '2026-11-10'
  session_ref: 'sesi 2026-11-10, AskUserQuestion paket usulan A01 (jawaban teks bebas), diteruskan A01'
  scope: 'Lingkup revisi terbatas DRAF 24 dan keluaran Markdown plus DOCX seperti diuraikan; bukan persetujuan paket usulan A01, bukan persetujuan jalur build DOCX, bukan persetujuan tim/pembimbing'
```

Catatan D-101 (2026-11-10, brief A01 memory_op record_decisions): keputusan PENGGUNA lingkup terbatas melalui AskUserQuestion (konfirmasi atas pilihan "2" sebelumnya), BUKAN persetujuan tim, pembimbing, atau RSIA. Tidak ada keputusan lama yang ditandai SUPERSEDED.

## D-101

```yaml
id: D-101
decision: 'Tiga entri Daftar Pustaka Kementerian Kesehatan RI (2021, 2022b, 2024: Permenkes 26/2021, Permenkes 24/2022, Kepmenkes 1596/2024) ditambahkan ke docx resmi Bab II (bab2/13523136-Proposal-IF4091-Capstone-Individu-2026-Draft-Bab2.docx), agar Daftar Pustaka DOCX Bab I memuatnya'
class: L3
status: APPROVED (keputusan pengguna lingkup terbatas; persetujuan tim/pembimbing BELUM ada)
date: '2026-11-10'
related: [F-A12-0001 (versi brief A01), D-100, D-92, Q-B1-aw, Q-B1-al, Q-B1-ax, Q-B1-bf]
basis: 'Jawaban pengguna atas AskUserQuestion konfirmasi (pilihan "2" sebelumnya dimintakan konfirmasi dengan rincian temuan a12), diteruskan A01'
alternatives_considered: ['Opsi 1: ubah skrip, ambil 3 entri dari Markdown', 'Opsi 3: bangun dengan 8 entri, tandai 3 yang hilang']
consequences: 'Menurut brief A01: pengguna/sesi Claude biasa (bukan agent) menambahkan tiga paragraf pustaka Kemenkes ke docx resmi Bab II, teks dari bab2/Bab_II_Revisi_Notulensi.md baris 261, 265, 267, urutan A-Z; tidak ada perubahan Bab II lain. A13 TIDAK memverifikasi isi docx (tidak dibaca) dan tidak memperbarui hash. Menyentuh docx Bab II resmi di luar Bab I; tidak mengubah D-100 (jalur build DOCX tetap BELUM diputuskan: Q-B1-aw, al, ax TERBUKA). D-92 (judul) tidak dipasang. Q-B1-bf (Permenkes 26/2021 hlm. 48-54) tetap BELUM diverifikasi; keputusan ini hanya soal keberadaan entri, bukan kebenaran rujukan atau halaman. Status F-A12-0001 versi brief tidak diubah A13 (RESOLVED hanya oleh a12 setelah pemeriksaan ulang).'
approval_evidence:
  question: 'Diagnosis a12 selesai (F-A12-0001, HIGH): 8 dari 11 awalan pustaka Bab I cocok dengan docx resmi Bab II. Tiga entri Kementerian Kesehatan RI (2021, 2022b, 2024: Permenkes 26/2021, Permenkes 24/2022, Kepmenkes 1596/2024) tidak ada di docx resmi (hanya 37 entri, tanpa kelompok institusional), padahal ada di bab2/Bab_II_Revisi_Notulensi.md baris 261, 265, 267. Pilihan Anda sebelumnya "2" saya mintakan konfirmasi dengan rincian ini. Bagaimana tiga entri itu masuk Daftar Pustaka DOCX Bab I?'
  options_offered: ['Opsi 2: tambahkan 3 entri ke docx resmi Bab II', 'Opsi 1: ubah skrip, ambil 3 entri dari Markdown', 'Opsi 3: bangun dengan 8 entri, tandai 3 yang hilang']
  user_answer: 'Opsi 2: tambahkan 3 entri ke docx resmi Bab II'
  answered_at: '2026-11-10'
  session_ref: 'sesi 2026-11-10, AskUserQuestion konfirmasi F-A12-0001, diteruskan A01'
  scope: 'Hanya tiga paragraf pustaka Kemenkes (2021, 2022b, 2024) ditambahkan ke bab2/13523136-Proposal-IF4091-Capstone-Individu-2026-Draft-Bab2.docx oleh pengguna/sesi Claude biasa (bukan agent), teks dari bab2/Bab_II_Revisi_Notulensi.md baris 261, 265, 267, urutan A-Z; tidak ada perubahan Bab II lain'
```

Catatan D-102..D-112 (2026-11-12, rekonsiliasi memory atas permintaan pengguna di sesi biasa tanpa agent): dicatat langsung oleh sesi Claude biasa, bukan A13 (pengecualian atas §A-9.6 butir 'hanya A13 menulis'; dasar: perintah pengguna 'rekonsiliasi semua memory'). D-102..D-105 = baseline resmi sementara dari pengguna, BUKAN persetujuan tim/pembimbing. D-06 dan D-49 ditandai SUPERSEDED (sebagian); tidak ada keputusan lain diubah (instruksi pengguna: jangan mengubah keputusan tanpa persetujuan). Konflik dibawa sebagai Q-REC-a..e.

## D-102

```yaml
id: D-102
decision: 'Baseline Bab I: I.1 naratif; I.2 dua rumusan masalah berbentuk ''Bagaimana'' tanpa subbutir; I.3 dua tujuan/ukuran keberhasilan; I.4 batasan berbentuk butir; I.5 lima tahapan metodologi konkret tanpa framework bernama (tahapan input-kegiatan-output). Mekanisme kombinasi, jumlah kasus, ambang, pencocokan hasil, dan komposisi penilai tidak ditentukan tanpa keputusan tim; dokumen Penyelarasan bukan sumber yang boleh diatribusikan di Bab I; informasi belum terverifikasi tidak ditulis sebagai fakta.'
class: L3
status: APPROVED (baseline sementara dari pengguna; titik konflik ambang/union/I.3 dikesampingkan oleh D-115; persetujuan tim/pembimbing BELUM ada)
date: '2026-11-12'
related:
- D-21
- D-29
- D-34
- D-77
- D-78
- D-79
- D-24
- D-111
- Q-REC-b
- Q-REC-c
basis: Bagian 1 CONTEXT TRANSFER yang diserahkan pengguna 2026-11-12
alternatives_considered:
- Tanpa alternatif; baseline diberikan pengguna
consequences: A13/agent memperlakukan butir ini sebagai baseline, bukan izin mengubah substansi sendiri. Tidak ada keputusan lama yang ditandai SUPERSEDED oleh butir ini; ketidakcocokan dengan naskah docx saat ini dan keputusan lama dibawa sebagai Q-REC-b, Q-REC-c, Q-REC-e untuk dikonfirmasi pengguna.
approval_evidence:
  question: Pengguna menyerahkan CONTEXT TRANSFER berisi keputusan Bab I dan Bab II sebagai baseline resmi sementara dan meminta rekonsiliasi semua memory
  options_offered:
  - Tidak ada opsi; pengguna menyerahkan baseline/arahan sebagai instruksi
  user_answer:
  - 'Pesan pengguna 2026-11-12: "sekarang saya mau rekonsiliasi semua memory saat ini. kurleb ini kemajuannya: # CONTEXT TRANSFER — KEPUTUSAN BAB I DAN BAB II CAPSTONE. Gunakan keputusan berikut sebagai baseline resmi sementara untuk melanjutkan pekerjaan proposal IF4091 Capstone."'
  - '## 1. Bab I

    - Struktur: I.1 naratif; I.2 dua rumusan masalah; I.3 dua tujuan/ukuran keberhasilan; I.4 batasan masalah berbentuk butir; I.5 lima tahapan metodologi.

    - I.2 menggunakan bentuk pertanyaan "Bagaimana", tanpa subbutir a/b.

    - I.2–I.5 menggunakan penomoran butir sesuai kebutuhan.

    - I.5 menjelaskan tahapan konkret, bukan hanya menyebut nama framework.

    - Belum ada framework metodologi bernama yang disetujui.

    - Arah yang pernah direkomendasikan adalah tidak menggunakan framework bernama, tetapi menjelaskan tahapan input–kegiatan–output.

    - Tahapan yang pernah dirumuskan: persiapan data, pelabelan tenaga ahli secara blind, pengembangan AI/NLP-RAG dan rule-based, pengujian tiga konfigurasi, serta evaluasi precision/recall dan kejelasan hasil.

    - Mekanisme kombinasi, jumlah kasus, ambang batas, pencocokan hasil, dan komposisi penilai tidak boleh ditentukan tanpa keputusan tim.

    - Dokumen Penyelarasan Pemahaman Capstone bukan sumber resmi yang boleh diatribusikan dalam Bab I.

    - Informasi yang belum terverifikasi tidak boleh ditulis sebagai fakta yang sudah terbukti.'
  answered_at: '2026-11-12'
  session_ref: sesi biasa (tanpa agent) 2026-11-12, pesan pengguna; dicatat langsung atas permintaan pengguna 'rekonsiliasi semua memory'
  scope: Hanya isi Bagian 1 CONTEXT TRANSFER; bukan persetujuan tim/pembimbing/RSIA
```

## D-103

```yaml
id: D-103
decision: Baseline struktur Bab II (II.1 sampai II.5 beserta sub-subbab seperti pada bagian 2 CONTEXT TRANSFER) dan nama judul sub-subbab menurut baseline.
class: L3
status: SUPERSEDED by D-114 (sebagian, hanya judul II.2, II.3.1, II.3.2 dan ejaan II.5.3; struktur lain tetap)
status_sebelumnya: APPROVED (baseline resmi sementara menurut pengguna; persetujuan tim/pembimbing BELUM ada)
date: '2026-11-12'
related:
- D-111
- D-112
- Q-REC-a
basis: Bagian 2 CONTEXT TRANSFER yang diserahkan pengguna 2026-11-12
alternatives_considered:
- Tanpa alternatif; baseline diberikan pengguna
consequences: 'Judul pada docx resmi yang disinkronkan 2026-11-12 berbeda pada II.2, II.3.1, II.3.2, dan ejaan II.5.3 (lihat Q-REC-a); tidak ada judul diubah oleh rekonsiliasi ini. Ejaan II.5.3: pengguna kemudian menyatakan ''Deidentifikasi'' (D-112), yang lebih baru dan dipakai.'
approval_evidence:
  question: Pengguna menyerahkan CONTEXT TRANSFER berisi keputusan Bab I dan Bab II sebagai baseline resmi sementara dan meminta rekonsiliasi semua memory
  options_offered:
  - Tidak ada opsi; pengguna menyerahkan baseline/arahan sebagai instruksi
  user_answer:
  - 'Pesan pengguna 2026-11-12: "sekarang saya mau rekonsiliasi semua memory saat ini. kurleb ini kemajuannya: # CONTEXT TRANSFER — KEPUTUSAN BAB I DAN BAB II CAPSTONE. Gunakan keputusan berikut sebagai baseline resmi sementara untuk melanjutkan pekerjaan proposal IF4091 Capstone."'
  - "## 2. Bab II\nGunakan struktur berikut:\n- II.1 Rekam Medis dan Dokumentasi Klinis dalam Konteks Klaim JKN\n  - II.1.1 Kewajiban dan Isi Rekam Medis Elektronik\n  - II.1.2 Catatan Perkembangan Pasien Terintegrasi\n  - II.1.3 Resume Medis\n  - II.1.4 Variabel dan Metadata Rekam Medis Elektronik Rawat Inap\n  - II.1.5 Pengodean dan Verifikasi Klaim INA-CBG\n- II.2 Representasi dan Standardisasi Informasi Klinis\n  - II.2.1 SATUSEHAT dan Profil Rawat Inap Berbasis HL7 FHIR\n  - II.2.2 Adopsi Terminologi Klinis\n  - II.2.3 Bagian SOAP dan Relasi antara Penilaian dan Rencana\n  - II.2.4 Graf Pengetahuan Berbasis Rekam Medis\n- II.3 Pemeriksaan Dokumentasi Klinis dengan Model Bahasa Besar\n  - II.3.1 Pemeriksaan Kesalahan dan Konsistensi Dokumentasi Klinis\n  - II.3.2 Ketahanan Model terhadap Variasi Teks Klinis\n- II.4 Retrieval-Augmented Generation dan Penjangkaran Keluaran pada Bukti\n  - II.4.1 Konsep dan Mekanisme RAG\n  - II.4.2 Penerapan Retrieval dan Penjangkaran Bukti pada Informasi Klinis\n- II.5 Tata Kelola dan Privasi Penggunaan AI Klinis\n  - II.5.1 Pengaturan dan Tata Kelola Penggunaan AI di Indonesia\n  - II.5.2 Rekomendasi Penggunaan LLM dalam Konteks Klinis dan Administratif\n  - II.5.3 De-identifikasi Data Rekam Medis"
  answered_at: '2026-11-12'
  session_ref: sesi biasa (tanpa agent) 2026-11-12, pesan pengguna; dicatat langsung atas permintaan pengguna 'rekonsiliasi semua memory'
  scope: Hanya struktur Bab II pada Bagian 2; bukan persetujuan tim/pembimbing
```

## D-104

```yaml
id: D-104
decision: 'Penyelarasan dan pemindahan: Bab II mengikuti cakupan Bab I (CPPT dan dokumen ringkasan pelayanan untuk rawat inap, rawat jalan, IGD; fokus II.1.4 tetap rawat inap); empat kategori ketidaksesuaian; tiga konfigurasi pembanding; evaluasi precision, recall, kejelasan. II.6 ''Sintesis Penelitian Terdahulu dan Posisi Penelitian'' dihapus dari Bab II; sintesis, perbandingan penelitian, research gap, dan posisi penelitian dipindahkan ke Bab III; Bab II berakhir di II.5.3; tidak ada subbab ''Ketidakpastian Keluaran dan Peringatan Tingkat Kepercayaan''; literatur yang dikeluarkan dari pembahasan Bab II: Susilo, Rotmensch, Ali, Skrabic, Jaganathan, Devanand, Testoni, Griot, Kompa, Rocher, Kudlicki, El Emam, Azzam (Susilo boleh tetap di daftar pustaka gabungan bila disitasi di Bab I).'
class: L3
status: APPROVED (baseline resmi sementara menurut pengguna; persetujuan tim/pembimbing BELUM ada)
date: '2026-11-12'
related:
- D-59
- D-60
- D-61
- D-62
- D-63
- D-64
- D-65
- D-81
- D-82
- D-83
- D-84
- D-85
- D-95
- Q-REC-d
- Q-REC-e
basis: Bagian 3 dan 4 CONTEXT TRANSFER yang diserahkan pengguna 2026-11-12
alternatives_considered:
- Tanpa alternatif; baseline diberikan pengguna
consequences: Keputusan lama tentang paragraf research gap di Bab I (D-59..D-65, D-81..D-85, D-95) terkait materi yang menurut baseline pindah ke Bab III; statusnya TIDAK diubah di sini dan ditanyakan pada Q-REC-e. Bab III di docx resmi masih berupa teks templat; `bab3/Bahan_Pindahan_dari_Bab_II.md` belum diselaraskan (Q-REC-d).
approval_evidence:
  question: Pengguna menyerahkan CONTEXT TRANSFER berisi keputusan Bab I dan Bab II sebagai baseline resmi sementara dan meminta rekonsiliasi semua memory
  options_offered:
  - Tidak ada opsi; pengguna menyerahkan baseline/arahan sebagai instruksi
  user_answer:
  - 'Pesan pengguna 2026-11-12: "sekarang saya mau rekonsiliasi semua memory saat ini. kurleb ini kemajuannya: # CONTEXT TRANSFER — KEPUTUSAN BAB I DAN BAB II CAPSTONE. Gunakan keputusan berikut sebagai baseline resmi sementara untuk melanjutkan pekerjaan proposal IF4091 Capstone."'
  - '## 3. Keputusan penyelarasan Bab I dan Bab II

    - Bab II harus mengikuti cakupan Bab I: CPPT dan dokumen ringkasan pelayanan untuk rawat inap, rawat jalan, dan IGD.

    - Jangan membatasi keseluruhan sistem hanya pada rawat inap.

    - Tetap pertahankan fokus khusus subbab II.1.4 pada variabel dan metadata rawat inap.

    - Kategori ketidaksesuaian: omission, contradiction, unsupported addition, dan contextual/temporal mismatch.

    - Konfigurasi pembanding: rule-based, AI/NLP-RAG, serta kombinasi setelah deduplikasi.

    - Evaluasi mencakup precision, recall, dan penilaian kejelasan hasil serta referensi.


    ## 4. Keputusan pemindahan dan penghapusan

    - Hapus II.6 "Sintesis Penelitian Terdahulu dan Posisi Penelitian" dari Bab II.

    - Pindahkan sintesis, perbandingan penelitian, research gap, dan posisi penelitian ke Bab III.

    - Bab II berakhir pada II.5.3.

    - Jangan membuat subbab tersendiri "Ketidakpastian Keluaran dan Peringatan Tingkat Kepercayaan" pada II.5.

    - Literatur berikut dikeluarkan dari pembahasan Bab II: Susilo, Rotmensch, Ali, Skrabic, Jaganathan, Devanand, Testoni, Griot, Kompa, Rocher, Kudlicki, El Emam, dan Azzam.

    - Susilo tetap dapat berada dalam daftar pustaka gabungan jika masih disitasi di Bab I.'
  answered_at: '2026-11-12'
  session_ref: sesi biasa (tanpa agent) 2026-11-12, pesan pengguna; dicatat langsung atas permintaan pengguna 'rekonsiliasi semua memory'
  scope: Hanya Bagian 3 dan 4; bukan persetujuan tim/pembimbing
```

## D-105

```yaml
id: D-105
decision: Prinsip pembahasan literatur (kelompok per tema, bahas substantif, tidak sekadar satu-dua kalimat, tidak menyimpulkan metode pasti cocok karena dipakai penelitian lain, bedakan temuan terdahulu dari rancangan capstone) dan instruksi agent (baseline bukan izin ubah substansi; jangan hidupkan kembali materi yang dihapus/dipindahkan; jangan mengarang keputusan terbuka; laporkan konflik sebelum mengubah; jaga konsistensi Bab I-II; jangan ubah keputusan tanpa persetujuan pengguna).
class: L3
status: APPROVED (baseline resmi sementara menurut pengguna; persetujuan tim/pembimbing BELUM ada)
date: '2026-11-12'
related:
- D-103
- D-104
- D-110
basis: Bagian 5 dan 6 CONTEXT TRANSFER yang diserahkan pengguna 2026-11-12
alternatives_considered:
- Tanpa alternatif; baseline diberikan pengguna
consequences: 'Instruksi agent butir 4 dan 6 diterapkan pada rekonsiliasi ini: konflik dilaporkan (Q-REC-a..e) dan tidak ada keputusan lama diubah statusnya kecuali D-06 dan D-49 (sebagian) yang disetujui eksplisit pada D-106 dan D-111.'
approval_evidence:
  question: Pengguna menyerahkan CONTEXT TRANSFER berisi keputusan Bab I dan Bab II sebagai baseline resmi sementara dan meminta rekonsiliasi semua memory
  options_offered:
  - Tidak ada opsi; pengguna menyerahkan baseline/arahan sebagai instruksi
  user_answer:
  - 'Pesan pengguna 2026-11-12: "sekarang saya mau rekonsiliasi semua memory saat ini. kurleb ini kemajuannya: # CONTEXT TRANSFER — KEPUTUSAN BAB I DAN BAB II CAPSTONE. Gunakan keputusan berikut sebagai baseline resmi sementara untuk melanjutkan pekerjaan proposal IF4091 Capstone."'
  - '## 5. Prinsip pembahasan literatur

    - Kelompokkan penelitian berdasarkan tema yang jelas.

    - Bahas penelitian secara substantif: objek/tujuan, temuan, relevansi, dan alasan penggunaannya.

    - Jangan hanya menjelaskan penelitian penting dalam satu atau dua kalimat.

    - Jangan menyimpulkan suatu metode pasti cocok hanya karena pernah digunakan oleh penelitian terdahulu.

    - Bedakan temuan penelitian terdahulu dengan rancangan capstone yang diusulkan.


    ## 6. Instruksi untuk agent

    1. Perlakukan keputusan di atas sebagai baseline, bukan izin untuk mengubah substansi secara mandiri.

    2. Jangan menghidupkan kembali struktur atau materi yang sudah diputuskan untuk dihapus/dipindahkan.

    3. Jangan mengarang keputusan untuk hal-hal yang masih terbuka.

    4. Jika menemukan konflik dengan dokumen sumber atau keputusan yang lebih baru, laporkan konflik tersebut sebelum melakukan perubahan.

    5. Pertahankan konsistensi Bab I dan Bab II.

    6. Jangan mengubah keputusan yang sudah disepakati tanpa persetujuan pengguna.'
  answered_at: '2026-11-12'
  session_ref: sesi biasa (tanpa agent) 2026-11-12, pesan pengguna; dicatat langsung atas permintaan pengguna 'rekonsiliasi semua memory'
  scope: Hanya Bagian 5 dan 6; bukan persetujuan tim/pembimbing
```

## D-106

```yaml
id: D-106
decision: Batas revisi otomatis diturunkan dari 2 menjadi 1 siklus per subbab; tidak ada 'perbaikan terarah' tambahan kecuali diminta pengguna untuk temuan yang disebut; satu subbab maksimal 3 draf; hanya temuan HIGH/MEDIUM memicu revisi, LOW/INFO dikerjakan sekali di akhir; QA hanya atas bagian yang berubah; a05 tidak menantang keputusan APPROVED.
class: L4
status: APPROVED
date: '2026-11-12'
related:
- D-06
- D-110
basis: Keluhan pengguna tentang pengulangan hingga DRAF 24 untuk Bab I dan jawaban '1' atas usulan langkah 1
alternatives_considered:
- Mempertahankan batas 2 siklus (D-06)
consequences: 'D-06 ditandai SUPERSEDED by D-106 (sebagian: batas siklus 2 -> 1). Diterapkan di .claude/agents/a01-orchestrator.md, .claude/skills/agent-contract/SKILL.md, CLAUDE.md §11.3 dan §3 (commit a4063ae). Draf Bab I yang ada tidak diubah oleh keputusan ini.'
approval_evidence:
  question: 'Sesi 2026-11-11/12: sesi Claude menganalisis 13 agent dan mengusulkan tiga langkah penghematan; ''Mau saya mulai merevisinya? Urutan yang saya usulkan: (1) ubah aturan siklus di a01-orchestrator.md dan CLAUDE.md, (2) gabung agent QA, (3) buat skrip linter untuk pola AI slop dan struktur. ... tolong konfirmasi dulu lingkupnya.'''
  options_offered:
  - (1) ubah aturan siklus di a01-orchestrator.md dan CLAUDE.md
  - (2) gabung agent QA
  - (3) buat skrip linter
  user_answer:
  - '... yang mana untuk bab 1 saja memakan hingga 24 draft, menurut anda apa yang perlu di revisi dari agent tersebut dalam membangun proposal'
  - padahal cuman bab 1 tapi pengulangan draft hingga draft ke 24 yang itu sangat boros waktu dan token, seharusnya ada maksimal revisi draft
  - '1'
  answered_at: '2026-11-12'
  session_ref: sesi biasa (tanpa agent) 2026-11-12, pesan pengguna; dicatat langsung atas permintaan pengguna 'rekonsiliasi semua memory'
  scope: Aturan siklus dan hemat siklus di a01, agent-contract, CLAUDE.md
```

## D-107

```yaml
id: D-107
decision: 'Roster menjadi 12 agent: a11-qa-technical digabung ke a07-qa-academic (a07 dengan focus: akademik atau teknis); berkas a11 dihapus; penomoran A11 tidak dipakai lagi; a09 menjalankan scripts/lint_prose.py lebih dulu (D-110).'
class: L4
status: APPROVED
date: '2026-11-12'
related:
- D-07
- D-110
basis: Jawaban 'lanjut langkah 2' dan 'lanjut langkah 3'
alternatives_considered:
- Mempertahankan 13 agent
- Nomori ulang A01..A12 (tidak dipilih; saran A01 tetap menomori)
consequences: Diterapkan di a07, a01, write_scopes.json, if4091-rules-map, check_agents.py (commit a4063ae). Temuan lama berawalan F-A11-xxxx tetap sah sebagai riwayat; auditor sekarang a07. Narasi docs/ menyebut A11 sebagai historis (blok Pembaruan 11 Nov 2026).
approval_evidence:
  question: 'Sesi 2026-11-11/12: sesi Claude menganalisis 13 agent dan mengusulkan tiga langkah penghematan; ''Mau saya mulai merevisinya? Urutan yang saya usulkan: (1) ubah aturan siklus di a01-orchestrator.md dan CLAUDE.md, (2) gabung agent QA, (3) buat skrip linter untuk pola AI slop dan struktur. ... tolong konfirmasi dulu lingkupnya.'''
  options_offered:
  - (1) ubah aturan siklus di a01-orchestrator.md dan CLAUDE.md
  - (2) gabung agent QA
  - (3) buat skrip linter
  user_answer:
  - lanjut langkah 2
  - lanjut langkah 3
  answered_at: '2026-11-12'
  session_ref: sesi biasa (tanpa agent) 2026-11-12, pesan pengguna; dicatat langsung atas permintaan pengguna 'rekonsiliasi semua memory'
  scope: Penggabungan a11 ke a07 dan skrip linter
```

## D-108

```yaml
id: D-108
decision: 'Git sepenuhnya urusan pengguna: tidak ada agent yang menjalankan git add, git commit, atau git push; gate G3 dihapus; a13 hanya membaca status Git; /sesi-tutup berhenti di laporan berkas yang berubah.'
class: L4
status: APPROVED
date: '2026-11-12'
related:
- D-12
- D-13
- D-109
basis: Pernyataan pengguna tidak ingin agent mengurus commit karena boros token
alternatives_considered:
- Mempertahankan a13 + G3
consequences: Diterapkan di a13-memory-manager.md, a01-orchestrator.md, write_scopes.json (kedua salinan), .claude/skills/sesi-tutup/SKILL.md, selftest.py. S7 (memory belum ter-commit) akan terus menjadi NOT_READY sampai pengguna commit; itu perilaku yang diharapkan, bukan galat.
approval_evidence:
  question: Sesi Claude menjelaskan bahwa a13 menjalankan git add/commit/push setelah G3 dan menanyakan apakah agent sudah lepas dari urusan commit
  options_offered:
  - Mempertahankan G3 dan a13 untuk Git
  user_answer:
  - terus buat urusan commit dan sebagainya agent itu udah lepas belum? saya gamau agent ngurus perihal commit karena buang-buang token aja
  answered_at: '2026-11-12'
  session_ref: sesi biasa (tanpa agent) 2026-11-12, pesan pengguna; dicatat langsung atas permintaan pengguna 'rekonsiliasi semua memory'
  scope: Pelepasan Git dari semua agent
```

## D-109

```yaml
id: D-109
decision: 'Sesi biasa (tanpa agent) menjadi bawaan di repo ini: kunci ''agent'' dihapus dari .claude/settings.json; mode orkestrasi hanya lewat ''claude --agent a01-orchestrator''. Perlindungan global (RSIA-source, Git berbahaya, aturan ask) tetap berlaku di sesi biasa.'
class: L4
status: APPROVED
date: '2026-11-12'
related:
- D-01
- D-108
basis: Pernyataan pengguna tidak selalu ingin memakai agent
alternatives_considered:
- Tetap memaksa a01 pada semua sesi
consequences: D-01 diubah sebagian oleh keputusan ini (a01 tetap main-thread agent bila diluncurkan dengan --agent, tetapi bukan bawaan). Perubahan memory di sesi biasa tidak tercatat otomatis; direkonsiliasi di sesi orkestrasi berikutnya.
approval_evidence:
  question: Sesi Claude menemukan bahwa settings.json memaksa semua sesi menjadi a01-orchestrator
  options_offered:
  - Tetap memaksa a01
  user_answer:
  - terus kan saya ga selamanya pengen selalu pake agent untuk repo ini, misal saya lagi gak pengen make agent jadi cuman sesi biasa di claude codenya itu tolong diantisipasi juga
  answered_at: '2026-11-12'
  session_ref: sesi biasa (tanpa agent) 2026-11-12, pesan pengguna; dicatat langsung atas permintaan pengguna 'rekonsiliasi semua memory'
  scope: settings.json dan USER_GUIDE.md
```

## D-110

```yaml
id: D-110
decision: 'Aturan penanda dan naskah siap-kumpul: penanda hanya untuk data/sumber yang benar-benar belum ada atau keputusan pihak luar; satu topik satu penanda; maksimal 10 penanda per bab; jawaban pengguna dan temuan QA tidak boleh menghasilkan penanda baru; naskah tanpa nomor D-/F-/Q-, label DRAF, ''usulan penulis'', atau riwayat revisi; keputusan dikumpulkan dalam satu batch sebelum penulisan ulang; scripts/lint_prose.py menandai kebocoran internal dan kelebihan penanda.'
class: L3
status: APPROVED
date: '2026-11-12'
related:
- D-106
- D-107
- D-105
basis: Penjelasan pengguna bahwa setiap jawaban melahirkan penanda baru hingga DRAF 24
alternatives_considered:
- Tidak mengubah agent
consequences: Diterapkan di a03, a01, a07, a09, CLAUDE.md §3, scripts/lint_prose.py (diverifikasi 157 kebocoran internal dan 59 penanda pada DRAF 24 lama). Naskah baru (D-111) tanpa penanda.
approval_evidence:
  question: Sesi Claude melaporkan 59 penanda dan penyebab draf berulang; pertanyaan perbaikan agent
  options_offered:
  - Tidak mengubah agent
  user_answer:
  - nah masalahnya berpenanda ini ketika saya jawab ia selalu menghasilkan penanda yang baru lagi dan itu terulang hingga draft ke 24 padahal hanya bab 1, alamat file yang saya kirimkan sebelumnya adalah hasil migrasi agent vs hasil migrasi non agent. silahkan anda perbaiki agentnya
  answered_at: '2026-11-12'
  session_ref: sesi biasa (tanpa agent) 2026-11-12, pesan pengguna; dicatat langsung atas permintaan pengguna 'rekonsiliasi semua memory'
  scope: Aturan agent dan linter
```

## D-111

```yaml
id: D-111
decision: 'Artefak resmi sekarang: modular/TA1 bab 1.docx, modular/TA1 bab 2.docx, dan 13523136-Proposal-IF4091-Capstone-Individu-2026-Draft-Bab1-Bab2.docx. Markdown disamakan dengan docx tersebut: bab1/Bab_I_Draft.md ditulis ulang dari docx (tanpa penanda/riwayat), bab2/ memuat Pembuka_Bab_II.md, II.1..II.5, Daftar_Pustaka.md, gambar/; berkas II.1..II.8 dan Pembuka lama dipindah ke bab2/arsip_sebelum_sinkron_docx/.'
class: L3
status: SUPERSEDED by D-119 (sebagian, hanya sumber kebenaran Bab I; Bab II tetap docx)
status_sebelumnya: APPROVED
date: '2026-11-12'
related:
- D-49
- D-35
- D-36
- D-100
- D-101
- Q-B1-al
- Q-B1-aw
- Q-B1-ax
basis: Pernyataan pengguna tentang artefak resmi dan perintah menyamakan draf dengan docx
alternatives_considered:
- Tetap memakai Markdown DRAF 24 sebagai sumber
consequences: 'D-49 ditandai SUPERSEDED by D-111 (sebagian: sumber kebenaran Bab I kini docx resmi, bukan Markdown DRAF 24). tools/build_modular.py untuk Bab I tidak lagi relevan dan akan menolak jalan (hash/jumlah penanda); jalur build modular (Q-B1-al/aw/ax) tidak diputuskan di sini. Teks DRAF 24 lama dan catatan kerjanya tersedia di riwayat Git (commit sebelum 2026-11-12).'
approval_evidence:
  question: Sesi Claude membandingkan docx hasil migrasi agent dan non-agent dan menanyakan perbaikan migrasi
  options_offered:
  - Tidak ada opsi lain ditawarkan
  user_answer:
  - yang versi resmi sekarang itu TA1 bab 1 dan TA2 bab 2 dan 13523136-Proposal-IF4091-Capstone-Individu-2026-Draft-Bab1-Bab2. sesuaikan draft dengan docx tersebut
  answered_at: '2026-11-12'
  session_ref: sesi biasa (tanpa agent) 2026-11-12, pesan pengguna; dicatat langsung atas permintaan pengguna 'rekonsiliasi semua memory'
  scope: Sinkronisasi Markdown Bab I/II dengan ketiga docx; pemindahan berkas lama ke arsip
```

## D-112

```yaml
id: D-112
decision: 'Perbaikan docx resmi: heading II.2.3 ''Rekomendasi Penggunaan LLM...'' diganti ''Bagian SOAP dan Relasi antara Penilaian dan Rencana'' (isi anotasi catatan perkembangan); judul Bab II ''KAJIAN PUSTAKA''; ''Pengodean dan Verifikasi Klaim INA-CBG'' menjadi Heading 3 (II.1.5) di TA1 bab 2; ejaan ''Deidentifikasi''; daftar isi, Daftar Gambar, dan Daftar Tabel TA1 bab 2 dibangun ulang (halaman dari render LibreOffice).'
class: L3
status: APPROVED
date: '2026-11-12'
related:
- D-103
- D-111
- Q-REC-a
basis: Jawaban pengguna atas empat butir (1 judul, 2 hierarki, 3 ejaan, 4 daftar gambar/tabel)
alternatives_considered:
- Membiarkan dua docx berbeda
consequences: Diterapkan pada modular/TA1 bab 2.docx, modular/TA1 bab 1.docx (satu 'de-identifikasi'), dan berkas Draft-Bab1-Bab2.docx (heading dan entri daftar isi II.2.3). Cadangan di .scratch/backup_docx_1112/. Nomor halaman perlu Update Field di Word. PDF TA1 bab 1/2 kini tertinggal dari docx.
approval_evidence:
  question: Sesi Claude melaporkan dua keanehan docx (judul II.2.3 tertukar, daftar isi TA1 bab 2 basi) dan beda antara TA1 bab 2 dan berkas gabungan; 'Mau saya (a) memperbaiki dua keanehan docx..., atau (b) menjalankan rekonsiliasi memory?' lalu 'Mau saya samakan TA1 bab 2.docx dengan berkas gabungan untuk poin 1 sampai 3, atau dibiarkan berbeda?'
  options_offered:
  - (a) perbaiki dua keanehan
  - (b) rekonsiliasi memory
  - samakan atau biarkan berbeda
  user_answer:
  - lakukan (a) untuk poin 1 itu kesalahan saya, untuk poin 2 silahkan anda perbaiki, untuk poin 3 memang disengaja.
  - 1. yang bener KAJIAN PUSTAKA, 2. ya, 3. harusnya Deidentifikasi, 4. Lakukan
  answered_at: '2026-11-12'
  session_ref: sesi biasa (tanpa agent) 2026-11-12, pesan pengguna; dicatat langsung atas permintaan pengguna 'rekonsiliasi semua memory'
  scope: Perbaikan judul, hierarki, ejaan, dan daftar pada docx
```

Catatan D-113..D-116 (2026-11-12, jawaban pengguna atas Q-REC-a..f): dicatat langsung oleh sesi biasa. 37 keputusan DRAF 24 ditandai SUPERSEDED sebagian oleh D-115: D-59, D-60, D-61, D-62, D-63, D-64, D-65, D-66, D-67, D-68, D-69, D-70, D-71, D-72, D-73, D-74, D-75, D-81, D-82, D-83, D-84, D-85, D-86, D-87, D-88, D-89, D-90, D-91, D-92, D-93, D-94, D-95, D-96, D-97, D-98, D-99, D-100. Status lama tiap keputusan disimpan di field status_sebelumnya.

## D-113

```yaml
id: D-113
decision: Gaya sitasi akhir sementara adalah APA (adaptasi Indonesia); K1 diputuskan pengguna dengan 'APA dulu'.
class: L3
status: APPROVED (keputusan pengguna sementara; konfirmasi tim, pembimbing, dan prodi BELUM ada)
date: '2026-11-12'
related:
- K1
- D-80
- Q-REC-f
basis: Jawaban pengguna atas Q-REC-f
alternatives_considered:
- Penulis-tahun dengan hlm. (konvensi DRAFT 6)
consequences: 'D-80 (usul APA) ditandai SUPERSEDED by D-113 (sebagian: usul menjadi keputusan sementara). Docx resmi masih campuran (''et al.''/''dkk.'', ''p.''/''hlm.''); penyeragaman ke APA BELUM dikerjakan dan butuh tugas tersendiri (a08 menilai format terhadap APA mulai sekarang).'
approval_evidence:
  question: 'Rekonsiliasi memory menghasilkan Q-REC-a..f: (a) judul Bab II baseline vs docx, (b) ambang 0,80/80%/union di Bab I docx vs baseline, (c) I.3 dua tujuan vs satu utama + lima khusus, (d) Bab III belum ditulis, (e) keputusan dan temuan lama atas DRAF 24, (f) gaya sitasi campuran. ''Mau jawab Q-REC-b dulu?'''
  options_offered:
  - Jawaban teks bebas pengguna atas enam butir
  user_answer:
  - gaya sitasi itu APA dulu
  answered_at: '2026-11-12'
  session_ref: sesi biasa (tanpa agent) 2026-11-12, jawaban pengguna atas Q-REC-a..f; dicatat langsung atas permintaan pengguna
  scope: Gaya sitasi akhir sementara; bukan persetujuan tim/pembimbing/prodi
```

## D-114

```yaml
id: D-114
decision: Judul sub-subbab Bab II mengikuti docx resmi (II.2 'Standar Interoperabilitas dan Terminologi Klinis di Indonesia'; II.3.1 'Deteksi Kesalahan pada Dokumentasi Klinis'; II.3.2 'Pemeriksaan Fakta Keluaran terhadap Rekam Medis Sumber'; II.2.3 'Bagian SOAP dan Relasi antara Penilaian dan Rencana'; II.5.3 'Deidentifikasi Data Rekam Medis').
class: L3
status: APPROVED
date: '2026-11-12'
related:
- D-103
- D-111
- D-112
- Q-REC-a
basis: Jawaban pengguna atas Q-REC-a
alternatives_considered:
- Mengikuti judul baseline D-103
consequences: 'D-103 ditandai SUPERSEDED by D-114 (sebagian: hanya judul II.2, II.3.1, II.3.2 dan ejaan II.5.3); struktur lain D-103 tetap. Tidak ada perubahan berkas: Markdown dan docx sudah memakai judul ini.'
approval_evidence:
  question: 'Rekonsiliasi memory menghasilkan Q-REC-a..f: (a) judul Bab II baseline vs docx, (b) ambang 0,80/80%/union di Bab I docx vs baseline, (c) I.3 dua tujuan vs satu utama + lima khusus, (d) Bab III belum ditulis, (e) keputusan dan temuan lama atas DRAF 24, (f) gaya sitasi campuran. ''Mau jawab Q-REC-b dulu?'''
  options_offered:
  - Jawaban teks bebas pengguna atas enam butir
  user_answer:
  - judul bab 2 sesuaikan dengan docx
  answered_at: '2026-11-12'
  session_ref: sesi biasa (tanpa agent) 2026-11-12, jawaban pengguna atas Q-REC-a..f; dicatat langsung atas permintaan pengguna
  scope: Judul sub-subbab Bab II
```

## D-115

```yaml
id: D-115
decision: 'Bab I pada docx resmi dibiarkan apa adanya, termasuk ambang 0,80, 80% skor 4 atau 5, mekanisme union dan deduplikasi, serta struktur I.3 (satu tujuan utama, lima tujuan khusus, tiga ukuran); pada titik-titik itu docx mengalahkan baseline D-102. Keputusan, temuan QA, dan pertanyaan terbuka yang bergantung pada teks Bab I DRAF 24 disesuaikan dengan kondisi docx saat ini: keputusan terkait ditandai SUPERSEDED sebagian, temuan OPEN/IN_PROGRESS atas Bab I DRAF 24 dibebaskan (WAIVED), pertanyaan Q-B1-* yang masih terbuka ditutup.'
class: L3
status: SUPERSEDED by D-118 (sebagian, hanya perubahan Bab I pada commit 80a13ba / Paket A; sisanya tetap berlaku)
status_sebelumnya: APPROVED (keputusan pengguna; persetujuan tim/pembimbing BELUM ada)
date: '2026-11-12'
related:
- D-102
- D-111
- Q-REC-b
- Q-REC-c
- Q-REC-e
- D-59..D-75
- D-81..D-100
basis: Jawaban pengguna atas Q-REC-b, c, dan e
alternatives_considered:
- Ubah Bab I mengikuti baseline
- Tandai ambang/union sebagai usulan
consequences: 'Keputusan yang ditandai SUPERSEDED by D-115 (sebagian): D-59..D-75, D-81..D-100 (status sebelumnya disimpan di field status_sebelumnya; substansi research gap/posisi dapat dirujuk saat menulis Bab III tetapi tidak mengikat naskah baru). Temuan FINDINGS_LOG atas Bab I (a02, a04, a05, a07, a08, a09, a10, a11) berstatus OPEN atau IN_PROGRESS menjadi WAIVED dengan bukti D-115; temuan a06 (lintas proposal), a12, a13, dan atas bab2/setup tidak diubah. Butir Q-B1-* berstatus TERBUKA/MENUNGGU ditutup. D-102 tetap APPROVED, tetapi titik konflik ambang/union/I.3 dikesampingkan oleh D-115. Persetujuan tim/pembimbing atas ambang dan union tetap BELUM ada; ini keputusan pengguna.'
approval_evidence:
  question: 'Rekonsiliasi memory menghasilkan Q-REC-a..f: (a) judul Bab II baseline vs docx, (b) ambang 0,80/80%/union di Bab I docx vs baseline, (c) I.3 dua tujuan vs satu utama + lima khusus, (d) Bab III belum ditulis, (e) keputusan dan temuan lama atas DRAF 24, (f) gaya sitasi campuran. ''Mau jawab Q-REC-b dulu?'''
  options_offered:
  - Jawaban teks bebas pengguna atas enam butir
  user_answer:
  - bab 1 biarkan saja ... draf 24 untuk bab 1 sesuaikan saja dengan kondisi docx saat ini
  answered_at: '2026-11-12'
  session_ref: sesi biasa (tanpa agent) 2026-11-12, jawaban pengguna atas Q-REC-a..f; dicatat langsung atas permintaan pengguna
  scope: Bab I docx apa adanya; penyesuaian catatan memory atas DRAF 24
```

## D-116

```yaml
id: D-116
decision: Bab III belum dimulai dan baru dimulai setelah rekonsiliasi ini benar-benar selesai; sampai saat itu tidak ada penulisan Bab III dan bab3/Bahan_Pindahan_dari_Bab_II.md tidak diubah.
class: L3
status: APPROVED
date: '2026-11-12'
related:
- D-104
- Q-REC-d
basis: Jawaban pengguna atas Q-REC-d
alternatives_considered:
- Menulis Bab III sekarang
consequences: Isi Bab III (sintesis, perbandingan, research gap, posisi penelitian) mengikuti D-104 dan D-105 saat dimulai.
approval_evidence:
  question: 'Rekonsiliasi memory menghasilkan Q-REC-a..f: (a) judul Bab II baseline vs docx, (b) ambang 0,80/80%/union di Bab I docx vs baseline, (c) I.3 dua tujuan vs satu utama + lima khusus, (d) Bab III belum ditulis, (e) keputusan dan temuan lama atas DRAF 24, (f) gaya sitasi campuran. ''Mau jawab Q-REC-b dulu?'''
  options_offered:
  - Jawaban teks bebas pengguna atas enam butir
  user_answer:
  - bab 3 memang belum dimulai dan akan dimulai setelah rekonsiliasi ini benar-benar selesai
  answered_at: '2026-11-12'
  session_ref: sesi biasa (tanpa agent) 2026-11-12, jawaban pengguna atas Q-REC-a..f; dicatat langsung atas permintaan pengguna
  scope: Urutan kerja Bab III
```

## D-117

```yaml
id: D-117
decision: 'Sitasi diseragamkan ke APA (adaptasi Indonesia) pada tiga docx resmi dan Markdown sinkron: ''et al.'' menjadi ''dkk.''; ''p.''/''pp.'' menjadi ''hlm.'' (termasuk daftar pustaka); rentang halaman memakai tanda pisah en; ''Kementerian Kesehatan'' di teks menjadi ''Kementerian Kesehatan Republik Indonesia'' sesuai daftar pustaka; ''Gao dkk., 2023'' pada keterangan Gambar II.4 menjadi ''Gao, Xiong, dkk., 2023'' (membedakan dua sumber Gao 2023); sumber sekunder ''Muroli dkk. (2020, sebagaimana dikutip dalam Simbolon & Gani, 2023)''; daftar pustaka: huruf miring pada judul karya mandiri dan nama jurnal beserta volume, indentasi gantung, urutan Gao (Churpek sebelum Tesch), dan entri Susilo ditambahkan ke daftar pustaka gabungan karena disitasi di Bab I.'
class: L3
status: APPROVED (pelaksanaan D-113; konfirmasi tim/pembimbing/prodi atas APA BELUM ada)
date: '2026-11-12'
related:
- D-113
- D-111
- D-104
- K1
basis: Jawaban pengguna 'seragamkan sitasi ke APA dulu' atas tawaran penyeragaman sitasi
alternatives_considered:
- Menunda sampai K1 dikonfirmasi tim
consequences: 'Diterapkan oleh skrip pada modular/TA1 bab 1.docx, modular/TA1 bab 2.docx, dan Draft-Bab1-Bab2.docx (cadangan di .scratch/backup_docx_1112b/); Markdown dibangkitkan ulang dari docx gabungan. Tidak ada isi substantif diubah. Temuan yang TIDAK diubah dan perlu dicek pengguna: (1) entri Zhang dkk. (2026) berakhir ''105053.3.'' (digit ''3'' tampak berlebih; belum diverifikasi ke sumber); (2) judul Simbolon & Gani (2023) memakai ''memengaruhi'' di Draft-Bab1-Bab2/TA1 bab 2 tetapi ''mempengaruhi'' di TA1 bab 1 (judul sumber harus sesuai terbitan asli, belum diverifikasi); (3) entri berbahasa Inggris tetap memakai ''In'' dan ''(Eds.)''; (4) PDF TA1 bab 1/2 tertinggal; (5) nomor halaman di daftar isi gabungan belum dihitung ulang.'
approval_evidence:
  question: Q-REC-f/K1 diputuskan APA (D-113); sesi Claude menawarkan 'menyeragamkan sitasi docx ke APA ... Mau lanjut ke Bab III, atau menyeragamkan sitasi ke APA dulu?'
  options_offered:
  - Lanjut ke Bab III
  - Seragamkan sitasi ke APA dulu
  user_answer:
  - seragamkan sitasi ke APA dulu
  answered_at: '2026-11-12'
  session_ref: sesi biasa (tanpa agent) 2026-11-12, dicatat langsung atas permintaan pengguna
  scope: Penyeragaman format sitasi ke APA pada docx resmi dan Markdown; bukan persetujuan tim/pembimbing/prodi
```

## D-118

```yaml
id: D-118
decision: 'Perubahan Bab I pada commit 80a13ba (revisi Paket A oleh a03, bab1/Bab_I_Draft.md +12/-10 baris) sah sebagai keputusan pengguna dan menggantikan D-115 sebatas perubahan itu; D-115 ditandai SUPERSEDED sebagian.'
class: L3
status: APPROVED (keputusan pengguna; persetujuan tim/pembimbing BELUM ada)
date: '2026-11-12'
related:
- D-115
- D-111
- D-119
- TSK-166
basis: Jawaban pengguna atas konflik C1 (ditemukan a13, TSK-165)
alternatives_considered:
- Opsi lain yang ditawarkan tidak tercatat lengkap di brief A01 (hanya opsi terpilih yang diteruskan)
consequences: 'D-115 tetap berlaku untuk bagian lain (penyesuaian keputusan/temuan/pertanyaan DRAF 24 dengan kondisi Bab I saat itu); lingkup supersede hanya perubahan Bab I di 80a13ba. Isi substantif perubahan Paket A tidak dinilai oleh A13; bila perubahan menyentuh rumusan masalah/tujuan/kontribusi, kecocokan dengan D-102 belum diverifikasi dan menjadi catatan untuk A01. Persetujuan tim/pembimbing tetap BELUM ada. TSK-166 dicatat DONE dengan jawaban ini sebagai approval_evidence.'
approval_evidence:
  question: 'Konflik C1 (ditemukan a13): memory mencatat D-115 "Bab I docx dibiarkan apa adanya" dan CONTEXT_TRANSFER melarang menulis revisi Bab I sebelum Approval Request, tetapi commit 80a13ba (Anda) sudah mengubah bab1/Bab_I_Draft.md (+12/-10 baris) lewat Paket A pada 12 Nov dini hari. Bagaimana status perubahan Bab I di 80a13ba?'
  options_offered:
  - 'Opsi terpilih (diteruskan A01): revisi Paket A sah; D-115 ditandai SUPERSEDED sebagian; TSK-166 DONE dengan jawaban ini sebagai approval_evidence'
  user_answer:
  - Keputusan saya, gantikan D-115
  answered_at: '2026-11-12'
  session_ref: sesi A01 2026-11-12 (/sesi-mulai), AskUserQuestion konflik C1; diteruskan A01 ke A13 dalam brief TSK-165 apply_reconcile
  scope: Perubahan Bab I pada commit 80a13ba menggantikan D-115 sebatas perubahan itu
```

## D-119

```yaml
id: D-119
decision: 'Naskah Bab I yang berlaku adalah Markdown bab1/Bab_I_Draft.md (sumber kebenaran Bab I); docx resmi Bab I (modular/TA1 bab 1.docx dan bagian Bab I pada 13523136-Proposal-IF4091-Capstone-Individu-2026-Draft-Bab1-Bab2.docx) berstatus USANG sampai diperbarui. Pembaruan docx menunggu Approval Request P2-02 tersendiri. Bab II tetap docx.'
class: L3
status: APPROVED (keputusan pengguna; persetujuan tim/pembimbing BELUM ada)
date: '2026-11-12'
related:
- D-111
- D-118
- D-49
- P2-02
basis: Jawaban pengguna atas konflik C2 (ditemukan a13, TSK-165)
alternatives_considered:
- Opsi lain yang ditawarkan tidak tercatat lengkap di brief A01 (hanya opsi terpilih yang diteruskan)
consequences: 'D-111 ditandai SUPERSEDED by D-119 sebagian (hanya sumber kebenaran Bab I). D-49 (sumber kebenaran Bab I = Markdown) sudah SUPERSEDED by D-111 sebagian; efeknya untuk Bab I kini sejalan lagi dengan D-119, tetapi status D-49 TIDAK diubah karena tidak ada instruksi eksplisit pengguna; diserahkan ke A01/pengguna bila ingin memulihkan secara formal. Build docx tidak disetujui oleh keputusan ini; P2-02 tetap berlaku. Butir baru di OPEN_QUESTIONS: pembaruan docx Bab I menunggu P2-02.'
approval_evidence:
  question: 'Konflik C2: setelah Paket A, bab1/Bab_I_Draft.md (Markdown) berbeda dari docx resmi Bab I (modular/TA1 bab 1.docx dan Draft-Bab1-Bab2.docx) yang di memory tercatat "sinkron" (D-111). Mana yang menjadi naskah Bab I yang berlaku sekarang?'
  options_offered:
  - 'Opsi terpilih (diteruskan A01): Markdown jadi sumber kebenaran Bab I; docx resmi Bab I ditandai USANG sampai diperbarui; build docx perlu Approval Request P2-02 tersendiri; D-111 sebagian SUPERSEDED untuk Bab I; Bab II tetap docx'
  user_answer:
  - Markdown berlaku, docx menyusul
  answered_at: '2026-11-12'
  session_ref: sesi A01 2026-11-12 (/sesi-mulai), AskUserQuestion konflik C2; diteruskan A01 ke A13 dalam brief TSK-165 apply_reconcile
  scope: Sumber kebenaran Bab I = Markdown; docx Bab I USANG; Bab II tidak berubah
```

## D-120

```yaml
id: D-120
decision: 'Pengumpulan bukti Bab III (PKT-B-A02, a02; .scratch/a02/bab3_evidence.md, status PARTIAL) sah dan Bab III resmi dibuka; syarat D-116 ("setelah rekonsiliasi selesai") dianggap terpenuhi setelah rekonsiliasi TSK-165 diterapkan. a02 dapat diminta melengkapi sisa scope sekali sebelum a03 menulis Bab III.'
class: L3
status: APPROVED (keputusan pengguna; persetujuan tim/pembimbing BELUM ada)
date: '2026-11-12'
related:
- D-116
- D-104
- D-105
- TSK-168
basis: Jawaban pengguna atas konflik C3 (ditemukan a13, TSK-165)
alternatives_considered:
- Opsi lain yang ditawarkan tidak tercatat lengkap di brief A01 (hanya opsi terpilih yang diteruskan)
consequences: 'D-116 tetap APPROVED dan kini terpenuhi. Isi Bab III mengikuti D-104 dan D-105. Bukti a02 berstatus PARTIAL: sebagian klaim TIDAK DIPERIKSA; halaman prosiding Lewis dan halaman cetak Wong belum diverifikasi; kualitas isi belum diaudit (belum ada laporan a02 ataupun QA). Tidak ada penulisan Bab III oleh keputusan ini.'
approval_evidence:
  question: 'Konflik C3: D-116 menyatakan Bab III dimulai "setelah rekonsiliasi selesai", tetapi pengumpulan bukti Bab III (PKT-B-A02, a02) sudah berjalan 12 Nov dan menghasilkan .scratch/a02/bab3_evidence.md (status PARTIAL ...). Bagaimana statusnya?'
  options_offered:
  - 'Opsi terpilih (diteruskan A01): TSK-168 PARTIAL sebagai pekerjaan sah; D-116 dianggap terpenuhi setelah rekonsiliasi ini diterapkan; a02 dapat diminta melengkapi sisa scope sekali sebelum a03 menulis Bab III'
  user_answer:
  - Sah; Bab III resmi dibuka
  answered_at: '2026-11-12'
  session_ref: sesi A01 2026-11-12 (/sesi-mulai), AskUserQuestion konflik C3; diteruskan A01 ke A13 dalam brief TSK-165 apply_reconcile
  scope: Pekerjaan PKT-B-A02 sah; Bab III dibuka; D-116 terpenuhi
```

## D-121

```yaml
id: D-121
decision: 'Akses berkas RSIA oleh sesi A01 pada 2026-11-12T05:21 (event rsia_access, target_hash 19e167c7bdb2) diizinkan pengguna secara pasca-fakta; dicatat tanpa isi data; manifest integritas RSIA dibuat. Tujuan akses tidak dinyatakan. Akses berikutnya tetap wajib brief sensitive_access.'
class: L3
status: APPROVED (keputusan pengguna; persetujuan tim/pembimbing BELUM ada)
date: '2026-11-12'
related:
- D-11
- D-17
- D-19
- TSK-165
basis: Jawaban pengguna atas konflik C4 (ditemukan a13, TSK-165)
alternatives_considered:
- Opsi lain yang ditawarkan tidak tercatat lengkap di brief A01 (hanya opsi terpilih yang diteruskan)
consequences: 'Isi berkas dan pengenal tidak dicatat di memory (S11). Tujuan akses: tidak dinyatakan. Aturan D-11/D-17/D-19 tidak berubah. Manifest dibuat lewat check_memory.py --init-rsia-manifest (hasil di TSK-165).'
approval_evidence:
  question: 'Konflik C4: log hook mencatat satu akses berkas RSIA (rsia_access, hash target 19e167c7bdb2) oleh sesi A01 pada 2026-11-12 pukul 05:21 tanpa brief sensitive_access ... Apakah akses itu Anda izinkan, dan bagaimana mencatatnya (tanpa memuat isi data)?'
  options_offered:
  - 'Opsi terpilih (diteruskan A01): izinkan, catat, dan buat manifest'
  user_answer:
  - Diizinkan; catat + buat manifest
  answered_at: '2026-11-12'
  session_ref: sesi A01 2026-11-12 (/sesi-mulai), AskUserQuestion konflik C4; diteruskan A01 ke A13 dalam brief TSK-165 apply_reconcile
  scope: Akses RSIA 2026-11-12T05:21 diizinkan pasca-fakta; pembuatan manifest; tanpa isi data
```
