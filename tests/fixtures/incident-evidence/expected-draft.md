# Incident Draft

## Observations
- Timeline contains 3 normalized events between 2026-07-14T17:58:00Z and 2026-07-14T18:00:00Z.
- Sources observed: github, kubernetes, prometheus.

## Timeline
- `2026-07-14T17:58:00Z` Investigating elevated 5xx responses in payments (evidence `github-note-1`)
- `2026-07-14T17:59:30Z` Readiness probe failed: HTTP probe failed with statuscode: 503 (evidence `k8s-event-1`)
- `2026-07-14T18:00:00Z` payments-api latency above threshold (evidence `prom-alert-1`)

## Notes
- Root cause not yet established from the current evidence set.
