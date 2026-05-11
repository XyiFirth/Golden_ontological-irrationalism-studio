from __future__ import annotations

import json
from pathlib import Path

from generator import build_anchors, build_generation_plan, generate_copy, generate_title
from models import ScentRequest
from critic import evaluate_copy

ROOT = Path(__file__).resolve().parents[2]
REQUEST_PATH = ROOT / "examples" / "seongsu-popup-request.json"


def main() -> None:
    payload = json.loads(REQUEST_PATH.read_text(encoding="utf-8"))
    request = ScentRequest(**payload)
    anchors = build_anchors(request)
    plan = build_generation_plan(request)
    title = generate_title(request, anchors)
    one_line, copy, scent_card = generate_copy(request, anchors)
    scores, warnings = evaluate_copy(copy, request)

    print("TITLE:", title)
    print("ONE LINE:", one_line)
    print("COPY:", copy)
    print("SCENT CARD:", scent_card)
    print("ANCHORS:", anchors.model_dump())
    print("PLAN:", plan.model_dump())
    print("SCORES:", scores.model_dump())
    print("WARNINGS:", warnings)


if __name__ == "__main__":
    main()
