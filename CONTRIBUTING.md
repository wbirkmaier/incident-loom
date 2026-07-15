# Contributing

## Local setup

1. Install `uv`.
2. Run `uv sync --all-extras --dev`.
3. Run `pre-commit install`.

## Validation

- `uv run ruff format --check .`
- `uv run ruff check .`
- `uv run mypy src`
- `uv run pytest`
- `uv run pytest --cov=src --cov-report=term-missing`
- `uv build`

## Scope

- Keep core ingestion and timeline generation deterministic.
- Isolate AI providers behind explicit adapters.
- Preserve evidence references in every summary path.
