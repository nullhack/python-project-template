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
2. **Find the smell category** (Creational / Structural / Behavioral) in [[software-craft/design-patterns]]
3. **Read the trigger and the before/after example** in [[software-craft/design-patterns]]
4. **Apply the pattern** — update the stub files (Step 2) or the refactored code (Step 3)

---

See [[software-craft/design-patterns]] for the full pattern catalogue, smell-triggered patterns, and quick lookup table.

---

## Core Heuristic — Procedural vs OOP

> **When procedural code requires modifying existing functions to add new variants, OOP is the fix.**

Procedural code is open to inspection but open to modification too — every new case touches existing logic.
OOP (via Strategy, State, Observer, etc.) closes existing code to modification and opens it to extension through new types.
The smell is always the same: **a place in the codebase that must change every time the domain grows.**