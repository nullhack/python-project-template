---
name: apply-patterns
description: GoF design pattern catalogue — smell triggers and Python before/after examples
version: "2.1"
author: software-engineer
audience: software-engineer
workflow: feature-lifecycle
---

# Design Patterns Reference

Load this skill when the refactor skill's smell table points to a GoF pattern and you need the Python before/after example.

Sources: Gamma, Helm, Johnson, Vlissides. *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley, 1995. See `docs/research/oop-design.md` entry 34.

---

## When to Use

Load this skill when the `refactor` skill's smell table points to a GoF pattern, or when the `implement` skill's Silent Pre-mortem detects a pattern smell in architecture stubs.

## Step-by-Step

1. **Identify the smell** from the refactor skill's lookup table
2. **Find the smell category** below (Creational / Structural / Behavioral)
3. **Read the trigger and the before/after example**
4. **Apply the pattern** — update the stub files (Step 2) or the refactored code (Step 3)

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

**Pattern**: Move Method to the envied class (Fowler refactoring that often precedes Strategy or Command)

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
        EmailService().send_confirmation(self)      # direct coupling
        InventoryService().reserve(self)             # direct coupling
        AnalyticsService().record_conversion(self)   # direct coupling
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

---

## Core Heuristic — Procedural vs OOP

> **When procedural code requires modifying existing functions to add new variants, OOP is the fix.**

Procedural code is open to inspection but open to modification too — every new case touches existing logic.
OOP (via Strategy, State, Observer, etc.) closes existing code to modification and opens it to extension through new types.
The smell is always the same: **a place in the codebase that must change every time the domain grows.**
