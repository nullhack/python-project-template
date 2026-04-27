---
name: create-skill
description: Create new OpenCode skills following the skill definition standard
version: "3.0"
author: software-engineer
audience: software-engineer
workflow: opencode
---

# Create Skill

Create a new reusable skill for OpenCode agents.

## When to Use

When you need to codify a repeatable workflow that multiple agents or sessions will follow. Skills are loaded on demand; they don't run automatically.

## Step-by-Step

### 1. Research

Before writing any skill, research the domain:

1. Identify the domain: what workflow or methodology will this skill codify?
2. Search for best practices (academic sources, vendor documentation, industry standards)
3. Read existing research in `docs/research/` for related entries
4. Read [[skill-design/principles#concepts]] for research-backed skill design patterns
5. Synthesize conclusions into actionable guidance embedded directly in steps

### 2. Create the directory

```bash
mkdir .opencode/skills/<skill-name>/
```

Read [[skill-design/opencode-format#key-takeaways]] for naming rules (1–64 chars, kebab-case, must match directory name).

### 3. Create SKILL.md with frontmatter

Read [[skill-design/opencode-format]] for the complete frontmatter specification. Key requirements:
- `name`: kebab-case, matches directory name
- `description`: 1 sentence, 10–1024 chars, include key terms and triggers
- `author`/`audience`: use role names from `AGENTS.md`

### 4. Write body content

Read [[skill-design/principles#concepts]] for research-backed patterns. Follow this structure:

1. **When to Use** — specific trigger conditions, not vague guidance
2. **Step-by-Step** — clear sequential steps with specific actions
3. **Checklist** — verification items the agent can self-check

Formatting rules:
- Imperative voice ("Write the test" not "You should write")
- One step per line item in checklists
- Include concrete examples (one is enough)
- Use tables for multi-column data
- Reference knowledge files with `[[domain/concept]]` wikilinks instead of duplicating content

### 5. Keep it lean

Read [[skill-design/principles#concepts]] — specifically the "Lean Skill Design" section. Target:
- < 150 lines for focused workflow skills
- < 250 lines for complex multi-phase skills

Cut without hesitation:
- Exhaustive examples when one is enough
- Reference documentation — link to knowledge files with `[[domain/concept]]`
- Knowledge content — extract to `.opencode/knowledge/`

### 6. Test with real usage

Use the skill in real tasks and iterate based on failures.

### 7. Reference from agents

Add the skill name to the agent's "Available Skills" section. Update the skills table in `AGENTS.md`.

## Checklist

- [ ] Skill name is kebab-case, matches directory name, 1–64 chars
- [ ] Description is 1 sentence with key terms and triggers
- [ ] Body follows: When to Use → Step-by-Step → Checklist
- [ ] No knowledge content embedded — all domain knowledge referenced via `[[domain/concept]]` wikilinks
- [ ] No duplication of `AGENTS.md` content or other skills
- [ ] Skill is under 250 lines (under 150 for focused skills)

## Available Skills in This Project

| Skill | Used By | Purpose |
|---|---|---|
| `run-session` | all agents | Session start/end protocol |
| `select-feature` | product-owner | Score and select next backlog feature (WSJF) |
| `define-scope` | product-owner | Step 1: define acceptance criteria |
| `implement` | software-engineer | Step 3: TDD loop |
| `apply-patterns` | software-engineer | Steps 2, 3: refactor when smell detected |
| `verify` | system-architect | Step 4: adversarial verification |
| `check-quality` | software-engineer | Quick reference — redirects to verify |
| `create-pr` | system-architect | Step 5: create PR with --no-ff merge |
| `git-release` | stakeholder | Step 5: semver versioning and release |
| `update-docs` | system-architect | post-acceptance + on stakeholder demand |
| `design-colors` | designer | Color palette selection and WCAG validation |
| `design-assets` | designer | SVG visual asset creation and updates |
| `create-skill` | software-engineer | Create new skills |
| `create-agent` | human-user | Create new agents with research-backed design |
| `create-knowledge` | all agents | Create new knowledge files |