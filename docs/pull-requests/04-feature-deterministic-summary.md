## Problem

IncidentLoom could ingest and render a timeline, but it still lacked a concise summary path for cases where no AI provider should be used.

## Approach

- added a deterministic `none` summary provider
- summarized only observable timeline scope and involved sources
- exposed `incident-loom summarize --provider none`

## Important decisions

- kept the summary observational and evidence-based rather than adding any hypothesis or root-cause language
- made unsupported providers fail explicitly instead of silently degrading behavior
- preserved the underlying evidence IDs in the summary output so the concise view still links back to the timeline

## Test evidence

- `uv run ruff check .`
- `uv run mypy src`
- `uv run pytest`
- `uv run pytest --cov=src --cov-report=term-missing`
- `uv build`
- `uv run incident-loom summarize --fixtures tests/fixtures/incident-evidence --provider none`

## Known limitations

- only the `none` provider is implemented in this slice
- no explicit contradiction or hypothesis rendering yet

## Self-review

- [x] Security reviewed
- [x] No write operations introduced
- [x] Output ordering is deterministic
- [x] Event and summary claims are evidence-based

## Review findings

- no material findings after local self-review
