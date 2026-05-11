# Scent Myth Engine MVP

A runnable MVP backend for the Scent Myth Engine: a scene-to-scent translation API for fragrance brands and pop-up personalization.

## What This MVP Does

- Loads `data/fragrance_ontology_seed.json`
- Accepts structured scent requests
- Maps notes, accords, and scenes to ontology anchors
- Builds a generation plan
- Generates commercial scent copy with controlled symbolic language
- Scores the output with a rule-based critic
- Returns JSON compatible with `schemas/scent_output.schema.json`

## Run Locally

```bash
cd apps/scent-myth-engine
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Open:

```text
http://localhost:8000/docs
```

## Test Request

```bash
curl -X POST http://localhost:8000/api/v1/generate/scent-copy \
  -H "Content-Type: application/json" \
  -d @../../examples/seongsu-popup-request.json
```

## Current Mode

This MVP uses a deterministic rule-based generator first. LLM integration should be added after the planner and critic outputs are stable.

## Next Upgrade

Add OpenAI structured outputs for:

1. planner
2. realizer
3. critic

The rule-based system should remain as a fallback and test oracle.
