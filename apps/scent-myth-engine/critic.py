from __future__ import annotations

import re
from typing import List

from models import ScoreBundle, ScentRequest

ABSTRACT_RISK_WORDS = [
    "ontology",
    "existence",
    "soul",
    "eternity",
    "destiny",
    "void",
    "transcendence",
    "metaphysical",
]

CLAIM_RISK_WORDS = [
    "healing",
    "therapeutic",
    "cure",
    "treats",
    "allergen-free",
    "hypoallergenic",
    "medical",
]

SENSORY_WORDS = [
    "clean",
    "fresh",
    "green",
    "soft",
    "warm",
    "cool",
    "crisp",
    "dry",
    "powdery",
    "woody",
    "musk",
    "citrus",
    "floral",
    "amber",
    "skin",
]

SITUATION_WORDS = [
    "cafe",
    "office",
    "meeting",
    "date",
    "daily",
    "afternoon",
    "evening",
    "rain",
    "gallery",
    "street",
    "visit",
]


def _contains_any(text: str, words: List[str]) -> bool:
    lowered = text.lower()
    return any(word.lower() in lowered for word in words)


def _count_any(text: str, words: List[str]) -> int:
    lowered = text.lower()
    return sum(1 for word in words if word.lower() in lowered)


def evaluate_copy(copy: str, request: ScentRequest) -> tuple[ScoreBundle, List[str]]:
    warnings: List[str] = []
    lowered = copy.lower()

    sensory_hits = _count_any(copy, SENSORY_WORDS + request.fragrance.top_notes + request.fragrance.middle_notes + request.fragrance.base_notes + request.fragrance.accords)
    situation_hits = _count_any(copy, SITUATION_WORDS + [request.scene.location, request.scene.situation, request.scene.target_impression])
    abstract_hits = _count_any(copy, ABSTRACT_RISK_WORDS)
    claim_hits = _count_any(copy, CLAIM_RISK_WORDS)

    forbidden_hits = [word for word in request.brand.forbidden_words if word.lower() in lowered]
    if forbidden_hits:
        warnings.append(f"Forbidden words found: {', '.join(forbidden_hits)}")

    if sensory_hits < 2:
        warnings.append("Output may not include enough concrete scent descriptors.")
    if situation_hits < 1:
        warnings.append("Output may not include a clear usage situation.")
    if abstract_hits > 1:
        warnings.append("Output may be too abstract for commercial fragrance copy.")
    if claim_hits > 0:
        warnings.append("Output may contain unsupported medical or safety claims.")

    sentence_count = max(1, len(re.findall(r"[.!?]", copy)))
    avg_sentence_length = len(copy.split()) / sentence_count
    readability_penalty = max(0, avg_sentence_length - 24) * 1.5

    clarity = min(100, 55 + sensory_hits * 10 - abstract_hits * 8 - readability_penalty)
    situation_specificity = min(100, 50 + situation_hits * 12)
    commercial_readability = min(100, 88 - readability_penalty - abstract_hits * 6)
    brand_consistency = 90 - len(forbidden_hits) * 20
    abstraction_risk = min(100, abstract_hits * 18 + max(0, request.irrationality_level - 0.25) * 120)
    claim_safety = max(0, 100 - claim_hits * 35)

    return ScoreBundle(
        clarity=max(0, round(clarity, 1)),
        situation_specificity=max(0, round(situation_specificity, 1)),
        commercial_readability=max(0, round(commercial_readability, 1)),
        brand_consistency=max(0, round(brand_consistency, 1)),
        abstraction_risk=max(0, round(abstraction_risk, 1)),
        claim_safety=max(0, round(claim_safety, 1)),
    ), warnings
