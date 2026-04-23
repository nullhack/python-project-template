# Scientific Research — Testing

Foundations for test design, TDD, BDD, and property-based testing used in this template.

---

### 11. Observable Behavior Testing

| | |
|---|---|
| **Source** | Fowler, M. (2018). *The Practical Test Pyramid*. Thoughtworks. https://martinfowler.com/articles/practical-test-pyramid.html |
| **Date** | 2018 |
| **Status** | Confirmed |
| **Core finding** | Tests should answer "if I enter X and Y, will the result be Z?" — not "will method A call class B first?" |
| **Mechanism** | A test is behavioural if its assertion describes something a caller/user can observe without knowing the implementation. The test should still pass if you completely rewrite the internals. |
| **Where used** | Contract test rule in `implementation/SKILL.md`: "Write every test as if you cannot see the production code." |

---

### 12. Test-Behavior Alignment

| | |
|---|---|
| **Source** | Google Testing Blog (2013). *Testing on the Toilet: Test Behavior, Not Implementation*. |
| **Date** | 2013 |
| **Status** | Confirmed |
| **Core finding** | Test setup may need to change if implementation changes, but the actual test shouldn't need to change if the code's user-facing behaviour doesn't change. |
| **Mechanism** | Tests that are tightly coupled to implementation break on refactoring and become a drag on design improvement. Behavioral tests survive internal rewrites. |
| **Where used** | Contract test rule in `implement/SKILL.md`, system-architect verification check in `verify/SKILL.md`. |

---

### 13. Tests as First-Class Citizens

| | |
|---|---|
| **Source** | Martin, R. C. (2017). *First-Class Tests*. Clean Coder Blog. |
| **Date** | 2017 |
| **Status** | Confirmed |
| **Core finding** | Tests should be treated as first-class citizens of the system — not coupled to implementation. Bad tests are worse than no tests because they give false confidence. |
| **Mechanism** | Tests written as "contract tests" — describing what the caller observes — remain stable through refactoring. Tests that verify implementation details are fragile and create maintenance burden. |
| **Where used** | Contract test rule in `implement/SKILL.md`, verification check in `verify/SKILL.md`. |

---

### 14. Property-Based Testing (Invariant Discovery)

| | |
|---|---|
| **Source** | MacIver, D. R. (2016). *What is Property Based Testing?* Hypothesis. https://hypothesis.works/articles/what-is-property-based-testing/ |
| **Date** | 2016 |
| **Status** | Confirmed |
| **Core finding** | Property-based testing is "the construction of tests such that, when these tests are fuzzed, failures reveal problems that could not have been revealed by direct fuzzing." Property tests test *invariants* — things that must always be true about the contract. |
| **Mechanism** | Meaningful property tests assert invariants: `assert Score(x).value >= 0` tests the contract. Tautological tests assert reconstruction: `assert Score(x).value == x` tests the implementation. |
| **Where used** | Meaningful vs. Tautological table in `implementation/SKILL.md`. |

---

### 15. Mutation Testing (Test Quality Verification)

| | |
|---|---|
| **Source** | King, K. N. (1991). *The Gamma (formerly mutants)*. |
| **Date** | 1991 |
| **Alternative** | Mutation testing tools: Cosmic Ray, mutmut (Python) |
| **Status** | Confirmed |
| **Core finding** | A meaningful test fails when a mutation (small deliberate code change) is introduced. A tautological test passes even with mutations because it doesn't constrain the behaviour. |
| **Mechanism** | If a test survives every mutation of the production code without failing, it tests nothing. Only tests that fail on purposeful "damage" to the code are worth keeping. |
| **Where used** | Implicitly encouraged: tests must describe contracts, not implementation, which is the theoretical complement to mutation testing. |

---

### 51. Canon TDD — Authoritative Red-Green-Refactor Definition

| | |
|---|---|
| **Source** | Beck, K. (2023). "Canon TDD." *tidyfirst.substack.com*. December 11, 2023. https://tidyfirst.substack.com/p/canon-tdd |
| **Date** | 2023 |
| **Alternative** | Fowler, M. (2023). "Test Driven Development." *martinfowler.com*. https://martinfowler.com/bliki/TestDrivenDevelopment.html |
| **Status** | Confirmed — canonical source; explicitly authored to stop strawman critiques |
| **Core finding** | The canonical TDD loop is: (1) write a list of test scenarios; (2) convert exactly one item into a runnable test; (3) make it pass; (4) optionally refactor; (5) repeat. Writing all test code before any implementation is an explicit anti-pattern. |
| **Mechanism** | The interleaving of test-writing and implementation is not cosmetic — each test drives interface decisions at the moment they are cheapest to make. |
| **Where used** | Justifies one-@id-at-a-time interleaved TDD in Step 3 of `implementation/SKILL.md`. |

---

### 52. GOOS — Outer/Inner TDD Loop

| | |
|---|---|
| **Source** | Freeman, S., & Pryce, N. (2009). *Growing Object-Oriented Software, Guided by Tests*. Addison-Wesley. |
| **Date** | 2009 |
| **Status** | Confirmed — canonical ATDD/BDD integration model |
| **Core finding** | Acceptance tests and unit tests operate at two separate, nested timescales. The outer loop: write one failing acceptance test before any implementation. The inner loop: drive implementation with unit-level Red-Green-Refactor cycles until the acceptance test passes. |
| **Mechanism** | The outer loop provides direction (what to build); the inner loop provides momentum (how to build it). The acceptance test stays red throughout all inner cycles and goes green only when the feature is complete. |
| **Where used** | Justifies the two-level structure in Step 3: outer loop per `@id` acceptance test, inner loop per unit. |

---

### 53. Is TDD Dead? — Anti-Bureaucracy Evidence

| | |
|---|---|
| **Source** | Beck, K., Fowler, M., & Hansson, D. H. (2014). "Is TDD Dead?" Video series. *martinfowler.com*. https://martinfowler.com/articles/is-tdd-dead/ |
| **Date** | 2014 |
| **Status** | Confirmed — primary evidence for what TDD practitioners reject as overhead |
| **Core finding** | Per-cycle human reviewer gates, per-cycle checklists, and tests with zero delta coverage are all explicitly identified as harmful overhead. The green bar is the quality gate — not a checklist. |
| **Mechanism** | Administrative overhead added to TDD workflows increases the cost per cycle without increasing coverage or catching defects. The optimal TDD loop is as lean as productive. |
| **Where used** | Justifies removing per-test reviewer gates. Self-declaration moves to end-of-feature (once), preserving accountability at feature granularity without interrupting cycle momentum. |

---

### 54. Introducing BDD — Behavioural-Driven Development Origin

| | |
|---|---|
| **Source** | North, D. (2006). "Introducing BDD." *Better Software Magazine*. https://dannorth.net/introducing-bdd/ |
| **Date** | 2006 |
| **Alternative** | Fowler, M. (2013). "Given When Then." *martinfowler.com*. https://martinfowler.com/bliki/GivenWhenThen.html |
| **Status** | Confirmed — primary BDD source |
| **Core finding** | BDD evolved directly from TDD to address persistent practitioner confusion. BDD reframes TDD vocabulary around observable behaviour: scenarios instead of tests, Given-When-Then instead of Arrange-Act-Assert. |
| **Mechanism** | "Given" captures preconditions (Arrange), "When" captures the triggering event (Act), "Then" captures the observable outcome (Assert). Translating to G/W/T shifts focus from implementation mechanics to user-observable behaviour. |
| **Where used** | Theoretical link between Gherkin `@id` Examples (Step 1 output) and the TDD inner loop (Step 3). |

---

## Bibliography

1. Beck, K. (2023). "Canon TDD." *tidyfirst.substack.com*. https://tidyfirst.substack.com/p/canon-tdd
2. Beck, K., Fowler, M., & Hansson, D. H. (2014). "Is TDD Dead?" *martinfowler.com*. https://martinfowler.com/articles/is-tdd-dead/
3. Fowler, M. (2018). *The Practical Test Pyramid*. https://martinfowler.com/articles/practical-test-pyramid.html
4. Freeman, S., & Pryce, N. (2009). *Growing Object-Oriented Software, Guided by Tests*. Addison-Wesley.
5. Google Testing Blog. (2013). Testing on the Toilet: Test Behavior, Not Implementation.
6. King, K. N. (1991). *The Gamma (formerly mutants)*.
7. MacIver, D. R. (2016). What is Property Based Testing? *Hypothesis*. https://hypothesis.works/articles/what-is-property-based-testing/
8. Martin, R. C. (2017). First-Class Tests. *Clean Coder Blog*.
9. North, D. (2006). Introducing BDD. *Better Software Magazine*. https://dannorth.net/introducing-bdd/
