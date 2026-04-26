---
domain: skill-design
tags: [skills, on-demand-loading, context-budget, research-backed]
last-updated: 2026-04-26
---

# Skill Design Principles

## Key Takeaways

- Skills load into context only when invoked; every token in an always-loaded file competes for attention against the task prompt — keep skills lean.
- Skills are how-to guides (Diátaxis): task-oriented, step-by-step instructions; reference and explanation belong in knowledge files.
- Cut without hesitation: exhaustive examples (one is enough), reference documentation (use wikilinks), boilerplate configuration, and knowledge content (extract to knowledge files).
- Embed IF-THEN triggers at the decision point, not in a separate reference document; prospective memory cues are 2-3x more likely to execute.

## Concepts

**On-Demand Loading**: Skills load into context only when the `skill` tool is invoked. Bloated always-loaded files cause LLMs to ignore critical instructions. Every token in an unconditionally-loaded file competes for attention against the task prompt. Skills must be self-contained when loaded but must not duplicate content that already exists in `AGENTS.md` or other skills.

**Skill as How-To Guide (Diátaxis)**: In the Diátaxis framework, skills serve as how-to guides: task-oriented, step-by-step instructions for achieving a specific outcome. Tutorials (learning a role) belong in agent files. Reference and explanation (looking something up, understanding why) belong in knowledge files. Mixing these in one file is the failure mode Diátaxis warns against.

**Lean Skill Design**: Skills consume context tokens. Target lengths: <150 lines for focused workflow skills, <250 lines for complex multi-phase skills, <500 lines absolute maximum. Cut without hesitation: exhaustive examples when one is enough, reference documentation (use wikilinks), boilerplate configuration (belongs in project files), knowledge content (extract to knowledge files).

**Prospective Memory Cues and De-Duplication**: Memory for intended actions is better when cues are embedded at the decision point, not in a separate reference document. Include the IF-THEN trigger and the knowledge reference at the point of decision. Redundant content across prompt sections creates competing attention targets — de-duplicate by referencing one canonical knowledge file instead of embedding copies.

## Content

### On-Demand Loading

Skills load into context only when the `skill` tool is invoked. Bloated always-loaded files cause LLMs to ignore critical instructions. Every token in an unconditionally-loaded file competes for attention against the task prompt. Long always-loaded files push important instructions beyond effective attention range, causing silent non-compliance. (Source: Anthropic, 2025; research entry #23.)

**Implication**: Skills must be self-contained when loaded, but must not duplicate content that already exists in `AGENTS.md` or other skills. Each piece of knowledge belongs in exactly one canonical location.

### Skill = How-To (Diátaxis)

In the Diátaxis framework, skills serve as **how-to guides**: task-oriented, step-by-step instructions for achieving a specific outcome. A skill tells you *when to do what*, not *why things work the way they do*.

| Diátaxis Type | Our File | Purpose | Reader's Mental State |
|---|---|---|---|
| Tutorial | Agent | "Who am I and what do I own?" | Learning a role |
| How-to guide | Skill | "Step-by-step: when X, do Y" | Doing a task |
| Reference | Knowledge | "Here are the facts about SOLID" | Looking something up |
| Explanation | Knowledge | "Why does SOLID matter?" | Understanding |

Mixing these in one file is exactly the failure mode Diátaxis warns against. (Source: Procida, 2021; research entry #61.)

### Lean Skill Design

Skills consume context tokens. Long skills push other content into lower-attention positions. (Source: Entry #25.)

Target lengths:
- < 150 lines for focused workflow skills
- < 250 lines for complex multi-phase skills
- < 500 lines absolute maximum (Anthropic recommendation)

**Cut without hesitation:**
- Exhaustive examples when one is enough
- Reference documentation — reference knowledge files instead: `[[domain/concept]]`
- Boilerplate configuration — belongs in project files, not skills
- Knowledge content — extract to `.opencode/knowledge/` and reference with `[[domain/concept]]`

### Prospective Memory Cues

Memory for intended actions is better when cues are embedded at the point of action, not in a separate reference document. (Source: McDaniel & Einstein, 2000; entry #10.)

**Implication for skills**: Include the IF-THEN trigger and the knowledge reference at the decision point:

```markdown
# Good: cue + reference at point of action
If a class has more than one reason to change, read [[software-craft/solid]]
and apply the Single Responsibility Principle.

# Bad: cue without reference (agent may not know the details)
Apply SOLID principles.

# Bad: reference without cue (agent may not know when to load it)
See [[software-craft/solid]] for design principles.
```

### De-Duplication

Redundant content across prompt sections creates competing attention targets. De-duplication concentrates relevant signal in one canonical location per concern. (Source: Sharma & Henley, 2026; entry #26.)

When two skills need the same knowledge, both should reference the same knowledge file rather than each embedding a copy.

## Related

- [[skill-design/opencode-format]]
- [[knowledge-design/principles]]
- [[agent-design/principles]]