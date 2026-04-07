"""Config command for promptkit."""

import os
import subprocess

from rich.panel import Panel
from rich.syntax import Syntax

from ..config import get_config, get_config_file, init_config, save_config
from ..console import console


def config_command(args):
    """Manage promptkit configuration."""
    config_path = get_config_file()

    if args.init:
        if config_path.exists():
            console.print(f"[yellow]Config file already exists at:[/yellow] {config_path}")
            console.print("[dim]Use --show to view or --edit to modify.[/dim]")
        else:
            init_config()
            console.print(f"[green]Created config file:[/green] {config_path}")
            console.print("[dim]Edit with: promptkit config --edit[/dim]")

    elif args.show:
        config = get_config()

        content = f"""# Promptkit Configuration

# Prompt Defaults
[prompt]
default_persona = "{config.default_persona or 'Not set'}"
default_output_format = "{config.default_output_format or 'Not set'}"

# UI Settings
[ui]
theme = "{config.theme}"
color_output = {config.color_output}

# Doctor Settings
[doctor]
ml_model = "{config.doctor_ml_model}"
ml_enabled = {config.doctor_ml_enabled}

# Paths
[paths]
custom_prompts_dir = "{config.custom_prompts_dir or 'Not set'}"

# Aliases
[aliases]
{chr(10).join(f"{k} = {v}" for k, v in config.aliases.items()) or "# No aliases defined"}
"""
        console.print(Panel(
            Syntax(content, "toml", theme="monokai"),
            title=f"Config: {config_path}",
            border_style="blue"
        ))

    elif args.edit:
        editor = os.environ.get("EDITOR", "nano")

        if not config_path.exists():
            init_config()

        try:
            subprocess.run([editor, str(config_path)], check=True)
            console.print("[green]Config updated.[/green]")
        except FileNotFoundError:
            console.print(f"[red]Editor not found: {editor}[/red]")
            console.print("[dim]Set EDITOR environment variable or edit manually:[/dim]")
            console.print(f"  {config_path}")
        except subprocess.CalledProcessError:
            console.print("[yellow]Editor exited with error. Config may not be saved.[/yellow]")

    elif args.set:

        config = get_config()

        for key, value in args.set:
            if key == "prompt.default_persona":
                config.default_persona = value
            elif key == "prompt.default_output_format":
                config.default_output_format = value
            elif key == "ui.theme":
                config.theme = value
            elif key == "ui.color_output":
                config.color_output = value.lower() in ("true", "yes", "1")
            elif key == "doctor.ml_model":
                config.doctor_ml_model = value
            elif key == "doctor.ml_enabled":
                config.doctor_ml_enabled = value.lower() in ("true", "yes", "1")
            elif key == "paths.custom_prompts":
                from pathlib import Path
                config.custom_prompts_dir = Path(value).expanduser()
            else:
                console.print(f"[red]Unknown config key: {key}[/red]")
                continue
            console.print(f"[green]Set {key} = {value}[/green]")

        save_config(config)
        console.print(f"[dim]Config saved to {config_path}[/dim]")

    else:
        # Default: show config file path and status
        if config_path.exists():
            console.print(f"[green]Config file:[/green] {config_path}")
            console.print("[dim]Commands:[/dim]")
            console.print("  --init    Create default config")
            console.print("  --show    Display current config")
            console.print("  --edit    Open in editor")
            console.print("  --set KEY VALUE  Set a value")
        else:
            console.print("[yellow]No config file found.[/yellow]")
            console.print("[dim]Create one with: promptkit config --init[/dim]")
