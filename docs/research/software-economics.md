# Scientific Research — Software Economics

Foundations for the shift-left, early defect detection, and workflow ordering decisions in this template.

---

### 16. Cost of Change Curve (Shift Left)

| | |
|---|---|
| **Source** | Boehm, B. W. (1981). *Software Engineering Economics*. Prentice-Hall. |
| **Date** | 1981 |
| **Alternative** | Boehm, B., & Papaccio, P. N. (1988). Understanding and controlling software costs. *IEEE Transactions on Software Engineering*, 14(10), 1462–1477. |
| **Status** | Confirmed |
| **Core finding** | The cost to fix a defect multiplies by roughly 10x per SDLC phase: requirements (1x) → design (5x) → coding (10x) → testing (20x) → production (200x). A defect caught during requirements costs 200x less than the same defect found after release. |
| **Mechanism** | Defects compound downstream: a wrong requirement becomes a wrong design, which becomes wrong code, which becomes wrong tests, all of which must be unwound. Catching errors at the source eliminates the entire cascade. This is the empirical foundation for "shift left" — investing earlier in quality always dominates fixing later. |
| **Where used** | Justifies the multi-session PO elicitation model: every acceptance criterion clarified at scope prevents 10–200x rework downstream. Also justifies the adversarial pre-mortem at the end of each elicitation cycle, and the adversarial mandate in `verify/SKILL.md`. The entire 5-step pipeline is ordered to surface defects at the earliest (cheapest) phase. |

---

## Bibliography

1. Boehm, B. W. (1981). *Software Engineering Economics*. Prentice-Hall.
2. Boehm, B., & Papaccio, P. N. (1988). Understanding and controlling software costs. *IEEE Transactions on Software Engineering*, 14(10), 1462–1477.
