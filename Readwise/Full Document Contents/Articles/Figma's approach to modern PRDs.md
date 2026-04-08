# Figma's approach to modern PRDs

![rw-book-cover](https://codaio.imgix.net/docs/1OS5N8pQpx/blobs/bl-sMUdgeJu3p/f558ecb641202ed228c1894d09ed9bef0a4ff0e728ae68bc3305d0b86b9c19f0fceef6176bb4f8ab178d01fc52507f7f27116681e55999cd1c658cdf33c80794cf61ce88c3b5ede49a97e79cc9dfd2d381a9624891fc04ae674ac06d39640be2d658aa05?auto=compress&fit=crop&ar=1.91%3A1&fm=jpg)

## Metadata
- Author: [[Yuhki Yamashita]]
- Full Title: Figma's approach to modern PRDs
- Category: #articles
- Summary: Writing effective PRDs is challenging due to the need to balance detail and clarity for different stakeholders. The author shares a template for PRDs that focuses on clearly defining the problem, setting goals, and ensuring launch readiness. Using this template in Coda can streamline the process and keep project information up-to-date automatically.
- URL: https://coda.io/@yuhki/figmas-approach-to-product-requirement-docs

## Full Document
![](https://codaio.imgix.net/docs/1OS5N8pQpx/blobs/bl-sMUdgeJu3p/f558ecb641202ed228c1894d09ed9bef0a4ff0e728ae68bc3305d0b86b9c19f0fceef6176bb4f8ab178d01fc52507f7f27116681e55999cd1c658cdf33c80794cf61ce88c3b5ede49a97e79cc9dfd2d381a9624891fc04ae674ac06d39640be2d658aa05?auto=format%2Ccompress&fit=max&w=1080&dpr=2)
[![](https://codaio.imgix.net/docs/1OS5N8pQpx/blobs/bl-i8pWKoh27_/53fe3d8f4b6a22098837dfcedec9226600071c7e41ebb04f360995d95053e111382a7dd6bbeaca0d6b4589897e55dea0c7d259fa595ffc2420fd0edf249122ec847d2a52593c15aa7fbe22ef34444c7488c813a6306bbb8743410a0eac1b6fedb3e1337b?auto=format%2Ccompress&fit=max&w=281.6&h=281.6&dpr=2)](https://coda.io/@yuhki/figmas-approach-to-product-requirement-docs/prd-name-of-project-1)
Writing a great Product Requirements Doc (

aka

“PRD”) can be hard. Even if you don’t use PRDs or consider the term outdated, you probably have

some

sort of product spec. For these types of docs, it’s hard to choose the right “altitude” to describe what your team is intending to build, as different cross-functional stakeholders care about different things and are equipped with varying levels of context. If you try to be exhaustive, you can easily write a 20-page spec that no one has the time to read (I’ve definitely written a couple of these in the past!). If you’re too vague, you’re not able to elicit meaningful feedback from the reader.

Over my time at Microsoft, YouTube, Uber, and now Figma, I’ve come to slowly gravitate towards a template for PRDs that captures just the right amount of information and displays it in a way that is useful to as many different stakeholders as possible.

I strongly believe that PMs are uniquely accountable for making sure the “why” of an initiative is well-defined and well-understood. So often I’ve seen a team spend a ton of time designing a solution only to have the very premise of the problem it’s solving challenged at the very end. For this reason, I think just as much time should be spent defining the problem as determining the solution, as this saves everyone time in the long run.

I’m not going to dive into what’s the right way to write a problem statement as there are enough blog posts about that on the Internet. Rather, I want to share some additional color I like to include when defining the problem:

Optimize for eliciting a meaningful reaction.

Sometimes a reader won’t give great feedback on your problem because it “sounds good in the abstract,” but it’s unclear what core assumptions underlie this problem, or how severe you think the problem really is (since, at some level, everything can be described as a problem). This is why the “High-level Approach” section is important—it can quickly give a sense of scope and lets the reader imagine what a prospective solution might look like, which for many is easier to react to.

State all your goals, even those immeasurable.

Sometimes, the insistence on having only perfectly measurable goals and KPIs prevents you from clearly explaining what you’re trying to achieve. Simply describing what you want users to think, feel, and do can be an important first step in defining what success looks like.

In this last section, we create a checklist of considerations you want all teams to make before actually launching a feature. Your project may have unintended legal consequences or important marketing implications, and this list is intended to flag the right stakeholders at the right time—and define criteria for launch readiness—so everyone can plan accordingly, well ahead of time.

![Frame 3 (5).png](https://codaio.imgix.net/docs/1OS5N8pQpx/blobs/bl---enR2DpjB/0fd9eaab0ccfc11ac09c52cc317cf855f691de4c768e13e82c4740baabe55e82471970c60f6fd99ffecdd66db0cbd1d1e0c46bb4acc0b5ce2a53d32b7727a5dc72e4957e15e7145daaf1baed78750079661f8d528824094424bcb58a25be8552411f8302?auto=format%2Ccompress&fit=max&dpr=2)
Because this template is written in Coda, I was able to remove any redundant data entry, and to make sure everything about the project is automatically kept up-to-date. At the very top, there’s a section that gives readers extra context about the project (e.g., its current status). Go ahead and try it for yourself—just change the Project listed below and see all of the underlying info update:

This is pulled in automatically from the Figma Project Tracker. As you add more collaborators, or as the status of the project changes, this will automatically be updated so you’re no longer having to keep multiple places up-to-date!
