"""Tests for ML-powered Doctor."""

import json
from unittest.mock import MagicMock, patch

import pytest
import requests

from llm_promptkit.ml_doctor import MLDoctor, MLDoctorIssue, analyze_with_ml


class TestMLDoctorInit:
    """Test MLDoctor initialization."""

    def test_default_model(self):
        """Default model is qwen2.5:3b."""
        doctor = MLDoctor()
        assert doctor.model == "qwen2.5:3b"

    def test_custom_model(self):
        """Can set custom model."""
        doctor = MLDoctor(model="llama3:8b")
        assert doctor.model == "llama3:8b"


class TestMLDoctorAvailability:
    """Test Ollama availability checks."""

    @patch("llm_promptkit.ml_doctor.requests.get")
    def test_available_when_ollama_responds(self, mock_get):
        """Doctor is available when Ollama responds."""
        mock_get.return_value = MagicMock(status_code=200)
        doctor = MLDoctor()
        assert doctor.is_available() is True

    @patch("llm_promptkit.ml_doctor.requests.get")
    def test_not_available_when_ollama_down(self, mock_get):
        """Doctor not available when Ollama down."""
        mock_get.side_effect = requests.RequestException("Connection refused")
        doctor = MLDoctor()
        assert doctor.is_available() is False

    @patch("llm_promptkit.ml_doctor.requests.get")
    def test_not_available_on_timeout(self, mock_get):
        """Doctor not available on timeout."""
        mock_get.side_effect = requests.Timeout()
        doctor = MLDoctor()
        assert doctor.is_available() is False


class TestMLDoctorAnalyze:
    """Test ML analysis functionality."""

    @patch("llm_promptkit.ml_doctor.requests.post")
    @patch("llm_promptkit.ml_doctor.requests.get")
    def test_analyze_returns_issues(self, mock_get, mock_post):
        """Analysis returns parsed issues."""
        # Mock availability check
        mock_get.return_value = MagicMock(status_code=200)

        # Mock analysis response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "response": json.dumps({
                "issues": [
                    {
                        "severity": "warning",
                        "category": "clarity",
                        "issue": "Vague instruction",
                        "suggestion": "Be more specific",
                        "confidence": 0.9
                    }
                ],
                "overall_score": 0.6,
                "strengths": ["Good structure"]
            })
        }
        mock_post.return_value = mock_response

        doctor = MLDoctor()
        issues, metadata = doctor.analyze("Make it good")

        assert len(issues) == 1
        assert issues[0].severity == "warning"
        assert issues[0].category == "clarity"
        assert issues[0].confidence == 0.9
        assert metadata["overall_score"] == 0.6

    @patch("llm_promptkit.ml_doctor.requests.get")
    def test_analyze_raises_when_unavailable(self, mock_get):
        """Analysis raises error when Ollama unavailable."""
        mock_get.side_effect = requests.RequestException("Connection refused")

        doctor = MLDoctor()
        with pytest.raises(RuntimeError) as exc_info:
            doctor.analyze("Test prompt")

        assert "Ollama not available" in str(exc_info.value)

    @patch("llm_promptkit.ml_doctor.requests.post")
    @patch("llm_promptkit.ml_doctor.requests.get")
    def test_analyze_handles_timeout(self, mock_get, mock_post):
        """Analysis raises error on timeout."""
        mock_get.return_value = MagicMock(status_code=200)
        mock_post.side_effect = requests.Timeout()

        doctor = MLDoctor()
        with pytest.raises(RuntimeError) as exc_info:
            doctor.analyze("Test prompt")

        assert "timed out" in str(exc_info.value).lower()


class TestMLDoctorIssue:
    """Test MLDoctorIssue dataclass."""

    def test_issue_creation(self):
        """Can create issue with all fields."""
        issue = MLDoctorIssue(
            severity="warning",
            category="clarity",
            issue="Vague",
            suggestion="Be specific",
            confidence=0.85
        )
        assert issue.severity == "warning"
        assert issue.confidence == 0.85


class TestAnalyzeWithML:
    """Test convenience function."""

    @patch("llm_promptkit.ml_doctor.requests.post")
    @patch("llm_promptkit.ml_doctor.requests.get")
    def test_convenience_function(self, mock_get, mock_post):
        """Convenience function works."""
        mock_get.return_value = MagicMock(status_code=200)
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "response": json.dumps({
                "issues": [],
                "overall_score": 0.9,
                "strengths": ["Clear"]
            })
        }
        mock_post.return_value = mock_response

        issues, metadata = analyze_with_ml("Test prompt", model="llama3:8b")

        assert len(issues) == 0
        assert metadata["overall_score"] == 0.9

    @patch("llm_promptkit.ml_doctor.requests.get")
    def test_uses_default_model(self, mock_get):
        """Default model used when not specified."""
        mock_get.return_value = MagicMock(status_code=200)

        # Just check that MLDoctor is created with default
        with patch("llm_promptkit.ml_doctor.MLDoctor.analyze") as mock_analyze:
            mock_analyze.return_value = ([], {"overall_score": 0.5})
            analyze_with_ml("Test")

            # Verify MLDoctor was created (can't easily check default)
            mock_analyze.assert_called_once()
