---
name: create-agent
description: Creates new OpenCode subagents following the agent definition standard
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: opencode
---
## What I do
Create new OpenCode subagent definitions following the OpenCode agent standard.

## When to use me
Use this when you need to create a new specialized subagent for OpenCode.

## How to create an agent
Create a markdown file in `.opencode/agents/<agent-name>.md` with:
- YAML frontmatter with agent configuration
- System prompt describing the agent's behavior

## Frontmatter options
- `description`: Brief description of what the agent does (required)
- `mode`: "primary", "subagent", or "all" (default: "all")
- `model`: Override the default model
- `temperature`: Control randomness (0.0-1.0)
- `tools`: Enable/disable specific tools
- `hidden`: Hide from @ autocomplete (for internal agents)
- `permission`: Configure tool permissions

## Example agent definition
```
---
description: Reviews code for quality and best practices
mode: subagent
model: anthropic/claude-sonnet-4-20250514
temperature: 0.1
tools:
  write: false
  edit: false
  bash: false
---
You are a code reviewer. Focus on:
- Code quality and best practices
- Potential bugs and edge cases
- Performance implications
- Security considerations

Provide constructive feedback without making direct changes.
```

## Tool configuration
```
tools:
  write: true
  edit: true
  bash: true
  read: true
  grep: true
  glob: true
  task: true
  skill: true
```

## Permission configuration
```
permission:
  edit: ask
  bash:
    "*": ask
    "git status *": allow
    "grep *": allow
  webfetch: deny
```

## Common agent types
- **subagent**: Specialized assistant for specific tasks
- **primary**: Main assistant (like build/plan)
- **readonly**: Read-only analysis agent
- **reviewer**: Code review agent
- **debugger**: Investigation-focused agent
- **docs**: Documentation writing agent
