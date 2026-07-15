## Problem

IncidentLoom could normalize and sort events, but there was still no concise human-readable timeline output for review.

## Approach

- added Markdown rendering from the normalized timeline model
- exposed `incident-loom render --fixtures <dir> --format markdown`
- kept the rendered timeline strictly derived from the deterministic event stream

## Important decisions

- rendered directly from normalized events rather than mixing in any summary or hypothesis layer
- kept evidence IDs and confidence labels inline so the Markdown remains auditable
- used a golden Markdown file to keep timeline presentation stable

## Test evidence

- `uv run ruff check .`
- `uv run mypy src`
- `uv run pytest`
- `uv run pytest --cov=src --cov-report=term-missing`
- `uv build`
- `uv run incident-loom render --fixtures tests/fixtures/incident-evidence --format markdown`

## Known limitations

- only Markdown rendering is supported in this slice
- no deterministic summary or provider-backed explanation yet

## Self-review

- [x] Security reviewed
- [x] No write operations introduced
- [x] Output ordering is deterministic
- [x] Event and summary claims are evidence-based

## Review findings

- no material findings after local self-review
