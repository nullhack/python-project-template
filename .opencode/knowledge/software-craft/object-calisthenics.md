---
domain: software-craft
tags: [object-calisthenics, oop, design, constraints]
last-updated: 2026-04-26
---

# Object Calisthenics

## Key Takeaways

- One indent level per method (OC-1); no `else` after `return` (OC-2) — flatten conditional logic with early returns.
- Wrap all primitives with domain meaning (OC-3); wrap collections with domain meaning (OC-4); one dot per line — no message chains (OC-5); no abbreviations (OC-6).
- Keep methods ≤20 lines and classes ≤50 lines (OC-7); ≤2 instance variables per behavioural class (OC-8); Tell, Don't Ask — no getters/setters, no external decision-making on another object's data (OC-9).
- Dataclasses, Pydantic models, value objects, and TypedDicts are exempt from OC-8 — they are data containers, not behavioural classes.

## Concepts

**OC-1 and OC-2 — Structure**: One indent level per method (OC-1) eliminates deep nesting. No `else` after `return` (OC-2) flattens conditional logic — each exit condition is an early return, the happy path stays at the left margin.

**OC-3 through OC-6 — Vocabulary**: Wrap all primitives with domain meaning (OC-3) — `UserId` instead of `int`. Wrap collections with domain meaning (OC-4) — `OrderCollection` instead of `list[Order]`. One dot per line, no message chains (OC-5) — `obj.repo.find(id).name` violates this. No abbreviations (OC-6) — every name must spell out its intent.

**OC-7, OC-8, OC-9 — Size and Encapsulation**: Keep methods ≤20 lines and classes ≤50 lines (OC-7). Limit behavioural classes to ≤2 instance variables (OC-8). Tell, Don't Ask (OC-9) — no getters/setters and no external decision-making on another object's data. Expose behaviour, not state. Tell objects what to do; don't ask them for their data and decide externally.

**OC-8 Exemption**: Dataclasses, Pydantic models, value objects, and TypedDicts are exempt from the two-instance-variable limit. These types exist to hold data, not to encapsulate behaviour. The constraint applies only to behavioural classes — classes whose purpose is to coordinate logic.

## Content

### OC-1 and OC-2 — Structure

| Rule | Constraint | Violation signal |
|---|---|---|
| OC-1 | One indent level per method | `for` inside `if` inside a method body |
| OC-2 | No `else` after `return` | `if cond: return x` then `else: return y` |

### OC-3 through OC-6 — Vocabulary

| Rule | Constraint | Violation signal |
|---|---|---|
| OC-3 | Wrap primitives with domain meaning | `def process(user_id: int)` instead of `UserId` |
| OC-4 | Wrap collections with domain meaning | `list[Order]` passed around instead of `OrderCollection` |
| OC-5 | One dot per line | `obj.repo.find(id).name` |
| OC-6 | No abbreviations | `usr`, `mgr`, `cfg`, `val`, `tmp` |

### OC-7, OC-8, OC-9 — Size and Encapsulation

| Rule | Constraint | Violation signal |
|---|---|---|
| OC-7 | Classes <= 50 lines, methods <= 20 lines | Any method requiring scrolling |
| OC-8 | <= 2 instance variables per class (behavioural classes only) | `__init__` with 3+ `self.x =` assignments in a behavioural class |
| OC-9 | Tell, Don't Ask — no getters/setters, no external decision-making on another object's data | `def get_name(self)` / `def set_name(self, v)` / `if obj.status == "active": obj.start()` (Ask pattern — decision made externally) |

### OC-8 Exemption

Dataclasses, Pydantic models, value objects, and TypedDicts are exempt from the two-instance-variable limit. These types exist to hold data, not to encapsulate behaviour. The constraint applies only to behavioural classes — classes whose purpose is to coordinate logic.

## Related

- [[software-craft/solid]] — SOLID principles overlap with OC-1 (SRP) and OC-5 (DIP)
- [[software-craft/smell-catalogue]] — OC violations are detectable as specific smells
- [[software-craft/self-declaration]] — OC items 12-20 in the declaration checklist
- [[software-craft/tdd]] — OC rules are checked during the REFACTOR phase