## Problem

IncidentLoom had a deterministic summary path, but it still coupled summarization directly to one implementation instead of leaving room for optional providers.

## Approach

- added a summary-provider adapter interface
- implemented the deterministic `none` provider as the shipped path
- added explicit future provider stubs for `ollama` and `bedrock`

## Important decisions

- kept provider boundaries separate from the core timeline so the deterministic incident record never depends on remote inference
- made unimplemented providers fail explicitly instead of silently returning a degraded summary
- reused the existing deterministic summary logic through the `none` adapter rather than duplicating it

## Test evidence

- `uv run ruff check .`
- `uv run mypy src`
- `uv run pytest`
- `uv run pytest --cov=src --cov-report=term-missing`
- `uv build`
- `uv run incident-loom summarize --fixtures tests/fixtures/incident-evidence --provider none`

## Known limitations

- `ollama` and `bedrock` providers are intentionally not implemented yet
- no postmortem draft rendering yet

## Self-review

- [x] Security reviewed
- [x] No write operations introduced
- [x] Output ordering is deterministic
- [x] Event and summary claims are evidence-based

## Review findings

- no material findings after local self-review
