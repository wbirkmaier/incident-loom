# Incident Timeline

- `2026-07-14T17:58:00Z` [github/human-note] Investigating elevated 5xx responses in payments evidence=`github-note-1` confidence=`observed`
- `2026-07-14T17:59:30Z` [kubernetes/readiness-failure] Readiness probe failed: HTTP probe failed with statuscode: 503 (Pod/payments/api-7786f8dd7b-mlwzg) evidence=`k8s-event-1` confidence=`observed`
- `2026-07-14T18:00:00Z` [prometheus/alert] payments-api latency above threshold (Deployment/payments/api) evidence=`prom-alert-1` confidence=`observed`
