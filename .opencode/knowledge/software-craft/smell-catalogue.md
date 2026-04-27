---
domain: software-craft
tags: [smells, refactoring, code-quality, fowler]
last-updated: 2026-04-26
---

# Smell Catalogue

## Key Takeaways

- Identify bloaters (long methods, large classes, primitive obsession, long parameter lists, data clumps) and apply Extract Function/Class, Replace Primitive with Object, or Introduce Parameter Object.
- Detect OO abusers (switch statements, temporary fields, refused bequest, alternative classes) and apply polymorphism, Extract Class, or Replace Inheritance with Delegation.
- Spot change preventers (divergent change, shotgun surgery, parallel hierarchies) and restructure by axis of change or move functions/fields.
- Remove dispensables (comments, duplicate code, lazy classes, data classes, dead code, speculative generality) by extracting, inlining, or deleting.
- Break couplers (feature envy, inappropriate intimacy, message chains, middle men) by moving functions, extracting classes, or hiding delegates.

## Concepts

**Bloaters**: Structures that have grown too large. Long Method needs a comment to understand sections. Large Class has too many responsibilities or instance variables. Primitive Obsession uses raw primitives for domain concepts. Long Parameter List has 3+ parameters or recurring parameter groups. Data Clumps have 2-3 data items always appearing together.

**OO Abusers**: Misapplied OOP constructs. Switch Statements use repeated `if/elif` or match on a type flag. Temporary Field is an instance variable set only in some code paths. Refused Bequest is a subclass that inherits methods it doesn't use. Alternative Classes with Different Interfaces are two classes doing the same thing under different names.

**Change Preventers**: Changes that ripple unexpectedly. Divergent Change requires one class to change for multiple unrelated reasons. Shotgun Surgery requires touching many classes for one concept change. Parallel Inheritance Hierarchies require new subclasses in lockstep.

**Dispensables**: Dead weight in the codebase. Comments explain what code could make obvious. Duplicate Code copies logic in 2+ places. Lazy Classes do too little to justify their existence. Data Classes hold only fields with getters/setters. Dead Code is unreachable. Speculative Generality adds abstractions for future use with no current caller.

**Couplers**: Excessive inter-object dependency. Feature Envy uses another class's data more than its own. Inappropriate Intimacy accesses another's private fields. Message Chains navigate through `a.b().c().d()`. Middle Man delegates most methods to another class. Incomplete Library Class lacks a needed method on an external class.

## Content

### Bloaters — structures grown too large

| Smell | Signal | Likely catalogue entry |
|---|---|---|
| Long Method | Method body needs a comment to understand any section | Extract Function, Decompose Conditional |
| Large Class | Class has too many responsibilities or instance variables | Extract Class, Extract Subclass |
| Primitive Obsession | Domain concept represented as a raw primitive | Replace Primitive with Object, Introduce Parameter Object |
| Long Parameter List | Function takes 3+ parameters, or parameter group repeats across signatures | Introduce Parameter Object, Replace Parameter with Query |
| Data Clumps | Same 2-3 data items always appear together across signatures or fields | Introduce Parameter Object, Extract Class |

### OO Abusers — misapplied OOP

| Smell | Signal | Likely catalogue entry |
|---|---|---|
| Switch Statements | Repeated `if/elif` or match on a type flag across callers | Replace Conditional with Polymorphism, Strategy, State |
| Temporary Field | Instance variable set only in some code paths; `None` in others | Extract Class, Introduce Null Object |
| Refused Bequest | Subclass inherits methods/data it does not use or overrides to do nothing | Push Down Method/Field, Replace Inheritance with Delegation |
| Alternative Classes with Different Interfaces | Two classes do the same thing under different names/signatures | Rename Method, Extract Superclass, unify via Protocol |

### Change Preventers — changes ripple unexpectedly

| Smell | Signal | Likely catalogue entry |
|---|---|---|
| Divergent Change | One class must change for multiple unrelated reasons | Extract Class (split by axis of change) |
| Shotgun Surgery | One concept change touches many classes | Move Function/Field, Inline Class, combine scattered behaviour |
| Parallel Inheritance Hierarchies | Adding a subclass to one hierarchy forces a new subclass in another | Move Function/Field to flatten or unify hierarchies |

### Dispensables — dead weight

| Smell | Signal | Likely catalogue entry |
|---|---|---|
| Comments | Comment explains *what* or *why* when the code could be self-explanatory | Extract Function, Rename Variable/Function |
| Duplicate Code | Same logic copied in 2+ places | Extract Function, Pull Up Method, Form Template Method |
| Lazy Class | Class does too little to justify its existence | Inline Class, Collapse Hierarchy |
| Data Class | Class holds only fields with getters/setters; no behaviour | Move Function into class, Encapsulate Field |
| Dead Code | Unreachable code, unused variable, never-called function | Delete it |
| Speculative Generality | Abstractions added "for future use" with no current caller | Inline Class/Function, Remove unused parameters |

### Couplers — excessive inter-object dependency

| Smell | Signal | Likely catalogue entry |
|---|---|---|
| Feature Envy | Method uses another class's data more than its own | Move Function, Extract Function |
| Inappropriate Intimacy | Class accesses another's private fields or implementation details | Move Function/Field, Extract Class, Replace Inheritance with Delegation |
| Message Chains | `a.b().c().d()` — navigating a chain of objects | Hide Delegate, Extract Function to encapsulate the chain |
| Middle Man | Class delegates most of its methods to another class | Inline Class, Remove Middle Man |
| Incomplete Library Class | External class lacks a needed method | Introduce Foreign Method, Introduce Extension Object |

## Related

- [[software-craft/solid]] — SOLID violations are detectable as specific smells
- [[software-craft/design-patterns]] — pattern selection starts from smell identification
- [[software-craft/tdd]] — smells are identified and resolved during REFACTOR phase
- [[software-craft/object-calisthenics]] — OC violations overlap with smell signals
- [[software-craft/test-design]] — test smells indicate coupling to implementation