---
name: facilitate-event-storming
description: "Divergent exploration: extract domain events, commands, read models, and hotspot candidates from interview notes using Brandolini's event storming technique"
---

# Facilitate Event Storming

Available knowledge: [[domain-modeling/event-storming]]. `in` artifacts: read all before starting work.

1. If `domain_model.md` already exists, read it — this is a cumulative artifact across iterations.
2. Read all interview notes from `in` artifacts.
3. Execute chaotic exploration per [[domain-modeling/event-storming#content]]: extract all domain events from interview data using extraction heuristics. Name each event in SubjectVerbEd PascalCase.
4. Enforce timeline: arrange events chronologically. For each gap, insert missing events exposed by the ordering.
5. Identify hotspots per [[domain-modeling/event-storming#content]]: mark conflicts, ambiguities, contradictions, and unclear triggers. Record each as `[event/term] — [conflict nature] — [source]`.
6. Map external systems: identify actors and systems outside the domain that trigger events.
7. Map commands per [[domain-modeling/event-storming#content]]: for each event, determine the command, actor, read model, preconditions, and rejection event.
8. Form candidate groupings per [[domain-modeling/event-storming#content]]: cluster into aggregate candidates (transactional consistency) and context candidates (linguistic boundary).
9. Write findings into `domain_model.md`: update or create the **summary** section with domain overview. Write the **Events and Commands** section with Domain Events and Commands tables per [[domain-modeling/event-storming#content]]. Add a **Changes** entry recording what was discovered.
