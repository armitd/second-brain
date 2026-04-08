# Let’s Architect! Designing architectures for multi-tenancy

![rw-book-cover](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2022/01/18/Site-Merch_Lets-Architect_REVIEW.jpg)

## Metadata
- Author: [[07 JUN 2023]]
- Full Title: Let’s Architect! Designing architectures for multi-tenancy
- Category: #articles
- Summary: Understanding architectural patterns for multi-tenancy is essential for architects and developers looking to create scalable, secure, and cost-effective solutions, particularly in SaaS environments. The document delves into various aspects of multi-tenant architectures, including SaaS microservices, serverless solutions, and EKS, providing insights into practical patterns for simplifying development processes. It also explores techniques and strategies that can impact the success of SaaS businesses, offering valuable information on optimizing multi-tenant SaaS architecture. The document emphasizes the importance of tenant data isolation and covers different storage models for multi-tenancy, detailing trade-offs and implementation strategies for each model.
- URL: https://aws.amazon.com/blogs/architecture/lets-architect-multi-tenant-saas-architectures/

## Full Document
Understanding architectural patterns for multi-tenancy has become crucial for architects and developers aiming to deliver scalable, secure, and cost-effective solutions. Isolating tenant data is a fundamental responsibility for Software as a Service (SaaS) providers. In this edition of *Let’s Architect!*, we talk about comprehensive exploration of multi-tenant architectures, covering various aspects, such as SaaS microservices, SaaS serverless, SaaS EKS, and an insightful whitepaper.

In this session, Michael Beardsley, Principal Solutions Architect at AWS, takes a deep dive into the realm of multi-tenant microservices, exploring various patterns and strategies that enable the seamless implementation of multi-tenant microservices, all while ensuring that additional complexity is not imposed upon the SaaS builders. He shares practical patterns to simplify the development process by addressing crucial aspect, such as authorization, data access, tenant isolation, metrics, billing, logging, and a plethora of other considerations; this is irrespective of the chosen compute platform (like [Amazon Elastic Container Service](https://aws.amazon.com/ecs/), [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) [Amazon EKS], or [AWS Lambda](https://aws.amazon.com/lambda/)) or database solution.

There is another session available that highlights specific techniques and architecture strategies that can directly impact the success of a SaaS business. If you’re interested in learning more about [optimizing multi-tenant SaaS architecture](https://www.youtube.com/watch?v=oMo8DVwGSXY), this session is a great opportunity.

[*Take me to this video!*](https://www.youtube.com/watch?v=oMo8DVwGSXY)

[![SaaS multi-tenant microservices](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2023/06/06/SaaS-multi-tenant-microservices.png)](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2023/06/06/SaaS-multi-tenant-microservices.png)
SaaS multi-tenant microservices

In this [AWS Partner Network (APN) Blog](https://aws.amazon.com/blogs/apn/) post, you will explore a reference solution that presents a comprehensive perspective on a functional multi-tenant serverless SaaS environment. This solution effectively showcases various essential components required to construct a multi-tenant SaaS solution using serverless services, including onboarding processes, tenant isolation mechanisms, data partitioning techniques, a tenant deployment pipeline, and robust observability measures.

By delving into these aspects, you can gain valuable insights into the architecture and design considerations involved in creating a successful multi-tenant SaaS solution.

[*Take me to this AWS APN blogpost!*](https://aws.amazon.com/blogs/apn/building-a-multi-tenant-saas-solution-using-aws-serverless-services/)

[![Tenant registration flow](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2023/06/06/Tenant-registration-flow.png)](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2023/06/06/Tenant-registration-flow.png)
Tenant registration flow

In this re:Invent 2021 presentation, Tod Golding, Principal Partner Solutions Architect, chats about a SaaS reference solution that addresses fundamental multi-tenant considerations, examining its approach to core SaaS topics, including tenant isolation, identity, onboarding, tenant administration, and data partitioning. The goal is to explore an Amazon EKS SaaS architecture through the lens of working code and highlight the key architectural strategies that were used in this reference environment.

There is also valuable information available on [Github](https://aws.github.io/aws-eks-best-practices/security/docs/multitenancy/) regarding EKS multi-tenancy. Exploring the Github repositories related to EKS multi-tenancy can provide further insights, resources, and practical examples for implementing multi-tenant architectures on EKS. This presentation is an engaging way to dive deeper into this topic and gain a more comprehensive understanding of best practices and real-world implementations.

[*Take me to this video!*](https://www.youtube.com/watch?v=tXVLjWjEEwo)

[![Tenant deployment model](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2023/06/06/Tenant-deployment-model.png)](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2023/06/06/Tenant-deployment-model.png)
Tenant deployment model

Storage represents a challenging aspect of building and delivering multi-tenant software solutions. There are different strategies that can be used to partition tenant data, each with a unique set of trade-offs for implementing separation between tenants. This whitepaper covers different storage models for multi-tenancy; in particular, you can learn about the:

* **Silo model** (data from the tenant is fully isolated)
* **Pool model** (all the tenants use the same database and table)
* **Bridge model** (single database but a different table for each tenant)

For each of these models, the whitepaper describes in detail how they can be implemented, as well as the different trade-offs in terms of isolation and agility. You can also discover how these tenancy models can be implemented specifically on databases, such as [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Relational Database Service](https://aws.amazon.com/rds/), thus covering both NoSQL and SQL scenarios.

[*Take me to this whitepaper!*](https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/finding-the-right-fit.html)

[![Partitioning model tradeoffs](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2023/06/06/Partitioning-model-tradeoffs-1024x534.png)](https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2023/06/06/Partitioning-model-tradeoffs.png)
Partitioning model tradeoffs

#### See you next time!

Thanks for joining our conversation on multi-tenant SaaS architectures! Next time, we’ll talk about open-source technologies.

To find all the blogs from this series, you can check out the[*Let’s Architect!*](https://aws.amazon.com/blogs/architecture/tag/lets-architect/) list of content on the [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/).
