# The software-defined vehicle: The architecture behind the next evolution of the automotive industry

![rw-book-cover](https://assets.ibm.com/is/image/ibm/ibm-8bar-logo-2560x2560?$original$)

## Metadata
- Author: [[ibm.com]]
- Full Title: The software-defined vehicle: The architecture behind the next evolution of the automotive industry
- Category: #articles
- Document Tags: [[automotive]] 
- Summary: This layer includes not only the vehicle but also the telco equipment, roadside units, smart city systems and similar components, as well as various backend systems of the original equipment manufacturers (OEMs).
- URL: https://www.ibm.com/think/insights/the-software-defined-vehicle-the-architecture-behind-the-next-evolution-of-the-automotive-industry

## Full Document
More and more consumers now expect their vehicles to offer an experience no different from that offered by other smart devices. They seek full integration into their digital lives, desiring a vehicle that can manage their operations, add functionality and enable new features primarily or entirely through software.

According to a [GMI report](https://www.gminsights.com/industry-analysis/software-defined-vehicle-market#:~:text=Software%2DDefined%20Vehicle%20Market%20size%20was%20valued%20at%20USD%2035.8,22.1%25%20between%202023%20and%202032) (link resides outside ibm.com), the global software-defined vehicle (SDV) market is expected to achieve a CAGR of 22.1% between 2023 and 2032. This growth is driven by increasing demand for advanced features in vehicles, stringent vehicle safety regulations, increased investments in research and development, and enhanced navigation and connectivity. But what exactly defines a SDV, and what is the architectural foundation behind the car that provides connectivity, automation and personalization?

#### The SDV in a nutshell

In an SDV, the vehicle serves as the technological base for future innovations, acting as a command center for collecting and organizing vast volumes of data, applying AI for insights and automating thoughtful actions. The SDV separates hardware from software, allowing for updates and upgrades, automation or autonomy and constant connectivity. It interacts with its environment, learns and supports service-based business models. Simultaneously, onboard electronics evolve from individual electronic control units to high-performance computers with higher performance and simplified integration.

#### A close-up of the SDV architecture

##### *The infrastructure* *layer*

This layer includes not only the vehicle but also the telco equipment, roadside units, smart city systems and similar components, as well as various backend systems of the original equipment manufacturers (OEMs). These elements are all part of a cyclical process in which vehicle data is used for development, operation and services. Based on insights from this data, new software is delivered to vehicles via over-the-air updates.

##### *The hybrid cloud platform layer*

In the IBM approach, a uniform Linux® and Kubernetes-based platform spans from the vehicle to the edge of the backend system. It’s supported by Red Hat® Enterprise Linux and Red Hat® Openshift®, allowing software to be flexibly distributed in the form of software containers, adhering to the principle of “build once, deploy anywhere.” The software can be developed and tested in the backend before being easily deployed into the vehicle or infrastructure. All of this provides unprecedented flexibility.

Standardization through abstraction of application software in the form of containers leads to better maintainability and portability of software, resulting in improved developer productivity. The hybrid cloud approach is complemented by the IBM Edge Application Manager, enabling OEMs to scale and operate edge solutions autonomously, along with the IBM Embedded Automotive Platform, a Java runtime optimized for in-vehicle use.

##### *The AI and data platform layer*

AI models have long played an important part in vehicle functionalities like ADAS/AD. Some OEMs, such as [Honda](https://www.ibm.com/case-studies/honda-rd-big-data.), use AI for knowledge management to deliver safer and more personalized automobiles. Regarding vehicle operation, AI is currently applied in cybersecurity to analyze incoming security events and incidents, and on the analysis of telematics data to gain insights into driving experiences.

Today, generative AI can greatly enhance SDV development and operation by automatically generating artifacts such as test cases, architecture models and software source code. This requires an AI and data platform like IBM [watsonx](https://www.ibm.com/watsonx)™ to manage various optimized [foundation models](https://www.ibm.com/products/watsonx-ai/foundation-models) for each use case, build custom-specific foundation models based on customer proprietary standards and safeguard engineering data from being incorporated into public open source foundation models that competitors might exploit. Furthermore, technologies like IBM Distributed AI API enable OEMs to optimize the deployment and usage of AI models in edge devices such as vehicles.

##### *The security layer*

OEMs are increasingly adopting a zero-trust framework for cybersecurity to counter external and internal threats across development, in-vehicle operations and enterprise environments. One central element in vehicle security is the Vehicle Security Operation Center, where IBM Security® QRadar® Suite can be used for threat detection and security orchestration, automation and response.

OEMs also need to encrypt messages within a vehicle and all other communications that extend beyond it. This can be achieved through the IBM Enterprise Key Management Foundation. Finally, IBM Security® X-Force® Red provides specific automotive testing offerings.

##### *The AI products layer*

A modern development platform, such as IBM Engineering Lifecycle Management, allows the automotive industry to practice agile software development in a modern CI/CD environment. It provides traceable requirements engineering, model-based system engineering and testing, facilitating collaboration, managing product complexity, applying data-driven insights and ensuring compliance. Furthermore, AI engineering, supported by platforms like watsonx, enables a personalized customer experience. Engineering Data Management solutions help customers in managing the extensive data needed for autonomous driving development, as illustrated in this [Continental](https://www.ibm.com/case-studies/continental-automotive) case study. Intelligent platforms, like IBM Cloud Pak® for Network Automation enable the automation and orchestration of network operations, particularly relevant for Telcos in the infrastructure. On the backend, IBM Connected Vehicle Insight helps manufacturers build their connected vehicle use cases.

Equally important, SDVs require many specialized technologies from different providers which is why ecosystem collaboration plays an important part in the SDV architecture.

Ultimately, every component in the architecture plays a well-defined role in ensuring the best possible experience for vehicle drivers and passengers, solidifying the SDV as the next evolution of the automotive industry.

*Do you plan to attend* [*CES*](https://www.ces.tech/) (link resides outside ibm.com)*, from 9-12 Jan 2024 in Las Vegas? Come by the IBM Meeting Center to learn more about SDV technologies.*

#### Author

###### Hans windpassinger

Principal Client Engagement, Global Manufacturing Industries, IBM Technology
