# Scent Myth Engine

A scene-to-scent translation engine for indie fragrance brands, pop-up retail, and IP fragrance collaborations.

This project extends Ontological Irrationalism Studio into a commercially grounded fragrance-storytelling system.

## Core Thesis

Fragrance storytelling often fails in two opposite ways:

1. Too technical: ingredient lists that consumers cannot imagine.
2. Too abstract: poetic copy that feels distant from purchase situations.

Scent Myth Engine translates structured scent data, brand tone, use situations, and emotional intent into commercially readable scent narratives.

## Product Positioning

Not an AI copywriter.

A scent-ontology-aware narrative engine.

## Core Formula

```text
Scent Ontology
+ Scene Ontology
+ Brand Constraints
+ Controlled Irrational Layer
= Sellable Scent Scene
```

Commercial mode should keep roughly:

```text
60% sensory clarity
25% situational concreteness
15% poetic distortion
```

The artistic golden-ratio mode can be exposed as a signature mode, but the default commercial fragrance mode must remain more grounded than the original irrational art engine.

## Beachhead Market

Initial market:

- indie niche perfume brands
- Seongsu/Hannam/Yeonnam-style pop-up fragrance brands
- lifestyle brands selling through spatial experience
- content/IP fragrance collaborations

## Recommended MVP Stack

- Frontend: Next.js or static React prototype
- API: FastAPI or Next.js API routes
- Database: PostgreSQL + pgvector for v1
- Ontology v1: relational tables + JSONB schema, graph-ready naming
- Retrieval: pgvector for scent notes, brand examples, scene references
- LLM: OpenAI API with strict structured output for the first MVP
- Guardrails: rule-based abstraction filter + moderation + brand taboo lexicon
- Evaluation: clarity, abstraction risk, situation specificity, brand safety, save/export rate

## Recommended v2 Stack

- Hybrid vector-graph architecture
- Canonical ontology: OWL/SKOS/SHACL files under version control
- Operational graph: Neo4j + n10s or GraphDB/Neptune if RDF-native reasoning becomes important
- Multi-provider LLM gateway: OpenAI + Anthropic + Cohere rerank + optional Mistral/Llama private deployment
- Feedback loop: human edits, brand approval, export/save behavior, kiosk completion data

## Key Modules

1. Fragrance ontology builder
2. Scene ontology builder
3. Controlled irrationality engine
4. Commercial constraint checker
5. Brand memory profile
6. Pop-up personalization flow
7. Shopify/CSV/JSON export
8. IP collaboration adapter
9. Human review and evaluation layer

## Documents

- `docs/product-planning.md`
- `docs/market-strategy.md`
- `docs/business-model.md`
- `modeling/architecture.md`
- `modeling/ontology-model-comparison.md`
- `modeling/api-candidates.md`
- `modeling/generation-pipeline.md`
- `modeling/evaluation-metrics.md`
- `modeling/data-strategy.md`
- `product/popup-flow.md`
- `schemas/fragrance-brief.schema.json`
