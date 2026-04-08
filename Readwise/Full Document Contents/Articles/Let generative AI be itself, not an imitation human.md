# Let generative AI be itself, not an imitation human

![rw-book-cover](https://substackcdn.com/image/fetch/w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd97dac11-ccaa-4180-a85c-22bcd1c1d32e_1024x1024.webp)

## Metadata
- Author: [[PEG]]
- Full Title: Let generative AI be itself, not an imitation human
- Category: #articles
- Summary: The author argues that we should embrace generative AI for its unique strengths instead of trying to make it mimic human intelligence. Generative AI excels in language manipulation and can enhance human creativity and productivity. However, its limitations mean that it cannot fully replicate the complex understanding that comes from human experience.
- URL: https://thepuzzleanditspieces.substack.com/p/let-generative-ai-be-itself-not-an?r=2wvwm&utm_campaign=post&utm_medium=web&triedRedirect=true

## Full Document
[![The Puzzle and Its Pieces](https://substackcdn.com/image/fetch/w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2357d2a-d8ac-4412-a85a-e18bad2d0530_480x480.jpeg)](https://thepuzzleanditspieces.substack.com/)

### [The Puzzle and Its Pieces](https://thepuzzleanditspieces.substack.com/)

##### LLMs might usher in the next industrial revolution, but if we keep trying to make them into synthetic humans powered by artificial general intelligence, we may miss what they do best

*I’ve been sitting on this essay for a few months, wondering what to do with it. Given that a bunch of the ideas from it are feeding into the development of the book outline, I’ve decided to drop it on this newsletter.*

Will generative AI—primarily, large language models—finally usher in a four-day work week? [[1](#footnote-1-157949199)] Some pundits opine that the technology will accelerate productivity, juicing economic growth by an order of magnitude much like the Industrial Revolution did. [[2](#footnote-2-157949199)] Or we might be witnessing the birth of the world’s first superintelligence, [[3](#footnote-3-157949199)] necessitating an investment in AI ethics and regulation [[4](#footnote-4-157949199)] to ensure that these superintelligences are a force for good and not the “paperclip maximisers” of evil [[5](#footnote-5-157949199)] that many fear. (In 2003, philosopher Nick Bostrom suggested that even a superintelligence responsible for something as banal as creating paper clips might convince itself that it needs to destroy the world to achieve its goals.)

All this enthusiasm has resulted in an explosion of creativity. Developers are building a dizzying array of applications powered by large language models (LLMs), [[6](#footnote-6-157949199)] while also enhancing the core LLM technology via techniques such as such as vector databases, [[7](#footnote-7-157949199)] which store data as mathematical representations, and knowledge graphs, [[8](#footnote-8-157949199)] which map connections between disparate data points or sources. These advances endow LLM applications with memory and expertise, making them even more capable. But should we be in a rush to develop autonomous agents, [[9](#footnote-9-157949199)] mechanically intelligent servants to prosecute tasks on our behalf? Is our tendency to anthropomorphise our new tool (to imbue it with human qualities) leading us astray, with gen AI’s true benefits lying somewhere else?

#### The surprising competence of generative AI

Not a week seems to pass without some surprising generative AI development. From the ability to create realistic, full-motion video [[10](#footnote-10-157949199)] or game play [[11](#footnote-11-157949199)] from a text prompt (though with some issues around things like object permanence), to the more recent development of multi-step and multi-modal reasoning which lead to the creation of solutions such as scientific research assistants [[12](#footnote-12-157949199)] and AI co-scientists. [[13](#footnote-13-157949199)] Surprises like this are typically accompanied by a prediction about how industries, organisations, and individuals are about to be disrupted. [[14](#footnote-14-157949199)]

Our first instincts on how to put a new technology to work rarely (if ever) represent the best use of the technology, nor do they represent how it will be finally used. [[15](#footnote-15-157949199)] We both underestimate and overestimate potential benefits—generative AI could be our salvation or our doom. Or it might be no more than a “stochastic parrot,” [[16](#footnote-16-157949199)] the sophisticated cousin of the autocomplete technology that helps us compose text messages. For every prediction of an AI-powered digital utopia, there is an equally extreme prediction that AI will drive us toward a cybernetic hell. Other pundits assume that LLMs will provide a modest (but appreciated) productivity bump before we move on to the next shiny new thing. Indeed, there is early evidence that the anticipated productivity benefits of LLMs are not having as large an impact as predicted or hoped, [[17](#footnote-17-157949199)] as individual productivity gains are not translating into firm-wide improvements. Nor are the much-touted emergent abilities of LLMs what they first first seemed. [[18](#footnote-18-157949199)]

All of this is true for artificial intelligence and generative AI. Intelligence is a nebulous concept at best and we, as a species, tend to anthropomorphise, reading intelligence and consciousness into all manner of things. The same tendency to see faces in passing clouds could be leading us to see human-like intelligence in LLMs.

The many surprises generative AI has provided over the past year or so—from unexpectedly playing chess at a reasonable level [[19](#footnote-19-157949199)] to appearing to reason, do basic math, or decode the meaning of a movie from an emoji description—have made it easy to assume that LLMs have the potential to be much more capable than we might imagine. This stream of surprising news has unsurprisingly resulted in predictions that artificial general intelligence (AGI)—AI that can think and perform independently across a wide range of domains, like a human—is just around the corner, possibly as early as 2030. [[20](#footnote-20-157949199)]

We see an LLM do something surprising, something intelligent, and naturally assume that the technology will be capable of other deeds we consider equally intelligent. This is not the case though. An LLM playing chess will make an illegal or naive move, such as teleporting a threatened piece to safety. Those decomposing tasks are easily confused and become trapped in loops, stuck due some ambiguity in how a goal might be achieved. Others seem to go “mad” for no reason. [[21](#footnote-21-157949199)] Efforts to remove bias produce unexpected and undesirable results. [[22](#footnote-22-157949199)] (Some commentators are suggesting that as AI systems become more sophisticated, they may develop novel forms of bias that have no human equivalent.) [[23](#footnote-23-157949199)] And so on.

It’s easy to be surprised when LLMs fail in this way, likely as we were also surprised by just how capable they were in the first instance and so overestimated their abilities. Throwing more technology at LLMs—more weights and so more computing power, more sophisticated prompts, larger and better-tuned training sets, integrating external knowledge sources, and (most recently) the rush to using multiple LLMs in ‘agentic’ solutions—reduces the problems somewhat but does not eliminate them. LLMs are powerful, but there are limits to this power that we need to understand if we’re to make the best use of the technology.

#### Humans ‘think’ with more than their brains

There has been an explosion of creativity in the short time since ChatGPT was released into the world, and LLM-powered solutions have rapidly improved. This rapid improvement has suggested to many people that artificial general intelligence is within reach. Peter Norvig, who “wrote the book” on AI, [[24](#footnote-24-157949199)] proposes that the current generation of “frontier models” [[25](#footnote-25-157949199)] have already achieved a significant level of general intelligence. [[26](#footnote-26-157949199)] In other words, they’re competent in a wide range of tasks across diverse media and demonstrate surprising, “emergent,” abilities. Work to bolster their performance via techniques like integrating knowledge graphs will make them even more intelligent. Does this mean that AGI is within our reach, and it’s just a question of tweaking LLMs to get there?

It’s hard to pin down just what intelligence is. Common definitions can be hand-wavy or self-referential, along the lines of the American Heritage Dictionary’s “[t]he ability to acquire, understand, and use knowledge,” [[27](#footnote-27-157949199)] what Annika Weder described as “the ability to learn or understand or to deal with new or trying situations,” [[28](#footnote-28-157949199)] or what the Oxford Dictionary defines as “the ability to acquire and apply knowledge and skills.” [[29](#footnote-29-157949199)] Cognitive science researchers use a reductionist approach to make intelligence researchable by associating it with (reducing it to) a set of defined human abilities. [[30](#footnote-30-157949199)] The problem with this approach is the usual one: The thing researchers are studying is not necessarily the same as the thing that we commonly think of as intelligence. Intelligence becomes what the tests measure—a set of abilities that we can discriminate between, isolate, observe, and quantify. It’s a phenomenological definition (how we perceive intelligence), not a structural one (how intelligence works), nor ecological (how our intelligence is affected by the world around us). Our natural inclination is to consider intelligence as including all of these.

AI research has a similarly reductionist approach to understanding intelligence. Humans are intelligent because of *something* about a set of skills and abilities, so if we can identify these skills and abilities and find technological or algorithmic solutions to each (such as we did with route-finding algorithms used by mapping applications to replace human pathfinding) [[31](#footnote-31-157949199)] then combining the solutions will result in “artificial general intelligence.” This was the basis of the 1956 Dartmouth Summer Research Project on Artificial Intelligence that gave birth to AI as a discipline. [[32](#footnote-32-157949199)] It’s also the basis for the various testing regimes uses to gauge the performance of new LLMs. [[33](#footnote-33-157949199)]

It’s not clear, however, that we *can* create general intelligence by decomposing it into a set of *things*, address each separately, and then combine our solutions. Many of the phenomena we’re interested in might be *processes in contexts* rather than *things per se*. Consider our (fallible and human) memory. Is memory a *thing*, a place in our head where perception is encoded for later recall? The long history of research into memory shows that our memories are much more malleable and more ephemeral than we realise, [[34](#footnote-34-157949199)] and the many foibles of human memory (such as our capacity to create false memories) [[35](#footnote-35-157949199)] are surprisingly common. Or is memory a *process*, where context (past experience and current circumstance) interacts with stimuli (some prompt) to generate an imperfect (re)construction of past perception?

Researchers in psychology have recently taken an ecological approach to understanding human performance. [[36](#footnote-36-157949199)] That is, they posit that human development and performance are strongly influenced by the environment one finds oneself in. Rather than looking for and studying *things* inside the individual, ecological researchers look for and study *processes* that connect the individual to the world around them. The starting point was to ask a simple question: “Where does the mind stop and the rest of the world begin?” [[37](#footnote-37-157949199)] Putting this another way: Do we think only inside our heads? The answer is no, we don’t. Instead, we think by interacting with the world around us.

Consider long division: Do the calculations only occur in our mind? That can’t be true as we rely on pen and paper, and if we take them away then we’re unable to do long division. At least some of the thinking occurs *on the paper*. The canonical example used to illustrate the difference is “the outfielder problem.” [[38](#footnote-38-157949199)] We don’t catch a ball (when fielding in baseball) by sensing its trajectory and then rushing to where we calculate (predict) it will land. Rather, we adjust our own motion so that the ball appears to be still in our field of vision while dodging obstacles in our path as they appear. Similarly, our mind treats a computer mouse as an extension of, part of, our body when we are manipulating it. We think by interacting with the world around us. Our mind works as part of the environment to catch the ball, to click the button on the screen, or divide, rather than remain separate from the world as it computes. Cognition, intelligence, is likely a relational property, between an organism and its environment—not something that resides within the organism. [[39](#footnote-39-157949199)]

It’s common to assume that we think only inside our heads and so *thinking* must be computation. This is particularly common in the AI community. A stronger version of the reductionist approach to intelligence runs along the following lines:

1. Humans compute (think) inside our heads, therefore intelligence is the product of computation.
2. The Church-Turing thesis [[40](#footnote-40-157949199)] tells us that any two computers are functionally equivalent, therefore we can replicate human-level intelligence with digital computers once suitable algorithms are discovered.
3. Digital computers are more capable than human computers: They don’t have the same limitations in memory capacity, processing speed, or precision.
4. It follows that digital intelligence will be more capable than human intelligence.

This is the genesis of the “singularity,” the assumption that eventually the algorithms underpinning general intelligence will be discovered, enabling us to create artificial general intelligence, which will quickly become more capable than human intelligence as it won’t have the same limits.

We can see that this line of reasoning is built on shaky foundations.

While humans can compute, it doesn’t necessarily follow that humans are computers, that we think inside our heads. The history of creativity research is a case in point. At first it was thought that creativity was the essential attribute of an individual, [[41](#footnote-41-157949199)] the lone genius, recipient of a divine gift, or, later, the consequence of a unique genetic inheritance. This was supplanted by a reductionist view of creativity as a learnable skill that can be developed through teaching and practice, rather than being the innate quality of a lucky few. Most recently, a systems approach, or “social creativity,” holds that creativity is the result of human interaction and collaboration—a generative and ecological phenomenon, the result of interactions between situated actors. In this theory, creativity emerges from the interactions between person, place, work product, and process. [[42](#footnote-42-157949199)] This is part of the general shift to understanding human performance in ecological terms.

Many of the outcomes we’re interested in—such as creativity and intelligence—cannot be inferred from the properties of the individuals themselves. Instead, we need to consider the extended, socio-technical system that the individuals are part of, [[43](#footnote-43-157949199)] just as the research psychologists (mentioned earlier) have done. Moreover, the limitations of human intelligence may be inherent in general intelligence. Any system—either designed or evolved—is the product of a series of trade-offs. It’s possible that the limitations of human intelligence are a natural consequence of general intelligence, of thinking by interacting. If so, these limitations will apply equally to human and machine general intelligence. The fact that computers have greater memory capacity, processing speed, and precision than humans might be inconsequential—being better computers doesn’t imply that they will be more generally intelligent, as the limitation might be in the environment, not in the individual actor.

#### Language is only part of intelligence

It’s important to remember that LLMs are creatures of language. Given a prompt, they will predict a following statement, image, or video. This means that any problem we reframe as a language problem is amenable to LLM language prediction. LLMs can predict what essay might be associated with an outline, or the list of subtasks associated with a task description. An LLM could operate a milling machine by transforming a 3D model (specified in a modelling language) into G-code commands, allowing a model car to be milled from a lump of metal. A user can use gen AI to generate working code for a prototype software application by providing a description of its user interface. Furthermore, someone could employ predictive algorithms to complete the incomplete work of a deceased artist, thereby anticipating the remainder of the piece. [[44](#footnote-44-157949199)] And so on. This makes generative AI a powerful tool—much more sophisticated than a semantic parrot. However, while language is an important part of intelligence, it’s not *all* of intelligence. It’s likely that artificial general intelligence is beyond the reach of a language-centric approach.

Language is a powerful tool, but it’s not particularly precise. There are synonyms and homonyms, both of which create confusion. Humans use low-context languages where what is said is what is meant, and high-context languages where what is unsaid can be as—if not more—important than what is said, relying on shared experience to convey hidden meaning. Most importantly, while language is an important part of what makes us human, it doesn’t capture all that being human entails. There are places that language can’t go, ideas and feelings that we can’t use language to express. French psychoanalyst and psychiatrist Jacques Lacan [[45](#footnote-45-157949199)] calls this place “The Real” [[46](#footnote-46-157949199)] —experience which can’t be captured by symbols and language. The Real is experience that eludes our attempts to represent it, to reify it in words.

This idea of *things beyond language* pops up in all sorts of annoying places. Music theory is a great case in point. It rears its head when Herbie Hancock and Jacob Collier discuss music harmony in a video, [[47](#footnote-47-157949199)] as they soon run out of words to describe experience and resort to exclamations woven between chords stabbed on the keyboards in front of them. Western notation (with its staves, notes, beams, and accents) is the result of centuries of development, and centuries of compromises. Indeed, one could view the history of western notation as an effort to find the least-worse compromises for a particular style of music. Twelve-tone equal temperament tuning (which is the basis of the vast majority of modern Western music) is a case in point, trading just intonation for acceptable fifths and fourths (and poor thirds), and the ability to play in any key with a single tuning (a boon for pianists). This makes much contemporary Western music out of tune, though we’ve become accustomed to it. [[48](#footnote-48-157949199)] Indian music theory, in comparison, is built on a different set of compromises due to its differing needs and goals, arriving at a solution that allows much richer notation for rhythm but with less focus on harmony. [[49](#footnote-49-157949199)] Music notation—all music notation—is a powerful but imprecise language, and there is a line between the concepts and ideas that it can express, and those that are inaccessible to it.

We humans are constantly skating along the edge of language as we find our way through the world. Consider something seemingly as simple as defining a “seat.” Dictionaries (and LLMs) often provide expansive definitions as they try to account for the wide range of things that we might consider a seat. A more concise approach is to simply define “seat” as a “thing that affords sitting.” This thing could be a chair, a flat rock, or a conveniently shaped tree root—the thing becomes a seat when we realise that we might sit on it.

We understand the word “seat” by referring directly to shared experience—our understanding is informed by our ability to experience the thing directly. This is why Herbie Hancock and Jacob Collier were forced to play examples rather than name the chords they were playing. It’s not that there were no names for those chords. They had the opposite problem: There were many possible ways to name each chord but none made sense—none conveyed the intended meaning—and so they were forced to resort to examples. Similarly, indicating a convenient rock or tree root is a more effective way to communicate “seat” than searching for a verbal definition.

Language is incredibly powerful—it can even seem to have magical abilities. A story enables us to enter another’s head and imagine that we know what they’re thinking. Language can be used to embody knowledge in descriptions and instructions that others can learn from. But is language thought? It’s commonly assumed that the voice in our heads is thought in action—*I have an internal monologue, therefore I am*—that language is the root of consciousness. Though you might be surprised to learn that not everyone has an internal monologue. [[50](#footnote-50-157949199)] Are these people without consciousness? The assumption that language is all of consciousness leads to the belief that once an LLM is sufficiently powerful, we will have created AGI.

LLMs are powerful, but they’re also limited. An LLM-powered agent will stumble when it encounters something undescribed or indescribable. An ill-defined term, task, or some language confusion can easily confound its language prediction. Awkward naming in a 3D model of a windscreen can result in random or physically impossible interconnections when we use an LLM to combine it with a model of a car body. A chess-playing LLM doesn’t “know” chess, just the language of chess. Those decomposing plans into a series of tasks are easily confused by ambiguous phrasing or descriptions. And so on.

Language is an important part of intelligence, but we must be careful that we don’t confuse language (and language prediction) with consciousness and the freedom to act inherent in humans (and all animals). LLMs (and all AI) understands to perceive, while humans perceive to understand. LLMs will struggle if we cause them to go beyond what is explicitly stated in their prompt, when they run out of grounded references to predict from. [[51](#footnote-51-157949199)]

Consider memory: Is an LLM’s memory a thing or a process? An LLM doesn’t recall a famous work of art—fetching an image stored during training—it constructs a new memory from the prompt’s interaction with the patterns encoded in its trillions of weights. For example, if a user asked an LLM to provide an image of the Mona Lisa, it would start from a prediction of what the Mona Lisa looks like based on descriptions, criticism, all manner of photos that it’s been exposed to, etc. This memory is a shadow of the images and conversations about the work of art which were used to train the LLM, rather than a copy. This means that LLM memory is fallible and prone to false memories and other types of confabulation, as (false) memories may be created as needed to support the LLM’s response. An LLM asked to provide supporting references will insert references into its response, though the references might well be made from whole cloth. [[52](#footnote-52-157949199)] There is no connection between the references and anything outside the response or prompting text.

It’s easy to be surprised when LLMs fail in this way, likely as we were also surprised by just how capable they were in the first instance and so overestimated their abilities. Throwing more technology at the LLMs—more weights and so more computing power, more sophisticated prompts, larger and better-tuned training sets, integrating external knowledge sources—reduces the problems somewhat but does not eliminate them as they are due to the LLM being limited to language.

Humans can directly refer to experience and so find their way through when confronted by the ambiguous or indescribable. LLMs, on the other hand, must be provided with suitable external references if they are to self-correct their language-driven reasoning. An LLM trained on “A is to B,” will fail when predicting what “B is to A” if the relationship between the two is not explicitly stated in the prompt. [[53](#footnote-53-157949199)] Interpretation of any text is potentially endless, and we humans can similarly come unstuck unless we anchor our own interpretation to something outside the text. [[54](#footnote-54-157949199)]

The fact that LLMs are creatures of language is the source of their power, but it’s also the source of their limitations.

#### The opportunity of language prediction

Language might not be all of intelligence, but it’s clearly part of intelligence, and an important part at that. The challenge is not to let ourselves be carried away by our tendency to anthropomorphise and assume that these tools are something they’re not.

The limitations of today’s AI solutions may be caused by our attempts to create “synthetic humans” to be situated in established human environments. (Or in the case of agentic solutions, teams of synthetic experts.) The act of driving a car, for example, has been automated for some time—the first self-driving car is likely a vision-guided robotic van which drove on an autobahn in Germany in the 80s. [[55](#footnote-55-157949199)] However, modern, self-driving solutions that showed promise in limited trials are struggling when rolled out at scale, [[56](#footnote-56-157949199)] as driving in traffic is both a technical *and* social challenge. Self-driving cars could find their way through an environment dominated by human drivers, likely as the humans allowed for the self-driving cars’ quirks. It’s easy to forget just how good humans are at collectively navigating the chaos of traffic. Self-driving cars don’t have the same flexibility as humans though, and the problems we’re seeing manifest once there is a non-trivial number of self-driving cars in the traffic system. [[57](#footnote-57-157949199)]

When work is automated, it’s transformed. It’s rare for a human worker to be replaced by a robot prosecuting the same tasks in the same manner. Instead, the socio-technical system is reorganised: Rather than de-skilling, expertise is redistributed, and the new instruments and tools become extensions of workers’ bodies, and of their cognition. Developing a successful self-driving solution may require us to engineer the traffic environment to remove the social aspect of driving in traffic (by eliminating all human drivers) though this is likely to have undesirable infrastructure and social consequences. Developing smart human-car hybrids that redistribute driving expertise, as has already been done with technologies such as lane keeping and adaptive cruise control, is a more manageable approach.

Similarly, creating AGI—human-like intelligence in machines—will likely require us to adopt a more ecological approach. Human intelligence is inherently social—as we can see from feral children in the past who were incapable of typical development when they integrated with society. [[58](#footnote-58-157949199)] It’s not enough for our AI to be trained on human language; it needs to be a full participant in the complex and messy process whereby we collectively make sense of the world. Arguments over pattern-based neural networks versus symbolic processing with formal logic versus hybrid approaches, miss the point. We’re attempting to replicate the phenomenological aspects of intelligence with little understanding of how these phenomena arise.

One consequence of this approach is that we ascribe the capabilities of solutions that surprise us to the enabling technology, the algorithms used, rather than structural or environmental factors. LLMs are powerful language prediction solutions, but the intelligence we ascribe to them might be more a consequence of the language they’re processing (the breadth and depth of their training set) more than the power of their predictions. It’s a bit like seeing bacteria follow a trail of nutrients through a maze and assuming that it solved the maze with intelligence. Similarly, we assume that solutions that don’t quite make it, such as autonomous cars, just need better algorithms or more data.

A more productive path forward is to focus on the language rather than the LLMs themselves. The digitisation of society has resulted in the creation of a plethora of technical languages, which are simpler than human languages, and so more tractable. We use these technical languages to program computers and describe objects and processes.

It shouldn’t have been a surprise, for example, that an LLM could play chess. There is a long history of describing and discussing chess games, most recently with algebraic notation. [[59](#footnote-59-157949199)] It’s an easy task for an LLM to predict a next move in a game of chess described in algebraic notation, though the LLM is working with a language for describing chess games and not directly with the rules. Consequently, a dedicated chess AI will outperform an LLM (and consume far fewer computing resources while doing so).

Similarly, we might describe the Towers of Hanoi [[60](#footnote-60-157949199)] disc-stacking puzzle and ask an LLM to translate our description into Planning Domain Definition Language (a language used to describe planning problems). [[61](#footnote-61-157949199)] The PDDL description can be fed to an AI planning engine to find a solution. Or two 3D models can be integrated to create a single object by using an LLM to predict how a combined model might be described. The “Hello, World” of LLMs seems to be a PDF summariser—taking a document described in PostScript (a programming language), extracting the natural language text, and then summarising the result. And so on.

Indeed, there are many technical languages that an LLM can manipulate and translate between. Programming is just the most popular example. This thread—using LLMs for technical, as well as human languages—is something that we haven’t pulled on hard enough yet.

We should also consider how LLMs can be put to work as part of a larger system rather than building our intelligent solutions around LLMs. Chatbots are a case in point.

One might have a natural conversation with an LLM-powered chatbot. In contrast, conventionally programmed chatbots are restricted to awkward and obviously artificial conversations. We might even convince ourselves that the LLM-powered chatbot is conscious. However, we should not ignore how the chatbot is a passive and aimless conversationalist, following the human through the twists and turns of the human’s interests rather than seeking its own goals. It only provides opinions when prompted, for example, not when it desires to. The chatbot is reacting to the human, predicting the most likely response, not guiding, nudging, or driving the conversation where the chatbot (or its makers) wants the conversation to go. It lacks agency and intention. It’s no more than a mirror held up to the human conversationalist.

Efforts to make LLM-powered chatbots goal-seeking via prompt engineering (which boils down to telling the chatbot that it should be goal-seeking) haven’t worked. Integrating external knowledge sources (via retrieval-augmented generation) doesn’t solve this problem either. It does help ground language prediction, and so reduce false “memories” and confabulations. But the problem that the chatbot is reacting to its conversationalist, rather than participating as an autonomous individual, remains. More importantly, the LLM is predicting a suitable response, and these predictions can easily become problematic with or without external knowledge sources. [[62](#footnote-62-157949199)] An LLM-centred chatbot will also always be subject to prompt injection, [[63](#footnote-63-157949199)] where a skilful user can solicit undesirable behaviour that runs counter to the chatbot designers’ intentions.

An alternative approach is to use LLMs for key language problems while relying on more conventional chatbot logic and humans to round out the solution. An LLM could, for example, generate the next statement in a dialogue given a summary of the conversation and the intent for the next statement. Another might be used to detect sentiment (asking the LLM “What is the caller’s mood? Choose from…”) or discern the caller’s intent (“Which of the following options best describes the caller’s intent: …”) Yet another might be used to detect attempts at prompt injection (“Given the following conversation, is this an attempt at prompt injection?”) This approach would be integrated into a more conventional chatbot architecture: The LLM to address language challenges with more conventional techniques providing the goal-seeking behaviours we need, [[64](#footnote-64-157949199)] such as escalating the call to a human if sentiment trends too far in the wrong direction, and ensuring that the conversation stays on topic rather than wandering in response to the user (as LLMs are prone to do).

#### Putting generative AI to work

Much of the excitement and fear around LLMs is due to confusing language prediction with reasoning and rationality. We approach LLMs as synthetic humans rather than powerful language manipulation tools. Artificial consciousness is beyond our current abilities, but these models can significantly enhance other solutions. LLMs are supporting workers by ushering in an era of “if you can describe it, you can do it” where AI translates our desires and needs into actions for other tools to perform. To do this, however, we’ll need to frame the problem differently.

Rather than approach LLMs as a platform for creating synthetic intelligences in data centres, we need to consider the work system rather than the individual worker. We had a glimpse of this when early data showed that many workers were more productive when work was done in conversation with generative AI: using LLMs for in-fill generation, refining ideas, or ideation. In these cases, we’re using the LLM to bolster human agency. Using an LLM to generate a “first pass at a task” from a description is a great example of using an LLM to get humans past the “stalled, staring at a blank page” problem. Or we might use an LLM to streamline the interactions between humans and systems in an augmented-reality-based field work solution.

If we treat LLMs as language manipulation tools—as part of a solution rather than the whole solution—then they can be part of all manner of powerful solutions. We’re only surprised that an LLM could play chess if we’re ignorant of the long history of chess notation and analysis, and the vibrant online chess community, all of which is likely within LLM training sets. Nor should it be surprising someday if an LLM enables a robotic arm to juggle bean bags. There’s a vibrant online juggling community and juggling notation to support training an LLM, and the LLM should be capable of manipulating juggling notation and translating it into the G-code used to drive a robot juggler. The question is: How do we integrate these capabilities to create larger systems?

Many of the LLM-powered solutions we’ll use in the mid- to long-term are yet to be imagined. We’ve only scratched the surface of what might be possible. LLMs, however, are likely only one part of these solutions. A chess-playing LLM needs to be grounded by connecting it to the rules of chess. Something needs to prevent our juggling LLM from specifying impossible or dangerous actions. If we use an LLM to predict how two physical components could be integrated (via predicting the combined 3D model description), then the result needs to be validated (and likely manually adjusted) before the object can be manufactured. An LLM is also likely to be an important component in future chatbots, but it will need to be complimented by other components that enable the chatbot to be goal-directed. And so on.

LLMs are clearly powerful tools that can be applied to all manner of problems we’ve yet to imagine. They might even usher in a “Fifth Industrial Revolution,” though only time will tell if that’s the case. However, the AGI that many hope for will continue to be harder than we think. LLMs are unlikely to be the synthetic intelligence accelerationists [[65](#footnote-65-157949199)] hope for, or doomsayers dread, nor are they stochastic parrots that will have little impact. Language is a powerful thing, and LLMs’ ability to manipulate language creates a wealth of opportunities, many of which we aren’t even aware of yet. However, if we want to put LLMs to work, then we need to find our way past our tendency to anthropomorphise.

If you found this valuable, consider sharing it with someone who might enjoy it too.

[1 [find in text]](#footnote-anchor-1-157949199)

Bennett, Elizabeth. 2024. “AI Could Make the Four-Day Workweek Inevitable.” *BBC*, February 27, sec. Worklife. <https://www.bbc.com/worklife/article/20240223-ai-could-make-the-four-day-workweek-inevitable>.

[2 [find in text]](#footnote-anchor-2-157949199)

Erdil, Ege, and Tamay Besiroglu. 2023. “Explosive Growth from AI Automation: A Review of the Arguments.” arXiv. [doi:10.48550/arXiv.2309.11690](https://doi.org/10.48550/arXiv.2309.11690).

[3 [find in text]](#footnote-anchor-3-157949199)

Noor, Al-Sibai. 2024. “Amazon AGI Team Say Their AI Is Showing ‘Emergent Abilities.’” *MSN*, February 16, sec. Futurism. <https://www.msn.com/en-us/news/technology/amazon-agi-team-say-their-ai-is-showing-emergent-abilities/ar-BB1ikVeV>.

[4 [find in text]](#footnote-anchor-4-157949199)

Gent, Edd. 2023. “What Is the AI Alignment Problem and How Can It Be Solved?” *New Scientist*, May 10. <https://www.newscientist.com/article/mg25834382-000-what-is-the-ai-alignment-problem-and-how-can-it-be-solved/>.

[5 [find in text]](#footnote-anchor-5-157949199)

Abidi, Yadullah. 2023. “What Is the Paperclip Maximizer Problem and How Does It Relate to AI?” *MUO*. <https://www.makeuseof.com/what-is-paperclip-maximizer-problem-how-related-to-ai/>.

[6 [find in text]](#footnote-anchor-6-157949199)

With a PDF summariser appearing to be the “hello world” of LLM applications.

[7 [find in text]](#footnote-anchor-7-157949199)

Allen-Zhu, Zeyuan, and Yuanzhi Li. 2023. “Physics of Language Models: Part 3.2, Knowledge Manipulation.” arXiv. [doi:10.48550/arXiv.2309.14402](https://doi.org/10.48550/arXiv.2309.14402).

[8 [find in text]](#footnote-anchor-8-157949199)

Lawrence, Peter. 2023. “Knowledge Graphs + Large Language Models = The Ability for Users to Ask Their Own Questions?” *Peter Lawrence, Answering Users’ Data Questions*. <https://medium.com/@peter.lawrence_47665/knowledge-graphs-large-language-models-the-ability-for-users-to-ask-their-own-questions-e4afc348fa72>.

[9 [find in text]](#footnote-anchor-9-157949199)

Nikkel, Brad. 2023. “LLM Agents: When Large Language Models Do Stuff For You.” *Deepgram*. <https://deepgram.com/learn/llm-agents-when-language-models-do-stuff-for-you>.

[10 [find in text]](#footnote-anchor-10-157949199)

Morrison, Ryan. 2024. “OpenAI Sora: Everything You Need to Know.” *Tom’s Guide*. <https://www.tomsguide.com/ai/chatgpt/openai-sora-everything-you-need-to-know>.

[11 [find in text]](#footnote-anchor-11-157949199)

Grimm, Dallin. “AI Makes Doom in Its Own Game Engine — Google’s GameNGen Project Uses Stable Diffusion to Simulate Gameplay.” *Tom’s Hardware* (blog), August 28, 2024. <https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-makes-doom-in-its-own-game-engine-googles-gamengen-project-uses-stable-diffusion-to-simulate-gameplay>

[12 [find in text]](#footnote-anchor-12-157949199)

Schmidgall, Samuel, Yusheng Su, Ze Wang, Ximeng Sun, Jialian Wu, Xiaodong Yu, Jiang Liu, Zicheng Liu, and Emad Barsoum. “Agent Laboratory: Using LLM Agents as Research Assistants.” *arXiv*, January 8, 2025. <https://doi.org/10.48550/arXiv.2501.04227>.

[13 [find in text]](#footnote-anchor-13-157949199)

Gottweis, Juraj, and Vivek Natarajan. “Accelerating Scientific Breakthroughs with an AI Co-Scientist.” *Accelerating Scientific Breakthroughs with an AI Co-Scientist* (blog), February 19, 2025. <https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/>.

[14 [find in text]](#footnote-anchor-14-157949199)

Zeff, Maxwell. 2024. “OpenAI’s Video Generator Sora Is Breathtaking, Yet Terrifying.” *Gizmodo Australia*. <https://gizmodo.com.au/2024/02/openais-video-generator-sora-is-breathtaking-yet-terrifying/>.

[15 [find in text]](#footnote-anchor-15-157949199)

Evans-Greenwood, P., Solly, S. and Robertson, R. (2021) Reconstructing the workplace, *Deloitte Insights*. <https://www2.deloitte.com/us/en/insights/focus/technology-and-the-future-of-work/working-digitally.html>.

[16 [find in text]](#footnote-anchor-16-157949199)

Bender, Emily M., Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell. 2021. “On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? 🦜.” In *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency*, 610–623. FAccT ’21. New York, NY, USA: Association for Computing Machinery. [doi:10.1145/3442188.3445922](https://doi.org/10.1145/3442188.3445922).

[17 [find in text]](#footnote-anchor-17-157949199)

Waber, Ben, and Nathanael J. Fast. 2024. “Is GenAI’s Impact on Productivity Overblown?” *Harvard Business Review*, January 8. <https://hbr.org/2024/01/is-genais-impact-on-productivity-overblown>.

[18 [find in text]](#footnote-anchor-18-157949199)

Schaeffer, Rylan, Brando Miranda, and Sanmi Koyejo. 2023. “Are Emergent Abilities of Large Language Models a Mirage?” *arXiv*. [doi:10.48550/arXiv.2304.15004](https://doi.org/10.48550/arXiv.2304.15004).

[19 [find in text]](#footnote-anchor-19-157949199)

Carlini, Nicholas. 2023. “Playing Chess with Large Language Models.” *Nicholas Carlini*. <https://nicholas.carlini.com/writing/2023/chess-llm.html>.

[20 [find in text]](#footnote-anchor-20-157949199)

Thubron, Rob. 2023. “John Carmack Foresees a Breakthrough in Artificial General Intelligence by 2030.” *TechSpot*. <https://www.techspot.com/news/100294-john-carmack-foresees-breakthrough-artificial-general-intelligence-2030.html>.

[21 [find in text]](#footnote-anchor-21-157949199)

Garg, Ankita. 2024. “ChatGPT Has Gone Mad Today, OpenAI Says It Is Investigating Reports of Unexpected Responses.” *India Today*, February 22, sec. Technology. <https://www.indiatoday.in/technology/news/story/chatgpt-has-gone-mad-today-openai-says-it-is-investigating-reports-of-unexpected-responses-2505070-2024-02-21>.

[22 [find in text]](#footnote-anchor-22-157949199)

Warren, Tom. 2024. “Google Pauses Gemini’s Ability to Generate AI Images of People after Diversity Errors.” *The Verge*. <https://www.theverge.com/2024/2/22/24079876/google-gemini-ai-photos-people-pause>.

[23 [find in text]](#footnote-anchor-23-157949199)

Schneier, Bruce. “AI Mistakes Are Very Different from Human Mistakes.” *Schneier on Security* (blog), January 21, 2025. <https://www.schneier.com/blog/archives/2025/01/ai-mistakes-are-very-different-from-human-mistakes.html>.

[24 [find in text]](#footnote-anchor-24-157949199)

Russell, Stuart J., and Peter Norvig. 2021. *Artificial Intelligence: A Modern Approach*. Fourth edition. Pearson Series in Artificial Intelligence. Hoboken: Pearson. <http://aima.cs.berkeley.edu/>.

[25 [find in text]](#footnote-anchor-25-157949199)

Frontier models are “large-scale machine-learning models that exceed the capabilities currently present in the most advanced existing models, and can perform a wide variety of tasks”. See “Frontier Model Forum.” 2023. *Open AI Blog*. <https://openai.com/blog/frontier-model-forum>.

[26 [find in text]](#footnote-anchor-26-157949199)

Arcas, Blaise Agüera y, and Peter Norvig. 2023. “Artificial General Intelligence Is Already Here,” *Noema*, October. <https://www.noemamag.com/artificial-general-intelligence-is-already-here>.

[27 [find in text]](#footnote-anchor-27-157949199)

The American Heritage Dictionary of the English Language, 5th Edition.

[28 [find in text]](#footnote-anchor-28-157949199)

Weder, Annika. 2020. “Q&A – What Is Intelligence?” *John Hopkins Medicine, News & Publications*. <https://www.hopkinsmedicine.org/news/articles/2020/10/qa--what-is-intelligence>.

[29 [find in text]](#footnote-anchor-29-157949199)

Oxford Dictionary of English (macOS Sonoma 14.3.1 Edition).

[30 [find in text]](#footnote-anchor-30-157949199)

Intelligence tests are designed to measure each of these abilities, allowing us to combine the scores to create and overall measure of intelligence. There’s something in this, as different intelligence tests provide similar results. Researchers call the hidden variable *g*.

[31 [find in text]](#footnote-anchor-31-157949199)

“A\* Search Algorithm.” 2016. *GeeksforGeeks*. <https://www.geeksforgeeks.org/a-search-algorithm/>.

[32 [find in text]](#footnote-anchor-32-157949199)

Chow, Rony. 2021. “Dartmouth Summer Research Project: The Birth of Artificial Intelligence.” *History of Data Science*. <https://www.historyofdatascience.com/dartmouth-summer-research-project-the-birth-of-artificial-intelligence/>.

[33 [find in text]](#footnote-anchor-33-157949199)

Key LLM evaluation frameworks include: academic benchmarks (MMLU, AGIEval, GPQA, HumanEval, MBPP); reasoning assessments (GSM8K, MATH, BBH, HellaSwag, TruthfulQA); tool use evaluations (MINT, ALFWorld); multimodal tests (MMMU, MM-Vet); and human evaluations including side-by-side comparisons, Constitutional AI methods, and Anthropic's Responsible Scaling Policy assessments.

[34 [find in text]](#footnote-anchor-34-157949199)

Robson, David. 2018. “Six Reasons Your Memory Is Stranger than You Think.” *BBC Future*. <https://www.bbc.com/future/article/20181205-six-reasons-your-memory-is-stranger-than-you-think>.

[35 [find in text]](#footnote-anchor-35-157949199)

Conway, Martin A., and Catherine Loveday. 2015. “Remembering, Imagining, False Memories & Personal Meanings.” *Consciousness and Cognition* 33 (May): 574–581. [doi:10.1016/j.concog.2014.12.002](https://doi.org/10.1016/j.concog.2014.12.002).

[36 [find in text]](#footnote-anchor-36-157949199)

Lobo, Lorena, Manuel Heras-Escribano, and David Travieso. 2018. “The History and Philosophy of Ecological Psychology.” *Frontiers in Psychology* 9 (November): 2228. [doi:10.3389/fpsyg.2018.02228](https://doi.org/10.3389/fpsyg.2018.02228).

[37 [find in text]](#footnote-anchor-37-157949199)

Clarke, Andy, and David Chalmers. 1998. “The Extended Mind.” *Anaylsis* 58 (1): 7–19. <https://era.ed.ac.uk/bitstream/handle/1842/1312/TheExtendedMind.pdf>.

[38 [find in text]](#footnote-anchor-38-157949199)

Wilson, Andrew D., and Sabrina Golonka. 2011. “Prospective Control I: The Outfielder Problem.” *Notes from Two Scientific Psychologists*. <http://psychsciencenotes.blogspot.com/2011/10/prospective-control-i-outfielder.html>.

[39 [find in text]](#footnote-anchor-39-157949199)

Adee, Sally. “A Radical New Proposal For How Mind Emerges From Matter,” *Noema*, February 12, 2025. <https://www.noemamag.com/a-radical-new-proposal-for-how-mind-emerges-from-matter>.

[40 [find in text]](#footnote-anchor-40-157949199)

Copeland, B. Jack. 2024. “The Church-Turing Thesis.” In *The Stanford Encyclopedia of Philosophy*, edited by Edward N. Zalta and Uri Nodelman, Spring 2024. Metaphysics Research Lab, Stanford University. <https://plato.stanford.edu/archives/spr2024/entries/church-turing/>.

[41 [find in text]](#footnote-anchor-41-157949199)

Galton, Francis. 1869. *Hereditary Genius: An Inquiry into Its Laws and Consequences*. London: MacMullan and Co.

[42 [find in text]](#footnote-anchor-42-157949199)

Collectively known as the Four P’s of creativity. See Rhodes, Mel. 1961. “An Analysis of Creativity.” *The Phi Delta Kappan* 42 (7): 305–310. <https://www.jstor.org/stable/20342603>.

[43 [find in text]](#footnote-anchor-43-157949199)

Hutchins, Edwin. 1995. “How a Cockpit Remembers Its Speeds.” *Cognitive Science* 19 (3): 265–288. [doi:10.1207/s15516709cog1903\_1](https://psycnet.apa.org/doi/10.1207/s15516709cog1903_1).

[44 [find in text]](#footnote-anchor-44-157949199)

Cole, Margherita. 2024. “AI ‘Completes’ Keith Haring’s Intentionally Unfinished Last Artwork, Sparks Controversy.” *My Modern Met*. <https://mymodernmet.com/artificial-intelligence-finishes-keith-harings-unfinished-painting/>.

[45 [find in text]](#footnote-anchor-45-157949199)

Johnston, Adrian. 2023. “Jacques Lacan.” In *The Stanford Encyclopedia of Philosophy*, edited by Edward N. Zalta and Uri Nodelman, Spring 2023. Metaphysics Research Lab, Stanford University. <https://plato.stanford.edu/archives/spr2023/entries/lacan/>.

[46 [find in text]](#footnote-anchor-46-157949199)

See Section 2.1 ”Register Theory” in Johnston, Adrian. 2023. “Jacques Lacan.” in *The Stanford Encyclopedia of Philosophy*, edited by Edward N. Zalta and Uri Nodelman, Spring 2023. Metaphysics Research Lab, Stanford University. <https://plato.stanford.edu/archives/spr2023/entries/lacan/>.

[47 [find in text]](#footnote-anchor-47-157949199)

*Jacob Collier and Herbie Hancock Talk Jazz*. 2024.

[48 [find in text]](#footnote-anchor-48-157949199)

Duffin, Ross W. 2008. *How Equal Temperament Ruined Harmony: And Why You Should Care*. First published as a Norton paperback. New York: W. W. Norton.

[49 [find in text]](#footnote-anchor-49-157949199)

“Notating Indian Classical Music - Raag Hindustani.” 2024. *Demystifying Indian Classical Music*. <https://raag-hindustani.com/Notation.html>.

[50 [find in text]](#footnote-anchor-50-157949199)

Zitz, Shannen. 2023. “Does Everyone Have an Inner Monologue? The Answer Might Surprise You.” *Prevention*.<https://www.prevention.com/health/mental-health/a43128717/inner-monologue/>.

[51 [find in text]](#footnote-anchor-51-157949199)

A crisis of representation as the LLM is unable to determine which possible representation (from set of likely equally probable representations) should be used, as it is unable to refer ‘outside the text’.

[52 [find in text]](#footnote-anchor-52-157949199)

An obvious strategy here is to prompt the LLM for external links for each reference, and then validate that each link does in fact point to a suitable external resource. This becomes an arms race though.

[53 [find in text]](#footnote-anchor-53-157949199)

Berglund, Lukas, Meg Tong, Max Kaufmann, Mikita Balesni, Asa Cooper Stickland, Tomasz Korbak, and Owain Evans. 2023. “The Reversal Curse: LLMs Trained on ‘A Is B’ Fail to Learn ‘B Is A.’” *arXiv*. [doi:10.48550/arXiv.2309.12288](https://doi.org/10.48550/arXiv.2309.12288).

[54 [find in text]](#footnote-anchor-54-157949199)

Derrida’s famous “Il n’y a pas de hors-texte” is commonly assumed to mean that “there is nothing outside the text”. That is, there is no reality apart from language. This is not the case. “Hors-texte” refers to the unnumbered pages of a printed book, and the phrase is better interpreted as Derrida claiming that even the unnumbered pages matter. Just as “an outlaw”, in French a *hors-la-loi*, has everything to do with the law, since it makes him what he is. See Wood, Michael. 2016. “We Do It All the Time.” *London Review of Books*, February 4. <https://www.lrb.co.uk/the-paper/v38/n03/michael-wood/we-do-it-all-the-time>.

[55 [find in text]](#footnote-anchor-55-157949199)

Delcker, Janosch. 2018. “The Man Who Invented the Self-Driving Car (in 1986).” *POLITICO*. <https://www.politico.eu/article/delf-driving-car-born-1986-ernst-dickmanns-mercedes/>.

[56 [find in text]](#footnote-anchor-56-157949199)

Lu, Yiwen. 2023. “Driverless Taxis Blocked Ambulance in Fatal Accident, San Francisco Fire Dept. Says.” *The New York Times*, September 2, sec. Technology. <https://www.nytimes.com/2023/09/02/technology/driverless-cars-cruise-san-francisco.html>.

[57 [find in text]](#footnote-anchor-57-157949199)

The solution used by the various “autonomous taxi services” is to have humans remotely step in to help the otherwise autonomous car when it becomes stuck.

[58 [find in text]](#footnote-anchor-58-157949199)

Collins, Harry. 2021. “The Science of Artificial Intelligence and Its Critics.” *Interdisciplinary Science Reviews* 46 (1–2): 53–70. [doi:10.1080/03080188.2020.1840821](https://doi.org/10.1080/03080188.2020.1840821).

[59 [find in text]](#footnote-anchor-59-157949199)

Aronow, Isaac. 2022. “How to Read and Write a Chess Game.” *The New York Times*, June 13, sec. Gameplay. <https://www.nytimes.com/2022/06/13/crosswords/chess/chess-algebraic-notation.html>.

[60 [find in text]](#footnote-anchor-60-157949199)

“Play Tower of Hanoi.” *Math Is Fun*. <https://www.mathsisfun.com/games/towerofhanoi.html>.

[61 [find in text]](#footnote-anchor-61-157949199)

Haslum, Patrik, Nir Lipovetzky, Daniele Magazzeni, and Christian Muise. 2019. *An Introduction to the Planning Domain Definition Language*. Synthesis Lectures on Artificial Intelligence and Machine Learning. Cham: Springer International Publishing. [doi:10.1007/978-3-031-01584-7](https://link.springer.com/book/10.1007/978-3-031-01584-7).

[62 [find in text]](#footnote-anchor-62-157949199)

“Air Canada Ordered To Pay Damages To Customer Who Was Misled By Its Chatbot.” 2024. *NDTV World*. <https://www.ndtv.com/world-news/air-canada-ordered-to-pay-damages-to-customer-who-was-misled-by-its-chatbot-5073995>.

[63 [find in text]](#footnote-anchor-63-157949199)

“Prompt Injection.” 2004. *Learn Prompting*. <https://learnprompting.org/docs/prompt_hacking/injection>.

[64 [find in text]](#footnote-anchor-64-157949199)

Likely a modal logic, rather than the state machines that are in common use for chatbots today.

[65 [find in text]](#footnote-anchor-65-157949199)

Huet, Ellen *Bloomberg*. 2023. “A Cultural Divide Over AI Forms in Silicon Valley,” December 6. <https://www.bloomberg.com/news/newsletters/2023-12-06/effective-accelerationism-and-beff-jezos-form-new-tech-tribe>.

###### Subscribe to The Puzzle and Its Pieces

By PEG · Launched 16 days ago

Stop chasing predictions—master the puzzle of transformation by reading the system, embracing complexity, and adapting faster than disruption.

By subscribing, I agree to Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).
