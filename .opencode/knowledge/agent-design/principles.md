---
domain: agent-design
tags: [agents, identity, subagents, separation-of-concerns]
last-updated: 2026-04-29
---

# Agent Design Principles

## Key Takeaways

- Agents contain identity only (who I am, what I decide); the flow YAML is the source of truth for routing, skills, and artifacts.
- Use subagents for investigation tasks that rapidly exhaust context; they quarantine token cost and prevent anchoring bias (Tversky & Kahneman, 1974).
- Maintain a three-file separation (AGENTS.md, agents, skills) to prevent conflicting instructions from competing sources, positional attention degradation (Liu et al., 2023), and redundant content creating competing attention targets.
- Agents are minimal — the flow determines which skill to load, the skill determines how to do the work, the knowledge provides the reference material.
- AGENTS.md must discover, not enumerate — provide discovery commands and naming conventions, never file inventories that go stale.

## Concepts

**Agent = Identity Only**: The agent file defines who the agent is and what it decides. It does NOT contain skill lists, ownership tables, routing logic, artifact paths, or knowledge references. The flow YAML is the single source of truth for routing (owner, skills, transitions, artifacts). Duplicating any of these in the agent creates a second source of truth that will drift.

**Three-File Separation**: Three failure modes observed in LLM context windows produce a three-file split:
- **Conflicting instructions** from multiple sources — each concern has one file
- **Positional attention degradation** (Liu et al., 2023 — middle content receives less attention) — keep files short
- **Redundant content** creating competing attention targets — each fact in one location

| Concern | File | Purpose | Loaded When |
|---|---|---|---|
| Navigation | `AGENTS.md` | Where files live, how to resolve wikilinks | Every session |
| Identity | `.opencode/agents/*.md` | Who I am, what I decide | When role invoked |
| Procedure | `.opencode/skills/*/SKILL.md` | Step-by-step instructions | On demand |
| Reference | `.opencode/knowledge/*/` | What and why | On demand, via wikilinks |

**Subagents for Investigation**: When a task requires extensive reading (auditing code, researching decisions), use a subagent with read-only or restricted permissions. Subagents quarantine token cost and prevent anchoring bias from the main conversation context.

**Effective Instruction Writing**: Specific IF-THEN triggers at decision points are 2-3x more likely to execute than general intentions (Gollwitzer, 1999). But these triggers belong in the skill steps at the decision point, NOT in the agent file. The agent file is too far from the work context for triggers to be effective.

**Discover, Don't Enumerate**: AGENTS.md must never enumerate files that can go stale. Instead, it provides discovery commands (`ls`, `find`) and file naming conventions so agents discover what exists at runtime. This prevents drift between documentation and reality — an inventory that lists 30 skills will be wrong the moment a skill is added or removed, but a discovery command is always correct.

**Naming Distinction**: `AGENTS.md` (project root) is the navigation file loaded every session. `.opencode/agents/*.md` are agent identity files loaded on demand. Despite the similar names, they serve different purposes: AGENTS.md tells you where things are; agent files tell you who you are.

**Research Notes Are Consultable, Not Session-Loaded**: Research notes in `docs/research/` are source material cited by knowledge files. They are not loaded every session. An agent consults them only when a knowledge file references them and more detail is needed.

## Content

### Agent File Format

```markdown
---
description: "<role> — <one-line summary>"
mode: subagent
temperature: <0.3-0.7>
---

# <Role Name>

You are the <Role Name>. <One-sentence identity>.
<One-sentence decision authority>.
```

That is the entire agent. No skill lists, no ownership tables, no IF-THEN triggers, no knowledge references, no routing.

### What NOT to Put in an Agent File

- **Skill lists** — the flow `skills` field determines which skill to load
- **Ownership tables** — the flow `input/edited/output_artifacts` defines what each state reads and writes
- **Routing logic** — the flow `next` field defines transitions
- **Knowledge references** — the skill's `## Load` section handles knowledge loading
- **Step procedures** — skills contain procedure, agents contain identity
- **Quality gates** — the flow `conditions` field defines gate conditions

### AGENTS.md Is Navigation Only

AGENTS.md is loaded every session. It should contain ONLY:
- Where files live (project structure)
- How to resolve wikilinks
- Session protocol (use `flowr status`, `flowr advance`)
- File naming conventions
- Discovery commands (not file inventories)

It must NOT contain quality gates, priority orders, step procedures, knowledge content, or file enumerations.

### Naming Conventions

| Path | Purpose | Loaded When |
|---|---|---|
| `/AGENTS.md` | Root navigation (where things are, how to discover them) | Every session |
| `.opencode/agents/{role}.md` | Agent identity (who I am, what I decide) | When role invoked |
| `.opencode/skills/{skill}/SKILL.md` | Skill procedure (step-by-step instructions) | On demand |
| `.opencode/knowledge/{domain}/{concept}.md` | Knowledge reference (progressive disclosure) | On demand, via wikilinks |
| `.templates/{path}.template` | Artifact templates | When creating artifacts |
| `docs/research/{domain}/{concept}.md` | Research source notes (cited by knowledge files) | When knowledge file references them |
| `docs/adr/ADR_YYYYMMDD_{slug}.md` | Architecture decision records | When referenced |

Note: Despite similar names, `AGENTS.md` (root navigation) and `.opencode/agents/` (identity files) serve different purposes.

## Related

- [[skill-design/principles]]
- [[knowledge-design/principles]]
- [[workflow/flowr-spec]]