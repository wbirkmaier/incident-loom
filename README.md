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
uv run incident-loom summarize --fixtures tests/fixtures/incident-evidence --provider none
uv run incident-loom draft --fixtures tests/fixtures/incident-evidence
```

The current slice ingests sanitized fixture evidence, emits a deterministic JSON timeline, renders Markdown from the normalized timeline, generates a deterministic summary through the `none` provider, and drafts a simple postmortem markdown document from the same evidence.

Provider adapters for `ollama` and `bedrock` are present as explicit boundaries but are not implemented in this cycle.
