---
domain: requirements
tags: [discovery, interview, elicitation, gap-finding]
last-updated: 2026-04-26
---

# Discovery Techniques

## Key Takeaways

- Use Critical Incident Technique (CIT) to ask about specific past events rather than general descriptions; concrete incidents force actual memory and surface edge cases.
- Use Laddering to climb from surface features to underlying consequences and terminal values; stop when the answer produces a design constraint.
- Use CI Perspective Change to ask stakeholders to describe the same situation from another actor's viewpoint; peripheral details and cross-role concerns surface.
- Apply three levels of active listening: per answer (paraphrase), per group (synthesis), end of session (full synthesis for approval).
- Use silent pre-mortem before writing any design or stub: ask "In 6 months this design is a mess — what mistakes did we make?" to surface hidden risks early.

## Concepts

**Critical Incident Technique (CIT)**: Ask about a specific past event rather than a general description. Schema-based recall ("usually we...") hides edge cases and workarounds. A concrete incident forces actual memory. Probe each incident with "What task were you doing? What happened next? What made it effective/ineffective?"

**Laddering / Means-End Chain**: Climb from surface feature to underlying consequence to terminal value. The first answer is rarely the real constraint. Keep asking "Why is that important?", "What does that enable?", "What would break if that were not available?" Stop when the stakeholder reaches a value they cannot explain further. In architecture context, stop when the answer produces a design constraint writable into an ADR.

**CI Perspective Change**: Ask the stakeholder to describe the same situation from another actor's point of view. Peripheral details and cross-role concerns surface that the primary perspective conceals. Ask "What do you think the end user experiences?", "What would your team lead's concern be?", "From the perspective of someone encountering this for the first time, what would they need to know?"

**Active Listening Protocol**: Three levels apply throughout every interview session. Level 1 (per answer): immediately paraphrase each answer. Level 2 (per group): brief synthesis when transitioning between behaviour groups. Level 3 (end of session): full synthesis for stakeholder approval. Do not introduce topic labels or categories during active listening.

**Silent Pre-mortem**: Before writing any design or stub, ask "In 6 months this design is a mess. What mistakes did we make?" For each candidate class, check for >2 instance variables (split) or >1 reason to change (isolate). For each external dependency, check if it is behind a Protocol. For each noun, check if it serves double duty across modules (isolate). This technique surfaces hidden risks before they become architectural problems.

## Content

### Critical Incident Technique (CIT) — Flanagan 1954

Ask about a specific past event rather than a general description. Schema-based recall ("usually we...") hides edge cases and workarounds. A concrete incident forces actual memory.

- "Tell me about a specific time when [X] worked exactly as you needed."
- "Tell me about a specific time when [X] broke down or frustrated you."
- Probe each incident: "What task were you doing? What happened next? What made it effective / ineffective?"

In architecture context: "If this entity is misused, what breaks?" and "Tell me about a concrete case where this boundary would be crossed."

### Laddering / Means-End Chain — Reynolds & Gutman 1988

Climb from surface feature to underlying consequence to terminal value. The first answer is rarely the real constraint.

- "Why is that important to you?"
- "What does that enable?"
- "What would break if that were not available?"
- Stop when the stakeholder reaches a value they cannot explain further.

In architecture context: "Why does this need to be immutable?" and "What breaks if this is not behind a Protocol?" Stop when the answer produces a design constraint that can be written into an ADR.

### CI Perspective Change — Fisher & Geiselman 1987

Ask the stakeholder to describe the same situation from another actor's point of view. Peripheral details and cross-role concerns surface that the primary perspective conceals.

- "What do you think the end user experiences in that situation?"
- "What would your team lead's concern be here?"
- "From the perspective of someone encountering this for the first time, what would they need to know?"

### Active Listening Protocol

Three levels of active listening apply throughout every interview session:

- **Level 1 — Per answer**: immediately paraphrase each answer before moving to the next question. "So if I understand correctly, you're saying that X happens when Y?" Catches misunderstanding in the moment.
- **Level 2 — Per group**: brief synthesis when transitioning between behaviour groups. "We've covered [area A] and [area B]. Before I ask about [area C], here is what I understood so far: [summary]. Does that capture it?" Confirms completeness, gives stakeholder a recovery point.
- **Level 3 — End of session**: full synthesis of everything discussed. Present to stakeholder for approval. This is the accuracy gate and the input to domain modelling.

Do not introduce topic labels or categories during active listening. The summary must reflect what the stakeholder said, not new framing that prompts reactions to things they haven't considered.

### Silent Pre-mortem (Architecture)

Before writing any design or stub:

> "In 6 months this design is a mess. What mistakes did we make?"

For each candidate class:
- >2 ivars? → split
- >1 reason to change? → isolate

For each external dependency:
- Is it behind a Protocol? → if not, add

For each noun:
- Serving double duty across modules? → isolate

## Related

- [[requirements/invest-moscow]] — story quality criteria applied after discovery
- [[requirements/gherkin]] — writing specifications from discovered requirements
- [[architecture/smell-check]] — design smell detection during architecture