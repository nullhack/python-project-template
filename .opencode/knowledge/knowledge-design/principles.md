---
domain: knowledge-design
tags: [knowledge, wikilinks, diataxis, architecture, progressive-disclosure]
last-updated: 2026-04-29
---

# Knowledge Design Principles

## Key Takeaways

- Knowledge, skills, and agents are separate concerns with one canonical location each; never duplicate knowledge across files.
- Knowledge files use a 4-section body structure (Key Takeaways, Concepts, Content, Related) with strict correspondence between tiers.
- Wikilinks reference knowledge on demand using `[[domain/concept]]` or `[[domain/concept#section]]` with cumulative extraction; skills are the authoritative routing mechanism.
- Knowledge files contain reference and explanation only; procedural instructions belong in skills.
- Maximum ~150 lines per file to avoid positional attention degradation (Liu et al., 2023); small focused files may omit the Content section.

## Concepts

**Separation of Concerns**: Knowledge, skills, and agents each have exactly one canonical location. Knowledge files hold reference and explanation; skills hold procedural instructions; agents hold role identity. The flow YAML holds routing, artifacts, and transitions. No knowledge is embedded in skills or agents — they reference it via wikilinks. Three failure modes observed in LLM context windows justify this separation: conflicting instructions from multiple sources (each concern gets one file), positional attention degradation (Liu et al., 2023 — middle content receives less attention; keep files short), and redundant content creating competing attention targets (each fact in one location).

**Three-Tier Progressive Disclosure**: Every knowledge file has four body sections ordered by depth: Key Takeaways (bullets), Concepts (paragraphs), Content (full reference), and Related (wikilinks). Each bullet in Key Takeaways corresponds to exactly one paragraph in Concepts and one or more subsections in Content. Small focused files may omit the Content section if bullets and concepts are sufficient.

**Wikilink Routing and Extraction**: Skills are the authoritative routing mechanism — they say when to load a knowledge file. Wikilinks support a `#section-name` fragment for cumulative extraction: `[[domain/concept#key-takeaways]]` loads frontmatter + Key Takeaways only (approximately 80% token savings), `[[domain/concept#concepts]]` loads through Concepts (approximately 65% savings), and no fragment loads the full file. Use `sed '/^## SectionName/Q' file.md` to extract up to but not including the next section header.

**Reference and Explanation Only**: Knowledge files contain reference and explanation content (the what and why). Procedural instructions (the when and how) belong in skills. This separation follows the Diátaxis framework (Procida, 2021): knowledge serves the Reference and Explanation modes, skills serve the How-to and Tutorial modes.

**Size Limit**: Maximum ~150 lines per file to avoid positional attention degradation (Liu et al., 2023). Files that exceed this should be split into separate knowledge files. Small focused topics may use only Key Takeaways and Concepts, omitting the Content section entirely.

## Content

### Philosophy

**Knowledge is what. Skills are when and how. Agents are who. Flows are where.**

| Concern | Location | Loaded When | Diátaxis Type |
|---|---|---|---|
| Project navigation | `AGENTS.md` | Every session | Reference |
| Role identity | `.opencode/agents/*.md` | When role invoked | Tutorial |
| Procedural instructions | `.opencode/skills/*/SKILL.md` | On demand | How-to guide |
| Domain knowledge | `.opencode/knowledge/*/` | On demand, referenced by skill | Reference + Explanation |
| Routing, artifacts, transitions | `.flowr/flows/*.yaml` | Via `flowr status` | — |

### Knowledge File Format

```markdown
---
domain: <domain-name>
tags: [<tag1>, <tag2>]
last-updated: <YYYY-MM-DD>
---

# <Title>

## Key Takeaways

- <one bullet per concept; closely related subsections may share a bullet>
- <imperative mood: "Test observable behaviour, not implementation details">

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

### Format Rules

1. **One concept per file** — each file covers exactly one topic
2. **Max ~150 lines** — avoid positional attention degradation (Liu et al., 2023)
3. **Self-contained** — understandable without reading linked files
4. **Key Takeaways first** — one bullet per concept, imperative mood, enables fast relevance scanning
5. **Concepts expand Key Takeaways** — one paragraph per bullet, same order and grouping
6. **Correspondence rule** — bullet N in Key Takeaways corresponds to paragraph N in Concepts and subsection(s) N in Content
7. **No procedural instructions** — how-to content belongs in skills (Diátaxis — Procida, 2021)
8. **YAML frontmatter** — `domain`, `tags`, `last-updated` for search and filtering
9. **Small files may omit Content** — focused topics with rules that fit in bullets and concepts need no expansion

### Wikilink Convention

Wikilinks reference knowledge using the format `[[domain/concept]]` or `[[domain/concept#section-name]]`.

**Resolution rule**: When you encounter `[[domain/concept]]` in any file, read `.opencode/knowledge/{domain}/{concept}.md` to load that knowledge before proceeding.

**Fragment syntax**: `#section-name` uses lowercase with hyphens. Fragments are cumulative:

| Fragment | Loads | Bash Command | Token Savings |
|---|---|---|---|
| `#key-takeaways` | Frontmatter + Key Takeaways | `sed '/^## Concepts/Q' file.md` | ~80% |
| `#concepts` | Frontmatter + Key Takeaways + Concepts | `sed '/^## Content/Q' file.md` | ~65% |
| (no fragment) | Entire file | `cat file.md` | 0% |

Wikilinks appear in skills, knowledge files, and agents. Wikilinks do NOT appear in `AGENTS.md` (always-loaded) except to document the convention itself.

### Directory Structure

```
.opencode/knowledge/
  requirements/
  agent-design/
  skill-design/
  knowledge-design/
  workflow/
```

Domain directories organize related concepts. Subdirectories within domains are allowed for deep hierarchies.

### Knowledge Graph

The knowledge graph emerges from wikilinks in the `## Related` sections. No separate edge file is needed. Validation can extract `[[...]]` patterns and check that target files exist and fragments resolve to valid sections.

## Related

- [[skill-design/principles]]
- [[agent-design/principles]]