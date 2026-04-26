---
name: create-knowledge
description: Create new knowledge files following the knowledge design standard
version: "2.0"
author: software-engineer
audience: all-agents
workflow: opencode
---

# Create Knowledge

Create a new knowledge file in `.opencode/knowledge/` following the project's knowledge design standard.

## When to Use

When you identify domain knowledge that is duplicated across skills or agents, or when a skill needs to reference expert-level reference or explanation content that would make it too long.

## Step-by-Step

### 1. Identify duplication or need

Check for these signals:
- The same concept appears in 2+ skills or agents
- A skill exceeds 150 lines because it embeds reference content
- An agent file contains explanatory knowledge instead of role identity
- A concept needs its own file for wikilink referencing

### 2. Read the design principles

Read [[knowledge-design/principles]] before writing any knowledge file. Key rules:
- One concept per file
- Max ~150 lines
- Self-contained (understandable without reading linked files)
- Key Takeaways first (enables fast relevance scanning)
- No procedural instructions (those belong in skills)
- Reference + Explanation only (per Diátaxis)

### 3. Choose the domain and filename

Domain directories organize related concepts. Choose or create a domain:

```
.opencode/knowledge/
  agent-design/       ← agent architecture, tool permissions, instruction writing
  skill-design/       ← skill format, on-demand loading, lean design
  knowledge-design/   ← knowledge file format, wikilink conventions
  software-craft/     ← SOLID, code quality, testing, design patterns
  ...
```

Filename is the concept slug: lowercase, hyphen-separated. Path becomes `[[domain/concept]]`.

### 4. Create the file

```bash
mkdir -p .opencode/knowledge/<domain>/
```

Create `.opencode/knowledge/<domain>/<concept>.md`:

```markdown
---
domain: <domain-name>
tags: [<tag1>, <tag2>]
last-updated: <YYYY-MM-DD>
---

# <Title>

## Key Takeaways

- <one bullet per concept; imperative mood; closely related subsections may share a bullet>

## Concepts

<one paragraph per concept, same grouping as Key Takeaways>
<paragraph 1 expands on bullet 1, paragraph 2 on bullet 2, etc.>

## Content

<Reference and explanatory content. No procedural instructions — those belong
in skills. Self-contained: understandable without reading linked files.
Subsections correspond to Key Takeaway bullets (1:1 or N:1 grouping).>

## Related

- [[domain/other-concept]]
```

### 5. Write the Key Takeaways section

The Key Takeaways section is critical — it enables fast relevance scanning. An agent reading a skill that says "read [[software-craft/solid]]" can load just `[[software-craft/solid#key-takeaways]]` to decide whether to read further.

Write the Key Takeaways section as one bullet per concept:
- Use imperative mood: "Test observable behaviour, not implementation details"
- Closely related Content subsections may share a bullet
- Bullets must correspond 1:1 or N:1 with Content subsections (the correspondence rule)

### 6. Write the Concepts section

The Concepts section expands each Key Takeaway bullet into a full paragraph. Each paragraph explains the *why* and *how* behind the bullet.

- One paragraph per Key Takeaway bullet, same order and grouping
- Paragraph N corresponds to bullet N
- No new concepts introduced here — every concept must have a Key Takeaway bullet

### 7. Write the Content section

Follow these rules from [[knowledge-design/principles]]:
- Reference + Explanation only (Diátaxis)
- No procedural instructions (those belong in skills)
- No step-by-step workflows
- Include research sources where applicable
- Self-contained: all necessary context within the file
- Max ~150 lines

Content subsections must correspond to Key Takeaway bullets (1:1 or N:1 grouping — closely related subsections may share a bullet and paragraph).

### 8. Add Related wikilinks

The `## Related` section creates edges in the knowledge graph. Link to:
- Prerequisites (knowledge needed before this one)
- Complementary concepts (knowledge that extends this one)
- Contrasting concepts (alternative approaches)

Use the `[[domain/concept]]` format for full file references, or `[[domain/concept#key-takeaways]]` or `[[domain/concept#concepts]]` for partial references. A validation script can check for broken links.

### 9. Update referencing skills

Replace embedded knowledge in skills and agents with `[[domain/concept]]` or `[[domain/concept#section]]` wikilinks. Each piece of knowledge should exist in exactly one canonical location.

### 10. Validate

Check:
- [ ] File follows the format in step 4 (Key Takeaways, Concepts, Content, Related)
- [ ] Key Takeaways has one bullet per concept, imperative mood
- [ ] Concepts has one paragraph per Key Takeaway bullet, same order and grouping
- [ ] Content subsections correspond to Key Takeaway bullets (1:1 or N:1)
- [ ] No `## Purpose` section (routing is handled by skills, tags, and Key Takeaways)
- [ ] Content is self-contained (understandable without reading linked files)
- [ ] Content is Reference + Explanation only (no procedural instructions)
- [ ] File is under 150 lines
- [ ] All `[[...]]` wikilinks resolve to existing `.opencode/knowledge/` files (fragments resolve to valid sections)
- [ ] No duplication with `AGENTS.md` or other knowledge files
- [ ] Added to the knowledge graph (referenced by at least one skill or other knowledge file)

## Checklist

- [ ] One concept per file — each file covers exactly one topic
- [ ] Key Takeaways section with one bullet per concept, imperative mood
- [ ] Concepts section with one paragraph per Key Takeaway bullet
- [ ] Correspondence rule: bullet N ↔ paragraph N ↔ Content subsection(s) N
- [ ] Content is self-contained, no procedural instructions
- [ ] All wikilinks in `## Related` resolve to existing files
- [ ] No `## Purpose` section — routing handled by skills, tags, and Key Takeaways
- [ ] Under 150 lines
- [ ] No duplication with other knowledge files, skills, or `AGENTS.md`
- [ ] Referenced by at least one skill or knowledge file