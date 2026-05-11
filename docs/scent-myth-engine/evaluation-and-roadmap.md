# Evaluation and Roadmap

## Evaluation Philosophy

The system should not be evaluated only on beauty or novelty. It must be evaluated on commercial usefulness.

A good output should be:

- understandable
- sensory
- situational
- brand-safe
- lightly memorable
- not over-abstract

## Core Metrics

### 1. Clarity Score

Question:

Can a consumer understand what kind of scent this is?

Signals:

- mentions sensory category
- mentions note or accord direction
- avoids vague abstraction

### 2. Situation Specificity Score

Question:

Does the copy suggest when or where to wear the scent?

Signals:

- time / season / occasion / social situation present
- concrete scene rather than vague mood

### 3. Commercial Readability Score

Question:

Can this be used on a product page or pop-up card?

Signals:

- short enough
- non-academic language
- no excessive metaphor stacking

### 4. Controlled Irrationality Score

Question:

Is the symbolic layer memorable but not alienating?

Signals:

- one or two fresh metaphors
- metaphor anchored to physical scent
- avoids incoherent dream logic

### 5. Brand Consistency Score

Question:

Does the output fit the saved brand voice?

Signals:

- preferred tone match
- forbidden words absent
- price position supported

### 6. Claim Safety Score

Question:

Does the copy avoid unsupported claims?

Risk examples:

- medical effects
- allergen-free claims
- exact dupe claims
- celebrity or IP misuse

## Scoring Rubric

Each output can be scored 1 to 5.

```text
1 = unusable
2 = weak, needs major rewrite
3 = acceptable draft
4 = commercially usable
5 = strong and brand-ready
```

## Human Feedback Labels

Collect:

- accepted
- copied
- exported
- edited
- rejected_too_abstract
- rejected_too_generic
- rejected_too_strong
- rejected_brand_mismatch
- rejected_claim_risk

## A/B Test Ideas

### Test 1: Note-first vs Scene-first Copy

Compare:

- ingredient-centered copy
- scene-centered copy

Measure:

- preference
- memorability
- purchase intent

### Test 2: Irrationality Ratio

Compare:

- 0% symbolic layer
- 15% symbolic layer
- 35% symbolic layer

Hypothesis:

- 15~25% symbolic layer performs best for commercial fragrance copy

### Test 3: Popup Personalization Card

Compare:

- standard product card
- personalized scent scene card

Measure:

- scan/share rate
- dwell time
- purchase conversion

## Roadmap

### Phase 0: Research Prototype

- static web prototype
- seed fragrance ontology JSON
- no database
- manual prompt chain

### Phase 1: MVP

- typed input schema
- OpenAI structured planner
- realizer and critic chain
- JSON export
- 100-note seed ontology
- local brand memory

### Phase 2: Pilot with Brands

- 3 to 5 indie fragrance brands
- collect approved/rejected outputs
- popup personalization demo
- create feedback dataset

### Phase 3: SaaS Product

- project dashboard
- brand tone memory
- product line management
- Shopify copy export
- CSV batch generation

### Phase 4: API Product

- `/generate/scent-copy`
- `/generate/popup-card`
- `/analyze/brand-tone`
- `/evaluate/copy`
- usage billing

### Phase 5: Expansion

- IP fragrance collaboration module
- location-based scent branding
- oracle/card symbolic product engine
- horror game lore engine reuse

## Key Milestone

The first real validation is not model accuracy. It is whether an indie fragrance brand would use the output on an actual product page or pop-up card.
