---
domain: software-craft
tags: [design-patterns, gof, oop, refactoring]
last-updated: 2026-04-26
---

# Design Patterns

## Key Takeaways

- Apply patterns during REFACTOR only when a smell triggers them; never speculatively.
- Creational smells (scattered construction, multi-step setup) trigger Factory Method, Abstract Factory, or Builder.
- Structural smells (type-switching, feature envy, parallel hierarchies) trigger Strategy, Visitor, Move Function, or Bridge.
- Behavioral smells (large state machines, scattered notifications, repeated algorithm skeletons) trigger State, Observer, or Template Method.
- Procedural code that requires modifying existing functions for new variants needs OOP — the smell is always a place that must change every time the domain grows.

## Concepts

**Pattern Selection from Smells**: GoF design patterns provide structural solutions to recurring code smells. Patterns are applied during REFACTOR only when a smell triggers them — never speculatively. The smell catalogue identifies the gap; the pattern provides the structural solution.

**Creational Smells and Patterns**: Scattered object construction (same object built in 3+ places) triggers Factory Method or Factory Function. Multi-step construction with optional parts (object requires several setup calls before valid) triggers Builder. The key change is centralizing creation knowledge or making invalid intermediate states impossible.

**Structural Smells and Patterns**: Type-switching (function branches on a type flag) triggers Strategy (behaviour varies per call) or Visitor (operation varies over fixed structure). Feature envy (method uses another class's data more than its own) triggers Move Function. Parallel inheritance hierarchies (two class hierarchies growing in lockstep) trigger Bridge.

**Behavioral Smells and Patterns**: Large state machines in one class trigger State pattern. Scattered notification (source directly calls multiple downstream systems) triggers Observer. Repeated algorithm skeletons (two functions sharing structure but differing in one step) trigger Template Method.

**Core Heuristic**: When procedural code requires modifying existing functions to add new variants, OOP is the fix. Procedural code is open to modification; OOP closes existing code to modification and opens it to extension through new types. The smell is always the same: a place in the codebase that must change every time the domain grows.

## Content

### Pattern Selection from Smells

GoF design patterns provide structural solutions to recurring code smells. Patterns are applied during REFACTOR only when a smell triggers them — never speculatively. The smell catalogue identifies the gap; the pattern provides the structural solution.

#### GoF Pattern Catalogue

##### Creational

| Pattern | Intent |
|---|---|
| Factory Method | Delegate object creation to a subclass or factory function |
| Abstract Factory | Create families of related objects without specifying concrete classes |
| Builder | Construct complex objects step-by-step, separating construction from representation |
| Prototype | Clone existing objects instead of creating new ones from scratch |
| Singleton | Ensure a class has only one instance (use sparingly — prefer dependency injection) |

##### Structural

| Pattern | Intent |
|---|---|
| Adapter | Wrap an incompatible interface to match an expected interface |
| Bridge | Separate abstraction from implementation so both can vary independently |
| Composite | Treat individual objects and compositions uniformly via a shared interface |
| Decorator | Add responsibilities to an object dynamically without subclassing |
| Facade | Provide a simplified interface to a complex subsystem |
| Flyweight | Share fine-grained objects to reduce memory when many similar instances are needed |
| Proxy | Control access to an object via a surrogate (lazy init, access control, logging) |

##### Behavioral

| Pattern | Intent |
|---|---|
| Chain of Responsibility | Pass a request along a chain of handlers until one handles it |
| Command | Encapsulate a request as an object, enabling undo/redo and queuing |
| Interpreter | Define a grammar and an interpreter for a language |
| Iterator | Provide sequential access to elements without exposing the underlying structure |
| Mediator | Centralize complex communication between objects through a mediator object |
| Memento | Capture and restore object state without violating encapsulation |
| Observer | Define a one-to-many dependency so dependents are notified automatically |
| State | Allow an object to alter its behaviour when its internal state changes |
| Strategy | Define a family of algorithms, encapsulate each, and make them interchangeable |
| Template Method | Define the skeleton of an algorithm; let subclasses fill in specific steps |
| Visitor | Separate an algorithm from the object structure it operates on |

#### Quick Smell to Pattern Lookup

| Smell | Pattern |
|---|---|
| Same object constructed in 3+ places | Factory Method / Factory Function |
| Multi-step setup before object is valid | Builder |
| Branching on a type, kind, or status field | Strategy |
| Method uses another class's data more than its own | Move Function (Fowler) |
| Two class hierarchies that grow in lockstep | Bridge |
| Many methods branch on the same state field | State |
| Object directly calls multiple downstream systems on change | Observer |
| Two functions share the same algorithm skeleton, differ in one step | Template Method |
| Subsystem is complex and callers need a simple entry point | Facade |

#### Pattern Smell Checks (Verification)

| Code smell | Pattern missed | How to check |
|---|---|---|
| Multiple if/elif on type/state | State or Strategy | Search for `isinstance` chains |
| Complex `__init__` | Factory or Builder | Check line count and side effects |
| Callers know multiple components | Facade | Check caller coupling |
| External dep without Protocol | Repository/Adapter | Check dependency injection |
| 0 domain classes, many functions | Missing domain model | Count classes vs functions |

### Creational Smells and Patterns

**Scattered Object Construction** — Same object constructed in 3+ places with slightly different arguments. Factory Method or Factory Function centralizes creation. Key change: creation knowledge moves from N call sites to one place.

**Multi-Step Construction with Optional Parts** — Object requires several setup calls before valid; callers must remember sequence. Builder enforces sequence and validates completeness. Key change: invalid intermediate states become impossible.

### Structural Smells and Patterns

**Type-Switching** — Function branches on a type flag, kind field, or status string. Strategy (behaviour varies per call) or Visitor (operation varies over fixed structure). Key change: Open/Closed principle restored — new variants extend without modifying existing code.

**Feature Envy** — Method in class A uses data from class B more than its own. Move Function (Fowler) relocates the computation. Key change: behaviour lives next to the data it depends on.

**Parallel Inheritance Hierarchies** — Two class hierarchies grow in lockstep. Bridge separates the two axes of variation. Key change: two axes become two independent hierarchies composed at runtime.

### Behavioral Smells and Patterns

**Large State Machine in One Class** — Many methods branch on a status field. State pattern gives each state its own class. Key change: state-specific behaviour is co-located; the context becomes a thin delegator.

**Scattered Notification / Event Fan-Out** — Source directly calls multiple downstream systems. Observer reverses coupling direction — listeners depend on the source, not the other way around. Key change: new listeners are added without touching the source.

**Repeated Algorithm Skeleton** — Two functions share high-level structure but differ in one or two steps. Template Method puts invariant structure in one place. Key change: variants are isolated in named hooks.

### Core Heuristic

When procedural code requires modifying existing functions to add new variants, OOP is the fix. Procedural code is open to modification; OOP closes existing code to modification and opens it to extension through new types. The smell is always the same: a place in the codebase that must change every time the domain grows.

## Related

- [[software-craft/smell-catalogue]] — smells trigger pattern selection
- [[software-craft/solid]] — patterns resolve SOLID violations
- [[software-craft/object-calisthenics]] — OC rules complement pattern application
- [[software-craft/tdd]] — patterns are applied during REFACTOR phase