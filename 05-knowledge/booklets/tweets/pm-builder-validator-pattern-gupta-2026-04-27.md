---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/The PMs screenshotting Claude Code outputs and saying fix the....md"
date_processed: "2026-04-27"
created: "2026-04-27 17:14"
title: "Builder-Validator Pattern — Puppeteer Self-QA in Claude Code Skills"
author: "Aakash Gupta (@aakashgupta)"
url: "https://twitter.com/aakashgupta/status/2039442140405895546"
tags: ["#readwise", "#thread", "#claude-code", "#puppeteer", "#builder-validator", "#qa", "#skills"]
relevance: "high"
related_projects: []
competitive_intel: false
status: "processed"
---

# Thread: Builder-Validator Pattern — Puppeteer Self-QA in Claude Code Skills

## Summary
Aakash Gupta introduces the builder-validator pattern for Claude Code: instead of humans screenshotting outputs and asking Claude to fix them, embed Puppeteer directly in the skill. Claude renders HTML output, takes a screenshot, measures overflow and layout issues, and iterates up to 3x before the human ever sees it. Supported by a Google paper showing that running the same prompt twice measurably improves quality — the second pass is the validator.

## Key Points
- **Builder-validator pattern:** Claude builds the output, then validates it using Puppeteer screenshots before presenting to humans
- **Puppeteer embedded in skill:** render HTML → screenshot → measure overflow/layout → iterate up to 3x automatically
- **Google paper backing:** running same prompt twice improves output quality — the validator pass is not redundant
- **Eliminates screenshot-feedback loop:** removes the most common PM interaction pattern (screenshot + "fix this") from the human's workflow
- **Applicable beyond UI:** the validate-before-surface principle applies to any Claude output that can be automatically checked

## Why It Matters
Applicable to COG skill development — any skill that generates a document or artefact could embed a lightweight validation step before surfacing to the user. Also relevant to the AI PoC work where Claude Code is generating customer-facing outputs.

## Full Thread
[[Readwise/Full Document Contents/Tweets/The PMs screenshotting Claude Code outputs and saying fix the....md|Full thread →]]

---
*Processed from Readwise by COG*
