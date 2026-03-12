---
name: create-skill
description: Creates new OpenCode skills following the skill definition standard
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: opencode
---
## What I do
Create new OpenCode skill directories with proper SKILL.md files following the OpenCode standard.

## When to use me
Use this when you need to create a new reusable skill for OpenCode agents.

## How to create a skill
1. Create a directory in `.opencode/skills/<skill-name>/`
2. Create a `SKILL.md` file with:
   - YAML frontmatter with name, description, license, compatibility
   - Content describing what the skill does and when to use it

## Frontmatter format
```
---
name: <skill-name>
description: 1-1024 character description
license: MIT
compatibility: opencode
metadata:
  key: value
---
```

## Naming rules
- Must be 1-64 characters
- Lowercase alphanumeric with single hyphen separators
- Cannot start or end with hyphen
- No consecutive hyphens
- Must match directory name

## Example SKILL.md
```
---
name: git-release
description: Create consistent releases and changelogs
license: MIT
compatibility: opencode
metadata:
  audience: maintainers
---
## What I do
- Draft release notes from merged PRs
- Propose a version bump
- Provide copy-pasteable git commands

## When to use me
Use this when preparing a tagged release.
```
