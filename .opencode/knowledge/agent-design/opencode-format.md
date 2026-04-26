---
domain: agent-design
tags: [agents, opencode, format, configuration]
last-updated: 2026-04-26
---

# OpenCode Agent Format

## Key Takeaways

- Agent files live at `.opencode/agents/<name>.md` (project) or `~/.config/opencode/agents/<name>.md` (global); the filename becomes the agent name.
- Frontmatter requires `description` and `mode` (primary/subagent/all); optional fields include model, temperature, steps, permissions, and more.
- Body sections in order: Role, Available Skills, Instructions, Escalation; write in third person.
- Permission values are `allow` (run immediately), `ask` (prompt user), `deny` (hidden/rejected); wildcards supported, last matching rule wins.

## Concepts

**File Location and Naming**: Agent files are discovered at `.opencode/agents/<name>.md` (project-level) and `~/.config/opencode/agents/<name>.md` (global). The filename without `.md` becomes the agent name. Project-level takes precedence.

**YAML Frontmatter Fields**: Required fields are `description` (1-sentence, shown in agent selection) and `mode` (primary for main agents, subagent for agents invoked by others, all for either). Key optional fields: `model` (override default model), `steps` (max agentic iterations), `hidden` (hide subagents from autocomplete), `permission` (fine-grained tool access control), `prompt` (custom system prompt).

**Body Structure**: Body sections in order: Role (who the agent is and what it owns), Available Skills (which skills to load and when), Instructions (step-by-step actions), Escalation (when to hand off).

**Permission Patterns**: Permission values are `allow` (run immediately), `ask` (prompt user), `deny` (hidden/rejected); wildcards are supported and the last matching rule wins. Common patterns: Read-only (deny edit, ask bash), Build (allow edit and bash), Restricted (ask for both).

## Content

### File Locations

- Project: `.opencode/agents/<name>.md`
- Global: `~/.config/opencode/agents/<name>.md`

The filename (without `.md`) becomes the agent name.

### YAML Frontmatter

```yaml
---
description: <1-sentence description>  # Required
mode: primary | subagent | all       # Required
model: <provider/model-id>           # Optional; inherits from primary
temperature: <0.0-1.0>               # Optional; model default
steps: <integer>                      # Optional; max agentic iterations
disable: true | false                 # Optional; default false
hidden: true | false                   # Optional; subagent only; hides from @ autocomplete
prompt: <text or {file:./path}>       # Optional; custom system prompt
color: <hex or theme-color>           # Optional; UI color
top_p: <0.0-1.0>                      # Optional; response diversity
permission:
  edit: allow | ask | deny
  bash:
    "*": ask | allow | deny            # Wildcard; last matching rule wins
    "git status *": allow              # Specific command patterns
  webfetch: allow | ask | deny
  skill:
    "<skill-name>": allow | deny
  task:
    "*": deny | allow
    "<agent-name>": allow
---
```

### Key Fields

- **description** (required): What the agent does and when to use it. Shown in agent selection.
- **mode**: `primary` for main agents, `subagent` for agents invoked by others, `all` for either.
- **model**: Override the default model. Subagents inherit the invoking primary's model unless specified.
- **steps**: Maximum agentic iterations before forced text-only response.
- **hidden**: Only for `mode: subagent`. Hides from `@` autocomplete but still invokable via Task tool.
- **permission.task**: Controls which subagents this agent can invoke via the Task tool. Glob patterns supported; last matching rule wins.

### Permission Values

| Value | Behavior |
|---|---|
| `allow` | Tool runs immediately without approval |
| `ask` | User prompted for approval before running |
| `deny` | Tool hidden from agent, access rejected |

### Markdown Body

After frontmatter, write the agent's instructions. Key sections:

1. **Role** — who the agent is and what it owns
2. **Available Skills** — which skills to load and when
3. **Instructions** — step-by-step actions for each owned step
4. **Escalation** — when to hand off to another agent or human

### Common Permission Patterns

| Pattern | edit | bash | Use Case |
|---|---|---|---|
| Read-only | deny | ask (specific: allow git read commands) | Review, analysis |
| Build | allow | allow | Full development |
| Restricted | ask | ask | Planning, cautious editing |

## Related

- [[agent-design/principles]]
- [[skill-design/opencode-format]]