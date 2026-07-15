# Examples

```bash
uv run incident-loom ingest tests/fixtures/incident-evidence
uv run incident-loom timeline --fixtures tests/fixtures/incident-evidence
uv run incident-loom render --fixtures tests/fixtures/incident-evidence --format markdown
uv run incident-loom summarize --fixtures tests/fixtures/incident-evidence --provider none
uv run incident-loom draft --fixtures tests/fixtures/incident-evidence
```

The shipped fixture includes Kubernetes events, a Prometheus alert, and a human incident note normalized onto one timeline.
