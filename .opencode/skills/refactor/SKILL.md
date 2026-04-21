---
name: refactor
description: Safe refactoring protocol for TDD — green bar rule, two-hats discipline, preparatory refactoring, and Fowler catalogue
version: "1.0"
author: software-engineer
audience: software-engineer
workflow: feature-lifecycle
---

# Refactor

Load this skill when entering the REFACTOR phase of a TDD cycle, or before starting RED on a new `@id` when preparatory refactoring is needed.

Sources: Fowler *Refactoring* 2nd ed. (2018); Beck *Canon TDD* (2023); Beck *Tidy First?* (2023); Martin *SOLID* (2000); Bay *Object Calisthenics* (2005). See `docs/research/oop-design.md` and `docs/research/refactoring-empirical.md`.

---

## The Definition

A refactoring is a **behavior-preserving** transformation of internal structure. If the transformation changes observable behavior, it is not a refactoring — it is a feature change, and requires its own RED-GREEN-REFACTOR cycle.

---

## The Green Bar Rule (absolute)

**Refactoring is only permitted while all existing tests pass.**

Every individual refactoring step must leave `test-fast` green. There are no exceptions.

---

## The Two-Hats Rule

Wear one hat at a time:

| Hat | Activity | Allowed during this hat |
|---|---|---|
| **Feature hat** | RED → GREEN | Write failing test, write minimum code to pass |
| **Refactoring hat** | REFACTOR | Restructure passing code; never add new behavior |

**Never mix hats in the same step.** If you discover a refactoring is needed while making a test pass (GREEN), note it — finish GREEN first, then switch hats.

---

## When to Use

### 1. REFACTOR phase (opportunistic)

After GREEN: `test-fast` passes for the current `@id`. Now restructure.

### 2. Preparatory refactoring (before RED)

When the current structure would make the next `@id` awkward to implement:
- Put on the **refactoring hat first**
- Refactor until the feature is easy to add
- Commit the preparatory refactoring separately (see Commit Discipline)
- Then put on the feature hat and run RED-GREEN-REFACTOR normally

Beck: *"For each desired change, make the change easy (warning: this may be hard), then make the easy change."*

---

## Step-by-Step

### Step 1 — Identify the smell

Run the smell checklist from your Self-Declaration or from the Architecture Smell Check:

| Smell | Likely catalogue entry |
|---|---|
| Function needs a comment to explain it | Extract Function |
| Class does two jobs | Extract Class |
| Method uses another class's data more than its own | Move Function |
| Same parameter group in multiple signatures | Introduce Parameter Object |
| Primitive with behaviour (money, email, range) | Replace Primitive with Object |
| Local variable holds a computed result | Replace Temp with Query |
| `isinstance` / type-flag conditionals | Replace Conditional with Polymorphism |
| Multiple functions share a data cluster | Combine Functions into Class |
| Nested conditions beyond 2 levels | Decompose Conditional / Guard Clauses |
| Object construction scattered without pattern | Factory Method / Builder |
| Scattered notification or state transition | Observer / State |
| Type-switching across callers | Strategy / Visitor |

If pattern smell detected: load `skill apply-patterns` for before/after examples.

### Step 2 — Apply one catalogue entry at a time

Apply a **single** catalogue entry, then run `test-fast` before moving to the next.

Never batch multiple catalogue entries into one step — you lose the ability to pinpoint which step broke something.

### Step 3 — Run after each step

```bash
uv run task test-fast
```

All tests green → proceed to next catalogue entry.
Any test red → see "When a Refactoring Breaks a Test" below.

### Step 4 — Commit when smell-free

Once no smells remain and `test-fast` is green:

```bash
uv run task test-fast   # must pass
```

Commit (see Commit Discipline below).

---

## Key Catalogue Entries

### Extract Function
Pull a cohesive fragment into a named function. Trigger: the fragment needs a comment to explain it.

```python
# Before
def process(order):
    # apply 10% discount
    order.total = order.total * Decimal("0.9")
    send_confirmation(order)

# After
def apply_discount(order: Order) -> None:
    """Apply the standard 10% discount."""
    order.total = order.total * Decimal("0.9")

def process(order: Order) -> None:
    """Process an order."""
    apply_discount(order)
    send_confirmation(order)
```

### Extract Class
Split a class doing two jobs. Trigger: data cluster + related behaviours that travel together.

```python
# Before
@dataclass
class Order:
    id: str
    street: str
    city: str
    total: Decimal

# After
@dataclass(frozen=True, slots=True)
class Address:
    """A delivery address."""
    street: str
    city: str

@dataclass
class Order:
    """An order placed by a customer."""
    id: str
    address: Address
    total: Decimal
```

### Introduce Parameter Object
Replace a recurring parameter group with a value object. Trigger: same 2+ params appear together across multiple signatures.

```python
# Before
def summarise(start_date: date, end_date: date) -> Report: ...
def filter_events(start_date: date, end_date: date) -> list[Event]: ...

# After
@dataclass(frozen=True, slots=True)
class DateRange:
    """An inclusive date range."""
    start: date
    end: date

def summarise(period: DateRange) -> Report: ...
def filter_events(period: DateRange) -> list[Event]: ...
```

### Replace Primitive with Object
Elevate a domain primitive to a class with behaviour. Trigger: primitive has validation rules or operations.

```python
# Before
def send_invoice(email: str) -> None: ...

# After
@dataclass(frozen=True, slots=True)
class EmailAddress:
    """A validated email address."""
    value: str

    def validate(self) -> None:
        """Validate the email format.

        Raises:
            ValueError: if the address has no '@' character.
        """
        if "@" not in self.value:
            raise ValueError(f"Invalid email: {self.value!r}")

def send_invoice(email: EmailAddress) -> None: ...
```

### Decompose Conditional / Guard Clauses
Flatten nested logic to ≤2 levels. Trigger: OC-1 violation or deeply nested `if` chains.

```python
# Before
def process(order):
    if order is not None:
        if order.total > 0:
            if order.is_confirmed:
                ship(order)

# After
def process(order: Order | None) -> None:
    """Ship a confirmed order."""
    if order is None:
        return
    if order.total <= 0:
        return
    if not order.is_confirmed:
        return
    ship(order)
```

---

## When a Refactoring Breaks a Test

A refactoring that breaks a test is **not a refactoring**. Stop. Diagnose:

### Diagnosis flow

```
Test fails after a structural change
         │
         ▼
Is the test testing internal structure
(private methods, specific call chains,
concrete types) rather than observable behavior?
         │
    YES  │  NO
         │   └──→ The "refactoring" changed observable behavior.
         │         This is a FEATURE CHANGE.
         │         Revert the step.
         │         Put on the feature hat.
         │         Run RED-GREEN-REFACTOR for it explicitly.
         ▼
Rewrite the test to use the public interface.
Re-apply the refactoring step.
Run test-fast — must be green.
```

**Never delete a failing test without diagnosing it first.**

---

## Commit Discipline

Refactoring commits are always **separate** from feature commits.

| Commit type | Message format | When |
|---|---|---|
| Preparatory refactoring | `refactor(<feature-stem>): <what>` | Before RED, to make the feature easier |
| REFACTOR phase | `refactor(<feature-stem>): <what>` | After GREEN, cleaning up the green code |
| Feature addition | `feat(<feature-stem>): <what>` | After GREEN (never mixed with refactor) |

Never mix a structural cleanup with a behavior addition in one commit. This keeps history bisectable and CI green at every commit.

---

## Self-Declaration Check (before exiting REFACTOR)

Before marking the `@id` complete, verify all of the following. Each failed item is a smell — apply the catalogue entry, run `test-fast`, then re-check.

### Green Bar
- [ ] `test-fast` passes
- [ ] No smell from the checklist in Step 1 remains

### Object Calisthenics (Bay 2005)
| Rule | Constraint | Violation signal |
|---|---|---|
| OC-1 | One indent level per method | `for` inside `if` inside a method body |
| OC-2 | No `else` after `return` | `if cond: return x` then `else: return y` |
| OC-3 | Wrap primitives with domain meaning | `def process(user_id: int)` instead of `UserId` |
| OC-4 | Wrap collections with domain meaning | `list[Order]` passed around instead of `OrderCollection` |
| OC-5 | One dot per line | `obj.repo.find(id).name` |
| OC-6 | No abbreviations | `usr`, `mgr`, `cfg`, `val`, `tmp` |
| OC-7 | Classes ≤ 50 lines, methods ≤ 20 lines | Any method requiring scrolling |
| OC-8 | ≤ 2 instance variables per class *(behavioural classes only; dataclasses, Pydantic models, value objects, and TypedDicts are exempt)* | `__init__` with 3+ `self.x =` assignments in a behavioural class |
| OC-9 | No getters/setters | `def get_name(self)` / `def set_name(self, v)` |

### SOLID (Martin 2000)
| Principle | Check |
|---|---|
| **S** — Single Responsibility | Does this class have exactly one reason to change? |
| **O** — Open/Closed | Can new behavior be added without editing this class? |
| **L** — Liskov Substitution | Do all subtypes honor the full contract of their base type? |
| **I** — Interface Segregation | Does every implementor use every method in the Protocol? |
| **D** — Dependency Inversion | Does domain code depend only on Protocols, not concrete I/O? |

#### SOLID Python signals

**S — Single Responsibility**
```python
# WRONG — Report handles both data and formatting
class Report:
    def generate(self) -> dict: ...
    def to_pdf(self) -> bytes: ...    # separate concern
    def to_csv(self) -> str: ...      # separate concern

# RIGHT
class Report:
    def generate(self) -> ReportData: ...

class PdfRenderer:
    def render(self, data: ReportData) -> bytes: ...
```

**O — Open/Closed**
```python
# WRONG — must edit this function to add a new format
def export(data: ReportData, fmt: str) -> bytes:
    if fmt == "pdf": ...
    elif fmt == "csv": ...

# RIGHT — new formats extend without touching existing code
class Exporter(Protocol):
    def export(self, data: ReportData) -> bytes: ...
```

**L — Liskov Substitution**
```python
# WRONG — ReadOnlyFile narrows the contract of File
class ReadOnlyFile(File):
    def write(self, content: str) -> None:
        raise PermissionError  # LSP violation

# RIGHT — separate interfaces
class ReadableFile(Protocol):
    def read(self) -> str: ...

class WritableFile(Protocol):
    def write(self, content: str) -> None: ...
```

**I — Interface Segregation**
```python
# WRONG — Printer forced to implement scan() and fax()
class Machine(Protocol):
    def print(self, doc: Document) -> None: ...
    def scan(self, doc: Document) -> None: ...
    def fax(self, doc: Document) -> None: ...

# RIGHT
class Printer(Protocol):
    def print(self, doc: Document) -> None: ...

class Scanner(Protocol):
    def scan(self, doc: Document) -> None: ...
```

**D — Dependency Inversion**
```python
# WRONG — domain imports infrastructure directly
from app.db import PostgresConnection

class OrderRepository:
    def __init__(self) -> None:
        self.db = PostgresConnection()

# RIGHT — domain defines the Protocol; infra implements it
class OrderRepository(Protocol):
    def find(self, order_id: OrderId) -> Order: ...
    def save(self, order: Order) -> None: ...

class PostgresOrderRepository:      # in adapters/
    def find(self, order_id: OrderId) -> Order: ...
    def save(self, order: Order) -> None: ...
```

### Law of Demeter / Tell, Don't Ask / CQS

**Law of Demeter** — a method should only call methods on: `self`, parameters, objects it creates, direct components (`self.x`).
- Violation signal: `a.b.c()` — two dots. Ask `a` to do the thing instead: `a.do_thing()`.

**Tell, Don't Ask** — tell objects what to do; don't query state and decide externally.
```python
# WRONG
if order.status == OrderStatus.PENDING:
    order.status = OrderStatus.CONFIRMED

# RIGHT
order.confirm()
```

**Command-Query Separation** — a method either changes state (command) or returns a value (query), never both.
- Apply to domain objects. Do not fight stdlib (`list.pop()` is a known violation).

### Python Zen (PEP 20) signals

| Zen item | Code implication |
|---|---|
| Explicit is better than implicit | Explicit return types; explicit Protocol dependencies; no magic |
| Simple is better than complex | One function, one job; prefer a plain function over a class |
| Flat is better than nested | OC-1 — one indent level; early returns |
| Readability counts | OC-6 — no abbreviations; docstrings on every public item |
| Errors should never pass silently | No bare `except:`; no `except Exception: pass` |
| In the face of ambiguity, refuse to guess | Raise on invalid input; never silently return a default |

### Type and docstring hygiene
- [ ] Type hints present on all public signatures
- [ ] Docstrings present on all public classes and methods
