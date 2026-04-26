---
domain: architecture
tags: [smell-check, quality-gate, SOLID, patterns, ADR]
last-updated: 2026-04-26
---

# Architecture Smell Check

## Key Takeaways

- Verify SOLID-S (one responsibility), OC-8 (≤2 instance variables), SOLID-D + Hexagonal (all external deps have Protocols), and bounded context (no noun with different meaning across modules).
- Check for missing creational patterns (Factory/Builder for repeated complex construction), structural patterns (Strategy/Visitor for type-switching), and behavioral patterns (State/Observer for state machines and notifications).
- Verify ADR consistency: each ADR must be consistent with each acceptance criterion — no contradictions.
- Fix any failing check before committing stubs; re-run the smell check; only commit when all 8 checks pass.

## Concepts

**Verify structural and architectural constraints**: The smell check verifies SOLID-S (one responsibility per class), OC-8 (≤2 instance variables per behavioural class), SOLID-D + Hexagonal (all external deps have Protocols), and DDD Bounded Context (no noun with different meaning across modules).

**Check for missing design patterns**: Verify creational patterns (Factory/Builder for repeated complex construction), structural patterns (Strategy/Visitor for type-switching), and behavioral patterns (State/Observer for state machines and notifications).

**Verify ADR consistency**: Each ADR must be consistent with each acceptance criterion — no contradictions between architectural decisions and specified behaviour.

**Fix before committing**: If any check fails, fix the stub files before committing, re-run the smell check, and only commit when all 8 checks pass.

## Content

The Architecture Smell Check is applied to all stub files after domain analysis and stub writing, before committing. Every item must pass.

### Checklist

- [ ] **SOLID-S**: No class with more than 2 responsibilities. Each class has one reason to change.
- [ ] **OC-8**: No behavioural class with more than 2 instance variables. Dataclasses, Pydantic models, value objects, and TypedDicts are exempt — they are data containers, not behavioural classes.
- [ ] **SOLID-D + Hexagonal**: All external dependencies assigned a Protocol. If no external dependencies exist in scope, this check is N/A.
- [ ] **DDD Bounded Context**: No noun with different meaning across modules. Same word, different meaning indicates a module boundary.
- [ ] **Creational pattern**: No missing Factory/Builder where construction is repeated. If objects are constructed in multiple places with complex logic, extract a Factory or Builder.
- [ ] **Structural pattern**: No missing Strategy/Visitor where type-switching occurs. If code switches on type, apply the appropriate structural pattern.
- [ ] **Behavioral pattern**: No missing State/Observer where a state machine or scattered notification exists. If behaviour depends on state or events need propagation, apply the pattern.
- [ ] **ADR consistency**: Each ADR is consistent with each @id acceptance criterion — no contradictions between architectural decisions and specified behaviour.

### Failure Protocol

If any check fails:
1. Fix the stub files before committing
2. Re-run the smell check
3. Only commit when all 8 checks pass

### When to Apply

- At the end of Step 2, before committing stubs and ADRs
- Not during Step 3 (TDD loop) — that phase has its own quality gates
- Not during Step 4 (Verification) — the SA uses a different review process

### Relationship to Design Patterns

If a pattern smell is detected during the smell check, load `skill apply-patterns` for the appropriate GoF pattern catalogue entry. The smell check identifies the gap; the pattern skill provides the structural solution.

## Related

- [[architecture/adr]] — recording architectural decisions that pass the smell check
- [[architecture/domain-stubs]] — writing stubs that satisfy the smell check
- [[requirements/discovery-techniques]] — silent pre-mortem technique used before the smell check