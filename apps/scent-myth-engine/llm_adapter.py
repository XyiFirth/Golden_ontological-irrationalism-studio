from __future__ import annotations

import os
from typing import Any, Dict

from models import GenerationPlan, ScentRequest


class LLMAdapter:
    """Interface for future LLM-backed planner/realizer/critic.

    The MVP defaults to rule-based generation. This adapter is intentionally
    small so OpenAI, Claude, or local model calls can be added later without
    changing the API layer.
    """

    def __init__(self) -> None:
        self.provider = os.getenv("LLM_PROVIDER", "none")

    def is_enabled(self) -> bool:
        return self.provider not in {"", "none", "rule_based"}

    def plan(self, request: ScentRequest, context: Dict[str, Any]) -> GenerationPlan | None:
        return None

    def realize(self, request: ScentRequest, plan: GenerationPlan) -> str | None:
        return None

    def critique(self, request: ScentRequest, copy: str) -> Dict[str, Any] | None:
        return None
