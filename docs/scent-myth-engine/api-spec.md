# API Specification

## Purpose

This API spec defines the first implementable backend interface for Scent Myth Engine.

The API should support:

- scene-to-scent copy generation
- popup personalization card generation
- copy evaluation
- brand tone analysis
- ontology lookup

## Base URL

```text
/api/v1
```

## 1. Generate Scent Copy

```http
POST /api/v1/generate/scent-copy
```

### Request

Uses `schemas/scent_request.schema.json`.

### Response

Uses `schemas/scent_output.schema.json`.

### Generation Steps

1. Validate request schema.
2. Map fragrance notes to ontology seed.
3. Retrieve sensory, scene, and emotion anchors.
4. Build generation plan.
5. Generate copy.
6. Evaluate copy.
7. Return result with scores and warnings.

---

## 2. Generate Popup Card

```http
POST /api/v1/generate/popup-card
```

### Purpose

Generate a short, shareable scent identity card for offline pop-up visitors.

### Output Fields

- scent_scene_title
- one_line_hook
- short_description
- recommended_product
- qr_payload
- share_text

---

## 3. Build Generation Plan

```http
POST /api/v1/plan/generation
```

### Purpose

Return the structured intermediate plan before final prose generation.

### Uses

- debugging
- human review
- prompt tuning
- model evaluation

### Response

Uses `schemas/generation_plan.schema.json`.

---

## 4. Evaluate Copy

```http
POST /api/v1/evaluate/copy
```

### Request

```json
{
  "copy": "A clean green musk for a rainy afternoon in Seongsu...",
  "brand": {
    "tone": "minimal literary",
    "forbidden_words": ["soul", "healing"]
  },
  "expected_scene": "rainy Seongsu afternoon",
  "expected_scent_direction": ["green musk", "bergamot", "fig", "musk"]
}
```

### Response

```json
{
  "clarity": 92,
  "situation_specificity": 95,
  "commercial_readability": 90,
  "brand_consistency": 88,
  "abstraction_risk": 18,
  "claim_safety": 98,
  "warnings": []
}
```

---

## 5. Analyze Brand Tone

```http
POST /api/v1/analyze/brand-tone
```

### Purpose

Convert existing brand copy into a reusable tone profile.

### Request

```json
{
  "brand_name": "Grey Room",
  "sample_copy": [
    "Clean, quiet fragrance for daily rituals.",
    "Soft musk and dry woods for calm afternoons."
  ]
}
```

### Response

```json
{
  "tone": "minimal literary",
  "preferred_descriptors": ["clean", "quiet", "soft", "dry"],
  "avoid": ["overly sweet", "loud", "mystical"],
  "metaphor_level": 0.18
}
```

---

## 6. Ontology Lookup

```http
GET /api/v1/ontology/notes/{note_id}
GET /api/v1/ontology/accords/{accord_id}
GET /api/v1/ontology/scenes/{scene_id}
```

### Purpose

Expose ontology seed data for frontend explainability.

---

## 7. Feedback Log

```http
POST /api/v1/feedback
```

### Request

```json
{
  "output_id": "out_123",
  "action": "accepted",
  "edited_copy": "optional edited copy",
  "labels": ["commercially_usable", "clear", "not_too_abstract"]
}
```

### Feedback Actions

- accepted
- copied
- exported
- edited
- rejected_too_abstract
- rejected_too_generic
- rejected_brand_mismatch
- rejected_claim_risk

## Implementation Notes

### MVP

- Use FastAPI or Express.
- Store requests, outputs, and feedback in PostgreSQL.
- Use JSON files for ontology seed.
- Use OpenAI structured outputs for planner and critic.

### Later

- Add pgvector for similar-output retrieval.
- Add Neo4j for graph exploration.
- Add admin dashboard for brand memory and ontology editing.

## API Principle

Every generated copy should be traceable to:

1. fragrance notes
2. scene anchors
3. brand constraints
4. controlled symbolic operators
5. critic scores
