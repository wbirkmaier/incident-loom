## Problem

IncidentLoom had a repository baseline but no working evidence or timeline path.

## Approach

- added typed normalized event records with timestamps, sources, evidence IDs, and source references
- implemented a fixture loader for incident evidence directories
- exposed `incident-loom ingest` and `incident-loom timeline` with deterministic JSON output

## Important decisions

- kept the first slice focused on a small number of evidence categories so the normalized event model could be exercised end to end
- sorted the timeline deterministically by timestamp and evidence ID
- preserved resource identity as optional because not every incident note or alert maps cleanly to one Kubernetes or cloud object

## Test evidence

- `uv run ruff check .`
- `uv run mypy src`
- `uv run pytest`
- `uv run pytest --cov=src --cov-report=term-missing`
- `uv build`
- `uv run incident-loom timeline --fixtures tests/fixtures/incident-evidence`

## Known limitations

- no rendering or summarization yet
- evidence categories are still fixture-backed rather than source-specific adapters

## Self-review

- [x] Security reviewed
- [x] No write operations introduced
- [x] Output ordering is deterministic
- [x] Event and summary claims are evidence-based

## Review findings

- fixed a missed CLI import for the normalized event bundle during local validation
