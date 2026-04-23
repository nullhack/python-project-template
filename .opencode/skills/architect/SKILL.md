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

## When to Use

Load this skill when starting Step 2 (Architecture) after the PO has moved a BASELINED feature to `in-progress/`.

## System-Architect Quality Gate Priority Order

During architecture, correctness priorities are (in order):

1. **Design correctness** — YAGNI > KISS > DRY > SOLID > Object Calisthenics > appropriate design patterns > complex code > complicated code > failing code > no code
2. **One test green** — `uv run task test-fast` passes after stub generation
3. **Commit** — when stubs and ADRs are complete

Design correctness is far more important than lint/pyright/coverage compliance. Never run lint or static-check during architecture — those are handoff-only checks.

---

## Step 2 — Architecture

### Prerequisites (stop if any fail — escalate to PO)

1. `docs/features/in-progress/` contains exactly one `.feature` file (not just `.gitkeep`). If none exists, **STOP** — update `WORK.md` `@state` to `[IDLE]` and stop. Never self-select or move a feature yourself.
2. The feature file's discovery section has `Status: BASELINED`. If not, escalate to PO — Step 1 is incomplete.
3. The feature file contains `Rule:` blocks with `Example:` blocks and `@id` tags. If not, escalate to PO — criteria have not been written.
4. Package name confirmed: read `pyproject.toml` → locate `[tool.setuptools]` → confirm directory exists on disk.
5. **Branch verification**: `git branch --show-current` must output `feat/<stem>` or `fix/<stem>`. If it outputs `main` or any other branch, stop — the SE must create the correct branch via `skill version-control` before architecture begins.

### Package Verification (mandatory — before writing any code)

1. Read `pyproject.toml` → locate `[tool.setuptools]` → record `packages = ["<name>"]`
2. Confirm directory exists: `ls <name>/`
3. All new source files go under `<name>/`

**Note on feature file moves**: The PO moves `.feature` files between folders. The system-architect never moves, creates, or edits `.feature` files. Verify `WORK.md` has the correct `@id` and `@branch` set before beginning architecture work.

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

---

## Architectural Interview Protocol

The arch interview surfaces decisions that must be recorded as ADRs. Each unresolved question becomes one ADR.

### Gap-Finding Techniques

Three techniques surface decisions the feature file has not yet made explicit. Apply them during the domain analysis pass.

**Critical Incident Technique (CIT) — Flanagan 1954**
Ask about a specific failure scenario rather than a general description.
- "If this entity is misused, what breaks?"
- "Tell me about a concrete case where this boundary would be crossed."

**Laddering / Means-End Chain — Reynolds & Gutman 1988**
Climb from surface constraint to architectural consequence.
- "Why does this need to be immutable?"
- "What breaks if this is not behind a Protocol?"
- Stop when the answer produces a design constraint that can be written into an ADR.

**Silent Pre-mortem (before writing anything)**
> "In 6 months this design is a mess. What mistakes did we make?"

For each candidate class:
- >2 ivars? → split
- >1 reason to change? → isolate

For each external dep:
- Is it behind a Protocol? → if not, add

For each noun:
- Serving double duty across modules? → isolate

If pattern smell detected, load `skill apply-patterns`.

### ADR Interview Pattern

For each unresolved decision identified during domain analysis:

1. **Frame the question**: state the decision as a clear question with known alternatives.
   Example: "Should `FrameworkAdapter` be a `typing.Protocol` or an ABC?"

2. **State constraints**: list what is known from the feature file, glossary, and existing ADRs that constrains the answer.

3. **Evaluate alternatives**: for each option, state the consequence. Apply laddering to surface hidden consequences.

4. **Record the decision**: write one ADR per question. Use the template in `adr.md.template`.
   - `## Context` — the question + constraints that produced it
   - `## Decision` — one sentence
   - `## Reason` — one sentence
   - `## Alternatives Considered` — rejected options with reasons
   - `## Consequences` — (+) and (-) outcomes

5. **Commit each ADR** as it is finalized: `feat(<feature-stem>): add ADR-<slug>`

Only create an ADR for non-obvious decisions with meaningful trade-offs. Routine YAGNI choices do not need a record.

---

## Domain Analysis

From `docs/glossary.md` + Rules (Business) in the `.feature` file:
- **Nouns** in feature/glossary language → candidate Entities, Value Objects, or Aggregates in the domain model
- **Verbs** in feature/glossary language → candidate Actions (operations with typed signatures on an Entity, a standalone function, or a Domain Service)
- **Datasets** → named types (not bare dict/list)
- **Bounded Context check**: same word, different meaning across features? → module boundary
- **Cross-feature entities** → candidate shared domain layer

### Update Domain Model (in `docs/system.md`)

Update the `## Domain Model` section of `docs/system.md`:

- **New feature, first entities**: add bounded contexts, entities, actions, and relationships to the Domain Model section.
- **Existing feature**: append new entities and actions. Deprecate old entries if retired in favour of a newer entry — move them to a `### Deprecated` subsection. Never edit existing live entries — code depends on them.
- Update the `## Context` section (Actors, Systems, and Interactions
  sub-tables) if new actors, external systems, or interactions are
  identified.
- Update the `## Container` section (Boundary and Interactions
  sub-tables) if new containers or container interactions are
  identified.

The PO reads `docs/system.md` but never writes to it.

### Architecture Smell Check (hard gate)

Apply to the stub files just written:

- [ ] No class with >2 responsibilities (SOLID-S)
- [ ] No behavioural class with >2 instance variables (OC-8; dataclasses, Pydantic models, value objects, and TypedDicts are exempt)
- [ ] All external deps assigned a Protocol (SOLID-D + Hexagonal) — N/A if no external dependencies identified in scope
- [ ] No noun with different meaning across modules (DDD Bounded Context)
- [ ] No missing Creational pattern: repeated construction without Factory/Builder
- [ ] No missing Structural pattern: type-switching without Strategy/Visitor
- [ ] No missing Behavioral pattern: state machine or scattered notification without State/Observer
- [ ] Each ADR consistent with each @id AC — no contradictions

If any check fails: fix the stub files before committing.

---

## Write Stubs into Package

From the domain analysis, write or extend `.py` files in `<package>/`. For each entity:

- **If the file already exists**: add the new class or method signature — do not remove or alter existing code.
- **If the file does not exist**: create it with the new signatures only.

**Stub rules (strictly enforced):**
- Method bodies must be `...` — no logic, no conditionals, no imports beyond `typing` and domain types
- No docstrings — signatures will change; add docstrings after GREEN (lint enforces this at quality gate)
- No inline comments, no TODO comments, no speculative code

**Example — correct stub style:**

```python
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True, slots=True)
class EmailAddress:
    value: str

    def validate(self) -> None: ...


class UserRepository(Protocol):
    def save(self, user: "User") -> None: ...
    def find_by_email(self, email: EmailAddress) -> "User | None": ...
```

**File placement (common patterns, not required names):**
- `<package>/domain/<noun>.py` — entities, value objects
- `<package>/domain/service.py` — cross-entity operations

Place stubs where responsibility dictates — do not pre-create `ports/` or `adapters/` folders unless a concrete external dependency was identified in scope. Structure follows domain analysis, not a template.

---

## Generate Test Stubs

Run `uv run task test-fast` once. It reads the in-progress `.feature` file (all `@id` tags must already be present — assigned by the PO at Step 1) and generates `tests/features/<feature_slug>/<rule_slug>_test.py` — one file per `Rule:` block, one skipped function per `@id`. Verify the files were created, then stage all changes.

Commit: `feat(<feature-stem>): add architecture and test stubs`

### Hand off to Step 3 (TDD Loop)

1. Update `WORK.md` `@state: STEP-3-WORKING`
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
- Note the gap in `WORK.md` and escalate to PO
- The PO will decide whether to add a new Example to the `.feature` file

---

## Templates

Templates for files written by this skill live in this skill's directory (`architect/`):

- `system.md.template` — `docs/system.md` structure (domain model + Context + Container sections included; markdown table format)
- `adr.md.template` — individual ADR file structure (includes `## Context` section)

Base directory for this skill: `.opencode/skills/architect/`
Relative paths in this skill (e.g., scripts/, reference/) are relative to this base directory.
Note: file list is sampled.
