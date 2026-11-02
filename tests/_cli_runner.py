"""Shared CliRunner factory: stderr must never mix into stdout.

click 8.1 (Python 3.9 leg) has CliRunner(mix_stderr=True) by default, which
merges stderr into result.stdout and breaks tests that parse stdout as
pure JSON. click >= 8.2 (requires Python >= 3.10) removed the parameter
and never mixes. This factory selects the correct construction for the
installed click version.
"""

from typer.testing import CliRunner


def make_runner() -> CliRunner:
    try:
        return CliRunner(mix_stderr=False)
    except TypeError:
        # click >= 8.2: parameter removed; stderr is always separated.
        return CliRunner()


def visible_text(result) -> str:
    """stdout + stderr combined — what the user sees in a real terminal.

    Error messages are emitted to stderr (typer.echo(..., err=True)); tests
    that check for them must assert visibility across both streams, since
    the CliRunner's stream separation depends on the installed click version.
    """
    text = result.output or ""
    try:
        text += (result.stderr or "") if hasattr(result, "stderr") else ""
    except (ValueError, AttributeError):
        # click 8.1 with mix_stderr=True: stderr not separately captured,
        # in which case result.output is already the combined stream.
        pass
    return text
