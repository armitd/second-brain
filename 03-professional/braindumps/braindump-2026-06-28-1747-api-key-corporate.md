---
type: "braindump"
domain: "professional"
date: "2026-06-28"
created: "2026-06-28 17:47"
themes: ["api-key", "cog-automation", "corporate-vs-personal"]
tags: ["#braindump", "#cog", "#action-required"]
status: "captured"
energy_level: "low"
emotional_tone: "neutral"
confidence: "high"
---

# Braindump: Switch COG Scripts to Corporate API Key

## Raw Thoughts
Need to remind myself to edit the API key in the Python code for the lecture function — use corporate key not personal one.

## Action Items

### Immediate
- [ ] Top up personal Anthropic account at console.anthropic.com to unblock lecture testing 📅 2026-06-29
- [ ] Update `ANTHROPIC_API_KEY` in `~/.zprofile` to the corporate API key when access is available 📅 2026-06-29

## Processing Notes

**Note:** The API key is not hardcoded in the Python scripts — it is read from the `ANTHROPIC_API_KEY` environment variable, which the launchd wrappers source from `~/.zprofile`. The fix is to update the key value in `~/.zprofile`, not in the Python code itself.

Three of the four COG automation scripts need the API key (`vault_review.py`, `article_processor.py`, `lecture_processor.py`). `run_daily_brief.sh` uses Claude Code's own auth and is unaffected.

**Current blocker:** Personal API account has insufficient credits — lecture processor failed on first test. The YouTube URL is still in `lecture_queue.txt` and will process automatically once credits are available or the corporate key is set.

**Options to unblock:**
1. Top up personal account at console.anthropic.com (a few dollars covers significant usage at Haiku/Sonnet rates)
2. Wait for corporate API key access
3. The other three automations (vault review, daily brief, articles) run fine tonight without it

---

*Processed by COG Brain Dump Analyst*
