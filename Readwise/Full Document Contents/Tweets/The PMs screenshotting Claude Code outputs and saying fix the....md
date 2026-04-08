# The PMs screenshotting Claude Code outputs and saying "fix the...

![rw-book-cover](https://pbs.twimg.com/profile_images/2021355466216062976/8MDXp7vR.jpg)

## Metadata
- Author: [[Aakash Gupta]]
- Full Title: The PMs screenshotting Claude Code outputs and saying "fix the...
- Category: #tweets
- Summary: The PMs screenshotting Claude Code outputs and saying "fix the alignment" five times are playing QA on a system that can QA itself.

The default workflow for anything visual: generate a slide, screenshot it, give feedback, screenshot again, give more feedback. Five rounds of you being the quality layer between Claude and the final output.

A Puppeteer skill eliminates that loop completely. You embed a screenshot tool directly in the skill file. Claude renders HTML, captures its own output, measures whether text overflows the page dimensions, and iterates three times before you ever see it. Pixel-level self-correction with zero human review.

One detail that stuck with me: a recent Google paper showed that literally running the same prompt twice improves output quality. The serious Claude Code builders are encoding that into every skill. Generate, re-validate against the original rules, generate again. Quality compounds automatically with each pass.

This is the builder-validator pattern. The AI does the work, then the AI audits the work against the same spec. You stop functioning as the manual checkpoint.

The setup cost is one skill file with Puppeteer embedded. The return is every visual task from that point forward shipping at production quality without a screenshot loop.

Build the check into the system. Stop being the system.
- URL: https://twitter.com/aakashgupta/status/2039442140405895546/?rw_tt_thread=True

## Full Document
The PMs screenshotting Claude Code outputs and saying "fix the alignment" five times are playing QA on a system that can QA itself.

The default workflow for anything visual: generate a slide, screenshot it, give feedback, screenshot again, give more feedback. Five rounds of you being the quality layer between Claude and the final output.

A Puppeteer skill eliminates that loop completely. You embed a screenshot tool directly in the skill file. Claude renders HTML, captures its own output, measures whether text overflows the page dimensions, and iterates three times before you ever see it. Pixel-level self-correction with zero human review.

One detail that stuck with me: a recent Google paper showed that literally running the same prompt twice improves output quality. The serious Claude Code builders are encoding that into every skill. Generate, re-validate against the original rules, generate again. Quality compounds automatically with each pass.

This is the builder-validator pattern. The AI does the work, then the AI audits the work against the same spec. You stop functioning as the manual checkpoint.

The setup cost is one skill file with Puppeteer embedded. The return is every visual task from that point forward shipping at production quality without a screenshot loop.

Build the check into the system. Stop being the system. 

Your browser does not support the video tag.

![](https://pbs.twimg.com/profile_images/2021355466216062976/8MDXp7vR.jpg)

[Aakash Gupta](https://twitter.com/aakashgupta)
[@aakashgupta](https://twitter.com/aakashgupta)

This guy literally broke down how to use Claude Code like an expert: 

1:40 - Code vs Cowork vs OpenClaw

6:51 - Setting up context status line

12:03 - Sub-agents

17:49 - Creating skills

23:58 - Ask user questions tool

33:33 - Tool-powered skills: Tavily

36:57 - CLI vs MCP vs API hierarchy

39:30 - Make slides skill w/ Puppeteer

43:32 - Auto-invoking skills with hooks

46:49 - Jupyter notebooks for data trust

55:09 - The operating system file structure 

Your browser does not support the video tag.

[Posted Mar 30, 2026 at 8:21PM](https://twitter.com/aakashgupta/status/2038713289254064321)

---

YouTube:
