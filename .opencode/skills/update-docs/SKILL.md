---
name: update-docs
description: Generate and update architecture diagrams, living glossary, and system overview from existing project docs
version: "3.0"
author: system-architect
audience: system-architect
workflow: feature-lifecycle
---

# Living Docs

This skill generates and updates living documents after a feature is accepted (Step 5) or on stakeholder request: the **Context and Container sections** of `docs/system.md` and the **living glossary**. Both are derived from existing project documentation — no new decisions are made.

The glossary is a secondary artifact derived from the code, the domain entities in `system.md`, and domain-expert conversations. The canonical sources are the completed feature files, the discovery synthesis, and the architectural decisions. The glossary is a human-readable projection of those sources — not an independent authority.

## When to Use

- **As part of the release process (Step 5)** — the `git-release` skill calls this skill inline at step 5, before the version-bump commit. Do not commit separately; the release process stages all files together.
- **Stakeholder on demand** — when the stakeholder asks "what does the system look like?" or "what does term X mean in this context?". In this case, commit with the standalone message in Step 5 below.

## Ownership Rules

| Document | Created/Updated by | Inputs read |
|---|---|---|
| `docs/system.md` (Context + Container sections) | SA at Step 2; `update-docs` skill (SA) updates these sections post-acceptance | `docs/discovery.md`, `docs/adr/ADR-*.md`, `docs/features/completed/` |
| `docs/glossary.md` | PO only (Step 1, via `define-scope` skill) | — |
| `docs/discovery.md` | PO only (Step 1) | — |

**Never edit `docs/adr/ADR-*.md` or `docs/discovery.md` in this skill.** Those files are owned by their respective agents. This skill reads them; it never writes to them.

---

## Step 1 — Read Phase (all before writing anything)

Read in this order:

1. `docs/discovery.md` — project scope, feature list per session
2. `docs/system.md` — all sections: domain model entities, modules, configuration, existing Context and Container diagrams
3. `docs/features/completed/` — all completed `.feature` files (full text: Rules, Examples, Constraints)
4. `docs/adr/` — all architectural decision files (containers, modules, protocols, external deps)
5. `docs/glossary.md` — existing glossary if it exists (extend, never remove existing entries)
6. `docs/branding.md` — if present, read `Visual > Primary color` and `Accent color`. Apply to Mermaid diagrams via `%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '<primary-hex>', 'lineColor': '<accent-hex>'}}}%%`. If absent or fields blank, use Mermaid defaults.

Identify from the read phase:

- **Actors** — named human roles from feature `As a <role>` clauses and discovery Scope section
- **External systems** — any system outside the package boundary named in features or architecture decisions
- **Containers** — deployable/runnable units identified in ADR files (Hexagonal adapters, CLIs, services)
- **Key domain terms** — all nouns and verbs from the Domain Model section of `system.md`, plus any terms defined in ADR decisions

---

## Step 2 — Update Context Section

Section: `## Context` in `docs/system.md`

The Context diagram answers: **who uses the system and what external systems does it interact with?**

Use Mermaid `C4Context` syntax. Use the template in `context.md.template` in this skill's directory for the diagram body.

Rules:
- One `Person(...)` per distinct actor found in completed feature files
- One `System_Ext(...)` per external dependency identified in ADR files
- Relationships (`Rel`) use verb phrases from feature `When` clauses or architecture decision labels
- If no external systems are identified in ADRs, omit `System_Ext` entries
- If the section already exists: update only — add new actors/systems, update relationship labels. Never remove an existing entry unless the feature it came from has been explicitly replaced

---

## Step 3 — Update Container Section

Section: `## Container` in `docs/system.md`

The Container diagram answers: **what are the major runnable/deployable units and how do they communicate?**

Only generate this diagram if `docs/adr/` contains at least one decision identifying a distinct container boundary (e.g., a CLI entry point separate from a library, a web server, a background worker, an external service adapter). If the project is a single-container system, note this in the section and skip the diagram body.

Use Mermaid `C4Container` syntax. Use the template in `container.md.template` in this skill's directory for the diagram body.

Rules:
- Container names and responsibilities come directly from ADR decisions — do not invent them
- Technology labels come from `pyproject.toml` dependencies when identifiable (e.g., "Python / fire CLI", "Python / FastAPI")
- If the section already exists: update incrementally — do not regenerate from scratch

---

## Step 4 — Read Glossary for Diagram Accuracy

File: `docs/glossary.md` — **read-only in this skill**

The glossary is owned by the PO (via `define-scope` skill). This skill reads it to verify that diagram labels and entity names in the Context and Container sections match the canonical domain terms.

### Rules

- Read `docs/glossary.md` if it exists
- Verify every actor name, container name, and relationship label in the Context and Container diagrams matches a term in the glossary or in the Domain Model section of `system.md`
- If a diagram label uses a term not found in either source, flag it as a potential inconsistency — do **not** add the term to the glossary; escalate to PO
- **Never write to `docs/glossary.md` in this skill** — if you identify a missing or incorrect glossary term, note it in the commit message or in a comment to the stakeholder and stop

---

## Step 5 — Commit

**When called from the release process**: skip this step — the `git-release` skill stages and commits all files together.

**When run standalone** (stakeholder on demand): commit after all sections and glossary are updated:

```
docs(update-docs): update context, container, and glossary after <feature-stem>
```

If triggered without a specific feature (general refresh):

```
docs(update-docs): refresh context, container, and glossary
```

---

## Checklist

- [ ] Read all source files before writing anything (including `docs/branding.md` if present)
- [ ] Context section in `system.md` reflects all actors from completed feature files
- [ ] Context section in `system.md` reflects all external systems from ADR files
- [ ] Container section in `system.md` present only if multi-container architecture confirmed in ADR files
- [ ] Glossary read; all diagram labels verified against glossary and Domain Model section of `system.md`
- [ ] Any unrecognized diagram term flagged to PO — not added to glossary unilaterally
- [ ] No edits made to ADR files or `docs/discovery.md`
- [ ] If standalone: committed with `docs(update-docs): ...` message
- [ ] If called from release: files staged but not committed (release process commits)

---

## Templates

All templates for diagrams written by this skill live in this skill's directory:

- `context.md.template` — Context diagram body (inserted into `## Context` section of `system.md`)
- `container.md.template` — Container diagram body (inserted into `## Container` section of `system.md`)

Base directory for this skill: `.opencode/skills/update-docs/`
Relative paths in this skill (e.g., scripts/, reference/) are relative to this base directory.
Note: file list is sampled.

<skill_files>
<file>.opencode/skills/update-docs/container.md.template</file>
<file>.opencode/skills/update-docs/context.md.template</file>
</skill_files>
