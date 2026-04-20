---
name: create-skill
description: Create new OpenCode skills following the skill definition standard
version: "2.0"
author: software-engineer
audience: software-engineer
workflow: opencode
---

# Create Skill

Create a new reusable skill for OpenCode agents, following research-backed best practices.

## When to Use

When you need to codify a repeatable workflow that multiple agents or sessions will follow. Skills are loaded on demand; they don't run automatically.

## How to Create a Skill

### 0. Research (mandatory — do this first)

Before writing any skill, research the domain to ground the skill in industry standards and scientifically-backed evidence:

1. **Identify the domain**: What workflow or methodology will this skill codify?
2. **Search for best practices**:
   - Academic sources (Google Scholar, IEEE, ACM)
   - Vendor documentation (OpenAI, Anthropic, Google, Microsoft)
   - Industry standards (ISO, NIST, OMG)
   - Established methodologies (e.g., FDD, Scrum, Kanban for process skills)
3. **Read existing research**: Check `docs/scientific-research/` for related entries — each file covers a domain (testing, oop-design, architecture, ai-agents, etc.)
4. **Synthesize conclusions**: Extract actionable conclusions — what works, why, and when to apply it
5. **Embed as guidance**: Write the skill's steps, checklists, and decision rules based on those conclusions — not as academic citations but as direct guidance ("Use X because it produces Y outcome")

**Example research synthesis:**
```
Research question: How to structure a security review skill?
Sources found: OWASP Testing Guide, NIST SP 800-53, Anthropic's agent design patterns
Conclusion: Security reviews should be adversarial (assume breakage), use defense-in-depth checklist, escalate on first critical finding.
→ Skill step: "3. Run adversarial checks — assume breach, verify every control"
```

### 1. Create the directory

```bash
mkdir .opencode/skills/<skill-name>/
```

Naming rules:
- 1–64 characters
- Lowercase alphanumeric with single hyphens
- Cannot start or end with hyphen, no consecutive hyphens
- Must match the directory name exactly

### 2. Create SKILL.md with frontmatter

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

**Frontmatter requirements:**
- `name`: Max 64 chars, lowercase letters/numbers/hyphens only
- `description`: 1 sentence, 10-100 chars, include key terms and triggers
- `author`/`audience`: Use role names from AGENTS.md
- `workflow`: Category like `feature-lifecycle`, `opencode`, `release-management`

### 3. Write body content

Follow these research-backed patterns:

**Structure:**
1. **When to Use** — specific trigger conditions, not vague guidance
2. **Step-by-Step** — clear sequential steps with specific actions
3. **Checklist** — verification items the agent can self-check

**Formatting rules:**
- Use imperative voice ("Write the test" not "You should write")
- One step per line item in checklists
- Include concrete examples (one is enough, not exhaustive)
- Use tables for multi-column data (tool options, decision criteria)
- Link to reference docs instead of duplicating them

**Tone:** Write in third person. The description is injected into the system prompt.

### 4. Keep it lean

Skills are loaded into context. Long skills consume tokens. Target:
- < 150 lines for focused workflow skills
- < 250 lines for complex multi-phase skills
- < 500 lines absolute maximum (Anthropic recommendation)

**Cut:**
- Exhaustive examples when one is enough
- Reference documentation (link to it instead)
- Boilerplate CI/CD YAML (it belongs in `.github/`, not skills)

### 5. Test with real usage

The most effective skill development process involves using the skill in real tasks and iterating based on failures.

### 6. Reference from agents

Add the skill name to the agent's "Available Skills" section so the agent knows to load it. Update AGENTS.md skills table.

## Available Skills in This Project

| Skill | Used By | Purpose |
|---|---|---|
| `run-session` | all agents | Session start/end protocol |
| `select-feature` | product-owner | Score and select next backlog feature (WSJF) |
| `define-scope` | product-owner | Step 1: define acceptance criteria |
| `implement` | software-engineer | Steps 2-3: architecture + TDD loop |
| `apply-patterns` | software-engineer | Steps 2, 3: refactor when smell detected |
| `verify` | reviewer | Step 4: adversarial verification |
| `check-quality` | software-engineer | Quick reference — redirects to verify |
| `create-pr` | software-engineer | Step 5: create PR with squash merge |
| `git-release` | software-engineer | Step 5: calver versioning and release |
| `update-docs` | product-owner | Step 5 (after acceptance) + on stakeholder demand: C4 diagrams + glossary |
| `design-colors` | designer | Color palette selection and WCAG validation |
| `design-assets` | designer | SVG visual asset creation and updates |
| `create-skill` | software-engineer | Create new skills |
| `create-agent` | human-user | Create new agents with research-backed design |