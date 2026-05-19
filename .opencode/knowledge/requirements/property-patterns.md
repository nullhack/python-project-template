---
domain: requirements
tags: [property-based-testing, examples, scenario-outline, test-design, bdd, hypothesis]
last-updated: 2026-05-19
---

# Property Patterns for BDD Example Selection

## Key Takeaways

- When writing BDD Examples, use these seven property patterns (Wlaschin, 2014) to decide whether an Example should be a simple `Example:` or a `Scenario Outline:` with multiple input combinations.
- **Simple `Example:`** is appropriate when the behaviour is a single observable outcome with fixed inputs — no interesting property to generalise.
- **`Scenario Outline:`** is appropriate when the same behavioural outcome holds across multiple input/output combinations — the property pattern reveals which combinations matter.
- The seven patterns also surface missing Examples: if a property pattern applies but has no corresponding Example, the specification is incomplete.

## Concepts

**Seven Property Patterns** (Wlaschin, 2014). When choosing what to verify in a specification, these patterns help discover what properties (invariants, relationships) the system should satisfy:

| Pattern | Core Idea | When to use Scenario Outline |
|---------|-----------|------------------------------|
| Different paths, same destination | Two operation sequences produce the same result | When multiple paths exist to the same outcome (e.g., different orderings, different constructors) |
| There and back again | An operation and its inverse return to the starting state | When serialise/deserialise, encode/decode, add/remove pairs exist |
| Some things never change | An invariant is preserved after a transformation | When a transform should preserve size, membership, ordering, or other invariants |
| The more things change, the more they stay the same | Applying an operation twice is the same as applying it once (idempotence) | When operations should be idempotent (e.g., deduplicate, round, normalise) |
| Solve a smaller problem first | A property true for a small case implies truth for a composed case (structural induction) | When recursive or composable structures are involved (lists, trees, nested objects) |
| Hard to prove, easy to verify | Finding the answer is complex, but checking it is simple | When output can be verified by a simpler check (e.g., sort result is a permutation, parse result concatenates to original) |
| The test oracle | An alternate implementation exists to verify results | When a brute-force or simplified reference implementation can validate the optimised version |

**Using Patterns to Choose Example vs Scenario Outline**: During feature example creation (write-bdd-features skill), apply these patterns to each Rule:

1. For each Rule, ask: "Does any of the seven patterns apply to this behaviour?"
2. If **no pattern applies** — the behaviour is a single discrete outcome with fixed inputs — write a simple `Example:`.
3. If a pattern applies — the behaviour holds across a range of inputs — write a `Scenario Outline:` with an `Examples:` table covering the significant input combinations surfaced by the pattern.
4. If a pattern reveals an edge case not covered by existing Examples — add the missing Example.

**Pattern-to-Example Decision Tree**:

```
Does the Rule describe an invariant that holds across inputs?
├─ Yes → Scenario Outline with inputs that exercise the invariant
│        + Hypothesis property test per [[software-craft/test-design#concepts]]
└─ No → Does the Rule have "easy to verify" checkable output?
    ├─ Yes → Can multiple inputs produce different valid outputs?
    │        ├─ Yes → Scenario Outline with representative input/output pairs
    │        └─ No → Simple Example with the key input
    └─ No → Simple Example (single observable outcome)
```

**Pre-mortem Integration**: During the behavior-level pre-mortem per [[requirements/pre-mortem#concepts]], apply property patterns adversarially: "Given this pattern applies to this Rule, what inputs would break it?" Surface failure modes as additional Examples.

## Content

### Pattern Application Examples

**Different paths, same destination**: A sort function produces the same result regardless of input order. Use Scenario Outline with different input orderings asserting identical sorted output. This also applies to commutative operations: `a + b == b + a`.

**There and back again**: JSON serialisation round-trips: `decode(encode(obj)) == obj`. Use Scenario Outline with different object shapes. HTTP encode/decode, compression/decompress, and format conversions all fit this pattern.

**Some things never change**: A `map` operation preserves list length. A `sort` preserves the multiset of elements. Use Scenario Outline with different input sizes and element values, asserting the invariant holds.

**Idempotence**: Calling `distinct()` twice produces the same result as calling it once. Use Scenario Outline with different input sets, some already distinct, some with duplicates. REST PUT operations are another common case.

**Structural induction**: If a property holds for a base case (empty list) and for appending one element, it holds for all lists. Use Scenario Outline with list sizes 0, 1, 2, N to cover induction steps.

**Hard to prove, easy to verify**: Finding a prime factorisation is hard, but multiplying the factors back is trivial. Tokenising a string is hard, but concatenating tokens should equal the original. Use Scenario Outline with different input strings or numbers, asserting the verification check.

**Test oracle**: A fast sorting algorithm can be verified against a naive bubble sort. A parallel computation can be verified against a sequential version. Use Scenario Outline where each row exercises a different input against both implementations.

### Integration with BDD Workflow

When the PO (or SE) writes Examples during `write-bdd-features`:

1. Write the Rule's declarative behaviour first (Given/When/Then).
2. Check each of the seven patterns against the Rule.
3. For each matching pattern, determine the input combinations that exercise the property.
4. If 1-2 combinations → simple `Example:` per combination.
5. If 3+ combinations with the same step structure → `Scenario Outline:` with `Examples:` table.
6. For invariant/structural Rules → also generate a Hypothesis property test per [[software-craft/test-design#concepts]].

### Hypothesis Property Tests from Patterns

Each invariant/structural Rule should produce both BDD Examples AND a Hypothesis property test. The property pattern guides the Hypothesis strategy:

| Pattern | Hypothesis Strategy |
|---------|-------------------|
| Different paths, same destination | `@given(inputs, order=strategies.permutations)` |
| There and back again | `@given(arbitrary_input)` then round-trip assert |
| Some things never change | `@given(transform_input)` then assert invariant |
| Idempotence | `@given(input)` then `assert f(f(x)) == f(x)` |
| Structural induction | `@given(recursive_strategy)` with base + step |
| Hard to prove, easy to verify | `@given(input)` then verify output with simple check |
| Test oracle | `@given(input)` then `assert fast(input) == oracle(input)` |

## Related

- [[requirements/gherkin]]
- [[requirements/pre-mortem]]
- [[software-craft/test-design]]
- [[software-craft/tdd]]

## Related

- [[software-craft/test-design]]
- [[software-craft/tdd]]
- [[requirements/gherkin]]
- [[requirements/pre-mortem]]
