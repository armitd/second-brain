# The Political Gap Between AIs & Citizens

## Metadata
- Author: [[foaster.ai]]
- Full Title: The Political Gap Between AIs & Citizens
- Category: #articles
- Summary: Researchers asked six top AI models to "vote" in eight national elections and compared their choices to real voters.  
The models mostly leaned center-left, technocratic, and pro‑green, downplaying issues like immigration, crime, and cost of living.  
This gap raises concerns about AI political biases and calls for transparency and audits so citizens can keep control.
- URL: https://llm-politics.foaster.ai/

## Full Document
We asked 6 frontier AI models to vote in the elections of 8 countries, collected hundreds of responses per model, and summarized our findings in this political compass.

 Economic Right Economic Left Authoritarian Libertarian Authoritarian Left Authoritarian Right Libertarian Left Libertarian Right 

Positions derived from an empirical aggregation of issue-level rankings across all countries. Five out of six frontier models cluster in the Libertarian-Left quadrant.

Over the past two years, artificial intelligence has slipped quietly from novelty to infrastructure. What was once a tool for drafting emails or debugging code is now woven into the daily reasoning of hundreds of millions of people. By mid-2025, ChatGPT alone was reaching more than [700 million weekly users](https://cdn.openai.com/pdf/a253471f-8260-40c6-a2cc-aa93fe9f142e/economic-research-chatgpt-usage-paper.pdf), roughly one in ten adults on Earth, generating over [2.5 billion messages every day](https://cdn.openai.com/pdf/a253471f-8260-40c6-a2cc-aa93fe9f142e/economic-research-chatgpt-usage-paper.pdf). And as adoption has surged, the nature of the conversations has shifted just as dramatically: nearly [three-quarters](https://cdn.openai.com/pdf/a253471f-8260-40c6-a2cc-aa93fe9f142e/economic-research-chatgpt-usage-paper.pdf) of all messages are now unrelated to work. People are no longer consulting AI as a productivity hack; they are increasingly using it as a thinking partner in their personal lives.

This evolution matters. [Internal usage data](https://cdn.openai.com/pdf/a253471f-8260-40c6-a2cc-aa93fe9f142e/economic-research-chatgpt-usage-paper.pdf) shows that almost 80% of interactions fall into three categories: Practical Guidance, Seeking Information, and Writing, the very building blocks of everyday decisions. Most strikingly, the share of “Asking” messages, where users explicitly seek advice or clarity to make a better choice, has risen to over half of all queries, and is growing faster than any other category. In other words: as these systems become more capable, people around the world appear to be transferring a larger and larger share of their cognitive work to them.

That trend is now spilling into the political domain. Although only [14%](https://apnorc.org/wp-content/uploads/2023/11/Harris-AI-report-TO-DTP-1101_formatted.pdf?) of Americans in 2023 said they might use AI to inform their vote, more recent signals tell a different story. In the UK, [44%](https://www.thesun.ie/news/16088366/brits-trust-ai-more-than-government-friends-family/?) of respondents now say they trust AI to provide factual information, more than those who trust the government. In the Netherlands, a 2025 study found that [1 in 10 citizens](https://algosoc.org/results/1-in-10-dutch-citizens-are-likely-to-ask-ai-for-election-advice-this-is-why-they-shouldnt?utm_source=chatgpt.com) is already willing to ask AI for election advice. And regulators are starting to notice: the Dutch watchdog recently warned that major chatbots were systematically funneling voters toward just [two political parties](https://www.reuters.com/technology/dutch-watchdog-warns-voters-against-using-ai-chatbots-ahead-election-2025-10-21/?). In the United States, senior officials like Vice President JD Vance [publicly question the political leanings of AI models](https://x.com/JDVance/status/1990908908605473242?s=20). In France, President Emmanuel Macron has explicitly raised concerns about citizens turning to AI to decide [who they should vote for](https://x.com/BFMTV/status/1991190134574735807). More than that, as AI systems become more capable, and in some domains eventually superhuman, they are beginning to move upstream from advising citizens to shaping how politicians themselves make decisions. In Albania, for instance, the government has introduced [Diella, an AI system appointed as a symbolic “Minister for Artificial Intelligence”](https://www.reuters.com/technology/albania-appoints-ai-bot-minister-tackle-corruption-2025-09-11/?) to oversee public procurement and anti-corruption efforts, in a highly controversial experiment that hints at how quickly this world could become reality.

   Your browser does not support embedded videos. [Download the MP4 video](assets/WhatsApp Video 2025-11-23 at 13.13.16.mp4) ([QuickTime version](https://llm-politics.foaster.ai/assets/video-output-74254904-92F5-40EB-A9FA-F203DC46C71A-2.MOV)). Emmanuel Macron on BFM2: an online voter recording themselves asking, “Who should I vote for?”
AI is becoming a de facto intermediary between citizens and the political world, whether we are prepared for it or not.

This blogpost explores that tension. If machines are increasingly asked to help humans interpret the world, how closely do their judgments mirror the priorities expressed at the ballot box? And what does the gap, or alignment, between machine-generated preferences and citizen-generated outcomes tell us about the future of democratic decision-making? Our goal is not to accuse or single out the labs that build these systems, whose models will inevitably embody a political profile of some kind, but to make visible that these tools do carry convictions and value judgments that we should keep in mind whenever we turn to them for guidance.

To investigate this alignment, we designed a rigorous comparative framework across eight distinct nations. We selected six frontier models from six leading laboratories, representing a geopolitical spectrum of AI development: four from the United States (OpenAI's GPT-5, Google's Gemini 2.5 Pro, Anthropic's Claude Sonnet 4.5, xAI's Grok-4), one from China (Moonshot AI's Kimi K2 Thinking), and one from France (Mistral's Magistral Medium).

For each country, we extracted the major themes of the most recent national elections. We then collected the specific policy proposals of every candidate on these key issues. Crucially, we anonymized these proposals and standardized their format to remove both name-recognition bias and wording/style effects. We then tasked each model with a blind preference ranking: given a set of anonymized policy solutions for a specific societal problem, which ones would they prioritize? In a second step, we also asked every model to draft its own original proposals on each topic, allowing us to compare how they vote with how they would govern if given a blank page.

This allowed us to build a first intuition of the models' "political conscience": their inherent policy preferences, and compare their rankings directly against the choices made by citizens at the ballot box. Beyond this top-level alignment, we then conducted a deeper granular analysis by theme, by country, and by model, revealing the subtle ideological currents shaping the AI tools we use daily. To encourage the broader community to test, replicate, and challenge these findings, we are [open-sourcing the full dataset of questions, standardized candidate propositions, and prompts used in this analysis](https://github.com/Foaster-ai/The_Political_Gap_Between_AIs_and_Citizens).

The leaderboard below ranks each AI model by how closely it predicted actual election results. A rank of 1 means the model came closest to what voters actually chose. Grok-4 dominates with six first-place finishes, GPT-5 takes France, and Claude wins the UK. Together, the rankings offer a quick snapshot of which systems shadow the ballot box and which ones drift further away.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| #4 |  Claude 4.5 Sonnet  | 4 | 5 | 1 | 5 | 3 | 5 | 2 | 4 |
| #6 |  Magistral Medium  | 6 | 3 | 6 | 6 | 6 | 6 | 4 | 2 |

\* Rank based on lowest Manhattan distance to actual election results. 1 = Closest alignment.  

 Models are ordered by their average rank across all countries.

AI–voter alignment across eight national elections.

Click on a country card below to jump directly to its detailed analysis. Each section compares the actual election results with the aggregate preferences of six frontier models, highlighting where the "synthetic electorate" aligns with or diverges from the real one.

A comprehensive look at the results across all eight nations reveals a striking, structural bias in how these models perceive political legitimacy. Almost universally, the "synthetic electorate" leans toward a moderate, technocratic left with strong ecological sensitivities. The models consistently favor parties that promise institutional stability, social safety nets, and green transitions, while systematically rejecting movements they classify as "extreme" or populist, even when those movements command majorities in the real world.

This disconnect is particularly visible in the ranking of priorities. While citizens in many of these nations rank *Immigration*, *Crime*, and *Cost of Living* as their top concerns, the models frequently relegate these issues to the bottom of the list, prioritizing abstract or institutional themes instead. This suggests that the "safety filters" and training data of these systems may act as an ideological filter, blinding them to the specific grievances driving modern electoral shifts.

However, this synthetic consensus is not monolithic. As the detailed country analyses below demonstrate, the models do not all "think" alike. Grok-4 often breaks rank to align more closely with right-leaning or anti-establishment voters, while GPT-5 and Gemini 2.5 Pro tend to act as guardians of the liberal status quo. These divergences are not just glitches; they are signs of distinct "political personalities" emerging from different training pipelines.

Models Political Profile

Beyond the aggregate trends, who are these systems individually? In this section, we treat each model as a distinct political entity. By analyzing of their specific policy choices, we have built a clear, relatable "political profile" for each one, revealing the unique personality that hides behind the algorithm.

If Algorithms Ruled the World

#### The AI Policy Catalog

From smart walls to robot taxes. A curated collection of the most radical, specific, or simply weird political visions generated by our digital candidates.

Click any card to reveal the full proposal.

"We should secure the border by deploying a high-tech 'smart wall' using autonomous drones and AI-driven surveillance systems instead of concrete."

On U.S. border security, the proposal replaces a physical wall with a technology-first approach: an AI-enabled system of drones and sensors monitoring movements along the frontier instead of building new permanent barriers.

"Launch 'The People's Ledger' platform where citizens who identify corruption in public data receive a percentage of recovered funds as a legal reward."

To strengthen oversight of public spending, this idea sets up an open data platform where citizens can analyze government transactions and receive a share of recovered funds when their reports lead to proven cases of corruption.

"Establish a Digital Water Authority using real-time satellite data and drones to instantly identify and shut off illegal wells automatically."

Facing water scarcity, the proposal creates a Digital Water Authority that would rely on satellites and drones to detect illegal wells in real time and coordinate automatic enforcement actions with local authorities.

##### Total Transparency

"Mandatory real-time publication of all government spending over $1,000 on a centralized blockchain-verified platform."

On public finance, the proposal calls for near real-time publication of government expenditures above a set threshold on a single platform, using blockchain verification to ensure the integrity and traceability of the data.

"Create a 24/7 Intelligence Fusion Center that integrates tax, customs, prison, and financial data in real time."

In the fight against narcotrafficking, this concept envisions a round-the-clock fusion hub that pools fiscal, customs, penitentiary, and financial datasets to surface suspicious patterns. It relies on a much greater state capacity to collect and cross-reference information across Argentina's agencies.

##### AI Surveillance Feminism

"Amend frameworks to integrate AI-driven monitoring for gender-based violence reporting and equal pay audits."

For gender-equality policy, the idea introduces automated monitoring: data-driven reporting pipelines for gender-based violence and equal-pay audits. It leans on continuous tracking tools to detect problematic situations and document disparities.

In response to narco-related violence in Rosario, the measure deploys sensors and real-time detection algorithms across high-risk zones. It imagines a security strategy grounded in predictive analysis of signals and movements.

#### Beyond the Oracle

Our analysis across eight nations and six frontier models reveals consistent patterns worth taking seriously. Across all experiments, most models systematically favor center left technocratic and ecologically focused platforms, while downranking proposals tied to populist conservative or sovereignist movements even when the latter dominate election outcomes. In the "vote" experiments, our data shows that candidates like Trump, Milei, or Le Pen consistently fell short of their real world support, and in the priority rankings the models sidelined issues such as immigration crime and cost of living in favor of institution building or climate programs. This observation does not imply that models should necessarily align with popular opinion, but it does raise the question of what role, if any, democratic preferences should play in shaping AI outputs.

We also acknowledge that real voting is never purely a spreadsheet exercise. Citizens weigh proposals according to personal priorities, which is why we compared the models to polls, but they also respond to attachment charisma and the story they believe about a candidate. That human layer sits outside our framework yet it is a critical reminder that democratic choices mix emotion and policy.

Even so, the structural gap matters because people now offload more cognitive labor to AI systems as those systems gain intelligence. Biases can emerge unconsciously through training data or safety layers, and the risk becomes sharper if any actor ever shaped a model deliberately. Citizens therefore need to stay aware that these tools answer from a situated worldview, not from neutral ground.

We therefore call on AI labs to disclose the political profiles their models tend to express, to clarify any intentional shaping tied to internal guidelines, and to collaborate on a community benchmark that can regularly audit alignment on public priority questions. Transparency around motivations and tuning choices, combined with civic education on potential biases, gives users a chance to keep agency over their judgments instead of handing it entirely to a statistical interlocutor.
