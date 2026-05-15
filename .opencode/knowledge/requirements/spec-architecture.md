---
domain: requirements
tags: [spec-architecture, single-source-of-truth, progressive-refinement, terminology]
last-updated: 2026-05-15
---

# Specification Architecture

## Key Takeaways

- Behavioral rules live in `.feature` files as the single source of truth. Domain spec (`domain_spec.md`) is structural only. Simulation results (`simulation_results.md`) is pain point tracking only.
- One .feature file per bounded context during simulation, refined into shippable features during planning. No rule exists in more than one file.
- The .feature file is progressively refined: simulation writes Rule blocks → feature-discovery renames/redistributes → feature-breakdown adds behavior hints → feature-examples writes Gherkin.
- Standardized terminology: walkthrough (simulation path), discovered rule (simulation finding), Rule block (Gherkin Rule:), behavior hint (pre-Gherkin outcome), Example block (Gherkin Example:).
- Spec documents are read-only during development. Issues are flagged, not fixed directly.

## Concepts

**Single Source of Truth**: Each behavioral requirement (Rule) lives in exactly one `.feature` file. The domain spec references `.feature` rules as derived summaries — not as authoritative copies. Pain points live in `simulation_results.md`. No triplicate storage.

**Progressive Refinement Chain**: A `.feature` file is never written in one pass. It accumulates content across states:

| State | Added | Removed |
|-------|-------|---------|
| `simulate-spec` | `Feature:` title + description, `Rule:` title + behavioral description | — |
| `feature-discovery` | Updated `Feature:` title + description (if split/renamed), `# Constraints:` comments | — |
| `feature-breakdown` | `Behavior hints:` under each Rule | — |
| `feature-examples` | `Example:` / `Scenario Outline:` blocks | `Behavior hints:` section |

**Artifact Purposes**:

| Artifact | Contains | Does NOT contain |
|----------|----------|-----------------|
| `domain_spec.md` | Entities, aggregates, data shapes, integration points, external contracts, context map. Derived summaries of state machines, error handling, invariants referencing .feature rules. | Behavioral rules as primary source. Given/When/Then. |
| `simulation_results.md` | Walkthroughs performed (with Discovered Rule column), I/O evidence references, pain points, resolution status, PASS/FAIL. | Rules Discovered. E2E Test Candidates. |
| `<feature>.feature` | `Feature:` title + description, `Rule:` blocks, `# Constraints:`, `Example:`/`Scenario Outline:` blocks. | Structural domain model. Pain points. State machines. |

**Feature Boundary Discovery**: Simulation creates one `.feature` per bounded context. During planning, `feature-discovery` splits/renames coarse `.feature` files into shippable features using the delivery order from `product_definition.md` validated against the context map. Rule blocks are redistributed but content is never edited — only the SA (simulation) and reviewer (fix-spec) may change Rule descriptions.

## Content

### Artifact Dependency Graph

```
discovery-flow
  domain_spec.md ──────────────────────────────────────────┐
  product_definition.md ───────────────┐                   │
  glossary.md ─────────────────────────┤                   │
                                       │                   │
spec-validation-flow                   │                   │
  domain_spec.md ◄─────────────────────┤ (structural only) │
  product_definition.md ◄──────────────┤                   │
  glossary.md ◄────────────────────────┤                   │
  features/<context>.feature ──────────┤ (Rule blocks)     │
  simulation_results.md ───────────────┤ (pain points)     │
                                       │                   │
planning-flow                          │                   │
  features/<context>.feature ◄─────────┤ (coarse input)    │
  domain_spec.md ◄─────────────────────┘                   │
  product_definition.md ◄──────────────┘
  ↓
  features/<feature_id>.feature (refined: splits, behavior hints, Gherkin)
```

### Terminology Map

| Project Term | Gherkin Equivalent | Old (Deprecated) |
|-------------|-------------------|-----------------|
| walkthrough | — | scenario, simulation scenario |
| discovered rule | — | business rule, coarse rule |
| Rule / Rule block | `Rule:` | story, user story |
| behavior hint | — | `Scenarios:`, `# Business rules:` |
| Example block | `Example:` | BDD scenario, acceptance test |
| Scenario Outline block | `Scenario Outline:` | (unchanged — Gherkin keyword) |
| pain point | — | (unchanged) |

### Rule Lifecycle

```
simulate-spec        feature-discovery       feature-breakdown      feature-examples
    │                      │                       │                      │
    ▼                      ▼                       ▼                      ▼
Rule: <title>         Rule: <title>           Rule: <title>          Rule: <title>
  description           description             description            description
  [written by SA]       [moved between          Behavior hints:        Example: <title>
                        files if split]          - x → y               Given/When/Then
                      # Constraints:             - a → b               Example: <title>
                      # - <threshold>           [added by PO]          Given/When/Then
                      [added by PO]                                   [hints removed]
```

### Constraint Lifecycle

Constraints in `# Constraints:` comment blocks come from two sources:

- **Quality attributes** from `product_definition.md` — mapped to features by `feature-discovery` (e.g. latency, reliability, security thresholds).
- **Technology requirements** from `domain_spec.md` Technology Requirements table — written by `simulate-spec` during spec validation (e.g. DSPy typed signatures, PostgreSQL persistence, gRPC service layer).

**Writer**: Quality attribute constraints → `feature-discovery` (PO). Technology constraints → `simulate-spec` (SA).
**Format**: `# Constraints:` comment block with `# - <constraint>` bullets. Each constraint carries a verifiable claim.
**Enforcement**: `review-gate` Tier 1 verifies constraints by executing the domain_spec.md Verification instruction. `accept-feature` traces technology Q&As to constraint evidence. Constraints are never converted to Examples.

### Cleanup Gates

| State | Gate |
|-------|------|
| `feature-discovery` | Coarse `.feature` files from simulation that were split: original files deleted or archived. No orphaned `.feature` files remain. |
| `feature-examples` | No `Behavior hints:` text remains in the `.feature` file. All hints converted to Gherkin. |
| `spec-review` | `# Constraints:` present for every quality attribute mapped to this feature. |

## Related

- [[requirements/gherkin]]: Gherkin specification format and conventions
- [[requirements/spec-simulation]]: spec simulation walkthrough procedure
- [[requirements/rule-derivation]]: rule sources and distribution
- [[requirements/feature-discovery]]: feature boundary identification
- [[requirements/feature-boundaries]]: deriving feature boundaries
- [[requirements/invest]]: INVEST criteria for Rule blocks
