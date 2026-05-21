---
type: "pattern-analysis"
pattern: "three-layer-data-architecture-agentic-ai"
created: "2026-05-21"
domains: ["professional", "enterprise-architecture", "data-architecture", "agentic-ai"]
frequency: "emerging"
tags: ["#pattern", "#analysis", "#data-architecture", "#agentic-ai", "#semantic-layer", "#zero-copy", "#data-governance"]
---

# Pattern: Three-Layer Data Architecture for Agentic AI

## Pattern Description

Enterprise AI quality failures are almost always misdiagnosed as model problems. The actual failure is in the data stack — and specifically in one or more of three layers that must all be functioning for AI agents to produce trustworthy, consistent output.

The three layers are ordered. Each is a prerequisite for the next:

```
Layer 3 — Meaning:    Semantic governance  — what does the data mean?
Layer 2 — Quality:    Data governance      — is the data trustworthy?
Layer 1 — Movement:   Efficient transport  — does the data arrive at all?
```

**The failure mode this pattern describes:** Data that arrives fast, clean, and meaningless.

An organisation can have world-class data infrastructure (Layer 1) and rigorous data quality controls (Layer 2) and still deploy AI agents that produce inconsistent, contradictory, or wrong outputs — because different agents interpret the same data differently (Layer 3 missing).

---

## The Three Layers in Detail

### Layer 1 — Movement: Efficient Transport

**The question:** Does the data arrive at the agent without unnecessary copying, latency, or loss?

**What this layer covers:**
- Physical data transport — zero-copy patterns, memory-mapped files, sendfile, DMA transfer
- Streaming architecture — Kafka, Arrow Flight, change data capture
- Pipeline design — avoiding unnecessary ETL hops, zero-copy data sharing (Snowflake), logical-first architecture

**Why it matters for AI:** Language models and agent frameworks are sensitive to context window size and latency. Data that is copied multiple times between systems introduces staleness, versioning risk, and pipeline complexity. Zero-copy principles applied to AI data pipelines mean: don't move data to the agent if you can move the agent to the data.

**When Layer 1 is missing:** Agents wait on slow pipelines. Training data is stale. Context windows are consumed by redundant data rather than signal. The model appears to underperform — but the bottleneck is infrastructure.

**Source:** [[05-knowledge/research/2026-05-21-zero-copy-architecture|Zero-Copy Architecture Research Paper]]

---

### Layer 2 — Quality: Data Governance

**The question:** Is the data trustworthy — profiled, lineage-tracked, and quality-controlled?

**What this layer covers:**
- Data quality profiling — completeness, accuracy, consistency, timeliness
- Data lineage — traceable from source to consumption, auditable for AI governance
- Data catalog — discoverable, understood by the teams building agents on top of it
- AI governance — model cards, risk scoring, policy gates (EU AI Act compliance)
- Master data management — canonical definitions of core business objects

**Why it matters for AI:** Only 38% of organisations have established data quality standards for AI training data (Informatica, 2026). An agent trained or grounded on unvalidated data will confidently return wrong answers. Quality problems at Layer 2 are invisible at Layer 3 — the semantic layer will interpret bad data consistently, which is worse than inconsistently (it makes errors harder to detect).

**When Layer 2 is missing:** AI training data is unvalidated. Model outputs are accurate-sounding but factually wrong. Lineage gaps make EU AI Act compliance impossible. Grounding retrieval returns plausible but inaccurate context.

**Source:** [[03-professional/braindumps/braindump-2026-05-14-1444-informatica-idmc-beyond-mdm|Informatica IDMC Braindump]]

---

### Layer 3 — Meaning: Semantic Governance

**The question:** Does the data mean the same thing to every system and agent that reads it?

**What this layer covers:**
- Controlled vocabulary — canonical definitions of business terms (customer, job, resolution, escalation, SLA)
- Ontology — structured relationships between concepts, not just definitions
- Evaluation rules — explicit, ontology-driven logic for the evaluate stage of agent workflows (not LLM inference)
- Cross-agent consistency — ensuring separate agents operating in parallel resolve to the same interpretation of shared terms

**Why it matters for AI:** A single agent making a mistake is a bug. Ten agents each making different-but-internally-consistent mistakes is an undetectable governance failure. Without Layer 3, agents that operate across business units, opcos, or product domains will each develop independent interpretations of the same business vocabulary — what Darlene Newman calls "parallel realities."

**The key architectural principle:** The tooling for semantic management can be purchased (dbt, Atlan, Collibra, graph databases). The *meaning itself* — the shared definitions, the controlled vocabulary, the ontology — must be built and governed by the organisation. It cannot be bought.

**Evaluate stage specifically:** The stage at which an agent checks its output against business rules should use explicit rule logic, not ask the model to evaluate. LLM evaluation is non-deterministic; rule-based evaluation is auditable.

**When Layer 3 is missing:** Agents return fast, clean answers that contradict each other across teams or systems. The same question asked of two agents produces two different answers — each defensible, neither wrong by its own logic. Debugging is nearly impossible because there is no single point of failure.

**Source:** [[03-professional/braindumps/braindump-2026-05-21-1700-semantic-layer-governance-newman|Semantic Layer Governance Braindump]] (Darlene Newman)

---

## Failure Mode Analysis

Solving two of three layers still produces AI failure:

| Layer 1 Movement | Layer 2 Quality | Layer 3 Meaning | Outcome |
|:---:|:---:|:---:|---|
| ✅ | ✅ | ❌ | Fast, clean answers that mean different things in different contexts. Agents contradict each other. Hard to detect. |
| ✅ | ❌ | ✅ | Fast, consistently-interpreted answers based on bad data. Confident and wrong. Harder to detect than inconsistency. |
| ❌ | ✅ | ✅ | Trustworthy and consistent but slow. Pipeline bottlenecks. Model appears to underperform. |
| ✅ | ❌ | ❌ | Fast delivery of wrong, inconsistent answers. Obvious failure — easiest to detect and fix. |
| ❌ | ❌ | ✅ | Slow delivery of bad data with a consistent interpretation. |
| ❌ | ❌ | ❌ | Complete failure. No ambiguity about what needs fixing. |

**The most dangerous failure mode is Layer 3 missing with Layers 1 and 2 present.** An organisation with good infrastructure and data quality controls will trust the outputs of its AI agents — until those agents are compared against each other and the contradictions surface. By then, decisions have been made on bad data.

---

## The EA Positioning Argument

The practical value of this pattern for Enterprise Architecture:

**Before deploying another agent, audit the stack.** Most enterprise AI projects fail at Layer 3 (never established shared meaning) or Layer 2 (underestimated data quality for AI). They rarely fail at Layer 1 (infrastructure). Yet organisations invest disproportionately in model selection and infrastructure, and underinvest in governance and meaning.

**The diagnostic question to ask of any AI deployment:** Which layers are present, which are absent, and which layer is the actual bottleneck?

**The repositioning this enables for EA:** EA's role is not to slow down AI deployment — it is to ensure the data stack beneath the model is fit for purpose before deployment. An EA function that can diagnose which layer is missing, and map that to existing platform capabilities (Informatica for Layer 2, semantic governance programme for Layer 3), is directional rather than procedural.

---

## Connections to Active Projects

| Project | Layer | Gap |
|---|---|---|
| **AI Damage Assessment PoC** | Layer 2 | Training data quality not yet validated against IDMC standards |
| **MCP Governance** | Layer 3 | MCP tools return data without semantic context — agents interpret independently |
| **Contact Centre of the Future** | Layer 3 | "Resolution", "escalation", "satisfaction" need consistent definitions across all CC AI agents |
| **Microsoft single-tenant strategy** | Layer 1 | Cross-opco data movement patterns depend on tenant consolidation decision |
| **Informatica IDMC audit** | Layer 2 | Full platform capabilities (DQ, Catalog, Governance) may already be licensed but inactive |

---

## Sources

- [[05-knowledge/research/2026-05-21-zero-copy-architecture|Zero-Copy Architecture Research Paper]]
- [[03-professional/braindumps/braindump-2026-05-14-1444-informatica-idmc-beyond-mdm|Informatica IDMC Braindump]]
- [[03-professional/braindumps/braindump-2026-05-21-1700-semantic-layer-governance-newman|Semantic Layer Governance Braindump]]

---

*Pattern synthesised 2026-05-21 from zero-copy research, Informatica IDMC analysis, and Darlene Newman's semantic layer framework*
