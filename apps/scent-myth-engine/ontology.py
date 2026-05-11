from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[2]
ONTOLOGY_PATH = ROOT / "data" / "fragrance_ontology_seed.json"


def _normalize(value: str) -> str:
    return value.strip().lower().replace(" ", "_").replace("-", "_")


@lru_cache(maxsize=1)
def load_ontology() -> Dict[str, Any]:
    with ONTOLOGY_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def _find_by_name(items: List[Dict[str, Any]], value: str) -> Dict[str, Any] | None:
    target = _normalize(value)
    for item in items:
        candidates = [item.get("id", ""), item.get("name", "")]
        if any(_normalize(candidate) == target for candidate in candidates if candidate):
            return item
    return None


def match_notes(note_names: List[str]) -> List[Dict[str, Any]]:
    ontology = load_ontology()
    matches = []
    for note in note_names:
        item = _find_by_name(ontology.get("notes", []), note)
        if item:
            matches.append(item)
        else:
            matches.append({
                "id": _normalize(note),
                "name": note,
                "family": "unknown",
                "layer": "unknown",
                "descriptors": [note],
                "occasions": [],
                "emotions": [],
                "commercial_use": []
            })
    return matches


def match_accords(accord_names: List[str]) -> List[Dict[str, Any]]:
    ontology = load_ontology()
    matches = []
    for accord in accord_names:
        item = _find_by_name(ontology.get("accords", []), accord)
        if item:
            matches.append(item)
        else:
            matches.append({
                "id": _normalize(accord),
                "name": accord,
                "descriptors": [accord],
                "best_for": [],
                "typical_notes": []
            })
    return matches


def match_scene(location: str, weather: str | None = None) -> Dict[str, Any] | None:
    ontology = load_ontology()
    haystack = f"{location} {weather or ''}".lower()
    for scene in ontology.get("scene_anchors", []):
        scene_text = " ".join([
            scene.get("id", ""),
            scene.get("name", ""),
            " ".join(scene.get("objects", [])),
            " ".join(scene.get("emotions", [])),
        ]).lower()
        if any(token in haystack or token in scene_text for token in ["seongsu", "gallery", "hotel"] if token in haystack):
            return scene
    return None


def symbolic_operator_examples() -> List[Dict[str, Any]]:
    return load_ontology().get("irrational_operators", [])
