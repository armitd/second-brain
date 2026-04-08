# What’s Lost When Data Systems Don’t Communicate

![rw-book-cover](https://hbr.org/resources/images/article_assets/2023/10/Oct23_11_6551-000359-1.jpg)

## Metadata
- Author: [[Rohan Narayana Murty,
Sandeep Dadlani,
Rajath B. Das,
Nikhil Mehta]]
- Full Title: What’s Lost When Data Systems Don’t Communicate
- Category: #articles
- Summary: Disconnected data systems can lead to significant inefficiencies and increased costs for companies, known as "disconnection debt." Employees often spend a large portion of their time manually transferring and reconciling data, which hampers productivity and creates risks. To address these issues, organizations need to regularly assess their systems and implement both short-term fixes and long-term strategies for better integration.
- URL: https://hbr.org/2023/10/whats-lost-when-data-systems-dont-communicate

## Full Document
![](https://hbr.org/resources/images/article_assets/2023/10/Oct23_11_6551-000359-1.jpg)
Raimund Koch/Getty Images

Imagine a scenario. Kelly, a dedicated employee in a large hospital network, readied herself for another day of handling upset customers. As a member of the consumer relations team, she addressed escalated calls from patients who had been redirected multiple times. Her challenge for the day involved a potential Alzheimer’s patient seeking a second opinion from a different hospital network. Unfortunately, this patient was informed that Kelly’s network was unable to transmit medical records electronically, and instead may have to undertake a 90-minute trip to collect the records on a CD.

Amid the stress of the call, Kelly identified a synchronization problem within their internal systems as the root cause. She took the initiative, navigating across various systems, including electronic health record systems, archives, health exchanges, and health information service provider systems. Kelly manually resolved the sync issue and ensured the records were sent over, earning the patient’s gratitude. This act of service, particularly meaningful because she herself had ageing parents, brought Kelly immense joy.

Every day, several super-advocates like Kelly work in hospital networks to tackle a multitude of member issues, largely stemming from processes ripe for modernization or disparate systems needing to communicate with each other. Indeed, in every industry, many large corporations have teams like this one, who help bridge outdated, disconnected systems, and databases. Without them, there is no way companies can upgrade their technology without causing disruption to their operations. This scenario, though imagined, is ubiquitous in reality across companies and industries.

The problem is that running a company on disconnected or barely patched together systems affects employees at all levels. In another case, one that is real, a Fortune 500 CFO grappled each quarter with consolidating financial data from over 70 systems across 50 subsidiaries. The team had to meticulously extract, reconcile, integrate, and validate data from these systems, a time-consuming and risky process prone to inaccuracies.

Every quarter the finance team and the IT team debated *the same* issues: *Why do we have a plethora of diverse systems? Why don’t these systems talk to each other? What can we do to eliminate these data silos that create more risk, delays, and effort?* *How can we dismantle these data silos that contribute to risks, delays, and additional effort?*

Like Kelly, the finance and IT teams, and the CFO, most workers are familiar with some version of these frustrations, no matter their job, department, or industry. They spend hours moving data from one system to another, troubleshooting incompatible applications, and often accept this dysfunction as an unavoidable friction in their work. But most companies have no idea how bad the problem is, because they haven’t taken the time to quantify the impact this disconnection has on business outcomes.

To understand what disconnected systems are costing companies — what we call “disconnection debt” — we measured the impact of information silos arising from disconnected systems, on business outcomes in over 100 teams across companies. Here’s what companies need to know about this problem — and how they can fix it.

#### Disconnection Debt: The cost of disconnected systems on business

In an ideal world, all systems in an organization would be integrated with each other in the backend with APIs and seamlessly talk to each other. For users — that is, employees — that would mean eschewing repetitive and manual work in copying or extracting information from multiple sources. Instead, users should ideally use their experience, judgement, and training to make decisions or recommendations based on information provided by the system, which is responsible for doing the tedious work of gathering that information from multiple sources. But this is rarely the case.

Disconnected systems exist because each system is built to meet the organization’s needs at a particular point in time. But over time, as business needs and workflows evolve, there is a gap between how these systems are designed and the evolving business needs. A cloud system, for example, does not talk to a mainframe system. And today’s new system is likely to be tomorrow’s disconnected legacy system. When organizations accept this as an unavoidable problem, they are implicitly accepting long-term costs: inefficiency, errors, delays that customers or end consumers experience, and risks to the business in terms of risks to revenue, impediment to scaling, customer experience, churn, or loss of market share.

To bridge these gaps, all organizations tend to “throw people at the problem”: employees manually extract data from multiple systems, make decisions, and then input data back into the relevant systems. These employees, act as human adhesive between disparate systems, taking on “swivel chair” roles. This, of course, comes with cognitive and productivity costs associated with [toggling between numerous applications](https://hbr.org/2022/08/how-much-time-and-energy-do-we-waste-toggling-between-applications). But that is only one part of the overall cost. Disconnected systems give rise to information silos that impose significant manual effort and excessive delays in execution. Ultimately, these shortcomings highlight the true cost of the disconnected debt: consistent negative impact on organizational outcomes and key performance indicators, therefore exacerbating risk. Organizations pay these costs over long periods of time.

To understand just how much the drag of disconnected systems was costing companies, we studied over 103 teams engaged in over 42 processes, in over 1,000 instances, in 13 key functions across 10 Fortune 500 companies and 8 small and medium-sized businesses. We used a work graph — a digital map of how teams work in organizations — to identify where and how these costs arose, sorting them across cost, customer experience, employee experience, revenue, and risk. The companies we looked at spanned banking, retail, telecom, life science, and consumer goods. To estimate the sole impact of disconnected systems on business outcomes, we left out the toggling tax that teams pay.

We found a high variance in the impact of disconnected systems on business outcomes. In some cases, teams spent up to 60% of their working day on activities arising from such systems — extracting information from multiple systems, entering data into other systems, etc. This inefficient use of effort contributed to “disconnection debt” — costs that organizations pay in terms of poor business outcomes and key performance indicators.

The results we found across functions and teams, and their impact on business outcomes are summarized in the table below.

###### Disconnection Debt

The cost of disconnected systems on businesses.

| Function | Process | Estimated average impact (disconnection debt) of disconnected systems | Business dimension |
| --- | --- | --- | --- |
| Function SUPPLY CHAIN | Process Order management | Estimated average impact (disconnection debt) of disconnected systems Order creation and handling delayed by 11% | Business dimension Revenue |
| Function SUPPLY CHAIN | Process Planning | Estimated average impact (disconnection debt) of disconnected systems All planning exercises delayed by 10%, impacting quarterly revenue | Business dimension Cost |
| Function SUPPLY CHAIN | Process Returns | Estimated average impact (disconnection debt) of disconnected systems Customer returns delayed by 12%–18%, leading to poor customer experience and retention challenges | Business dimension Customer experience |
| Function CUSTOMER SERVICE | Process Billing | Estimated average impact (disconnection debt) of disconnected systems Customer bills processed 7% slower, leading to poor customer retention | Business dimension Customer experience |
| Function CUSTOMER SERVICE | Process Customer onboarding | Estimated average impact (disconnection debt) of disconnected systems Customers onboarded 5% slower, likely leading to lower customer satisfaction (CSAT) scores and lower market share | Business dimension Customer experience |
| Function CUSTOMER SERVICE | Process Order fulfillment | Estimated average impact (disconnection debt) of disconnected systems Customer orders processed 15% slower, likely leading to lower CSAT scores | Business dimension Revenue/customer experience |
| Function CUSTOMER SERVICE | Process Service assurance | Estimated average impact (disconnection debt) of disconnected systems Customers served 34% slower than expected, leading to poor CSAT scores | Business dimension Cost/customer experience |
| Function FINANCE | Process Account receivables | Estimated average impact (disconnection debt) of disconnected systems Lower working capital due to 16% delay in receivables | Business dimension Cost/risk |
| Function FINANCE | Process Account payables | Estimated average impact (disconnection debt) of disconnected systems Vendor payments 20% slower than expected, likely leading to higher vendor churn | Business dimension Cost |
| Function HUMAN RESOURCES | Process Offer letters | New employees received offer letters 8% slower | Business dimension Employee experience |
| Function HUMAN RESOURCES | Process Employee onboarding | Estimated average impact (disconnection debt) of disconnected systems New employees faced 11% longer delays during onboarding | Business dimension Employee experience |
| Function HUMAN RESOURCES | Process Hiring | Estimated average impact (disconnection debt) of disconnected systems Hiring process was 14% slower | Business dimension Cost/employee experience |
| Function HUMAN RESOURCES | Process Training | Estimated average impact (disconnection debt) of disconnected systems Training-related functions operated 8% slower | Business dimension Cost/employee experience |

Regardless of the size of the company, we found that disconnection debt was responsible for slower execution, redundant manual efforts, and more errors. The end impact on business outcomes is likely range of possibilities, including, slower revenue growth, increased costs, more risk, and poorer customer and employee experience.

For example, in the above table, disconnected systems caused a U.S.-based fast-moving consumer goods retailer an additional 10% delay (amounting to a few extra days) when selling $300,000,000 of its products to distribution channels each year. Similarly, over 6,000 new employees joining a F500 life sciences company experienced additional delay of four weeks in completing their onboarding formalities. Finally, in one instance, customers signing up for a new bank account experienced several days of delay in being approved. During this process, because systems in the backend were not well integrated, the organization had repeated back and forth with customers, requesting them to fill in additional forms and details. And slow internal processes that required pulling together data from multiple systems and then stitching them together. Not only did all this result in poor customer experience but also, the management was concerned that they are likely to lose prospective customers to competition, who offered a more streamlined experience for signing up. Other areas of organizations that we have not yet studied will suffer from similar costs of disconnected systems. In the few cases where teams were not suffering from disconnection debt, we found they were either performing all their work within one system or were largely involved in making decisions, based on data from one system.

#### What Leaders Can Do

As business needs evolve, information silos arising from disconnected systems and the risk they pose to business outcomes will continue to be a reality. This issue affects all parts of an organization and creates risk to businesses. Hence, dealing with this issue needs to be on the agenda for all leaders in organizations. CEOs and risk committees on the board must set quarterly targets and metrics to actively track and mitigate risks arising from disconnected systems.

Essentially, organizations need to take a product management lifecycle approach to managing disconnected systems and always stay on top of this problem.

A thumb rule to prioritize which areas to investigate further and improve — teams in critical parts of your business that spend more than 5% of their workday extracting information from at least 2-3 disconnected systems. Hence, to get started, the first priority of leaders ought to be in gaining visibility — finding silos that may be hurting the business and mitigating their impact.

##### 1. Gain visibility into the existence and impact of disconnected systems on business outcomes

##### Find your “Kellys”:

Find colleagues, often on the frontlines, with firsthand insights into customer frustrations caused by disconnected systems. Foster a culture where they can openly share friction points with senior leaders, generating a heatmap of customer challenges. Supplement this with social listening and direct exposure of senior leaders to distressed calls. Some companies have embraced a “[zero distance](https://hbsp.harvard.edu/product/115006-PDF-ENG)” approach, striving to comprehend frontline issues and systematically address them.

##### Create telemetry for your systems and processes:

With today’s tools, you can map and measure system interactions, [creating a “work-graph,” a map of how your teams get work done](https://hbr.org/2021/12/do-you-know-how-your-teams-get-work-done). This helps identify and quantify breakpoints, especially between departments and systems. Consequently, it allows for a prioritized list of the busiest breakpoints in your processes.

A combination of finding “Kellys” and the work-graph gives you a priority list to attack with short-term and long-term fixes. Overlapping breakpoints or friction points highlighted by your “Kellys” and the work-graph measurements yield priorities that you can address with conviction. Make this a weekly discipline in your company. Create metrics and targets out of this visibility that is sent all the way to your board’s risk committees.

##### 2. Short-term fixes to buy time.

There are short-term fixes for these problems, which function more as band-aid solutions that are susceptible to changes in the business including acquisitions, regulatory changes, process changes, etc. But they can ameliorate the situation and buy more time for long-term changes. Solutions include:

* Building single-pane applications: their sole purpose is to gather data from multiple systems and aggregate them into a single view. Hence, users will not spend effort in manually pulling data from multiple systems and instead focus on a [single application window](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-1-7.html).
* Automating tasks: that pull data from multiple systems, pre-populating fields in applications, and writing data back into systems. However, this solution is temporary since it does not fix the underlying problem and may only lead to proliferating more automation solutions on top of disconnected solutions.
* Leverage latest advances in computing: LLMs, among other tools, may be useful in extracting unstructured information from multiple systems, reducing manual effort, and normalizing them into a structured format.

These solutions shift the mechanical manual effort in extracting information from disconnected systems, from humans to software. This approach mitigates the risk of disconnectedness and buys business leaders room to fix the root issue in the underlying problem. For example, an outdated and slow system, despite the automation built on top, still slows down the overall airline booking process and customer experience.

##### 3. Long-term fixes.

Sustainable long-term solutions are expensive and difficult to implement. Typically, they may involve:

* Fundamentally re-engineering systems leveraging newer technology: These initiatives take 18–36 months and usually involve a larger change management effort that requires a lot of discipline.
* Mandate building more APIs and adapters that are faster, more scalable, and secure. As business needs evolve and new workflows are created, these APIs and interfaces will need to be updated.

But these sorts of changes are not discrete events since business needs continue to evolve and hence these newly engineering systems too will soon be out of date. Hence, organizations need a strategy of constantly iterating – gaining visibility into the current impact of disconnected systems on business goals, short-term fixes to buy some time and space, and a long-term deeper fix. And to then iterate again from the beginning.
