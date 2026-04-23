---
name: apply-patterns
description: GoF design pattern catalogue — smell triggers and before/after structural descriptions
version: "3.0"
author: software-engineer
audience: software-engineer
workflow: feature-lifecycle
---

# Design Patterns Reference

Load this skill when the refactor skill's smell table points to a GoF pattern and you need structural guidance on how to apply it.

Sources: Gamma, Helm, Johnson, Vlissides. *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley, 1995; Shvets, A. *Refactoring.Guru* (2014–present) https://refactoring.guru/design-patterns. See `docs/research/oop-design.md` entries 34 and 36.

---

## When to Use

Load this skill when the `refactor` skill's smell table points to a GoF pattern, or when the `implement` skill's Silent Pre-mortem detects a pattern smell in architecture stubs.

## Step-by-Step

1. **Identify the smell** from the refactor skill's lookup table
2. **Find the smell category** below (Creational / Structural / Behavioral)
3. **Read the trigger and the before/after example**
4. **Apply the pattern** — update the stub files (Step 2) or the refactored code (Step 3)

---

## GoF Pattern Catalogue — One-Liner Reference

### Creational
| Pattern | Intent |
|---|---|
| **Factory Method** | Delegate object creation to a subclass or factory function |
| **Abstract Factory** | Create families of related objects without specifying concrete classes |
| **Builder** | Construct complex objects step-by-step, separating construction from representation |
| **Prototype** | Clone existing objects instead of creating new ones from scratch |
| **Singleton** | Ensure a class has only one instance (use sparingly — prefer dependency injection) |

### Structural
| Pattern | Intent |
|---|---|
| **Adapter** | Wrap an incompatible interface to match an expected interface |
| **Bridge** | Separate abstraction from implementation so both can vary independently |
| **Composite** | Treat individual objects and compositions uniformly via a shared interface |
| **Decorator** | Add responsibilities to an object dynamically without subclassing |
| **Facade** | Provide a simplified interface to a complex subsystem |
| **Flyweight** | Share fine-grained objects to reduce memory when many similar instances are needed |
| **Proxy** | Control access to an object via a surrogate (lazy init, access control, logging) |

### Behavioral
| Pattern | Intent |
|---|---|
| **Chain of Responsibility** | Pass a request along a chain of handlers until one handles it |
| **Command** | Encapsulate a request as an object, enabling undo/redo and queuing |
| **Interpreter** | Define a grammar and an interpreter for a language |
| **Iterator** | Provide sequential access to elements without exposing the underlying structure |
| **Mediator** | Centralize complex communication between objects through a mediator object |
| **Memento** | Capture and restore object state without violating encapsulation |
| **Observer** | Define a one-to-many dependency so dependents are notified automatically |
| **State** | Allow an object to alter its behaviour when its internal state changes |
| **Strategy** | Define a family of algorithms, encapsulate each, and make them interchangeable |
| **Template Method** | Define the skeleton of an algorithm; let subclasses fill in specific steps |
| **Visitor** | Separate an algorithm from the object structure it operates on |

---

## Smell-Triggered Patterns

### Creational Smells

---

#### Smell: Scattered Object Construction
**Signal**: The same object is constructed in 3+ places with slightly different arguments, or construction logic is duplicated across callers. Changes to construction (e.g. adding a required field) require updating every call site.

**Pattern**: Factory Method or Factory Function

**Before**: Construction is repeated inline at every call site with raw arguments. Tests, services, and importers each hardcode the construction details.

**After**: A dedicated factory function or factory method owns construction. All callers go through it. The factory can inject defaults, substitute a clock or ID generator, and be swapped in tests.

**Key structural change**: Creation knowledge moves from N call sites to one place.

---

#### Smell: Multi-Step Construction with Optional Parts
**Signal**: An object requires several setup calls before it is valid. Callers must remember the correct sequence. Forgetting a step leaves the object in an invalid or partially initialised state.

**Pattern**: Builder

**Before**: Object constructed with a series of setter calls. Order matters but is not enforced. Optional sections may be skipped by accident.

**After**: A builder object accepts each optional part via named methods and produces the final object only when `build()` is called. The builder validates completeness and enforces sequence.

**Key structural change**: Invalid intermediate states are impossible; callers read as a named sequence of intent.

---

### Structural Smells

---

#### Smell: Type-Switching (branching on a type or status field)
**Signal**: A function or method branches on a type flag, kind field, or status string. Adding a new variant requires editing this function — it is open to modification but closed to extension.

**Pattern**: Strategy (behaviour varies per call) or Visitor (operation varies over a fixed structure)

**Before**: A single function contains a multi-branch conditional on the variant. Every new variant requires modifying the function and all its tests.

**After (Strategy)**: Each variant is encapsulated in its own class implementing a shared interface. The caller receives the strategy as a dependency. Adding a new variant means adding a new class — the caller and existing variants are untouched.

**After (Visitor)**: When the object structure is stable but operations vary, a visitor separates each operation into its own class. Each element accepts a visitor and dispatches to the right method.

**Key structural change**: Open/Closed principle restored — new variants extend without modifying existing code.

---

#### Smell: Feature Envy
**Signal**: A method in class A uses data or methods from class B more than its own. The method "envies" class B and is likely in the wrong place.

**Pattern**: Move Function (Fowler) — often a precursor to Strategy or Command

**Before**: A method on one class navigates into another class's fields to perform a computation. The computation is separated from the data it operates on.

**After**: The computation moves to the class whose data it uses. The original class delegates to it. The envied class gains behaviour; the original class becomes a coordinator.

**Key structural change**: Behavior lives next to the data it depends on.

---

#### Smell: Parallel Inheritance Hierarchies
**Signal**: Every time a subclass is added to hierarchy A, a corresponding subclass must also be added to hierarchy B. The two trees grow in lockstep — a sign that the two axes of variation are entangled.

**Pattern**: Bridge

**Before**: Two hierarchies are coupled. A `Shape` hierarchy and a `Renderer` hierarchy grow together. Each shape–renderer combination requires its own subclass.

**After**: The Bridge pattern separates the two hierarchies. The abstraction (shape) holds a reference to the implementation (renderer) as a dependency. Each axis can vary independently. Combinatorial subclass explosion is eliminated.

**Key structural change**: Two axes of variation become two independent hierarchies composed at runtime.

---

### Behavioral Smells

---

#### Smell: Large State Machine in One Class
**Signal**: A class has a status or state field, and many methods begin by branching on that field. Adding a new state requires editing all of those methods. The class grows in proportion to the number of states.

**Pattern**: State

**Before**: The class contains multi-branch conditionals in every method that involves state. Each state's transitions and guards are scattered across the class body.

**After**: Each state is its own class implementing a shared interface. Each state object owns its transitions — it knows which transitions are valid and what the next state is. The context object (the original class) delegates to the current state. Adding a new state means adding a new class.

**Key structural change**: State-specific behaviour is co-located in the state class; the context becomes a thin delegator.

---

#### Smell: Scattered Notification / Event Fan-Out
**Signal**: When something happens in class A, it directly calls methods on classes B, C, and D. Adding a new listener requires modifying class A. Class A knows about all downstream consumers.

**Pattern**: Observer

**Before**: The event source directly invokes each downstream system. The source and all consumers are tightly coupled. Adding a consumer modifies the source.

**After**: The source defines a listener interface and maintains a list of registered listeners. Each listener registers itself. When the event occurs, the source notifies all listeners without knowing their concrete types. New listeners are added without touching the source.

**Key structural change**: Coupling direction reversed — listeners depend on the source, not the other way around.

---

#### Smell: Repeated Algorithm Skeleton
**Signal**: Two or more functions share the same high-level structure (setup → process → teardown, or read → parse → validate → save) but differ only in one or two steps. The structure is copied rather than shared.

**Pattern**: Template Method

**Before**: Two functions duplicate the pipeline structure. When the shared steps change (e.g. validation logic), both must be updated in sync. The differing step is buried inside the duplication.

**After**: A base class defines the algorithm skeleton as a method that calls abstract hook methods for the varying steps. Each subclass implements only the hook(s) that differ. The shared steps exist in one place.

**Key structural change**: Invariant structure lives in one place; variants are isolated in named hooks.

---

## Quick Smell → Pattern Lookup

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

---

## Core Heuristic — Procedural vs OOP

> **When procedural code requires modifying existing functions to add new variants, OOP is the fix.**

Procedural code is open to inspection but open to modification too — every new case touches existing logic.
OOP (via Strategy, State, Observer, etc.) closes existing code to modification and opens it to extension through new types.
The smell is always the same: **a place in the codebase that must change every time the domain grows.**
