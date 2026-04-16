# Academic Research — Theoretical Foundations

This document explains the cognitive and social-science mechanisms that justify the workflow reforms in this template. Each mechanism is grounded in peer-reviewed research.

---

## Mechanisms

### 1. Pre-mortem (Prospective Hindsight)

| | |
|---|---|
| **Source** | Klein, G. (1998). *Sources of Power: How People Make Decisions*. MIT Press. |
| **Core finding** | Asking "imagine this failed — why?" catches 30% more issues than forward-looking review. |
| **Mechanism** | Prospective hindsight shifts from prediction (weak) to explanation (strong). The brain is better at explaining past events than predicting future ones. By framing as "it already failed," you activate explanation mode. |
| **Where used** | PO pre-mortem at scope, developer pre-mortem before handoff. |

---

### 2. Implementation Intentions

| | |
|---|---|
| **Source** | Gollwitzer, P. M. (1999). Implementation intentions: Strong effects of simple planning aids. *American Journal of Preventive Medicine*, 16(4), 257–276. |
| **Core finding** | "If X then Y" plans are 2–3x more likely to execute than general intentions. |
| **Mechanism** | If-then plans create automatic cue-response links in memory. The brain processes "if function > 20 lines then extract helper" as an action trigger, not a suggestion to consider. |
| **Where used** | Refactor Self-Check Gates in `implementation/SKILL.md`, Code Quality checks in `verify/SKILL.md`. |

---

### 3. Commitment Devices

| | |
|---|---|
| **Source** | Cialdini, R. B. (2001). *Influence: The Psychology of Persuasion* (rev. ed.). HarperBusiness. |
| **Core finding** | Forcing an explicit micro-commitment (filling in a PASS/FAIL cell) creates resistance to reversals. A checkbox checked is harder to uncheck than a todo noted. |
| **Mechanism** | Structured tables with PASS/FAIL cells create commitment-device effects. The act of marking "FAIL" requires justification, making silent passes psychologically costly. |
| **Where used** | SOLID enforcement table, ObjCal enforcement table, Design Patterns table — all require explicit PASS/FAIL with evidence. |

---

### 4. System 2 Before System 1

| | |
|---|---|
| **Source** | Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux. |
| **Core finding** | System 1 (fast, automatic) is vulnerable to anchoring and confirmation bias. System 2 (slow, deliberate) must be activated before System 1's judgments anchor. |
| **Mechanism** | Running semantic review *before* automated commands prevents the "all green" dopamine hit from anchoring the reviewer's judgment. Doing hard cognitive work first protects against System 1 shortcuts. |
| **Where used** | Verification order in `verify/SKILL.md`: semantic alignment check before commands. |

---

### 5. Adversarial Collaboration

| | |
|---|---|
| **Source** | Mellers, B. A., Hertwig, R., & Kahneman, D. (2001). Do frequency representations eliminate cooperative bias? *Psychological Review*, 108(4), 709–735. |
| **Core finding** | Highest-quality thinking emerges when parties hold different hypotheses and are charged with finding flaws in each other's reasoning. |
| **Mechanism** | Explicitly framing the reviewer as "your job is to break this feature" activates the adversarial collaboration mode. The reviewer seeks disconfirmation rather than confirmation. |
| **Where used** | Adversarial mandate in `reviewer.md` and `verify/SKILL.md`. |

---

### 6. Accountability to Unknown Audience

| | |
|---|---|
| **Source** | Tetlock, P. E. (1983). Accountability: A social determinant of judgment. In M. D. B. T. Strother (Ed.), *Psychology of Learning and Motivation* (Vol. 17, pp. 295–332). Academic Press. |
| **Core finding** | Accountability to an unknown audience with unknown views improves reasoning quality. The agent anticipates being audited and adjusts reasoning. |
| **Mechanism** | The explicit report format (APPROVED/REJECTED with evidence) creates an accountability structure — the reviewer's reasoning will be read by the PO. |
| **Where used** | Report format in `verify/SKILL.md`, structured evidence columns in all enforcement tables. |

---

### 7. Chunking and Cognitive Load Reduction

| | |
|---|---|
| **Source** | Miller, G. A. (1956). The magical number seven, plus or minus two. *Psychological Review*, 63(2), 81–97. |
| **Alternative** | Sweller, J. (1988). Cognitive load during problem solving. *Cognitive Science*, 12(2), 257–285. |
| **Core finding** | Structured tables reduce working memory load vs. narrative text. Chunking related items into table rows enables parallel processing. |
| **Mechanism** | Replacing prose checklists ("Apply SOLID principles") with structured tables (5 rows, 4 columns) allows the reviewer to process all items in a single pass. |
| **Where used** | All enforcement tables in `verify/SKILL.md` and `reviewer.md`. |

---

### 8. Elaborative Encoding

| | |
|---|---|
| **Source** | Craik, F. I. M., & Lockhart, R. S. (1972). Levels of processing: A framework for memory research. *Journal of Verbal Learning and Verbal Behavior*, 11(6), 671–684. |
| **Core finding** | Deeper processing — explaining *why* a rule matters — leads to better retention and application than shallow processing (just listing rules). |
| **Mechanism** | Adding a "Why it matters" column to enforcement tables forces the reviewer to process the rationale, not just scan the rule name. |
| **Where used** | SOLID table, ObjCal table, Design Patterns table — all have "Why it matters" column. |

---

### 9. Error-Specific Feedback

| | |
|---|---|
| **Source** | Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research*, 77(1), 81–112. |
| **Core finding** | Feedback is most effective when it tells the agent exactly what went wrong and what the correct action is. "FAIL: function > 20 lines at file:47" is actionable. "Apply function length rules" is not. |
| **Mechanism** | The evidence column in enforcement tables requires specific file:line references, turning vague rules into actionable directives. |
| **Where used** | Evidence column in all enforcement tables. |

---

### 10. Prospective Memory Cues

| | |
|---|---|
| **Source** | McDaniel, M. A., & Einstein, G. O. (2000). Strategic and automatic processes in prospective memory retrieval. *Applied Cognitive Psychology*, 14(7), S127–S144. |
| **Core finding** | Memory for intended actions is better when cues are embedded at the point of action, not in a separate appendix. |
| **Mechanism** | Placing if-then gates inline (in the REFACTOR section) rather than in a separate "reference" document increases adherence. The cue appears exactly when the developer is about to make the relevant decision. |
| **Where used** | Refactor Self-Check Gates embedded inline in `implementation/SKILL.md`. |

---

### 11. Observable Behavior Testing

| | |
|---|---|
| **Source** | Fowler, M. (2018). *The Practical Test Pyramid*. Thoughtworks. https://martinfowler.com/articles/practical-test-pyramid.html |
| **Core finding** | Tests should answer "if I enter X and Y, will the result be Z?" — not "will method A call class B first?" |
| **Mechanism** | A test is behavioral if its assertion describes something a caller/user can observe without knowing the implementation. The test should still pass if you completely rewrite the internals. |
| **Where used** | Contract test rule in `tdd/SKILL.md`: "Write every test as if you cannot see the production code." |

---

### 12. Test-Behavior Alignment

| | |
|---|---|
| **Source** | Google Testing Blog (2013). *Testing on the Toilet: Test Behavior, Not Implementation*. |
| **Core finding** | Test setup may need to change if implementation changes, but the actual test shouldn't need to change if the code's user-facing behavior doesn't change. |
| **Mechanism** | Tests that are tightly coupled to implementation break on refactoring and become a drag on design improvement. Behavioral tests survive internal rewrites. |
| **Where used** | Contract test rule + bad example in `tdd/SKILL.md`, reviewer verification check in `reviewer.md`. |

---

### 13. Tests as First-Class Citizens

| | |
|---|---|
| **Source** | Martin, R. C. (2017). *First-Class Tests*. Clean Coder Blog. |
| **Core finding** | Tests should be treated as first-class citizens of the system — not coupled to implementation. Bad tests are worse than no tests because they give false confidence. |
| **Mechanism** | Tests written as "contract tests" — describing what the caller observes — remain stable through refactoring. Tests that verify implementation details are fragile and create maintenance burden. |
| **Where used** | Contract test rule in `tdd/SKILL.md`, verification check in `reviewer.md`. |

---

### 14. Property-Based Testing (Invariant Discovery)

| | |
|---|---|
| **Source** | MacIver, D. R. (2016). *What is Property Based Testing?* Hypothesis. https://hypothesis.works/articles/what-is-property-based-testing/ |
| **Core finding** | Property-based testing is "the construction of tests such that, when these tests are fuzzed, failures reveal problems that could not have been revealed by direct fuzzing." Property tests test *invariants* — things that must always be true about the contract, not things that fall out of how you wrote it. |
| **Mechanism** | Meaningful property tests assert invariants: "assert Score(x).value >= 0" tests the contract. Tautological tests assert reconstruction: "assert Score(x).value == x" tests the implementation. |
| **Where used** | Meaningful vs. Tautological table in `tdd/SKILL.md`, Property-Based Testing Decision Rule table in `tdd/SKILL.md`. |

---

### 15. Mutation Testing (Test Quality Verification)

| | |
|---|---|
| **Source** | King, K. N. (1991). *The Gamma (formerly mutants)*. |
| **Alternative** | Mutation testing tools: Cosmic Ray, mutmut (Python) |
| **Core finding** | A meaningful test fails when a mutation (small deliberate code change) is introduced. A tautological test passes even with mutations because it doesn't constrain the behavior. |
| **Mechanism** | If a test survives every mutation of the production code without failing, it tests nothing. Only tests that fail on purposeful "damage" to the code are worth keeping. |
| **Where used** | Note in `tdd/SKILL.md` Quality Rules (implicitly encouraged: tests must describe contracts, not implementation, which is the theoretical complement to mutation testing). |

---

### 16. Cost of Change Curve (Shift Left)

| | |
|---|---|
| **Source** | Boehm, B. W. (1981). *Software Engineering Economics*. Prentice-Hall. |
| **Alternative** | Boehm, B., & Papaccio, P. N. (1988). Understanding and controlling software costs. *IEEE Transactions on Software Engineering*, 14(10), 1462–1477. |
| **Core finding** | The cost to fix a defect multiplies by roughly 10x per SDLC phase: requirements (1x) → design (5x) → coding (10x) → testing (20x) → production (200x). A defect caught during requirements costs 200x less than the same defect found after release. |
| **Mechanism** | Defects compound downstream: a wrong requirement becomes a wrong design, which becomes wrong code, which becomes wrong tests, all of which must be unwound. Catching errors at the source eliminates the entire cascade. This is the empirical foundation for "shift left" — investing earlier in quality always dominates fixing later. |
| **Where used** | Justifies the multi-session PO elicitation model: every acceptance criterion clarified at scope prevents 10–200x rework downstream. Also justifies the adversarial pre-mortem at the end of each elicitation cycle, and the adversarial mandate in `verify/SKILL.md`. The entire 6-step pipeline is ordered to surface defects at the earliest (cheapest) phase. |

---

### 17. INVEST Criteria for User Stories

| | |
|---|---|
| **Source** | Wake, B. (2003). *INVEST in Good Stories, and SMART Tasks*. XP123.com. |
| **Alternative** | Cohn, M. (2004). *User Stories Applied: For Agile Software Development*. Addison-Wesley. |
| **Core finding** | Stories that are Independent, Negotiable, Valuable, Estimable, Small, and Testable produce fewer downstream defects and smoother development cycles. Stories that fail INVEST — especially "Testable" and "Small" — are the leading cause of scope creep and unbounded iteration. |
| **Mechanism** | INVEST serves as a quality gate before stories enter development. "Testable" forces the PO to express observable outcomes (directly enabling Given/When/Then). "Small" forces decomposition, which reduces cognitive load and makes estimation feasible. "Independent" prevents hidden ordering dependencies between stories. |
| **Where used** | INVEST gate in Phase 3 of `scope/SKILL.md`. PO verifies every story against all 6 letters before committing. |

---

### 18. Example Mapping (Rules Layer)

| | |
|---|---|
| **Source** | Wynne, M. (2015). *Introducing Example Mapping*. Cucumber Blog. https://cucumber.io/blog/bdd/example-mapping-introduction/ |
| **Core finding** | Inserting a "rules" layer between stories and examples prevents redundant or contradictory acceptance criteria. A story with many rules needs splitting; a story with many open questions is not ready for development. |
| **Mechanism** | Example Mapping uses four card types: Story (yellow), Rules (blue), Examples (green), Questions (red). The rules layer groups related examples under the business rule they illustrate. Without this layer, POs jump from story directly to examples and lose the reasoning that connects them. Red cards (unanswered questions) are a first-class signal to stop and investigate rather than assume. |
| **Where used** | `## Rules` section in per-feature `discovery.md` (Phase 2). PO identifies business rules before writing Examples in Phase 4, making the reasoning behind Example clusters visible and reviewable. |

---

### 19. Declarative Gherkin

| | |
|---|---|
| **Source** | Cucumber Team. (2024). *Better Gherkin*. Cucumber Documentation. https://cucumber.io/docs/bdd/better-gherkin/ |
| **Core finding** | Declarative Gherkin ("When Bob logs in") produces specifications that survive UI changes. Imperative Gherkin ("When I click the Login button") couples specs to implementation details and breaks on every UI redesign. |
| **Mechanism** | Declarative steps describe *what happens* at the business level. Imperative steps describe *how the user interacts with a specific UI*. The distinction maps to the abstraction level: declarative = behavior contract, imperative = interaction script. AI agents are especially prone to writing imperative Gherkin because they mirror literal steps. |
| **Where used** | Declarative vs. imperative table in Phase 4 of `scope/SKILL.md`. PO is explicitly instructed to write behavior descriptions, not UI interaction scripts. |

---

### 20. MoSCoW Prioritization (Within-Story Triage)

| | |
|---|---|
| **Source** | Clegg, D., & Barker, R. (1994). *Case Method Fast-Track: A RAD Approach*. Addison-Wesley (DSDM origin). |
| **Core finding** | Classifying requirements as Must/Should/Could/Won't forces explicit negotiation about what is essential vs. desired. When applied *within* a single story (not just across a backlog), it reveals bloated stories that should be split. |
| **Mechanism** | DSDM mandates that Musts cannot exceed 60% of total effort. At the story level: if a story has 12 Examples and only 3 are Musts, the remaining 9 can be deferred or split into a follow-up story. This prevents gold-plating and keeps stories small. |
| **Where used** | MoSCoW triage in Phase 4 of `scope/SKILL.md`. PO applies Must/Should/Could when a story exceeds 5 Examples. |

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
