---
domain: knowledge-design
tags: [knowledge, wikilinks, diataxis, architecture, research-backed]
last-updated: 2026-04-26
---

# Knowledge Design Principles

## Key Takeaways

- Knowledge, skills, and agents are separate concerns with one canonical location each; never duplicate knowledge across files.
- Three research-backed failure modes (instruction conflict, positional attention degradation, redundancy interference) justify keeping knowledge in its own files.
- Knowledge files use a 4-section body structure (Key Takeaways, Concepts, Content, Related) with strict correspondence between tiers.
- Wikilinks reference knowledge on demand using `[[domain/concept]]` or `[[domain/concept#section]]` with cumulative extraction.
- Knowledge files contain reference and explanation only; procedural instructions belong in skills.

## Concepts

**Separation of concerns**: Knowledge, skills, and agents each have exactly one canonical location. Knowledge files hold reference and explanation; skills hold procedural instructions; agents hold role identity. No knowledge is embedded in skills or agents — they reference it via wikilinks. This prevents instruction conflict (Entry #24), positional attention degradation (Entry #25), and redundancy interference (Entry #26).

**Three-tier progressive disclosure**: Every knowledge file has four body sections ordered by depth: Key Takeaways (bullets), Concepts (paragraphs), Content (full reference), and Related (wikilinks). Each bullet in Key Takeaways corresponds to exactly one paragraph in Concepts and one or more subsections in Content. Closely related Content subsections may share a bullet and paragraph. This structure lets agents load only the depth they need via wikilink fragments.

**Wikilink routing**: Skills are the authoritative routing mechanism — they say when to load a knowledge file. Tags categorize files for pre-filtering without reading the body. Key Takeaways provide a relevance signal for agents scanning a file. There is no separate "purpose" section or frontmatter key; routing is handled by these three mechanisms.

**Fragment-based extraction**: Wikilinks support a `#section-name` fragment for cumulative extraction. `[[domain/concept#key-takeaways]]` loads frontmatter + Key Takeaways only (~80% token savings). `[[domain/concept#concepts]]` loads through Concepts (~65% savings). No fragment loads the full file. Section names use lowercase with hyphens (e.g., `#key-takeaways`, not `#Key Takeaways`).

**Reference and explanation only**: Knowledge files contain reference and explanation content (the "what" and "why"). Procedural instructions (the "when" and "how") belong in skills. This separation follows the Diátaxis framework: knowledge serves the Reference and Explanation modes, skills serve the How-to and Tutorial modes.

## Content

### Philosophy

**Knowledge is what. Skills are when and how. Agents are who.**

Each concern has exactly one canonical location:

| Concern | Location | Loaded When | Diátaxis Type |
|---|---|---|---|
| Project conventions | `AGENTS.md` | Every session | Reference |
| Role identity | `.opencode/agents/*.md` | When role invoked | Tutorial |
| Procedural instructions | `.opencode/skills/*/SKILL.md` | On demand | How-to guide |
| Domain knowledge | `.opencode/knowledge/*/` | On demand, referenced by skill | Reference + Explanation |

No knowledge is embedded in skills or agents. They reference it via wikilinks.

### Why Separate Knowledge

Three research-backed failure modes justify the separation:

1. **Instruction conflict** (Entry #24): LLMs cannot reliably resolve conflicting instructions from multiple sources. When the same knowledge appears in two places with divergent details, the model selects based on statistical priors, not prompt structure.

2. **Positional attention degradation** (Entry #25): Content in the middle of long contexts receives less attention. Duplicating knowledge across always-loaded files increases total context length, pushing other content into lower-attention positions.

3. **Redundancy interference** (Entry #26): Redundant content across prompt sections creates competing attention targets. De-duplication concentrates relevant signal in one canonical location.

### Wikilink Convention

Knowledge is referenced using wikilinks in the format `[[domain/concept]]` or `[[domain/concept#section-name]]`.

**Resolution rule**: When you encounter `[[domain/concept]]` in any file, read `.opencode/knowledge/{domain}/{concept}.md` to load that knowledge before proceeding with the task that requires it. When a fragment is specified, use cumulative extraction to read only the requested depth.

**Fragment syntax**: `#section-name` uses lowercase with hyphens (matching MediaWiki and HTML anchor conventions). Fragments are cumulative:

| Fragment | Loads | Approximate token savings |
|---|---|---|
| `#key-takeaways` | Frontmatter + Key Takeaways | ~80% |
| `#concepts` | Frontmatter + Key Takeaways + Concepts | ~65% |
| (no fragment) | Entire file | 0% |

**Extraction method**: `sed '/^## NextSection/Q' file.md` — reads from line 1 up to (but not including) the next `## ` heading. Frontmatter is always included.

Examples:
- `[[agent-design/principles]]` → full file `.opencode/knowledge/agent-design/principles.md`
- `[[software-craft/solid#key-takeaways]]` → frontmatter + Key Takeaways of `software-craft/solid.md`
- `[[skill-design/opencode-format#concepts]]` → frontmatter + Key Takeaways + Concepts of `skill-design/opencode-format.md`

Wikilinks appear in:
- **Skills**: "Before verifying code quality, read [[software-craft/code-quality]]"
- **Knowledge files**: "See [[agent-design/principles]] for agent design guidelines"
- **Agents**: "Load [[agent-design/principles]] when creating new agents"

Wikilinks do NOT appear in `AGENTS.md` (always-loaded) except to document the convention itself. AGENTS.md should contain brief references, not wikilinks to knowledge that would need to be resolved during every session.

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

#### Format Rules

1. **One concept per file** — each file covers exactly one topic
2. **Max ~150 lines** — avoid positional attention degradation (Entry #25)
3. **Self-contained** — understandable without reading linked files (Entry #10)
4. **Key Takeaways first** — one bullet per concept, imperative mood, enables fast relevance scanning
5. **Concepts expand Key Takeaways** — one paragraph per bullet, same order and grouping
6. **Correspondence rule** — bullet N in Key Takeaways corresponds to paragraph N in Concepts and subsection(s) N in Content
7. **No procedural instructions** — how-to content belongs in skills (Diátaxis)
8. **Reference + Explanation only** — knowledge serves these two Diátaxis modes
9. **YAML frontmatter** — `domain`, `tags`, `last-updated` for search and filtering; no `purpose` key needed
10. **No `## Purpose` section** — routing is handled by skills, tags, and Key Takeaways

#### Directory Structure

```
.opencode/knowledge/
  agent-design/
    principles.md
    opencode-format.md
  skill-design/
    principles.md
    opencode-format.md
  knowledge-design/
    principles.md
  software-craft/
    code-quality.md
    solid.md
    object-calisthenics.md
  ...
```

Domain directories organize related concepts. Subdirectories within domains are allowed for deep hierarchies.

### Knowledge Graph

The knowledge graph emerges from wikilinks in the `## Related` sections. No separate edge file is needed. A validation script can extract `[[...]]` patterns and check:
- No broken links (target file must exist, fragment must resolve to a valid section)
- No orphaned files (every file should be referenced by at least one other file or skill)

## Related

- [[skill-design/principles]]
- [[agent-design/principles]]