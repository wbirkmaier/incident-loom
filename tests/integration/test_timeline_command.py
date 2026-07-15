import json
from pathlib import Path

from typer.testing import CliRunner

from incident_loom.cli import app


def test_timeline_command_matches_expected_output() -> None:
    fixture_dir = Path("tests/fixtures/incident-evidence")
    expected = json.loads((fixture_dir / "expected-timeline.json").read_text())

    result = CliRunner().invoke(app, ["timeline", "--fixtures", str(fixture_dir)])

    assert result.exit_code == 0
    assert json.loads(result.stdout) == expected
