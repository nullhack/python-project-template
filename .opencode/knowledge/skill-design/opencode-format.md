---
domain: skill-design
tags: [skills, opencode, format, configuration]
last-updated: 2026-04-26
---

# OpenCode Skill Format

## Key Takeaways

- Place skills in `.opencode/skills/<name>/SKILL.md` (project-level) or `~/.config/opencode/skills/<name>/SKILL.md` (global); project-level takes precedence.
- Require `name` (1-64 chars, kebab-case, must match directory) and `description` (1-1024 chars) in frontmatter; optional fields include `license`, `compatibility`, `metadata`, `permission`.
- Order body sections as Title (H1), When to Use, Step-by-Step, Checklist (optional); write in third person.
- Use wildcards in permission configuration; last matching rule wins; control skill access per agent.

## Concepts

**File Location and Discovery**: Skills are discovered in project-level (`.opencode/skills/<name>/SKILL.md`) and global (`~/.config/opencode/skills/<name>/SKILL.md`) directories, plus Claude Code compatibility paths. Project-level takes precedence. OpenCode walks up from the current working directory to the git worktree, loading matching skill files.

**YAML Frontmatter**: Required fields are `name` (1-64 chars, kebab-case, must match directory name) and `description` (1-1024 chars, specific enough for agent selection). Optional fields include `license`, `compatibility`, and `metadata` (string-to-string map with `audience` and `workflow`).

**Body Structure**: Recommended body sections in order: Title (H1), When to Use, Step-by-Step, Checklist (optional). Write in third person.

**Permissions**: Permissions control which agents can access which skills, configured in `opencode.json` or per-agent frontmatter. Wildcards are supported and the last matching rule wins.

## Content

### File Location

Skills are discovered in these directories (project-level takes precedence):

1. `.opencode/skills/<name>/SKILL.md` — project-level
2. `~/.config/opencode/skills/<name>/SKILL.md` — global
3. `.claude/skills/<name>/SKILL.md` — Claude Code compatibility
4. `~/.claude/skills/<name>/SKILL.md` — global Claude Code compatibility

OpenCode walks up from the current working directory until it reaches the git worktree, loading any matching `skills/*/SKILL.md` along the way.

### YAML Frontmatter

```yaml
---
name: <skill-name>          # Required; 1-64 chars, kebab-case, must match directory
description: <1-sentence>    # Required; 1-1024 chars; key terms and triggers
license: <string>           # Optional
compatibility: <string>     # Optional
metadata:                   # Optional; string-to-string map
  audience: <role-name>
  workflow: <category>
---
```

#### Name Rules

- 1–64 characters
- Lowercase alphanumeric with single hyphen separators
- Cannot start or end with `-`, no consecutive `--`
- Must match the directory name exactly
- Regex: `^[a-z0-9]+(-[a-z0-9]+)*$`

#### Description Rules

- 1–1024 characters
- Specific enough for the agent to choose correctly between similar skills
- Include key terms and trigger words

### Body Structure

Recommended sections in order:

1. **Title** — what the skill does (H1)
2. **When to Use** — specific trigger conditions
3. **Step-by-Step** — sequential procedural steps
4. **Checklist** — verification items (optional)

Write in third person. The description is injected into the system prompt.

### Discovery

OpenCode lists available skills in the `skill` tool description. Each entry shows name and description. Agents load skills by calling `skill({ name: "skill-name" })`.

### Permission Configuration

Control which agents can access which skills in `opencode.json`:

```json
{
  "permission": {
    "skill": {
      "*": "allow",
      "internal-*": "deny"
    }
  }
}
```

Or per-agent in agent frontmatter:

```yaml
permission:
  skill:
    "documents-*": "allow"
```

Patterns support wildcards. Last matching rule wins.

## Related

- [[skill-design/principles]]
- [[agent-design/opencode-format]]