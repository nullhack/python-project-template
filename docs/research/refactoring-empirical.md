# Scientific Research — Refactoring (Empirical)

Empirical studies on code smells, refactoring prioritization, and OOP complexity used in this template.

---

### 36. QDIR — Bad-Smells + OO Metrics Prioritization

| | |
|---|---|
| **Source** | Malhotra, R., Singh, P. (2020). "Exploiting bad-smells and object-oriented characteristics to prioritize classes for refactoring." *Int. J. Syst. Assur. Eng. Manag.* 11(Suppl 2), 133–144. Springer. |
| **Date** | 2020 |
| **URL** | https://doi.org/10.1007/s13198-020-01001-x |
| **Status** | Confirmed — empirical |
| **Core finding** | QDIR (Quality Depreciation Index Rule) combines bad-smell severity with OO metrics (LOC, WMC, CBO, RFC, DIT) to prioritize classes for refactoring. Validated on 8 open-source Java systems. |
| **Mechanism** | Classes with high smell severity AND high OO metrics are prioritized. QDIR = weighted sum. |
| **Where used** | Refactor prioritization: when smell detected, check OO metrics to prioritize. |

---

### 37. Smells + Architectural Refactoring

| | |
|---|---|
| **Source** | Silva, C. et al. (2020). "When Are Smells Indicators of Architectural Refactoring Opportunities." *Proc. 28th Int. Conf. on Program Comprehension*. ACM. |
| **Date** | 2020 |
| **URL** | https://doi.org/10.1145/3387904.3389276 |
| **Status** | Confirmed — empirical |
| **Core finding** | Study of 50 projects, 52,667 refactored elements. 67.53% of smells co-occur. Smells that co-occur are indicators of architectural refactoring in 88.53% of cases. |
| **Mechanism** | Single smells are often code-level; co-occurring smells indicate architectural problems. Pattern catalogue for smells → specific architectural refactorings. |
| **Where used** | Smell detection triggers architectural analysis when co-occurrence patterns detected. |

---

### 38. SPIRIT Tool — Code Smell Prioritization

| | |
|---|---|
| **Source** | Vidal, S. A., Marcos, C., Díaz-Pace, J. A. (2014). "An Approach to Prioritize Code Smells for Refactoring." *Automated Software Engineering*, 23(3), 501–532. |
| **Date** | 2014 |
| **URL** | https://doi.org/10.1007/s10515-014-0175-x |
| **Status** | Confirmed — tool |
| **Core finding** | SPIRIT (Smart Identification of Refactoring opportunITies) prioritizes smells by 3 criteria: (1) component stability, (2) impact on modifiability scenarios, (3) smell relevance. Top-ranked smells correlate with expert developer judgment. |
| **Mechanism** | Semi-automated ranking. Combines version history (stable vs. unstable), impact analysis, and smell type. |
| **Where used** | Refactor prioritization: stability = has the class changed recently? Unstable + smelly = prioritize. |

---

### 39. Bad Engineering Properties of OOP

| | |
|---|---|
| **Source** | Cardelli, L. (1996). "Bad Engineering Properties of Object-Oriented Languages." *ACM Computing Surveys*, 28(4), 150. |
| **Date** | 1996 |
| **URL** | https://www.microsoft.com/en-us/research/publication/bad-engineering-properties-of-object-oriented-languages/ |
| **Status** | Confirmed — foundational critique |
| **Core finding** | OOP has 5 "economy" problems: (1) Execution (virtual methods prevent inlining), (2) Compilation (no code/interface separation), (3) Small-scale dev (expressive type systems missing), (4) Large-scale dev (poor class extension/modification), (5) Language features (baroque complexity). |
| **Mechanism** | OOP is not universally superior. Trade-offs exist. Knowing these helps avoid over-engineering. |
| **Where used** | Anti-pre-pattern: know when OOP adds complexity vs. value. |

---

### 40. Code Complexity Model of OOP

| | |
|---|---|
| **Source** | Aluthwaththage, J. H., Thathsarani, H. A. N. N. (2024). "A Novel OO-Based Code Complexity Metric." *Proc. Future Technologies Conference (FTC)*, 616–628. Springer/IEEE. |
| **Date** | 2024 |
| **URL** | https://link.springer.com/chapter/10.1007/978-3-031-73125-9_39 |
| **Alternative** | Misra et al. (2024). "A Suite of Object Oriented Cognitive Complexity Metrics." IEEE. |
| **Status** | Partially confirmed — recent |
| **Core finding** | CWC (Combined Weighted Complexity) measures OOP complexity at statement level, considering 8 factors: nesting depth, control types, compound conditions, try-catch, threads, pointers, references, dynamic memory. Addresses gap in existing metrics ignoring cognitive load. |
| **Mechanism** | Granular complexity scoring. Higher scores indicate more cognitively demanding code. |
| **Where used** | Complexity measurement: when function > 20 lines, consider CWC-style granular scoring. |

---

### 41. Metric Thresholds for Smell Detection

| | |
|---|---|
| **Source** | Bigonha, M. A. S., et al. (2019). "The usefulness of software metric thresholds for detection of bad smells and fault prediction." *Information and Software Technology*, 115, 79–92. |
| **Date** | 2019 |
| **URL** | https://doi.org/10.1016/j.infsof.2019.08.005 |
| **Alternative** | Catal et al. (2018). "Software metrics thresholds calculation techniques." *Info. Softw. Technol.* |
| **Status** | Confirmed |
| **Core finding** | Metric thresholds (e.g., LOC > 600) used for smell detection are unreliable. Study on 92 open-source systems found precision too low for practical use. Neither heuristic-based nor ML approaches achieve acceptable accuracy. |
| **Mechanism** | Fixed thresholds are context-dependent. Thresholds should be project-specific, not universal. |
| **Where used** | Anti-pre-pattern: do not rely on fixed thresholds. Use co-occurrence patterns (entry 37) instead. |

---

## Bibliography

1. Aluthwaththage, J. H., & Thathsarani, H. A. N. N. (2024). A Novel OO-Based Code Complexity Metric. *Proc. Future Technologies Conference (FTC)*, 616–628. https://link.springer.com/chapter/10.1007/978-3-031-73125-9_39
2. Bigonha, M. A. S., et al. (2019). The usefulness of software metric thresholds. *Information and Software Technology*, 115, 79–92. https://doi.org/10.1016/j.infsof.2019.08.005
3. Cardelli, L. (1996). Bad Engineering Properties of Object-Oriented Languages. *ACM Computing Surveys*, 28(4), 150. https://www.microsoft.com/en-us/research/publication/bad-engineering-properties-of-object-oriented-languages/
4. Malhotra, R., & Singh, P. (2020). Exploiting bad-smells and OO characteristics. *Int. J. Syst. Assur. Eng. Manag.*, 11(Suppl 2), 133–144. https://doi.org/10.1007/s13198-020-01001-x
5. Silva, C. et al. (2020). When Are Smells Indicators of Architectural Refactoring Opportunities. *Proc. 28th ICPC*. https://doi.org/10.1145/3387904.3389276
6. Vidal, S. A., Marcos, C., & Díaz-Pace, J. A. (2014). An Approach to Prioritize Code Smells. *Automated Software Engineering*, 23(3), 501–532. https://doi.org/10.1007/s10515-014-0175-x
