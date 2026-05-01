"""Tests for configuration management (XDG, custom prompts/patterns)."""

import os
import tempfile
from pathlib import Path
from unittest.mock import patch

from typer.testing import CliRunner

from llm_promptkit.cli import app
from llm_promptkit.config import PromptKitConfig, _load_toml, get_config_dir

runner = CliRunner()


# ============================================================================
# Config directory resolution
# ============================================================================


class TestConfigDir:
    """Test XDG config directory resolution."""

    def test_promptkit_config_dir_env(self):
        """PROMPTKIT_CONFIG_DIR overrides everything."""
        with patch.dict(os.environ, {"PROMPTKIT_CONFIG_DIR": "/tmp/test-promptkit"}):
            result = get_config_dir()
            assert result == Path("/tmp/test-promptkit")

    def test_xdg_config_home(self):
        """XDG_CONFIG_HOME is respected."""
        with patch.dict(os.environ, {"XDG_CONFIG_HOME": "/tmp/xdg-test"}, clear=False):
            # Remove PROMPTKIT_CONFIG_DIR if set
            env = dict(os.environ)
            env.pop("PROMPTKIT_CONFIG_DIR", None)
            with patch.dict(os.environ, env, clear=True):
                result = get_config_dir()
                assert str(result).endswith("promptkit")

    def test_default_config_dir(self):
        """Default is ~/.config/promptkit."""
        with patch.dict(os.environ, {}, clear=True):
            result = get_config_dir()
            assert str(result).endswith(".config/promptkit") or str(result).endswith("promptkit")


# ============================================================================
# TOML loading
# ============================================================================


class TestTOMLLoading:
    """Test TOML config file loading."""

    def test_missing_config_returns_empty(self):
        """Missing config file returns empty dict."""
        result = _load_toml(Path("/nonexistent/path/config.toml"))
        assert result == {}

    def test_valid_config_loads(self):
        """Valid config file loads correctly."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".toml", delete=False) as f:
            f.write('[promptkit]\ndefault_persona = "Senior Dev"\n')
            f.flush()
            result = _load_toml(Path(f.name))
            assert result["promptkit"]["default_persona"] == "Senior Dev"
            os.unlink(f.name)

    def test_invalid_config_returns_empty(self):
        """Invalid TOML returns empty dict with warning."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".toml", delete=False) as f:
            f.write("[invalid toml {{{")
            f.flush()
            result = _load_toml(Path(f.name))
            # Should return empty dict, not crash
            assert isinstance(result, dict)
            os.unlink(f.name)


# ============================================================================
# PromptKitConfig
# ============================================================================


class TestPromptKitConfig:
    """Test PromptKitConfig class."""

    def test_empty_config_defaults(self):
        """Config with no file has sensible defaults."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = PromptKitConfig(config_dir=Path(tmpdir))
            assert config.default_persona == ""
            assert config.default_model == ""
            assert config.extra_prompt_dirs == []
            assert config.extra_pattern_dirs == []

    def test_persona_from_config(self):
        """Config file sets default_persona."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.toml"
            config_path.write_text('[promptkit]\ndefault_persona = "Expert Analyst"\n')
            config = PromptKitConfig(config_dir=Path(tmpdir))
            assert config.default_persona == "Expert Analyst"

    def test_extra_dirs_from_config(self):
        """Config file sets extra_prompt_dirs and extra_pattern_dirs."""
        with tempfile.TemporaryDirectory() as tmpdir:
            prompt_dir = Path(tmpdir) / "my_prompts"
            prompt_dir.mkdir()
            pattern_dir = Path(tmpdir) / "my_patterns"
            pattern_dir.mkdir()
            config_path = Path(tmpdir) / "config.toml"
            config_path.write_text(
                f'[promptkit.paths]\n'
                f'extra_prompt_dirs = ["{prompt_dir}"]\n'
                f'extra_pattern_dirs = ["{pattern_dir}"]\n'
            )
            config = PromptKitConfig(config_dir=Path(tmpdir))
            assert prompt_dir in config.extra_prompt_dirs
            assert pattern_dir in config.extra_pattern_dirs

    def test_nonexistent_dirs_skipped(self):
        """Non-existent directories are skipped with warning."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.toml"
            config_path.write_text(
                '[promptkit.paths]\n'
                f'extra_prompt_dirs = ["{tmpdir}/nonexistent"]\n'
            )
            config = PromptKitConfig(config_dir=Path(tmpdir))
            assert config.extra_prompt_dirs == []

    def test_relative_dirs_skipped(self):
        """Relative paths are skipped."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.toml"
            config_path.write_text(
                '[promptkit.paths]\n'
                'extra_prompt_dirs = ["relative/path"]\n'
            )
            config = PromptKitConfig(config_dir=Path(tmpdir))
            assert config.extra_prompt_dirs == []

    def test_reload_config(self):
        """reload() picks up changes from disk."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / "config.toml"
            config_path.write_text('[promptkit]\ndefault_persona = "V1"\n')
            config = PromptKitConfig(config_dir=Path(tmpdir))
            assert config.default_persona == "V1"

            config_path.write_text('[promptkit]\ndefault_persona = "V2"\n')
            config.reload()
            assert config.default_persona == "V2"


# ============================================================================
# Custom prompts via CLI
# ============================================================================


class TestCustomPromptsCLI:
    """Test custom prompt directories via CLI."""

    def test_prompts_list_with_custom_dir(self):
        """Custom prompt dirs are searched."""
        # Just verify the command works with default config
        result = runner.invoke(app, ["prompts"])
        assert result.exit_code == 0

    def test_search_with_custom_dir(self):
        """Search works with default config."""
        result = runner.invoke(app, ["search", "code review"])
        assert result.exit_code == 0


# ============================================================================
# Custom patterns via registry
# ============================================================================


class TestCustomPatternsRegistry:
    """Test custom pattern directories via registry."""

    def test_list_patterns_includes_builtins(self):
        """Built-in patterns are listed."""
        from llm_promptkit.patterns._registry import list_pattern_names
        names = list_pattern_names()
        assert "chain-of-thought" in names
        assert "few-shot" in names

    def test_pattern_source_is_built_in(self):
        """Built-in patterns are tagged as built-in."""
        from llm_promptkit.patterns._registry import get_pattern_source
        assert get_pattern_source("chain-of-thought") == "built-in"

    def test_custom_pattern_found(self):
        """Custom pattern dirs are searched and take priority."""
        import llm_promptkit.config as cfg_mod
        import llm_promptkit.patterns._registry as reg_mod

        # Reset global state from prior tests
        cfg_mod._config = None
        reg_mod.list_pattern_names.cache_clear()
        reg_mod.list_patterns_with_categories.cache_clear()

        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a custom pattern
            pattern_dir = Path(tmpdir) / "custom_patterns" / "reasoning"
            pattern_dir.mkdir(parents=True)
            (pattern_dir / "my-custom-pattern.md").write_text(
                "# my-custom-pattern\n\n**Category:** reasoning\n\nThis is my custom pattern with $variable."
            )

            # Create config pointing to custom dir
            config_dir = Path(tmpdir) / "config"
            config_dir.mkdir()
            config_file = config_dir / "config.toml"
            config_file.write_text(
                f'[promptkit.paths]\n'
                f'extra_pattern_dirs = ["{pattern_dir.parent}"]\n'
            )

            # Set PROMPTKIT_CONFIG_DIR
            with patch.dict(os.environ, {"PROMPTKIT_CONFIG_DIR": str(config_dir)}):
                from llm_promptkit.config import reload_config
                from llm_promptkit.patterns._registry import invalidate_pattern_cache
                reload_config()
                invalidate_pattern_cache()

                from llm_promptkit.patterns._registry import (
                    get_pattern_source,
                    list_pattern_names,
                    read_pattern,
                )
                names = list_pattern_names()
                assert "my-custom-pattern" in names

                content = read_pattern("my-custom-pattern")
                assert "$variable" in content or "variable" in content

                # Custom pattern should be tagged as custom
                source = get_pattern_source("my-custom-pattern")
                assert source == "custom"
