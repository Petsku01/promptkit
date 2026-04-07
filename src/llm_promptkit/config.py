"""Configuration management for promptkit."""

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Optional

import tomllib


@dataclass
class Config:
    """Promptkit configuration."""

    # Default values for prompt building
    default_persona: Optional[str] = None
    default_output_format: Optional[str] = None

    # UI settings
    theme: str = "default"  # default, minimal, verbose
    color_output: bool = True

    # Doctor settings
    doctor_ml_model: str = "qwen2.5:3b"
    doctor_ml_enabled: bool = False

    # Paths
    custom_prompts_dir: Optional[Path] = None

    # Aliases (user-defined pattern shortcuts)
    aliases: Dict[str, str] = field(default_factory=dict)


def get_config_dir() -> Path:
    """Get configuration directory."""
    if os.name == "nt":  # Windows
        config_dir = Path(os.environ.get("APPDATA", "~")) / "promptkit"
    else:  # Linux/macOS
        config_dir = Path.home() / ".config" / "promptkit"
    return config_dir


def get_config_file() -> Path:
    """Get configuration file path."""
    return get_config_dir() / "config.toml"


def load_config(path: Optional[Path] = None) -> Config:
    """Load configuration from file.

    Args:
        path: Optional config file path. Uses default if not provided.

    Returns:
        Config object with loaded values (or defaults if file doesn't exist).
    """
    config_path = path or get_config_file()
    config = Config()

    if config_path.exists():
        try:
            with open(config_path, "rb") as f:
                data = tomllib.load(f)

            # Load prompt defaults
            if "prompt" in data:
                prompt = data["prompt"]
                config.default_persona = prompt.get("default_persona")
                config.default_output_format = prompt.get("default_output_format")

            # Load UI settings
            if "ui" in data:
                ui = data["ui"]
                config.theme = ui.get("theme", "default")
                config.color_output = ui.get("color_output", True)

            # Load doctor settings
            if "doctor" in data:
                doctor = data["doctor"]
                config.doctor_ml_model = doctor.get("ml_model", "qwen2.5:3b")
                config.doctor_ml_enabled = doctor.get("ml_enabled", False)

            # Load paths
            if "paths" in data:
                paths = data["paths"]
                if "custom_prompts" in paths:
                    config.custom_prompts_dir = Path(paths["custom_prompts"]).expanduser()

            # Load aliases
            if "aliases" in data:
                config.aliases = data["aliases"]

        except (OSError, tomllib.TOMLDecodeError, KeyError, ValueError) as e:
            from .console import console
            console.print(f"[yellow]Warning: Failed to load config from {config_path}: {e}[/yellow]")

    return config


def save_config(config: Config, path: Optional[Path] = None) -> None:
    """Save configuration to file.

    Args:
        config: Config object to save
        path: Optional config file path. Uses default if not provided.
    """
    config_path = path or get_config_file()
    config_path.parent.mkdir(parents=True, exist_ok=True)

    # Build TOML content
    lines = []
    lines.append('# Promptkit configuration file')
    lines.append('')

    # Prompt defaults
    lines.append('[prompt]')
    if config.default_persona:
        lines.append(f'default_persona = "{config.default_persona}"')
    if config.default_output_format:
        lines.append(f'default_output_format = "{config.default_output_format}"')
    lines.append('')

    # UI settings
    lines.append('[ui]')
    lines.append(f'theme = "{config.theme}"')
    lines.append(f'color_output = {str(config.color_output).lower()}')
    lines.append('')

    # Doctor settings
    lines.append('[doctor]')
    lines.append(f'ml_model = "{config.doctor_ml_model}"')
    lines.append(f'ml_enabled = {str(config.doctor_ml_enabled).lower()}')
    lines.append('')

    # Paths
    lines.append('[paths]')
    if config.custom_prompts_dir:
        lines.append(f'custom_prompts = "{config.custom_prompts_dir}"')
    lines.append('')

    # Aliases
    if config.aliases:
        lines.append('[aliases]')
        for alias, pattern in config.aliases.items():
            lines.append(f'{alias} = "{pattern}"')

    config_path.write_text('\n'.join(lines))


def init_config() -> Path:
    """Initialize default configuration file.

    Returns:
        Path to created config file.
    """
    config_path = get_config_file()

    if config_path.exists():
        return config_path

    config = Config()
    save_config(config, config_path)
    return config_path


# Global config instance (lazy-loaded)
_config: Optional[Config] = None


def get_config() -> Config:
    """Get global configuration (cached)."""
    global _config
    if _config is None:
        _config = load_config()
    return _config


def reload_config() -> Config:
    """Reload configuration from disk."""
    global _config
    _config = load_config()
    return _config
