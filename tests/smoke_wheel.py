"""Run directly with the fresh wheel venv's Python, never an editable install."""

import json
import sys
import sysconfig
from pathlib import Path

from typer.testing import CliRunner

import llm_promptkit
from llm_promptkit import PromptBuilder
from llm_promptkit.cli import app

package_dir = Path(llm_promptkit.__file__).resolve().parent
site_packages = Path(sysconfig.get_path("purelib")).resolve()
assert site_packages in package_dir.parents, package_dir
assert sys.prefix != sys.base_prefix, "A fresh virtual environment is required"
assert (package_dir / "py.typed").is_file()

prompt = PromptBuilder().pattern("chain-of-thought").task("Wheel smoke").build()
assert "Think through this step-by-step" in prompt
assert "Task: Wheel smoke" in prompt

runner = CliRunner()
doctor = runner.invoke(app, ["doctor", "Write something", "--format", "json"])
assert doctor.exit_code == 0, doctor.output
report = json.loads(doctor.output)
assert isinstance(report, dict), report
assert report["issues"], report

providers = runner.invoke(app, ["prompts"])
assert providers.exit_code == 0, providers.output
assert "openai" in providers.output.lower(), providers.output
shown = runner.invoke(app, ["prompts", "--show", "openai/o3/coding"])
assert shown.exit_code == 0, shown.output
content = (package_dir / "prompts/model-optimized/openai/o3/coding.md").read_text(
    encoding="utf-8"
)
assert content.strip(), "Packaged prompt is empty"
assert "not found" not in shown.output.lower(), shown.output
assert "coding" in shown.output.lower(), shown.output
print("wheel smoke: import + py.typed + builder + doctor + prompts PASS")
