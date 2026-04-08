# How CIOs Can Avoid Making The Wrong Data Decisions

![rw-book-cover](https://imageio.forbes.com/specials-images/imageserve/6031fbc53da5640cc0fbebac/0x0.jpg?format=jpg&width=1200)

## Metadata
- Author: [[Bruno Aziza]]
- Full Title: How CIOs Can Avoid Making The Wrong Data Decisions
- Category: #articles
- Summary: If you’re a CIO looking to make your mark in your company’s digital transformation journey, 2021 could be your year.
- URL: https://www.forbes.com/sites/brunoaziza/2021/02/21/how-cios-can-avoid-making-the-wrong-data-decisions/

## Full Document
If you’re a CIO looking to make your mark in your company’s digital transformation journey, 2021 could be your year.

As a growing number of organizations see that their CIO’s scope can go beyond the safe and sane operation of technical infrastructure, CEOs have started to turn to their “Chief Technologist” for business critical and strategic decisions that directly impact the company’s bottom line.

This trend is bound to increase over the next few years: according to [Gartner, 25% of traditional large-enterprise CIOs will be held accountable for digital business operational results, effectively becoming “COO by proxy” by 2024](https://www.gartner.com/smarterwithgartner/gartner-top-10-strategic-predictions-for-2021-and-beyond/).

CIOs starting on this journey wonder:

1. What must I do to make this transition effective for my company but also for my people?
2. What pitfalls must I consider before I embark on this somewhat uncharted path?

In this post, I look at 3 key considerations: where “data stacks” actually start; which architectural shifts CIOs should pay close attention to and how they can design to be “best-in-class” vs. “better-than-self.”

According to Gartner, 25% of traditional large-enterprise CIOs will be held accountable for digital ... [+]

getty
#### **Modernizing Your “Data Stack”**

When addressing the modernization of their “technical infrastructure,” CIOs ought to first pay attention to the recent changes occurring with the fast growing Data, AI and Analytics workforce.

While it feels that it was just a few years ago that DJ Patil and Tom Davenport declared the “Data Scientist” profession the “sexiest job on earth,” Data Scientists have in fact now been dethroned: [“Artificial Intelligence Specialist” is the #1 & fastest growing job according to LinkedIn's 2020 Emerging Jobs Report](https://business.linkedin.com/content/dam/me/business/en-us/talent-solutions/emerging-jobs-report/Emerging_Jobs_Report_U.S._FINAL.pdf).

This doesn’t mean that Data Scientists have become irrelevant though. They are #3 on the list but their hiring growth pales in comparison to that of the “AI Specialists” (37% vs. 74% over the past 4 years).

**Bottom line:** modernizing your “data stack” starts with your people. Assess current skills & make sure you’re hiring for the future. Do you have a plan to train up your existing workforce to become Data Scientists? How will that differ from maturing them to “AI Specialists?”

##### Hint: An [**Artificial Intelligence Specialist stands to make about 40% more than Data Scientists**](https://www.linkedin.com/pulse/dig-deeper-15-jobs-rise-andrew-seaman/): check out this [**LinkedIn interactive tool**](https://www.linkedin.com/pulse/dig-deeper-15-jobs-rise-andrew-seaman/) to learn about skills, degrees and salary expectations before you publish your internal curriculum and job descriptions.

Is your head spinning yet?! With so much advice and best practices, what is a CIO to do? 

getty
#### **Tech-tonic Architectural Shifts**

Over the last decade, the Data, AI and Analytics landscape has gone through a massive transformation: from the rise and fall of Hadoop to the rush to the cloud as the main engine for innovation.

Just a few months ago, Gartner predicted that Cloud would be “a given” and that, [by 2022, public cloud services will be essential for 90% of data and analytics innovation](https://www.gartner.com/smarterwithgartner/gartner-top-10-trends-in-data-and-analytics-for-2020/).

McKinsey warns that, to [become a data-driven organization, you must modernize the IT estate with a cloud data warehouse, an open data lake and a real-time analytics platform](https://www.mckinsey.com/business-functions/mckinsey-digital/our-insights/tech-forward/modernizing-the-it-estate-to-become-a-data-driven-organization).

The Boston Consulting Group suggests you [retool your approach to build Data and Digital Platform](https://www.bcg.com/publications/2020/how-to-successfully-accelerate-digital-transformation) (a.k.a. DDP) and anchor it around tenants that might appear new and radical for your organization:

* The separation of data from core transactional systems
* The creation of modular interfaces between systems via APIs, and
* The delivery of data as a service to an omni channel smart business layer

Finally, Venture Capital firm Andreessen Horowitz calls for a [“Unified Data Infrastructure Architecture”](https://a16z.com/2020/10/15/the-emerging-architectures-for-modern-data-infrastructure/) to accommodate the industry’s latest architectural shifts.

Is your head spinning yet?! With so much advice and best practices, what is a CIO to do? My suggestion is this: focus on the reasons why any of these changes matter to your people and your company’s business outcomes. Let’s look at the recent top 3 data architectural shifts and approach them from that perspective:

1. **The Cloud Data Warehouse:** there used to be a time when IT departments embarked on multi-year journeys to centralize all of their company’s data into one place they called the data warehouse. The idea behind that vision was that IT would maintain one version of the truth (or “data”) and serve it to their company’s business departments. That data would be sanitized, maintained and secured. Along the way, the industry discovered many issues with the implementation of that vision: moving data was harder and costlier than anticipated, and scaling IT services to business demands was more challenging than predicted. The cost of storing, securing and maintaining data on-premises led IT departments to limit the amount of data that was stored in the data warehouse—a decision counterproductive to their initial goal. The reason why the Cloud Data Warehouse concept is booming is because it allows companies to provision resources never available to them previously a lot faster, at a much cheaper cost and in a self-service mode. Furthermore, as data sources that feed into the data warehouse have become more disparate than ever, enterprises need an agile system that can pull data between on-premises systems, SaaS applications and third-party sources in batch and real-time mode. In business terms, the reasons why the Cloud Data Warehouse should make sense for your organization is because it allows you to provide a cost-effective, secure and agile way to let your people gain access to the information they need, at the speed they need, to make the right decisions.
2. **From ETL To ELT:** you’ll hear these terms thrown around quite a bit so it’s important you define what makes sense for your teams and their needs. In the olden days, the majority of companies “believed” in ***E****xtracting* data from source systems, ***T****ransforming* it (think “Preparing”) before ***L***oading it into target datastores (a process known as ETL). Note the quotes on the term “believed.” One of the reasons for this process choice was data storage cost: ETL allowed teams to reduce the amount of data loaded in the data warehouse. But it came with major disadvantages: the teams in charge of the “T” would have to make decisions about how much data would need to be brought over and what shape this data would take. Imagine what could happen by the time it got into the hands of end-users: teams might decide they needed different types, shapes or data volumes. The solution to that problem was to go back to the “E” team, often a technical team far far away from the consumers of data, causing tremendous loss in the company's ability to accomplish their business goals in a timely manner. E**L**T changes this process by suggesting your teams should extract as much data as possible first, load it for analysts and scientists to work with, and then transform it as the last mile before analysis. Again, the cloud data warehouse economics make this option a lot more affordable. But, before considering this option, you should make sure your teams have or can gain the skills required to work with this new process. E**L**T has major advantages. For instance, if you believe that more data is better (I do!), you'll want to make sure, the first step of your extraction process doesn’t limit the ability of your business users to access as much data as possible.
3. **Composable and Intelligent Applications:** with the rise of the low-code/no-code movement and the need for more data-rich applications, your people will require more agile and flexible ways to get their needs met. This means that you should embrace the growth of composable applications as part of your ecosystem, as long as you can secure access to the data from which they source. The composable and intelligent applications movement is [one of the 2 trends CIOs can’t afford to miss](https://www.forbes.com/sites/brunoaziza/2020/12/13/2-trends-you-cant-afford-to-miss-in-2021/?sh=a80e5492adb4) in my opinion: in its [2021 “Business at Work” report](https://www.okta.com/businesses-at-work/2021/), Okta found that the [average organization has 88 applications](https://chiefmartec.com/2021/01/stacks-expanding-yes-best-breed-yes/), with some industries like technology or media featuring sometimes twice as many (155 and 133 respectively).

Average Number of Applications per Customer, by Industry

chiefmartec.com
#### **“Best-In-Class” vs. “Better-Than-Self”**

While many of the blueprints available today will help CIOs get a start, in 2021, CIOs have the opportunity to make their mark by asking their team to think about what it takes to become the standard everyone will look up to.

The leaders I’ve had the opportunity to work with are not optimizing to be “better than they were last year.” They’re modernizing to be “best-in-class in industry.”

The technology choices are plentiful but focus on the few, most meaningful “Tech-tonic Architectural Shifts” and align your team’s capabilities to them.

To avoid making the wrong data decisions, don’t just start with technology, start with your people.
