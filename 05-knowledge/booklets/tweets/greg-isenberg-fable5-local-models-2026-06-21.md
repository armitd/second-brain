---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/The takeaway from Fable 5 being BANNED by the government....md"
date_processed: "2026-06-21"
created: "2026-06-21 12:09"
title: "The takeaway from Fable 5 being BANNED: local models as insurance"
author: "GREG ISENBERG (@gregisenberg)"
url: "https://twitter.com/gregisenberg/status/2065773938915889253/"
tags: ["#readwise", "#thread", "#foundation-models", "#agentic-ai", "#ai-governance"]
relevance: "high"
related_projects: ["AI Damage Assessment PoC", "MCP Governance"]
competitive_intel: false
status: "processed"
---

# Thread: The Takeaway from Fable 5 Being Banned — Local Models as Insurance

## Summary

Greg Isenberg's immediate response to the Fable 5 export ban: stop building your entire workflow on models that can disappear with a single letter. His answer: get fluent with local models so you have 100% control. The thread is a practical local model setup guide, but the strategic framing is what matters: this is the "lost your Facebook traffic overnight" moment for AI.

## Key Points

- **The principle:** "Don't build your entire workflow on something that can disappear with a single letter. Own part of your stack. Local models are insurance." The parallel to Facebook algo changes killing organic traffic is pointed.
- **Runtime:** Ollama or LM Studio to run models locally
- **Model selection by hardware:** 7B models run on most laptops; 32B needs 32GB+ RAM Mac; 70B needs a DGX Spark or Mac Studio
- **Model-to-job matching:** Qwen 3 (best all-around), DeepSeek (reasoning/coding), Gemma 4 (tiny/phone), Llama (largest community/fine-tunes)
- **Quantization (Q4/Q5):** Shrink a model to weaker hardware with minimal quality loss — this is the key concept that makes local models practical
- **Context window is the real local constraint:** Cloud models give huge context for free; local models make you pay in RAM. Keep sessions tight.
- **Tools matter more than model size:** A smaller local model with web search + file access + code execution beats a larger model with none

## Why It Matters

Directly validates the AIDA PoC architectural principle: multi-model, model-agnostic by design. The Fable 5 ban is now a documented precedent that a cloud model can disappear overnight. For any production AI system Belron builds — AIDA PoC or CCOTF virtual agent — model availability risk needs to be in the architecture, not just in the risk register.

## Full Thread
[[Readwise/Full Document Contents/Tweets/The takeaway from Fable 5 being BANNED by the government....|Full thread →]]

---
*Processed from Readwise by COG · 2026-06-21*
