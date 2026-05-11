# Generation Pipeline

## Pipeline Summary

```text
Input
→ schema validation
→ ontology mapping
→ anchor retrieval
→ irrational operator planning
→ commercial copy generation
→ critic scoring
→ rewrite or approve
→ export
```

## 1. Input Parsing

Input must be typed. Free text is allowed, but it should be normalized into structured fields.

Required fields:

- fragrance notes
- intended usage situation
- target impression
- brand tone
- output channel

Optional fields:

- location
- weather
- time of day
- target customer
- forbidden words
- reference copy

## 2. Ontology Mapping

Map inputs to stable categories:

- note family
- accord
- scene type
- emotional valence
- social distance
- commercial use case

Example:

```text
bergamot → citrus / fresh / top note / clean opening
musk → soft / skin / base note / intimate residue
rainy Seongsu → urban / after-rain / concrete / cafe / casual premium
```

## 3. Anchor Retrieval

Retrieve grounded anchors:

- physical sensory descriptors
- concrete scenes
- brand-approved terms
- channel length constraints
- forbidden expressions

The retrieval result should constrain generation, not replace generation.

## 4. Irrational Operator Planning

Choose one to three controlled symbolic operators.

Allowed examples:

- note-to-texture
- weather-to-skin-feel
- location-to-social-impression
- object-to-memory
- time-to-residue

Commercial rule:

- no more than 15~25% of final copy should be symbolic distortion
- the first sentence should be sensory or situational, not philosophical

## 5. Structured Generation Plan

The planner must output JSON before prose.

Plan fields:

- primary_sensory_anchor
- scene_anchor
- usage_situation
- target_impression
- allowed_metaphors
- forbidden_directions
- output_sections

## 6. Realization

The realizer writes the final output based only on the approved plan.

Supported output types:

- product_page
- one_line_hook
- scent_card
- popup_result
- instagram_caption
- ip_collaboration_description

## 7. Critic and Guardrail Layer

Critic checks:

- Is it too abstract?
- Does it mention the actual scent direction?
- Does it include a usage situation?
- Does it make unsupported claims?
- Does it violate brand forbidden words?
- Is the tone consistent?

If failed, produce rewrite instructions and regenerate.

## 8. Export

Export formats:

- JSON
- Markdown
- Shopify product copy block
- popup card copy
- CSV batch output

## Example Output Logic

Input:

```text
Notes: bergamot, iris, musk
Scene: rainy Seongsu cafe afternoon
Target impression: clean but slightly distant
Brand tone: minimal literary
```

Bad output:

```text
A fragrance of ontological longing and urban absence.
```

Good output:

```text
A clean green musk for a rainy afternoon in Seongsu. It opens cool and crisp, then settles like a white shirt after light rain.
```

## Product Principle

Commercial fragrance copy should make the scent imaginable before it makes the brand look intelligent.
