"""Canonical models for prompt doctor analysis."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict


class IssueSeverity(Enum):
    """Severity levels for doctor issues."""
    CRITICAL = "Critical"
    WARNING = "Warning"
    SUGGESTION = "Suggestion"
    INFO = "Info"


@dataclass
class DoctorIssue:
    """Represents an issue found by prompt analysis.
    
    This is the canonical model used across all doctor backends
    (rule-based and ML-based).
    """
    severity: IssueSeverity
    category: str
    issue: str
    suggestion: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __repr__(self) -> str:
        return f"DoctorIssue({self.severity.value}: {self.issue[:50]}...)"
