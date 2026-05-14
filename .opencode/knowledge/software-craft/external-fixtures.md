---
domain: software-craft
tags: [fixtures, external-adapters, mocking, real-data, api-fixtures]
last-updated: 2026-05-14
---

# External Adapter Fixtures

## Key Takeaways

- Domains dependent on external adapters or APIs must mock with real captured output, not imagined data. Real fixtures close the gap between test expectations and production behaviour.
- Capture real API responses once (call the API or ask the stakeholder to call and provide the response), then store as JSON in `tests/fixtures/<service_name>/`.
- Fixture files are frozen once captured. If the API changes, capture a new fixture (new file) and deprecate the old one. Never edit an existing fixture to make a test pass.
- Fixtures must exist BEFORE write-test for any feature touching an external adapter. This is a flow gate: no test implementation without real fixture data.

## Concepts

**Why Real Fixtures**: Imagining what an external API returns introduces a systematic bias: tests verify against what the developer thinks the API does, not what it actually does. Real fixtures anchor tests to observable truth. When the real response surprises (extra fields, unexpected nesting, different types), the fixture captures that surprise before it becomes a production incident.

**Capture Process**: For each External Contract in the domain spec:
1. Identify the external service and endpoint/operation from the domain spec's External Contracts section.
2. Call the API once (automated script, curl, or ask the stakeholder to call and provide the response).
3. Store the full HTTP response as JSON in `tests/fixtures/<service_name>/<endpoint_or_operation>.json`.
4. Document the fixture: capture date, API version, authentication scope, and any stakeholder notes in a comment block at the top of the JSON file or in an adjacent `README.md`.

**Storage Convention**:
- Directory: `tests/fixtures/<service_name>/`
- File: `<endpoint_or_operation>.json` (snake_case)
- Each fixture file is a single real response (or a minimal set: success response, error response)
- A `README.md` in each service directory documents: capture date, API version, authentication scope used, and any caveats

**Fixture Lifecycle**:
- **Frozen once captured**: fixtures are immutable after creation, like Examples after criteria commit.
- **Deprecation on API change**: if the external API changes, capture a new fixture (new file) and update tests to reference it. Add the old fixture filename to a `# Deprecated fixtures:` section in the README.
- **Never edit to fix tests**: if a test fails because the fixture doesn't match expectations, the fixture is correct (it's real data). The code or the spec is wrong. Fix the code, not the fixture.

**Usage in Tests**: Load via `conftest.py` fixtures:

```python
import json
from pathlib import Path

import pytest

@pytest.fixture
def payment_service_charge_response():
    path = Path("tests/fixtures/payment_service/charge.json")
    return json.loads(path.read_text(encoding="utf-8"))
```

Tests use these as mock return values for adapter ports. The adapter Protocol is what gets mocked; the fixture provides the data.

**Precondition Gate**: Before any test implementation for a feature that touches an external adapter, the fixture must already exist in `tests/fixtures/`. If the fixture is missing, the write-test step must flag this as a blocker and request fixture capture. This prevents tests from being written against imagined data.

## Content

### When Real Fixtures Are Required

Real fixtures are required when the domain spec's External Contracts section defines integration with an external system. This includes:
- Third-party APIs (payment processors, email services, analytics platforms)
- External databases or message queues not owned by the bounded context
- File-based integrations (CSV uploads, SFTP drops)
- Any port/adapter boundary where the domain depends on an external contract

### When Real Fixtures Are NOT Required

- Pure domain logic with no external dependencies
- Internal bounded context boundaries (these are specified, not external)
- CLI or UI entry points (these are tested via subprocess or in-process calls)

### Fixture File Format

```json
{
  "id": "pay_abc123",
  "amount": 4999,
  "currency": "usd",
  "status": "succeeded"
}
```

### Directory Structure Example

```
tests/
  fixtures/
    payment_service/
      README.md
      charge_success.json
      charge_declined.json
      refund_success.json
    weather_api/
      README.md
      current_weather.json
      forecast_5day.json
  features/
    cli_entrypoint/
      ...
  unit/
    ...
```

## Related

- [[architecture/contract-design]]: port/adapter contracts that fixtures mock
- [[requirements/gherkin]]: how literal values in steps must match fixture data
- [[software-craft/test-stubs]]: how beehave generates stubs that reference fixtures
- [[software-craft/test-design]]: test location and coupling spectrum
