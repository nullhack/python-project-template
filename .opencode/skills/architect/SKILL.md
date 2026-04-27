---
name: architect
description: Step 2 — Architecture and domain design, one feature at a time
version: "2.0"
author: system-architect
audience: system-architect
workflow: feature-lifecycle
---

# Architect

Step 2: conduct the architectural interview, design the domain model, write architecture stubs, record decisions as ADRs, and generate test stubs. The system-architect owns this step entirely.

This step is a subflow defined in `.flowr/arch-cycle.yaml` with 5 states: **read → interview → validate → design → stubs**.

## When to Use

Load this skill when starting Step 2 (Architecture) after the PO has moved a BASELINED feature to `in-progress/`.

## System-Architect Quality Gate Priority Order

During architecture, correctness priorities are (in order):

1. **Design correctness** — YAGNI > KISS > DRY > SOLID > Object Calisthenics > appropriate design patterns > complex code > complicated code > failing code > no code
2. **One test green** — `uv run task test-fast` passes after stub generation
3. **Commit** — when stubs and ADRs are complete (ADRs require stakeholder validation before commit)

Design correctness is far more important than lint/pyright/coverage compliance. Never run lint or static-check during architecture — those are handoff-only checks.

---

## Step 2 — Architecture (arch-cycle subflow)

### Prerequisites (stop if any fail — escalate to PO)

1. `docs/features/in-progress/` contains exactly one `.feature` file (not just `.gitkeep`). If none exists, **STOP** — update the session file in `.flowception/` `@state` to `idle` and stop. Never self-select or move a feature yourself.
2. The feature file's discovery section has `Status: BASELINED`. If not, escalate to PO — Step 1 is incomplete.
3. The feature file contains `Rule:` blocks with `Example:` blocks and `@id` tags. If not, escalate to PO — criteria have not been written.
4. Package name confirmed: read `pyproject.toml` → locate `[tool.setuptools]` → confirm directory exists on disk.

### Package Verification (mandatory — before writing any code)

1. Read `pyproject.toml` → locate `[tool.setuptools]` → record `packages = ["<name>"]`
2. Confirm directory exists: `ls <name>/`
3. All new source files go under `<name>/`

**Note on feature file moves**: The PO moves `.feature` files between folders. The system-architect never moves, creates, or edits `.feature` files. Verify the session file in `.flowception/` has the correct `id` and `branch` set before beginning architecture work.

---

## Subflow State: `read`

### Read Phase (targeted reads only — before writing anything)

| Read | Why |
|---|---|
| `docs/system.md` — all sections | Domain model, Context, Container, module structure, constraints, key decisions |
| `docs/glossary.md` | Use existing domain terms; do not invent synonyms |
| In-progress `.feature` file | Rules + Examples + @id |
| `tree <package>/` | Package structure without reading every file |
| Specific `.py` files matching feature nouns | Understand what already exists |

ADR details are available on demand: reference Key Decisions in `system.md`, then read specific ADR files only when a decision needs deeper context. Do not read all ADRs upfront.

1. Read `docs/system.md` — all sections: domain model, Context, Container, module structure, constraints, key decisions
2. Read `docs/glossary.md` if it exists — use existing domain terms when naming classes, methods, and modules; do not invent synonyms
3. Read in-progress `.feature` file (full: Rules + Examples + @id)
4. Run `tree <package>/` — understand package structure without reading every file
5. Read **specific `.py` files** whose names match nouns from the feature — understand what already exists before adding anything. Do not read the entire package.

**Transition**: `ready` → `interview` | `spec-gap` → `blocked` (escalate to PO)

---

## Subflow State: `interview`

### Architectural Interview Protocol

The arch interview surfaces decisions that must be recorded as ADRs. Related questions from the interview are grouped into one ADR — multiple Q&A pairs converge on a single decision.

### Gap-Finding Techniques

Apply gap-finding techniques (CIT, Laddering, Silent Pre-mortem) during the domain analysis pass to surface decisions the feature file has not yet made explicit. If a pattern smell is detected, load `skill apply-patterns`. See [[requirements/discovery-techniques]].

### ADR Interview Pattern

For each group of related unresolved decisions identified during domain analysis, follow the ADR interview pattern to frame questions, evaluate alternatives, draft ADRs, and validate with the stakeholder. See [[architecture/adr]].

**Do not commit ADRs yet** — ADRs must be validated with the stakeholder first (next state: `validate`).

**Transition**: `gaps-found` → `interview` (loop) | `adrs-drafted` → `validate` (contract: `adrs_drafted == "true"`)

---

## Subflow State: `validate`

Present the ADR validation table to the stakeholder for approval. See [[architecture/adr]] for the validation table format.

Commit each approved ADR: `feat(<feature-stem>): add ADR-<slug>`

**Transition**: `adrs-approved` → `design` (contract: `adrs_approved == "true"`) | `adrs-rejected` → `interview` (revise and re-draft)

---

## Subflow State: `design`

### Domain Analysis

Identify nouns, verbs, datasets, and bounded contexts from the glossary and feature file, then update the domain model in `docs/system.md`. See [[architecture/domain-stubs]] for the full domain analysis process and stub writing rules.

### Update Domain Model (in `docs/system.md`)

- **New feature, first entities**: add bounded contexts, entities, actions, and relationships to the Domain Model section.
- **Existing feature**: append new entities and actions. Deprecate old entries if retired in favour of a newer entry — move them to a `### Deprecated` subsection. Never edit existing live entries — code depends on them.
- Update the `## Context` section if new actors, external systems, or interactions are identified.
- Update the `## Container` section if new containers or container interactions are identified.

The PO reads `docs/system.md` but never writes to it.

### Architecture Smell Check (hard gate)

Apply the smell check to stub files before committing. If any check fails, fix the stubs before committing. See [[architecture/smell-check]].

### Write Stubs into Package

From the domain analysis, write or extend `.py` files in `<package>/`. Follow the stub rules and file placement patterns in [[architecture/domain-stubs]].

**Transition**: `stubs-written` → `stubs` (contract: `stubs_written == "true"`)

---

## Subflow State: `stubs`

### Generate Test Stubs

Run `uv run task test-fast` once. It reads the in-progress `.feature` file (all `@id` tags must already be present — assigned by the PO at Step 1) and generates `tests/features/<feature_slug>/<rule_slug>_test.py` — one file per `Rule:` block, one skipped function per `@id`. Verify the files were created, then stage all changes.

Commit: `feat(<feature-stem>): add architecture and test stubs`

**Transition**: `test-fast-green` → `complete` (subflow exit)

### Hand off to Step 3 (TDD Loop)

1. Update the session file in `.flowception/`: `state` to `step-3-working` (the TDD subflow's `setup` state handles branch creation)
2. Provide the SE with:
   - Feature file path
   - Summary of stubs created
   - Any ADRs that constrain implementation
   - Any domain model changes in `system.md`
3. Stop. The SE takes over.

---

## Handling Spec Gaps

If during architecture you discover behaviour not covered by existing acceptance criteria:
- **Do not extend criteria yourself** — escalate to PO
- Note the gap in the session file in `.flowception/` and escalate to PO
- The PO will decide whether to add a new Example to the `.feature` file

---

## Templates

Templates for files written by this skill live in this skill's directory (`architect/`):

- `system.md.template` — `docs/system.md` structure (domain model + Context + Container sections included; markdown table format)
- `adr.md.template` — ADR file structure (Status, Context, Interview Q&A table, Decision, Reason, Alternatives Considered, Consequences)

Base directory for this skill: `.opencode/skills/architect/`
Relative paths in this skill (e.g., scripts/, reference/) are relative to this base directory.
Note: file list is sampled.