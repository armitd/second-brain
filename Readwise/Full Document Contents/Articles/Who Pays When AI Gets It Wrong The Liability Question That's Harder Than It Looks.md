# "Who Pays When AI Gets It Wrong? The Liability Question That's Harder Than It Looks"

![rw-book-cover](https://media.licdn.com/dms/image/v2/D4E12AQEtQ-nagMFDoQ/article-cover_image-shrink_720_1280/B4EZsnb_XnHEAI-/0/1765893212417?e=2147483647&v=beta&t=cEMg_fREldWpWp0Khc2OMRwzcRZ_oHqlmBZAH3UySGQ)

## Metadata
- Author: [[Peter Stansbury]]
- Full Title: "Who Pays When AI Gets It Wrong? The Liability Question That's Harder Than It Looks"
- Category: #articles
- Summary: AI-driven decisions create bigger and murkier liability than many organisations expect. Insurance often doesn't cover AI risks and vendors limit their liability, so the organisation remains legally responsible. Leaders must document, govern, and insure AI use before mistakes reveal costly exposures.
- URL: https://www.linkedin.com/pulse/who-pays-when-ai-gets-wrong-liability-question-thats-harder-peter-m6uee?utm_source=share&utm_medium=member_ios&utm_campaign=share_via

## Full Document
!["Who Pays When AI Gets It Wrong? The Liability Question That's Harder Than It Looks"](https://media.licdn.com/dms/image/v2/D4E12AQEtQ-nagMFDoQ/article-cover_image-shrink_720_1280/B4EZsnb_XnHEAI-/0/1765893212417?e=2147483647&v=beta&t=cEMg_fREldWpWp0Khc2OMRwzcRZ_oHqlmBZAH3UySGQ) 

 

#####  Peter Stansbury

The AI made that decision" isn't a legal defence. But the liability landscape is more complex than most deployment plans account for.

There's a pattern emerging in conversations with leadership teams deploying AI:

The discussion focuses naturally on capability and cost. 

* What can the AI do?
* How much will we save?
* How fast can we deploy?

When liability comes up, the initial response is often: "We've considered that. The vendor has limitations. We have professional indemnity insurance. We're covered."

####  But the full picture is more complex than it first appears.

Many organisations discover they have liability exposure that's broader than they'd initially mapped, insurance coverage that's more limited than they'd assumed, and risk that only becomes fully visible when something goes wrong.

By which point, the options are more limited.

##### The Liability Landscape Is More Complex Than It First Appears

Here's what's straightforward about AI liability at first glance:

Initial assessment: "If the AI makes a bad decision, we'll check the vendor liability clause, rely on our professional indemnity insurance, and ensure the employee who approved it followed reasonable processes."

##### The complexity that emerges:

On vendor liability: Most AI vendor contracts limit liability to the subscription cost. They're typically not liable for decisions made using their tool, similar to how Microsoft isn't liable when you write a defamatory email in Outlook. Worth checking your specific contracts, but this pattern is common.

On insurance coverage: Many traditional PI policies were written before AI-enabled decisions became common. They may exclude or severely limit coverage for AI-related claims. The gap isn't always obvious until you need to make a claim.

On employee responsibility: If an employee is approving 200 AI-generated documents a day instead of 20 human-drafted ones, can they reasonably verify everything? The liability question becomes: who's actually responsible when automation changes what's humanly verifiable?

On process documentation: Demonstrating reasonable care requires documentation: what the AI was asked to do, what parameters it used, who reviewed the output, what checks were performed, why the decision was made. This level of documentation doesn't always exist for AI-assisted decisions.

The legal reality is consistent: Organisations remain liable for decisions, regardless of how much automation was involved.

"The AI did it" doesn't change the liability. It just makes the situation harder to explain.

####  Domain 1: Employment Decisions (Where Exposure Develops Quietly)

One of the most common AI deployments: using AI in recruitment, performance management, or workforce decisions.

##### What's typically deployed:

* AI screens CVs
* AI conducts initial candidate assessments
* AI analyses performance data
* AI recommends redundancy selections
* AI predicts flight risk or promotion readiness

What the intention is: "Making data-driven decisions" and "removing human bias."

What can develop: Discrimination claims that are harder to defend than anticipated.

##### The legal framework (UK):

Under the Equality Act 2010, discrimination based on protected characteristics (age, disability, gender reassignment, marriage/civil partnership, pregnancy/maternity, race, religion/belief, sex, sexual orientation) is unlawful.

##### This applies whether a human or an AI makes the decision.

If your AI rejects candidates because its training data reflected historical bias (fewer women in senior roles, fewer disabled people in physical jobs, age correlations with technology skills), discrimination has occurred.

And "the AI did it" doesn't change the liability.

##### Documented example:

In 2018, Amazon scrapped an AI recruiting tool after discovering it penalised CVs containing the word "women's" (as in "women's chess club"). The AI had learnt from historical hiring data that men were more likely to be hired, so it optimised for male candidates.

Amazon caught this before deployment. The challenge is that these patterns aren't always obvious until they're tested systematically.

##### The liability:

Employment tribunal awards for discrimination typically range from £10,000 to £50,000 per claimant. These can be uncapped for serious cases.

The broader implications include:

* Potential for multiple claims (every rejected candidate in a protected group could have grounds)
* Reputational impact (these cases are public)
* Regulatory investigation (Equality and Human Rights Commission)
* Organisational liability (not limited to the hiring manager)

##### What's emerging:

Employment lawyers are advising clients to request: "Please provide the AI's decision-making criteria and explain why I was rejected." This question can be harder to answer than it first appears.

####  Domain 2: Customer-Facing Decisions (Where Regulators Are Developing Expertise)

The second area of complexity: using AI to make decisions that affect customers.

##### Common deployments:

* AI handles customer complaints
* AI approves/rejects transactions
* AI determines credit decisions
* AI provides product recommendations
* AI triages support requests

##### Example that's becoming visible:

A financial services firm deployed AI to handle complaints. The AI was trained to identify "vexatious complainants" and route them to a simplified process.

The complication: the AI's definition of "vexatious" included anyone who had complained more than three times in 12 months, regardless of whether previous complaints were valid.

Result: customers with legitimate repeated complaints (fraud, service failures, billing errors) were being funnelled into a process designed for time-wasters.

When the Financial Conduct Authority reviewed this during a routine inspection, demonstrating that the AI's decision-making was fair proved challenging. FCA fines can reach £500,000 or more.

##### The legal framework:

Consumer Rights Act 2015: Requires services to be performed with reasonable care and skill. AI-generated advice or decisions must meet this standard.

Financial services regulation: FCA requires firms to treat customers fairly, explain decisions, and have appropriate oversight. "The AI recommended it" doesn't satisfy these requirements.

General product liability: If AI provides advice that causes loss, the organisation can be liable.

##### What's developing:

Regulators are asking more detailed questions during inspections:

* How is AI decision-making overseen?
* Can specific AI decisions be explained?
* How are AI errors identified?
* What controls prevent AI from causing customer harm?

These questions can be harder to answer comprehensively than they first appear, particularly if governance was implemented after deployment rather than before.

####  Domain 3: Professional Advice (Where Claims Can Be Substantial)

The third domain: using AI to generate professional advice (legal, financial, medical, technical).

##### Common applications:

* Law firms use AI to draft contracts and provide legal analysis
* Accountants use AI for tax advice and compliance
* Consultants use AI to generate recommendations
* Financial advisors use AI for investment guidance

##### Scenario (based on patterns that are emerging):

A law firm uses AI to review a commercial contract. The AI misses a critical jurisdiction clause that exposes the client to significant liability in a foreign court.

The client sues for professional negligence. The claim is £2 million.

The firm's position: "Our associate reviewed the AI's output. They're competent but they were reviewing 50 contracts a week instead of 10. They can't reasonably catch everything the AI misses."

The court's likely response: "You're a professional firm. You're liable for the advice you provided. How you produced that advice (human only, AI-assisted, entirely automated) doesn't change your duty of care."

##### The professional indemnity complexity:

Many PI policies were written before AI-assisted work became common. Some contain provisions like:

* Exclusions for automated decision-making systems
* Separate sublimits for algorithmic outputs
* Requirements for specific endorsements for AI-generated advice

What this can mean: A £5 million PI policy might have a £500,000 sublimit for AI claims. Or certain AI applications might not be covered at all.

##### New AI-specific PI insurance is available, but:

* It typically costs £50,000-£150,000 annually for £5 million coverage
* Excess (the amount you pay before insurance responds) can be £100,000+
* Coverage often depends on demonstrating appropriate AI governance
* Claims history is limited, so pricing is uncertain and may increase

##### The liability scale:

Professional negligence claims in legal, financial, and consulting work typically range from £100,000 to £5 million+.

Unlike employment tribunal claims (which have some caps), professional negligence liability can be substantial. A single AI-generated error in a large transaction can create significant exposure.

####  Domain 4: Data Processing (Where Compliance Is Technical)

The fourth domain: how AI accesses, processes, and uses data.

##### Common patterns:

* AI processes personal data to generate insights
* AI accesses customer information to provide recommendations
* AI analyses employee data for workforce decisions
* AI combines data sets to identify patterns

##### The legal framework:

UK GDPR and Data Protection Act 2018 require:

* Lawful basis for processing
* Purpose limitation (only use data for specified purposes)
* Data minimisation (only access what you need)
* Accuracy requirements
* Storage limitations
* Security requirements
* Individual rights (right to explanation, right to object to automated decisions)

##### AI creates specific challenges:

Data minimisation: AI models often require more data than traditional processes. The justification needs to be documented.

Purpose limitation: Training AI on customer data for one purpose, then using it for another, can violate GDPR.

Security considerations: AI models can potentially leak training data. If personal data was in the training set, this creates data protection risk.

Automated decision-making: GDPR Article 22 restricts decisions based solely on automated processing (including profiling) that have legal or similarly significant effects. This requires either explicit consent or legitimate interests with appropriate safeguards.

Explainability: GDPR requires that individuals can understand how automated decisions were made. Providing sufficient explanation can be technically challenging.

##### Example that's becoming visible:

A healthcare provider used AI to predict patient deterioration. The AI was trained on patient data without explicit consent for this specific purpose.

When investigated, demonstrating several things proved challenging:

* Lawful basis for this specific processing
* That patients were informed their data would be used this way
* How the AI's predictions were validated
* What safeguards existed to prevent incorrect predictions causing harm

ICO fines under UK GDPR can reach £17.5 million or 4% of global annual turnover, whichever is higher.

####  The Pattern Across All Four Domains

Here's what's becoming clear:

Organisations are deploying AI to make or assist with consequential decisions (hiring, customer service, professional advice, data processing). The complexity often emerges in:

1. Understanding the full scope of legal liability being created
2. Verifying that insurance coverage actually matches the exposure
3. Implementing governance that would satisfy regulatory scrutiny
4. Documenting decisions in ways that would survive legal challenge
5. Training staff on when and how to override AI recommendations
6. Establishing clear accountability when things go wrong

##### This isn't about malicious intent. It's about capability moving faster than risk infrastructure.

Leadership teams naturally ask: "What can this AI do?" (Capability question)

The question that's often harder to answer comprehensively is: "What liability does this create?" (Risk question)

The result: Organisations have deployed AI, achieved efficiency gains, and built liability exposure that may only become fully visible when something goes wrong.

##### Why "The AI Made That Decision" Doesn't Change Liability

Let me be clear about why this explanation doesn't affect the legal position:

In employment law: Organisations are responsible for hiring decisions. Whether a human reviewed 100 CVs or AI screened 10,000 doesn't change liability under the Equality Act.

In consumer law: Organisations are responsible for the service provided. Whether advice was generated by AI or human doesn't change the duty of care.

In professional services: Firms are liable for negligence. Whether an associate missed something or AI missed something is typically irrelevant to the client's claim.

In data protection: Organisations are the data controller. How data is processed (manually, algorithmically) doesn't change GDPR obligations.

##### The law treats organisational liability as organisational.

Liability can't typically be outsourced to a technology vendor. It can't be delegated to junior staff reviewing AI outputs. It doesn't disappear because a process was automated.

The organisation deployed the AI. The organisation used its outputs. The organisation is responsible for the consequences.

####  What Due Diligence Is Starting to Reveal

This is becoming visible in M&A processes.

Buyers looking at professional services firms, financial services, or any business deploying AI in consequential decisions are asking more detailed questions:

##### About AI deployment:

* What decisions does AI make or assist with?
* What's the governance framework?
* Who can override AI recommendations?
* How are decisions documented?
* What training exists for staff using AI tools?

##### About liability:

* What's the AI liability exposure?
* Can potential claims be quantified?
* What's covered by existing insurance?
* What gaps exist?
* Have there been any claims or near-misses?

##### About regulatory risk:

* How is AI compliance with employment law ensured?
* How are data protection requirements satisfied?
* How would the organisation respond to a regulator asking about AI decisions?
* Can algorithmic fairness be demonstrated?

##### About vendor relationships:

* What liability does the AI vendor accept?
* What happens if the vendor disappears?
* Are there IP rights to the models?
* Can operations continue without the vendor?

The challenge: These questions can be harder to answer comprehensively than they first appear.

And uncertainty creates valuation risk. Buyers adjust valuations for unquantified liability. In recent transactions, AI-related governance gaps are leading to 20-40% valuation adjustments or deal structures with holdbacks until liability frameworks are established.

####  The "We'll Strengthen Governance Later" Challenge

A common response when these issues are raised: "We'll implement more robust governance once we've proven the value."

The complication: Governance is harder to implement retrospectively.

Once AI has already been deployed to make thousands of decisions, certain things can't be retrofitted:

* Documentation for decisions that weren't documented at the time
* Oversight for processes that didn't have it
* Training for staff who weren't trained
* Remediation for discrimination that may have already occurred
* Demonstrating to regulators that appropriate processes were in place

##### Liability claims can arise from decisions made during the "prove the value" phase.

And the explanation "We were moving quickly and planned to implement governance later" doesn't typically constitute a strong defence.

What "Appropriate Governance" Looks Like

So what would satisfy a regulator, insurer, or due diligence process?

##### The key elements typically include:

Documentation:

* What AI systems are deployed and for what purposes
* What decisions they make or assist with
* Who can override AI recommendations and in what circumstances
* How decisions are logged and reviewed
* What the escalation process is when AI produces questionable outputs

Oversight:

* Regular audits of AI decisions (sampling for errors, bias, compliance)
* Human review of high-stakes decisions
* Monitoring of AI accuracy and drift over time
* Process for investigating complaints about AI decisions

Training:

* Staff understand what the AI does and its limitations
* Staff know when to override AI recommendations
* Staff can explain decisions to customers/candidates/regulators
* Staff understand personal and organisational liability

Technical controls:

* Explainability (ability to understand why AI made specific decisions)
* Bias testing (regular checks for discrimination)
* Version control (knowing which AI model made which decisions)
* Data governance (ensuring AI only accesses appropriate data)

Insurance:

* Professional indemnity coverage that explicitly includes AI
* Cyber liability that covers AI-related data breaches
* Employment practices liability that covers AI-enabled discrimination
* Policy limits that match the actual exposure

The gap: Many organisations have some of these elements but not all, or implemented them after deployment rather than before.

####  What This Means for Leadership Teams

If you're deploying or have deployed AI for consequential decisions (employment, customer service, professional advice, data processing), these questions are worth considering:

1. What liability have we actually created?

* Where is AI making or assisting with decisions?
* What could go wrong in each domain?
* What's the potential scale of claims?

2. What does our insurance actually cover?

* Does our PI policy cover AI-related claims?
* What are the sublimits or exclusions?
* Would additional AI-specific coverage be valuable?

3. Can we demonstrate appropriate care?

* Do we have governance documentation?
* Can we explain AI decisions if challenged?
* Do we have adequate audit trails?
* Is staff training sufficient?

4. What would a buyer find in due diligence?

* Could they quantify our AI liability?
* What gaps would they identify?
* How might this affect valuation?

5. What happens when something goes wrong?

* Do we have an incident response process?
* Who's accountable?
* How do we investigate AI errors?
* What's our regulatory notification process?

If these questions are harder to answer than expected, that's useful information.

####  The Trade-Off That's Easy to Underestimate

Here's the tension that's becoming visible:

Deploying AI without comprehensive governance is faster.

You move more quickly. You automate more extensively. You achieve bigger productivity gains. You don't slow down for detailed risk assessment, documentation, oversight, training.

But speed creates liability risk that compounds over time.

Eventually, the AI will make a mistake. It might reject a candidate who should have been hired. It might provide advice that's incorrect. It might make a decision you struggle to explain to a regulator.

And when that happens, the central question will be: Was there appropriate governance?

If the answer is "not yet" or "we were planning to implement it," defending the position becomes significantly harder. The efficiency gains won't offset the liability. The cost savings won't prevent claims. Regulators will ask why consequential AI was deployed without appropriate controls.

The alternative requires more initial investment:

Implement governance before or during deployment. Document decisions properly. Train staff comprehensively. Establish robust oversight. Verify insurance coverage. Move more deliberately.

You'll achieve smaller initial efficiency gains. You'll automate less aggressively. Implementation will take longer.

But when something goes wrong (which becomes increasingly likely over time), you'll be able to demonstrate you acted reasonably.

That's the difference between a defendable position and a difficult situation.

What's Developing

Currently, AI liability is still relatively limited in scope. Large-scale claims haven't materialised yet across most sectors.

But the trajectory is visible:

Employment tribunals are seeing early "AI rejected me" cases. Financial regulators are asking AI governance questions in routine inspections. Professional negligence lawyers are building AI-specific expertise. Data protection authorities are investigating algorithmic decision-making.

The organisations that will navigate this effectively are likely to be those asking comprehensive liability questions now.

Before claims materialise. Before regulatory investigations intensify. Before due diligence processes reveal significant gaps.

The organisations that may struggle are those treating AI purely as a capability question.

They're optimising for efficiency and assuming liability will be manageable.

It may not be as straightforward as it appears.

"The AI made that decision" doesn't change the legal liability.

And discovering that when a claim arrives is significantly harder than addressing it beforehand.

####  How Ocovai Can Help

At Ocovai, we help organisations map AI liability exposure across employment, customer-facing, professional advice, and data processing domains before claims arise. We work with leadership teams to quantify potential liability comprehensively, verify that insurance coverage actually matches exposure, design governance that would satisfy regulators and due diligence, and establish accountability frameworks that can withstand legal scrutiny.

This isn't about slowing AI adoption. It's about understanding that "the AI did it" doesn't change legal liability and that organisations deploying AI without comprehensive governance are building exposure that's often broader than initially mapped and harder to insure than assumed. The most valuable time to address this is before the employment tribunal, before the professional negligence claim, before the regulatory investigation deepens, and before the due diligence process that adjusts valuation by 40% because certain questions prove difficult to answer.

Get in touch if you want to map and address AI liability before it becomes more complex.

#AITransformation #ProfessionalIndemnity #LegalCompliance #AIStrategy #RegulatoryCompliance #DueDiligence
