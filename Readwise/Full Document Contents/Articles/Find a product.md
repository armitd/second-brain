# Find a product

![rw-book-cover](https://1.cms.s81c.com/sites/default/files/styles/ibm_cloud_wide_background/public/2020-09-02/SOA-versus-microservices_LS_final.jpg?itok=_12kEClp)

## Metadata
- Author: [[IBM Cloud Team]]
- Full Title: Find a product
- Category: #articles
- Summary: IBM Cloud Pak for Security offers connected security that’s built for a hybrid, multicloud world. Connect apps, services and data with the IBM Cloud Pak for Integration platform, the most comprehensive integration software solution.
- URL: https://www.ibm.com/cloud/blog/soa-vs-microservices

## Full Document
####  In this article, we'll explain the basics of service-oriented architecture (SOA) and microservices, touch on their key differences and look at which approach would be best for your situation.

If you work in IT or the [cloud computing](https://www.ibm.com/cloud/learn/cloud-computing) field, you're probably well aware of the service-oriented architecture (SOA) vs. microservices debate. After all, everyone is talking about microservices and [agile](https://www.ibm.com/cloud/blog/agile-vs-waterfall) applications these days.

At first glance, the two approaches sound very similar, and in some ways, they are. Both involve cloud or [hybrid cloud](https://www.ibm.com/cloud/learn/hybrid-cloud) environments for agile application development and deployment, and both can scale to meet the speed and operational demands of big data. Both break large, complex applications into small, flexible components that are easier to work with. And both differ from a traditional, monolithic architecture in that every service has its own responsibility.

However, even with these key commonalities, a closer examination of the two approaches reveals important differences.

#### What is service-oriented architecture (SOA)?

[Service-oriented architecture (SOA)](https://www.ibm.com/cloud/learn/soa) is an enterprise-wide approach to software development of application components that takes advantage of reusable software components, or services. In SOA software architecture, each service is comprised of the code and data integrations required to execute a specific business function — for example, checking a customer’s credit, signing into a website or processing a mortgage application.

The service interfaces provide loose coupling, which means that they can be called with little or no knowledge of how the integration is implemented underneath. Because of this loose coupling and the way the services are published, development teams can save time by reusing components in other applications across the enterprise. This is both a benefit and a risk. As a result of the shared access to the [enterprise service bus (ESB)](https://www.ibm.com/cloud/learn/esb), if issues arise, it can also affect the other connected services.

XML data is a key ingredient for solutions that are based on SOA architecture. XML-based SOA applications can be used to build web services, for example.

SOA emerged in the late 1990s and represents an important stage in the evolution of application development and integration. Before SOA was an option, connecting a monolithic application to data or functionality in another system required complex point-to-point integration that developers had to recreate for each new development project. Exposing those functions through SOA eliminates the need to recreate the deep integration every time.

**SOA provides four different service types:**

1. **Functional services** (i.e., business services), which are critical for business applications.
2. **Enterprise services**, which serve to implement functionality.
3. **Application services**, which are used to develop and deploy apps.
4. **Infrastructure services**, which are instrumental for backend processes like security and authentication.

**Each service consists of three components:**

1. The **interface**, which defines how a service provider will execute requests from a service consumer.
2. The **contract**, which defines how the service provider and service consumer should interact.
3. The **implementation**, which is the service code.

SOA services can be combined to create higher-level services and applications.

#### What are microservices?

Like SOA, [microservices architectures](https://www.ibm.com/cloud/learn/microservices) are made up of loosely coupled, reusable, and specialized components that often work independently of one another. Microservices also use a high degree of cohesion, otherwise known as bounded context. Bounded context refers to the relationship between a component and its data as a standalone entity or unit with very few dependencies. Rather than being adopted enterprise-wide, microservices typically communicate via application programming interfaces (APIs) to build individual applications that perform a specific business functionality (or functionality for specific areas of the business) in a way that makes them more agile, scalable and resilient. Typically, Java is the programming language of choice to develop Microservices. Other programming languages may also be used, such as Golang and [Python](https://www.ibm.com/cloud/blog/python-vs-r).

Microservices are a true [cloud-native](https://www.ibm.com/cloud/learn/cloud-native) architectural approach, often operating in [containers](https://www.ibm.com/cloud/learn/containers), which make them more scalable and portable for the creation of independent services. Teams can use microservices to update code more easily, use different stacks for different components and scale the components independently of one another, reducing the waste and cost associated with having to scale entire applications because a single feature might be facing too much load. Because of their independence, microservices produce services that are more fault-tolerant than the alternatives.

Check out the following video for more info on microservices architecture:

 
![Video thumbnail for What are Microservices](https://cfvod.kaltura.com/p/1773841/sp/177384100/thumbnail/entry_id/1_7u1clfaw/version/100001/width/651/height/366)
#### The main difference between SOA and microservices: Scope

The main distinction between the two approaches comes down to ***scope***. To put it simply, service-oriented architecture (SOA) has an enterprise scope, while the microservices architecture has an application scope.

![Graphic relating soa to microservices](https://1.cms.s81c.com/sites/default/files/2020-09-02/SOA_microservices%20%281%29.png)
Many of the core principles of each approach become incompatible when you neglect this difference. If you accept the difference in scope, you may quickly realize that the two can potentially complement each other, rather than compete.

Here are a few use cases where this distinction comes into play:

##### Reuse

In SOA, reusability of integrations is the primary goal, and at an enterprise level, striving for some level of reuse is essential. Reusability and component sharing in an SOA architecture increases scalability and efficiency.

In microservices architecture, creating a microservices component that is reused at runtime throughout an application results in dependencies that reduce agility and resilience. Microservices components generally prefer to reuse code by copying and accepting data duplication to help improve decoupling.

##### Synchronous calls

The reusable services in SOA are available across the enterprise using predominantly synchronous protocols like [RESTful APIs](https://www.ibm.com/cloud/learn/rest-apis).

However, *within* a microservice application, synchronous calls introduce real-time dependencies, resulting in a loss of resilience. These dependencies may also cause latency, which impacts performance. Within a microservices application, interaction patterns based on asynchronous communication are preferred, such as event sourcing, in which a publish/subscribe model is used to enable a microservices component to remain up to date on changes happening to the data in another component.

##### Data duplication

A clear aim of providing services in an SOA is for all applications to synchronously obtain and alter data directly at its primary source, which reduces the need to maintain complex data synchronization patterns.

In microservices applications, ideally, each microservice has local access to all the data it needs to ensure its independence from other microservices — and indeed from other applications — even if this means some duplication of data in other systems. Of course, this duplication adds complexity, so it must be balanced against the gains in agility and performance, but this is accepted as a reality of microservices design.

#### Other key differences between SOA and microservices

* **Communication:** In a microservices architecture, each service is developed independently, with its own communication protocol. With SOA, each service must share a common communication mechanism called an enterprise service bus (ESB). SOA manages and coordinates the services it delivers through the ESB. However, the ESB can become a single point of failure for the whole enterprise, and if a single service slows down, the entire system can be affected.
* **Interoperability:** In the interest of keeping things simple, microservices use lightweight messaging protocols like HTTP/REST (Representational State Transfers) and JMS (Java Messaging Service). SOAs are more open to heterogeneous messaging protocols such as SOAP (Simple Object Access Protocol), AMQP (Advanced Messaging Queuing Protocol) and MSMQ (Microsoft Messaging Queuing).
* **Service granularity:** Microservices architectures are made up of highly specialized services, each of which is designed to do one thing very well. The services that make up SOAs, on the other hand, can range from small, specialized services to enterprise-wide services.
* **Speed:** By leveraging the advantages of sharing a common architecture, SOAs simplify development and troubleshooting. However, this also tends to make SOAs operate more slowly than microservices architectures, which minimize sharing in favor of duplication.
* **Governance:** The nature of SOA, involving shared resources, enable the implementation of common data governance standards across all services. The independent nature of microservices does not enable consistent data governance. This provides greater flexibility for each service, which can encourage greater collaboration across the organization.
* **Storage:** SOA and microservices also differ in terms of how storage resources are allocated. SOA architecture typically includes a single data storage layer shared by all services within a given application, whereas microservices will dedicate a server or database for data storage for any service that needs it.

#### Migration from SOA to microservices

For some organizations, SOA architecture is a steppingstone to replace the monolith, providing a more flexible and agile environment. SOA services can be developed and utilized in a large environment, but they do not address specific needs of individual businesses that wish to address business processes within their purview. DevOps can be used to help an organization transition from SOA architecture to microservices to address specific needs.

#### SOA vs. microservices: Which is best for you?

Architectural styles have their advantages, so how can you determine which one will work best for your purposes? In general, it depends on how large and diverse your application environment is.

Both SOA and microservices can use automation to speed up business processes. Larger, more diverse environments tend to lean towards service-oriented architecture (SOA), which supports integration between heterogenous applications and messaging protocols via an enterprise-service bus (ESB). Smaller environments, including web and mobile applications, do not require such a robust communication layer and are easier to develop using a microservices architecture.

#### Learn more about SOA and microservices

Some will point out that the SOA vs. microservices debate is much more complicated, and that’s true. There is a great deal more to it. For a more detailed technical explanation of these nuances, we encourage you to delve into the SOA and microservices Learn Hub articles, which provide a great deal of in-depth information. From a business perspective, however, scope is the crucial distinction.

To learn more about how to build agile applications, download your free copy of the [Agile Applications Architecture ebook](https://www.ibm.com/account/reg/signup?formid=urx-34200).
