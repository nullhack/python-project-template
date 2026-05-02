---
domain: software-craft
tags: [solid, design-principles, oop, code-quality]
last-updated: 2026-04-30
---

# SOLID Principles

## Key Takeaways

- SRP: A class should have only one reason to change — multiple responsibilities mean multiple change axes that conflict (Martin, 2000).
- OCP: Software entities should be open for extension but closed for modification — add new behaviour by adding new code, not by changing existing code.
- LSP: Subtypes must be substitutable for their base types — a subclass that breaks the contract of its superclass violates Liskov Substitution.
- ISP: Clients should not be forced to depend on interfaces they do not use — split fat interfaces into smaller, cohesive ones.
- DIP: Depend on abstractions, not concretions — high-level modules should not depend on low-level modules; both should depend on abstractions.

## Concepts

**Single Responsibility Principle (SRP)** — A class with more than one reason to change has more than one responsibility. When requirements change, a class that handles multiple responsibilities must change in multiple unrelated ways, creating coupling between unrelated concerns. The fix: extract each responsibility into its own class. A class with >2 instance variables often has >1 responsibility (OC-7 overlap).

**Open-Closed Principle (OCP)** — When new variants are added to a system, existing code should not be modified. Instead, new behaviour is added by creating new types that implement existing interfaces. Type-switching (`if/elif` on a kind field) is an OCP violation — each new variant requires modifying every switch statement. The fix: Replace Conditional with Polymorphism, Strategy, or State.

**Liskov Substitution Principle (LSP)** — If a function expects a base type, it must work correctly with any subtype. A subclass that overrides methods to do nothing, throws `NotImplementedError`, or narrows pre-conditions violates LSP. Refused Bequest is the corresponding smell. The fix: Replace Inheritance with Delegation, or Push Down Method to isolate the problematic inheritance.

**Interface Segregation Principle (ISP)** — A fat interface forces all clients to depend on methods they do not use. When a client depends on an interface with 10 methods but only calls 2, any change to the other 8 methods triggers a recompile or retest. The fix: Extract Interface into smaller, cohesive interfaces, each serving one client role.

**Dependency Inversion Principle (DIP)** — High-level policy should not depend on low-level detail; both should depend on abstractions. A module that imports a concrete database adapter is tightly coupled to that adapter's implementation. The fix: define a Protocol (abstract interface) and inject the adapter via dependency injection. External dependencies should always be behind a Protocol.

## Content

### SOLID Violation Smell Mapping

| Principle | Smell | Signal | Fix |
|---|---|---|---|
| SRP | Divergent Change | One class changes for multiple unrelated reasons | Extract Class by axis of change |
| SRP | Large Class | Class has too many instance variables or methods | Extract Class, Extract Subclass |
| OCP | Switch Statements | `if/elif` on type/kind/status that must change for each new variant | Replace Conditional with Polymorphism, Strategy, State |
| OCP | Shotgun Surgery | Adding one variant requires modifying many call sites | Move dispatch to type hierarchy |
| LSP | Refused Bequest | Subclass overrides methods to do nothing or raises NotImplementedError | Push Down Method, Replace Inheritance with Delegation |
| LSP | Alternative Classes with Different Interfaces | Two classes doing the same thing with different signatures | Extract Superclass, unify via Protocol |
| ISP | Fat Interface | Client depends on methods it does not use | Extract Interface per client role |
| ISP | Temporary Field | Interface forces fields that are only set in some code paths | Extract Class, Introduce Null Object |
| DIP | Direct Dependency on Concrete | Module imports a concrete class instead of an abstraction | Define Protocol, inject via constructor |
| DIP | Hard-coded Construction | `__init__` creates concrete dependencies | Replace Constructor with Factory Method, inject dependencies |

### SOLID in the Design Principle Priority

The design principle priority in TDD is: YAGNI > KISS > DRY > ObjCal > Smells > SOLID > Design Patterns. SOLID principles are checked during REFACTOR only when a smell triggers them. They are not applied speculatively.

## Related

- [[software-craft/smell-catalogue]] — each SOLID violation maps to specific smells
- [[software-craft/design-patterns]] — patterns resolve SOLID violations (e.g., Strategy resolves OCP violations)
- [[software-craft/refactoring-techniques]] — refactoring techniques fix SOLID violations
- [[software-craft/refactoring]] — when and how to refactor, clean code, technical debt
- [[software-craft/object-calisthenics]] — Object Calisthenics rules overlap with SOLID (ObjCal-7 enforces SRP, ObjCal-4 enforces DIP)
- [[software-craft/tdd]] — SOLID is part of the design principle priority in REFACTOR