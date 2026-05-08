---
domain: requirements
tags: [rule-derivation, business-rules, invariants, events, commands]
last-updated: 2026-05-08
---

# Rule Derivation

## Key Takeaways

- Business rules are derived from three systematic sources: domain events (behavioral rules), aggregate invariants (structural rules), and commands (action rules). Every rule traces back to at least one domain model artifact.
- Event → Rule pattern: "When [event], then [consequence]." Each domain event in the domain model implies at least one behavioral rule about what must happen when that event occurs.
- Invariant → Rule pattern: "[Entity] must always [condition]." Each aggregate invariant in the domain model IS a business rule; record it as-is.
- Command → Rule pattern: "[Actor] can [action] when [precondition]." Each command implies what actors can do and under what conditions.
- Quality attributes from product_definition.md constrain rules: each attribute produces at least one Constraint that bounds the feature's behavior with a measurable threshold.

## Concepts

**Three Sources of Rules**: Business rules are not invented — they are derived from the domain model. Domain events produce behavioral rules (what happens when). Aggregate invariants produce structural rules (what must always be true). Commands produce action rules (who can do what, when). Cross-referencing all three sources ensures comprehensive coverage; missing rules indicate either a gap in the domain model or an implicit assumption that must be made explicit.

**Event → Rule Derivation**: Each domain event (past-tense: OrderPlaced, FillDetected, KillSwitchActivated) implies rules about what must happen when that event occurs. The rule answers: what triggered this event? What must be true afterward? What must not happen? Example: "When a fill is detected, the tracked order must be updated before the next detection cycle."

**Invariant → Rule Derivation**: Each aggregate invariant from the domain model's aggregate boundary table IS a business rule. Record it verbatim as a rule bullet, then refine into active voice during breakdown. Example invariant: "A tracked order must be atomically removed when cancelled or fully filled." This becomes a rule directly.

**Command → Rule Derivation**: Each command (imperative: PlaceOrder, CancelOrder) implies rules about who can act and under what conditions. The rule answers: who can issue this command? What preconditions must hold? What happens on success? What happens on rejection? Example: "An operator can place a limit order when the spread exceeds the fee floor."

**Quality Attribute → Constraint Mapping**: Each quality attribute in product_definition.md (latency, reliability, safety) constrains feature behavior. Map each attribute to the feature(s) responsible for enforcing it. If no feature enforces a quality attribute, it is a gap. Constraints include measurable thresholds: "Latency: tick-to-order under 100ms", "Reliability: no orphaned orders after crash", "Safety: kill switch halts all trading within 1 tick."

**Traceability Matrix**: Every rule must trace back to at least one domain model artifact (event, invariant, or command). Every domain event, invariant, and command must trace forward to at least one rule. Gaps in either direction indicate missing rules or incomplete domain modeling.

## Content

### Derivation Procedure

For each feature, starting with the feature that has the most entities from the domain model:

**Step 1: Assign domain model artifacts to features.** Using the bounded context column in the domain model's entity table, assign each entity to the feature that corresponds to its context. Assign each aggregate invariant to the feature that contains the aggregate root. Assign each domain event and command to the feature corresponding to its bounded context.

**Step 2: Derive behavioral rules from events.** For each event assigned to this feature:
- What triggers this event? → Rule about precondition
- What must happen after this event? → Rule about consequence
- What must NOT happen during/after this event? → Rule about prohibition
- Write each as a coarse bullet: "When [event], then [consequence]"

**Step 3: Derive structural rules from invariants.** For each invariant assigned to this feature:
- Record the invariant verbatim as a rule bullet
- These are non-negotiable: they define the consistency boundary
- Write as: "[Entity] must always [condition]"

**Step 4: Derive action rules from commands.** For each command assigned to this feature:
- Who can issue this command? → Rule about actor
- What preconditions must hold? → Rule about guard condition
- What happens on rejection? → Rule about failure handling
- Write as: "[Actor] can [action] when [precondition]"

**Step 5: Map quality attributes to constraints.** For each quality attribute in product_definition.md:
- Which feature(s) enforce this attribute? → Add Constraint to those features
- Include measurable threshold from the quality attribute
- If no feature enforces it → add to Questions table as a gap

### Traceability Verification

After deriving rules for all features, verify:

1. **Every event → at least one rule.** If an event has no rule, either the event is out of scope or a rule is missing.
2. **Every invariant → at least one rule.** If an invariant has no rule, add it.
3. **Every command → at least one rule.** If a command has no rule, either it's out of scope or a rule is missing.
4. **Every quality attribute → at least one constraint.** If a quality attribute has no enforcing feature, flag it as a gap.
5. **Every rule → at least one source artifact.** If a rule has no trace to events, invariants, or commands, it may be an assumption that needs validation.

### Example Derivation

From `FillDetected` event (Order Execution context):
- "When a fill is detected, the tracked order's filled quantity must be updated atomically"
- "When a fill is detected, the position must reflect the fill before the next tick"

From `TrackedOrder` aggregate invariant:
- "A tracked order must be atomically removed when cancelled or fully filled"
- "Fill detection must not produce duplicate Fill records"

From `PlaceOrder` command (Strategy → Order Execution):
- "An operator can place a limit order when the spread exceeds the fee floor"
- "A limit order must specify pair, side, price, and quantity"

From `Safety` quality attribute → Engine feature constraint:
- "Kill switch must halt all trading within 1 tick cycle"

## Related

- [[requirements/feature-discovery]]
- [[requirements/feature-boundaries]]
- [[domain-modeling/event-storming]]
- [[domain-modeling/domain-modeling]]