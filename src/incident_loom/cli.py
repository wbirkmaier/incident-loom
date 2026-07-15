from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from incident_loom.exceptions import IncidentLoomError
from incident_loom.fixtures import load_event_bundle
from incident_loom.models import EventBundle
from incident_loom.rendering import render_markdown
from incident_loom.summarize import summarize_timeline
from incident_loom.timeline import build_timeline

app = typer.Typer(
    help="Normalize incident evidence into a deterministic timeline.",
    no_args_is_help=True,
    pretty_exceptions_enable=False,
)


@app.callback()
def callback() -> None:
    """IncidentLoom command group."""


@app.command("version")
def version() -> None:
    typer.echo("incident-loom 0.1.0")


@app.command("ingest")
def ingest(
    fixtures: Annotated[
        Path,
        typer.Argument(exists=True, readable=True, file_okay=False, dir_okay=True),
    ],
) -> None:
    try:
        bundle = load_event_bundle(fixtures)
    except IncidentLoomError as error:
        raise typer.Exit(code=error.exit_code) from error

    typer.echo(bundle.model_dump_json(indent=2))


@app.command("timeline")
def timeline(
    fixtures: Annotated[
        Path,
        typer.Option(
            "--fixtures",
            exists=True,
            readable=True,
            file_okay=False,
            dir_okay=True,
        ),
    ],
) -> None:
    try:
        timeline_events = build_timeline(load_event_bundle(fixtures))
    except IncidentLoomError as error:
        raise typer.Exit(code=error.exit_code) from error

    typer.echo(EventBundle(events=timeline_events).model_dump_json(indent=2))


@app.command("render")
def render(
    fixtures: Annotated[
        Path,
        typer.Option(
            "--fixtures",
            exists=True,
            readable=True,
            file_okay=False,
            dir_okay=True,
        ),
    ],
    output_format: Annotated[
        str, typer.Option("--format", help="Only 'markdown' is currently supported.")
    ] = "markdown",
) -> None:
    if output_format != "markdown":
        raise typer.Exit(code=2)
    try:
        timeline_events = build_timeline(load_event_bundle(fixtures))
    except IncidentLoomError as error:
        raise typer.Exit(code=error.exit_code) from error

    typer.echo(render_markdown(timeline_events))


@app.command("summarize")
def summarize(
    fixtures: Annotated[
        Path,
        typer.Option(
            "--fixtures",
            exists=True,
            readable=True,
            file_okay=False,
            dir_okay=True,
        ),
    ],
    provider: Annotated[
        str, typer.Option("--provider", help="Only 'none' is currently supported.")
    ] = "none",
) -> None:
    try:
        timeline_events = build_timeline(load_event_bundle(fixtures))
        summary = summarize_timeline(timeline_events, provider)
    except IncidentLoomError as error:
        raise typer.Exit(code=error.exit_code) from error

    typer.echo(summary.model_dump_json(indent=2))


def main(argv: Annotated[list[str] | None, typer.Argument(hidden=True)] = None) -> None:
    app(args=argv)
