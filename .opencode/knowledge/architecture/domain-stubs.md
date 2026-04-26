---
domain: architecture
tags: [domain-analysis, stubs, protocols, file-placement]
last-updated: 2026-04-26
---

# Domain Analysis and Stub Writing

## Key Takeaways

- Extract nouns from feature/glossary language as candidate Entities, Value Objects, or Aggregates; verbs as candidate Actions; datasets as named types.
- Write stubs with `...` bodies only — no logic, no conditionals, no docstrings, no imports beyond `typing` and domain types.
- Assign a Protocol for every external dependency (SOLID-D + Hexagonal); if no external dependencies exist, SOLID-D is N/A.
- Place stubs where responsibility dictates; do not pre-create `ports/` or `adapters/` folders unless a concrete external dependency was identified.

## Concepts

**Domain Analysis Process**: From `docs/glossary.md` and Rules (Business) in the `.feature` file, nouns become candidate Entities/Value Objects/Aggregates, verbs become candidate Actions, datasets become named types. A bounded context check identifies module boundaries: same word, different meaning across features indicates a boundary. Cross-feature entities become candidates for a shared domain layer.

**Stub Rules**: Method bodies must be `...` only — no logic, no conditionals, no imports beyond `typing` and domain types. No docstrings (signatures will change; add after GREEN). No inline comments, no TODO comments, no speculative code. Stubs define the shape of the domain; GREEN fills in the behaviour.

**Protocol Pattern for External Dependencies**: All external dependencies must be assigned a Protocol (SOLID-D + Hexagonal architecture). A Protocol defines the interface; concrete implementations live in adapter modules. If no external dependencies exist in scope, the SOLID-D check is N/A.

**File Placement Patterns**: Place domain entities and value objects in `<package>/domain/<noun>.py`, cross-entity operations in `<package>/domain/service.py`. Place stubs where responsibility dictates. Do not pre-create `ports/` or `adapters/` folders unless a concrete external dependency was identified. Structure follows domain analysis, not a template.

## Content

### Domain Analysis Process

From `docs/glossary.md` + Rules (Business) in the `.feature` file:

- **Nouns** in feature/glossary language become candidate Entities, Value Objects, or Aggregates in the domain model
- **Verbs** in feature/glossary language become candidate Actions (operations with typed signatures on an Entity, a standalone function, or a Domain Service)
- **Datasets** become named types (not bare dict/list)
- **Bounded Context check**: same word, different meaning across features? That indicates a module boundary
- **Cross-feature entities** become candidates for a shared domain layer

### Updating the Domain Model

Update the `## Domain Model` section of `docs/system.md`:

- **New feature, first entities**: add bounded contexts, entities, actions, and relationships
- **Existing feature**: append new entities and actions. Deprecate old entries by moving them to a `### Deprecated` subsection. Never edit existing live entries — code depends on them
- Update `## Context` section if new actors, external systems, or interactions are identified
- Update `## Container` section if new containers or container interactions are identified

The PO reads `docs/system.md` but never writes to it. The SA owns this file.

### Stub Rules (Strictly Enforced)

- Method bodies must be `...` — no logic, no conditionals, no imports beyond `typing` and domain types
- No docstrings — signatures will change; add docstrings after GREEN (lint enforces this at quality gate)
- No inline comments, no TODO comments, no speculative code

Example of correct stub style:

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

### Protocol Pattern for External Dependencies

All external dependencies must be assigned a Protocol (SOLID-D + Hexagonal architecture). A Protocol defines the interface; concrete implementations live in adapter modules. This enables dependency inversion and testability.

If no external dependencies exist in scope, the SOLID-D check is N/A.

### File Placement Patterns

Common patterns (not required names):

- `<package>/domain/<noun>.py` — entities, value objects
- `<package>/domain/service.py` — cross-entity operations

Place stubs where responsibility dictates. Do not pre-create `ports/` or `adapters/` folders unless a concrete external dependency was identified in scope. Structure follows domain analysis, not a template.

If the file already exists: add the new class or method signature — do not remove or alter existing code. If the file does not exist: create it with the new signatures only.

## Related

- [[architecture/smell-check]] — quality gate applied to stubs before commit
- [[architecture/adr]] — recording decisions about protocols and patterns
- [[requirements/gherkin]] — the source of nouns and verbs for domain analysis