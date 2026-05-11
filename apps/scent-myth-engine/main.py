from __future__ import annotations

from fastapi import FastAPI

from critic import evaluate_copy
from generator import build_anchors, build_generation_plan, generate_copy, generate_title
from models import GenerationPlan, ScentOutput, ScentRequest
from ontology import load_ontology

app = FastAPI(
    title="Scent Myth Engine MVP",
    description="Scene-to-scent translation API for commercial fragrance storytelling.",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/v1/ontology")
def get_ontology() -> dict:
    return load_ontology()


@app.post("/api/v1/plan/generation", response_model=GenerationPlan)
def plan_generation(request: ScentRequest) -> GenerationPlan:
    return build_generation_plan(request)


@app.post("/api/v1/generate/scent-copy", response_model=ScentOutput)
def generate_scent_copy(request: ScentRequest) -> ScentOutput:
    anchors = build_anchors(request)
    title = generate_title(request, anchors)
    one_line, copy, scent_card = generate_copy(request, anchors)
    scores, warnings = evaluate_copy(copy, request)
    return ScentOutput(
        title=title,
        one_line_hook=one_line,
        copy=copy,
        scent_card=scent_card,
        anchors=anchors,
        scores=scores,
        warnings=warnings,
    )


@app.post("/api/v1/generate/popup-card", response_model=ScentOutput)
def generate_popup_card(request: ScentRequest) -> ScentOutput:
    request.output_type = "popup_result"
    return generate_scent_copy(request)


@app.post("/api/v1/evaluate/copy")
def evaluate_existing_copy(payload: dict) -> dict:
    request = ScentRequest(**payload["request"])
    scores, warnings = evaluate_copy(payload["copy"], request)
    return {"scores": scores.model_dump(), "warnings": warnings}
