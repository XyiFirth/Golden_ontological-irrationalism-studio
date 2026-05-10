# Modeling Architecture

## Goal

Build a commercially grounded scene-to-scent generation engine.

The system should avoid two failure modes:

1. Overly technical note listing
2. Overly abstract poetic language

## High-Level Pipeline

```text
User Brief
→ Input Normalization
→ Fragrance Ontology Structuring
→ Scene Ontology Structuring
→ Brand Memory Retrieval
→ Controlled Irrational Transformation
→ Commercial Constraint Check
→ Structured Output
→ Evaluation + Feedback Logging
```

## Component Architecture

### 1. Input Normalizer

Converts free-form user input into structured fields.

Example:

```json
{
  "notes": ["fig", "wet soil", "iris", "musk"],
  "scene": "hotel corridor after rain",
  "emotion": ["quiet jealousy", "old afternoon"],
  "tone": "minimal literary",
  "target_use": "solo cafe / gallery visit"
}
```

### 2. Fragrance Ontology Layer

Stores scent terms, note families, volatility, common impressions, and related consumer language.

Suggested v1 implementation:

- PostgreSQL relational tables
- JSONB metadata for flexible descriptors
- pgvector embeddings for semantic retrieval

### 3. Scene Ontology Layer

Maps scenes into commercially understandable contexts:

- season
- weather
- time
- location
- social distance
- desired impression
- usage situation

### 4. Brand Memory Layer

Stores brand tone, forbidden words, preferred metaphors, existing products, and sample copy.

Recommended storage:

- PostgreSQL table for brand profile
- pgvector for example copy retrieval
- versioned prompt snippets

### 5. Controlled Irrational Layer

Adds poetic displacement without breaking commercial clarity.

Allowed transformations:

- note → physical scene
- scene → wearable impression
- emotion → texture
- memory → aftertaste / drydown

Not allowed:

- inaccessible philosophy
- metaphors without sensory anchor
- hallucinated ingredients
- therapeutic/medical claims

### 6. Commercial Constraint Checker

Checks generated outputs against rules:

- usage scenario exists
- sensory description exists
- abstraction score below threshold
- no forbidden words
- no unsupported ingredient claim
- brand tone consistency

### 7. Output Formatter

Generates multiple formats:

- product page copy
- one-line hook
- scent card
- Instagram caption
- pop-up kiosk result
- Shopify JSON export

## Recommended MVP Stack

```text
Frontend: Next.js / React
Backend: FastAPI or Next.js API routes
DB: PostgreSQL + pgvector
Ontology: relational + JSONB hybrid
LLM: API-based structured generation
Queue: optional, only for batch generation
Hosting: Vercel + Supabase / Render + Neon
```

## Why This Stack

- Lower complexity than Neo4j/RDF for MVP
- Enough structure for ontology-like modeling
- pgvector enables retrieval without separate vector DB
- JSONB allows schema evolution
- Works well with LLM structured output

## v2 Stack

When data volume and relationship complexity grow:

```text
PostgreSQL + pgvector
+ Neo4j or ArangoDB for relationship-heavy exploration
+ evaluation service
+ batch generation workers
+ brand-specific fine-tuning or adapter layer
```

## Non-Goals for MVP

- Do not train a fragrance foundation model.
- Do not claim to predict actual smell perception.
- Do not scrape proprietary review data without license.
- Do not overbuild RDF/OWL before product-market fit.
