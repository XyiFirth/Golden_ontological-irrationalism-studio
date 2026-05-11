# Data Sources and Legal Strategy

## Goal

Scent Myth Engine needs fragrance knowledge, but it should not depend on legally risky scraping as its core asset.

The product should begin with a small curated ontology and expand through brand-approved data and user feedback.

## Data Categories

### 1. Fragrance Note Vocabulary

Needed fields:

- note name
- note family
- common descriptors
- volatility layer: top / middle / base
- seasonality
- commercial tone: clean / sensual / cozy / fresh / woody / green
- risk tags: allergen mention, medical claim risk, cultural sensitivity

Initial strategy:

- manually curate a small seed vocabulary
- use public educational references only for inspiration
- avoid copying proprietary descriptions

### 2. Accord Vocabulary

Needed fields:

- accord name
- typical notes
- sensory profile
- common use occasions
- associated emotions

Examples:

- green musk
- clean floral
- smoky wood
- citrus aromatic
- wet concrete
- soft amber

### 3. Scene Vocabulary

Needed fields:

- location type
- weather
- time
- object cues
- social context
- emotional affordance

Examples:

- rainy Seongsu street
- quiet hotel hallway
- clean white shirt
- late afternoon cafe
- gallery opening

### 4. Brand Voice Data

Collect only from:

- user-provided brand guidelines
- user-approved output
- public copy with careful paraphrasing
- direct client permission

### 5. Feedback Data

Most important proprietary dataset:

- saved outputs
- copied outputs
- exported outputs
- rejected outputs
- human edits
- selected tone
- purchase or conversion signal if available

## External Source Candidates

### IFRA

Use case:

- safety awareness
- regulatory awareness
- terminology reference

Important:

- do not treat the system as a safety or compliance authority
- avoid making medical, allergen-free, or regulatory claims unless provided by the brand

### Public Perfume Taxonomies

Use case:

- note family inspiration
- vocabulary exploration
- manual ontology design

Caution:

- do not bulk scrape protected websites without permission
- do not copy review text or brand descriptions
- prefer manually curated seed data and licensed datasets

### Brand-Provided Data

Best source for commercial use.

Examples:

- product note pyramids
- brand tone guide
- target audience
- forbidden expressions
- approved copy examples
- existing product pages

### Synthetic Data

Useful for:

- testing the pipeline
- creating edge cases
- generating evaluator examples

Caution:

- synthetic data should not become the only training source
- validate against real brand feedback

## Legal and Ethical Constraints

Avoid:

- copying proprietary perfume descriptions
- claiming medical or therapeutic effects
- claiming exact similarity to another brand perfume
- using celebrity or IP references without permission
- generating fake regulatory or allergen guarantees

Required disclaimers in product docs:

- The system generates marketing copy, not regulatory advice.
- Brands are responsible for ingredient compliance and safety claims.
- Outputs should be reviewed before publication.

## Recommended Data Strategy

### Phase 1: Manual Seed Dataset

Create:

- 100 fragrance notes
- 30 accords
- 50 scene anchors
- 30 emotional descriptors
- 20 brand tone presets
- 20 taboo categories

### Phase 2: Brand Memory

Store:

- brand profile
- product line notes
- approved examples
- rejected examples
- preferred metaphor level

### Phase 3: Feedback Dataset

Build a supervised dataset from:

- accepted outputs
- rejected outputs
- edited outputs
- copy/export events

### Phase 4: Licensed or Partner Data

Add:

- licensed fragrance datasets
- direct brand catalogs
- popup interaction logs

## Core Principle

The moat should not be scraped perfume descriptions. The moat should be structured feedback on which scent narratives are understandable, memorable, and commercially useful.
