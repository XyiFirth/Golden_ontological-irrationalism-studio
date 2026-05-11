# MVP Implementation Plan

## Objective

Build a working Scent Myth Engine prototype that can generate commercially usable scent copy from structured fragrance and scene inputs.

## MVP Scope

Must support:

- structured scent request form
- ontology seed lookup
- generation plan creation
- LLM-based copy generation
- critic scoring
- JSON export
- popup card preview

Must not support yet:

- full RDF reasoning
- automated scraping
- fine-tuned model
- regulatory compliance claims
- live Shopify integration

## Week 1: Static Prototype

Tasks:

1. Build input form based on `scent_request.schema.json`.
2. Load `data/fragrance_ontology_seed.json` in browser or backend.
3. Render ontology-mapped anchors.
4. Show generation plan preview.
5. Use static examples first.

Deliverable:

- frontend demo with Seongsu popup example

## Week 2: Backend API

Tasks:

1. Implement FastAPI or Express server.
2. Add `/generate/scent-copy` endpoint.
3. Add `/plan/generation` endpoint.
4. Add schema validation.
5. Add basic rule-based critic.

Deliverable:

- local API with valid request/response cycle

## Week 3: LLM Integration

Tasks:

1. Add planner prompt.
2. Add realizer prompt.
3. Add critic prompt.
4. Force JSON structured outputs for planner and critic.
5. Add retry loop if critic fails.

Deliverable:

- generated product copy with scores

## Week 4: Brand Memory and Feedback

Tasks:

1. Store brand profiles.
2. Store generated outputs.
3. Store feedback labels.
4. Add copy/export tracking.
5. Add admin review page.

Deliverable:

- usable pilot product for 3 to 5 indie brands

## Suggested Tech Stack

### Frontend

- Next.js or React
- Tailwind CSS
- JSON Schema form renderer optional

### Backend

- FastAPI preferred for Python-based model orchestration
- Express acceptable for JS-only stack

### Database

MVP:

- SQLite or PostgreSQL

V1:

- PostgreSQL + JSONB
- pgvector for similar examples

V2:

- Neo4j for graph exploration

### LLM

MVP:

- OpenAI structured outputs for planner and critic
- OpenAI or Claude for final copy generation

## Prompt Chain

### Planner Prompt

Inputs:

- request JSON
- ontology matches
- brand constraints

Output:

- generation plan JSON

### Realizer Prompt

Inputs:

- generation plan JSON
- output type

Output:

- final copy

### Critic Prompt

Inputs:

- final copy
- request JSON
- constraints

Output:

- scores
- warnings
- rewrite instruction if needed

## Rule-Based Guardrails

Reject or rewrite if:

- forbidden word appears
- no concrete scent descriptor appears
- no use situation appears
- too many abstract nouns appear
- medical or therapeutic claim appears
- more than one metaphor appears in one short paragraph

## First Pilot Test

Recruit:

- 3 indie fragrance brands
- 1 pop-up store operator
- 1 lifestyle brand planning scented goods

Ask them to evaluate:

- Would you use this on a product page?
- Would you use this on a pop-up card?
- Is it too abstract?
- Does it sound like your brand?
- What would you edit?

## Success Criteria

MVP is validated if:

- 30%+ of generated outputs are usable without major rewrite
- 60%+ are usable after minor edits
- brands prefer scene-based copy over note-list copy
- popup card format is seen as shareable

## Next Step After MVP

Build the feedback dataset. The most important asset is not the seed ontology or LLM prompt. It is the edited and approved scent copy from real brands.
