---
name: create-skill
description: Create new OpenCode skills following the skill definition standard
version: "1.0"
author: developer
audience: developer
workflow: opencode
---

# Create Skill

Create a new reusable skill for OpenCode agents.

## When to Use

When you need to codify a repeatable workflow that multiple agents or sessions will follow. Skills are loaded on demand; they don't run automatically.

## How to Create a Skill

### 1. Create the directory

```bash
mkdir .opencode/skills/<skill-name>/
```

Naming rules:
- 1–64 characters
- Lowercase alphanumeric with single hyphens
- Cannot start or end with hyphen, no consecutive hyphens
- Must match the directory name exactly

### 2. Create SKILL.md

```markdown
---
name: <skill-name>
description: <1-sentence description, 10-100 characters>
version: "1.0"
author: <agent-name>
audience: <agent-name | all-agents>
workflow: <workflow-category>
---

# <Skill Title>

<One paragraph explaining what this skill does and when to use it.>

## When to Use

<Specific trigger conditions>

## Step-by-Step

### 1. <First step>
<Instructions>

### 2. <Second step>
<Instructions>

## Checklist

- [ ] <Verification item>
```

### 3. Keep it lean

Skills are loaded into context. Long skills consume tokens. Target:
- < 150 lines for focused workflow skills
- < 250 lines for complex multi-phase skills

Cut:
- Exhaustive examples when one is enough
- Reference documentation (link to it instead)
- Boilerplate CI/CD YAML (it belongs in `.github/`, not skills)

### 4. Reference from agents

Add the skill name to the agent's "Available Skills" section so the agent knows to load it.

## Available Skills in This Project

| Skill | Used By | Purpose |
|---|---|---|
| `session-workflow` | all agents | Session start/end protocol |
| `scope` | product-owner | Step 1: define acceptance criteria |
| `tdd` | developer | Step 3: write failing tests |
| `implementation` | developer | Step 4: Red-Green-Refactor |
| `verify` | reviewer | Step 5: run commands and review code |
| `code-quality` | developer | Redirects to `verify` (quick reference) |
| `pr-management` | developer | Create PRs with proper format |
| `git-release` | developer | Calver versioning and release naming |
| `create-skill` | developer | Create new skills |
