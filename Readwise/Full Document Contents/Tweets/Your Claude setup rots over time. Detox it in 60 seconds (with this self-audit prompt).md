# Your Claude setup rots over time. Detox it in 60 seconds (with this self-audit prompt):

![rw-book-cover](https://pbs.twimg.com/profile_images/1633697720291704832/GBmxTCa6.jpg)

## Metadata
- Author: [[Ole Lehmann]]
- Full Title: Your Claude setup rots over time. Detox it in 60 seconds (with this self-audit prompt):
- Category: #tweets
- Summary: This tweet contains no text.
- URL: https://twitter.com/itsolelehmann/status/2036533756572639611/?rw_tt_thread=True

## Full Document
![Your Claude setup rots over time. Detox it in 60 seconds (with this self-audit prompt):](https://pbs.twimg.com/media/HEMrxAPW0AA3Crj.jpg)

I deleted half my Claude setup last week and every output got better. 

Sounds backwards...but Anthropic's own prompting docs just explained exactly why this happens. 

Here's the one prompt that tells you what to cut (you don't even have to paste anything, Claude audits your files itself): 

*P.S. If you want AI workflows like this one delivered to your inbox every week, join 35k readers getting them free: [aisolo.beehiiv.com/subscribe](https://aisolo.beehiiv.com/subscribe)* 

#### **What happens to everyone**

You get a bad output. So you add a rule to your [CLAUDE.md](http://CLAUDE.md) (the file where your custom instructions live). *"Be more concise."* 

Next week, another bad output. Another rule. *"Use a casual tone."* 

A month later, something else breaks. *"Always explain technical terms."* 

Each rule makes sense when you add it. You're fixing a real problem you just experienced. It feels productive. 

But nobody ever goes back and removes one. 

3 months in, you've got 89 rules piled on top of each other. 

And the model is trying to satisfy all of them simultaneously, on every single output, whether they're relevant or not. 

It's like handing a chef a 47-step recipe when they only need 12. 

The extra 35 steps just add confusion. 

The chef second-guesses the parts they already know, spends mental energy reconciling steps that contradict each other, and the dish comes out worse than if you'd just **let them cook.** 

That's over-prompting. And almost everyone's setup has it. 

Anthropic's own engineering team recently found the same thing in their internal Claude setups. 

Their scaffolding was actually making the AI worse. 

These are among the smartest people in tech, which means your custom instructions are almost ***certainly*** doing the same thing. 

#### **The Self-Audit Prompt (copy-paste this)**

Instead of manually reading through every file in your setup line by line (which nobody actually does), just tell Claude to audit itself. 

If you're using Claude's desktop app (Cowork), Claude already has access to your whole setup. 

Your [CLAUDE.md](http://CLAUDE.md), your skills folder (where your reusable instruction files live), your context files, everything. It can read all of it without you pasting a single thing. 

Just open a session and copy-paste this: 

```
Read my entire setup before responding. Check my [CLAUDE.md](http://CLAUDE.md), every skill in my skills folder, every file in my context folder, and any other instruction files you can find.  
Then go through every rule, instruction, and preference you found. For each one, tell me:  
1. Is this something you already do by default without being told?  
2. Does this contradict or conflict with another rule somewhere else in my setup?  
3. Does this repeat something that's already covered by a different rule or file?  
4. Does this read like it was added to fix one specific bad output rather than improve outputs overall?  
5. Is this so vague that you'd interpret it differently every time? (ex: "be more natural" or "use a good tone")  
Then give me:  
- A list of everything you'd cut, with a one-line reason for each  
- A list of any conflicts you found between files  
- A cleaned-up version of my [CLAUDE.md](http://CLAUDE.md) with the dead weight removed  

```
One message. Claude reads your entire setup, checks every rule against those 5 filters, and comes back with exactly what to cut and why. 

#### **How to test the trimmed setup**

Once you get the audit back, don't just blindly delete everything it flags. Here's the process: 

1. Read what Claude flagged and why. If you disagree with a specific cut, keep that rule. You know your workflow better than Claude knows your workflow
2. Delete the rest. All of them at once, not one at a time. You want to feel the difference
3. Run your 3 most common tasks with the trimmed setup. The things you use Claude for every day, not edge cases
4. Did the outputs stay the same or get better? The deleted rules were confirmed dead weight. Leave them gone
5. Did one specific thing get worse? Add back just that one rule

The goal is to find your minimum viable setup. The fewest instructions that consistently get you the output quality you want. 

#### **Make it run automatically (so your Claude hygiene stays clean)**

The audit only works if you actually do it. And you won't remember to paste that prompt every few weeks. I definitely wouldn't. 

So instead of relying on willpower, turn it into a scheduled task that runs itself. 

Cowork has a built-in scheduling feature that lets you set up any prompt to fire on a recurring basis. 

Here's how to set it up (takes about 45 seconds): 

1. Open Cowork
2. Tell it:

```
Create a weekly scheduled task called "setup-audit" that runs every Monday at 9am.  
The task should: read my entire setup ([CLAUDE.md](http://CLAUDE.md), all skills, all context files, everything), then audit every rule against these 5 filters:  
1. Is this something you already do by default?  
2. Does it contradict another rule somewhere else?  
3. Does it repeat something already covered?  
4. Does it look like a bandaid for one bad output?  
5. Is it so vague you'd interpret it differently every time?  
Then give me a list of what to cut with reasons, any conflicts between files, and a summary of how many rules passed vs got flagged. Don't change any files, just report.  

```
Cowork creates the task and puts it in your Scheduled section in the sidebar 

Every Monday morning you get a fresh audit report without doing anything. 

Read it, delete what's flagged, then move on with your week. 

That's it. One setup, and your prompt hygiene runs on autopilot. 

(The first time it runs, it'll ask you to approve tool access. After that it runs silently in the background.) 

Your AI setup should be getting simpler over time. 

Every model update and every skill you add will likely make some of your old instructions unnecessary. 

The people getting the best outputs are the ones who regularly cut the dead weight. You are now one of them. 

Addition by subtraction :) 

*P.S. I'm hosting an in-depth Claude Cowork workshop soon, where I'll teach you how to leverage it to get the output of a $500k/year marketing team.* 

*180 people joined last time.* 

*You can pre-register to reserve a spot here (no payment needed): <https://tally.so/r/LZbxKl>*
