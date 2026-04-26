---
domain: agent-design
tags: [agents, best-practices, ownership, context-isolation, research-backed]
last-updated: 2026-04-26
---

# Agent Design Principles

## Key Takeaways

- Define the smallest agent that can own a clear task; add agents only for separate ownership, different instructions, different tool surface, or different approval policy.
- Use subagents for investigation tasks that rapidly exhaust context; they quarantine token cost and prevent anchoring bias.
- Maintain a three-file separation (AGENTS.md, agents, skills) to prevent instruction conflict, positional attention degradation, and redundancy interference.
- Embed specific IF-THEN triggers at decision points, not vague references; error-specific feedback is actionable, vague feedback is not.

## Concepts

**Minimal-Scope Agent Design**: Define the smallest agent that can own a clear task. Add more agents only for separate ownership, different instructions (not just more detail), different tool surface, or different approval policy. The split criterion is ownership boundary, not instruction volume. Anti-pattern: creating agents just to organize instructions.

**Context Isolation via Subagents**: Subagents run in their own context windows and report back summaries. This keeps the primary conversation clean for implementation. Every file read in a subagent burns tokens in a child window, not the primary window. Context window is the primary performance constraint for LLM agents. A fresh context also prevents anchoring bias from prior conversation state.

**Three-File Separation**: Three failure modes (instruction conflict, positional attention degradation, redundancy interference) produce a three-file split with defined content rules: AGENTS.md (every session, project conventions), agents (when role invoked, role identity), skills (on demand, procedural instructions), and knowledge (on demand, reference + explanation only).

**Effective Instruction Writing and Tool Permission Design**: Specific triggers at decision points are 2-3x more likely to execute than general intentions. Error-specific feedback like "FAIL: function > 20 lines at file:47" is actionable; "Apply function length rules" is not. Agent-Computer Interface design is as important as Human-Computer Interface design: start with bash for breadth, promote to dedicated tools for security, structured output, or audit patterns.

## Content

### Minimal-Scope Agent Design

Define the smallest agent that can own a clear task. Add more agents only when you need:
- **Separate ownership** — different domain responsibility
- **Different instructions** — not just more detail, but fundamentally different guidance
- **Different tool surface** — distinct actions and permissions
- **Different approval policy** — different escalation rules

The split criterion is **ownership boundary**, not instruction volume. A single agent with more tools is usually better than multiple agents that share the same domain. (Source: OpenAI Agents SDK, 2024; research entry #21.)

Anti-pattern: Creating agents just to organize instructions. If two agents need the same knowledge and perform similar actions, they should be one agent with skill-based differentiation.

### Context Isolation via Subagents

Subagents run in their own context windows and report back summaries. This keeps the primary conversation clean for implementation. Every file read in a subagent burns tokens in a child window, not the primary window.

Context window is the primary performance constraint for LLM agents. Investigation tasks rapidly exhaust context if done inline. Delegating to a subagent quarantines that cost; the primary agent receives only the distilled result. A fresh context also prevents anchoring bias from prior conversation state. (Source: Anthropic, 2025; research entry #22.)

### Three-File Separation

Three failure modes converge to produce a three-file split with defined content rules:

| Failure Mode | Source | Prevention |
|---|---|---|
| Instruction conflict on drift | Entry #24 — LLMs cannot reliably resolve conflicting instructions | Single source of truth per concern |
| Positional attention degradation | Entry #25 — Middle content gets less attention | Keep always-loaded files lean |
| Redundancy interference | Entry #26 — Redundant content creates competing attention targets | De-duplicate across all files |

| File | When Loaded | Contains | Must NOT Contain |
|---|---|---|---|
| `AGENTS.md` | Every session | Project conventions, commands, formats | Step procedures, role-specific rules, knowledge |
| `.opencode/agents/*.md` | When role invoked | Role identity, skill loads, permissions, escalation | Workflow details, knowledge content |
| `.opencode/skills/*/SKILL.md` | On demand | Procedural instructions, self-contained | Duplication of `AGENTS.md` or other skills |
| `.opencode/knowledge/` | On demand | Reference + explanation only | Procedural instructions, step-by-step workflows |

### Effective Instruction Writing

- **Specific triggers**: "Load skill X when condition Y" not "use judgment"
- **Clear actions**: Every step corresponds to a specific output
- **Concrete examples**: Include before/after code where helpful (one is enough)
- **Verification criteria**: How does the agent know it's done?
- **Implementation intentions**: "If X then Y" plans are 2–3x more likely to execute than general intentions (Source: Gollwitzer, 1999; entry #2.)
- **Error-specific feedback**: "FAIL: function > 20 lines at file:47" is actionable; "Apply function length rules" is not (Source: Hattie & Timperley, 2007; entry #9.)

### Tool Permission Design (ACI)

Agent-Computer Interface design is as important as Human-Computer Interface design. More time was spent optimizing tools than prompts in SWE-bench work. (Source: Anthropic Engineering Blog, 2024.)

- Start with bash for breadth
- Promote to dedicated tools when you need to: gate security-sensitive actions, render structured output, audit usage patterns
- Poka-yoke your tools: make the right action easy and the wrong action hard
- Give agents enough tokens to think — truncating tool descriptions to save tokens often costs more in misunderstandings

### Adversarial Verification

The reviewer's job is to try to break the feature, not to confirm it works. Default hypothesis: "it might be broken despite green checks; prove otherwise."

Highest-quality thinking emerges when parties hold different hypotheses and are charged with finding flaws in each other's reasoning. (Source: Mellers, Hertwig, & Kahneman, 2001; entry #5.)

Accountability to an unknown audience improves reasoning quality. Structured PASS/FAIL tables with evidence columns create commitment-device effects. (Source: Cialdini, 2001; entry #3; Tetlock, 1983; entry #6.)

## Related

- [[agent-design/opencode-format]]
- [[skill-design/principles]]
- [[knowledge-design/principles]]