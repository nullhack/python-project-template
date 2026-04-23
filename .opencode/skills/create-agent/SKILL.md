---
name: create-agent
description: Create new OpenCode agents with research-backed design patterns and industry standards
version: "1.0"
author: human-user
audience: human-user
workflow: opencode
---

# Create Agent

Create a new OpenCode agent following research-backed best practices from OpenAI, Anthropic, and scientific literature.

## When to Use

When you need a new agent with distinct ownership, instructions, tool surface, or approval policy. Not for simple routing — only when the task requires a separate domain of responsibility.

## How to Create an Agent

### 0. Research (mandatory — do this first)

Before writing any agent, research the domain to ground the agent design in industry standards and scientifically-backed evidence:

1. **Identify the agent's domain**: What role, responsibility, and domain will this agent own?
2. **Search for domain-specific best practices**:
   - For agent architecture: OpenAI Agents SDK, Anthropic Claude Agent SDK, Google Agents SDK
   - For domain methodology: Academic papers, vendor guides, established standards (e.g., OWASP for security, IEEE for software engineering)
   - For known failure modes: Post-mortems, case studies, industry reports
3. **Synthesize conclusions**: What ownership boundaries work? What tool design patterns? What escalation rules?
4. **Embed as design decisions**: Write the agent's ownership definition, instruction patterns, tool surface, and escalation rules based on those conclusions — not as citations but as direct guidance

**Example research synthesis:**
```
Agent domain: Security reviewer agent
Research: OWASP Testing Guide, NIST security controls, Anthropic's adversarial verification patterns
Conclusion: Security agents should assume breach by default, escalate on any critical finding, use defence-in-depth checklist.
→ Agent design: "role: reviewer", "escalation: any critical = human", "tool: security-scan + vuln-check"
```

### 1. Create the agent file

```bash
mkdir -p .opencode/agents/
```

Create `.opencode/agents/<agent-name>.md`:

```markdown
---
name: <agent-name>
description: <1-sentence description of what this agent does>
role: <product-owner | system-architect | software-engineer | setup-project | human-user>
steps: <step numbers this agent owns, e.g., "2, 3">
---

# <Agent Name>

[Brief description of the agent's purpose and when it's invoked.]

## Role

<What this agent does in the workflow.>

## Available Skills

| Skill | When to Load | Purpose |
|---|---|---|
| `run-session` | Every session | Session start/end protocol |
| `<skill-name>` | When needed | <What the skill provides> |

## Instructions

<Detailed instructions for this agent. Include:>

- When to invoke this agent (trigger conditions)
- What steps it owns
- How to use tools
- When to escalate or hand off
```

### 2. Follow the structural rules

Apply the research conclusions about file organisation:

| File | When Loaded | Content | Avoid |
|---|---|---|---|
| `AGENTS.md` | Always | Shared conventions, commands | Workflow details |
| `.opencode/agents/*.md` | When role invoked | Role identity, step ownership, skill loads, tool permissions | Duplication |
| `.opencode/skills/*.md` | On demand | Full procedural instructions | Duplication |

**Why**: Keeping always-loaded files lean preserves attention budget for the task at hand.

### 3. Define clear ownership boundaries

**Split criteria**:
- Separate ownership (different domain responsibility)
- Different instructions (not just more detail)
- Different tool surface (distinct actions)
- Different approval policy (escalation rules)

**Anti-pattern**: Creating agents just to organise instructions. A single agent with more tools is usually better than multiple agents.

### 4. Write effective instructions

Write instructions that work in practice:

- **Specific triggers**: "Load this skill when X" not "use judgment"
- **Clear actions**: Every step corresponds to a specific output
- **Concrete examples**: Include before/after code where helpful
- **Verification criteria**: How does the agent know it's done?

### 5. Define tool permissions

Design the tool surface based on what the agent needs to accomplish:

- **Start with bash** for breadth
- **Promote to dedicated tools** when you need to:
  - Gate security-sensitive actions
  - Render structured output
  - Audit usage patterns
  - Serialize vs. parallelize

### 6. Add to AGENTS.md

Register the agent in the workflow section of `AGENTS.md`:

```markdown
## Agents

| Agent | Role | Steps | Skills |
|-------|------|-------|--------|
| <name> | <role> | <steps> | <skills> |
```

## Agent Template

```markdown
---
name: <agent-name>
description: <what this agent does, 1 sentence>
role: <product-owner | system-architect | software-engineer | setup-project | human-user>
steps: <owned steps, e.g., "2-3">
---

# <Agent Title>

<2-3 paragraphs: what this agent does, when invoked, what it delivers.>

## Context

<What this agent knows/has access to>

## Available Skills

- `run-session` — always
- `<skill>` — when <trigger>

## Instructions

### Step <N>: <Step Name>

1. <Specific action>
2. <Specific action>
3. <Verification>

### Hand-off

When to transfer to <other agent>: <condition>

## Tool Permissions

- Read files: <scope>
- Write files: <scope>
- Execute commands: <scope>
- Network access: <yes/no>

## Escalation

When to escalate to human: <conditions>
```

## Existing Agents in This Project

| Agent | Role | Steps | Purpose |
|---|---|---|---|
| `product-owner` | product-owner | 1, 5 | Scope discovery, acceptance |
| `system-architect` | system-architect | 2, 4 | Architecture, adversarial verification |
| `software-engineer` | software-engineer | 3, 5 | TDD, releases |
| `setup-project` | setup-project | meta | Initialize new projects |

## Best Practices Summary

1. **Start with a single agent** — add more only when ownership boundaries are clear
2. **Define ownership, not volume** — separate domains, not instruction sets
3. **Keep instructions specific** — concrete triggers, not vague guidance
4. **Match tools to security needs** — bash for flexibility, dedicated tools for gating
5. **Test with real usage** — iterate based on failures
6. **Reference, don't duplicate** — link to skills and AGENTS.md, don't copy content