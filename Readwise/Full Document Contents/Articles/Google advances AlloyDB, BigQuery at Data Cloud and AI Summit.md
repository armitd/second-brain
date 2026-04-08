# Google advances AlloyDB, BigQuery at Data Cloud and AI Summit

![rw-book-cover](https://venturebeat.com/wp-content/uploads/2023/03/data_cloud_ai_summit.max-2500x2500-1.png?w=1200&strip=all)

## Metadata
- Author: [[Sean Michael Kerner]]
- Full Title: Google advances AlloyDB, BigQuery at Data Cloud and AI Summit
- Category: #articles
- Summary: Google announced updates to its data and AI platforms at the virtual Data Cloud and AI Summit, including enhancements to BigQuery and the introduction of AlloyDB Omni. BigQuery Editions will offer users more flexibility and auto-scaling options for managing their data workloads. AlloyDB Omni allows organizations to run a PostgreSQL-based database wherever they choose, reducing concerns about vendor lock-in.
- URL: https://venturebeat.com/ai/google-advances-alloydb-bigquery-at-data-cloud-and-ai-summit/

## Full Document
![](https://venturebeat.com/wp-content/uploads/2023/03/data_cloud_ai_summit.max-2500x2500-1.png?fit=750%2C370&strip=all)
*Join top executives in San Francisco on July 11-12, to hear how leaders are integrating and optimizing AI investments for success*. *[Learn More](https://avolio.swapcard.com/Transform2023/registrations/Start?utm_source=vb&utm_medium=boiler&utm_content=landingpage&utm_campaign=T23_BoilerPlates)*

Google today unleashed a series of updates to its data and AI platforms to help companies more efficiently harness the power of data and drive innovation.

[Subscribe](https://info.venturebeat.com/website-preference-center.html?utm_source=VBsite&utm_medium=adblockCTA)

​​The announcements, made at the virtual [Google Cloud Data and AI Summit](https://cloudonair.withgoogle.com/events/summit-data-cloud-2023), included a new approach to running BigQuery, Google’s serverless data warehouse. The company said that BigQuery Editions would give customers more flexibility to operate and scale their data workloads. Google also unveiled data clean rooms, a service to keep data separate and anonymous.

Internal threats that create external attack opportunities and how to combat them

This is a modal window.

No compatible source was found for this media.

Some content could not be imported from the original document. [View content ↗](https://imasdk.googleapis.com/js/core/bridge3.566.2_en.html#goog_729104076) 

In addition, Google launched AlloyDB Omni, a database service that handles transactions and analytics. First announced in May 2022, [AlloyDB](https://venturebeat.com/data-infrastructure/google-announces-alloydb-a-faster-hosted-version-of-postgresql/) is a managed cloud database that is based on the open source PostgreSQL relational database.

Rather than just being focused on transactional workloads — which is what PostgreSQL supports by default — AlloyDB also has capabilities to support analytics workloads. To date, AlloyDB has only been available as a service running in the Google Cloud. That will change with AlloyDB Omni, which will provide organizations the ability to run the database wherever they want.

##### Event

Transform 2023

Join us in San Francisco on July 11-12, where top executives will share how they have integrated and optimized AI investments for success and avoided common pitfalls.

 [Register Now](https://avolio.swapcard.com/Transform2023/registrations/Start?utm_source=vb&utm_medium=incontent&utm_content=landingpage&utm_campaign=T23_incontent) 

#### New tools driven by customer demand

Rounding out Google’s new product announced is the Looker Modeler service. Looker is a business intelligence (BI) technology that Google acquired for $2.6 billion in 2020. The Modeler service provides a new way for organizations to define and access business metrics.

In a press briefing, Gerrit Kazmaier, Google Cloud GM and VP of data analytics, noted that the new updates are driven by customer requests.

“One was an increased need for flexibility specifically now in the current year with all of its challenges,” said Kazmaier. “They’re asking for help to optimize for both their predictable and unpredictable data needs.”

#### BigQuery gets smart about scaling

Flexibility where users pay for what they use is an original promise of the cloud. It’s a promise that Google is helping to deliver on with the BigQuery Editions update.

Kazmaier said that BigQuery Editions offers multiple tiers of service with different feature set capabilities per tier, that customers can choose and select from. Organizations can also choose to mix and match tiers for individual workloads.

The new flexibility that BigQuery Editions provides is enabled by a few underlying infrastructure capabilities enhancements from Google for storage and auto-scaling. Kazmaier explained that BigQuery compressed storage provides access to data in a highly compressed format using a proprietary multistage compression process. The end result is that organizations will be able to store more data for less cost.

#### New auto-scaling capability

The flexibility provided by BigQuery Editions is also enabled by way of a new auto-scaling capability for workloads. Kazmaier noted that Google built out a new resource scheduler as part of the BigQuery Editions infrastructure for doing query planning and execution. He explained that a query basically can get compute resources on the fly, as it processes operations.

Kazmaier also provided an update on the BigQuery ML service, which first became available in 2019. BigQuery ML integrates the data warehouse with [machine learning](https://venturebeat.com/ai/artificial-intelligence-ai-vs-machine-learning-ml-key-comparisons/) (ML), such that organizations can use the data of AI model development.

Over the last year, Kazmaier said that Google has increased its focus on making machine ML accessible at scale and helping organizations connect it with their own data. A day ahead of the summit on March 28, Google announced an incremental update to BigQuery ML, allowing inference to be done using remotely hosted models, not just models that are directly integrated with the BigQuery service.

#### Google breaks AlloyDB out of its cloud

A cloud database like AlloyDB, by definition, will typically only reside in the cloud, but that’s not always what organizations want or need.

During the press briefing, Andi Gutmans, VP and GM of Databases at Google, commented that many organizations want to run databases in different clouds and some still have a need to run on-premises. There can also be a fear among some users that having a technology only available to run in a single cloud provider can lead to a lock-in risk. The AlloyDB Omni database is an effort to answer that challenge by enabling users to run the database wherever they want.

This isn’t the first time that Google has unshackled one of its data technologies from its own cloud platform. In 2021, Google launched [BigQuery Omni](https://venturebeat.com/business/google-debuts-new-data-powered-cloud-analytics-products/), which enables data queries to be run across multiple cloud providers. While BigQuery Omni enables multi-cloud support, the AlloyDB Omni is going a little further, by allowing users to download a full container image of the database. The container can be run in any environment that will support containers, whether that’s on-premises or another cloud provider.

The idea of removing the fear of lock-in also extends to Google’s views on the open source foundation of AlloyDB Omni, which is the PostgreSQL database.

“We want customers to be able to run on any PostgreSQL, whether that is AlloyDB or without us,” said Gutmans. “With any work that we do, including differentiated work, our goal is to really make sure that there is compatibility out there.”
