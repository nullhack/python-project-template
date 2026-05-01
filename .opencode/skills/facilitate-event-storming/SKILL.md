---
name: facilitate-event-storming
description: "Facilitate an event storming workshop to surface domain events, commands, and aggregate candidates"
---

# Facilitate Event Storming

Load [[domain-modeling/event-storming#key-takeaways]] before starting. 

1. Identify domain events (past-tense verbs) from interview data per [[domain-modeling/event-storming#key-takeaways]].
2. Chronologically order events on a timeline.
3. Identify commands (imperative verbs) that trigger each event per [[domain-modeling/event-storming#key-takeaways]].
4. Group events and commands into candidate bounded contexts per [[domain-modeling/event-storming#key-takeaways]].
5. Identify aggregate candidates per [[domain-modeling/event-storming#key-takeaways]].
6. Write results to artifacts listed in the current state's `out` attrs. If findings affect artifacts outside the `out` contract, flag them in output notes for the appropriate step.
7. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.
