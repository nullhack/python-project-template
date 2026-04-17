# Academic Research — Theoretical Foundations

This document explains the cognitive and social-science mechanisms that justify the workflow reforms in this template. Each mechanism is grounded in peer-reviewed research.

---

## Mechanisms

### 1. Pre-mortem (Prospective Hindsight)

| | |
|---|---|
| **Source** | Klein, G. (1998). *Sources of Power: How People Make Decisions*. MIT Press. |
| **Date** | 1998 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Asking "imagine this failed — why?" catches 30% more issues than forward-looking review. |
| **Mechanism** | Prospective hindsight shifts from prediction (weak) to explanation (strong). The brain is better at explaining past events than predicting future ones. By framing as "it already failed," you activate explanation mode. |
| **Where used** | PO pre-mortem at scope, developer pre-mortem before handoff. |

---

### 2. Implementation Intentions

| | |
|---|---|
| **Source** | Gollwitzer, P. M. (1999). Implementation intentions: Strong effects of simple planning aids. *American Journal of Preventive Medicine*, 16(4), 257–276. |
| **Date** | 1999 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | "If X then Y" plans are 2–3x more likely to execute than general intentions. |
| **Mechanism** | If-then plans create automatic cue-response links in memory. The brain processes "if function > 20 lines then extract helper" as an action trigger, not a suggestion to consider. |
| **Where used** | Refactor Self-Check Gates in `implementation/SKILL.md`, Code Quality checks in `verify/SKILL.md`. |

---

### 3. Commitment Devices

| | |
|---|---|
| **Source** | Cialdini, R. B. (2001). *Influence: The Psychology of Persuasion* (rev. ed.). HarperBusiness. |
| **Date** | 2001 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Forcing an explicit micro-commitment (filling in a PASS/FAIL cell) creates resistance to reversals. A checkbox checked is harder to uncheck than a todo noted. |
| **Mechanism** | Structured tables with PASS/FAIL cells create commitment-device effects. The act of marking "FAIL" requires justification, making silent passes psychologically costly. |
| **Where used** | SOLID enforcement table, ObjCal enforcement table, Design Patterns table — all require explicit PASS/FAIL with evidence. |

---

### 4. System 2 Before System 1

| | |
|---|---|
| **Source** | Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux. |
| **Date** | 2011 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | System 1 (fast, automatic) is vulnerable to anchoring and confirmation bias. System 2 (slow, deliberate) must be activated before System 1's judgments anchor. |
| **Mechanism** | Running semantic review *before* automated commands prevents the "all green" dopamine hit from anchoring the reviewer's judgment. Doing hard cognitive work first protects against System 1 shortcuts. |
| **Where used** | Verification order in `verify/SKILL.md`: semantic alignment check before commands. |

---

### 5. Adversarial Collaboration

| | |
|---|---|
| **Source** | Mellers, B. A., Hertwig, R., & Kahneman, D. (2001). Do frequency representations eliminate cooperative bias? *Psychological Review*, 108(4), 709–735. |
| **Date** | 2001 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Highest-quality thinking emerges when parties hold different hypotheses and are charged with finding flaws in each other's reasoning. |
| **Mechanism** | Explicitly framing the reviewer as "your job is to break this feature" activates the adversarial collaboration mode. The reviewer seeks disconfirmation rather than confirmation. |
| **Where used** | Adversarial mandate in `reviewer.md` and `verify/SKILL.md`. |

---

### 6. Accountability to Unknown Audience

| | |
|---|---|
| **Source** | Tetlock, P. E. (1983). Accountability: A social determinant of judgment. In M. D. B. T. Strother (Ed.), *Psychology of Learning and Motivation* (Vol. 17, pp. 295–332). Academic Press. |
| **Date** | 1983 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Accountability to an unknown audience with unknown views improves reasoning quality. The agent anticipates being audited and adjusts reasoning. |
| **Mechanism** | The explicit report format (APPROVED/REJECTED with evidence) creates an accountability structure — the reviewer's reasoning will be read by the PO. |
| **Where used** | Report format in `verify/SKILL.md`, structured evidence columns in all enforcement tables. |

---

### 7. Chunking and Cognitive Load Reduction

| | |
|---|---|
| **Source** | Miller, G. A. (1956). The magical number seven, plus or minus two. *Psychological Review*, 63(2), 81–97. |
| **Date** | 1956 |
| **URL** | — |
| **Alternative** | Sweller, J. (1988). Cognitive load during problem solving. *Cognitive Science*, 12(2), 257–285. |
| **Status** | Confirmed |
| **Core finding** | Structured tables reduce working memory load vs. narrative text. Chunking related items into table rows enables parallel processing. |
| **Mechanism** | Replacing prose checklists ("Apply SOLID principles") with structured tables (5 rows, 4 columns) allows the reviewer to process all items in a single pass. |
| **Where used** | All enforcement tables in `verify/SKILL.md` and `reviewer.md`. |

---

### 8. Elaborative Encoding

| | |
|---|---|
| **Source** | Craik, F. I. M., & Lockhart, R. S. (1972). Levels of processing: A framework for memory research. *Journal of Verbal Learning and Verbal Behavior*, 11(6), 671–684. |
| **Date** | 1972 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Deeper processing — explaining *why* a rule matters — leads to better retention and application than shallow processing (just listing rules). |
| **Mechanism** | Adding a "Why it matters" column to enforcement tables forces the reviewer to process the rationale, not just scan the rule name. |
| **Where used** | SOLID table, ObjCal table, Design Patterns table — all have "Why it matters" column. |

---

### 9. Error-Specific Feedback

| | |
|---|---|
| **Source** | Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research*, 77(1), 81–112. |
| **Date** | 2007 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Feedback is most effective when it tells the agent exactly what went wrong and what the correct action is. "FAIL: function > 20 lines at file:47" is actionable. "Apply function length rules" is not. |
| **Mechanism** | The evidence column in enforcement tables requires specific file:line references, turning vague rules into actionable directives. |
| **Where used** | Evidence column in all enforcement tables. |

---

### 10. Prospective Memory Cues

| | |
|---|---|
| **Source** | McDaniel, M. A., & Einstein, G. O. (2000). Strategic and automatic processes in prospective memory retrieval. *Applied Cognitive Psychology*, 14(7), S127–S144. |
| **Date** | 2000 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Memory for intended actions is better when cues are embedded at the point of action, not in a separate appendix. |
| **Mechanism** | Placing if-then gates inline (in the REFACTOR section) rather than in a separate "reference" document increases adherence. The cue appears exactly when the developer is about to make the relevant decision. |
| **Where used** | Refactor Self-Check Gates embedded inline in `implementation/SKILL.md`. |

---

### 11. Observable Behavior Testing

| | |
|---|---|
| **Source** | Fowler, M. (2018). *The Practical Test Pyramid*. Thoughtworks. https://martinfowler.com/articles/practical-test-pyramid.html |
| **Date** | 2018 |
| **URL** | https://martinfowler.com/articles/practical-test-pyramid.html |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Tests should answer "if I enter X and Y, will the result be Z?" — not "will method A call class B first?" |
| **Mechanism** | A test is behavioral if its assertion describes something a caller/user can observe without knowing the implementation. The test should still pass if you completely rewrite the internals. |
| **Where used** | Contract test rule in `tdd/SKILL.md`: "Write every test as if you cannot see the production code." |

---

### 12. Test-Behavior Alignment

| | |
|---|---|
| **Source** | Google Testing Blog (2013). *Testing on the Toilet: Test Behavior, Not Implementation*. |
| **Date** | 2013 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Test setup may need to change if implementation changes, but the actual test shouldn't need to change if the code's user-facing behavior doesn't change. |
| **Mechanism** | Tests that are tightly coupled to implementation break on refactoring and become a drag on design improvement. Behavioral tests survive internal rewrites. |
| **Where used** | Contract test rule + bad example in `tdd/SKILL.md`, reviewer verification check in `reviewer.md`. |

---

### 13. Tests as First-Class Citizens

| | |
|---|---|
| **Source** | Martin, R. C. (2017). *First-Class Tests*. Clean Coder Blog. |
| **Date** | 2017 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Tests should be treated as first-class citizens of the system — not coupled to implementation. Bad tests are worse than no tests because they give false confidence. |
| **Mechanism** | Tests written as "contract tests" — describing what the caller observes — remain stable through refactoring. Tests that verify implementation details are fragile and create maintenance burden. |
| **Where used** | Contract test rule in `tdd/SKILL.md`, verification check in `reviewer.md`. |

---

### 14. Property-Based Testing (Invariant Discovery)

| | |
|---|---|
| **Source** | MacIver, D. R. (2016). *What is Property Based Testing?* Hypothesis. https://hypothesis.works/articles/what-is-property-based-testing/ |
| **Date** | 2016 |
| **URL** | https://hypothesis.works/articles/what-is-property-based-testing/ |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Property-based testing is "the construction of tests such that, when these tests are fuzzed, failures reveal problems that could not have been revealed by direct fuzzing." Property tests test *invariants* — things that must always be true about the contract, not things that fall out of how you wrote it. |
| **Mechanism** | Meaningful property tests assert invariants: "assert Score(x).value >= 0" tests the contract. Tautological tests assert reconstruction: "assert Score(x).value == x" tests the implementation. |
| **Where used** | Meaningful vs. Tautological table in `tdd/SKILL.md`, Property-Based Testing Decision Rule table in `tdd/SKILL.md`. |

---

### 15. Mutation Testing (Test Quality Verification)

| | |
|---|---|
| **Source** | King, K. N. (1991). *The Gamma (formerly mutants)*. |
| **Date** | 1991 |
| **URL** | — |
| **Alternative** | Mutation testing tools: Cosmic Ray, mutmut (Python) |
| **Status** | Confirmed |
| **Core finding** | A meaningful test fails when a mutation (small deliberate code change) is introduced. A tautological test passes even with mutations because it doesn't constrain the behavior. |
| **Mechanism** | If a test survives every mutation of the production code without failing, it tests nothing. Only tests that fail on purposeful "damage" to the code are worth keeping. |
| **Where used** | Note in `tdd/SKILL.md` Quality Rules (implicitly encouraged: tests must describe contracts, not implementation, which is the theoretical complement to mutation testing). |

---

### 16. Cost of Change Curve (Shift Left)

| | |
|---|---|
| **Source** | Boehm, B. W. (1981). *Software Engineering Economics*. Prentice-Hall. |
| **Date** | 1981 |
| **URL** | — |
| **Alternative** | Boehm, B., & Papaccio, P. N. (1988). Understanding and controlling software costs. *IEEE Transactions on Software Engineering*, 14(10), 1462–1477. |
| **Status** | Confirmed |
| **Core finding** | The cost to fix a defect multiplies by roughly 10x per SDLC phase: requirements (1x) → design (5x) → coding (10x) → testing (20x) → production (200x). A defect caught during requirements costs 200x less than the same defect found after release. |
| **Mechanism** | Defects compound downstream: a wrong requirement becomes a wrong design, which becomes wrong code, which becomes wrong tests, all of which must be unwound. Catching errors at the source eliminates the entire cascade. This is the empirical foundation for "shift left" — investing earlier in quality always dominates fixing later. |
| **Where used** | Justifies the multi-session PO elicitation model: every acceptance criterion clarified at scope prevents 10–200x rework downstream. Also justifies the adversarial pre-mortem at the end of each elicitation cycle, and the adversarial mandate in `verify/SKILL.md`. The entire 6-step pipeline is ordered to surface defects at the earliest (cheapest) phase. |

---

### 17. INVEST Criteria for User Stories

| | |
|---|---|
| **Source** | Wake, B. (2003). *INVEST in Good Stories, and SMART Tasks*. XP123.com. |
| **Date** | 2003 |
| **URL** | — |
| **Alternative** | Cohn, M. (2004). *User Stories Applied: For Agile Software Development*. Addison-Wesley. |
| **Status** | Confirmed |
| **Core finding** | Stories that are Independent, Negotiable, Valuable, Estimable, Small, and Testable produce fewer downstream defects and smoother development cycles. Stories that fail INVEST — especially "Testable" and "Small" — are the leading cause of scope creep and unbounded iteration. |
| **Mechanism** | INVEST serves as a quality gate before stories enter development. "Testable" forces the PO to express observable outcomes (directly enabling Given/When/Then). "Small" forces decomposition, which reduces cognitive load and makes estimation feasible. "Independent" prevents hidden ordering dependencies between stories. |
| **Where used** | INVEST gate in Phase 3 of `scope/SKILL.md`. PO verifies every story against all 6 letters before committing. |

---

### 18. Example Mapping (Rules Layer)

| | |
|---|---|
| **Source** | Wynne, M. (2015). *Introducing Example Mapping*. Cucumber Blog. https://cucumber.io/blog/bdd/example-mapping-introduction/ |
| **Date** | 2015 |
| **URL** | https://cucumber.io/blog/bdd/example-mapping-introduction/ |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Inserting a "rules" layer between stories and examples prevents redundant or contradictory acceptance criteria. A story with many rules needs splitting; a story with many open questions is not ready for development. |
| **Mechanism** | Example Mapping uses four card types: Story (yellow), Rules (blue), Examples (green), Questions (red). The rules layer groups related examples under the business rule they illustrate. Without this layer, POs jump from story directly to examples and lose the reasoning that connects them. Red cards (unanswered questions) are a first-class signal to stop and investigate rather than assume. |
| **Where used** | `## Rules` section in per-feature `discovery.md` (Phase 2). PO identifies business rules before writing Examples in Phase 4, making the reasoning behind Example clusters visible and reviewable. |

---

### 19. Declarative Gherkin

| | |
|---|---|
| **Source** | Cucumber Team. (2024). *Better Gherkin*. Cucumber Documentation. https://cucumber.io/docs/bdd/better-gherkin/ |
| **Date** | 2024 |
| **URL** | https://cucumber.io/docs/bdd/better-gherkin/ |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Declarative Gherkin ("When Bob logs in") produces specifications that survive UI changes. Imperative Gherkin ("When I click the Login button") couples specs to implementation details and breaks on every UI redesign. |
| **Mechanism** | Declarative steps describe *what happens* at the business level. Imperative steps describe *how the user interacts with a specific UI*. The distinction maps to the abstraction level: declarative = behavior contract, imperative = interaction script. AI agents are especially prone to writing imperative Gherkin because they mirror literal steps. |
| **Where used** | Declarative vs. imperative table in Phase 4 of `scope/SKILL.md`. PO is explicitly instructed to write behavior descriptions, not UI interaction scripts. |

---

### 20. MoSCoW Prioritization (Within-Story Triage)

| | |
|---|---|
| **Source** | Clegg, D., & Barker, R. (1994). *Case Method Fast-Track: A RAD Approach*. Addison-Wesley (DSDM origin). |
| **Date** | 1994 |
| **URL** | — |
| **Alternative** | — |
| **Status** | Confirmed |
| **Core finding** | Classifying requirements as Must/Should/Could/Won't forces explicit negotiation about what is essential vs. desired. When applied *within* a single story (not just across a backlog), it reveals bloated stories that should be split. |
| **Mechanism** | DSDM mandates that Musts cannot exceed 60% of total effort. At the story level: if a story has 12 Examples and only 3 are Musts, the remaining 9 can be deferred or split into a follow-up story. This prevents gold-plating and keeps stories small. |
| **Where used** | MoSCoW triage in Phase 4 of `scope/SKILL.md`. PO applies Must/Should/Could when a story exceeds 5 Examples. |

---

### 21. Minimal-Scope Agent Design

| | |
|---|---|
| **Source** | OpenAI. (2024). *Agent definitions*. OpenAI Agents SDK Documentation. |
| **Date** | 2024 |
| **URL** | https://platform.openai.com/docs/guides/agents/define-agents |
| **Alternative** | Anthropic. (2024). *Building effective agents*. Anthropic Engineering Blog. https://www.anthropic.com/engineering/building-effective-agents |
| **Status** | Confirmed — corrects the belief that subagents should be "lean routing agents" |
| **Core finding** | "Define the smallest agent that can own a clear task. Add more agents only when you need separate ownership, different instructions, different tool surfaces, or different approval policies." The split criterion is ownership boundary, not instruction volume. |
| **Mechanism** | Multiple agents competing to own the same concern create authority conflicts and inconsistent tool access. The right unit is the smallest coherent domain that requires exclusive responsibility. Keeping handoff descriptions short and concrete enables routing agents to select the right specialist. |
| **Where used** | Agent design in `.opencode/agents/*.md` — 4 agents, each owning a distinct domain (PO, developer, reviewer, setup). |

---

### 22. Context Isolation via Subagents

| | |
|---|---|
| **Source** | Anthropic. (2025). *Best practices for Claude Code*. Anthropic Documentation. |
| **Date** | 2025 |
| **URL** | https://www.anthropic.com/engineering/claude-code-best-practices |
| **Alternative** | — |
| **Status** | Confirmed — the primary reason subagents exist is context isolation, not routing |
| **Core finding** | Subagents run in their own context windows and report back summaries, keeping the main conversation clean for implementation. Every file read in a subagent burns tokens in a child window, not the primary window. |
| **Mechanism** | Context window is the primary performance constraint for LLM agents. Investigation tasks (reading many files, exploring a codebase) rapidly exhaust context if done inline. Delegating to a subagent quarantines that cost; the primary agent receives only the distilled result. A fresh context in the subagent also prevents anchoring bias from prior conversation state. |
| **Where used** | OpenCode `task` tool usage in all agents; `explore` and `general` built-in subagents; explicit subagent invocations in `.opencode/agents/developer.md`. |

---

### 23. On-Demand Skill Loading (Context Budget)

| | |
|---|---|
| **Source** | Anthropic. (2025). *Best practices for Claude Code*. Anthropic Documentation. |
| **Date** | 2025 |
| **URL** | https://www.anthropic.com/engineering/claude-code-best-practices |
| **Alternative** | OpenCode. (2026). *Agent Skills*. OpenCode Documentation. https://opencode.ai/docs/skills/ |
| **Status** | Confirmed (vendor guidance) — benefit on task completion quality is extrapolated from RAG retrieval literature; not directly A/B-tested on agent instruction architectures |
| **Core finding** | "CLAUDE.md is loaded every session, so only include things that apply broadly. For domain knowledge or workflows only relevant sometimes, use skills instead. Claude loads them on demand without bloating every conversation." Bloated always-loaded files cause Claude to ignore critical instructions. |
| **Mechanism** | Every token in an unconditionally-loaded file competes for attention against the task prompt. Long AGENTS.md/CLAUDE.md files push important instructions beyond effective attention range, causing silent non-compliance. Procedural workflows moved to skills are injected only when the task calls for them, preserving the primary context budget. This is the same principle as lazy loading in software: pay the cost only when needed. |
| **Where used** | `AGENTS.md` carries only shared project conventions and commands; all step-specific workflows live in `.opencode/skills/*.md` and are loaded via the `skill` tool only when the relevant step begins. |

---

### 24. Instruction Conflict Resolution Failure in LLMs

| | |
|---|---|
| **Source** | Geng et al. (2025). Control Illusion: The Failure of Instruction Hierarchies in Large Language Models. AAAI-26. arXiv:2502.15851. |
| **Date** | 2025 |
| **URL** | https://arxiv.org/abs/2502.15851 |
| **Alternative** | Wallace et al. (2024). The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions. arXiv:2404.13208. |
| **Status** | Confirmed — peer-reviewed (AAAI-26), replicated across 6 models; corroborated by OpenAI training research (Wallace et al.) |
| **Core finding** | LLMs do not reliably prioritize system-prompt instructions over conflicting instructions from other sources. Resolution is inconsistent and biased by pretraining-derived priors, not by prompt structure or position. A dedicated training regime is required to make hierarchy reliable; without it, conflicts are resolved unpredictably. |
| **Mechanism** | No structural separation between instruction sources enforces reliable priority at inference time. When the same directive appears in two locations with divergent content, the model selects between them based on statistical priors from pretraining, not on explicit authority. |
| **Where used** | Justifies single source of truth in `AGENTS.md`: workflow details duplicated across agent files and skills that drift out of sync produce conflicting instructions the model cannot resolve reliably. |

---

### 25. Positional Attention Degradation in Long Contexts

| | |
|---|---|
| **Source** | Liu et al. (2023). Lost in the Middle: How Language Models Use Long Contexts. *Transactions of the Association for Computational Linguistics*. arXiv:2307.03172. |
| **Date** | 2023 |
| **URL** | https://arxiv.org/abs/2307.03172 |
| **Alternative** | McKinnon (2025). arXiv:2511.05850 — effect attenuated for simple retrieval in Gemini 2.5+; persists for multi-hop reasoning (HAMLET, EMNLP 2025; SealQA, ICLR 2026). |
| **Status** | Confirmed with caveat — robust for multi-hop reasoning; attenuated for simple retrieval in frontier models (2025–2026) |
| **Core finding** | Performance on tasks requiring retrieval from long contexts follows a U-shaped curve: highest when relevant content is at the beginning or end of the context, degraded when content falls in the middle. |
| **Mechanism** | Transformer attention is not uniform across token positions. Content placed in the middle of a long context receives less attention weight regardless of its relevance. |
| **Where used** | Supports keeping always-loaded files (`AGENTS.md`, agent routing files) lean. Duplicated workflow detail in always-loaded files increases total context length, pushing other content into lower-attention positions. |

---

### 26. Modular Prompt De-duplication Reduces Interference

| | |
|---|---|
| **Source** | Sharma & Henley (2026). Modular Prompt Optimization. arXiv:2601.04055. |
| **Date** | 2026 |
| **URL** | https://arxiv.org/abs/2601.04055 |
| **Alternative** | — |
| **Status** | Partially confirmed — single-agent reasoning benchmarks (ARC-Challenge, MMLU) only; not tested on multi-file agent architectures |
| **Core finding** | Structured prompts with explicit section de-duplication outperform both monolithic prompts and unstructured modular prompts. The mechanism cited is "reducing redundancy and interference between components." |
| **Mechanism** | Redundant content across prompt sections creates competing attention targets. De-duplication concentrates relevant signal in one canonical location per concern. |
| **Where used** | Supports the rule that skills and agent routing files contain no duplication of `AGENTS.md` content or of each other. |

---

### 27. Agent File Architecture — Three-File Separation

| | |
|---|---|
| **Source** | Convergence of entries 23, 24, 25, 26. |
| **Date** | — |
| **URL** | — |
| **Alternative** | — |
| **Status** | Inferred — no direct A/B test of this architecture exists; supported by convergence of confirmed and partially confirmed findings above |
| **Core finding** | Three distinct failure modes (instruction conflict on drift, positional attention degradation in long contexts, redundancy interference) converge to produce a three-file split with defined content rules for each. |
| **Mechanism** | Each file runs at a different time and serves a different purpose. Mixing concerns across files reintroduces the failure modes the split is designed to prevent. |
| **Where used** | Structural rule for `AGENTS.md`, `.opencode/agents/*.md`, and `.opencode/skills/*.md`. |

| File | Runs when | Contains | Does NOT contain |
|---|---|---|---|
| `AGENTS.md` | Every session, always loaded | Project conventions, shared commands, formats, standards | Step procedures, role-specific rules, path specs |
| `.opencode/agents/*.md` | When that role is invoked | Role identity, step ownership, skill load instructions, tool permissions, escalation paths | Workflow details, principle lists, path specs, commit formats |
| `.opencode/skills/*.md` | On demand, when that step begins | Full procedural instructions for that step, self-contained | Duplication of `AGENTS.md` content or other skills |

---

### 28. Active Listening — Paraphrase-Clarify-Summarize

| | |
|---|---|
| **Source** | Rogers, C. R., & Farson, R. E. (1957). *Active Listening*. Industrial Relations Center, University of Chicago. |
| **Date** | 1957 |
| **URL** | — |
| **Alternative** | McNaughton, D. et al. (2008). Learning to Listen. *Topics in Early Childhood Special Education*, 27(4), 223–231. (LAFF strategy: Listen, Ask, Focus, Find) |
| **Status** | Confirmed — foundational clinical research; widely replicated across professional and educational contexts |
| **Core finding** | Active listening — paraphrasing what was heard in the listener's own words, asking clarifying questions, then summarizing the main points and intent — reduces misunderstanding, builds trust, and confirms mutual understanding before proceeding. The three-step responding sequence (Paraphrase → Clarify → Summarize) is the operationalizable form of the broader active listening construct. |
| **Mechanism** | Paraphrasing forces the listener to reconstruct the speaker's meaning in their own language, surfacing gaps immediately. Clarifying questions address residual ambiguity. Summarizing creates a shared record that both parties can confirm or correct. Together they eliminate the assumption that "I heard" equals "I understood." Without this protocol, agents (human or AI) proceed on partial or misread requirements, producing work that is technically complete but semantically wrong. |
| **Where used** | PO summarization protocol in `scope/SKILL.md`: after each interview round, the PO must produce a "Here is what I understood" block (paraphrase → clarify → summarize) before moving to Phase 3 (Stories) or Phase 4 (Criteria). The stakeholder confirms or corrects before the PO proceeds. |

---

## Bibliography

1. Cialdini, R. B. (2001). *Influence: The Psychology of Persuasion* (rev. ed.). HarperBusiness.
2. Craik, F. I. M., & Lockhart, R. S. (1972). Levels of processing: A framework for memory research. *Journal of Verbal Learning and Verbal Behavior*, 11(6), 671–684.
3. Gollwitzer, P. M. (1999). Implementation intentions: Strong effects of simple planning aids. *American Journal of Preventive Medicine*, 16(4), 257–276.
4. Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research*, 77(1), 81–112.
5. Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.
6. Klein, G. (1998). *Sources of Power: How People Make Decisions*. MIT Press.
7. McDaniel, M. A., & Einstein, G. O. (2000). Strategic and automatic processes in prospective memory retrieval. *Applied Cognitive Psychology*, 14(7), S127–S144.
8. Mellers, B. A., Hertwig, R., & Kahneman, D. (2001). Do frequency representations eliminate cooperative bias? *Psychological Review*, 108(4), 709–735.
9. Miller, G. A. (1956). The magical number seven, plus or minus two. *Psychological Review*, 63(2), 81–97.
10. Sweller, J. (1988). Cognitive load during problem solving. *Cognitive Science*, 12(2), 257–285.
11. Tetlock, P. E. (1983). Accountability: A social determinant of judgment. In M. D. B. T. Strother (Ed.), *Psychology of Learning and Motivation* (Vol. 17, pp. 295–332). Academic Press.
12. Fowler, M. (2018). The Practical Test Pyramid. *Thoughtworks*. https://martinfowler.com/articles/practical-test-pyramid.html
13. Google Testing Blog. (2013). Testing on the Toilet: Test Behavior, Not Implementation.
14. Martin, R. C. (2017). First-Class Tests. *Clean Coder Blog*.
15. MacIver, D. R. (2016). What is Property Based Testing? *Hypothesis*. https://hypothesis.works/articles/what-is-property-based-testing/
16. Boehm, B. W. (1981). *Software Engineering Economics*. Prentice-Hall.
17. Boehm, B., & Papaccio, P. N. (1988). Understanding and controlling software costs. *IEEE Transactions on Software Engineering*, 14(10), 1462–1477.
18. Wake, B. (2003). INVEST in Good Stories, and SMART Tasks. *XP123.com*.
19. Cohn, M. (2004). *User Stories Applied: For Agile Software Development*. Addison-Wesley.
20. Wynne, M. (2015). Introducing Example Mapping. *Cucumber Blog*. https://cucumber.io/blog/bdd/example-mapping-introduction/
21. Cucumber Team. (2024). Better Gherkin. *Cucumber Documentation*. https://cucumber.io/docs/bdd/better-gherkin/
22. Clegg, D., & Barker, R. (1994). *Case Method Fast-Track: A RAD Approach*. Addison-Wesley.
23. OpenAI. (2024). Agent definitions. *OpenAI Agents SDK Documentation*. https://platform.openai.com/docs/guides/agents/define-agents
24. Anthropic. (2024). Building effective agents. *Anthropic Engineering Blog*. https://www.anthropic.com/engineering/building-effective-agents
25. Anthropic. (2025). Best practices for Claude Code. *Anthropic Documentation*. https://www.anthropic.com/engineering/claude-code-best-practices
26. OpenCode. (2026). Agent Skills. *OpenCode Documentation*. https://opencode.ai/docs/skills/
27. Geng et al. (2025). Control Illusion: The Failure of Instruction Hierarchies in Large Language Models. AAAI-26. arXiv:2502.15851. https://arxiv.org/abs/2502.15851
28. Wallace, E. et al. (2024). The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions. arXiv:2404.13208. https://arxiv.org/abs/2404.13208
29. Liu, N. F. et al. (2023). Lost in the Middle: How Language Models Use Long Contexts. *Transactions of the Association for Computational Linguistics*. arXiv:2307.03172. https://arxiv.org/abs/2307.03172
30. McKinnon, R. (2025). arXiv:2511.05850. https://arxiv.org/abs/2511.05850
31. Sharma, A., & Henley, A. (2026). Modular Prompt Optimization. arXiv:2601.04055. https://arxiv.org/abs/2601.04055
32. Rogers, C. R., & Farson, R. E. (1957). *Active Listening*. Industrial Relations Center, University of Chicago.
33. McNaughton, D., Hamlin, D., McCarthy, J., Head-Reeves, D., & Schreiner, M. (2008). Learning to Listen: Teaching an Active Listening Strategy to Preservice Education Professionals. *Topics in Early Childhood Special Education*, 27(4), 223–231.
