---
domain: software-craft
tags: [testing, refactoring, test-design, coverage, coupling]
last-updated: 2026-04-26
---

# Refactor-Safe Test Design

## Key Takeaways

- Maximise feature and contract tests; minimise white-box tests; use property tests for invariants.
- Public interface evolution is a feature change, not a refactoring — update tests as part of a RED-GREEN-REFACTOR cycle.
- Test what a caller observes, not how the code achieves it; test outcomes, not steps.
- Use Hypothesis for invariants that hold regardless of implementation, not for exercising specific code paths.
- Reach internal code through the public interface; if a path is unreachable, it's dead code — remove it.
- Keep the public interface small via Interface Segregation and OC-8 to minimise test coupling.
- When a test breaks during refactoring, diagnose first: if it tests internal structure, rewrite it; if it tests observable behaviour, the "refactoring" is a feature change — revert and run RED-GREEN-REFACTOR explicitly.

## Concepts

**The Refactor-Safety Spectrum**: Tests fall on a spectrum from most refactor-safe to least. Feature tests (through the outermost public interface) are the most resilient. Unit contract tests (through module/class public API) are highly resilient. Property tests (testing invariants via Hypothesis) are the most resilient of all. White-box unit tests (testing internal methods, private state, call chains) are the least resilient and should be minimised.

**Public Interface Evolution Is a Feature Change**: Changing a public interface is not a refactoring — it requires its own RED-GREEN-REFACTOR cycle. When the public interface changes, tests that depend on the old interface should break (the contract they verify no longer exists). Update tests as part of the cycle. To minimise this pain, keep the surface area of inner public APIs small using SOLID-I and OC-8.

**Test What a Caller Observes**: Test observable behaviour, not implementation details. Avoid testing private methods, specific call chains, or concrete types. Test outcomes, not sequences of internal calls. Feature tests in `tests/features/` are the anchor — if internal restructuring breaks one, it was a feature change, not a refactoring.

**Use Hypothesis for Invariants**: Use Hypothesis `@given` for properties that hold regardless of implementation — mathematical invariants, parsing contracts, value object constraints. Do not use Hypothesis to exercise specific code paths. Property tests verify that a property holds across many inputs, not that a particular path is reached.

**Achieving 100% Coverage Without Coupling**: Coverage and coupling are independent dimensions. The target is high coverage with weak coupling. Reach internal code through the public interface. Use Hypothesis `@given` for branch coverage. Add targeted edge-case tests in `tests/unit/` for specific boundary values. If a code path is unreachable through the public interface, it's dead code — remove it.

**Keep the Public Interface Small**: Fewer public methods means fewer tests depend on the contract. Interface Segregation (SOLID-I) splits wide interfaces into narrow ones. OC-8 (≤2 instance variables per behavioural class) keeps classes small. The Facade pattern provides simplified entry points for complex subsystems.

**Diagnostic for Breaking Tests**: When a test breaks during refactoring, diagnose before deleting. If the test is coupled to internal structure (private methods, call chains, concrete types), rewrite it to use the public interface and re-apply the refactoring. If the test is coupled to observable behaviour, the "refactoring" changed observable behaviour — it is a feature change. Revert the step, put on the feature hat, and run RED-GREEN-REFACTOR explicitly. Never delete a failing test without diagnosing it first.

## Content

### The Refactor-Safety Spectrum

Tests fall on a spectrum from most refactor-safe to least:

| Tier | Location | Tests through | Resilience | When they break |
|---|---|---|---|---|
| Feature | `tests/features/` | Outermost public interface (user-facing behaviour) | Highest | User needs changed, not internal restructuring |
| Unit (contract) | `tests/unit/` | Module/class public API | High | Public contract changed — this is a feature change |
| Unit (property) | `tests/unit/` | Invariants via Hypothesis `@given` | Highest | Mathematical or domain property violated |
| Unit (white-box) | `tests/unit/` | Internal methods, private state, call chains | **Low** | Any internal restructuring — avoid these |

**Goal**: Maximise feature and contract tests. Minimise white-box tests. Use property tests for invariants that hold regardless of implementation.

### Public Interface Evolution Is a Feature Change

Changing a public interface — adding, removing, or modifying a function's signature or observable behaviour — is **not a refactoring**. It is a **feature change** that requires its own RED-GREEN-REFACTOR cycle.

When the public interface changes:
1. Tests that depend on the old interface **should break** — the contract they verify no longer exists
2. Update tests as part of the RED-GREEN-REFACTOR cycle: write the new failing test (RED), make it pass (GREEN), then remove or update tests for the dead interface (REFACTOR)
3. This is expected and correct — do not try to make old tests survive a contract change

The strategy to minimise this pain is to **keep the surface area of inner public APIs small**. The smaller the contract, the fewer tests depend on it. SOLID (especially Interface Segregation) and Object Calisthenics (OC-8: ≤2 instance variables per behavioural class) naturally constrain API surface area.

### Practical Patterns for Refactor-Safe Tests

#### 1. Test what a caller observes, not how the code achieves it

```python
# Fragile — coupled to internal structure
def test_parse_splits_on_comma():
    result = parser._split_on_comma("a,b,c")
    assert result == ["a", "b", "c"]

# Refactor-safe — coupled to public contract
def test_parse_returns_ordered_elements():
    result = parser.parse("a,b,c")
    assert result.elements == ["a", "b", "c"]
```

If `_split_on_comma` is renamed, replaced, or restructured, the fragile test breaks. The refactor-safe test survives because the observable behaviour (`parse` returns elements in order) is unchanged.

#### 2. Use Hypothesis for invariants, not for exercising implementation paths

```python
# Fragile — tests a specific code path
@given(x=st.integers())
def test_sort_uses_merge(x):
    result = sort([x])
    assert result == sorted([x])

# Refactor-safe — tests a property that holds regardless of algorithm
@given(xs=st.lists(st.integers()))
def test_sort_idempotent(xs):
    assert sort(sort(xs)) == sort(xs)
```

The property "sorting is idempotent" holds whether the implementation uses merge sort, quicksort, or timsort. The specific code path test breaks if you change algorithms.

#### 3. Test outcomes, not steps

```python
# Fragile — coupled to sequence of internal calls
def test_checkout_calls_calculate_then_apply_discount():
    checkout.calculate_total(order)
    checkout.apply_discount(order)
    assert checkout.total == 90

# Refactor-safe — coupled to observable outcome
def test_checkout_applies_discount_to_total():
    result = checkout.checkout(order)
    assert result.total == 90
```

If the checkout process is restructured to combine calculation and discounting, the fragile test breaks because the call sequence changed. The refactor-safe test only cares about the final total.

#### 4. No `isinstance()`, `type()`, or private attribute checks

From [[software-craft/test-conventions]]:
- `isinstance()` and `type()` checks assert that a specific concrete type is returned, locking the implementation to that type
- Private attribute (`_x`) checks assert that internal state is stored in a particular shape, locking the data layout

Both break when you refactor to a different type or data structure. Test the observable return value or public state instead.

#### 5. Feature tests are your anchor

Feature tests in `tests/features/` trace to `@id` acceptance criteria and test through the outermost public interface. They are the most refactor-safe tier. If internal restructuring breaks a feature test, the restructuring changed observable behaviour — it was a feature change, not a refactoring.

### Achieving 100% Coverage Without Coupling

Coverage is a measure of which code paths execute, not how tests are coupled to implementation. These are independent dimensions:

| | Weak coupling | Strong coupling |
|---|---|---|
| High coverage | **Target** — tests exercise all paths through the public interface | Fragile — tests exercise all paths but through internals |
| Low coverage | Gaps — refactoring-safe but incomplete | Worst — fragile and incomplete |

To achieve high coverage with weak coupling:

1. **Reach internal code through the public interface.** If a private method `._validate()` exists, test it indirectly by calling the public method that calls it with invalid input. The test exercises the validation path without depending on the private method's existence.

2. **Use Hypothesis `@given` for branch coverage.** Property-based testing explores many input combinations, naturally covering edge cases and branches without naming specific paths. Mark with `@pytest.mark.slow`.

3. **Add targeted edge-case tests in `tests/unit/`** for specific boundary values that Hypothesis might not hit. These test the *outcome* at the boundary, not the branch itself.

4. **If a code path is unreachable through the public interface**, it is dead code — remove it. Code that cannot be reached by any caller does not need test coverage.

### Diagnostic: When a Test Breaks During Refactoring

See [[software-craft/tdd]] for the full diagnostic flow. Summary:

1. **Is the test testing internal structure rather than observable behaviour?**
   - YES → Rewrite the test to use the public interface. Re-apply the refactoring.
   - NO → The "refactoring" changed observable behaviour. This is a feature change. Revert the step. Put on the feature hat. Run RED-GREEN-REFACTOR explicitly.

Never delete a failing test without diagnosing it first.

### Keeping the Public Interface Small

The fewer public methods a class has, the fewer tests depend on its contract, and the less painful it is to evolve. Design principles that help:

- **Interface Segregation (SOLID-I)**: Split wide interfaces into narrow ones. Clients depend only on what they use.
- **OC-8 (≤2 instance variables per behavioural class)**: Smaller classes have smaller public interfaces.
- **Facade pattern**: Provide a simplified entry point for complex subsystems. Feature tests go through the facade.

## Related

- [[software-craft/test-conventions]] — file layout, naming, markers, semantic alignment rule
- [[software-craft/tdd]] — RED-GREEN-REFACTOR cycle, green bar rule, two-hats discipline, diagnostic when a test breaks
- [[software-craft/code-quality]] — quality gates, semantic alignment, size limits
- [[software-craft/solid]] — Interface Segregation keeps public interfaces narrow
- [[software-craft/object-calisthenics]] — OC-8 constrains class surface area
- [[software-craft/smell-catalogue]] — test smells indicate coupling to implementation