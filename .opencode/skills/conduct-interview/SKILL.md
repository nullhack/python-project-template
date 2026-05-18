---
name: conduct-interview
description: "Interview stakeholders to elicit pain points, business goals, domain terms, and quality attributes"
---

# Conduct Stakeholder Interview

Available knowledge: [[requirements/interview-techniques#key-takeaways]]. `in` artifacts: read all before starting work.

1. Start with general questions per [[requirements/interview-techniques#concepts]].
2. If general questions reveal multiple behaviour groups, probe each as a
   cross-cutting group per [[requirements/interview-techniques#concepts]].
3. If specific features are identified, drill into feature-level questions to
   define feature names and rough boundaries per [[requirements/interview-techniques#concepts]].
4. If a feature candidate spans multiple bounded contexts, flag for splitting per [[requirements/decomposition]].
5. Write confirmation gate before any file writes.
6. Write interview notes to `.cache/interview-notes/IN_YYYYMMDD_<session_id>.md` from the template at `.templates/.cache/interview-notes/IN_YYYYMMDD_<session_id>.md.template`.
