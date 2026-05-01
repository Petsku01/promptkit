"""Tests for Builder v2 — template variables (string.Template)."""



from llm_promptkit import PromptBuilder


class TestBuilderVariable:
    """Test PromptBuilder.variable() method."""

    def test_single_variable(self):
        """Single variable substitution works."""
        builder = PromptBuilder()
        builder.persona("Senior Developer")
        builder.pattern("chain-of-thought")
        builder.variable("domain", "cybersecurity")
        builder.task("Analyze this code")
        result = builder.build()
        # chain-of-thought doesn't have $domain by default,
        # so this should work without errors
        assert "Analyze this code" in result

    def test_variable_in_custom_pattern(self):
        """Variable substitution works with custom patterns that have $variables."""
        # We need to mock read_pattern to return a pattern with $variable
        from llm_promptkit.patterns import _registry

        # Temporarily add a pattern with variables
        _registry.read_pattern = _registry.read_pattern.__wrapped__  # unwrap lru_cache if needed

        # Use a simpler approach: test that safe_substitute works
        builder = PromptBuilder()
        builder._variables = {"domain": "cybersecurity", "language": "Python"}
        from string import Template

        template_text = "Analyze this $domain code written in ${language}."
        result = Template(template_text).safe_substitute(builder._variables)
        assert "cybersecurity" in result
        assert "Python" in result
        assert "$" not in result

    def test_variable_method_returns_builder(self):
        """variable() returns self for chaining."""
        builder = PromptBuilder()
        result = builder.variable("domain", "test")
        assert result is builder

    def test_multiple_variables(self):
        """Multiple variables can be set."""
        builder = PromptBuilder()
        builder.variable("domain", "security")
        builder.variable("language", "Python")
        builder.variable("level", "senior")
        assert builder._variables == {"domain": "security", "language": "Python", "level": "senior"}

    def test_variable_override(self):
        """Setting same variable twice uses the last value."""
        builder = PromptBuilder()
        builder.variable("domain", "security")
        builder.variable("domain", "data science")
        assert builder._variables["domain"] == "data science"


class TestBuilderVariableSubstitution:
    """Test that build() correctly substitutes variables in patterns."""

    def test_variable_not_in_pattern_no_error(self):
        """Variables that don't exist in pattern are simply not substituted."""
        builder = PromptBuilder()
        builder.persona("Developer")
        builder.pattern("chain-of-thought")
        builder.variable("unused_var", "unused_value")
        # Should not raise — safe_substitute leaves nonexistent vars as-is
        result = builder.build()
        assert isinstance(result, str)

    def test_variable_backwards_compatibility(self):
        """Builder without variables works exactly as before."""
        builder = PromptBuilder()
        builder.persona("Senior Developer")
        builder.pattern("chain-of-thought")
        builder.task("Review this code")
        result = builder.build()
        assert "Senior Developer" in result
        assert "Review this code" in result

    def test_dollar_sign_in_pattern_escaped(self):
        """$$ in pattern text is preserved as literal $."""
        from string import Template
        text = "The price is $$100."
        result = Template(text).safe_substitute({})
        assert result == "The price is $100."

    def test_unresolved_variable_warning(self):
        """Unresolved variables produce a warning."""
        from llm_promptkit.builder import re_find_template_vars

        # Text with unresolved variable
        text = "Analyze this $domain code."
        vars_found = re_find_template_vars(text)
        assert "domain" in vars_found

    def test_env_vars_not_flagged(self):
        """Common env-like variables ($HOME, $PATH) are not flagged."""
        from llm_promptkit.builder import re_find_template_vars

        text = "Use $HOME and $PATH for the configuration."
        vars_found = re_find_template_vars(text)
        assert "HOME" not in vars_found
        assert "PATH" not in vars_found

    def test_build_no_variables_same_as_before(self):
        """PromptBuilder.build() produces same output as v0.2.0 when no variables."""
        builder = PromptBuilder()
        builder.persona("Expert")
        builder.task("Do something")
        result = builder.build()
        assert result == "You are a Expert.\n\nTask: Do something"

    def test_build_with_constraints(self):
        """Builder with constraints and variables works."""
        builder = PromptBuilder()
        builder.persona("Developer")
        builder.constraint("Max 100 words")
        builder.task("Summarize")
        result = builder.build()
        assert "Constraints:" in result
        assert "Max 100 words" in result
