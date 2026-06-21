---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/This is the best site on the internet to learn....md"
date_processed: "2026-06-21"
created: "2026-06-21 12:09"
title: "How LLMs Actually Work — The 5-Stage Pipeline"
author: "Rahul (@sairahul1)"
url: "https://twitter.com/sairahul1/status/2066145067337937029/"
tags: ["#readwise", "#thread", "#foundation-models", "#ai-literacy", "#llm-internals"]
relevance: "high"
related_projects: ["AI Damage Assessment PoC"]
competitive_intel: false
status: "processed"
---

# Thread: The 5-Stage Pipeline Behind Every LLM (GPT, Claude, Gemini, Llama)

## Summary

Rahul's breakdown of how LLMs actually work under the hood — structured as a 5-stage pipeline with code examples and niche build ideas. The core argument: the transformer architecture is the least important part (published, copied, shared). Everything that matters is in the other four stages.

## Key Points

1. **Stage 1 — Data** (where models are actually won): Raw web text is garbage. Multi-step filtering: extract clean HTML, filter harmful/NSFW/PII, deduplicate by URL/document/line, model-based quality scoring. "Data quality beats data quantity. Every time. The most guarded secret in the field is how the data was cleaned."

2. **Stage 2 — Tokenization**: Models read tokens, not raw text. Byte-Pair Encoding (BPE) standard: starts with characters, merges common pairs until fixed vocabulary (32K–100K tokens). Rule of thumb: 1 token ≈ 0.75 words; 100K context ≈ a full novel.

3. **Stage 3 — Training**: Single deceptively simple objective: predict the next token. Do this across trillions of examples and grammar, facts, reasoning, code all emerge. Nobody taught it — it emerged from scale.

4. **Stage 4 — Alignment** (turn text predictor into assistant): Step 1: Supervised Fine-Tuning (SFT) on thousands of prompt → ideal response examples. Step 2: RLHF — model generates two answers, human picks better one, reward model trained on preferences. Without RLHF: fluent, capable, but confidently wrong. With RLHF: helpful, clear, safe.

5. **Stage 5 — Evaluation**: During training: perplexity (how surprised the model is by real text — lower is better). After alignment: perplexity breaks. Switch to human benchmarks: MMLU (academic subjects), Chatbot Arena (human blind comparison), AlpacaEval (LLM-as-judge, 98% correlation with humans). Key: no single score captures a good model.

**5 mistakes that sink LLM projects:** obsessing over architecture; treating data as commodity; skipping scaling math (optimal ratio: ~20 tokens per parameter); stopping at SFT; trusting perplexity after alignment.

## Why It Matters

Foundational AI literacy for understanding the AIDA PoC benchmark design. When comparing Claude Opus 4.8, GPT-5.6, and Gemini 3.5 Pro accuracy on windscreen damage assessment: evaluation methodology is Stage 5 — and no single score captures a good model. The PoC benchmark should include a human-judge comparison, not just automated accuracy metrics. Also: the "data quality beats data quantity" principle applies directly to AIDA training data strategy if Belron ever moves from foundation model to fine-tuned model.

## Reference Link
Best site to learn how LLMs work: [0xkato.xyz/how-llms-actually-work](http://0xkato.xyz/how-llms-actually-work)

## Full Thread
[[Readwise/Full Document Contents/Tweets/This is the best site on the internet to learn....|Full thread →]]

---
*Processed from Readwise by COG · 2026-06-21*
