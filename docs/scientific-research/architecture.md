# Scientific Research — Architecture

Foundations for the architectural decisions and patterns used in this template.

---

### 42. Hexagonal Architecture — Ports and Adapters

| | |
|---|---|
| **Source** | Cockburn, A. (2005). "Hexagonal Architecture." *alistair.cockburn.us*. https://alistair.cockburn.us/hexagonal-architecture/ |
| **Date** | 2005 |
| **Alternative** | Freeman, S., & Pryce, N. (2009). *Growing Object-Oriented Software, Guided by Tests*. Addison-Wesley. (Chapter 7: "Ports and Adapters") |
| **Status** | Confirmed — foundational; widely adopted as Clean Architecture, Onion Architecture |
| **Core finding** | The application domain should have no knowledge of external systems (databases, filesystems, network, UI). All contact between the domain and the outside world passes through a **port** (an interface / Protocol) and an **adapter** (a concrete implementation of that port). The domain is independently testable without any infrastructure. The key structural rule: dependency arrows point inward — domain code never imports from adapters; adapters import from domain. |
| **Mechanism** | Two distinct sides of any application: the "driving side" (actors who initiate action — tests, UI, CLI) and the "driven side" (actors the application drives — databases, filesystems, external services). Each driven-side dependency is hidden behind a port. Tests supply a test adapter; production supplies a real adapter. Substituting adapters requires no domain code changes. This is SOLID-D at the architectural layer. |
| **Where used** | Step 2 (Architecture): if an external dependency is identified during domain analysis, assign it a Protocol. `ports/` and `adapters/` folders emerge when a concrete dependency is confirmed — do not pre-create them. The dependency-inversion principle (SOLID-D) is the goal; the folder names are convention, not law. |

---

## Bibliography

1. Cockburn, A. (2005). Hexagonal Architecture. *alistair.cockburn.us*. https://alistair.cockburn.us/hexagonal-architecture/
2. Freeman, S., & Pryce, N. (2009). *Growing Object-Oriented Software, Guided by Tests*. Addison-Wesley.
