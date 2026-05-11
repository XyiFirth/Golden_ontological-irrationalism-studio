# Ontology Model Comparison

## Design Question

What ontology model should Scent Myth Engine use?

The system needs to represent:

- fragrance notes
- note families
- volatility and drydown
- sensory descriptors
- use situations
- emotional impressions
- brand tone
- IP/world context

## Candidate 1: RDF / OWL

### Strengths

- Strong semantic-web standard
- Formal reasoning support
- Good for explicit class/property logic
- Useful if later integrating with public linked-data resources

### Weaknesses

- High implementation complexity
- Steeper learning curve
- Less convenient for fast product iteration
- LLM integration requires additional mapping layer
- Overkill for MVP

### Best Use

Academic or enterprise semantic interoperability.

### Recommendation

Do not use for v1. Consider only if the project becomes a formal knowledge-graph product.

---

## Candidate 2: Property Graph (Neo4j)

### Strengths

- Excellent relationship modeling
- Intuitive graph traversal
- Good for exploring note-emotion-scene relationships
- Strong visualization tooling

### Weaknesses

- Another database to operate
- Cost/complexity higher than PostgreSQL-only MVP
- Less natural for transactional SaaS data
- Vector search integration exists but is less universal than PostgreSQL + pgvector for simple MVP

### Best Use

When the product needs rich relationship navigation:

- find all scents connected to rainy urban scenes
- trace note → emotion → use-case paths
- generate graph-based explanations

### Recommendation

Good v2 candidate.

---

## Candidate 3: Relational Schema + JSONB

### Strengths

- Simple to build and operate
- Excellent for product data, brands, outputs, user feedback
- JSONB allows flexible descriptors
- Works well with SaaS CRUD workflows
- Easy integration with pgvector

### Weaknesses

- Less elegant for deep graph traversal
- Ontology semantics are enforced by application logic
- Complex many-to-many relationships can become verbose

### Best Use

MVP and early commercial product.

### Recommendation

Use this for v1.

---

## Candidate 4: Hybrid Vector-Graph Architecture

### Strengths

- Combines structured ontology and semantic retrieval
- LLM-friendly
- Can support both deterministic constraints and creative retrieval
- Useful for brand memory and example-based generation

### Weaknesses

- Requires careful schema design
- Risk of confusing semantic similarity with actual fragrance similarity
- Needs evaluation and guardrails

### Best Use

Commercial LLM product with growing data.

### Recommendation

Use a lightweight version in v1:

- PostgreSQL relational schema
- JSONB fields for descriptors
- pgvector for example copy and semantic tags

Then add graph DB in v2 only if relationship traversal becomes a bottleneck.

---

## Recommended v1 Ontology Design

### Tables

```text
brands
brand_profiles
fragrance_products
notes
note_families
product_notes
scene_tags
emotion_tags
copy_examples
generation_outputs
feedback_events
```

### Core Relations

```text
fragrance_product → product_notes → notes
notes → note_families
fragrance_product → scene_tags
fragrance_product → emotion_tags
brand_profile → forbidden_words
brand_profile → preferred_tone_examples
```

### JSONB Metadata Example

```json
{
  "volatility": "top",
  "sensory_descriptors": ["bright", "green", "bitter"],
  "commercial_language": ["fresh", "clean", "light"],
  "avoid_language": ["medical", "chemical"]
}
```

### Vector Usage

Use embeddings for:

- retrieving similar product descriptions
- matching user scene to scent copy examples
- brand-tone memory retrieval
- clustering feedback patterns

Do not use embeddings as the only source of truth for note relationships.

---

## Recommended v2 Ontology Design

Add graph layer if needed:

```text
PostgreSQL = product/user/brand truth
Graph DB = relationship exploration
Vector DB = semantic retrieval
```

Possible graph queries:

```text
fig → green note → after-rain scene → quiet nostalgia → cafe use case
musk → skin scent → intimate distance → daily wear
iris → powdery floral → clean formality → gallery visit
```

## Final Recommendation

For v1:

Use PostgreSQL + JSONB + pgvector.

For v2:

Add Neo4j or ArangoDB only after the system needs rich relationship reasoning, visual graph editing, or complex ontology exploration.
