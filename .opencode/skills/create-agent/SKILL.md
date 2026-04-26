---
name: create-agent
description: Create new OpenCode agents with research-backed design patterns
version: "2.0"
author: human-user
audience: human-user
workflow: opencode
---

# Create Agent

Create a new OpenCode agent following research-backed best practices.

## When to Use

When you need a new agent with distinct ownership, instructions, tool surface, or approval policy. Not for simple routing — only when the task requires a separate domain of responsibility.

## Step-by-Step

### 1. Research

Before writing any agent, research the domain:

1. Identify the agent's domain: role, responsibility, and ownership
2. Search for domain-specific best practices (OpenAI Agents SDK, Anthropic Claude Agent SDK, academic papers)
3. Read [[agent-design/principles#concepts]] for research-backed design patterns
4. Synthesize conclusions into ownership boundaries, instruction patterns, tool surfaces, and escalation rules

### 2. Create the agent file

```bash
mkdir -p .opencode/agents/
```

Create `.opencode/agents/<agent-name>.md`. Read [[agent-design/opencode-format]] for the complete frontmatter specification and permission options.

### 3. Define ownership boundaries

Read [[agent-design/principles#concepts]] — specifically the "Minimal-Scope Agent Design" and "Split Criteria" sections. Only create a new agent when you need:
- Separate ownership (different domain responsibility)
- Different instructions (not just more detail)
- Different tool surface (distinct actions)
- Different approval policy (escalation rules)

Anti-pattern: creating agents just to organize instructions.

### 4. Write effective instructions

Read [[agent-design/principles#concepts]] — specifically the "Effective Instruction Writing" section. Include:
- Specific triggers ("Load skill X when condition Y")
- Clear actions (every step corresponds to a specific output)
- Concrete examples (one is enough)
- Verification criteria (how does the agent know it's done?)

### 5. Define tool permissions

Read [[agent-design/principles#concepts]] — specifically the "Tool Permission Design" section. Design the tool surface based on what the agent needs to accomplish:
- Start with bash for breadth
- Promote to dedicated tools when you need gating, structured output, or auditing
- Use permission patterns from [[agent-design/opencode-format]]

### 6. Add to AGENTS.md

Register the agent in the workflow section of `AGENTS.md`:

```markdown
## Agents

| Agent | Role | Steps | Skills |
|-------|------|-------|--------|
| <name> | <role> | <steps> | <skills> |
```

## Checklist

- [ ] Agent has a clear ownership boundary (not just "more instructions")
- [ ] Frontmatter follows [[agent-design/opencode-format#key-takeaways]] spec
- [ ] Instructions use specific triggers, not vague guidance
- [ ] Tool permissions match the agent's domain needs
- [ ] Agent registered in `AGENTS.md`
- [ ] No knowledge content embedded — all references use `[[domain/concept]]` wikilinks

## Existing Agents in This Project

| Agent | Role | Steps | Purpose |
|---|---|---|---|
| `product-owner` | product-owner | 1, 5 | Scope discovery, acceptance |
| `system-architect` | system-architect | 2, 4 | Architecture, adversarial verification |
| `software-engineer` | software-engineer | 3, 5 | TDD, releases |
| `setup-project` | setup-project | meta | Initialize new projects |