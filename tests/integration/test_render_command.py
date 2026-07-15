from pathlib import Path

from typer.testing import CliRunner

from incident_loom.cli import app


def test_render_command_matches_expected_output() -> None:
    fixture_dir = Path("tests/fixtures/incident-evidence")
    expected = (fixture_dir / "expected-render.md").read_text().rstrip("\n")

    result = CliRunner().invoke(
        app, ["render", "--fixtures", str(fixture_dir), "--format", "markdown"]
    )

    assert result.exit_code == 0
    assert result.stdout == expected + "\n"
