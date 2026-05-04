---
domain: requirements
tags: [discovery, interview, elicitation, gap-finding, CIT, laddering]
last-updated: 2026-04-29
---

# Interview Techniques

## Key Takeaways

- Use Critical Incident Technique (CIT — Flanagan, 1954) to ask about specific past events rather than general descriptions; concrete incidents force actual memory and surface edge cases.
- Use Laddering (Reynolds & Gutman, 1988) to climb from surface features to underlying consequences and terminal values; stop when the answer produces a design constraint.
- Use CI Perspective Change (Fisher & Geiselman, 1987) to ask stakeholders to describe the same situation from another actor's viewpoint; peripheral details and cross-role concerns surface.
- Apply three levels of active listening (Rogers & Farson, 1957): per answer (paraphrase), per group (synthesis), end of session (full synthesis for approval).
- Use the Funnel technique to order questions from broad to specific, preventing priming bias (Tversky & Kahneman, 1974) from early category labels.
- Discovery interviews follow a three-level funnel: General (big picture) → Cross-cutting (behaviour groups) → Feature identification (feature names and rough boundaries). Feature specification happens separately in planning.
- Feature specification interviews focus on one feature at a time, probing behavioral rules, edge cases (CIT), and real constraints (Laddering) to produce stories and scenarios.

## Concepts

**Critical Incident Technique (CIT — Flanagan, 1954)**: Ask about a specific past event rather than a general description. Schema-based recall ("usually we...") hides edge cases and workarounds (Christel & Kang, 1992). A concrete incident forces actual memory. Probe each incident with "What task were you doing? What happened next? What made it effective/ineffective?" In architecture context: "If this entity is misused, what breaks?" and "Tell me about a concrete case where this boundary would be crossed."

**Laddering / Means-End Chain**: Climb from surface feature to underlying consequence to terminal value. The first answer is rarely the real constraint. Keep asking "Why is that important?", "What does that enable?", "What would break if that were not available?" Stop when the stakeholder reaches a value they cannot explain further. In architecture context, stop when the answer produces a design constraint writable into an ADR.

**CI Perspective Change**: Ask the stakeholder to describe the same situation from another actor's point of view. Peripheral details and cross-role concerns surface that the primary perspective conceals. Ask "What do you think the end user experiences?", "What would your team lead's concern be?", "From the perspective of someone encountering this for the first time, what would they need to know?"

**Active Listening Protocol**: Three levels apply throughout every interview session. Level 1 (per answer): immediately paraphrase each answer before moving to the next question. Level 2 (per group): brief synthesis when transitioning between behaviour groups. Level 3 (end of session): full synthesis of everything discussed, presented for stakeholder approval. Do not introduce topic labels or categories during active listening — the summary must reflect what the stakeholder said.

**Funnel Technique**: Start with broad open-ended questions before narrowing to specifics. Priming bias (Tversky & Kahneman, 1974) is structural: any category name the interviewer introduces activates a schema that filters what the interviewee considers worth reporting. The funnel sequences questions so the interviewee's own categories emerge first.

**Discovery Interview Structure**: Discovery interviews follow a three-level funnel aligned with the Funnel technique. Level 1 — General: seven standard questions (Who, What, Why, When/Where, Success, Failure, Out-of-scope) establish the big picture. Level 2 — Cross-cutting: behaviour groups, bounded contexts, integration points, and lifecycle events structure the domain. Level 3 — Feature identification: feature names and rough boundaries are identified; detailed feature specification (stories, criteria) happens later during planning interviews, not here. The purpose of the discovery interview is to understand the domain and identify what features exist, not to specify each feature in detail.

**Feature Specification via Story Mapping**: Coarse story discovery happens during the discovery-flow's `feature-discovery` state using story mapping (Patton, 2014). The story mapping workshop IS the collaborative specification — it produces coarse Rules (Business) bullet points for all features in one pass. During planning-flow's `feature-breakdown` state, the PO refines coarse Rules into full Rule blocks. Targeted clarification questions may use CIT ("Tell me about a time when [feature behavior] went wrong") and laddering ("Why is that important?") when a Rule needs more detail, but this is lightweight — not a separate full interview session.

## Content

### Critical Incident Technique (CIT) — Flanagan 1954

Ask about a specific past event rather than a general description. Schema-based recall ("usually we...") hides edge cases and workarounds. A concrete incident forces actual memory.

- "Tell me about a specific time when [X] worked exactly as you needed."
- "Tell me about a specific time when [X] broke down or frustrated you."
- Probe each incident: "What task were you doing? What happened next? What made it effective / ineffective?"

Architecture context: "If this entity is misused, what breaks?" and "Tell me about a concrete case where this boundary would be crossed."

### Laddering / Means-End Chain — Reynolds & Gutman 1988

Climb from surface feature to underlying consequence to terminal value. The first answer is rarely the real constraint.

- "Why is that important to you?"
- "What does that enable?"
- "What would break if that were not available?"
- Stop when the stakeholder reaches a value they cannot explain further.

Architecture context: "Why does this need to be immutable?" and "What breaks if this is not behind a Protocol?" Stop when the answer produces a design constraint that can be written into an ADR.

### CI Perspective Change — Fisher & Geiselman 1987

Ask the stakeholder to describe the same situation from another actor's point of view. Peripheral details and cross-role concerns surface that the primary perspective conceals. The enhanced Cognitive Interview elicits approximately 35% more correct information than standard interviews with equal accuracy rates.

- "What do you think the end user experiences in that situation?"
- "What would your team lead's concern be here?"
- "From the perspective of someone encountering this for the first time, what would they need to know?"

### Active Listening Protocol — Rogers & Farson, 1957

Three levels of active listening apply throughout every interview session:

- **Level 1 — Per answer**: immediately paraphrase each answer before moving to the next question. "So if I understand correctly, you're saying that X happens when Y?" Catches misunderstanding in the moment.
- **Level 2 — Per group**: brief synthesis when transitioning between behaviour groups. "We've covered [area A] and [area B]. Before I ask about [area C], here is what I understood so far: [summary]. Does that capture it?" Confirms completeness, gives stakeholder a recovery point.
- **Level 3 — End of session**: full synthesis of everything discussed. Present to stakeholder for approval. This is the accuracy gate and the input to domain modelling.

Do not introduce topic labels or categories during active listening. The summary must reflect what the stakeholder said, not new framing that prompts reactions to things they haven't considered.

### Funnel Technique — Question Ordering to Prevent Priming (Tversky & Kahneman, 1974)

Start with broad open-ended questions before narrowing to specifics. Priming bias is structural: any category name the interviewer introduces activates a schema that filters what the interviewee considers worth reporting. The funnel sequences questions so the interviewee's own categories emerge first.

The standard seven general questions (Who, What, Why, When/Where, Success, Failure, Out-of-scope) are an application of the Funnel technique combined with the Kipling Method (5W1H).

## Related

- [[requirements/pre-mortem]] — prospective hindsight technique applied at specification and design stages
- [[requirements/invest]] — story quality criteria applied after discovery
- [[requirements/gherkin]] — writing specifications from discovered requirements