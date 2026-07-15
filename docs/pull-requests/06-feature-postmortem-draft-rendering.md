## Problem

IncidentLoom had a timeline and deterministic summary, but it still lacked a concise postmortem-style draft built directly from that evidence.

## Approach

- added a deterministic postmortem draft renderer
- built the draft from the normalized timeline and the `none` summary provider
- exposed `incident-loom draft --fixtures <dir>`

## Important decisions

- kept the draft explicitly non-causal by stating that root cause is not established from the current evidence set
- reused the deterministic summary path rather than creating a second set of observations
- kept the draft markdown minimal so it remains a starting point for human incident review rather than a finished postmortem

## Test evidence

- `uv run ruff check .`
- `uv run mypy src`
- `uv run pytest`
- `uv run pytest --cov=src --cov-report=term-missing`
- `uv build`
- `uv run incident-loom draft --fixtures tests/fixtures/incident-evidence`

## Known limitations

- the draft is intentionally concise and does not yet include action items or contradictions sections
- provider-backed summaries are still not implemented in this cycle

## Self-review

- [x] Security reviewed
- [x] No write operations introduced
- [x] Output ordering is deterministic
- [x] Event and summary claims are evidence-based

## Review findings

- no material findings after local self-review
