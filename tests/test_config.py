"""Tests for config module and config command."""

from pathlib import Path
from unittest.mock import patch

from llm_promptkit.config import Config, get_config_dir, init_config, load_config, save_config


class TestConfig:
    """Tests for the Config dataclass and config functions."""

    def test_default_config(self):
        config = Config()
        assert config.default_persona is None
        assert config.default_output_format is None
        assert config.theme == "default"
        assert config.color_output is True
        assert config.doctor_ml_model == "qwen2.5:3b"
        assert config.doctor_ml_enabled is False
        assert config.custom_prompts_dir is None
        assert config.aliases == {}

    def test_get_config_dir(self):
        config_dir = get_config_dir()
        assert isinstance(config_dir, Path)

    def test_load_config_no_file(self, tmp_path):
        config = load_config(tmp_path / "nonexistent.toml")
        assert isinstance(config, Config)
        assert config.theme == "default"

    def test_save_and_load_roundtrip(self, tmp_path):
        """Save a config, load it back, verify all fields survive the roundtrip."""
        config_path = tmp_path / "config.toml"
        original = Config(
            default_persona="senior engineer",
            default_output_format="json",
            theme="minimal",
            color_output=False,
            doctor_ml_model="llama3:8b",
            doctor_ml_enabled=True,
            custom_prompts_dir=Path("/custom/prompts"),
            aliases={"cot": "chain-of-thought", "sr": "senior-reviewer"},
        )
        save_config(original, config_path)
        loaded = load_config(config_path)

        assert loaded.default_persona == "senior engineer"
        assert loaded.default_output_format == "json"
        assert loaded.theme == "minimal"
        assert loaded.color_output is False
        assert loaded.doctor_ml_model == "llama3:8b"
        assert loaded.doctor_ml_enabled is True
        assert loaded.custom_prompts_dir == Path("/custom/prompts")
        assert loaded.aliases == {"cot": "chain-of-thought", "sr": "senior-reviewer"}

    def test_save_config_creates_parent_dirs(self, tmp_path):
        config_path = tmp_path / "nested" / "dir" / "config.toml"
        save_config(Config(), config_path)
        assert config_path.exists()

    def test_save_roundtrip_with_defaults(self, tmp_path):
        """Default config survives save/load without corruption."""
        config_path = tmp_path / "config.toml"
        save_config(Config(), config_path)
        loaded = load_config(config_path)

        assert loaded.theme == "default"
        assert loaded.color_output is True
        assert loaded.doctor_ml_model == "qwen2.5:3b"
        assert loaded.doctor_ml_enabled is False

    def test_load_config_malformed_file_warns(self, tmp_path):
        """Malformed TOML returns default config and prints a warning."""
        config_path = tmp_path / "bad.toml"
        config_path.write_text("this is not valid toml {{{{")

        with patch("llm_promptkit.console.console") as mock_console:
            config = load_config(config_path)

        assert isinstance(config, Config)
        assert config.theme == "default"
        # Verify the warning was printed
        mock_console.print.assert_called_once()
        warning_text = mock_console.print.call_args[0][0]
        assert "Warning" in warning_text
        assert str(config_path) in warning_text

    def test_init_config_creates_file(self, tmp_path):
        with patch("llm_promptkit.config.get_config_file", return_value=tmp_path / "config.toml"):
            path = init_config()
            assert path.exists()
            # Verify the created file is valid TOML by loading it
            loaded = load_config(path)
            assert loaded.theme == "default"

    def test_init_config_does_not_overwrite(self, tmp_path):
        config_path = tmp_path / "config.toml"
        config_path.write_text("# existing config")
        with patch("llm_promptkit.config.get_config_file", return_value=config_path):
            path = init_config()
            assert path.read_text() == "# existing config"


class TestConfigCommand:
    """Tests for the config CLI command."""

    def _make_args(self, init=False, show=False, edit=False, set=None):
        class Args:
            pass
        args = Args()
        args.init = init
        args.show = show
        args.edit = edit
        args.set = set
        return args

    @patch('llm_promptkit.commands.config.console')
    def test_config_init_new(self, mock_console, tmp_path):
        from llm_promptkit.commands.config import config_command
        config_path = tmp_path / "config.toml"

        # Patch get_config_file in BOTH the commands module and the config module
        # so init_config's internal call also resolves to our tmp_path
        with (
            patch('llm_promptkit.commands.config.get_config_file', return_value=config_path),
            patch('llm_promptkit.config.get_config_file', return_value=config_path),
        ):
            config_command(self._make_args(init=True))

        mock_console.print.assert_any_call(f"[green]Created config file:[/green] {config_path}")
        assert config_path.exists()

    @patch('llm_promptkit.commands.config.console')
    @patch('llm_promptkit.commands.config.get_config_file')
    def test_config_init_existing(self, mock_get_file, mock_console, tmp_path):
        from llm_promptkit.commands.config import config_command
        config_path = tmp_path / "config.toml"
        config_path.write_text("# existing")
        mock_get_file.return_value = config_path

        config_command(self._make_args(init=True))
        mock_console.print.assert_any_call(f"[yellow]Config file already exists at:[/yellow] {config_path}")

    @patch('llm_promptkit.commands.config.console')
    @patch('llm_promptkit.commands.config.get_config_file')
    @patch('llm_promptkit.commands.config.get_config')
    def test_config_show(self, mock_get_config, mock_get_file, mock_console, tmp_path):
        from llm_promptkit.commands.config import config_command
        mock_get_file.return_value = tmp_path / "config.toml"
        mock_get_config.return_value = Config()

        config_command(self._make_args(show=True))
        assert mock_console.print.called

    def test_config_set_and_persist(self, tmp_path):
        """Set a value via the command, then verify it was saved to disk."""
        from llm_promptkit.commands.config import config_command

        config_path = tmp_path / "config.toml"
        save_config(Config(), config_path)
        config = load_config(config_path)

        with (
            patch('llm_promptkit.commands.config.console'),
            patch('llm_promptkit.commands.config.get_config_file', return_value=config_path),
            patch('llm_promptkit.config.get_config_file', return_value=config_path),
            patch('llm_promptkit.commands.config.get_config', return_value=config),
        ):
            config_command(self._make_args(set=[("prompt.default_persona", "senior dev")]))

        reloaded = load_config(config_path)
        assert reloaded.default_persona == "senior dev"

    @patch('llm_promptkit.commands.config.console')
    @patch('llm_promptkit.commands.config.get_config_file')
    @patch('llm_promptkit.commands.config.get_config')
    @patch('llm_promptkit.commands.config.save_config')
    def test_config_set_unknown_key(self, mock_save, mock_get_config, mock_get_file, mock_console, tmp_path):
        from llm_promptkit.commands.config import config_command
        mock_get_file.return_value = tmp_path / "config.toml"
        mock_get_config.return_value = Config()

        config_command(self._make_args(set=[("unknown.key", "value")]))
        mock_console.print.assert_any_call("[red]Unknown config key: unknown.key[/red]")

    @patch('llm_promptkit.commands.config.console')
    @patch('llm_promptkit.commands.config.get_config_file')
    def test_config_default_with_existing_file(self, mock_get_file, mock_console, tmp_path):
        from llm_promptkit.commands.config import config_command
        config_path = tmp_path / "config.toml"
        config_path.write_text("# config")
        mock_get_file.return_value = config_path

        config_command(self._make_args())
        mock_console.print.assert_any_call(f"[green]Config file:[/green] {config_path}")

    @patch('llm_promptkit.commands.config.console')
    @patch('llm_promptkit.commands.config.get_config_file')
    def test_config_default_no_file(self, mock_get_file, mock_console, tmp_path):
        from llm_promptkit.commands.config import config_command
        mock_get_file.return_value = tmp_path / "nonexistent.toml"

        config_command(self._make_args())
        mock_console.print.assert_any_call("[yellow]No config file found.[/yellow]")

    @patch('llm_promptkit.commands.config.console')
    @patch('llm_promptkit.commands.config.get_config_file')
    @patch('llm_promptkit.commands.config.get_config')
    @patch('llm_promptkit.commands.config.save_config')
    def test_config_set_ml_enabled(self, mock_save, mock_get_config, mock_get_file, mock_console, tmp_path):
        from llm_promptkit.commands.config import config_command
        mock_get_file.return_value = tmp_path / "config.toml"
        config = Config()
        mock_get_config.return_value = config

        config_command(self._make_args(set=[("doctor.ml_enabled", "true")]))
        assert config.doctor_ml_enabled is True

    @patch('llm_promptkit.commands.config.console')
    @patch('llm_promptkit.commands.config.get_config_file')
    @patch('llm_promptkit.commands.config.get_config')
    @patch('llm_promptkit.commands.config.save_config')
    def test_config_set_theme(self, mock_save, mock_get_config, mock_get_file, mock_console, tmp_path):
        from llm_promptkit.commands.config import config_command
        mock_get_file.return_value = tmp_path / "config.toml"
        config = Config()
        mock_get_config.return_value = config

        config_command(self._make_args(set=[("ui.theme", "minimal")]))
        assert config.theme == "minimal"
