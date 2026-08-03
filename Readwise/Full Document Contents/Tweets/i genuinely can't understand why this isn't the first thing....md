# i genuinely can't understand why this isn't the first thing...

![rw-book-cover](https://pbs.twimg.com/profile_images/2077104068128862208/P_qFITRc.jpg)

## Metadata
- Author: [[kai]]
- Full Title: i genuinely can't understand why this isn't the first thing...
- Category: #tweets
- Summary: i genuinely can't understand why this isn't the first thing every claude user builds...

anthropic quietly shipped a folder system where claude loads specialized instructions on its own based on what you ask. no prompt engineering after setup. almost nobody uses it

here's how it actually works...

you drop a folder into your skills directory. inside: a SKILL.md that says "trigger this when the user asks about X". claude reads the description once at startup. next time you ask about X, it silently pulls in the whole skill - custom instructions, scripts, examples - like a specialist walking into the room

1. skill for your writing voice - loads only when you draft, never when you analyze

2. skill for your codebase conventions - loads only when you edit that repo, not others

3. skill for your accounting flow - loads only when you say invoice, receipt, or expense

your context window stays empty until you need it. one claude behaves like 30 different specialists in one chat and you never manage the switching

full breakdown in the article below

i test things like this on myself and share the results. follow @0xkkai if you want to see what's next
- URL: https://twitter.com/0xkkai/status/2083928030930469315/?rw_tt_thread=True

## Full Document
i genuinely can't understand why this isn't the first thing every claude user builds...

anthropic quietly shipped a folder system where claude loads specialized instructions on its own based on what you ask. no prompt engineering after setup. almost nobody uses it

here's how it actually works...

you drop a folder into your skills directory. inside: a [SKILL.md](http://SKILL.md) that says "trigger this when the user asks about X". claude reads the description once at startup. next time you ask about X, it silently pulls in the whole skill - custom instructions, scripts, examples - like a specialist walking into the room

1. skill for your writing voice - loads only when you draft, never when you analyze
2. skill for your codebase conventions - loads only when you edit that repo, not others
3. skill for your accounting flow - loads only when you say invoice, receipt, or expense

your context window stays empty until you need it. one claude behaves like 30 different specialists in one chat and you never manage the switching

full breakdown in the article below

i test things like this on myself and share the results. follow [@0xkkai](https://twitter.com/0xkkai) if you want to see what's next 

![](https://pbs.twimg.com/profile_images/2077104068128862208/P_qFITRc.jpg)

[kai](https://twitter.com/0xkkai)
[@0xkkai](https://twitter.com/0xkkai)

![One Post by Karpathy Made 41,000 Developers Realize They Were Using AI at 5%. Here's the Full Guide](https://pbs.twimg.com/media/HOD6_nSXEAAS-Mz.jpg)

**In April 2026, Andrej Karpathy published 800 words on GitHub that started a mass migration away from traditional AI workflows. This is the engineering guide nobody wrote - with the complete architecture, every prompt, and the math behind why it works.** 

#### The problem Karpathy solved

Every AI tool today has the same flaw: it forgets. 

You upload a PDF. Claude reads it. Gives you a great answer. You close the tab. Tomorrow you upload the same PDF. Claude reads it again. Same tokens. Same processing. Same cost. Zero memory of yesterday. 

Karpathy's insight was that this isn't a model problem. It's an architecture problem. And he solved it with a pattern so simple that most people dismissed it when they first read the gist. 

He called it the **LLM Wiki**.

**Karpathy's core insight:**

Raw documents are source code. A wiki is the compiled product. You don't recompile a program every time you run it. So why are you making AI reprocess your files every session? 

The idea: let AI read your raw documents **once**. Let it extract, structure, and interlink the knowledge into clean wiki pages. Then only ever query the wiki - never the raw files again. 

One-time cost. Permanent knowledge. The gist hit 5,000 stars in days.

![Image](https://pbs.twimg.com/media/HOD7y6DXMAAJOoo.jpg) 

A massive Obsidian vault - thousands of notes, every connection built automatically by Claude 

#### The architecture: three folders that run everything

[Posted Jul 25, 2026 at 1:13PM](https://twitter.com/0xkkai/status/2081005037992464894)
