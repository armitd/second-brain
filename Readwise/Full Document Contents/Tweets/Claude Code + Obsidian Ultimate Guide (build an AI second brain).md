# Claude Code + Obsidian Ultimate Guide (build an AI second brain)

![rw-book-cover](https://pbs.twimg.com/profile_images/1910271186442846208/vrYKSYRn.jpg)

## Metadata
- Author: [[AI Edge]]
- Full Title: Claude Code + Obsidian Ultimate Guide (build an AI second brain) 
- Category: #tweets
- Summary: This guide explains how to use an AI called Claude Code with Obsidian to build a smart, organized wiki from many documents. The AI reads, summarizes, links, and updates the wiki automatically, making it easier to find and understand information. Users can ask complex questions, get answers, and keep improving their knowledge base without manual editing.
- URL: https://twitter.com/aiedge_/status/2041908011078447222/?rw_tt_thread=True

## Full Document
![Claude Code + Obsidian Ultimate Guide (build an AI second brain) ](https://pbs.twimg.com/media/HFQHXzra4AA-erY.jpg)

Claude Code + Obsidian is the most powerful AI combo I've ever used. 

I literally built an AI second brain that contains everything I think, read, write, research online, and more. 

It contains my business plans, all my YouTube videos (ever), articles I've written, and anything else that is important to me. 

Claude Code + Obsidian has gone mega-viral across all platforms, and for good reason. 

For me personally, this AI system has taken the biggest mental load off my mind, allowing me to focus on what really matters in my business and my personal life.

![Image](https://pbs.twimg.com/media/HFQISiyasAAQlCS.jpg) 

This might look complicated, but it literally only takes 5 minutes to set up, and the crazy part is, it improves over time with a built-in memory system. 

Allow me to show you exactly how you can replicate this AI second brain system that will genuinely boost your productivity. 

#### Be sure to stick around until the end of this article, where I give you my full Claude Code + Obsidian playbook cheatsheet, and every resource I mention below (100% for free).

#### Pre-game

I cannot take all the credit for this system, as it was inspired by Andrej Karpathy's viral tweet about LLM Knowledge Bases a few days ago.

![](https://pbs.twimg.com/profile_images/1296667294148382721/9Pr6XrPB.jpg)

[Andrej Karpathy](https://twitter.com/karpathy)
[@karpathy](https://twitter.com/karpathy)

LLM Knowledge Bases

Something I'm finding very useful recently: using LLMs to build personal knowledge bases for various topics of research interest. In this way, a large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge (stored as markdown and images). The latest LLMs are quite good at it. So:

Data ingest:

I index source documents (articles, papers, repos, datasets, images, etc.) into a raw/ directory, then I use an LLM to incrementally "compile" a wiki, which is just a collection of .md files in a directory structure. The wiki includes summaries of all the data in raw/, backlinks, and then it categorizes data into concepts, writes articles for them, and links them all. To convert web articles into .md files I like to use the Obsidian Web Clipper extension, and then I also use a hotkey to download all the related images to local so that my LLM can easily reference them.

IDE:

I use Obsidian as the IDE "frontend" where I can view the raw data, the the compiled wiki, and the derived visualizations. Important to note that the LLM writes and maintains all of the data of the wiki, I rarely touch it directly. I've played with a few Obsidian plugins to render and view data in other ways (e.g. Marp for slides).

Q&A:

Where things get interesting is that once your wiki is big enough (e.g. mine on some recent research is ~100 articles and ~400K words), you can ask your LLM agent all kinds of complex questions against the wiki, and it will go off, research the answers, etc. I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files and brief summaries of all the documents and it reads all the important related data fairly easily at this ~small scale.

Output:

Instead of getting answers in text/terminal, I like to have it render markdown files for me, or slide shows (Marp format), or matplotlib images, all of which I then view again in Obsidian. You can imagine many other visual output formats depending on the query. Often, I end up "filing" the outputs back into the wiki to enhance it for further queries. So my own explorations and queries always "add up" in the knowledge base.

Linting:

I've run some LLM "health checks" over the wiki to e.g. find inconsistent data, impute missing data (with web searchers), find interesting connections for new article candidates, etc., to incrementally clean up the wiki and enhance its overall data integrity. The LLMs are quite good at suggesting further questions to ask and look into.

Extra tools:

I find myself developing additional tools to process the data, e.g. I vibe coded a small and naive search engine over the wiki, which I both use directly (in a web ui), but more often I want to hand it off to an LLM via CLI as a tool for larger queries. 

Further explorations:

As the repo grows, the natural desire is to also think about synthetic data generation + finetuning to have your LLM "know" the data in its weights instead of just context windows.

TLDR: raw data from a given number of sources is collected, then compiled by an LLM into a .md wiki, then operated on by various CLIs by the LLM to do Q&A and to incrementally enhance the wiki, and all of it viewable in Obsidian. You rarely ever write or edit the wiki manually, it's the domain of the LLM. I think there is room here for an incredible new product instead of a hacky collection of scripts. 

[Posted Apr 2, 2026 at 8:42PM](https://twitter.com/karpathy/status/2039805659525644595)

This tweet went mega viral because it lays the foundation for solving a HUGE issue with the current state of AI. 

And that is the need to constantly re-prompt, add context, and essentially start from scratch anytime you start a new chat or migrate to a new AI tool. 

#### By pairing his system prompt above with Obsidian & Claude Code, you're able to eliminate that problem completely and get significantly better AI outputs.

#### How this system works

This system has 4 moving parts: 

1. **Your data** - articles, notes, transcripts, ideas, etc.
2. **Organization** - done by Claude Code in Obsidian
3. **Instant Prompting -** ask your new database anything at any time
4. **Evolving Memory -** the ability to get smarter over time ![Image](https://pbs.twimg.com/media/HFQNi5rbcAAlqqM.jpg)

**The power of this system** 

As humans, we only have so much mental bandwidth. 

We forget things, sometimes it's hard to connect ideas, and ultimately, we can only keep track of so much. 

By using this 4-piece system, you're essentially freeing up mental bandwidth and allowing Obsidian/Claude Code to connect, visualize, and interpret your data. 

#### Your ideas are now linked together, your notes make connections to other notes, and you can extract them all via Claude - the sky is truly the limit here.

#### Setting up your AI brain (in 5 minutes)

1. **Download Obsidian -** *<https://obsidian.md/>*

![Image](https://pbs.twimg.com/media/HFQQNCqaUAAm-lL.jpg)
2. **Set up your Vault -** once downloaded, you'll be asked to set up a "Vault." Think of this as a simple desktop folder where we can give Claude Code access.

You can name this whatever you'd like - mine is "Obsidian Vault." 

![Image](https://pbs.twimg.com/media/HFQQlZ2bAAAf4D7.jpg) 

This Vault is where Obsidian will store all your data, notes, etc., in MD (markdown) files. 

3. **Claude Code set up -** next, you'll need a way of accessing Claude Code.

For me personally (and probably most of you), I've found the easiest way is to simply use the desktop app. 

In the main chatbox, click "Select Folder" and find your Obsidian Vault.

![Image](https://pbs.twimg.com/media/HFQSNnPaEAAgYW8.jpg) 

4. **System Prompt** - once your folder is selected, go ahead and paste Andrej Karpathy's system prompt into the main chatbox.

You can copy the prompt here: *<https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>* 

```
The core idea  
Most people's experience with LLMs and documents looks like RAG: you upload a collection of files, the LLM retrieves relevant chunks at query time, and generates an answer. This works, but the LLM is rediscovering knowledge from scratch on every question. There's no accumulation. Ask a subtle question that requires synthesizing five documents, and the LLM has to find and piece together the relevant fragments every time. Nothing is built up. NotebookLM, ChatGPT file uploads, and most RAG systems work this way.The idea here is different. Instead of just retrieving from raw documents at query time, the LLM incrementally builds and maintains a persistent wiki — a structured, interlinked collection of markdown files that sits between you and the raw sources. When you add a new source, the LLM doesn't just index it for later retrieval. It reads it, extracts the key information, and integrates it into the existing wiki — updating entity pages, revising topic summaries, noting where new data contradicts old claims, strengthening or challenging the evolving synthesis. The knowledge is compiled once and then kept current, not re-derived on every query.

This is the key difference: the wiki is a persistent, compounding artifact. 

There are three layers:

Raw sources — your curated collection of source documents. Articles, papers, images, data files. These are immutable — the LLM reads from them but never modifies them. This is your source of truth.

The wiki — a directory of LLM-generated markdown files. Summaries, entity pages, concept pages, comparisons, an overview, a synthesis. The LLM owns this layer entirely. It creates pages, updates them when new sources arrive, maintains cross-references, and keeps everything consistent. You read it; the LLM writes it.

The schema — a document (e.g. [CLAUDE.md](http://CLAUDE.md) for Claude Code or [AGENTS.md](http://AGENTS.md) for Codex) that tells the LLM how the wiki is structured, what the conventions are, and what workflows to follow when ingesting sources, answering questions, or maintaining the wiki. This is the key configuration file — it's what makes the LLM a disciplined wiki maintainer rather than a generic chatbot. You and the LLM co-evolve this over time as you figure out what works for your domain.

Operations  
Ingest. You drop a new source into the raw collection and tell the LLM to process it. An example flow: the LLM reads the source, discusses key takeaways with you, writes a summary page in the wiki, updates the index, updates relevant entity and concept pages across the wiki, and appends an entry to the log. A single source might touch 10-15 wiki pages. Personally I prefer to ingest sources one at a time and stay involved — I read the summaries, check the updates, and guide the LLM on what to emphasize. But you could also batch-ingest many sources at once with less supervision. It's up to you to develop the workflow that fits your style and document it in the schema for future sessions.

Query. You ask questions against the wiki. The LLM searches for relevant pages, reads them, and synthesizes an answer with citations. Answers can take different forms depending on the question — a markdown page, a comparison table, a slide deck (Marp), a chart (matplotlib), a canvas. The important insight: good answers can be filed back into the wiki as new pages. A comparison you asked for, an analysis, a connection you discovered — these are valuable and shouldn't disappear into chat history. This way your explorations compound in the knowledge base just like ingested sources do.

Lint. Periodically, ask the LLM to health-check the wiki. Look for: contradictions between pages, stale claims that newer sources have superseded, orphan pages with no inbound links, important concepts mentioned but lacking their own page, missing cross-references, data gaps that could be filled with a web search. The LLM is good at suggesting new questions to investigate and new sources to look for. This keeps the wiki healthy as it grows.

Indexing and logging  
Two special files help the LLM (and you) navigate the wiki as it grows. They serve different purposes:

[index.md](http://index.md) is content-oriented. It's a catalog of everything in the wiki — each page listed with a link, a one-line summary, and optionally metadata like date or source count. Organized by category (entities, concepts, sources, etc.). The LLM updates it on every ingest. When answering a query, the LLM reads the index first to find relevant pages, then drills into them. This works surprisingly well at moderate scale (~100 sources, ~hundreds of pages) and avoids the need for embedding-based RAG infrastructure.

[log.md](http://log.md) is chronological. It's an append-only record of what happened and when — ingests, queries, lint passes. A useful tip: if each entry starts with a consistent prefix (e.g. ## [2026-04-02] ingest | Article Title), the log becomes parseable with simple unix tools — grep "^## \[" [log.md](http://log.md) | tail -5 gives you the last 5 entries. The log gives you a timeline of the wiki's evolution and helps the LLM understand what's been done recently.

Optional: CLI tools  
At some point you may want to build small tools that help the LLM operate on the wiki more efficiently. A search engine over the wiki pages is the most obvious one — at small scale the index file is enough, but as the wiki grows you want proper search. qmd is a good option: it's a local search engine for markdown files with hybrid BM25/vector search and LLM re-ranking, all on-device. It has both a CLI (so the LLM can shell out to it) and an MCP server (so the LLM can use it as a native tool). You could also build something simpler yourself — the LLM can help you vibe-code a naive search script as the need arises.

Tips and tricks  
Obsidian Web Clipper is a browser extension that converts web articles to markdown. Very useful for quickly getting sources into your raw collection.  
Download images locally. In Obsidian Settings → Files and links, set "Attachment folder path" to a fixed directory (e.g. raw/assets/). Then in Settings → Hotkeys, search for "Download" to find "Download attachments for current file" and bind it to a hotkey (e.g. Ctrl+Shift+D). After clipping an article, hit the hotkey and all images get downloaded to local disk. This is optional but useful — it lets the LLM view and reference images directly instead of relying on URLs that may break. Note that LLMs can't natively read markdown with inline images in one pass — the workaround is to have the LLM read the text first, then view some or all of the referenced images separately to gain additional context. It's a bit clunky but works well enough.  
Obsidian's graph view is the best way to see the shape of your wiki — what's connected to what, which pages are hubs, which are orphans.  
Marp is a markdown-based slide deck format. Obsidian has a plugin for it. Useful for generating presentations directly from wiki content.  
Dataview is an Obsidian plugin that runs queries over page frontmatter. If your LLM adds YAML frontmatter to wiki pages (tags, dates, source counts), Dataview can generate dynamic tables and lists.  

```
Your input should look like this:

![Image](https://pbs.twimg.com/media/HFQT0jibYAARYIG.jpg) 

**Tip:** You literally never need to touch Obsidian if you don't want to. You can just give Claude Code access to the MD folder and the input data, and that data will then appear in your Obsidian second brain (since Claude Code can modify the folder). 

5. **Building your database**

After inputting the initial system prompt above, Claude Code will then ask you for some data points to start populating your second brain.

![Image](https://pbs.twimg.com/media/HFQU_LvaMAA4zDA.jpg) 

It's important to think of Obsidian as a blank notebook, where you have to initially input data to start building your database. 

Think: notes, CSV files, MD/text, etc. 

Some tips: 

* Export some data from your pre-existing notes app.
* If you use Notion, export CSV files.
* Ask your Claude chat (or other LLMs) to give you information about yourself so you can inject it into your second brain.
* If you have articles, bookmarks, ideas, etc., go ahead and input them now - this is the time to get at least some initial data in your second brain, and you can always add to it later.

Building a database like mine (with lots of data) takes time to input various data sets. 

![Image](https://pbs.twimg.com/media/HFQWUG5aMAATRWH.jpg) 

That's it; your AI second brain is now fully set up and ready to run. 

#### Now, let me give you some pro tips for optimizing it.

#### Pro Tips

1. **Obsidian Chrome Extension**

To easily input data, all you need is the Obsidian Chrome Extension, which allows you to click "add to Obsidian" on any data source. 

This makes it super easy to build your second brain. 

I use this feature often to add articles, online data, research, and more.

![Image](https://pbs.twimg.com/media/HFQYVNnbgAAEHkn.jpg) 

However, this adds the dataset as a lone source. 

What you then want to do is tell Claude Code, "Hey, I just input [x] into Obsidian; please ingest the data into my Wiki." 

Claude Code will then make connections and links to other data sources within your second brain/Wiki. 

This is why this tool stack combo is so powerful. 

2. **Separate folders**

Karpathy recommends keeping two separate folders/Vaults. 

One for business/work. 

And one for personal/goals. 

I've also found this to be the ideal setup. 

3. **Practicality**

One of the best use cases I've found for this system is simply making my LLM prompts more accurate. 

With access to my entire life, business plans, writing context, etc., it's very powerful in creating curated (and up-to-date) mega prompts. 

Obviously, there are a ton of use cases for this system, but one of the most practical use cases has been creating accurate prompts - I recommend you use it for that. 

4. **Orphans**

"Orphans" in Obsidian let you see which data points lack connections. 

This can be useful for identifying which ideas you may want to build on and potential "weak points" in your database that don't overlap much.

![Image](https://pbs.twimg.com/media/HFQayrabYAA0oHH.jpg) 

#### You can find the toggle switch for Orphans by tapping the 3 dots in the top right.

#### Potential Cons to this system

Alright, we've gone through all the pros, some cool use cases, and how to optimize this AI system. 

But what about the potential cons? When should someone NOT use this? 

1. **You're not a visual person**

One of the main benefits of this setup is that you get to visualize your data. 

If you're not someone who benefits from visualization tools, this may not be for you. 

2. **Maintenance**

Secondly, if you don't want to maintain a database, this probably isn't for you. 

The maintenance isn't much, but without actually inputting data into your second, it's useless. 

3. **Storage**

These MD files will take up storage on your device. 

#### Just something to keep in mind.

#### Final Thoughts

If you made it this far, thank you for reading, and I hope you found this article valuable. 

As a thank you for reading my content, you can grab my *free* cheatsheet for this entire guide here: 

*<https://www.aiedgehq.co/>* 

*All I ask is that you sign up for my free newsletter and join my Instagram community - the entire Obsidian x Claude Code cheatsheet is there.* 

For more AI content like this, be sure to follow me @aiedge\_ - I upload AI articles 2-3x/week on the hottest topics in the space. 

Lastly, if you can, please Like/Repost this article so others can find it 💙
