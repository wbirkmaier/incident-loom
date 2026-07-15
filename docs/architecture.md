# Architecture

IncidentLoom separates raw evidence ingestion, normalization, timeline ordering, and optional summarization.

## Planned flow

1. Adapters load incident evidence from fixtures or live sources.
2. Normalizers convert source records into a typed event model with evidence IDs.
3. Timeline logic orders events deterministically.
4. Renderers and optional providers build summaries on top of the timeline.

The deterministic `none` provider ships today, while remote providers remain behind explicit adapter boundaries so the core timeline never depends on them.
