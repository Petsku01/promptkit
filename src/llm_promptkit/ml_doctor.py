"""ML-powered prompt analysis using local Ollama models."""

import json
import os
import re
import subprocess
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import requests


@dataclass
class MLDoctorIssue:
    """Issue found by ML analysis."""
    severity: str  # "critical", "warning", "suggestion", "info"
    category: str  # "clarity", "completeness", "tone", "structure", etc.
    issue: str
    suggestion: str
    confidence: float  # 0.0-1.0


class MLDoctor:
    """ML-powered prompt doctor using local Ollama models."""

    DEFAULT_MODEL = "qwen2.5:3b"
    DEFAULT_OLLAMA_URL = "http://localhost:11434/api/generate"

    SYSTEM_PROMPT = """You are an expert prompt engineer analyzing prompts for LLMs.

Analyze the given prompt and identify issues in these categories:
1. CLARITY: Vague or ambiguous instructions
2. COMPLETENESS: Missing context, role, or constraints
3. TONE: Inappropriate formality, verbosity, or politeness
4. STRUCTURE: Poor formatting, missing examples, unclear output format
5. CONSTRAINTS: Negative constraints, undefined edge cases

For each issue found, return:
- severity: "critical" | "warning" | "suggestion" | "info"
- category: one of the above
- issue: brief description of the problem
- suggestion: concrete fix
- confidence: 0.0-1.0

Return ONLY valid JSON in this format:
{
  "issues": [
    {
      "severity": "warning",
      "category": "clarity",
      "issue": "Phrase 'make it good' is vague",
      "suggestion": "Replace with specific criteria like 'optimize for performance under 100ms'",
      "confidence": 0.95
    }
  ],
  "overall_score": 0.7,
  "strengths": ["Clear task description", "Good use of examples"]
}

If no issues found, return empty issues array. Be thorough but concise."""

    def __init__(self, model: Optional[str] = None, url: Optional[str] = None):
        self.model = model or self.DEFAULT_MODEL
        self.url = url or os.environ.get("OLLAMA_URL", self.DEFAULT_OLLAMA_URL)
        self._base_url = self.url.rsplit("/api/", 1)[0] if "/api/" in self.url else self.url.rstrip("/")
        self._check_ollama()

    def _check_ollama(self) -> bool:
        """Check if Ollama is running."""
        try:
            response = requests.get(f"{self._base_url}/api/tags", timeout=2)
            return response.status_code == 200
        except requests.RequestException:
            return False

    def is_available(self) -> bool:
        """Check if ML analysis is available."""
        return self._check_ollama()

    def _pull_model_if_needed(self) -> bool:
        """Try to pull model if not available."""
        try:
            result = subprocess.run(
                ["ollama", "pull", self.model],
                capture_output=True,
                text=True,
                timeout=300
            )
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return False

    def analyze(self, prompt_text: str, timeout: int = 30) -> Tuple[List[MLDoctorIssue], Dict]:
        """Analyze prompt using ML model.

        Returns:
            Tuple of (issues list, metadata dict with overall_score and strengths)
        """
        if not self.is_available():
            raise RuntimeError(
                f"Ollama not available. Make sure Ollama is running: "
                f"curl {self._base_url}/api/tags"
            )

        analysis_prompt = f"Analyze this prompt:\n\n```\n{prompt_text}\n```\n\nReturn JSON analysis."

        try:
            response = requests.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": analysis_prompt,
                    "system": self.SYSTEM_PROMPT,
                    "stream": False,
                    "format": "json"
                },
                timeout=timeout
            )
            response.raise_for_status()

            result = response.json()
            response_text = result.get("response", "")

            # Parse JSON response
            return self._parse_response(response_text)

        except requests.Timeout:
            raise RuntimeError(f"ML analysis timed out after {timeout}s")
        except requests.RequestException as e:
            raise RuntimeError(f"Ollama request failed: {e}")

    def _parse_response(self, response_text: str) -> Tuple[List[MLDoctorIssue], Dict]:
        """Parse JSON response from model."""
        # Try to extract JSON from response
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if not json_match:
            # Fallback: try entire response as JSON
            json_text = response_text
        else:
            json_text = json_match.group()

        try:
            data = json.loads(json_text)
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Failed to parse ML response as JSON: {e}\nResponse: {response_text[:200]}")

        issues = []
        for issue_data in data.get("issues", []):
            issues.append(MLDoctorIssue(
                severity=issue_data.get("severity", "info"),
                category=issue_data.get("category", "general"),
                issue=issue_data.get("issue", ""),
                suggestion=issue_data.get("suggestion", ""),
                confidence=float(issue_data.get("confidence", 0.5))
            ))

        metadata = {
            "overall_score": data.get("overall_score", 0.5),
            "strengths": data.get("strengths", []),
            "model": self.model
        }

        return issues, metadata


def analyze_with_ml(prompt_text: str, model: Optional[str] = None) -> Tuple[List[MLDoctorIssue], Dict]:
    """Convenience function for ML analysis.

    Args:
        prompt_text: The prompt to analyze
        model: Ollama model to use (default: qwen2.5:3b)

    Returns:
        Tuple of (issues list, metadata)

    Raises:
        RuntimeError: If Ollama is not available
    """
    doctor = MLDoctor(model=model)
    return doctor.analyze(prompt_text)
