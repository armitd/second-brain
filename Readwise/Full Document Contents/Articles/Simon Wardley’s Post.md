# Simon Wardley’s Post

![rw-book-cover](https://media.licdn.com/dms/image/v2/D4E22AQGyEi68F2gfaQ/feedshare-shrink_2048_1536/B4EZsYdVPdGYAw-/0/1765641902323?e=2147483647&v=beta&t=tjiK4K4MRiSYpPxHNtK88dmoko03SplbaC_apdMLn2s)

## Metadata
- Author: [[Simon Wardley, Will Wilson]]
- Full Title: Simon Wardley’s Post
- Category: #articles
- Summary: Top teams are cutting back on AI-generated code because it creates accountability gaps, deskills engineers, and erases tacit knowledge. Letting AI decide code structure risks making systems inscrutable and hard to maintain or adapt. That loss of understanding could cause large organizational failures over time.
- URL: https://www.linkedin.com/posts/simonwardley_an-interesting-trend-im-seeing-is-that-some-activity-7405743850549379072-6HV_?utm_medium=ios_app&rcm=ACoAAABPpUoBj4B7xm5echiwOkJMCY_W821MbqI&utm_source=social_share_send&utm_campaign=share_via

## Full Document
[Simon Wardley](https://uk.linkedin.com/in/simonwardley?trk=public_post_feed-actor-name) 

"some of the most elite teams are abandoning AI coding altogether" ... I suspect this is overstated. It's more likely that they are restricting LLM/GPT use to narrow, supervised tasks that can be easily reviewed. Understanding what you have built turns out to be important.

Specification driven development is an interesting approach when used as an aid to learning. However, many think the ideal approach is to write a specification and then let the system or swarm of agents build the functionality you require and test against it. The bit they miss is that functionality is just one part of what we code, the rest is structure i.e. all those micro decisions that impact maintenance, adaptability, off specification behaviour, trade-offs, constraints and ultimately resilience.

If you allow the system to make those decisions for you, then either you simply accept it has made good choices for you (a path that is neither craft nor engineering but belief based development) or you have to read all the code to try and understand it.

This is little different from dealing with legacy environments where the original coders have gone. In other words, we are simply accelerating the scale of the legacy problem. Alas, many think the solution to that is to point another LLM/GPT at it.

It can only be a matter of time before some well known company collapses into bankruptcy because it has lost control of its own systems due to a strategy of handing such decision making (i.e. coding) to various AIs. The problem is not that LLM/GPTs write bad code, the failure mode will be organisations that can no longer reason about their own systems quickly enough to adapt and compete.

Always remember the tale of Knight Capital (2012) when an update to its trading system reactivated old, partially disabled code that the organisation no longer understood. Within an hour, the company lost over $400 million. The code worked as written, behaved according to internal logic but the organisation had lost control of its system and could not reason about its behaviour.

If you think this is a problem for a few organisations, I'd suggest deeply reading “Scale and information-processing thresholds in Holocene social evolution", Shin, J et al.  

[https://lnkd.in/eBDHqx-B](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Flnkd%2Ein%2FeBDHqx-B&urlhash=BSPa&trk=public_post-text)

The paper doesn't say that too much information causes a collapse of society but instead it happens when complexity increases demand for information processing faster than societies naturally upgrade their ability to do so. Of course, if you've lost control of structure then ... well, you've lost that ability, you're relying on statistical continuity without structural guarantees. Given enough time collapse is inevitable.

Maybe that's the great filter for the Fermi Paradox. AI causes collapse not by making mistakes, it fails by removing the conditions under which mistakes can be understood, corrected, and learned from.

 [Will Wilson](https://www.linkedin.com/in/will-wilson-330276112?trk=public_post_reshare_feed-actor-name) 

An interesting trend I'm seeing is that some of the most elite teams are abandoning AI coding altogether.

The reasons are varied, but they generally boil down to three issues: accountability, deskilling, and loss of tacit knowledge. I'm curious how others are getting around these problems.

(1) Accountability. This one is kind of obvious. Code authored by AI is "owned" by nobody. Nobody stands behind it. Nobody's neck is on the line if it breaks. That's a recipe for terrible incentives. Some have tried to fix this by making the code "owned" by whoever reviews it, but the review burden for massive amounts of AI-generated code is just too high and creates an even worse bottleneck.

(2) Deskilling. Just like any other language, the moment you stop practicing coding is the moment you start forgetting how to do it. I think everybody in the industry has horror stories about interviewing new CS grads who can't actually code at all. But this affects very senior engineers as well -- skills atrophy when you stop using them. This creates an interesting catch-22 because so many studies have shown that AI coding is most effective for very skilled engineers, but it simultaneously degrades that skill. I don't know where the equilibrium will shake out here.

(3) Tacit knowledge. This is the most subtle one, and in some ways the most interesting. Let's use writing as an analogy: when you write an essay yourself, you really "inhabit" it. You know exactly how the argument proceeds, where the important moments of tension are, where it doesn't quite hang together. If you need to edit it, it's \*yours\*. The writing is already part of your brain's context window, already available in a powerful and compact mental representation, so you can change it quickly and with awareness of how your local changes affect the rest of the argument. Editing an AI-authored essay basically requires rewriting it from scratch.

Coding is exactly the same. When you write something yourself, it's \*yours\* almost like a part of your body, and that makes it easy to change it later or review somebody else's changes. You recognize the crazy knock-on effects those changes can have because you see not just the change, but the whole thing. Reading somebody else's code is \*much\* harder, but at least you can go ask them about it. When a team uses a lot of AI, whole areas of code become nobody's, and this isn't just an accountability issue, it's a productivity issue, because really understanding changes to that code require basically learning it all over again from scratch.

These are the issues I'm seeing. I have no dog in this fight, because Antithesis has plenty of customers who use AI and plenty who don't. Curious if anybody else sees bleeding-edge teams ditching AI, or has developed practices that ameliorate these issues.

* ![No alternative text description for this image](https://media.licdn.com/dms/image/v2/D4E22AQGyEi68F2gfaQ/feedshare-shrink_2048_1536/B4EZsYdVPdGYAw-/0/1765641902323?e=2147483647&v=beta&t=tjiK4K4MRiSYpPxHNtK88dmoko03SplbaC_apdMLn2s)
