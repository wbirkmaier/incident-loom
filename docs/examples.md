# Examples

```bash
uv run incident-loom ingest tests/fixtures/incident-evidence
uv run incident-loom timeline --fixtures tests/fixtures/incident-evidence
```

The shipped fixture includes Kubernetes events, a Prometheus alert, and a human incident note normalized onto one timeline.
