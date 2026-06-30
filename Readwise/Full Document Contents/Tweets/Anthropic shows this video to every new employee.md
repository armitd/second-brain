# Anthropic shows this video to every new employee

![rw-book-cover](https://pbs.twimg.com/profile_images/2067701265044295680/_WbwZKUv.png)

## Metadata
- Author: [[Raytar]]
- Full Title: Anthropic shows this video to every new employee
- Category: #tweets
- Summary: Anthropic shows this video to every new employee. Someone re-uploaded it.

I hope Anthropic doesn't see this.

14 minutes of how the Claude team actually uses Claude in real work.

I watched the recording last night and kept pausing it. Each time realizing I've been using Claude like a toy.

claude.md + loops is what makes Claude stop fighting you and start working for you.

Most people will keep using Claude the hard way.
- URL: https://twitter.com/Raytar/status/2070219094255599645/?rw_tt_thread=True

## Full Document
Anthropic shows this video to every new employee. Someone re-uploaded it.

I hope Anthropic doesn't see this.

14 minutes of how the Claude team actually uses Claude in real work.

I watched the recording last night and kept pausing it. Each time realizing I've been using Claude like a toy.

[claude.md](http://claude.md) + loops is what makes Claude stop fighting you and start working for you.

Most people will keep using Claude the hard way. 

Your browser does not support the video tag.

![Article cover image](https://pbs.twimg.com/media/HLdRbboXgAAwWuw.jpg)

![](https://pbs.twimg.com/profile_images/2067701265044295680/_WbwZKUv.png)

[Raytar](https://twitter.com/Raytar)
[@Raytar](https://twitter.com/Raytar)

![Stop Being the Loop. Here's How to Make Claude Work While You Sleep.](https://pbs.twimg.com/media/HLdRbboXgAAwWuw.jpg)

The person who built Claude Code at Anthropic stopped prompting Claude.

![](https://pbs.twimg.com/profile_images/1902044548936953856/J2jeik0t.jpg)

[Boris Cherny](https://twitter.com/bcherny)
[@bcherny](https://twitter.com/bcherny)

Hello from Code with Claude Tokyo!! 

![Image](https://pbs.twimg.com/media/HKfyDFoXYAAgRLb.jpg?name=orig) 

[Posted Jun 11, 2026 at 1:39AM](https://twitter.com/bcherny/status/2064885111477219664)

His name is Boris Cherny. In June 2026 he said it out loud: "I don't prompt Claude anymore." 

Loops prompt Claude for him. His actual job now is writing loops. 

That sounds like a flex. But no. It's the biggest shift in how people use Claude and ChatGPT right now. You've probably heard the phrase. Almost nobody does it yet. 

Here is how you work right now. 

* You type a prompt.
* Claude edits a file.
* You run the test.
* It breaks.
* You paste the error back.
* It tries again.

Twenty minutes later you realize you've been babysitting the exact thing you wanted to hand off. 

**You are the loop.** You're the one checking the work and deciding the next step, every single time. That is the job a loop takes over. 

#### One example shows the whole difference

Ask Claude to write you a one page brief on any topic. Simple task. It writes something clean and confident, with sources at the bottom.

![Image](https://pbs.twimg.com/media/HLcRAF0aQAAuwrJ.jpg) 

Now read the sources. **Some of them are fake(!!!)**. Claude made them up and has no idea it did. They look real. The links go nowhere, or they go somewhere that doesn't say what Claude claimed. This is the quiet way Claude burns you, and **a single prompt can never catch it**, because Claude stays confident it's right until something opens the link. 

Now run it as a loop instead. Same brief, but you add a bar it can measure: 

every claim needs at least three sources, and every link has to open to a real page that backs up the claim. 

Watch what happens. Claude writes the brief, then goes link by link. It opens each one. It throws out the dead ones and the fake ones. It finds real replacements. It keeps checking until every single source on the page is something you can open. Then it stops. 

It never gets bored. It never skips the boring ones. 

Here's how you'd write that in Claude Code. Don't worry about the command yet, I break it down below: 

Some content could not be imported from the original document. [View content ↗](https://twitter.com/Raytar/status/2070219094255599645/?rw_tt_thread=True) 

### What a loop is

![Image](https://pbs.twimg.com/media/HLdPrvlWUAAVWIN.jpg) 

A loop is a small system that prompts Claude for you, over and over, until a job is done. 

Every loop, no matter how fancy, is the same five beats: 

1. **Find the work.** Open tasks, failing tests, unread emails, files in a folder.
2. **Do it.** Claude handles one item at a time, like you would by hand.
3. **Check itself.** A second pass confirms the work is done and correct, not just produced.
4. **Remember.** It writes down what's finished, so it never repeats work or loses its place.
5. **Go again.** It repeats until nothing's left, then stops or pings you.

One line to keep: prompting is doing the work. **Loop engineering is managing the worker.** 

#### "Isn't this just a scheduled task?"

![Image](https://pbs.twimg.com/media/HLdOGUyXoAAZSoY.jpg) 

Good question. No. 

You can already make your computer run the same thing every morning at 8am. That's a cron job. It's older than most of us. It runs a fixed script. Same steps, every time, no thinking. 

A loop is different because of one thing: there's **a decision-maker inside it**. 

A cron job runs a script. A loop runs Claude. Claude looks at the current situation, picks the next action, does it, checks the result, and then decides what to do next. Keep going. Try again. Undo. Stop. 

That decision in the middle is the entire point. A script can't look at a broken test and figure out a different fix. Claude can. This only became possible once Claude and ChatGPT got good enough to make real judgment calls mid-job. 

#### The two commands that run a loop

![Image](https://pbs.twimg.com/media/HLdO2TKXQAA6Omo.jpg) 

Here's where most people go wrong. You don't build a loop by typing "do this in a loop" into a normal chat. Claude Code has two commands built in, and which one you reach for depends on the kind of loop you need. 

**1. /goal is the loop that works until it's done.**

![](https://pbs.twimg.com/profile_images/2044472418815893504/xf14RxM8.png)

[ClaudeDevs](https://twitter.com/ClaudeDevs)
[@ClaudeDevs](https://twitter.com/ClaudeDevs)

/goooooal ⚽ 

Your browser does not support the video tag.

[Posted Jun 11, 2026 at 9:58PM](https://twitter.com/ClaudeDevs/status/2065192057535373473)

But obviously not that kind of goal. xD 

You saw /goal up in the brief example. You type it, then describe what "done" looks like. Claude keeps working, turn after turn, on its own. After every turn, a second copy of Claude quietly checks: are we at the goal yet? If not, it tells the first one why, and the work continues. The moment the goal is met, the loop stops by itself. 

That self-check after every turn is the whole difference between a real loop and a prompt that runs once and hopes. 

Use /goal when there's a finish line. Work until this is true. 

**2. /loop is the loop that repeats on a rhythm.** 

Reach for this when the job isn't "finish a pile" but "keep an eye on something." You tell it how often and what to do, and Claude re-runs it for you. 

Some content could not be imported from the original document. [View content ↗](https://twitter.com/Raytar/status/2070219094255599645/?rw_tt_thread=True) 

The 30m means every 30 minutes. You can also just say "every morning, triage my inbox" and Claude will schedule it. 

Use /loop when there's no finish line, just a beat. Check this again and again. 

Most of the strong loops you'll build start with /goal. These are recent Claude Code features, so if you don't see the commands, update Claude Code and they'll show up. 

#### Your first loop, ready to paste

A one line goal is plenty for a small job. For a bigger job with lots of steps, you hand Claude a full charter: where to find the work, how to check itself, how to remember, when to stop. 

Fill in the brackets and paste this into Claude Code: 

You are running as a loop, not answering one prompt. Here is your charter. 

Some content could not be imported from the original document. [View content ↗](https://twitter.com/Raytar/status/2070219094255599645/?rw_tt_thread=True) 

The state file is the quiet hero. Without it, every run starts from zero. With it, the loop picks up exactly where it left off, even when it runs on a schedule. 

#### When not to build a loop

Loops are not free and not for everything. Three honest things before you start. 

1. **One-off tasks don't need a loop.** If the job is a single answer, a plain prompt is faster. Loops earn their setup cost on work that repeats or has many pieces.
2. **Loops cost more.** A loop that checks itself and retries is running Claude several times per item. On a Claude plan, you'll hit your usage limit faster.
3. **Vague work doesn't belong in a loop.** "Think of a better product strategy" is not a loop. Go figure out the actual goal first.

#### Start this week

Pick one task you keep doing by hand, the kind with lots of small pieces. Paste the charter. Fill in the brackets. Run it once while you watch every step. 

When you trust it, put it on a schedule. The first time you wake up to work that finished overnight, you'll stop typing prompts one at a time. Just like Boris.

![Image](https://pbs.twimg.com/media/HLcj4zWawAECxGg.jpg) 

*Helped? Follow me. I share this stuff so you don't have to dig for it* 

[Posted Jun 23, 2026 at 12:13AM](https://twitter.com/Raytar/status/2069212188619805179)
