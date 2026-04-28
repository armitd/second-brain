---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/One research task adds 10% to your Claude Code context....md"
date_processed: "2026-04-27"
created: "2026-04-27 17:14"
title: "Sub-Agents Preserve Claude Code Context — CLI / API / MCP Cost Hierarchy"
author: "Aakash Gupta (@aakashgupta)"
url: "https://twitter.com/aakashgupta/status/2041666842411069729"
tags: ["#readwise", "#thread", "#claude-code", "#context-engineering", "#sub-agents", "#mcp"]
relevance: "high"
related_projects: []
competitive_intel: false
status: "processed"
---

# Thread: Sub-Agents Preserve Claude Code Context — CLI / API / MCP Cost Hierarchy

## Summary
Aakash Gupta measures the context cost of Claude Code operations. A single research task without a sub-agent consumed 9% of the context window (16%→25%); the same task run via a sub-agent consumed only 0.5% (16%→16.5%). Also establishes the MCP cost hierarchy: MCP tools are always loaded into context even when not used, making them the most expensive per-token; CLI tools cost zero context; API calls are mid-range.

## Key Points
- **Sub-agents dramatically reduce context consumption:** same research query 9% without sub-agent vs 0.5% with
- **MCP tools are the most expensive:** always loaded into context window regardless of whether called — choose MCP integrations selectively
- **CLI tools cost zero context:** the cheapest way to extend Claude Code's capabilities
- **API calls mid-range:** between free CLI and always-on MCP
- **Practical rule:** use sub-agents for research and long-running tasks; prefer CLI over MCP for lightweight integrations

## Why It Matters
Directly relevant to COG architecture. The MCP always-on cost is a key design constraint — every MCP integration should be justified. Sub-agent delegation (already built into COG team mode) is vindicated by this data.

## Full Thread
[[Readwise/Full Document Contents/Tweets/One research task adds 10% to your Claude Code context....md|Full thread →]]

---
*Processed from Readwise by COG*
