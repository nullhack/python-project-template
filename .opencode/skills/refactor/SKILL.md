---
name: refactor
description: Safe refactoring protocol for TDD — green bar rule, two-hats discipline, preparatory refactoring, and smell catalogue
version: "2.0"
author: software-engineer
audience: software-engineer
workflow: feature-lifecycle
---

# Refactor

Load this skill when entering the REFACTOR phase of a TDD cycle, or before starting RED on a new `@id` when preparatory refactoring is needed.

Sources: Fowler *Refactoring* 2nd ed. (2018); Beck *Canon TDD* (2023); Beck *Tidy First?* (2023); Martin *SOLID* (2000); Bay *Object Calisthenics* (2005); Shvets *Refactoring.Guru* (2014–present). See `docs/research/oop-design.md` entries 33–36 and `docs/research/refactoring-empirical.md`.

---

## The Definition

A refactoring is a **behaviour-preserving** transformation of internal structure. If the transformation changes observable behaviour, it is not a refactoring — it is a feature change, and requires its own RED-GREEN-REFACTOR cycle.

---

## The Green Bar Rule (absolute)

**Refactoring is only permitted while all existing tests pass.**

Every individual refactoring step must leave `test-fast` green. There are no exceptions.

---

## The Two-Hats Rule

Wear one hat at a time:

| Hat | Activity | Allowed during this hat |
|---|---|---|
| **Feature hat** | RED → GREEN | Write failing test, write minimum code to pass |
| **Refactoring hat** | REFACTOR | Restructure passing code; never add new behaviour |

**Never mix hats in the same step.** If you discover a refactoring is needed while making a test pass (GREEN), note it — finish GREEN first, then switch hats.

---

## When to Use

### 1. REFACTOR phase (opportunistic)

After GREEN: `test-fast` passes for the current `@id`. Now restructure.

### 2. Preparatory refactoring (before RED)

When the current structure would make the next `@id` awkward to implement:
- Put on the **refactoring hat first**
- Refactor until the feature is easy to add
- Commit the preparatory refactoring separately (see Commit Discipline)
- Then put on the feature hat and run RED-GREEN-REFACTOR normally

Beck: *"For each desired change, make the change easy (warning: this may be hard), then make the easy change."*

---

## Step-by-Step

### Step 1 — Identify the smell

Run the smell checklist from your Self-Declaration or from the Architecture Smell Check.

Smell categories from Shvets *Refactoring.Guru* (2014–present); each smell links to its Fowler catalogue entry.

#### Bloaters — structures grown too large

| Smell | Signal | Likely catalogue entry |
|---|---|---|
| Long Method | Method body needs a comment to understand any section | Extract Function, Decompose Conditional |
| Large Class | Class has too many responsibilities or instance variables | Extract Class, Extract Subclass |
| Primitive Obsession | Domain concept represented as a raw primitive | Replace Primitive with Object, Introduce Parameter Object |
| Long Parameter List | Function takes 3+ parameters, or parameter group repeats across signatures | Introduce Parameter Object, Replace Parameter with Query |
| Data Clumps | Same 2–3 data items always appear together across signatures or fields | Introduce Parameter Object, Extract Class |

#### OO Abusers — misapplied OOP

| Smell | Signal | Likely catalogue entry |
|---|---|---|
| Switch Statements | Repeated `if/elif` or match on a type flag across callers | Replace Conditional with Polymorphism, Strategy, State |
| Temporary Field | Instance variable set only in some code paths; `None` in others | Extract Class, Introduce Null Object |
| Refused Bequest | Subclass inherits methods/data it does not use or overrides to do nothing | Push Down Method/Field, Replace Inheritance with Delegation |
| Alternative Classes with Different Interfaces | Two classes do the same thing under different names/signatures | Rename Method, Extract Superclass, unify via Protocol |

#### Change Preventers — changes ripple unexpectedly

| Smell | Signal | Likely catalogue entry |
|---|---|---|
| Divergent Change | One class must change for multiple unrelated reasons | Extract Class (split by axis of change) |
| Shotgun Surgery | One concept change touches many classes | Move Function/Field, Inline Class, combine scattered behaviour |
| Parallel Inheritance Hierarchies | Adding a subclass to one hierarchy forces a new subclass in another | Move Function/Field to flatten or unify hierarchies |

#### Dispensables — dead weight

| Smell | Signal | Likely catalogue entry |
|---|---|---|
| Comments | Comment explains *what* or *why* when the code could be self-explanatory | Extract Function, Rename Variable/Function |
| Duplicate Code | Same logic copied in 2+ places | Extract Function, Pull Up Method, Form Template Method |
| Lazy Class | Class does too little to justify its existence | Inline Class, Collapse Hierarchy |
| Data Class | Class holds only fields with getters/setters; no behaviour | Move Function into class, Encapsulate Field |
| Dead Code | Unreachable code, unused variable, never-called function | Delete it |
| Speculative Generality | Abstractions added "for future use" with no current caller | Inline Class/Function, Remove unused parameters |

#### Couplers — excessive inter-object dependency

| Smell | Signal | Likely catalogue entry |
|---|---|---|
| Feature Envy | Method uses another class's data more than its own | Move Function, Extract Function |
| Inappropriate Intimacy | Class accesses another's private fields or implementation details | Move Function/Field, Extract Class, Replace Inheritance with Delegation |
| Message Chains | `a.b().c().d()` — navigating a chain of objects | Hide Delegate, Extract Function to encapsulate the chain |
| Middle Man | Class delegates most of its methods to another class | Inline Class, Remove Middle Man |
| Incomplete Library Class | External class lacks a needed method | Introduce Foreign Method, Introduce Extension Object |

If pattern smell detected: load `skill apply-patterns` for pattern selection guidance.

### Step 2 — Apply one catalogue entry at a time

Apply a **single** catalogue entry, then run `test-fast` before moving to the next.

Never batch multiple catalogue entries into one step — you lose the ability to pinpoint which step broke something.

### Step 3 — Run after each step

```bash
uv run task test-fast
```

All tests green → proceed to next catalogue entry.
Any test red → see "When a Refactoring Breaks a Test" below.

### Step 4 — Commit when smell-free

Once no smells remain and `test-fast` is green:

```bash
uv run task test-fast   # must pass
```

Commit (see Commit Discipline below).

---

## Key Catalogue Entries

### Extract Function
Pull a cohesive fragment into a named function.

**Trigger**: a fragment needs a comment to explain what it does.
**Outcome**: the extracted function's name makes the comment unnecessary; the caller reads as a sequence of named steps.

### Extract Class
Split a class that is doing two jobs.

**Trigger**: a data cluster (2–3 fields that always travel together) with related behaviour that could be named independently.
**Outcome**: each class has one reason to change; the new class becomes a value object or a collaborator.

### Introduce Parameter Object
Replace a recurring parameter group with a dedicated object.

**Trigger**: the same 2+ parameters appear together across multiple function signatures.
**Outcome**: a named type captures the concept; callers are simplified; the object can later carry behaviour.

### Replace Primitive with Object
Elevate a domain concept represented as a raw primitive to its own type.

**Trigger**: a primitive has validation rules, formatting logic, or operations that are repeated at every call site.
**Outcome**: behaviour moves into the type; callers are protected from invalid states; the type can be named and tested independently.

### Decompose Conditional / Guard Clauses
Flatten nested conditional logic to ≤2 levels.

**Trigger**: OC-1 violation (nesting beyond one indent level per method), or multi-level nested `if` chains.
**Outcome**: each exit condition is expressed as an early return (guard clause); the happy path is at the left margin; no `else` after `return`.

---

## When a Refactoring Breaks a Test

A refactoring that breaks a test is **not a refactoring**. Stop. Diagnose:

### Diagnosis flow

```
Test fails after a structural change
         │
         ▼
Is the test testing internal structure
(private methods, specific call chains,
concrete types) rather than observable behaviour?
         │
    YES  │  NO
         │   └──→ The "refactoring" changed observable behaviour.
         │         This is a FEATURE CHANGE.
         │         Revert the step.
         │         Put on the feature hat.
         │         Run RED-GREEN-REFACTOR for it explicitly.
         ▼
Rewrite the test to use the public interface.
Re-apply the refactoring step.
Run test-fast — must be green.
```

**Never delete a failing test without diagnosing it first.**

---

## Commit Discipline

Refactoring commits are always **separate** from feature commits.

| Commit type | Message format | When |
|---|---|---|
| Preparatory refactoring | `refactor(<feature-stem>): <what>` | Before RED, to make the feature easier |
| REFACTOR phase | `refactor(<feature-stem>): <what>` | After GREEN, cleaning up the green code |
| Feature addition | `feat(<feature-stem>): <what>` | After GREEN (never mixed with refactor) |

Never mix a structural cleanup with a behaviour addition in one commit. This keeps history bisectable and CI green at every commit.

---

## Self-Declaration Check (before exiting REFACTOR)

Before marking the `@id` complete, verify all of the following. Each failed item is a smell — apply the catalogue entry, run `test-fast`, then re-check.

### Green Bar
- [ ] `test-fast` passes
- [ ] No smell from the checklist in Step 1 remains

### Object Calisthenics (Bay 2005)
| Rule | Constraint | Violation signal |
|---|---|---|
| OC-1 | One indent level per method | `for` inside `if` inside a method body |
| OC-2 | No `else` after `return` | `if cond: return x` then `else: return y` |
| OC-3 | Wrap primitives with domain meaning | `def process(user_id: int)` instead of `UserId` |
| OC-4 | Wrap collections with domain meaning | `list[Order]` passed around instead of `OrderCollection` |
| OC-5 | One dot per line | `obj.repo.find(id).name` |
| OC-6 | No abbreviations | `usr`, `mgr`, `cfg`, `val`, `tmp` |
| OC-7 | Classes ≤ 50 lines, methods ≤ 20 lines | Any method requiring scrolling |
| OC-8 | ≤ 2 instance variables per class *(behavioural classes only; dataclasses, Pydantic models, value objects, and TypedDicts are exempt)* | `__init__` with 3+ `self.x =` assignments in a behavioural class |
| OC-9 | No getters/setters | `def get_name(self)` / `def set_name(self, v)` |

### SOLID (Martin 2000)
| Principle | Check | Violation signal |
|---|---|---|
| **S** — Single Responsibility | Does this class have exactly one reason to change? | Class handles data + formatting, or business logic + persistence |
| **O** — Open/Closed | Can new behaviour be added without editing this class? | Adding a case requires editing an `if/elif` chain inside the class |
| **L** — Liskov Substitution | Do all subtypes honour the full contract of their base type? | Subclass raises on an inherited method, or narrows a precondition |
| **I** — Interface Segregation | Does every implementor use every method in the interface? | Implementors stub out methods they don't need |
| **D** — Dependency Inversion | Does domain code depend only on abstractions, not concrete I/O? | Domain class directly imports a database, file, or network class |

### Law of Demeter / Tell, Don't Ask / CQS

**Law of Demeter** — a method should only call methods on: `self`, its parameters, objects it creates, and its direct components.
- Violation signal: chaining through two or more intermediaries (`a.b().c()`). Ask `a` to do the thing instead of navigating through it.

**Tell, Don't Ask** — tell objects what to do; don't query their state and decide externally.
- Violation signal: querying an object's status field, then setting it based on that query from outside the object. Move the decision into the object itself.

**Command-Query Separation** — a method either changes state (command) or returns a value (query), never both.
- Apply to domain objects. Standard library collections are a known exception (e.g., pop-style methods).

### Design Clarity Signals

| Principle | Signal |
|---|---|
| Explicit over implicit | Dependencies stated at construction; no hidden side effects or magic initialization |
| Simple over complex | One function, one job; prefer a plain function over a class when no state is needed |
| Flat over nested | OC-1 — one indent level per method; early returns over deep nesting |
| Readability | OC-6 — no abbreviations; public items documented |
| Errors surface explicitly | Raise on invalid input; never silently swallow errors or return a default that hides failure |
| No ambiguous defaults | Invalid input raises; callers are never surprised by silent fallbacks |

### Type and documentation hygiene
- [ ] Type annotations present on all public signatures
- [ ] Documentation present on all public classes and methods
