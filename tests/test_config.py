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

    def test_save_and_load_config(self, tmp_path):
        config_path = tmp_path / "config.toml"
        config = Config(
            default_persona="senior engineer",
            theme="minimal",
            doctor_ml_model="llama3:8b",
        )
        save_config(config, config_path)

        assert config_path.exists()
        content = config_path.read_text()
        assert "senior engineer" in content
        assert "minimal" in content
        assert "llama3:8b" in content

    def test_save_config_creates_parent_dirs(self, tmp_path):
        config_path = tmp_path / "nested" / "dir" / "config.toml"
        save_config(Config(), config_path)
        assert config_path.exists()

    def test_save_config_with_aliases(self, tmp_path):
        config_path = tmp_path / "config.toml"
        config = Config(aliases={"cot": "chain-of-thought", "sr": "senior-reviewer"})
        save_config(config, config_path)

        content = config_path.read_text()
        assert "cot" in content
        assert "chain-of-thought" in content

    def test_save_config_with_custom_prompts_dir(self, tmp_path):
        config_path = tmp_path / "config.toml"
        config = Config(custom_prompts_dir=Path("/custom/prompts"))
        save_config(config, config_path)

        content = config_path.read_text()
        assert "/custom/prompts" in content

    def test_load_config_malformed_file(self, tmp_path):
        config_path = tmp_path / "bad.toml"
        config_path.write_text("this is not valid toml {{{{")
        config = load_config(config_path)
        # Should return default config, not crash
        assert isinstance(config, Config)
        assert config.theme == "default"

    def test_init_config_creates_file(self, tmp_path):
        with patch("llm_promptkit.config.get_config_file", return_value=tmp_path / "config.toml"):
            path = init_config()
            assert path.exists()

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
    @patch('llm_promptkit.commands.config.get_config_file')
    def test_config_init_new(self, mock_get_file, mock_console, tmp_path):
        from llm_promptkit.commands.config import config_command
        config_path = tmp_path / "config.toml"
        mock_get_file.return_value = config_path

        config_command(self._make_args(init=True))
        mock_console.print.assert_any_call(f"[green]Created config file:[/green] {config_path}")

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

    @patch('llm_promptkit.commands.config.console')
    @patch('llm_promptkit.commands.config.get_config_file')
    @patch('llm_promptkit.commands.config.get_config')
    @patch('llm_promptkit.commands.config.save_config')
    def test_config_set_persona(self, mock_save, mock_get_config, mock_get_file, mock_console, tmp_path):
        from llm_promptkit.commands.config import config_command
        mock_get_file.return_value = tmp_path / "config.toml"
        config = Config()
        mock_get_config.return_value = config

        config_command(self._make_args(set=[("prompt.default_persona", "senior dev")]))
        assert config.default_persona == "senior dev"

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
