# Scent Myth Engine

Scent Myth Engine is a scene-to-scent translation system for fragrance brands, pop-up experiences, and IP-based scent collaborations.

It does not aim to produce abstract poetic copy. Its goal is to translate fragrance notes, scenes, emotions, and brand constraints into commercially usable scent narratives.

## Core Positioning

> Not an AI copywriter. A scene-to-scent translation engine.

The engine combines:

1. **Fragrance ontology**: notes, accords, seasonality, intensity, projection, longevity, safety tags
2. **Scene ontology**: place, weather, time, objects, cultural cues, usage situation
3. **Emotion ontology**: primary emotion, secondary emotion, valence, arousal, nostalgia, restraint
4. **Brand ontology**: voice, taboo lexicon, audience, luxury level, commerciality floor
5. **Controlled irrationality layer**: symbolic distortion operators constrained by brand safety and commercial readability

## Strategic Hypothesis

Fragrance brands do not win by listing ingredients or writing inaccessible poetic copy. They win by owning concrete scenes that consumers can imagine wearing.

Bad direction:

> The scent of ontological longing and inner absence.

Better direction:

> A clean green musk for a rainy afternoon in Seongsu. It opens cool and crisp, then settles like a white shirt after light rain.

## MVP Recommendation

For v1, use a hybrid architecture:

- Canonical ontology files: OWL/SKOS/SHACL-inspired schemas stored in Git
- Operational graph: Neo4j + neosemantics later, JSON graph seed for prototype
- Generation: OpenAI structured-output based planner, realizer, critic
- Retrieval: simple local seed data first; Cohere rerank can be added in v2
- Safety: taboo lexicon, abstraction limit, commerciality floor, human review log

## Folder Structure

```text

docs/scent-myth-engine/
├── README.md
├── architecture.md
├── ontology-model.md
├── model-and-api-comparison.md
├── data-sources-and-legal.md
├── generation-pipeline.md
├── evaluation-and-roadmap.md

schemas/
├── scent_request.schema.json
├── generation_plan.schema.json
├── scent_output.schema.json

data/
├── fragrance_ontology_seed.json

examples/
├── seongsu-popup-request.json
├── seongsu-popup-output.json
```

## Recommended Build Order

1. Fix the 4-layer ontology scope.
2. Create typed JSON schemas for input, planning, and output.
3. Build a no-database prototype with seed JSON.
4. Add OpenAI structured-output generation.
5. Add critic/guard checks before showing outputs.
6. Add brand memory and feedback logs.
7. Move to Neo4j + n10s only when the graph becomes operationally useful.

## Key Principle

The product should not make surrealism louder. It should make surrealism wearable.
