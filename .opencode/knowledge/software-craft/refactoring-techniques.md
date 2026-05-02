---
domain: software-craft
tags: [refactoring, fowler, code-quality, refactoring-techniques]
last-updated: 2026-04-30
---

# Refactoring Techniques

## Key Takeaways

- Composing Methods (9 techniques): extract, inline, and substitute to make methods short and focused — Long Method is the most common smell and Extract Method is the most common refactoring (Fowler, 1999).
- Moving Features between Objects (8 techniques): relocate methods and fields to the class where they belong — Feature Envy and Inappropriate Intimacy are resolved by moving behaviour next to the data it depends on.
- Organizing Data (15 techniques): replace primitives with objects, encapsulate fields, and change type codes — Primitive Obsession and Data Clumps are resolved by giving data domain-specific types.
- Simplifying Conditional Expressions (8 techniques): decompose conditionals, replace conditionals with polymorphism, and introduce guard clauses — Switch Statements are resolved by distributing conditional logic to the types that own it.
- Simplifying Method Calls (14 techniques): rename methods, introduce parameter objects, and replace constructors with factory methods — Long Parameter Lists and data class smells are resolved by giving methods clearer interfaces.
- Dealing with Generalization (12 techniques): pull up, push down, extract, and collapse hierarchies — Refused Bequest and Parallel Inheritance Hierarchies are resolved by aligning inheritance with responsibility.

## Concepts

**Composing Methods** — The most fundamental category. Most other refactorings depend on methods being small enough to name clearly. Extract Method is the workhorse: when a method does more than one thing, extract each thing into its own method with a descriptive name. Inline Method is the inverse: when a method body is as clear as its name, inline it. Replace Temp with Query eliminates temporary variables by turning them into query methods.

**Moving Features between Objects** — When a method uses another class's data more than its own (Feature Envy), Move Method relocates it. When a class is doing too much, Extract Class splits it. When a class is doing too little, Inline Class merges it back. Hide Delegate and Remove Middle Man adjust delegation levels.

**Organizing Data** — Primitive Obsession is resolved by wrapping primitives in domain-specific types (Replace Data Value with Object). Type codes are resolved by replacing them with class hierarchies (Replace Type Code with Subclasses) or State/Strategy (Replace Type Code with State/Strategy). Encapsulate Field and Encapsulate Collection protect data from uncontrolled access.

**Simplifying Conditional Expressions** — Switch Statements and nested conditionals are resolved by decomposing them (Decompose Conditional), replacing them with polymorphism (Replace Conditional with Polymorphism), or introducing guard clauses (Replace Nested Conditional with Guard Clauses). Introduce Null Object eliminates null checks by providing a do-nothing implementation.

**Simplifying Method Calls** — Method interfaces are simplified by renaming (Rename Method), reducing parameters (Introduce Parameter Object, Preserve Whole Object), and replacing constructors with factory methods (Replace Constructor with Factory Method). Separate Query from Modifier ensures methods have clear single responsibilities.

**Dealing with Generalization** — Inheritance hierarchies are refined by pulling up common behaviour (Pull Up Method/Field) and pushing down specialised behaviour (Push Down Method/Field). Extract Superclass and Extract Subclass create new levels of abstraction. Replace Inheritance with Delegation converts misapplied inheritance to composition.

## Content

### Composing Methods

| Technique | When to Apply | Mechanics |
|---|---|---|
| Extract Method | Method is too long or needs a comment to understand a section | (1) Create new method with name describing intent (2) Copy extracted code (3) Replace original with call (4) Replace temp variables with parameters (5) Compile and test |
| Inline Method | Method body is as clear as its name; delegation adds no value | (1) Find all callers (2) Replace calls with method body (3) Remove method (4) Compile and test |
| Extract Variable | A complex expression needs a named intermediate result | (1) Declare new variable with descriptive name (2) Assign expression result (3) Replace expression with variable (4) Compile and test |
| Inline Temp | A temporary variable is only used once and its name adds no clarity | (1) Find all references to the temp (2) Replace with the right-hand expression (3) Remove declaration (4) Compile and test |
| Replace Temp with Query | A temporary variable holds the result of an expression used more than once | (1) Extract expression into a method (2) Replace temp with method call (3) Compile and test after each replacement |
| Split Temporary Variable | A variable is assigned more than once and is not a loop counter or collecting variable | (1) Change variable name for second assignment (2) Declare new variable (3) Update references (4) Compile and test |
| Remove Assignments to Parameters | A parameter is reassigned inside the method body | (1) Create local variable (2) Replace parameter assignments with local variable (3) Compile and test |
| Replace Method with Method Object | A long method uses so many local variables that Extract Method is impractical | (1) Create new class with local variables as fields (2) Create constructor taking params and locals (3) Move method body to new class (4) Original method creates object and delegates |
| Substitute Algorithm | A clearer or simpler algorithm replaces a complex one | (1) Prepare tests for existing algorithm (2) Replace body with new algorithm (3) Test — results must be identical |

### Moving Features between Objects

| Technique | When to Apply | Mechanics |
|---|---|---|
| Move Method | A method uses more data from another class than its own (Feature Envy) | (1) Copy method to target class (2) Adjust references — change `self` to source object param if needed (3) Replace body in source with delegation (4) Consider removing delegation later |
| Move Field | A field is used more by another class than its owner | (1) Create field in target class (2) Change all source references to target (3) Remove field from source (4) Compile and test |
| Extract Class | A class has too many responsibilities or instance variables | (1) Create new class (2) Move related fields and methods (3) Create reference from old to new (4) Adjust callers (5) Compile and test |
| Inline Class | A class does too little to justify its existence | (1) Move all features into the host class (2) Remove class (3) Adjust callers (4) Compile and test |
| Hide Delegate | A client calls a delegate through a chain of objects (Message Chains) | (1) Create delegate method on the middle object (2) Change client to call middle object (3) Remove direct delegate access (4) Compile and test |
| Remove Middle Man | A class delegates most methods to another, adding no value | (1) Create getter for delegate in middle man (2) Replace delegation calls with direct delegate access (3) Remove delegation methods (4) Compile and test |
| Introduce Foreign Method | A library class lacks a needed method and cannot be modified | (1) Create method in client class that takes library object as first param (2) Method operates on library object (3) Document as foreign method |
| Introduce Local Extension | A library class needs multiple new methods and cannot be modified | (1) Create subclass or wrapper (2) Add extension methods (3) Use extension where needed (4) Compile and test |

### Organizing Data

| Technique | When to Apply | Mechanics |
|---|---|---|
| Self Encapsulate Field | A class needs to control access to its own field (e.g., for lazy init or validation) | (1) Create getter/setter (2) Replace direct field access with getter/setter inside class (3) Compile and test |
| Replace Data Value with Object | A primitive field has associated behaviour (Primitive Obsession) | (1) Create value class wrapping the primitive (2) Replace field type (3) Move behaviour to value class (4) Compile and test |
| Change Value to Reference | Multiple copies of the same data object exist and should be unified | (1) Create repository/factory for shared objects (2) Replace constructors with lookup (3) Compile and test |
| Change Reference to Value | An object is used as a value and identity comparison is unnecessary | (1) Make object immutable (2) Implement value equality (3) Replace references with copies (4) Compile and test |
| Replace Array with Object | An array is used to hold heterogeneous data that has named fields | (1) Create class with named fields (2) Replace array access with field access (3) Compile and test |
| Duplicate Observed Data | Domain data must be kept in sync with UI data | (1) Make domain class Observable (2) Add Observer to UI (3) Remove direct UI state manipulation (4) Compile and test |
| Change Unidirectional Association to Bidirectional | Two classes need to navigate to each other | (1) Add back-reference (2) Update setters to maintain both sides (3) Compile and test |
| Change Bidirectional Association to Unidirectional | One direction of a bidirectional association is no longer needed | (1) Find all references to the removed direction (2) Replace with alternative navigation (3) Remove field (4) Compile and test |
| Replace Magic Number with Symbolic Constant | A numeric or string literal has a meaning that should be named | (1) Declare constant with descriptive name (2) Replace literal (3) Compile and test |
| Encapsulate Field | A public field needs accessor methods for controlled access | (1) Make field private (2) Create getter/setter (3) Replace direct access (4) Compile and test |
| Encapsulate Collection | A collection field is directly accessible and needs read-only access | (1) Make collection private (2) Create getter returning read-only view or copy (3) Create add/remove methods (4) Compile and test |
| Replace Type Code with Class | A type code is a primitive that should be a domain object | (1) Create class for type code (2) Replace primitive with class (3) Compile and test |
| Replace Type Code with Subclasses | A type code affects behaviour differently per variant | (1) Create subclass per variant (2) Replace type code checks with polymorphism (3) Make superclass abstract (4) Compile and test |
| Replace Type Code with State/Strategy | A type code changes at runtime and affects behaviour | (1) Create state/strategy hierarchy (2) Delegate type-dependent behaviour (3) Replace type code field with state object (4) Compile and test |
| Replace Subclass with Fields | Subclasses differ only in constant data, not behaviour | (1) Add fields to superclass (2) Replace subclass methods with field values (3) Remove subclasses (4) Compile and test |

### Simplifying Conditional Expressions

| Technique | When to Apply | Mechanics |
|---|---|---|
| Decompose Conditional | A complex conditional has complicated condition, then, or else parts | (1) Extract condition into named method (2) Extract then block (3) Extract else block (4) Compile and test |
| Consolidate Conditional Expression | Multiple conditionals lead to the same result | (1) Combine conditions with `and`/`or` (2) Extract combined condition into named method (3) Compile and test |
| Consolidate Duplicate Conditional Fragments | The same code appears in all branches of a conditional | (1) Identify duplicate fragment (2) Move before or after conditional (3) Remove from branches (4) Compile and test |
| Remove Control Flag | A boolean variable controls loop exit instead of using break/return | (1) Find control flag assignments (2) Replace with break or return (3) Remove flag (4) Compile and test |
| Replace Nested Conditional with Guard Clauses | A method has nested if/else that can be replaced with early returns | (1) Identify edge-case conditions (2) Replace with guard clause (early return) (3) Flatten remaining logic (4) Compile and test |
| Replace Conditional with Polymorphism | A conditional switches on a type code or variant (Switch Statements) | (1) Create type hierarchy with common interface (2) Create subclass per variant (3) Move conditional branch to each subclass (4) Replace conditional with polymorphic call (5) Compile and test |
| Introduce Null Object | Repeated null checks appear for the same object | (1) Create null object class implementing same interface (2) Return null object instead of None (3) Remove null checks (4) Compile and test |
| Introduce Assertion | A section of code assumes a condition is true but does not verify it | (1) Add assertion for the assumed condition (2) Keep assertion in development; consider removing in production (3) Compile and test |

### Simplifying Method Calls

| Technique | When to Apply | Mechanics |
|---|---|---|
| Rename Method | Method name does not communicate its purpose | (1) Check all callers (2) Create new method with better name (3) Copy body (4) Change callers (5) Remove old method (6) Compile and test |
| Add Parameter | A method needs additional information from its caller | (1) Add parameter to signature (2) Update all callers (3) Compile and test |
| Remove Parameter | A parameter is no longer used by the method body | (1) Verify parameter unused (2) Remove from signature (3) Update all callers (4) Compile and test |
| Separate Query from Modifier | A method both returns a value and modifies state | (1) Create query method returning value (2) Modify original to only modify state (3) Update callers to use both (4) Compile and test |
| Parameterize Method | Several methods do similar things with different numeric values | (1) Create parameterized method (2) Replace each variant with call passing value (3) Remove variants (4) Compile and test |
| Replace Parameter with Explicit Methods | A method branches on a parameter value to do different things | (1) Create method per parameter value (2) Replace calls with specific method (3) Remove parameter (4) Compile and test |
| Preserve Whole Object | A method receives multiple values from the same object as separate parameters | (1) Replace parameters with single object parameter (2) Update method body to access fields (3) Compile and test |
| Replace Parameter with Method Call | A parameter is obtained by asking another object for data | (1) Remove parameter (2) Add method call inside method body (3) Update callers (4) Compile and test |
| Introduce Parameter Object | A group of parameters naturally belong together (Data Clumps) | (1) Create value class for parameter group (2) Replace parameters with single object (3) Update callers (4) Compile and test |
| Remove Setting Method | A field should not be changed after construction | (1) Remove setter (2) Verify all callers only set in constructor (3) Make field final/read-only (4) Compile and test |
| Hide Method | A method is not used by other classes | (1) Change visibility to private (2) Compile and test |
| Replace Constructor with Factory Method | Object creation needs to be delegated to a subclass or needs complex logic | (1) Create factory method (2) Replace constructor calls with factory calls (3) Consider making constructor private (4) Compile and test |
| Replace Error Code with Exception | A method returns a special value to indicate an error | (1) Define exception class (2) Replace return with raise (3) Update callers to catch (4) Compile and test |
| Replace Exception with Test | An exception is used for a condition that can be checked with a conditional | (1) Add condition check before operation (2) Replace try/except with conditional (3) Compile and test |

### Dealing with Generalization

| Technique | When to Apply | Mechanics |
|---|---|---|
| Pull Up Field | Subclasses have the same field | (1) Add field to superclass (2) Remove from subclasses (3) Compile and test |
| Pull Up Method | Subclasses have methods with identical results | (1) Copy method to superclass (2) Remove from subclasses (3) Compile and test |
| Pull Up Constructor Body | Subclass constructors have identical setup code | (1) Create superclass constructor with common code (2) Call from subclass constructors (3) Compile and test |
| Push Down Method | A superclass method is relevant only to some subclasses | (1) Copy method to relevant subclasses (2) Remove from superclass (3) Compile and test |
| Push Down Field | A superclass field is relevant only to some subclasses | (1) Copy field to relevant subclasses (2) Remove from superclass (3) Compile and test |
| Extract Subclass | A class has features that apply only in some cases | (1) Create subclass (2) Move case-specific fields and methods (3) Replace type flags with type checks or polymorphism (4) Compile and test |
| Extract Superclass | Two classes have similar features | (1) Create superclass (2) Move common fields and methods up (3) Make classes extend superclass (4) Compile and test |
| Extract Interface | Multiple clients use the same subset of a class's interface | (1) Define Protocol/interface with the common methods (2) Make class implement it (3) Change client references to interface type (4) Compile and test |
| Collapse Hierarchy | A superclass and subclass are no longer meaningfully different | (1) Merge subclass fields and methods into superclass (2) Remove subclass (3) Update callers (4) Compile and test |
| Form Template Method | Two methods in subclasses have similar structure | (1) Decompose methods into steps (2) Pull identical steps to superclass (3) Define template method calling steps (4) Make varying steps abstract (5) Compile and test |
| Replace Inheritance with Delegation | A subclass uses only part of a superclass's interface | (1) Create field holding superclass instance (2) Change methods to delegate (3) Remove inheritance (4) Compile and test |
| Replace Delegation with Inheritance | A class delegates all methods to another and could inherit instead | (1) Make class inherit from delegate (2) Remove delegation methods (3) Remove delegate field (4) Compile and test |

## Related

- [[software-craft/smell-catalogue]] — each smell maps to specific refactoring techniques
- [[software-craft/design-patterns]] — patterns are applied when refactoring techniques are insufficient
- [[software-craft/refactoring]] — when and how to refactor, clean code, technical debt
- [[software-craft/tdd]] — refactoring techniques are applied during REFACTOR phase
- [[software-craft/object-calisthenics]] — Object Calisthenics violations signal specific refactoring opportunities
- [[software-craft/solid]] — SOLID violations are resolved by specific refactoring techniques
