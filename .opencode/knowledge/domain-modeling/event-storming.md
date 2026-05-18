---
domain: domain-modeling
tags: [ddd, event-storming, domain-events, commands, aggregates, brandolini]
last-updated: 2026-05-08
---

# Event Storming

## Key Takeaways

- Event storming is a structured brainstorming technique with six phases: chaotic exploration, timeline enforcement, hotspot identification, external system mapping, command mapping, and candidate grouping (Brandolini, 2012).
- Domain events are facts expressed in past tense (OrderPlaced, FillDetected). Extract from interview transcripts by scanning for business-relevant state changes and outcome statements.
- Commands are intents in imperative (PlaceOrder, DetectFill). Each command has an actor, preconditions, and produces zero or more events. Read models are the decision information needed before executing a command.
- Hotspots mark conflicts, ambiguities, or disagreements. They are not resolved during event storming — they are flagged for stakeholder follow-up and indicate context boundary candidates.
- Candidate bounded contexts emerge from clustering related events. Candidate aggregates emerge from grouping events that must be transactionally consistent. Formalization converts these candidates into entity tables, aggregate boundaries, and context maps.

## Concepts

**Event Storming Phases** (Brandolini, 2012): The workshop proceeds through six phases of increasing structure. Chaotic exploration: brainstorm all domain events without ordering. Timeline enforcement: place events chronologically, adding missing events exposed by gaps. Hotspot identification: mark conflicts, ambiguities, and areas where stakeholders disagree. External systems: identify actors and systems outside the domain. Command mapping: for each event, identify the triggering command and the read model needed. Candidate grouping: cluster into aggregate and bounded context hypotheses.

**Domain Event Extraction**: Events represent business-relevant state changes that have already occurred. Extract from interview transcripts by scanning for: outcome statements ("the order was filled"), state transitions ("the position changed from flat to long"), and time markers ("after the tick completes"). Each event gets a past-tense name in SubjectVerbEd format: OrderPlaced, FillDetected, SpreadCalculated. Events are facts — they cannot be undone, only compensated by subsequent events.

**Commands and Read Models**: A command is an intent to change state, expressed in imperative (PlaceOrder, CancelOrder, DetectFill). Each command has: an actor (who or what triggers it), preconditions (what must be true), and produces zero or more events on success or rejection events on failure. A read model is the information needed to decide whether and how to execute a command. For PlaceOrder, the read model includes current orderbook, balances, and open orders.

**Hotspots**: Hotspots are marked when stakeholders disagree about an event's meaning, when two events seem contradictory, or when the same term is used for different concepts. Hotspots are NOT resolved during event storming — they are recorded as boundary candidates and deferred to stakeholder follow-up. The number and location of hotspots reveals where the domain is most complex.

**Candidate Grouping**: After all events and commands are identified, group them into hypotheses: aggregates (events/commands that must be transactionally consistent) and bounded contexts (clusters sharing a ubiquitous language). This is hypothesis, not final — the domain-discovery step formalizes these candidates.

## Content

### Formalization

Event storming produces candidates. Formalization converts candidates into structural specification artifacts.

**Entity vs Value Object**: An entity has identity persisting across state changes (a Slot is the same Slot regardless of state). A value object has no identity — defined entirely by attribute values (PriceLevel at price=100, qty=5 equals any other with same values). Only entities can be aggregate roots. Value objects are always owned by an entity.

**Relationship Extraction**: Relationships derive from: event flow (entity A produces an event entity B consumes), data flow (entity A composed from entity B's data), and domain constraints (a rule involves both entities). Three types: composition, dependency, domain flow. Cardinality constrains design: 1:1 enables direct reference, 1:N enables collection, M:N requires indirection.

**Formalization Steps**:

1. List entity candidates from events and commands. Each event's subject is an entity candidate. Each command's target is an entity candidate. Deduplicate across events.
2. Classify each candidate: entity if it has identity and lifecycle; value object if defined by attributes and immutable.
3. Determine relationships: composition (A contains B), dependency (A uses B), or domain flow (A produces output for B). Cardinality: 1:1, 1:N, M:N.
4. Define aggregate boundaries: group entities sharing invariants. Document root entity, invariants, and business reason for grouping.
5. Identify context boundaries: group aggregates sharing a ubiquitous language. Document name, responsibility, key entities, capability, why separate, integration points.
6. Map context relationships per [[domain-modeling/context-mapping#key-takeaways]].

**Entity Table Format**:

| Field | Purpose |
|---|---|
| Name | PascalCase entity name |
| Type | Entity or Value Object |
| Description | What it represents |
| Bounded Context | Owning context |
| Aggregate Root? | Yes if root, — if value object |

**Aggregate Boundary Table Format**:

| Field | Purpose |
|---|---|
| Aggregate | PascalCase name |
| Root Entity | Identity root |
| Invariants | Business rules enforced |
| Why Grouped | Business reason for boundary |
| Bounded Context | Owning context |

**Boundary Decision Heuristics**:

- If an invariant references two entities, they share an aggregate
- If an aggregate exceeds memory, split and accept eventual consistency
- If two contexts use the same term with different definitions, they are separate contexts
- If removing one aggregate doesn't change term meanings in another, they are separate contexts
- If a rule can be checked eventually (not immediately), entities may be in different aggregates

### Phase 1: Chaotic Exploration

Goal: surface ALL domain events without judgment or ordering.

Extraction heuristics — scan interview transcripts for:
- Outcome verbs: "placed", "filled", "cancelled", "detected", "calculated", "exceeded"
- State transitions: "changed to", "moved from", "became"
- Business milestones: "completed", "started", "halted", "resumed"
- Exclude technical events (database writes, API calls) — focus on business events
- Include negative/rejection events: OrderRejected, InsufficientFunds

Naming convention: SubjectVerbEd in PascalCase. Examples: OrderPlaced, FillDetected, PositionOpened, KillSwitchActivated.

### Phase 2: Timeline Enforcement

Goal: place events in chronological order, which reveals gaps.

1. Arrange events left-to-right on a timeline
2. For each adjacent pair, ask: "What must happen between these two?"
3. Insert any missing events exposed by gaps
4. Identify parallel events (events that happen simultaneously in different contexts)

### Phase 3: Hotspot Identification

Goal: mark conflicts and ambiguities for follow-up.

Mark a hotspot when:
- Stakeholders use the same word for different concepts
- The timeline has contradictory events
- A decision has multiple valid outcomes
- An event's trigger is unclear or contested
- A domain rule is inconsistent across interviews

Record each hotspot as: `[event/term] — [nature of conflict] — [stakeholders who disagree]`.

### Phase 4: External Systems and Actors

Goal: identify what triggers events from outside the domain.

For each event without an internal trigger:
- Identify the external actor (user, exchange API, timer, external system)
- Note whether the actor is a source (provides data) or a trigger (initiates action)

### Phase 5: Command Mapping

Goal: for each event, identify the command and read model.

For each event, determine:
- **Command**: What intent produces this event? (PlaceOrder → OrderPlaced)
- **Actor**: Who/what issues the command?
- **Read model**: What information does the actor need to decide?
- **Preconditions**: What must be true for success?
- **Rejection event**: What happens on failure? (PlaceOrderRejected)

Edge cases:
- An event with no command is externally triggered
- A command may produce multiple events
- A command may produce no events if rejected

### Phase 6: Aggregate and Context Candidates

Goal: cluster into transactional boundaries and linguistic boundaries.

**Aggregate candidates**: Group commands that must execute atomically. If two commands must always succeed or fail together, they belong to the same aggregate. If they can execute independently, they are separate aggregates.

**Context candidates**: Group aggregates sharing a ubiquitous language. If the same term means different things in two groups, they are separate contexts. If removing one aggregate changes the meaning of terms in another, they are in the same context.

Record as: `Candidate Aggregate: [name] — [events] — [commands] — [consistency reason]` and `Candidate Context: [name] — [aggregates] — [shared terms]`.

## Related

- [[domain-modeling/context-mapping]]
- [[requirements/ubiquitous-language]]
- [[requirements/interview-techniques]]
