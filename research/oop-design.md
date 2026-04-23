# Scientific Research — OOP Design

Foundations for object-oriented design principles used in this template.

---

### 32. Object Calisthenics — Nine Rules

| | |
|---|---|
| **Source** | Bay, J. "Object Calisthenics." *The Thoughtworks Anthology* (PragProg, 2008). Original in IEEE Software/DevX, ~2005. https://www.bennadel.com/resources/uploads/2012/objectcalisthenics.pdf |
| **Date** | ~2005 |
| **Status** | Practitioner synthesis |
| **Core finding** | 9 rules to internalize OOP: (1) One level indentation per method, (2) No ELSE, (3) Wrap primitives/Strings, (4) First class collections, (5) One dot per line, (6) No abbreviations, (7) Classes ≤50 lines, (8) ≤2 instance variables, (9) No getters/setters. 7 of 9 enforce data encapsulation; 1 drives polymorphism; 1 drives naming. |
| **Mechanism** | Restrictions force decomposition. When you cannot use getters, behaviour must move into the object. When you cannot use ELSE, you use polymorphism. When classes must be ≤2 ivars, you discover missing abstractions. |
| **Where used** | Refactor self-declaration checklist in `refactor/SKILL.md`. |

---

### 33. Refactoring

| | |
|---|---|
| **Source** | Fowler, M. (1999/2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.). Addison-Wesley. https://martinfowler.com/books/refactoring.html |
| **Date** | 1999, 2018 |
| **Status** | Confirmed — foundational |
| **Core finding** | Refactoring = behaviour-preserving transformations. 68 catalogued refactorings, each small enough to do safely but cumulative effect significant. Code smells (duplicate code, long methods, feature envy) indicate refactoring opportunities. |
| **Mechanism** | Small steps reduce risk. Each refactoring is reversible. Test suite validates behaviour unchanged. |
| **Where used** | `refactor/SKILL.md`: smell detection triggers refactoring; full protocol and catalogue entries. |

---

### 34. Design Patterns

| | |
|---|---|
| **Source** | Gamma, E., Helm, R., Johnson, R., Vlissides, J. (1995). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley. |
| **Date** | 1995 |
| **Status** | Confirmed — foundational |
| **Core finding** | 23 patterns catalogued in 3 categories: Creational (5), Structural (7), Behavioral (11). Key principles: "Favor composition over inheritance," "Program to an interface, not an implementation." |
| **Mechanism** | Patterns are recurring solutions to common problems. Named and catalogued so developers don't rediscover them. |
| **Where used** | `design-patterns/SKILL.md`: full GoF catalogue with smell-triggered Python before/after examples. |

---

### 35. SOLID Principles

| | |
|---|---|
| **Source** | Martin, R. C. (2000). "Principles of OOD." *ButUncleBob.com*. Acronym coined by Michael Feathers (2004). https://blog.interface-solv.com/wp-content/uploads/2020/07/Principles-Of-OOD.pdf |
| **Date** | 2000 |
| **Status** | Confirmed |
| **Core finding** | S: One reason to change. O: Open extension, closed modification. L: Subtypes substitutable. I: No forced stub methods. D: Depend on abstractions, not concretes. |
| **Mechanism** | Each principle targets a specific coupling failure mode. Together they produce low coupling, high cohesion. |
| **Where used** | Refactor self-declaration checklist in `refactor/SKILL.md`: 5-row SOLID table with Python before/after examples. |

---

### 36. refactoring.guru — Code Smells, Refactoring Techniques, and Design Patterns

| | |
|---|---|
| **Source** | Shvets, A. (2014–present). *Refactoring.Guru*. https://refactoring.guru |
| **Date** | 2014–present (continuously updated) |
| **Status** | Practitioner synthesis — widely used reference |
| **Core finding** | Three interconnected catalogs: (1) **22 code smells** in 5 categories (Bloaters, OO Abusers, Change Preventers, Dispensables, Couplers); (2) **~70 refactoring techniques** in 6 categories (Composing Methods, Moving Features, Organizing Data, Simplifying Conditionals, Simplifying Method Calls, Dealing with Generalization); (3) **22 GoF design patterns** with visual diagrams and multi-language examples. The unique value is the **interconnected navigation**: each smell links to the techniques that address it, and techniques link to patterns they lead toward. |
| **Mechanism** | Navigation chain: smell → techniques → patterns. Smell categories group related structural problems (e.g., Bloaters = classes/methods grown too large; Dispensables = code that can safely be removed; Couplers = excessive dependency between classes). Each technique has a before/after structure, prerequisites, and trade-offs. |
| **Smell categories** | **Bloaters** (Long Method, Large Class, Primitive Obsession, Long Parameter List, Data Clumps); **OO Abusers** (Switch Statements, Temporary Field, Refused Bequest, Alternative Classes with Different Interfaces); **Change Preventers** (Divergent Change, Shotgun Surgery, Parallel Inheritance Hierarchies); **Dispensables** (Comments, Duplicate Code, Lazy Class, Data Class, Dead Code, Speculative Generality); **Couplers** (Feature Envy, Inappropriate Intimacy, Message Chains, Middle Man, Incomplete Library Class) |
| **Technique categories** | Composing Methods, Moving Features Between Objects, Organizing Data, Simplifying Conditional Expressions, Simplifying Method Calls, Dealing with Generalization |
| **Where used** | `refactor/SKILL.md`: expanded smell table with all 5 categories. `apply-patterns/SKILL.md`: cross-reference for GoF pattern selection. |

---

## Bibliography

1. Bay, J. (~2005). "Object Calisthenics." *IEEE Software/DevX*. https://www.bennadel.com/resources/uploads/2012/objectcalisthenics.pdf
2. Fowler, M. (1999/2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.). Addison-Wesley. https://martinfowler.com/books/refactoring.html
3. Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1995). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.
4. Martin, R. C. (2000). "Principles of OOD." *ButUncleBob.com*. https://blog.interface-solv.com/wp-content/uploads/2020/07/Principles-Of-OOD.pdf
5. Shvets, A. (2014–present). *Refactoring.Guru*. https://refactoring.guru
