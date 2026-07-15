# ADR 0001: Start With Deterministic Timeline Generation

## Status

Accepted

## Context

Incident review needs a trustworthy event ordering even when no AI provider is available.

## Decision

Build deterministic normalized event and timeline flows before adding optional summarization providers.

## Consequences

- core incident review works offline
- later provider adapters can reuse the same timeline evidence model
