---
file: DECISION_LOG
revision: 13
status: CURRENT
updated: 2026-11-06
updated_by: a13-memory-manager
based_on_commit: b005ff0
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
