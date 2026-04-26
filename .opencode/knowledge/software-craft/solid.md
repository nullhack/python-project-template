---
domain: software-craft
tags: [solid, principles, oop, design]
last-updated: 2026-04-26
---

# SOLID Principles

## Key Takeaways

- Keep each class to one reason to change; count distinct concerns to detect SRP violations.
- Design for extension without modification; `if/elif` chains that require editing are the violation signal.
- Ensure subtypes honour the full base contract; `NotImplementedError` stubs signal LSP violations.
- Split wide interfaces so no client depends on methods it doesn't use; stubbed methods signal ISP violations.
- Depend on abstractions, not concrete I/O; direct imports of database/file/network classes signal DIP violations.

## Concepts

**Single Responsibility Principle**: A class should have exactly one reason to change. When a class handles data + formatting, or business logic + persistence, it has more than one concern. Extract Class by axis of change to resolve.

**Open/Closed Principle**: Software entities should be open for extension but closed for modification. If adding a case requires editing an `if/elif` chain inside the class, the class is not closed for modification. Apply Replace Conditional with Polymorphism, Strategy, or State.

**Liskov Substitution Principle**: Subtypes must be substitutable for their base types without altering program correctness. A subclass that raises on an inherited method or narrows a precondition breaks polymorphic code silently. Push Down Method/Field or Replace Inheritance with Delegation.

**Interface Segregation Principle**: No client should be forced to depend on methods it does not use. When implementors stub out methods they don't need or raise `NotImplementedError`, the interface is too wide. Extract Superclass, unify via Protocol, or split the interface.

**Dependency Inversion Principle**: High-level modules should not depend on low-level modules. Both should depend on abstractions. When domain code directly imports a database, file, or network class, unit testing becomes impossible. Introduce Protocol for external dependency; apply Repository/Adapter pattern.

## Content

### S — Single Responsibility Principle

A class should have exactly one reason to change.

**Check**: Does this class have exactly one reason to change?

**Violation signal**: Class handles data + formatting, or business logic + persistence. Count distinct concerns — if more than one, the class violates SRP.

**Catalogue entry**: Extract Class (split by axis of change).

### O — Open/Closed Principle

Software entities should be open for extension but closed for modification.

**Check**: Can new behaviour be added without editing this class?

**Violation signal**: Adding a case requires editing an `if/elif` chain inside the class. Every new variant forces a modification to existing code.

**Catalogue entry**: Replace Conditional with Polymorphism; Strategy; State.

### L — Liskov Substitution Principle

Subtypes must be substitutable for their base types without altering program correctness.

**Check**: Do all subtypes honour the full contract of their base type?

**Violation signal**: Subclass raises on an inherited method, or narrows a precondition. Subtypes that cannot stand in for their base break polymorphic code silently.

**Catalogue entry**: Push Down Method/Field; Replace Inheritance with Delegation.

### I — Interface Segregation Principle

No client should be forced to depend on methods it does not use.

**Check**: Does every implementor use every method in the interface?

**Violation signal**: Implementors stub out methods they don't need, or raise `NotImplementedError` for interface methods they don't care about. The interface is too wide.

**Catalogue entry**: Extract Superclass; unify via Protocol; split the interface.

### D — Dependency Inversion Principle

High-level modules should not depend on low-level modules. Both should depend on abstractions.

**Check**: Does domain code depend only on abstractions, not concrete I/O?

**Violation signal**: Domain class directly imports a database, file, or network class. Concrete I/O in domain code makes unit testing impossible.

**Catalogue entry**: Introduce Protocol for external dependency; Repository/Adapter pattern.

## Related

- [[software-craft/object-calisthenics]] — complementary structural constraints
- [[software-craft/smell-catalogue]] — smells that trigger SOLID violations
- [[software-craft/design-patterns]] — patterns that resolve SOLID violations
- [[software-craft/self-declaration]] — SOLID items 7-11 in the declaration checklist