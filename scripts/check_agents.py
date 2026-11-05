"""Static validation of the 13 fixed agents (docs/AGENT_SPECIFICATIONS.md §6, T-07, T-20).

Checks: exactly 13 agent files a01..a13 and no 14th; required frontmatter; subagents have omitClaudeMd and no
Agent tool; a01's Agent(...) allowlist names exactly a02..a13; each body has '## Batas' and
'## Kontrak keluaran'; policy agents match the roster; every 'RULES.md §x' / 'CLAUDE.md §x' reference in the
rules-map skill resolves to a heading. Exit 1 on any failure.
"""
import json, re, sys
from _common import ROOT, POLICY_PATH

AGENTS = ROOT / ".claude" / "agents"
ROSTER = ["a01-orchestrator", "a02-research-evidence", "a03-academic-writer", "a04-supervisor",
          "a05-critical-reviewer", "a06-cross-proposal", "a07-qa-academic", "a08-qa-citation",
          "a09-qa-editorial", "a10-qa-structure", "a11-qa-technical", "a12-qa-integrity", "a13-memory-manager"]
RULES_MAP = ROOT / ".claude" / "skills" / "if4091-rules-map" / "SKILL.md"


def frontmatter(text):
    import yaml
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    return (yaml.safe_load(m.group(1)), m.group(2)) if m else (None, text)


def split_tools(s):
    out, depth, cur = [], 0, ""
    for ch in s or "":
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    return [t for t in out + [cur.strip()] if t]


def heading_exists(text, num):
    return re.search(rf"^#{{2,3}} {re.escape(num)}[ .]", text, re.M) is not None


def main():
    errors = []
    files = sorted(AGENTS.glob("*.md"))
    names = [f.stem for f in files]
    if names != ROSTER:
        extra = sorted(set(names) - set(ROSTER))
        missing = [r for r in ROSTER if r not in names]
        errors.append(f"roster tidak tepat 13: kurang {missing}, berlebih {extra}")
    for f in files:
        fm, body = frontmatter(f.read_text(encoding="utf8"))
        if not fm:
            errors.append(f"{f.name}: tanpa frontmatter")
            continue
        if fm.get("name") != f.stem:
            errors.append(f"{f.name}: name '{fm.get('name')}' tidak sama dengan nama berkas")
        if not fm.get("description"):
            errors.append(f"{f.name}: description kosong")
        tools = split_tools(fm.get("tools"))
        if f.stem == "a01-orchestrator":
            agent_tool = [t for t in tools if t.startswith("Agent(")]
            allowed = [a.strip() for a in agent_tool[0][6:-1].split(",")] if agent_tool else []
            if allowed != ROSTER[1:]:
                errors.append(f"a01: allowlist Agent(...) harus tepat a02–a13, ditemukan {allowed}")
            for t in ("SendMessage", "AskUserQuestion"):
                if t not in tools:
                    errors.append(f"a01: tool {t} tidak tercantum")
            if any(t in tools for t in ("Write", "Edit", "NotebookEdit")):
                errors.append("a01: tidak boleh memiliki tool tulis")
        else:
            if any(t == "Agent" or t.startswith("Agent(") for t in tools):
                errors.append(f"{f.stem}: subagent tidak boleh memiliki tool Agent (D-02)")
            if fm.get("omitClaudeMd") is not True:
                errors.append(f"{f.stem}: omitClaudeMd harus true (D-03)")
            if "agent-contract" not in (fm.get("skills") or []):
                errors.append(f"{f.stem}: skill agent-contract tidak dipreload")
        for h in ("## Batas", "## Kontrak keluaran"):
            if h not in body:
                errors.append(f"{f.stem}: bagian '{h}' tidak ada")
    policy = json.loads(POLICY_PATH.read_text(encoding="utf8"))
    if sorted(policy["agents"]) != sorted(ROSTER):
        errors.append("write_scopes.json: daftar agent tidak sama dengan roster")
    spec = (ROOT / "docs" / "AGENT_SPECIFICATIONS.md").read_text(encoding="utf8")
    m = re.search(r"```json\n(.*?)\n```", spec[spec.find("## 4. Draf kebijakan izin"):], re.S)
    if not m or json.loads(m.group(1)) != policy:
        errors.append("AGENT_SPECIFICATIONS.md §4 tidak identik dengan .claude/policy/write_scopes.json")
    srcs = {"RULES.md": (ROOT / "RULES.md").read_text(encoding="utf8"),
            "CLAUDE.md": (ROOT / "CLAUDE.md").read_text(encoding="utf8")}
    refs = 0
    for line in RULES_MAP.read_text(encoding="utf8").splitlines():
        for doc, nums in re.findall(r"(RULES\.md|CLAUDE\.md) ((?:§[\d.]+(?:–§[\d.]+)?(?:, )?)+)", line):
            for num in re.findall(r"§(\d+(?:\.\d+)?)", nums):
                refs += 1
                if not heading_exists(srcs[doc], num):
                    errors.append(f"if4091-rules-map: {doc} §{num} tidak ditemukan sebagai heading")
    if errors:
        print("check_agents: GAGAL")
        for e in errors:
            print("  - " + e)
        return 1
    print(f"check_agents: OK (13 agent, {refs} rujukan aturan valid)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
