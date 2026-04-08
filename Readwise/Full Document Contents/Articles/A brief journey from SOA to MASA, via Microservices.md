# A brief journey from SOA to MASA, via Microservices

![rw-book-cover](https://media.licdn.com/dms/image/v2/C4D12AQFyGttGRkfo9A/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1599947256006?e=2147483647&v=beta&t=k3gwFTxC3z0io7CqTlBqz-PYXUKxmo2tkifKiQ1_UEI)

## Metadata
- Author: [[Chris Wild]]
- Full Title: A brief journey from SOA to MASA, via Microservices
- Category: #articles
- Summary: MASA (Mesh Applications and Service Architecture) is gaining traction as a ‘the way to do integration these days’, but what is it? How is it different to SOA, and why would MASA succeed when many SOA implementations failed? The content below is entirely a reflection of my own views.
- URL: https://www.linkedin.com/pulse/brief-journey-from-soa-masa-via-microservices-chris-wild

## Full Document
![A brief journey from SOA to MASA, via Microservices](https://media.licdn.com/dms/image/v2/C4D12AQFyGttGRkfo9A/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1599947256006?e=2147483647&v=beta&t=k3gwFTxC3z0io7CqTlBqz-PYXUKxmo2tkifKiQ1_UEI)
#####  Chris Wild

######  Experienced Enterprise / Digital Architect, Architecture Practice Lead and Consultant | CCSP

MASA (Mesh Applications and Service Architecture) is gaining traction as a ‘the way to do integration these days’, but what is it? How is it different to SOA, and why would MASA succeed when many SOA implementations failed?

***The content below is entirely a reflection of my own views.***

#### A brief intro to SOA

When it arrived on the scene, SOA was touted as the solution to all integration problems, and before talking about Microservices and MASA I think it’s important to reflect on what SOA was meant to be. Here is a definition from IBM:

*“SOA, or service-oriented architecture, defines a way to make software components reusable via service interfaces. These interfaces utilize common communication standards in such a way that they can be rapidly incorporated into new applications without having to perform deep integration each time. Each service in a SOA embodies the code and data integrations required to execute a complete, discrete business function (e.g., checking a customer’s credit, calculating a monthly loan payment, or processing a mortgage application). The service interfaces provide loose coupling, meaning they can be called with little or no knowledge of how the integration is implemented underneath. The services are exposed using standard network protocols”*

SOA was intended to be about creating reusable software components, with well defined, published interfaces that you can interact with using common communication standards, so that you can compose them into new applications easily. SOA Services were meant to be highly cohesive: “Doing one thing and one thing well” and were loosely coupled.

What I find interesting is that if you replace the term ‘SOA’ with ‘Microservice Architecture’ in the above paragraph, the definition still applies. If SOA was intended to solve the same problems that Microservices are intended to solve, why did many SOA implementations fail, and why should we expect Microservice implementations to be any different?

#### Why did SOA fail?

In my opinion, SOA failed for four reasons:

· Monolithic SOA platforms

· Centres of Excellence

· Canonical Data Models

· No / inadequate developer portals

When SOA was brand new, all of the large vendors were heavily involved in the creation of Enterprise Service Bus platforms as the runtime engines for SOA. These platforms were expensive, heavyweight, and difficult to work with (and I’m saying this as someone who was fully certified in one of the major platforms). This meant that when organisations deployed their ESB, they almost always built a ‘Centre of Excellence’ around the technology stack: - a team of highly skilled people who understood the technology and how to design, deploy and operate SOA services.

Because the skillset was niche, these ‘Centres of Excellence’ were almost always centrally located and operated on a factory model. – If you wanted to create a SOA service you had to make a request to the SOA CoE, if you wanted to change a service, you needed to make a request to the SOA CoE... This invariably led to the SOA CoE becoming a bottleneck in any IT project, and the promise of SOA delivering agility evaporated.

This evaporation of agility was compounded by what at the time was a common best practice:- Defining an organisation-wide canonical data model that was used by the ESB, and transforming data into and out of the canonical model as necessary. Having an organisation-wide data model sounded like nirvana at the time, but the reality of the situation was that it meant that any SOA initiative first had to go through a ‘big up front’ data design.

The final nail in SOA’s coffin was (in my opinion) the lack of good developer portals. In an ideal world if a developer needed to call a service they should have been able to easily identify what services were available within the organisation, and how to interact with these services, via a developer portal. The SOA Spec even had specific standards to facilitate this (UDDI / Universal Description Discovery and Integration). In reality, vendors often sold their developer portals as additional products that were poorly thought out and difficult to cost-justify. The result of this was that instead of having a fully functional portal, most developers ended up browsing the service catalogue in Excel, or at best a Wiki. This meant that it was often easier to request / build a new service than to figure out how to reuse an existing one.

So instead of being an integration capability that was agile and easy to use, most SOA implementations ended up being a major bottleneck in any IT delivery.

#### If SOA failed, what’s different about Microservices?

It’s just as easy to create a failed microservice implementation as it was to create a failed SOA implementation, if you make the same mistakes:

· If you are building a central ‘Centre of Excellence’ where Microservices are designed, built and operated, and your plan is to run this as a factory model where projects deliver requirements to the CoE, your initiative is going to fail because you just introduced a bottleneck.

· If you decide you need an organisational wide ‘microservice data model’ you are going to fail because you now need to do ‘big up-front design’

· If you build and deploy microservices without considering how developers are going to find and use those services, you are going to fail because your developers are going to build new services instead of reusing existing ones

Microservices however do have huge advantages over traditional SOA, if they are used correctly.

Firstly, microservices do not rely on monolithic ESB platforms. They are meant to be extremely lightweight: easy to build, deploy and use. This means that it is much easier to embed Microservice delivery capabilities within your development teams. An organisational model that really works here is hub and spoke: Have a small, centralised team responsible for best practice, standards, guidelines, HowTos etc. but federate the delivery and operation of services into teams aligned with business units: - (Check out [Conway’s law](https://www.thoughtworks.com/insights/articles/demystifying-conways-law) and the [Inverse Conway manoeuvre](https://nordicapis.com/conways-law-what-does-it-mean-for-your-api-strategy/) for the reasoning behind why this is so important)

Secondly, thinking around data modelling has evolved since SOA Canonical models were fashionable. Modern best practice is to think of your data around [bounded contexts](https://martinfowler.com/bliki/BoundedContext.html): Create agreed models of your data, but model it within specific domains.

Even if you nail your organisational design so that you have microservice delivery teams acting autonomously and closely aligned with business units designing data models around bounded contexts, you still need to worry about maximising reuse if you are going to truly unlock the potential of Microservices. Adopting an API-led design paradigm using something like [OpenAPI](https://www.openapis.org/) will help hugely, as will investing in a modern developer portal where the API specs are published to.

#### What does MASA have to do with any of this?

MASA is an architecture model first defined by Gartner in 2016 that reflects ‘common best practice’ for Microservice implementations. In a MASA implementation, an application is made up of a network of independent and autonomous services that communicate with each other in a ‘mesh’. In Gartner’s words:

***“Evolving business needs require an application architecture that enables agility, flexibility, integration and innovation. MASA — a mesh architecture of apps, APIs and services — provides application technical professionals delivering applications with the optimal architecture to meet those needs”*** 

Typical MASA implementations are built on Kubernetes to enable rapid deployment and autoscaling of service instances and use service mesh implementations that adhere to the Service Mesh Interface (SMI) Specification. The mesh consists of three key components, **sidecar proxies**, a **control plane** and a **data plane**.

The control plane manages configuration changes across the mesh. When a developer wishes to change a configuration, they update the control plane, and the control plane is responsible for pushing these config changes out to all of the services within the mesh.

The data plane consists of sidecar proxies that are deployed along with every service instance. Capabilities that each service needs are placed in the sidecar and deployed whenever the service is deployed. A key feature of a MASA mesh is that these proxies are configured automatically by the control plane.

An SMI compliant MASA gives you three key capabilities ‘out of the box’

1. **Traffic Policies:** The ability to automatically secure communication channels, manage timeouts and retries, apply security policies, create circuit breakers etc.
2. **Traffic Telemetry:** The ability to capture key service metrics such as health checks and usage metrics (e.g. latency, success rate, failure count)
3. **Traffic Management:** The ability to configure mesh-wide routing rules, supporting canary releases etc.

There are however limitations. The SMI specification only defines synchronous communication across the control and data plane, so if you are looking to implement an architecture where services communicate asynchronously via messaging or events, you are going to need to do some work (There are common patterns for this)

#### So is MASA the answer to the integration problem?

It depends. In my experience, Integration projects do not typically fail because of the technology choice or architecture style, they fail for the following reasons:

1. Organisational structures do not support streamlined delivery (use the inverse Conway manoeuvre)

2. The governance model is wrong (either too much and too centralised, or not enough)

3. The delivery methodology gets in the way (You need to be agile, but you need people who really understand agile, not people who think that agile means no project management)

***If you have fixed these three key issues and you are starting an API initiative, you should definitely think about using MASA.***
