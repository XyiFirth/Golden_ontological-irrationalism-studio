# Ontology Model

## Purpose

The ontology exists to prevent the product from becoming generic AI perfume copy. It gives the system stable domain structure before any symbolic or irrational transformation happens.

## Core Ontology Domains

### 1. Fragrance Ontology

Entities:

- Note
- Accord
- FragranceFamily
- Concentration
- Intensity
- Projection
- Longevity
- Seasonality
- Occasion
- SensoryDescriptor

Example relations:

- `note_belongs_to_family`
- `note_evokes_descriptor`
- `accord_contains_note`
- `fragrance_has_top_note`
- `fragrance_has_middle_note`
- `fragrance_has_base_note`
- `note_has_volatility_level`
- `note_has_commercial_risk`

### 2. Scene Ontology

Entities:

- Place
- Weather
- TimeOfDay
- Season
- SocialSituation
- Object
- Clothing
- Activity
- CulturalCue

Example relations:

- `scene_has_place`
- `scene_has_weather`
- `scene_implies_occasion`
- `place_affords_emotion`
- `object_evokes_memory`

### 3. Emotion Ontology

Entities:

- Emotion
- Valence
- Arousal
- SocialDistance
- NostalgiaLevel
- RestraintLevel

Example relations:

- `emotion_has_valence`
- `emotion_has_arousal`
- `emotion_matches_fragrance_descriptor`
- `emotion_conflicts_with_brand_tone`

### 4. Brand Ontology

Entities:

- BrandTone
- Audience
- PricePosition
- ForbiddenLexicon
- CopyStyle
- Channel

Example relations:

- `brand_prefers_descriptor`
- `brand_forbids_word`
- `brand_targets_audience`
- `channel_requires_length`

## Modeling Options

### Option A: RDF / OWL / SKOS

Best for:

- formal semantic modeling
- reasoning
- interoperable vocabulary
- long-term knowledge management

Pros:

- strong semantic rigor
- standard ontology tooling
- SHACL validation possible
- good for public ontology publication

Cons:

- slower to build
- more complex developer experience
- overkill for early MVP

### Option B: Property Graph

Best for:

- operational graph queries
- fast traversal
- graph visualization
- flexible relationship modeling

Pros:

- easier to work with than RDF for product teams
- Neo4j has good visualization and query tooling
- ideal for concept relationship exploration

Cons:

- less formal semantics than OWL
- ontology standards are less native

### Option C: Relational + JSONB

Best for:

- MVP and SaaS operations
- brand profiles
- user projects
- logs and exports

Pros:

- simplest to deploy
- easy to combine with app data
- works well with JSON Schema
- low operational complexity

Cons:

- graph reasoning is limited
- relationship exploration is weaker

### Option D: Vector-Graph Hybrid

Best for:

- v2 retrieval
- semantic search over notes, scenes, and prior outputs
- brand memory

Pros:

- retrieves similar scent concepts and brand examples
- useful for personalization
- combines symbolic and semantic similarity

Cons:

- can be harder to debug
- requires quality evaluation to prevent vague retrieval

## Recommendation

### MVP

Use:

- JSON Schema for runtime validation
- PostgreSQL + JSONB for structured storage
- optional pgvector for retrieval
- canonical ontology files in Markdown/JSON

Why:

- fastest to build
- easy to debug
- enough for commercial copy generation
- avoids premature graph complexity

### V1.5

Add:

- Neo4j for graph visualization and relationship traversal
- export from canonical JSON into graph nodes and edges

Why:

- good for showing the ontology visually
- useful for internal authoring and debugging
- easier than full RDF stack

### V2

Add:

- OWL/SKOS/SHACL canonical ontology if external interoperability or formal reasoning becomes important
- RDF triplestore only if clients require enterprise semantic infrastructure

## Practical Modeling Rule

The fragrance ontology should not try to model all perfumery knowledge at first. It should model what improves output quality:

1. note family
2. sensory descriptors
3. seasonality
4. use case
5. emotional associations
6. taboo and risk labels
7. brand tone fit

## Minimum Viable Ontology Classes

```text
FragranceNote
Accord
Descriptor
Scene
Place
Weather
Emotion
BrandTone
UsageOccasion
OutputChannel
IrrationalOperator
Constraint
```

## Minimum Viable Relations

```text
HAS_TOP_NOTE
HAS_MIDDLE_NOTE
HAS_BASE_NOTE
BELONGS_TO_FAMILY
EVOKES_DESCRIPTOR
MATCHES_SCENE
MATCHES_EMOTION
CONFLICTS_WITH_BRAND
ALLOWS_OPERATOR
REQUIRES_CLARITY
```

## Key Principle

The ontology should not make the writing more academic. It should make the output more grounded, consistent, and commercially usable.
