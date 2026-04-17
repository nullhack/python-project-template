---
name: design-patterns
description: Reference skill for GoF design patterns, SOLID, Object Calisthenics, Python Zen, and other SE principles — with smell triggers and Python before/after examples
version: "1.0"
author: developer
audience: developer
workflow: feature-lifecycle
---

# Design Patterns Reference

Load this skill when:
- Running the architecture smell check in Step 2 and a smell is detected
- Refactoring in Step 4 and a pattern smell appears in the self-declaration

---

## How to Use This Skill

1. **Identify the smell** from the checklist in your self-declaration or architecture check
2. **Find the smell category** below (Creational / Structural / Behavioral)
3. **Read the trigger and the before/after example**
4. **Apply the pattern** and update the Architecture section (Step 2) or the refactored code (Step 4)

---

## GoF Pattern Catalogue — One-Liner Reference

### Creational
| Pattern | Intent |
|---|---|
| **Factory Method** | Delegate object creation to a subclass or factory function |
| **Abstract Factory** | Create families of related objects without specifying concrete classes |
| **Builder** | Construct complex objects step-by-step, separating construction from representation |
| **Prototype** | Clone existing objects instead of creating new ones from scratch |
| **Singleton** | Ensure a class has only one instance (use sparingly — prefer dependency injection) |

### Structural
| Pattern | Intent |
|---|---|
| **Adapter** | Wrap an incompatible interface to match an expected interface |
| **Bridge** | Separate abstraction from implementation so both can vary independently |
| **Composite** | Treat individual objects and compositions uniformly via a shared interface |
| **Decorator** | Add responsibilities to an object dynamically without subclassing |
| **Facade** | Provide a simplified interface to a complex subsystem |
| **Flyweight** | Share fine-grained objects to reduce memory when many similar instances are needed |
| **Proxy** | Control access to an object via a surrogate (lazy init, access control, logging) |

### Behavioral
| Pattern | Intent |
|---|---|
| **Chain of Responsibility** | Pass a request along a chain of handlers until one handles it |
| **Command** | Encapsulate a request as an object, enabling undo/redo and queuing |
| **Interpreter** | Define a grammar and an interpreter for a language |
| **Iterator** | Provide sequential access to elements without exposing the underlying structure |
| **Mediator** | Centralize complex communication between objects through a mediator object |
| **Memento** | Capture and restore object state without violating encapsulation |
| **Observer** | Define a one-to-many dependency so dependents are notified automatically |
| **State** | Allow an object to alter its behavior when its internal state changes |
| **Strategy** | Define a family of algorithms, encapsulate each, and make them interchangeable |
| **Template Method** | Define the skeleton of an algorithm; let subclasses fill in specific steps |
| **Visitor** | Separate an algorithm from the object structure it operates on |

---

## Smell-Triggered Patterns — Python Examples

### Creational Smells

---

#### Smell: Scattered Object Construction
**Signal**: The same object is constructed in 3+ places with slightly different arguments, or construction logic is duplicated across callers.

**Pattern**: Factory Method or Factory Function

```python
# BEFORE — scattered construction
# in order_service.py
order = Order(id=uuid4(), status="pending", created_at=datetime.now())

# in test_order.py
order = Order(id=UUID("abc..."), status="pending", created_at=datetime(2026, 1, 1))

# in import_service.py
order = Order(id=uuid4(), status="pending", created_at=datetime.now())
```

```python
# AFTER — factory function owns construction
def make_order(
    *,
    order_id: OrderId | None = None,
    clock: Callable[[], datetime] = datetime.now,
) -> Order:
    return Order(
        id=order_id or OrderId(uuid4()),
        status=OrderStatus.PENDING,
        created_at=clock(),
    )
```

---

#### Smell: Multi-Step Construction with Optional Parts
**Signal**: An object requires several setup calls before it is valid. Callers must remember the correct sequence.

**Pattern**: Builder

```python
# BEFORE — callers must know the correct build sequence
report = Report()
report.set_title("Q4 Sales")
report.add_section(summary)
report.add_section(detail)
report.set_footer("Confidential")
# easy to forget a step or get the order wrong
```

```python
# AFTER — builder enforces sequence and provides defaults
report = (
    ReportBuilder("Q4 Sales")
    .with_section(summary)
    .with_section(detail)
    .with_footer("Confidential")
    .build()
)
```

---

### Structural Smells

---

#### Smell: Type-Switching (if/elif on type or status)
**Signal**: A function or method contains `if isinstance(x, A): ... elif isinstance(x, B): ...` or `if x.type == "a": ... elif x.type == "b": ...`. Adding a new type requires editing this function.

**Pattern**: Strategy (behavior varies) or Visitor (operation varies over a fixed structure)

```python
# BEFORE — type switch must be updated for every new discount type
def apply_discount(order: Order, discount_type: str) -> Money:
    if discount_type == "percentage":
        return order.total * (1 - order.rate)
    elif discount_type == "fixed":
        return order.total - order.amount
    elif discount_type == "bogo":
        return order.total - (order.total / 2)
    else:
        raise ValueError(discount_type)
```

```python
# AFTER — Strategy: each discount is a callable, closed to modification
class DiscountStrategy(Protocol):
    def apply(self, order: Order) -> Money: ...

@dataclass
class PercentageDiscount:
    rate: Decimal
    def apply(self, order: Order) -> Money:
        return order.total * (1 - self.rate)

@dataclass
class FixedDiscount:
    amount: Money
    def apply(self, order: Order) -> Money:
        return order.total - self.amount

def apply_discount(order: Order, strategy: DiscountStrategy) -> Money:
    return strategy.apply(order)
```

---

#### Smell: Feature Envy
**Signal**: A method in class A uses data from class B more than its own data. The method "envies" class B.

**Pattern**: Move Method to the envied class (not a GoF pattern — a Fowler refactoring that often precedes Strategy or Command)

```python
# BEFORE — OrderPrinter knows too much about Order internals
class OrderPrinter:
    def format_total(self, order: Order) -> str:
        subtotal = sum(item.price * item.quantity for item in order.items)
        tax = subtotal * order.tax_rate
        return f"{subtotal + tax:.2f}"
```

```python
# AFTER — total belongs on Order
@dataclass
class Order:
    items: list[LineItem]
    tax_rate: Decimal

    def total(self) -> Money:
        subtotal = sum(item.subtotal() for item in self.items)
        return subtotal * (1 + self.tax_rate)

class OrderPrinter:
    def format_total(self, order: Order) -> str:
        return f"{order.total():.2f}"
```

---

#### Smell: Parallel Inheritance Hierarchies
**Signal**: Every time you add a subclass to hierarchy A, you must also add a corresponding subclass to hierarchy B. The two trees grow in lockstep.

**Pattern**: Bridge

```python
# BEFORE — adding a new Shape requires a new renderer subclass too
class Shape: ...
class Circle(Shape): ...
class Square(Shape): ...

class SVGCircle(Circle): ...
class SVGSquare(Square): ...
class PNGCircle(Circle): ...
class PNGSquare(Square): ...
```

```python
# AFTER — Bridge separates shape from renderer
class Renderer(Protocol):
    def render_circle(self, radius: float) -> None: ...
    def render_square(self, side: float) -> None: ...

@dataclass
class Circle:
    radius: float
    renderer: Renderer
    def draw(self) -> None:
        self.renderer.render_circle(self.radius)

@dataclass
class Square:
    side: float
    renderer: Renderer
    def draw(self) -> None:
        self.renderer.render_square(self.side)
```

---

### Behavioral Smells

---

#### Smell: Large State Machine in One Class
**Signal**: A class has a `status` or `state` field, and many methods begin with `if self.state == X: ... elif self.state == Y: ...`. Adding a new state requires editing all these methods.

**Pattern**: State

```python
# BEFORE — Order methods all branch on status
class Order:
    def confirm(self) -> None:
        if self.status == "pending":
            self.status = "confirmed"
        else:
            raise InvalidTransition(self.status, "confirm")

    def ship(self) -> None:
        if self.status == "confirmed":
            self.status = "shipped"
        else:
            raise InvalidTransition(self.status, "ship")
```

```python
# AFTER — each state owns its own transitions
class OrderState(Protocol):
    def confirm(self, order: Order) -> None: ...
    def ship(self, order: Order) -> None: ...

class PendingState:
    def confirm(self, order: Order) -> None:
        order.state = ConfirmedState()
    def ship(self, order: Order) -> None:
        raise InvalidTransition("pending", "ship")

class ConfirmedState:
    def confirm(self, order: Order) -> None:
        raise InvalidTransition("confirmed", "confirm")
    def ship(self, order: Order) -> None:
        order.state = ShippedState()

@dataclass
class Order:
    state: OrderState = field(default_factory=PendingState)
    def confirm(self) -> None: self.state.confirm(self)
    def ship(self) -> None: self.state.ship(self)
```

---

#### Smell: Scattered Notification / Event Fan-Out
**Signal**: When something happens in class A, it directly calls methods on classes B, C, and D. Adding a new listener requires modifying class A.

**Pattern**: Observer

```python
# BEFORE — Order directly notifies every downstream system
class Order:
    def confirm(self) -> None:
        self.status = "confirmed"
        EmailService().send_confirmation(self)     # direct coupling
        InventoryService().reserve(self)            # direct coupling
        AnalyticsService().record_conversion(self)  # direct coupling
```

```python
# AFTER — Order emits an event; listeners register independently
class OrderConfirmedListener(Protocol):
    def on_order_confirmed(self, order: Order) -> None: ...

@dataclass
class Order:
    _listeners: list[OrderConfirmedListener] = field(default_factory=list)

    def add_listener(self, listener: OrderConfirmedListener) -> None:
        self._listeners.append(listener)

    def confirm(self) -> None:
        self.status = OrderStatus.CONFIRMED
        for listener in self._listeners:
            listener.on_order_confirmed(self)
```

---

#### Smell: Repeated Algorithm Skeleton
**Signal**: Two or more functions share the same high-level structure (setup → process → teardown) but differ only in one or two steps. The structure is copied rather than shared.

**Pattern**: Template Method

```python
# BEFORE — CSV and JSON importers duplicate the pipeline structure
def import_csv(path: Path) -> list[Record]:
    raw = path.read_text()
    rows = parse_csv(raw)        # varies
    records = [validate(r) for r in rows]
    save_all(records)
    return records

def import_json(path: Path) -> list[Record]:
    raw = path.read_text()
    rows = parse_json(raw)       # varies
    records = [validate(r) for r in rows]
    save_all(records)
    return records
```

```python
# AFTER — Template Method: skeleton in base, varying step overridden
class Importer(ABC):
    def run(self, path: Path) -> list[Record]:
        raw = path.read_text()
        rows = self.parse(raw)          # hook
        records = [validate(r) for r in rows]
        save_all(records)
        return records

    @abstractmethod
    def parse(self, raw: str) -> list[dict]: ...

class CsvImporter(Importer):
    def parse(self, raw: str) -> list[dict]:
        return parse_csv(raw)

class JsonImporter(Importer):
    def parse(self, raw: str) -> list[dict]:
        return parse_json(raw)
```

---

## SOLID — Python Examples

### S — Single Responsibility
One class, one reason to change.

```python
# WRONG — Report handles both data and formatting
class Report:
    def generate(self) -> dict: ...
    def to_pdf(self) -> bytes: ...    # separate concern
    def to_csv(self) -> str: ...      # separate concern

# RIGHT — split concerns
class Report:
    def generate(self) -> ReportData: ...

class PdfRenderer:
    def render(self, data: ReportData) -> bytes: ...
```

### O — Open/Closed
Open for extension, closed for modification.

```python
# WRONG — must edit this function to add a new format
def export(data: ReportData, fmt: str) -> bytes:
    if fmt == "pdf": ...
    elif fmt == "csv": ...

# RIGHT — new formats extend without touching existing code
class Exporter(Protocol):
    def export(self, data: ReportData) -> bytes: ...

class PdfExporter:
    def export(self, data: ReportData) -> bytes: ...
```

### L — Liskov Substitution
Subtypes must be fully substitutable for their base type.

```python
# WRONG — ReadOnlyFile violates the contract of File
class File:
    def write(self, content: str) -> None: ...

class ReadOnlyFile(File):
    def write(self, content: str) -> None:
        raise PermissionError  # narrows the contract — LSP violation

# RIGHT — separate interfaces for readable and writable
class ReadableFile(Protocol):
    def read(self) -> str: ...

class WritableFile(Protocol):
    def write(self, content: str) -> None: ...
```

### I — Interface Segregation
No implementor should be forced to implement methods it doesn't use.

```python
# WRONG — Printer is forced to implement scan() and fax()
class Machine(Protocol):
    def print(self, doc: Document) -> None: ...
    def scan(self, doc: Document) -> None: ...
    def fax(self, doc: Document) -> None: ...

# RIGHT — each capability is its own Protocol
class Printer(Protocol):
    def print(self, doc: Document) -> None: ...

class Scanner(Protocol):
    def scan(self, doc: Document) -> None: ...
```

### D — Dependency Inversion
Domain depends on abstractions (Protocols), not on concrete I/O or frameworks.

```python
# WRONG — domain imports infrastructure directly
from app.db import PostgresConnection

class OrderRepository:
    def __init__(self) -> None:
        self.db = PostgresConnection()  # domain imports infra

# RIGHT — domain defines the Protocol; infra implements it
class OrderRepository(Protocol):
    def find(self, order_id: OrderId) -> Order: ...
    def save(self, order: Order) -> None: ...

class PostgresOrderRepository:      # in adapters/
    def find(self, order_id: OrderId) -> Order: ...
    def save(self, order: Order) -> None: ...
```

---

## Object Calisthenics — Python Rules

Jeff Bay's 9 rules for object-oriented discipline. Each has a Python signal.

| Rule | Constraint | Python Signal of Violation |
|---|---|---|
| **OC-1** | One indent level per method | `for` inside `if` inside a method body |
| **OC-2** | No `else` after `return` | `if cond: return x \n else: return y` |
| **OC-3** | Wrap all primitives that have domain meaning | `def process(user_id: int)` instead of `def process(user_id: UserId)` |
| **OC-4** | Wrap all collections that have domain meaning | `list[Order]` passed around instead of `OrderCollection` |
| **OC-5** | One dot per line | `obj.repo.find(id).name` |
| **OC-6** | No abbreviations | `usr`, `mgr`, `cfg`, `val`, `tmp` |
| **OC-7** | Keep classes small (≤50 lines) and methods short (≤20 lines) | Any method requiring scrolling |
| **OC-8** | No class with more than 2 instance variables | `__init__` with 3+ `self.x =` assignments |
| **OC-9** | No getters/setters | `def get_name(self)` / `def set_name(self, v)` |

---

## Python Zen — Mapped to Code Practices

The relevant items from PEP 20 (`import this`) with concrete code implications:

| Zen Item | Code Practice |
|---|---|
| Beautiful is better than ugly | Name things clearly; prefer named types over bare primitives |
| Explicit is better than implicit | Explicit return types; explicit Protocol dependencies; no magic |
| Simple is better than complex | KISS — one function, one job; prefer a plain function over a class |
| Complex is better than complicated | A well-designed abstraction is acceptable; an accidental tangle is not |
| Flat is better than nested | OC-1 — one indent level; early returns |
| Sparse is better than dense | One statement per line; no semicolons; no lambda chains |
| Readability counts | OC-6 — no abbreviations; docstrings on every public function |
| Special cases aren't special enough to break the rules | Do not add `if isinstance` branches to avoid refactoring |
| Errors should never pass silently | No bare `except:`; no `except Exception: pass` |
| In the face of ambiguity, refuse the temptation to guess | Raise on invalid input; never silently return a default |
| There should be one obvious way to do it | DRY — every shared concept in exactly one place |
| If the implementation is hard to explain, it's a bad idea | KISS — if you can't describe the function in one sentence, split it |

---

## Other Principles

### Law of Demeter (Tell, Don't Ask)
A method should only call methods on:
- `self`
- Objects passed as parameters
- Objects it creates
- Direct component objects (`self.x`)

**Violation signal**: `a.b.c()` — two dots. Assign `b = a.b` and call `b.c()`, or better: ask `a` to do what you need (`a.do_thing()`).

### Command-Query Separation (CQS)
A method either **changes state** (command) or **returns a value** (query) — never both.

```python
# WRONG — pop() both returns and mutates
value = stack.pop()

# RIGHT (CQS strict)
value = stack.peek()   # query — no mutation
stack.remove_top()     # command — no return value
```

Note: Python's standard library violates CQS in places (`list.pop()`, `dict.update()`). Apply CQS to your domain objects; do not fight the stdlib.

### Tell, Don't Ask
Instead of querying an object's state and acting on it externally, tell the object to do the work itself.

```python
# WRONG — ask state, decide externally
if order.status == OrderStatus.PENDING:
    order.status = OrderStatus.CONFIRMED

# RIGHT — tell the object
order.confirm()   # Order decides if the transition is valid
```

---

## Quick Smell → Pattern Lookup

| Smell | Pattern |
|---|---|
| Same object constructed in 3+ places | Factory Method / Factory Function |
| Multi-step setup before object is valid | Builder |
| `if type == X: ... elif type == Y:` | Strategy |
| Method uses another class's data more than its own | Move Method (Fowler) |
| Two class hierarchies that grow in lockstep | Bridge |
| `if self.state == X:` in multiple methods | State |
| Class directly calls B, C, D on state change | Observer |
| Two functions share the same skeleton, differ in one step | Template Method |
| Subsystem is complex and callers need a simple entry point | Facade |
| Object needs logging/caching without changing its class | Decorator / Proxy |
