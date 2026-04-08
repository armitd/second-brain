# 5 Architecture principles for Digital Initiatives

![rw-book-cover](https://media.licdn.com/dms/image/v2/C4D12AQEO0KHcqDTGjA/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1559653513954?e=2147483647&v=beta&t=tfWC2nGWa97bqAqAhLB0fBGdqCfjiq35fsjA7WveR7k)

## Metadata
- Author: [[Kurt Wiener]]
- Full Title: 5 Architecture principles for Digital Initiatives
- Category: #articles
- Summary: Digital initiatives require a shift towards customer-centric services, prioritizing understanding customer needs and delivering tailored experiences. Companies should adapt standardized frameworks like ToGAF to create flexible, agile architectures that support rapid changes and secure designs. Key principles include putting customers first, enabling business architecture, implementing a customer-facing service layer, ensuring security, and leveraging customer insights for better service delivery.
- URL: https://www.linkedin.com/pulse/5-architecture-principles-digital-initiatives-kurt-wiener

## Full Document
![5 Architecture principles for Digital Initiatives ](https://media.licdn.com/dms/image/v2/C4D12AQEO0KHcqDTGjA/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1559653513954?e=2147483647&v=beta&t=tfWC2nGWa97bqAqAhLB0fBGdqCfjiq35fsjA7WveR7k)
#####  Kurt Wiener

######  Strategic Accounts @ Lemongrass | Driving SAP on Cloud Growth

Working in Digital Initiatives requires a shift in mindset of all involved disciplines towards speedy, flexible customer-centric services. In all my projects [ToGAF](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=4&cad=rja&uact=8&ved=2ahUKEwifmu630rHiAhVEqxoKHXXyDwcQFjADegQIAhAB&url=https%3A%2F%2Fde.wikipedia.org%2Fwiki%2FTOGAF&usg=AOvVaw335yXpqNOzJmOuQOkO0WG-) has rather been indoctrinated and applied with standardized Architectural principles. Developing digital customer-centric services needs a different approach towards delivering the best experiences for customers. I am a strong believer of ToGAF, but as all standardized frameworks, ToGAF needs to be adapted to the specific needs of a company in their specific environment.

In context of digitization, it is all about:

* understanding customer and user needs
* flexibility in adapting to customer and consumer needs
* speed in delivering changes by focusing on customer relevant activities

So, the standard Architectural principles are useful in some areas only and rather handicap Digital Transformation Initiatives as they are focused in structuring existing tech landscapes. Based on my personal experience, here my five cents on the 5 essential architectural principles which need to be applied when designing a digital architecture for customer-centric Services:

1. Customer First
2. Business Architecture as Enabler
3. Customer-facing Service Layer
4. Secure by Design
5. Leverage Customer Insights

##### 1. Customer First

In the current [age of experience](https://etailment.de/news/stories/kundenbindung-touchpoints-kundenzufriedenheit-kundenbed%C3%BCrfnisse-22256) customers decide for companies reducing their costs, saving time and delivering the best experiences. Companies need to go the next step in interacting with their customers: from communicating to getting engaged.

“2021, 40% of organizations will use enterprise architects to help ideate new business innovations made possible by [emerging technologies](https://www.gartner.com/smarterwithgartner/5-trends-emerge-in-gartner-hype-cycle-for-emerging-technologies-2018/),” says [Marcus Blosch](https://www.gartner.com/analyst/18482/Marcus-Blosch), Vice President Analyst, Gartner”.

Companies aiming to build valuable services for their customers and consumers, first have to understand what the customers needs are (B2C oder B2B) before they start implementing any kind of digital initiative. Customer Journeys as appropriate medium to map those needs, identify service opportunities and monitor customer behavior are not questioned anymore. In addition, online and multi-channel interfaces need to be personalized, rich, intuitive, responsive, easy to use and visually appealing. A separate look and feel for customers needs must be implemented (UI-Layer), next to data, logic and back-end layers.

##### 2. Business Architecture as Enabler

Once a company or digital initiative understands which business drivers and customer needs are to be implemented, the first layer of an Enterprise Architecture needs to be defined:

The Business Architecture including Business Domains and Business Capabilities (BC). In every project in the past 10 years, I first started creating a Business Capability (BC) Map to help my customers understand which current business capabilities they have in place and which new BC´s are needed (target BC Map). This is the basic for the definition of strategic fields of action to e.g. improve skills, product offerings, services, business models, processes, kpi´s and finally estimate implementation costs around Business Capabilities. A nice workshop exercise to have stakeholders engaged, is to visualize on a BC Map where new BC´s are needed or existing BC´s need to be improved to highlight fields of action. This Strategic fields of action are perfect for prioritizing activities e.g based on BSC KPI´s and can be further utilized for the design of a Strategic Roadmap.

The main objectives of a BC Map are:

1. Bring the business perspective into IT Initiatives
2. Understand impact to existing organization
3. Structure Business and IT using Business Domains
4. Cluster Business Objects and Application Layer accordingly
5. Serve as Map to highlight Strategic Fields of Action and
6. Help designing a Strategic Roadmap

##### 3. Install a customer-facing Service Layer

One of the main obstacles I had in the last years, is that IT departments stick to current tech landscapes and try to implement customer-facing services within their existing legacy systems and computer centres. Mostly ignoring all negative consequences applying like different release cycles, different operating models, security issues, application silos and kingdoms, monolithical applications with complex change processes and so on. The list is long.

A radical cut from how IT systems are operated today is needed. If you really want to get speed in delivering customer-centric services, you need to decouple from your existing legacy systems, or as Forrester calls them: systems of record. Therefore lightweight, loosely coupled, scalable, 24/7, self-contained, standards based and configurable micro-services are needed.

Do not try to “save the world” by resolving data quality issues in existing complex back-end systems. It´s a waste of time. Rather focus on which data is needed to operate customer-facing services and to keep your legacy systems running.

Establishing a service layer between your UI-Layer and your existing back-end systems, since the emergence of SOA (Service Oriented Architecture) in 2001, is not rocket science. Yes, probably you will need redundant data in this service layer as the answering times for a consumer should be below 3 ms. Therefore the “North Star” should be to establish customer facing micro-services acting as Single Source of truth with batch sync to legacy systems. And yes, those Services need to be able to be addressed by any kind of Touchpoint or even other platforms and therefore as well need to be designed as an API. So please do not start your Digital Initiatives with principles like mobile or API first, rather focus on principle 1 and principle 2.

Ideally customer-facing services are deployed in a Cloud Environment. Digital systems are expected to be ubiquitous systems across geographies and locations. Digital systems are also expected to be agile and flexible and available 24/7. Cloud based principles and systems are a pre-requisite for IT automation, infrastructure as code and agile approaches like DevOps. Many cloud providers like [Microsoft](https://www.microsoft.com/de-de/cloud/compliance-und-datenschutz.aspx) invested heavily in fulfilling compliancy according to EU law or [BaFin](https://www.bafin.de/SharedDocs/Veroeffentlichungen/DE/Fachartikel/2018/fa_bj_1804_Cloud_Computing.html) regulations. Cloud based services and deployments enable flexibility, agility, scalability and performance to deliver services. Digital Architects need to enable the organization to react fast:

* Active monitoring: automated systems controlling the whole status health, able to learn and adapt, with ready-made backup plans (datacenter rollover, drop of dynamic transaction,…)
* Predictive maintenance: based on machine learning, being able to monitor trends and act in advance, even with architectural changes
* Apply principle 2: “Business Architecture as enabler” to slice Cloud Services per Business Domain and be able to quickly switch-on or –off when required. Here an [article how this can be done with Microsoft Azure](https://docs.microsoft.com/en-us/azure/architecture/cloud-adoption/appendix/azure-scaffold).

##### 4. Secure by Design

With data and application security becoming more and more a critical factor, security needs to be part of any digital architecture upfront and constructed end-to-end. This includes security considerations across multiple dimensions like authentication, multi-factor, key management, SSO, authorization, auditing, logging, and encryption of data in transit and data at rest.

A lacking confidence in security is one of the main blocking criteria why consumers are not willing to store private information. [Here one of many articles you can find on the web supporting this topic.](https://www.information-age.com/customers-lack-trust-personal-data-123471751/)

##### 5. Leverage Customer Insights

As soon as the different layers of an Enterprise Architecture are designed, analytics needs to be thought of as a fundamental functionality on all levels. In Digital Initiatives it is not about feeding tons of data into a big Data Warehouse dump. Digital workers need consumer data instantly to be able to provide personalized, regional services, campaigns, targeting based on consumer data, behavior and preferences. Therefore Digital Initiatives need to focus on collecting relevant customer data and therefore require a data framework orchestrating data channels over all touchpoints. This has an ever bigger significance in the age of AI where e.g. bots are utilized to automatically suggest the next best guess.

Customer insights are the key to earn more money and supporting Principle 1: "Customer First". The more you know about your customer and his preferences and needs, the better companies can provide customer-specific services and improve the brands relationship towards a customer. This will pay-out in increased revenue and customer loyalty.
