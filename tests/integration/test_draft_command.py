from pathlib import Path

from typer.testing import CliRunner

from incident_loom.cli import app


def test_draft_command_matches_expected_output() -> None:
    fixture_dir = Path("tests/fixtures/incident-evidence")
    expected = (fixture_dir / "expected-draft.md").read_text().rstrip("\n")

    result = CliRunner().invoke(app, ["draft", "--fixtures", str(fixture_dir)])

    assert result.exit_code == 0
    assert result.stdout == expected + "\n"
