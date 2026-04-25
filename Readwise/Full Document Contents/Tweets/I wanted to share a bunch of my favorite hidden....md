# I wanted to share a bunch of my favorite hidden...

![rw-book-cover](https://pbs.twimg.com/profile_images/1902044548936953856/J2jeik0t.jpg)

## Metadata
- Author: [[Boris Cherny]]
- Full Title: I wanted to share a bunch of my favorite hidden...
- Category: #tweets
- Summary: Boris Cherny shares his favorite hidden features in Claude Code, like the mobile app and remote control. He highlights powerful tools like /loop, /schedule, and git worktrees for efficient coding. He also recommends using voice input and custom agents to boost productivity.
- URL: https://twitter.com/bcherny/status/2038454336355999749/?rw_tt_thread=True

## Full Document
I wanted to share a bunch of my favorite hidden and under-utilized features in Claude Code. I'll focus on the ones I use the most.

Here goes. 

---

1/ Did you know Claude Code has a mobile app?

Personally, I write a lot of my code from the iOS app. It's a convenient way to make changes without opening a laptop.

Download the Claude app for iOS/Android > Code tab on the left. 

![Image](https://pbs.twimg.com/media/HEnnQaub0AAavjA.jpg?name=orig) 

---

2/ Move sessions back and forth between mobile/web/desktop and terminal

Run "claude --teleport" or /teleport to continue a cloud session on your machine.

Or run /remote-control to control a locally running session from your phone/web. Personally, I have "Enable Remote Control 

---

3/ Two of the most powerful features in Claude Code: /loop and /schedule

Use these to schedule Claude to run automatically at a set interval, for up to a week at a time.

I have a bunch of loops running locally:

* /loop 5m /babysit, to auto-address code review, auto-rebase, and

---

4/ Use hooks to deterministically run logic as part of the agent lifecycle

For example, use hooks to:

- Dynamically load in context each time you start Claude (SessionStart)

- Log every bash command the model runs (PreToolUse)

- Route permission prompts to WhatsApp for you to 

---

5/ Cowork Dispatch

I use Dispatch every day to catch up on Slack and emails, manage files, and do things on my laptop when I'm not at a computer. When I'm not coding, I'm dispatching.

Dispatch is a secure remote control for the Claude Desktop app. It can use your MCPs, browser, 

---

6/ Use the Chrome extension for frontend work

The most important tip for using Claude Code is: give Claude a way to verify its output. Once you do that, Claude will iterate until the result is great.

Think of it like any other engineer: if you ask someone to build a website but 

---

7/ Use the Claude Desktop app to have Claude automatically start and test web servers

Along the same vein, the Desktop app bundles in the ability for Claude to automatically run your web server and even test it in a built-in browser.

You can set up something similar in CLI or 

---

8/ Fork your session

People often ask how to fork an existing session. Two ways:

1. Run /branch from your session
2. From the CLI, run claude --resume <session-id> --fork-session

![Image](https://pbs.twimg.com/media/HEnycEgaQAADXoU.jpg?name=orig) 

---

9/ Use /btw for side queries

I use this all the time to answer quick questions while the agent works 

![Image](https://pbs.twimg.com/media/HEn0JM2bEAAZ_po.jpg?name=orig) 

---

10/ Use git worktrees

Claude Code ships with deep support for git worktrees. Worktrees are essential for doing lots of parallel work in the same repository. I have dozens of Claudes running at all times, and this is how I do it.

Use claude -w to start a new session in a 

---

11/ Use /batch to fan out massive changesets

/batch interviews you, then has Claude fan out the work to as many worktree agents as it takes (dozens, hundreds, even thousands) to get it done. 

Use it for large code migrations and others kinds of parallelizable work. 

---

12/ Use --bare to speed up SDK startup by up to 10x

By default, when you run claude -p (or the TypeScript or Python SDKs) we search for local [CLAUDE.md](http://CLAUDE.md)'s, settings, and MCPs.

But for non-interactive usage, most of the time you want to explicitly specify what to load via 

![Image](https://pbs.twimg.com/media/HEn6dsabEAAQQE1.jpg?name=orig) 

---

13/ Use --add-dir to give Claude access to more folders

When working across multiple repositories, I usually start Claude in one repo and use --add-dir (or /add-dir) to let Claude see the other repo. This not only tells Claude about the repo, but also gives it permissions to 

---

14/ Use --agent to give Claude Code a custom system prompt & tools

Custom agents are a powerful primitive that often gets overlooked.

To use it, just define a new agent in .claude/agents, then run claude --agent=<your agent's name>

[code.claude.com/docs/en/sub-ag…](https://code.claude.com/docs/en/sub-agents) 

![Image](https://pbs.twimg.com/media/HEoE3ijagAAKFSb.jpg?name=orig) 

---

15/ Use /voice to enable voice input

Fun fact: I do most of my coding by speaking to Claude, rather than typing.

To do the same, run /voice in CLI then hold the space bar, press the voice button on Desktop, or enable dictation in your iOS settings. 

---

Hope this was useful! I wanted to keep going but had to stop myself. Will post more soon.

What are your favorite underrated Claude Code features?
