from typer.testing import CliRunner

from incident_loom.cli import app


def test_help_exits_successfully() -> None:
    result = CliRunner().invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "Normalize incident evidence" in result.stdout


def test_version_command_prints_version() -> None:
    result = CliRunner().invoke(app, ["version"])

    assert result.exit_code == 0
    assert "incident-loom 0.1.0" in result.stdout
