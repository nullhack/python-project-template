---
domain: software-craft
tags: [code-smells, refactoring, fowler, code-quality]
last-updated: 2026-04-30
---

# Smell Catalogue

## Key Takeaways

- Bloaters (Long Method, Large Class, Primitive Obsession, Long Parameter List, Data Clumps) are structures that have grown too large; apply Extract Function/Class, Replace Primitive with Object, or Introduce Parameter Object (Fowler, 1999; Shvets, 2014).
- OO Abusers (Switch Statements, Temporary Field, Refused Bequest, Alternative Classes with Different Interfaces) misapply OOP; apply polymorphism, Extract Class, or Replace Inheritance with Delegation.
- Change Preventers (Divergent Change, Shotgun Surgery, Parallel Inheritance Hierarchies) cause changes to ripple; restructure by axis of change or move functions/fields.
- Dispensables (Comments, Duplicate Code, Lazy Class, Data Class, Dead Code, Speculative Generality) are dead weight; extract, inline, or delete.
- Couplers (Feature Envy, Inappropriate Intimacy, Message Chains, Middle Man, Incomplete Library Class) create excessive inter-object dependency; move functions, extract classes, or hide delegates.

## Concepts

**Bloaters**: Structures that have grown to gargantuan proportions. They accumulate over time as the program evolves, usually unnoticed until they become blockers. Unlike other smell categories, bloaters are not introduced deliberately — they creep in because "it's easier to add one more line than to refactor." Long Method needs a comment to understand sections. Large Class has too many responsibilities or instance variables. Primitive Obsession uses raw primitives for domain concepts (strings as field names, constants for type codes). Long Parameter List has 3+ parameters or recurring parameter groups. Data Clumps have 2-3 data items always appearing together across multiple signatures or fields (Shvets, 2014).

**OO Abusers**: Incomplete or incorrect application of object-oriented programming. These smells arise when developers use OOP tools (inheritance, polymorphism, encapsulation) incorrectly or partially. Switch Statements use repeated `if/elif` or match on a type flag instead of polymorphism. Temporary Field is an instance variable set only in some code paths — an object is not always fully populated. Refused Bequest is a subclass that inherits methods it does not use, or overrides them to do nothing. Alternative Classes with Different Interfaces are two classes doing the same thing under different names (Shvets, 2014).

**Change Preventers**: Changes that ripple unexpectedly across the codebase. These are the most damaging smells because they make the codebase resistant to change. Divergent Change requires one class to change for multiple unrelated reasons (one-to-many axis). Shotgun Surgery requires touching many classes for one concept change (many-to-one axis). Parallel Inheritance Hierarchies require new subclasses in lockstep across two hierarchies (Shvets, 2014).

**Dispensables**: Dead weight that makes the codebase harder to maintain. Something unnecessary is present, and removing it would make the code cleaner. Comments explain what code could make obvious. Duplicate Code copies logic in 2+ places. Lazy Class does too little to justify its existence. Data Class holds only fields with getters/setters. Dead Code is unreachable. Speculative Generality adds abstractions for future use with no current caller (Shvets, 2014).

**Couplers**: Excessive coupling between classes, or excessive delegation that replaces one form of coupling with another. Feature Envy uses another class's data more than its own. Inappropriate Intimacy accesses another's private fields. Message Chains navigate through `a.b().c().d()`. Middle Man delegates most methods to another class, adding no value. Incomplete Library Class lacks a needed method on an external class (Shvets, 2014).

## Content

### Bloaters

| Smell | Signal | Why It Happens | Detection | Refactoring |
|---|---|---|---|---|
| Long Method | Method body needs a comment to understand any section; >10 lines is a warning sign | Easier to add a line than refactor; conditional branches grow; comments replace extraction | Method line count >10; comments inside method body that label sections | Extract Method, Decompose Conditional, Replace Temp with Query |
| Large Class | Class has too many responsibilities or instance variables | Class grows by accretion; each new feature adds fields and methods; "God Object" | Instance variable count >2 (OC-7); class line count >50; class name contains "Manager" or "Handler" | Extract Class, Extract Subclass, Extract Interface |
| Primitive Obsession | Domain concept represented as a raw primitive; constants for type codes; strings as field names | Creating a class feels like overkill; habit from non-OO languages; fear of "too many classes" | `isinstance` checks on primitives; string/integer constants used as type flags; dictionaries with fixed keys | Replace Data Value with Object, Replace Type Code with Class, Introduce Parameter Object |
| Long Parameter List | Function takes 3+ parameters, or parameter group repeats across signatures | Method needs data from several sources; fear of making object dependencies explicit; passing individual fields instead of objects | Parameter count >3; same group of parameters appears in 2+ method signatures | Introduce Parameter Object, Preserve Whole Object, Replace Parameter with Method Call |
| Data Clumps | Same 2-3 data items always appear together across signatures or fields | Related data not yet recognised as a domain concept; laziness in creating a value object | Search for repeated parameter groups; fields that always appear together in constructors | Introduce Parameter Object, Extract Class, Preserve Whole Object |

### OO Abusers

| Smell | Signal | Why It Happens | Detection | Refactoring |
|---|---|---|---|---|
| Switch Statements | Repeated `if/elif` or match on a type flag across callers | Developer hasn't learned polymorphism; performance fear; habit from procedural languages | `isinstance` chains; `if x.type ==` patterns; match statements on type/kind/status fields | Replace Conditional with Polymorphism, Replace Type Code with State/Strategy, Extract Method |
| Temporary Field | Instance variable set only in some code paths; `None` in others | A field is needed only for a specific algorithm or code path; object partially initialised | `None` default values that "should never be None during usage"; fields used only in one method | Extract Class, Introduce Null Object |
| Refused Bequest | Subclass inherits methods/data it does not use or overrides to do nothing | Subclass created for reuse of only part of a superclass; hierarchy doesn't match responsibility | `NotImplementedError` overrides; methods that just call `super()` with no addition; `pass` bodies | Push Down Method/Field, Replace Inheritance with Delegation, Extract Subclass |
| Alternative Classes with Different Interfaces | Two classes do the same thing under different names/signatures | Independent development by different people; renaming one was never done | Two classes with similar method sets but different names; same data, different method names | Rename Method, Extract Superclass, unify via Protocol |

### Change Preventers

| Smell | Signal | Why It Happens | Detection | Refactoring |
|---|---|---|---|---|
| Divergent Change | One class must change for multiple unrelated reasons | Class accumulated multiple responsibilities over time; no Extract Class was done | When a single requirement change touches one class in multiple places; class name contains multiple nouns | Extract Class (split by axis of change) |
| Shotgun Surgery | One concept change touches many classes | Behaviour scattered across classes instead of co-located; over-decomposition | Touch count per requirement; many files changed in one PR for a single concept | Move Method, Move Field, Inline Class, combine scattered behaviour |
| Parallel Inheritance Hierarchies | Adding a subclass to one hierarchy forces a new subclass in another | Two hierarchies evolved in tandem but weren't unified; duplicate dispatch | New subclass requires creating matching subclass elsewhere; hierarchy depth is identical | Move Method, Move Field to flatten or unify hierarchies |

### Dispensables

| Smell | Signal | Why It Happens | Detection | Refactoring |
|---|---|---|---|---|
| Comments | Comment explains *what* or *why* when code could be self-explanatory | Complex code that should be simplified; fear of deleting comments; documenting intent instead of improving code | Comments inside methods that label sections; "This hack is needed because…" | Extract Method, Rename Variable, Rename Method |
| Duplicate Code | Same logic copied in 2+ places | Copy-paste for "quick fix"; fear of breaking existing code by extracting; different context same logic | Same 3+ lines appearing in multiple methods; similar conditional structures | Extract Method, Pull Up Method, Form Template Method, Extract Class |
| Lazy Class | Class does too little to justify its existence | Once-useful class reduced by refactoring; over-decomposition; premature extraction | Class with <3 methods; class used in only one place | Inline Class, Collapse Hierarchy |
| Data Class | Class holds only fields with getters/setters; no behaviour | Database-first design; DTOs that never gained behaviour; anemic domain model | Class with only `__init__`, getters, setters; all logic in callers | Move Method into class, Encapsulate Field |
| Dead Code | Unreachable code, unused variable, never-called function | Feature removed but code left behind; commented-out code; conditional always false | Linter warnings; code coverage gaps; imports of unused modules | Delete it |
| Speculative Generality | Abstractions added "for future use" with no current caller | Over-engineering; "we might need this"; framework mindset in application code | Abstract classes with one subclass; unused parameters; methods never called from production code | Inline Class, Inline Method, Remove unused parameters |

### Couplers

| Smell | Signal | Why It Happens | Detection | Refactoring |
|---|---|---|---|---|
| Feature Envy | Method uses another class's data more than its own | Method was placed in the wrong class; data and behaviour separated; anemic domain model | Method makes more calls to another class than its own; accesses another's fields via getters | Move Method, Extract Method |
| Inappropriate Intimacy | Class accesses another's private fields or implementation details | Over-familiarity between classes; evolved from one class split incompletely; test class accessing internals | Direct access to `_private` attributes; one class importing internal modules of another | Move Method, Move Field, Extract Class, Replace Inheritance with Delegation |
| Message Chains | `a.b().c().d()` — navigating a chain of objects | Client knows too much about object structure; intermediate objects treated as mere pass-throughs | Chained method calls where each returns a different object; `getattr` chains | Hide Delegate, Extract Method to encapsulate the chain |
| Middle Man | Class delegates most of its methods to another class | Overzealous delegation; class existed for an interface that was later simplified | >50% of methods are one-line delegations; class adds no logic beyond forwarding | Inline Class, Remove Middle Man |
| Incomplete Library Class | External class lacks a needed method | Third-party library doesn't support your use case; library API incomplete for your domain | Utility functions that take a library object as first argument; wrapper classes that add one method | Introduce Foreign Method, Introduce Local Extension |

## Related

- [[software-craft/design-patterns]] — pattern selection starts from smell identification
- [[software-craft/refactoring-techniques]] — the refactoring techniques referenced in each smell entry
- [[software-craft/refactoring]] — when and how to refactor, clean code, technical debt
- [[software-craft/solid]] — SOLID violations manifest as specific smells
- [[software-craft/tdd]] — smells are identified and resolved during REFACTOR phase
- [[software-craft/object-calisthenics]] — OC violations overlap with smell signals
- [[software-craft/code-review]] — smells are checked during design review
