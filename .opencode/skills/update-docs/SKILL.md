---
name: update-docs
description: Generate and update C4 architecture diagrams, living glossary, and system overview from existing project docs
version: "2.0"
author: product-owner
audience: product-owner
workflow: feature-lifecycle
---

# Living Docs

This skill generates and updates two living documents after a feature is accepted (Step 5) or on stakeholder request: the **C4 architecture diagrams** and the **living glossary**. Both are derived from existing project documentation — no new decisions are made.

The glossary is a secondary artifact derived from the code, the domain model, and domain-expert conversations. The canonical sources are the completed feature files, the discovery synthesis, and the architectural decisions. The glossary is a human-readable projection of those sources — not an independent authority.

## When to Use

- **As part of the release process (Step 5)** — the `git-release` skill calls this skill inline at step 5, before the version-bump commit. Do not commit separately; the release process stages all files together.
- **Stakeholder on demand** — when the stakeholder asks "what does the system look like?" or "what does term X mean in this context?". In this case, commit with the standalone message in Step 5 below.

## Ownership Rules

| Document | Created/Updated by | Inputs read |
|---|---|---|
| `docs/context.md` | `update-docs` skill (PO) | `docs/discovery.md`, `docs/features/completed/` |
| `docs/container.md` | `update-docs` skill (PO) | `docs/adr/ADR-*.md`, `docs/features/completed/` |
| `docs/glossary.md` | `update-docs` skill (PO) | `docs/domain-model.md`, `docs/glossary.md` (existing), `docs/adr/ADR-*.md`, `docs/features/completed/` |
| `docs/system.md` | SA (Step 2), PO reviews (Step 5) | `docs/discovery.md`, `docs/adr/ADR-*.md`, `docs/features/completed/` |
| `docs/discovery.md` | PO only (Step 1) | — |
| `docs/domain-model.md` | SA only (Step 2) | — |

**Never edit `docs/adr/ADR-*.md`, `docs/discovery.md`, or `docs/domain-model.md` in this skill.** Those files are owned by their respective agents. This skill reads them; it never writes to them.

---

## Step 1 — Read Phase (all before writing anything)

Read in this order:

1. `docs/discovery.md` — project scope, feature list per session
2. `docs/domain-model.md` — all entities, nouns, verbs, bounded contexts
3. `docs/features/completed/` — all completed `.feature` files (full text: Rules, Examples, Constraints)
4. `docs/adr/` — all architectural decision files (containers, modules, protocols, external deps)
5. `docs/context.md` and `docs/container.md` — existing C4 diagrams if they exist (update, do not replace from scratch)
6. `docs/glossary.md` — existing glossary if it exists (extend, never remove existing entries)
7. `docs/branding.md` — if present, read `Visual > Primary color` and `Accent color`. Apply to C4 Mermaid diagrams via `%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '<primary-hex>', 'lineColor': '<accent-hex>'}}}%%`. If absent or fields blank, use Mermaid defaults.

Identify from the read phase:

- **Actors** — named human roles from feature `As a <role>` clauses and discovery Scope section
- **External systems** — any system outside the package boundary named in features or architecture decisions
- **Containers** — deployable/runnable units identified in ADR files (Hexagonal adapters, CLIs, services)
- **Key domain terms** — all nouns and verbs from `docs/domain-model.md`, plus any terms defined in ADR decisions

---

## Step 2 — Update C4 Context Diagram (Level 1)

File: `docs/context.md`

The Context diagram answers: **who uses the system and what external systems does it interact with?**

Use Mermaid `C4Context` syntax. Use the template in `context.md.template` in this skill's directory.

Rules:
- One `Person(...)` per distinct actor found in completed feature files
- One `System_Ext(...)` per external dependency identified in ADR files
- Relationships (`Rel`) use verb phrases from feature `When` clauses or architecture decision labels
- If no external systems are identified in ADRs, omit `System_Ext` entries
- If the file already exists: update only — add new actors/systems, update relationship labels. Never remove an existing entry unless the feature it came from has been explicitly superseded

---

## Step 3 — Update C4 Container Diagram (Level 2)

File: `docs/container.md`

The Container diagram answers: **what are the major runnable/deployable units and how do they communicate?**

Only generate this diagram if `docs/adr/` contains at least one decision identifying a distinct container boundary (e.g., a CLI entry point separate from a library, a web server, a background worker, an external service adapter). If the project is a single-container system, note this in the file and skip the diagram body.

Use Mermaid `C4Container` syntax. Use the template in `container.md.template` in this skill's directory.

Rules:
- Container names and responsibilities come directly from ADR decisions — do not invent them
- Technology labels come from `pyproject.toml` dependencies when identifiable (e.g., "Python / fire CLI", "Python / FastAPI")
- If the file already exists: update incrementally — do not regenerate from scratch

---

## Step 4 — Update Living Glossary

File: `docs/glossary.md`

The glossary answers: **what does each domain term mean in this project's context?**

Use the template in `glossary.md.template` in this skill's directory.

### Rules

- Extract all entities and verbs from `docs/domain-model.md`
- Extract all roles from `As a <role>` clauses in completed `.feature` files
- Extract all external system names from ADR decisions
- Extract any term defined or clarified in architectural decision `Reason:` fields
- **Do not remove existing glossary entries** — if a term's meaning has changed, add a `**Superseded by:**` line pointing to the new entry and write a new entry
- **Every term must have a traceable source** — completed feature files or ADR decisions. If a term appears in sources but is never defined, write `Definition: Term appears in [source] but has not been explicitly defined.` Do not invent a definition.
- Terms are sorted alphabetically within the file

### Merge with existing glossary

If `docs/glossary.md` already exists:
1. Read all existing entries
2. For each new term found in sources: check if it already exists in the glossary
   - Exists, definition unchanged → skip
   - Exists, definition changed → append `**Superseded by:** <new-term-or-date>` to old entry; write new entry
   - Does not exist → append new entry in alphabetical order

---

## Step 5 — Commit

**When called from the release process**: skip this step — the `git-release` skill stages and commits all files together.

**When run standalone** (stakeholder on demand): commit after all diagrams and glossary are updated:

```
docs(update-docs): update C4 and glossary after <feature-stem>
```

If triggered without a specific feature (general refresh):

```
docs(update-docs): refresh C4 diagrams and glossary
```

---

## Checklist

- [ ] Read all source files before writing anything (including `docs/branding.md` if present)
- [ ] Context diagram reflects all actors from completed feature files
- [ ] Context diagram reflects all external systems from ADR files
- [ ] Container diagram present only if multi-container architecture confirmed in ADR files
- [ ] Glossary contains all entities and verbs from `docs/domain-model.md`
- [ ] No existing glossary entry removed
- [ ] Every new term has a traceable source in completed feature files or ADRs; no term is invented
- [ ] No edits made to ADR files, `docs/discovery.md`, or `docs/domain-model.md`
- [ ] If standalone: committed with `docs(update-docs): ...` message
- [ ] If called from release: files staged but not committed (release process commits)

---

## Templates

All templates for files written by this skill live in this skill's directory:

- `context.md.template` — `docs/context.md` structure
- `container.md.template` — `docs/container.md` structure
- `glossary.md.template` — `docs/glossary.md` entry format

Base directory for this skill: file:///home/user/Documents/projects/python-project-template/.opencode/skills/update-docs
Relative paths in this skill (e.g., scripts/, reference/) are relative to this base directory.
Note: file list is sampled.

<skill_files>
<file>/home/user/Documents/projects/python-project-template/.opencode/skills/update-docs/container.md.template</file>
<file>/home/user/Documents/projects/python-project-template/.opencode/skills/update-docs/context.md.template</file>
<file>/home/user/Documents/projects/python-project-template/.opencode/skills/update-docs/glossary.md.template</file>
</skill_files>
