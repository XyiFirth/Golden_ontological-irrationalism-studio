from __future__ import annotations

from typing import List

from models import AnchorBundle, GenerationPlan, ScentRequest
from ontology import match_accords, match_notes, match_scene, symbolic_operator_examples


def _unique(values: List[str]) -> List[str]:
    seen = set()
    result = []
    for value in values:
        cleaned = value.strip()
        key = cleaned.lower()
        if cleaned and key not in seen:
            seen.add(key)
            result.append(cleaned)
    return result


def build_anchors(request: ScentRequest) -> AnchorBundle:
    all_notes = request.fragrance.top_notes + request.fragrance.middle_notes + request.fragrance.base_notes
    matched_notes = match_notes(all_notes)
    matched_accords = match_accords(request.fragrance.accords)
    matched_scene = match_scene(request.scene.location, request.scene.weather)

    sensory = []
    for note in matched_notes:
        sensory.extend(note.get("descriptors", [])[:3])
    for accord in matched_accords:
        sensory.extend(accord.get("descriptors", [])[:3])

    scene = [
        request.scene.location,
        request.scene.situation,
        request.scene.target_impression,
    ]
    if request.scene.weather:
        scene.append(request.scene.weather)
    if request.scene.time_of_day:
        scene.append(request.scene.time_of_day)
    if matched_scene:
        scene.extend(matched_scene.get("objects", []))
        scene.extend(matched_scene.get("commercial_language", []))

    emotion = list(request.scene.emotions)
    for note in matched_notes:
        emotion.extend(note.get("emotions", [])[:2])
    if matched_scene:
        emotion.extend(matched_scene.get("emotions", []))

    symbolic = []
    for operator in symbolic_operator_examples()[:3]:
        safe = operator.get("safe_example")
        if safe:
            symbolic.append(safe)

    return AnchorBundle(
        sensory=_unique(sensory)[:12],
        scene=_unique(scene)[:12],
        emotion=_unique(emotion)[:10],
        symbolic=_unique(symbolic)[:6],
    )


def build_generation_plan(request: ScentRequest) -> GenerationPlan:
    anchors = build_anchors(request)
    operators = []
    if request.irrationality_level > 0.05:
        operators.append("weather_to_skin_feel")
    if request.irrationality_level > 0.12:
        operators.append("note_to_texture")
    if request.irrationality_level > 0.2:
        operators.append("place_to_social_impression")

    constraints = [
        "include at least one concrete scent descriptor",
        "include at least one usage situation",
        "avoid medical or therapeutic claims",
        "avoid excessive abstraction",
        "use no more than one symbolic metaphor per paragraph",
    ]
    if request.brand.forbidden_words:
        constraints.append(f"avoid forbidden words: {', '.join(request.brand.forbidden_words)}")

    return GenerationPlan(
        sensory_anchors=anchors.sensory,
        scene_anchors=anchors.scene,
        emotional_anchors=anchors.emotion,
        symbolic_operators=operators,
        commercial_frame=f"{request.scene.situation}; target impression: {request.scene.target_impression}",
        constraints=constraints,
    )


def generate_title(request: ScentRequest, anchors: AnchorBundle) -> str:
    if "Seongsu" in request.scene.location or "seongsu" in request.scene.location.lower():
        return "Rain on Grey Concrete"
    if request.scene.weather:
        return f"{request.scene.weather.title()} {request.fragrance.accords[0].title() if request.fragrance.accords else 'Scent'}"
    return f"{request.fragrance.accords[0].title() if request.fragrance.accords else 'Untitled Scent Scene'}"


def generate_copy(request: ScentRequest, anchors: AnchorBundle) -> tuple[str, str, str]:
    accord = request.fragrance.accords[0] if request.fragrance.accords else "soft scent"
    top = request.fragrance.top_notes[0] if request.fragrance.top_notes else "a fresh opening"
    middle = ", ".join(request.fragrance.middle_notes[:2]) or "a soft middle"
    base = ", ".join(request.fragrance.base_notes[:2]) or "a clean base"
    scene_label = request.scene.location
    weather = f" {request.scene.weather}" if request.scene.weather else ""
    situation = request.scene.situation
    impression = request.scene.target_impression
    symbol = anchors.symbolic[0] if anchors.symbolic else "settles close to the skin"

    one_line = f"A {accord} for {situation} in {scene_label}."

    copy = (
        f"A {accord} for {situation} in {scene_label}{weather}. "
        f"It opens with {top}, moves through {middle}, and settles into {base}. "
        f"The scent feels {impression}. "
        f"It works best when you want something clear, wearable, and memorable without feeling loud. "
        f"On skin, it {symbol}."
    )

    scent_card = (
        f"Your scent scene is {generate_title(request, anchors)}. "
        f"Think {', '.join(anchors.scene[:3])}. "
        f"The impression is {impression}, with {accord} staying close to the skin."
    )
    return one_line, copy, scent_card
