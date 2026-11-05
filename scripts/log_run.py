"""SubagentStart/SubagentStop hook: append one metadata line to .scratch/agent_runs.jsonl (§A-12.6).

Only timing and identity are recorded (no prompts, no tool content), so the log can never carry RSIA data.
On SubagentStart it also injects the resolved skill script paths for agents that have `skill_scripts` in the
policy (D-20: only a12), so the absolute path (it contains the Windows account name) never has to be written
into a committed prompt. The hook never blocks: it always exits 0.
"""
import json, sys
from _common import RUNS_LOG, SKILLS_DIR, append_jsonl, load_policy, now_iso


def skill_context(agent):
    """Additional context naming the skill scripts an agent may run (policy skill_scripts), or '' if none."""
    try:
        cfg = load_policy()["agents"].get(agent) or {}
    except (OSError, ValueError, KeyError):
        return ""
    scripts = cfg.get("skill_scripts") or []
    if not scripts or not SKILLS_DIR:
        return ""
    lines = [f"Path skill user-level untuk {agent} (hasil resolve <SKILL_DIR:...>, D-20). "
             "Tulis path persis seperti ini, dalam tanda kutip ganda, dengan garis miring maju:"]
    lines += [f'- python "{SKILLS_DIR}/{s}"' for s in scripts]
    return "\n".join(lines)


def main():
    try:
        p = json.loads(sys.stdin.read() or "{}")
    except ValueError:
        p = {}
    event = p.get("hook_event_name", "unknown")
    agent = p.get("agent_type") or p.get("subagent_type") or ""
    append_jsonl(RUNS_LOG, {
        "ts": now_iso(),
        "event": event,
        "agent_type": agent,
        "agent_id": p.get("agent_id") or "",
        "session_id": p.get("session_id") or "",
    })
    if event == "SubagentStart":
        ctx = skill_context(agent)
        if ctx:
            print(json.dumps({"hookSpecificOutput": {"hookEventName": "SubagentStart", "additionalContext": ctx}},
                             ensure_ascii=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
