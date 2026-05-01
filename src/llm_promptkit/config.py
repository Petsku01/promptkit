"""Configuration management for llm-promptkit.

Reads from $XDG_CONFIG_HOME/promptkit/config.toml (or platform equivalent).
If config is missing or invalid, everything works with defaults (opt-in).
"""

import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional


def get_config_dir() -> Path:
    """Resolve config directory path. No external dependencies.

    Priority:
    1. PROMPTKIT_CONFIG_DIR environment variable
    2. Platform-specific default:
       - Windows: %APPDATA%/promptkit
       - Others: $XDG_CONFIG_HOME/promptkit or ~/.config/promptkit
    """
    env = os.environ.get("PROMPTKIT_CONFIG_DIR")
    if env:
        return Path(env)

    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA", "")
        if appdata:
            return Path(appdata) / "promptkit"
        return Path.home() / "AppData" / "Roaming" / "promptkit"

    xdg = os.environ.get("XDG_CONFIG_HOME", "")
    if xdg:
        return Path(xdg) / "promptkit"
    return Path.home() / ".config" / "promptkit"


def _load_toml(path: Path) -> Dict[str, Any]:
    """Load a TOML file. Uses tomllib (3.11+) or tomli as fallback.

    Returns empty dict if file doesn't exist.
    Returns empty dict (with stderr warning) if file is invalid.
    """
    if not path.exists():
        return {}

    try:
        if sys.version_info >= (3, 11):
            import tomllib
        else:
            import tomli as tomllib  # type: ignore[no-redef]
    except ImportError:
        # No TOML parser available at all — fall back to empty config
        print(
            f"Warning: Cannot parse {path} — no TOML parser available. "
            "Install tomli for Python < 3.11.",
            file=sys.stderr,
        )
        return {}

    try:
        with open(path, "rb") as f:
            return tomllib.load(f)  # type: ignore[attr-defined]
    except Exception as e:
        print(
            f"Warning: Failed to parse {path}: {e}. Using defaults.",
            file=sys.stderr,
        )
        return {}


class PromptKitConfig:
    """Configuration for llm-promptkit.

    Attributes:
        default_persona: Default persona for prompt building.
        default_model: Default model for token estimation (reserved).
        extra_prompt_dirs: Additional directories to search for prompts.
        extra_pattern_dirs: Additional directories to search for patterns.
        config_dir: The resolved config directory path.
        config_path: The resolved config file path.
    """

    def __init__(self, config_dir: Optional[Path] = None):
        self.config_dir = config_dir or get_config_dir()
        self.config_path = self.config_dir / "config.toml"
        self._raw: Dict[str, Any] = {}

        self._load()

    def _load(self) -> None:
        """Load configuration from TOML file."""
        self._raw = _load_toml(self.config_path)
        self._validate()

    def _validate(self) -> None:
        """Validate configuration values and warn about issues."""
        # Validation warnings are emitted by _resolve_dirs for better locality
        pass

    @property
    def promptkit(self) -> Dict[str, Any]:
        """Top-level [promptkit] section."""
        return self._raw.get("promptkit", {})

    @property
    def paths(self) -> Dict[str, Any]:
        """[promptkit.paths] section."""
        return self.promptkit.get("paths", {})

    @property
    def default_persona(self) -> str:
        """Default persona for prompt building."""
        return self.promptkit.get("default_persona", "")

    @property
    def default_model(self) -> str:
        """Default model for token estimation (reserved for future use)."""
        return self.promptkit.get("default_model", "")

    def _resolve_dirs(self, key: str) -> List[Path]:
        """Resolve directory list from config, filtering invalid entries.

        Only absolute paths that exist are included.
        Non-absolute paths and non-existent paths are skipped with warnings.
        """
        raw_dirs = self.paths.get(key, [])
        result = []
        for d in raw_dirs:
            p = Path(d)
            if not p.is_absolute():
                print(
                    f"Warning: {key} entry '{d}' is not absolute — skipping.",
                    file=sys.stderr,
                )
                continue
            if not p.exists():
                print(
                    f"Warning: {key} entry '{d}' does not exist — skipping.",
                    file=sys.stderr,
                )
                continue
            result.append(p)
        return result

    @property
    def extra_prompt_dirs(self) -> List[Path]:
        """Additional directories to search for prompts (user > built-in)."""
        return self._resolve_dirs("extra_prompt_dirs")

    @property
    def extra_pattern_dirs(self) -> List[Path]:
        """Additional directories to search for patterns (user > built-in)."""
        return self._resolve_dirs("extra_pattern_dirs")

    def reload(self) -> None:
        """Re-read configuration from disk."""
        self._load()

    def __repr__(self) -> str:
        return (
            f"PromptKitConfig("
            f"config_dir={self.config_dir!r}, "
            f"extra_prompt_dirs={self.extra_prompt_dirs!r}, "
            f"extra_pattern_dirs={self.extra_pattern_dirs!r}, "
            f"default_persona={self.default_persona!r})"
        )


# Module-level singleton for performance — lazy-loaded
_config: Optional[PromptKitConfig] = None


def get_config() -> PromptKitConfig:
    """Get or create the configuration singleton."""
    global _config
    if _config is None:
        _config = PromptKitConfig()
    return _config


def reload_config() -> PromptKitConfig:
    """Force reload configuration from disk."""
    global _config
    if _config is not None:
        _config.reload()
    else:
        _config = PromptKitConfig()
    return _config
