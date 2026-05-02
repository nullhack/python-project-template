---
domain: software-craft
tags: [design-patterns, gof, oop, refactoring, architecture]
last-updated: 2026-04-30
---

# Design Patterns

## Key Takeaways

- Apply patterns during REFACTOR only when a smell triggers them; never speculatively (Shvets, 2014).
- Creational smells (scattered construction, multi-step setup) trigger Factory Method, Abstract Factory, or Builder.
- Structural smells (type-switching, feature envy, parallel hierarchies) trigger Strategy, Visitor, Move Method, or Bridge.
- Behavioral smells (large state machines, scattered notifications, repeated algorithm skeletons) trigger State, Observer, or Template Method.
- When procedural code requires modifying existing functions for new variants, OOP is the fix — the smell is always a place that must change every time the domain grows.

## Concepts

**Pattern Selection from Smells** (Shvets, 2014; Gamma et al., 1994) — GoF design patterns provide structural solutions to recurring code smells. Patterns are applied during REFACTOR only when a smell triggers them — never speculatively. The smell catalogue identifies the gap; the pattern provides the structural solution.

**Creational Smells and Patterns** — Scattered object construction (same object built in 3+ places) triggers Factory Method or Factory Function. Multi-step construction with optional parts (object requires several setup calls before valid) triggers Builder. The key change is centralizing creation knowledge or making invalid intermediate states impossible.

**Structural Smells and Patterns** — Type-switching (function branches on a type flag) triggers Strategy (behaviour varies per call) or Visitor (operation varies over fixed structure). Feature envy (method uses another class's data more than its own) triggers Move Method. Parallel inheritance hierarchies (two class hierarchies growing in lockstep) trigger Bridge.

**Behavioral Smells and Patterns** — Large state machines in one class trigger State pattern. Scattered notification (source directly calls multiple downstream systems) triggers Observer. Repeated algorithm skeletons (two functions sharing structure but differing in one step) trigger Template Method.

**Core Heuristic** — When procedural code requires modifying existing functions to add new variants, OOP is the fix. Procedural code is open to modification; OOP closes existing code to modification and opens it to extension through new types. The smell is always the same: a place in the codebase that must change every time the domain grows.

## Content

### GoF Pattern Catalogue

#### Creational

| Pattern | Intent | Problem | Applicability |
|---|---|---|---|
| Factory Method | Delegate object creation to a subclass or factory function | Direct construction couples code to concrete classes; adding a new type requires changes throughout | Don't know exact types beforehand; framework users extend components; reuse existing objects (caching, pooling) |
| Abstract Factory | Create families of related objects without specifying concrete classes | Code depends on families of related objects and must work with any family | Multiple product variants that must be used together; configuration-driven object creation |
| Builder | Construct complex objects step-by-step, separating construction from representation | Telescoping constructor with many optional parameters; subclass explosion for every configuration | Eliminate telescoping constructor; different representations with similar construction steps; construct Composite trees |
| Prototype | Clone existing objects instead of creating new ones from scratch | Object creation is expensive or complex; object configuration is the hard part, not the class | Object has many configuration options; deep copy needed; avoid subclass explosion for configuration |
| Singleton | Ensure a class has only one instance (use sparingly — prefer dependency injection) | Shared resource that must have exactly one instance | Database connection, configuration, logger — but prefer DI over Singleton |

#### Structural

| Pattern | Intent | Problem | Applicability |
|---|---|---|---|
| Adapter | Wrap an incompatible interface to match an expected interface | Existing class has the right behaviour but the wrong interface | Integrate third-party or legacy code; make incompatible interfaces work together |
| Bridge | Separate abstraction from implementation so both can vary independently | Parallel inheritance hierarchies: creating a subclass for one forces a subclass for another | Two dimensions of variation that must evolve independently; avoid permanent binding between abstraction and implementation |
| Composite | Treat individual objects and compositions uniformly via a shared interface | Code must treat primitive and container objects the same way | Tree structures; UI components; any part-whole hierarchy |
| Decorator | Add responsibilities to an object dynamically without subclassing | Subclass explosion from combining optional features; need to add behaviour without modifying existing classes | Layered features (logging, caching, compression); avoid "God Object" from feature accumulation |
| Facade | Provide a simplified interface to a complex subsystem | Complex subsystem requires initializing many objects, tracking dependencies, correct ordering; business logic coupled to implementation details | Limited straightforward interface to complex subsystem; structure subsystem into layers. Caution: can become god object |
| Flyweight | Share fine-grained objects to reduce memory when many similar instances are needed | Too many similar objects consuming excessive memory | Large numbers of similar objects (characters in a text editor, tiles in a game); intrinsic vs extrinsic state separation |
| Proxy | Control access to an object via a surrogate (lazy init, access control, logging) | Object is expensive to create, needs access control, or requires remote access | Lazy initialization; access control; logging; remote object access |

#### Behavioral

| Pattern | Intent | Problem | Applicability |
|---|---|---|---|
| Chain of Responsibility | Pass a request along a chain of handlers until one handles it | Multiple handlers may process a request, but which one is determined at runtime | Event bubbling; logging levels; validation pipelines; middleware stacks |
| Command | Encapsulate a request as an object, enabling undo/redo and queuing | Requests are tied to specific callers; undo/redo needed; request execution must be deferred | Undo/redo; job queues; macro recording; UI action handling |
| Iterator | Provide sequential access to elements without exposing the underlying structure | Collection internals are exposed to clients; different collection types need uniform traversal | Custom collection traversal; filtering; lazy iteration over large datasets |
| Mediator | Centralize complex communication between objects through a mediator object | Many-to-many communication between objects; objects know too much about each other | UI form coordination; air traffic control; chat room; replace complex fan-out with central hub |
| Memento | Capture and restore object state without violating encapsulation | Direct state access violates encapsulation; need to save/restore state | Undo/redo (with Command); snapshots; transaction rollback |
| Observer | Define a one-to-many dependency so dependents are notified automatically | Either observers poll subject (wasteful) or subject notifies all (wasteful if not all interested); set of dependents is unknown or dynamic | State change in one object requires changing others; dynamic subscribe/unsubscribe; event systems. Structure: Publisher + Subscriber interface + Concrete Subscribers |
| State | Allow an object to alter its behaviour when its internal state changes | State machine with conditionals grows into bloated mess; each new state requires changing conditionals in every method. States may know about each other and initiate transitions | Object behaves differently per current state with many states and frequent changes; class polluted with massive conditionals on state fields. Key distinction from Strategy: states may trigger transitions |
| Strategy | Define a family of algorithms, encapsulate each, and make them interchangeable | Class has many variants of same algorithm, each adding bloat, merge conflicts, changes to one algorithm affect whole class. Strategies are independent and unaware of each other | Massive conditional switching between algorithm variants; many similar classes differing only in behavior execution; isolating business logic from algorithm details. Key distinction from State: strategies don't know about each other |
| Template Method | Define the skeleton of an algorithm; let subclasses fill in specific steps | Two methods share the same algorithm structure but differ in one or two steps | Framework design; invariant algorithm with variable steps; avoid duplicate control flow in subclasses |
| Visitor | Separate an algorithm from the object structure it operates on | Adding operations to a stable object structure requires modifying every element class | Compiler AST passes; reporting over stable data structures; double dispatch needs |

### Quick Smell to Pattern Lookup

| Smell | Pattern |
|---|---|
| Same object constructed in 3+ places | Factory Method / Factory Function |
| Multi-step setup before object is valid | Builder |
| Branching on a type, kind, or status field | Strategy |
| Method uses another class's data more than its own | Move Method (Fowler) |
| Two class hierarchies that grow in lockstep | Bridge |
| Many methods branch on the same state field | State |
| Object directly calls multiple downstream systems on change | Observer |
| Two functions share the same algorithm skeleton, differ in one step | Template Method |
| Subsystem is complex and callers need a simple entry point | Facade |
| Need to add behaviour to objects without modifying their classes | Decorator |
| Incompatible interface between collaborating classes | Adapter |
| Need to treat individual and composite objects uniformly | Composite |

### Pattern Smell Checks (Verification)

| Code smell | Pattern missed | How to check |
|---|---|---|
| Multiple if/elif on type/state | State or Strategy | Search for `isinstance` chains |
| Complex `__init__` | Factory or Builder | Check line count and side effects |
| Callers know multiple components | Facade | Check caller coupling |
| External dep without Protocol | Adapter or Repository | Check dependency injection |
| 0 domain classes, many functions | Missing domain model | Count classes vs functions |
| Repeated algorithm skeleton | Template Method | Find duplicate control flow |
| Direct calls to multiple listeners | Observer | Find fan-out call sites |

## Related

- [[software-craft/smell-catalogue]] — smells trigger pattern selection
- [[software-craft/refactoring-techniques]] — refactoring techniques that resolve smells before patterns are needed
- [[software-craft/refactoring]] — when and how to refactor, clean code, technical debt
- [[software-craft/solid]] — patterns resolve SOLID violations
- [[software-craft/object-calisthenics]] — Object Calisthenics rules complement pattern application
- [[software-craft/tdd]] — patterns are applied during REFACTOR phase
