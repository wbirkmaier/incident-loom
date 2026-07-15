# Threat Model

## Assets

- incident evidence records
- normalized timeline events
- rendered summaries and postmortem drafts

## Risks

- leaking sensitive incident details or credentials
- presenting hypotheses as confirmed facts
- losing provenance between normalized events and original evidence

## Mitigations

- evidence IDs preserved on all normalized events
- deterministic timeline independent of any AI provider
- explicit distinction between observation and hypothesis in later summary layers
