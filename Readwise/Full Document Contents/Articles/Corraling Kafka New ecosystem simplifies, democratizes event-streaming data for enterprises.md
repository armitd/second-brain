# Corraling Kafka: New ecosystem simplifies, democratizes event-streaming data for enterprises

![rw-book-cover](https://venturebeat.com/wp-content/uploads/2022/02/GettyImages-1003898550-e1670426859355.jpg?w=1024?w=1200&strip=all)

## Metadata
- Author: [[George Lawton]]
- Full Title: Corraling Kafka: New ecosystem simplifies, democratizes event-streaming data for enterprises
- Category: #articles
- Summary: Join our daily and weekly newsletters for the latest updates and exclusive content on industry-leading AI coverage. Learn More Aiven, a cloud-data platform based in Helsinki, has fleshed out an open-source ecosystem for Apache Kafka, a popular event-streaming platform.
- URL: https://venturebeat.com/data-infrastructure/corraling-kafka-new-ecosystem-simplifies-democratizes-event-streaming-data-for-enterprises/

## Full Document
![Vibrantly colored light trails form a complex conduit filled with streaming data in an image about technology, communications, and the future.](https://venturebeat.com/wp-content/uploads/2022/02/GettyImages-1003898550-e1670426859355.jpg?w=750)Image Credit:  [John Lund](https://www.gettyimages.com/detail/photo/streaming-data-light-trail-royalty-free-image/1003898550?adppopup=true)
*Join our daily and weekly newsletters for the latest updates and exclusive content on industry-leading AI coverage. [Learn More](https://venturebeat.com/newsletters/?utm_source=VBsite&utm_medium=desktopNav)*

[Aiven](https://venturebeat.com/data-infrastructure/aiven-expands-data-warehousing-new-clickhouse-offering/), a cloud-data platform based in Helsinki, has fleshed out an open-source ecosystem for Apache Kafka, a popular [event-streaming](https://venturebeat.com/data-infrastructure/want-a-streaming-database-without-hiring-a-data-engineer-risingwave-raises-36m-bring-it-to-you/) platform. The new offerings promise to help enterprises consolidate their Kafka infrastructure using open-source components.

“Event streaming is transitioning toward the main stack of the IT infrastructure,” Filip Yonov, director of data streaming product management at Aiven, told VentureBeat. “At Aiven, we have witnessed the fastest growth in the event-streaming domain compared to all other products.”

Apache Kafka provides the infrastructure for wiring streams of data together from databases, apps, IoT devices, and third-party sources. Kafka helps organize raw data into event streams that reduce data size and are easier to integrate into event-driven apps and analytics. Enterprises use it to improve customer experiences, build the [industrial metaverse](https://venturebeat.com/2022/03/22/nvidia-gtc-how-to-build-the-industrial-metaverse/) and monitor patients.

However, building out a Kafka infrastructure involves a lot of moving parts. Aiven has consolidated all the necessary tooling into one place to simplify this process. Key new enhancements include support for Apache Flink and [data governance](https://venturebeat.com/data-infrastructure/putting-privacy-first-a-global-approach-to-data-governance/). These complement existing tools for connecting services, replicating data and managing schemas for Kafka deployments.

#### The need for simplicity

LinkedIn originally developed Kafka to integrate data across its large microservices infrastructure and open-sourced it in 2011. Over the intervening years, large enterprises have customized the tooling for their own needs, and several vendors have rolled out proprietary enhancements to fill in gaps around governance and integration. Many organizations use Kafka for various data pipeline scenarios, such as transferring data between applications in real-time or moving data from a database to a data warehouse.

Yonov told VentureBeat that as Kafka clusters become larger and more complex, they require additional tooling and governance to ensure proper operation and management. “Unlike existing Kafka solutions, Aiven’s offering does not require organizations to choose between proprietary tools and vendor lock-in or open-source technologies without support,” he said.

#### Improving the developer experience with event streaming

One essential aspect has been to democratize the experience for working with event-streaming data. The open-source tool, Klaw, provides a self-service interface for managing Kafka clusters. [Kafkawize](https://kafkawize.com/), which develops Klaw, recently joined Aiven’s open-source development office in September to help integrate their tools together. Now they are working together to improve self-service, simplify user management and enforce data governance.

Another significant development was to connect streaming data to SQL queries familiar to data engineers. The new Aiven for Apache Flink tools allows teams to process larger volumes of events and run real-time analytics using SQL. Aiven provides this as a fully managed service that reduces the complexity of deploying a Flink cluster. It also simplifies the integration with Aiven for Apache Kafka to filter, enrich and aggregate events on the fly.

Aiven hopes to replicate the success of other open-source frameworks like PostgreSQL, Kubernetes and Linux, built by a healthy mix of contributions from various communities.

“We truly believe that fostering an open-source, community-driven and inclusive ecosystem of technologies around Apache Kafka can drive further innovations and new developments in the data-streaming domain, ensuring the long sustainment of the technology in the future,” Yonov said.

**VB Daily**

Stay in the know! Get the latest news in your inbox daily

By subscribing, you agree to VentureBeat's [Terms of Service.](https://venturebeat.com/terms-of-service/)

 #### The AI Impact Tour Dates

 Join leaders in enterprise AI for networking, insights, and engaging conversations at the upcoming stops of our AI Impact Tour. See if we're coming to your area!
