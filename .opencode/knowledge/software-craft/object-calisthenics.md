---
domain: software-craft
tags: [object-calisthenics, oc, design-constraints, code-quality]
last-updated: 2026-04-30
---

# Object Calisthenics

## Key Takeaways

- OC-1: Use only one level of indentation per method — deep nesting signals mixed concerns.
- OC-2: Do not use the `else` keyword — early returns and guard clauses eliminate branching.
- OC-3: Wrap all primitives and strings in small domain-specific types — `Age` instead of `int`, `Email` instead of `str`.
- OC-4: Use only one dot per line — `a.b.c` is a Law of Demeter violation; the middle object should handle the request.
- OC-5: Do not abbreviate names — if a name is long, the scope is too broad or the concept is unclear.
- OC-6: Keep all entities small — classes ≤ 50 lines, methods ≤ 5 lines, packages with ≤ 10 classes.
- OC-7: Do not use more than two instance variables per class — more signals the class has multiple responsibilities (Bay, 2008).
- OC-8: Use first-class collections — a class that holds a collection should hold no other instance variables.
- OC-9: Do not use getters, setters, or properties — tell objects to do work rather than asking for their data (Tell, Don't Ask).

## Concepts

**OC-1: One Level of Indentation** — Nested `if`/`for`/`try` blocks indicate that a method is doing too many things. Extract each nested block into its own method with a descriptive name. The result is a sequence of guard clauses and early returns, each expressing a single decision.

**OC-2: No Else** — Every `else` branch can be replaced by an early return (guard clause), a ternary expression, or polymorphism. Early returns eliminate the cognitive load of tracking which branch you are in. Polymorphism replaces conditional branching with type-driven dispatch.

**OC-3: Wrap Primitives** — A bare `int` could be an age, a quantity, a score, or an ID. Wrapping primitives in domain-specific types (`Age`, `Quantity`, `Score`, `ID`) gives the type system enforcement power, prevents invalid combinations (you cannot add an `Age` to a `Score`), and attaches behaviour to the data it describes.

**OC-4: One Dot Per Line** — `a.b.c` means the caller knows about the internal structure of `a.b`. This violates encapsulation and the Law of Demeter. The fix: ask `a` to perform the operation, delegating through `b` internally. Each object should talk to its immediate neighbours, not their neighbours.

**OC-5: No Abbreviations** — Abbreviations obscure meaning and create ambiguity. `usr` could mean user, usual, or USB. If a name is too long to type, the method or class is probably doing too much — extract until the name is naturally short.

**OC-6: Small Entities** — A class longer than 50 lines is doing too many things. A method longer than 5 lines is mixing levels of abstraction. A package with more than 10 classes lacks a clear boundary. These thresholds force decomposition toward single-responsibility objects.

**OC-7: Two Instance Variables** (Bay, 2008) — More than two instance variables means the class is holding multiple responsibilities. Each variable represents a cohesive cluster; three or more clusters signal the need to extract collaborators. This is the most impactful constraint: it directly prevents god-objects and forces distribution of behaviour.

**OC-8: First-Class Collections** — When a class contains a collection (list, dict, set), that collection should be the only instance variable. The class becomes the collection's behaviour: filtering, mapping, validating, computing aggregates. This prevents a collection from being one of five variables in a class that also holds configuration, state, and identifiers.

**OC-9: Tell, Don't Ask** — Calling `obj.get_x()` then making a decision based on the result means the caller owns the decision. Instead, `obj.do_thing()` lets the object own its own behaviour. Getters expose internal structure and invite misuse; telling objects to act preserves encapsulation and keeps behaviour where the data lives.

## Related

- [[software-craft/tdd]] — design principle priority includes Object Calisthenics
- [[software-craft/code-review]] — self-declaration checks include Object Calisthenics
- [[software-craft/smell-catalogue]] — Object Calisthenics violations overlap with smell signals
- [[software-craft/design-patterns]] — patterns complement Object Calisthenics rules
- [[software-craft/refactoring-techniques]] — Object Calisthenics violations signal specific refactoring opportunities
- [[software-craft/solid]] — Object Calisthenics rules overlap with SOLID (ObjCal-7 enforces SRP, ObjCal-4 enforces DIP)
- [[software-craft/refactoring]] — when and how to refactor, clean code, technical debt
- [[requirements/pre-mortem]] — pre-mortem checks include ObjCal-7 (two instance variables)