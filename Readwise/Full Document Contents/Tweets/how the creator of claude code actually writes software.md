# how the creator of claude code actually writes software

![rw-book-cover](https://pbs.twimg.com/profile_images/2005314466255360000/XtVoqVdV.jpg)

## Metadata
- Author: [[Rohit]]
- Full Title: how the creator of claude code actually writes software
- Category: #tweets
- Summary: Boris Cherny runs many Claude AI sessions in parallel to work like a smart team, not just a single assistant. He builds a shared knowledge file and uses planning, verification, and tool integration to make AI coding fast and reliable. This new way of working shows that future software development is about managing AI teamwork, not just writing code.
- URL: https://x.com/rohit4verse/status/2011105761867510229/?s=12&t=iGBahVZb08SpJ-immXsWdQ&rw_tt_thread=True

## Full Document
![how the creator of claude code actually writes software](https://pbs.twimg.com/media/G-d0JYNaMAA4uXZ.jpg)

the creator of claude code just revealed his personal setup and it makes every other workflow look obsolete. 

Boris Cherny runs 5 Claude instances in his terminal. He runs another 10 sessions in the browser. He operates 15 parallel streams of intelligence simultaneously. 

While most developers are still figuring out how to write a decent prompt, he's shipping production features by treating AI like a distributed team working in parallel. 

Here's everything he does that you're not doing.

![Image](https://pbs.twimg.com/media/G-jBsc4bQAQMpY2.jpg) 

#### The Parallel Processing Strategy

Most people use AI like a single assistant. Boris treats it like a development team. 

He numbers his terminal tabs 1 through 5. He uses system notifications to know exactly when a specific Claude instance needs input. Each instance works on different aspects of the same project or completely separate tasks. 

He also runs 5 to 10 Claudes on [claude.ai](http://claude.ai) in parallel with his local instances. 

As he codes in his terminal, he hands off local sessions to the web using the 

'&' command. He manually kicks off sessions in Chrome. He uses --teleport to move context back and forth seamlessly. 

He even starts sessions from his phone using the Claude iOS app in the morning, checking in on them later in the day. 

**This isn't multitasking. This is orchestration.** 

The key insight: When you are blocked on one task waiting for Claude to think or execute, you are not sitting idle. You are managing four other active streams of work. 

#### The Model Choice Nobody Talks About

Boris uses **Opus 4.5 with thinking** for everything. 

Not Sonnet. Not Haiku. Only Opus 4.5. 

Even though Opus is bigger and slower than Sonnet, you have to steer it less. It is better at tool use. It makes fewer mistakes. 

Most developers optimize for **model speed**. Boris optimizes for **total task completion time**. 

This includes all the back-and-forth corrections you make with faster, less capable models. The thinking mode is non-negotiable. It dramatically improves planning quality and reduces the iterations needed to get working code. 

#### The [CLAUDE.md](http://CLAUDE.md) File System

This is where most teams fail with AI coding tools. 

Boris's team shares a single [CLAUDE.md](http://CLAUDE.md) file for the Claude Code repository. It is checked into git. The whole team contributes to it multiple times a week. 

The file contains every mistake Claude has made and every correction the team wants it to remember. 

When Claude does something incorrectly, they add it to [CLAUDE.md](http://CLAUDE.md) so it never happens again.

![Image](https://pbs.twimg.com/media/G-jFRZDawAAn1F4.jpg) 

Different teams maintain their own [CLAUDE.md](http://CLAUDE.md) files. It is the team's responsibility to keep theirs updated. 

During code review, Boris tags `@.claude` on coworkers' pull requests to add items to the file as part of the PR. They use the Claude Code GitHub action to automate this. 

**This is compounding engineering.**

Every mistake becomes institutional knowledge that prevents future mistakes. The AI gets smarter with every sprint.

Context engineering replaces prompt engineering. Instead of writing better prompts, you structure better context through files, folders, and documentation that Claude can reference. 

#### Planning Mode Is Everything

Most sessions start in **planning mode**, accessed by pressing shift + tab twice. 

If the goal is to write a pull request, Boris uses planning mode and goes back and forth with Claude until he likes its plan. Only then does he switch into auto-accept-edits mode. 

With a good plan, Claude can usually one-shot the implementation.

![Image](https://pbs.twimg.com/media/G-jId-4aEAAlLAl.jpg) 

Planning mode is really important. It lets you map out what you're doing and how before jumping in. That gives you time to review the approach, tweak things, and catch bad assumptions (like file formats or how something's actually implemented) before the AI wastes tokens going the wrong way.

It’s basically the measure twice, cut once rule applied to AI coding - having a solid plan matters more than having a perfect prompt.

Aakash Gupta's analysis of workflows emphasizes this exact point: context engineering through folder structure dramatically improves output quality. 

Create directories like: 

* /business-info for strategy docs
* /writing-styles for tone guides
* /examples for past work

Instead of writing massive prompts, you simply say: *"Write a PRD using the style in /writing-styles/[technical.md](http://technical.md) based on the context in /business-info."* 

The CLI shows real-time token usage and cost, forcing you to be aware of context bloat. Use the clear command to reset context between unrelated tasks. 

#### Slash Commands for Inner Loop Workflows

He uses slash commands for every workflow he repeats daily. This saves him from repeated prompting and ensures Claude uses the exact workflow required. 

Commands are checked into git and live in .claude/commands/. 

```
# /commit-push-pr command  
git_status=$(git status --short)  
branch=$(git branch --show-current)Create a commit message for these changes:  
$git\_status

Then push to origin/$branch and open a PR with:  
- Summary of changes  
- Testing completed  
- Any breaking changes  

```
He runs /commit-push-pr dozens of times a day. It’s optimized with inline bash to pre-fetch git info, ensuring the process stays fast and minimizes model lag. 

Slash commands turn repetitive tasks into one command. They are custom APIs for your specific workflow. 

#### Subagents Automate Review Workflows

He uses subagents regularly to handle post-coding tasks automatically. 

A **code simplifier subagent** simplifies code after Claude finishes working. A **verify app subagent** has detailed instructions for testing Claude Code end-to-end.

![Image](https://pbs.twimg.com/media/G-jMh0aaYAA1RLo.jpg) 

You can create persona-based review agents defined by simple text files: 

* A system architect focused on structural organization
* A senior engineer focused on implementation patterns
* An integration specialist focused on interface definitions
* A technical author focused on synthesis and clarity

These agents run concurrently, providing 360-degree reviews of documents instantly. What would take an hour of manual review across different stakeholders happens in seconds. 

Think of subagents like having a junior dev who handles all the repetitive PR stuff. You know - updating dependencies, running formatters, fixing obvious linting issues, that kind of thing. They take care of the tedious checklist items that have to get done anyway, which frees you up to actually think about the interesting problems. 

#### The PostToolUse Hook for Formatting

Boris uses a PostToolUse hook to format Claude's code automatically. 

Claude usually generates well-formatted code out of the box. The hook handles the last 10% to avoid formatting errors in CI later. 

Hooks run automatically after certain events. They are perfect for enforcing team standards without manual intervention every time. 

#### Smart Permission Management

He creates a frictionless environment without sacrificing security. 

He does not use --dangerously-skip-permissions blindly. Instead, he uses /permissions to pre-allow common bash commands he knows are safe in his environment. 

This avoids unnecessary permission prompts while maintaining security. Most of these permissions are checked into .claude/settings.json and shared with the team. 

For very long-running tasks, he either:

Prompts Claude to verify its work with a background agent when done.

Uses an agent stop hook for more deterministic verification.

Uses the ralph wiggum plugin. 

#### Claude Code Uses All Your Tools

This is where the power multiplies exponentially. 

Boris's Claude Code setup:

Searches and posts to Slack via MCP server.

Runs BigQuery queries to answer analytics questions using bq CLI.

Grabs error logs from Sentry. 

The Slack MCP configuration is checked into .mcp.json and shared with the team.

![Image](https://pbs.twimg.com/media/G-jOcF3aMAEVw7d.jpg) 

Claude can analyze a meeting transcript, identify that someone is late on a task, and draft a Slack message using the appropriate internal tone while referencing specific strategic objectives. 

It sounds professional and urgent because Claude has access to **all** the context: the meeting notes, the strategy docs, the writing style guide, and the Slack workspace. 

Model Context Protocols (MCP) turn Claude Code into a universal interface for all your tools. It is not just writing code anymore. It is managing your entire workflow. 

#### The Verification Loop Is Non-Negotiable

The most important tip Boris emphasizes: **give Claude a way to verify its work.** 

If Claude has that feedback loop, it will 2x to 3x the quality of the final result. 

Claude tests every single change landed to [claude.ai/code](http://claude.ai/code) using the Claude Chrome extension. It opens a browser, tests the UI, and iterates until the code works and the UX feels good. 

Verification looks different for each domain:

Running a bash command

Executing a test suite

Testing the app in a browser simulator 

The key is making this verification rock solid. Without it, you are shipping code blind. 

#### What This Actually Means for You

Boris's setup is not just about productivity tricks. It represents a fundamental shift in how software gets built. 

He is not writing code. He is orchestrating a distributed intelligence system where 15 parallel streams work simultaneously. He is not prompting an AI. He is maintaining institutional knowledge through [CLAUDE.md](http://CLAUDE.md) files that make the AI smarter with every interaction. He is not using tools manually. He has given Claude access to every tool in his stack so it can execute entire workflows autonomously. 

The bottleneck isn't the AI's capabilities anymore. It is how well you architect the context, verification loops, and tool access. 

Most developers will keep using AI like a fancy autocomplete. A small number will adopt this workflow and ship 10 times faster than their peers. 

The gap between these two groups will define the next generation of software development. 

The Free Alternative: 

If you want to learn terminal-based AI coding without API costs, **Open Code** gives you similar capabilities. 

While it lacks the polish of Claude Code, it is powerful enough for most use cases and perfect for learning the workflow before committing to paid tools. 

The principles remain the same. Parallel processing, context engineering, verification loops, and tool integration work regardless of which terminal-based AI coding tool you choose. 

Start with Open Code to learn the patterns. Graduate to Claude Code when you are ready to scale.

![Image](https://pbs.twimg.com/media/G-jLzqlbIAAoLBd.jpg) 

The future of software development isn't about writing better code. It's about orchestrating intelligence better. 

Boris figured this out before everyone else. Now you know exactly how he does it.
