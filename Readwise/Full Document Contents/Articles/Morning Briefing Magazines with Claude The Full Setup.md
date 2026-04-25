# Morning Briefing Magazines with Claude: The Full Setup

![rw-book-cover](attachment:ea62f7bc-0f10-425e-ba1f-517f21edaa77:Notion_Banners.webp)

## Metadata
- Author: [[versed-keyboard-69d on Notion]]
- Full Title: Morning Briefing Magazines with Claude: The Full Setup
- Category: #articles
- Summary: This guide shows how to create a personalized daily magazine using Claude Cowork that gathers news you care about and skips what you don’t. You customize your sources, topics, and style, then it runs automatically every morning as a stylish HTML file. It's quick to set up and helps you start the day informed and inspired.
- URL: https://versed-keyboard-69d.notion.site/Morning-Briefing-Magazines-with-Claude-The-Full-Setup-34529316004781b887c4d250e2d3ad78?pvs=149

## Full Document
![](https://www.notion.so/image/attachment%3Aea62f7bc-0f10-425e-ba1f-517f21edaa77%3ANotion_Banners.webp?table=block&id=34529316-0047-81b8-87c4-d250e2d3ad78&spaceId=8a287078-c4d7-4453-a419-fcf84efa9342&width=2000&userId=&cache=v2)
![📰 Page icon](https://notion-emojis.s3-us-west-2.amazonaws.com/prod/svg-twitter/1f4f0.svg)

> Hey! I’m so excited that you’re here! This is such a fun (and powerful) scheduled task to set up in Claude - it will give you a curated morning briefing based on your areas of interest + make it look super cute too!   
> Built by [The Limitless Jess](https://www.instagram.com/thelimitlessjess/)​

##### What you're about to build

A custom daily magazine that:

* Pulls stories from the publications you actually trust
* Covers only the topics you care about
* Is written through your lens (your work, your goals, your life)
* Lands on your laptop every morning at the time you choose
* Reads like a real magazine, not a wall of AI text

Takes about 10 minutes to set up. Then it runs on autopilot forever.

![](https://www.notion.so/image/attachment%3A32cbb035-eb8c-49c7-bc26-6b847c0ea6fb%3A4cb98377-5dfa-4159-8314-82324e5c9af7.png?table=block&id=34529316-0047-807c-9bce-f2e32d078181&spaceId=8a287078-c4d7-4453-a419-fcf84efa9342&width=1420&userId=&cache=v2)
#####  Before you start: you need Claude Cowork

This is the most important thing on the page, so please don't skip it.

This setup only works in Claude Cowork, not in the regular Claude chat on [claude.ai](http://claude.ai/) or the app.

Why? Because your magazine needs to run as a scheduled task (meaning Claude automatically runs the prompt every morning without you having to do anything). Scheduled tasks only live inside Cowork.

Claude Cowork is a free desktop tool from Anthropic designed for non-developers to automate exactly this kind of thing. You can download it here: <https://claude.com/product/cowork>

![](https://www.notion.so/image/attachment%3A324985cc-e866-44ee-879c-45db87b033ab%3AScreenshot_2026-04-17_at_12.02.43.png?table=block&id=34529316-0047-8008-bd81-e9704860908b&spaceId=8a287078-c4d7-4453-a419-fcf84efa9342&width=1420&userId=&cache=v2)
##### Step 1: Open Cowork and start a new chat

Once Cowork is installed, open it up and start a new conversation from the “Scheduled” option in the left-hand menu, then click “New Task” in the top right-hand corner:

![](https://www.notion.so/image/attachment%3A8ac65d8a-907b-473c-a7c0-e053eb867708%3AScreenshot_2026-04-17_at_12.04.26.png?table=block&id=34529316-0047-8063-84c4-d385ce7ebe47&spaceId=8a287078-c4d7-4453-a419-fcf84efa9342&width=1420&userId=&cache=v2)
##### Step 2: Personalise your prompt

Here's the prompt. Before you paste it in, you need to customise 4 things (highlighted in brackets). This is the part that turns a generic news summary into YOUR magazine.

###### The 4 things to customise:

1. Your sources

The publications, newsletters and sites you'd actually read if you had the time. For example: CNN, The Economist, TIME, The Cut, Refinery29, The Verge and TechCrunch, Vogue Business, Morning Brew, Bloomberg, The Hustle, Substack writers you love….

2. Your topics (5 to 7)

This is what you actually care about (and deserves your attention). Mine are AI, the creator economy, current affairs, pop culture and women + work. Yours might be parenting, wellness, property, business, politics, travel.

3. Your skip list

The stuff you don't want. Mine skips crypto, sports etc. Yours could skip anything that bores you or stresses you out.

4. Your lens

Tell Claude who YOU are, so every story comes with a "so what does this mean for me." Be specific about your work, your life stage, your goals.

###### Copy this prompt (then personalise the bracketed bits):

```
Build me a daily "Morning Edition" magazine.  
Sources to pull from every morning: [ADD YOUR SOURCES HERE: publications, newsletters, sites, specific writers]  
Topics I care about: [ADD YOUR 5 TO 7 TOPICS]  
Topics to skip: [ADD WHAT YOU DO NOT WANT, e.g. crypto, sports, celebrity gossip]  
My lens (read this carefully): I'm [WHO YOU ARE: your work, your life, what you are building or working towards]. Filter every story through: does this affect my work or life, is this something I'd want to talk about, or is this something I could create content on or use at work? Lead every story with why it matters to me specifically.  
Curate the top 10 stories that fit my taste. Flag any story that's directly urgent or actionable for me with a ⚡ icon at the top.  
Writing style: Each story gets 2 to 3 tight paragraphs. No fluff, no filler, no "according to sources." Lead with the insight or the "why I should care," then the details. Think editorial, not AI summary.  
Design: Render as a single self-contained HTML file styled like an editorial magazine. Use Fraunces and Inter via Google Fonts. Huge display typography throughout (no small fonts anywhere). Include a "jump to section" nav at the top. Give each of the 10 stories its own distinct spread: different background colours, layouts, and numeral treatments (hero, dark/midnight, rose-alert-stamp, terminal, academic drop-cap, big-stat finish, magazine pull-quote, etc.).  
Save to a magazines/ folder, named YYYY-MM-DD.html.  
Schedule this to run daily at 7am so it's ready when I wake up.  
​
```

I actually run mine at 10am because Cowork needs your computer to be active in order for tasks to run, so I want to make sure I’m sitting at my desk with my computer on:

![](https://www.notion.so/image/attachment%3A65a40d06-f147-4ab9-8276-31fea3f07c9a%3AScreenshot_2026-04-17_at_12.11.52.png?table=block&id=34529316-0047-80d8-a511-d5f961dbb8ef&spaceId=8a287078-c4d7-4453-a419-fcf84efa9342&width=1420&userId=&cache=v2)
##### Step 4: Let it run once (to test)

Before you go to bed on that first night, run the prompt once manually to make sure everything works. Claude will go off and build your first magazine. It'll save as an HTML file in a

magazines/

folder on your computer (or you can choose another location of course)

Open the file. Read it. Does it feel like YOUR magazine? If something's off, tell Claude what to tweak. For example:

* "Make the stories shorter"
* "Add a fashion section"
* "Less tech, more business strategy"
* "I don't like the pink background on story 3, make them all neutral"

##### Step 5: Wake up to it every morning

That's it. From tomorrow onwards, your magazine will be waiting for you every morning in your

magazines/

folder. Grab your coffee, open today's issue, skim for 5 minutes, and you're the most informed person in the room by 10:15am.

##### A few things worth knowing

What if I don't want to use Cowork?

Can I add or change sources later?

What if Claude can't access a specific source?

Do I need to be technical to do this?

##### One last thing

If you build yours and you love it, I’d love to see it!! Tag me on Instagram @thelimitlessjess or send me a DM with a screenshot. I genuinely love seeing how other women set this up for themselves.

Go build something that makes your mornings smarter.

Jess x

#####  Keep Going with The Limitless Jess

Follow [@thelimitlessjess](https://www.instagram.com/thelimitlessjess/) on Instagram for daily AI tips

>  Built with love by The Limitless Jess - your go-to source for making AI actually work for you.   
> ![](https://www.notion.so/image/attachment%3A1f036868-dfe3-4668-9b15-b8e2358a1c67%3AIMG_2095.jpg?table=block&id=34529316-0047-80a9-a8af-f8e7acb5b94e&spaceId=8a287078-c4d7-4453-a419-fcf84efa9342&width=480&userId=&cache=v2)
