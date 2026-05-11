# Model and API Comparison

## Modeling Goal

The model stack should not maximize creativity. It should maximize controlled commercial usefulness:

- clear sensory description
- concrete scene anchoring
- low hallucination
- brand-safe symbolic language
- consistent tone across a product line

## Generation Roles

Scent Myth Engine should use multiple model roles rather than one prompt.

### 1. Planner Model

Input:

- fragrance notes
- scene context
- emotional target
- brand constraints

Output:

- structured generation plan
- anchors
- forbidden directions
- allowed irrational operators

### 2. Realizer Model

Input:

- validated plan

Output:

- product copy
- scent card
- pop-up text
- Instagram copy

### 3. Critic Model

Input:

- generated output
- constraints

Output:

- clarity score
- abstraction risk
- commercial readability
- violation list
- rewrite instruction

## Candidate API Families

### OpenAI

Best for:

- structured outputs
- tool calling
- multi-step orchestration
- controllability
- production API reliability

Strengths:

- strong instruction following
- suitable for planner/critic roles
- good JSON adherence
- good for brand-safe constraints

Weaknesses:

- cost must be monitored
- external API dependency

Recommended use:

- MVP planner
- MVP critic
- commercial copy realizer

### Anthropic Claude

Best for:

- long context brand documents
- nuanced writing
- careful tone
- editorial review

Strengths:

- strong prose quality
- strong long-document reasoning
- useful for brand voice analysis

Weaknesses:

- structured API workflow can be less convenient depending on implementation
- cost and latency should be compared per use case

Recommended use:

- alternative realizer
- brand voice analyzer
- long-form campaign editor

### Google Gemini

Best for:

- multimodal expansion
- future image/video/context integration
- large-context retrieval scenarios

Strengths:

- useful if product later includes visual moodboards, packaging, and video references

Weaknesses:

- evaluate output consistency before commercial use

Recommended use:

- v2 multimodal moodboard and pop-up experience assistant

### Open-source Llama / Mistral / Qwen

Best for:

- private deployment
- fine-tuned house style
- lower marginal cost at scale

Strengths:

- data control
- fine-tuning possible
- cost control for high-volume generation

Weaknesses:

- more infrastructure work
- guardrails and quality control become your responsibility
- weaker out-of-box commercial copy reliability than top APIs

Recommended use:

- v2 or enterprise/private mode
- LoRA fine-tuning on approved output pairs

## Recommended V1 Stack

Use API-based LLMs first.

```text
Planner: OpenAI structured output
Realizer: OpenAI or Claude
Critic: OpenAI structured output
Embeddings: OpenAI embeddings or equivalent
Storage: PostgreSQL + JSONB + optional pgvector
```

Why:

- fastest to ship
- least modeling overhead
- strong controllability
- easy to inspect intermediate plans

## Recommended V2 Stack

```text
Planner: OpenAI or fine-tuned small model
Realizer: Claude/OpenAI for premium mode; open-source model for bulk mode
Critic: deterministic rules + LLM judge
Retriever: vector + graph hybrid
Storage: PostgreSQL + pgvector + Neo4j
```

## Irrational Layer Implementation

The irrational layer should not be a separate chaotic model at MVP stage. It should be a controlled operator system.

Operators:

- scene-to-body mapping
- weather-to-emotion mapping
- note-to-memory mapping
- object-to-relationship mapping
- time-to-texture mapping
- material-to-social-impression mapping

Example:

```text
Input: rain, green musk, white shirt, Seongsu cafe
Operator: weather-to-texture
Output: clean musk that settles like a white shirt after light rain
```

## Why Not Train a New Model First?

Training too early is unnecessary.

MVP value comes from:

1. domain ontology
2. structured prompts
3. output constraints
4. brand memory
5. evaluation loop

Fine-tuning should begin only after collecting approved/rejected examples from real brands.

## Fine-tuning Trigger

Start fine-tuning when you have:

- at least 2,000 approved scent copy examples
- rejection labels
- brand tone labels
- copy channel labels
- before/after human edits

Candidate fine-tuning targets:

- rewrite vague copy into concrete scene copy
- classify abstraction risk
- imitate brand-specific tone
- generate compact scent cards

## Model Risk Controls

Risks:

- too abstract
- too generic
- unsupported ingredient claims
- unsafe allergy or medical claims
- luxury cliche overuse

Controls:

- schema validation
- taboo lexicon
- claim filter
- readability metric
- critic rewrite loop
- human approval for client-facing output

## Final Recommendation

Do not build a mystical irrational API first.
Build a controllable symbolic transformation engine around a strong general LLM.

The moat is not the base model. The moat is the fragrance ontology, brand memory, output feedback, and approved commercial scent-writing dataset.
