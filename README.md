# IncidentLoom

IncidentLoom turns scattered incident evidence into a deterministic timeline before any summarizer tries to explain it.

## Current focus

- offline evidence ingestion from sanitized fixture directories
- deterministic normalized event records
- explicit separation between timeline facts and optional summaries

## Deliberate limits

- no mandatory AI dependency
- no hidden network calls
- no claim of root cause without evidence

## Running modes

- Offline: fixture-backed event ingestion and timeline generation
- Live: planned read-only adapters for Kubernetes, CloudWatch, GitHub, and alert sources

## Safety

- read-only by default
- deterministic core timeline output
- evidence IDs preserved end to end

## Status

```bash
uv run incident-loom ingest tests/fixtures/incident-evidence
uv run incident-loom timeline --fixtures tests/fixtures/incident-evidence
uv run incident-loom render --fixtures tests/fixtures/incident-evidence --format markdown
```

The current slice ingests sanitized fixture evidence, emits a deterministic JSON timeline, and renders Markdown from the normalized timeline. Summarization lands in later slices.
