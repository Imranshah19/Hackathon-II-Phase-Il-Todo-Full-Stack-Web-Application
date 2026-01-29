"""
Models package.

Exports commonly used models and enums.
"""

# Base utilities
from src.models.base import utc_now
from src.models.failure_mode import (
    STANDARD_FAILURE_MODES,
    FailureCode,
    FailureDetails,
    FailureModeDefinition,
    FailureResponse,
    Severity,
)
from src.models.skill import SkillCategory

# Task models (Data Schemas Phase-2)
from src.models.task import Task, TaskBase, TaskCreate, TaskPublic, TaskUpdate

# User models (Data Schemas Phase-2)
from src.models.user import User, UserBase, UserCreate, UserPublic

__all__ = [
    # Skill enums
    "SkillCategory",
    # Failure mode enums and models
    "FailureCode",
    "Severity",
    "FailureModeDefinition",
    "FailureDetails",
    "FailureResponse",
    "STANDARD_FAILURE_MODES",
    # User models
    "User",
    "UserBase",
    "UserCreate",
    "UserPublic",
    # Task models
    "Task",
    "TaskBase",
    "TaskCreate",
    "TaskPublic",
    "TaskUpdate",
    # Base utilities
    "utc_now",
]
