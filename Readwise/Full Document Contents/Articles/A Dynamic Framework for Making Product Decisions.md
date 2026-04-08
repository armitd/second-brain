# A Dynamic Framework for Making Product Decisions

![rw-book-cover](https://d24ovhgu8s7341.cloudfront.net/uploads/post/social_media_image/3476/puzzle.png)

## Metadata
- Author: [[Edmar Ferreira]]
- Full Title: A Dynamic Framework for Making Product Decisions
- Category: #articles
- Summary: VICE is a new product prioritization framework that uses pairwise comparisons to rank features based on their relative value. Unlike traditional scoring systems, VICE adapts to evolving insights and emphasizes human judgment. This dynamic approach helps teams make better decisions by directly comparing features and understanding trade-offs.
- URL: https://every.to/source-code/introducing-vice-a-dynamic-framework-for-making-product-decisions

## Full Document
![](https://d24ovhgu8s7341.cloudfront.net/uploads/post/cover/3476/puzzle.png)DALL-E/Every illustration.
Frustrated with product frameworks that feel static and forced, I built one that can evolve along with my thought process

Having built products for over a decade, I've encountered my fair share of challenges when it comes to prioritization. Whether it's deciding which features to build next or figuring out how to allocate resources, it often boils down to balancing intuition with structured [frameworks](https://every.to/c/ai-frontiers).

I've experimented with various methods, from gut-driven decisions to widely-used scoring systems like RICE (Reach, Impact, Confidence, Effort), a framework that was popularized by the customer support software firm Intercom and is now used at companies like Spotify and DoorDash. You score your proposed product decision from 0 to 10 for each category and use those category scores to compute a final score. Features that score the highest should be prioritized.

While these scoring methods bring much-needed structure to decision-making—helping teams quantify and compare different opportunities—I've always felt they miss a critical element: the subtle interplay of human judgment and context.

Why do we try to reduce complex, multi-dimensional decisions to absolute scores? These scores often feel like a facade—an attempt to rationalize instinct rather than genuinely informing our choices. So I decided to explore how we might evolve these frameworks, maintaining their structural benefits while embracing a more dynamic and intuitive process.

Driven by these frustrations—and inspired by the principles of selfish software—I built my own prioritization tool. I called it VICE**:** Vibe, Impact, Confidence, Effort.

VICE is designed to reflect the nuances of human judgment, intuition, and evolving context. And like the best [selfish software](https://every.to/source-code/selfish-software), it started as a tool I built purely for myself. Now, I’m excited to share it—because I believe prioritization should feel intuitive, flexible, and genuinely useful, not just structured and rationalized.

#### The limits of absolute scoring

The RICE (Reach, Impact, Confidence, Effort) product prioritization framework works by giving scores for each of its attributes and computing a final score. For example:

* **Reach:** How many people will this feature impact? (Estimate within a defined time period.)
* **Impact:** How much impact will this feature have on each person? (Massive = 3x, high = 2x,medium = 1x, low = 0.5x, minimal = 0.25x)
* **Confidence:** How confident are you in your estimates? (High = 100%, medium = 80%, low = 50%)
* **Effort:** How many “person-months” will this take? (Use whole numbers and a minimum of half a month. Don’t get into the weeds of estimation.)

Score = (Reach \* Impact \* Confidence)/Effort

Let’s use this formula in two examples that we’re considering building:

1. **A simpler onboarding tutorial** that’s quicker to build and directly addresses user drop-off.
2. A **chatbot upgrade** that improves user interaction and requires significant development time.

###### Example 1: Onboarding tweak

* **Reach:** 5,000 new users per month who go through the onboarding process
* **Impact:** High (2x)—significant improvement to user understanding and retention
* **Confidence:** Medium (80%)—based on similar changes and user feedback
* **Effort:** 0.5 person-months (a relatively quick implementation)

RICE score calculation:

* Score = (Reach × Impact × Confidence)/Effort
* Score = (5,000 × 2 × 0.8)/0.5
* Score = 16,000

###### Example 2: Advanced chatbot integration

* **Reach:** 12,000 users per month who use customer support
* **Impact:** Medium (1x)—improved support experience
* **Confidence:** Low (50%)—new technology with uncertain adoption
* **Effort:** 4 person-months (substantial development effort)

RICE score calculation:

* Score = (Reach × Impact × Confidence)/Effort
* Score = (12,000 × 1 × 0.5)/4
* Score = 1,500

According to the RICE framework, the onboarding tweak (score: 16,000) would be prioritized over the chatbot integration (score: 1,500). The onboarding tweak affects a substantial number of users, has a high impact and good confidence, and requires minimal effort, resulting in the highest overall score.

Frameworks like RICE provide structure and clarity, forcing you to think critically about the impact, confidence, and the effort necessary to achieve an outcome. When I first adopted the RICE framework in my role at a previous company, we had a backlog overflowing with ideas, each backed by passionate team members. By scoring each idea with RICE, we discovered that our excitement had previously blinded us—some high-effort tasks had low projected impact. One initiative, that seemingly modest onboarding tweak we’d overlooked, surfaced as a clear winner. We prioritized it, and within weeks our user retention jumped nearly 15 percent. RICE cut through our biases, showing us what mattered most.

But they also come with significant limitations:

**Assigning absolute scores to features is rarely an objective process.** Personal biases and incomplete data can easily influence how we evaluate a feature's impact or the effort it requires. Stakeholders may overestimate the impact of initiatives they champion while underestimating technical complexity they don't fully understand. That can lead to skewed prioritization decisions that don't reflect true value.

**Predicting precise values for attributes like impact or reach is inherently difficult,** especially for innovative or unprecedented features. Scores may be more guesswork than grounded reality. Without historical data or comparable reference points, teams resort to speculation and assumptions, undermining the framework's purpose of bringing objectivity to the process.

**Scores can oversimplify complex trade-offs**, leading teams to prioritize the "highest score" rather than what's truly valuable. Therein lies one of the principal dangers in letting numbers dictate decision-making: It often results in short-sighted decisions that look good on paper but fail to address deeper user needs or business objectives.

These limitations are what prompted me to rethink the approach entirely. Instead of trying to assign perfect scores to individual features, what if we focused on how features compare to one another?

#### Enter VICE: A new prioritization tool

VICE uses pairwise comparisons and the Elo rating system to rank features dynamically. The name VICE is a play on the ICE framework, but with an added “V” to emphasize the “vibe” of intuition and relative judgment, capturing the essence of subjective yet structured decision-making.

The Elo rating system, originally developed by Hungarian-American physics professor **Arpad Elo** to rank chess players, assigns a numerical rating to each item—in this case, product features—to reflect their relative strength or value. Each feature starts with an initial rating, and then features are compared head-to-head through a series of pairwise matchups—one against the other, as in a tournament. After each comparison, ratings are adjusted: The winning feature’s rating increases while the losing feature’s rating decreases. Over multiple comparisons, Elo ratings naturally evolve to reflect an intuitive yet mathematically sound ranking that aligns closely with user judgments.

Here’s how it works:

###### **1. Make a pairwise comparison**

Instead of scoring features in isolation, VICE asks you to compare any two features at a time. For each pair, evaluate which feature has a greater impact, higher confidence, or better ease of implementation—or if it’s a draw.

The system presents comparison-based questions, such as: “Which feature would have a greater impact: the onboarding tweak or the advanced chatbot integration?” The user selects one of the two options, transforming the prioritization process into an engaging, game-like experience.

[![](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3476/optimized_1.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3476/optimized_1.png)
*A feature choice in VICE. Source: Edmar Ferreira.*

###### 2. **Use the Elo rating system**

Just like in chess rankings, every feature starts with a base rating (e.g., 1,500 points). When you compare two features, the "winner" gains points while the "loser" loses points. The amount of points exchanged depends on the expected outcome—beating a higher-rated feature earns more points than beating a lower-rated one. Features that consistently win comparisons accumulate higher ratings and naturally rise to the top of your priority list, while features that frequently lose comparisons drop lower. This dynamic creates an intuitive ranking that evolves with each new comparison, without requiring you to rescore everything from scratch.

For example, the user is faced with the question, “Which feature would have a greater impact: the onboarding tweak or the advanced chatbot integration?” By choosing the “onboarding tweak,” the chatbot integration loses points and the onboarding tweak gains them.

###### 3. **Calculate your VICE score**

The final ranking is based on a calculated VICE score, which is the multiplication of a feature’s impact, confidence, and effort ratings. This score evolves as you make more comparisons, ensuring that the prioritization adapts to new insights and shifting priorities. A new feature that consistently wins over other top features will naturally rise to the top fast.

The leaderboard displays six features ranked by their VICE score, as well as a breakdown of individual scores (Impact, Ease, Confidence). Each individual score is computed by winning a match with another feature on that criteria.

[![](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3476/optimized_2.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3476/optimized_2.png)
*The VICE leaderboard. Source: Edmar Ferreira.*

#### Why VICE works

VICE's comparative approach offers significant advantages over traditional scoring frameworks. By directly comparing features against each other, VICE naturally captures contextual nuances and interdependencies that absolute scoring systems miss. The framework recognizes that a feature's value isn't fixed but relative to other priorities and the broader product strategy.

Let’s return to our onboarding tweak versus chatbot upgrade example. In a traditional scoring framework like RICE, we independently assigned each feature an absolute score. But these isolated scores don’t fully capture the strategic trade-offs between the two: Does the immediate benefit of reducing user drop-off outweigh the longer-term strategic advantage of an advanced chatbot experience? With VICE, you compare them head-to-head, forcing you to explicitly evaluate trade-offs.

Your team can quickly identify not only which feature matters more right now but also clarify *why*—for instance, the urgency of improving onboarding to secure immediate growth may outweigh longer-term enhancements. VICE thus makes prioritization both dynamic and deeply contextual, aligning your roadmap directly with your evolving product strategy.

The system's flexibility comes from its ability to continuously evolve without requiring wholesale recalibration. As new information emerges or priorities shift, teams can run additional comparisons, allowing the framework to adapt naturally. Since you only need to choose between two items at a time, it takes just a few minutes to add a new item and rank it. The other features will adapt because each comparison will rescore them. For example, if you have a new chatbot feature you want to add, it will be compared to the other features and rescore the whole list.

VICE's pairwise comparison method aligns with humans’ natural decision-making processes. Rather than assigning arbitrary numerical values, product teams can rely on their judgment to make simple A/B choices. This approach leverages collective expertise while maintaining systematic rigor, bridging the gap between intuition and structured decision-making.

The Elo rating system provides a dynamic foundation for feature prioritization. Much like its original use in chess rankings, Elo creates a responsive system where priorities adjust based on the outcomes of ongoing comparisons. This ensures the product roadmap remains current and reflects evolving business needs and market conditions.

#### Building VICE with vibe coding

I built the first version of VICE over the course of one weekend. In preparation for writing this piece, I decided to experiment with “[vibe coding](https://x.com/karpathy/status/1886192184808149383)” to rebuild VICE. Instead of coding everything myself, I only talked to AI until the project was completely coded. I used SuperWhisper to talk to my computer and Claude Code, a command-line coding tool, to handle the coding. It took four hours, and only that long because I kept fiddling with the design.

[![](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3476/optimized_3.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3476/optimized_3.png)
*Terminal with Claude Code. Source: Edmar Ferreira.*

I started by creating a [product requirement document template](https://every.to/podcast/inside-the-pod-build-a-six-figure-side-hustle-in-one-weekend) using Claude Projects and provided it to Claude Code for implementation. I could focus on refining the PRD through conversation and see the changes in real time, creating a smooth workflow. This method proved effective, especially for smaller, well-defined projects without legacy code.

With the rise of AI, human judgment and intuition can be amplified—not replaced—by technology. We now have the tools to encode human judgment into systems that can augment our decision-making processes. For me, VICE represents a step in that direction—a way to marry the power of structured frameworks with the subtlety of intuition.

After all, prioritization isn’t about the perfect score—it’s about making the best possible decision with the information you have. And that’s exactly what VICE is designed to help you do.

*If you’re interested in trying the VICE framework, send me a* [*DM on X*](https://x.com/edmarferreira)*.*

[***Edmar Ferreira***](https://x.com/edmarferreira) *is an entrepreneur-in-residence at Every. Previously he founded and sold Rock Content, a leading content marketing platform.* 

*We also* [*build AI tools*](https://every.to/studio) *for readers like you. Automate repeat writing with* [***Spiral***](https://spiral.computer/?utm_source=everyfooter)*. Organize files automatically with* [***Sparkle***](https://makeitsparkle.co/?utm_source=everyfooter)*. Write something great with* [***Lex***](https://lex.page/?utm_source=everyfooter)*. Deliver yourself from email with* [***Cora***](https://cora.computer/)*.*

*We also do AI training, adoption, and innovation for companies.* [*Work with us*](https://every.to/consulting?utm_source=emailfooter) *to bring AI into your organization.*

*Get paid for sharing Every with your friends. Join our* [*referral program*](https://every.getrewardful.com/signup)*.*
