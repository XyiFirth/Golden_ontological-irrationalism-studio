from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class OutputType(str, Enum):
    product_page = "product_page"
    one_line_hook = "one_line_hook"
    scent_card = "scent_card"
    popup_result = "popup_result"
    instagram_caption = "instagram_caption"
    ip_collaboration = "ip_collaboration"


class BrandProfile(BaseModel):
    name: str
    tone: str
    price_positioning: Optional[str] = None
    forbidden_words: List[str] = Field(default_factory=list)


class FragranceProfile(BaseModel):
    top_notes: List[str]
    middle_notes: List[str]
    base_notes: List[str]
    accords: List[str] = Field(default_factory=list)
    intensity: int = Field(default=3, ge=1, le=5)
    longevity: int = Field(default=3, ge=1, le=5)


class SceneProfile(BaseModel):
    location: str
    weather: Optional[str] = None
    time_of_day: Optional[str] = None
    season: Optional[str] = None
    situation: str
    target_impression: str
    emotions: List[str] = Field(default_factory=list)


class ScentRequest(BaseModel):
    brand: BrandProfile
    fragrance: FragranceProfile
    scene: SceneProfile
    output_type: OutputType
    irrationality_level: float = Field(default=0.18, ge=0, le=1)


class AnchorBundle(BaseModel):
    sensory: List[str] = Field(default_factory=list)
    scene: List[str] = Field(default_factory=list)
    emotion: List[str] = Field(default_factory=list)
    symbolic: List[str] = Field(default_factory=list)


class ScoreBundle(BaseModel):
    clarity: float = Field(ge=0, le=100)
    situation_specificity: float = Field(ge=0, le=100)
    commercial_readability: float = Field(ge=0, le=100)
    brand_consistency: float = Field(default=80, ge=0, le=100)
    abstraction_risk: float = Field(default=20, ge=0, le=100)
    claim_safety: float = Field(default=95, ge=0, le=100)


class ScentOutput(BaseModel):
    title: str
    copy: str
    one_line_hook: Optional[str] = None
    scent_card: Optional[str] = None
    anchors: AnchorBundle
    scores: ScoreBundle
    warnings: List[str] = Field(default_factory=list)


class GenerationPlan(BaseModel):
    sensory_anchors: List[str]
    scene_anchors: List[str]
    emotional_anchors: List[str]
    symbolic_operators: List[str]
    commercial_frame: str
    constraints: List[str]
