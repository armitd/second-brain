# Public Cloud Giants Turn Their Attention To Private Clouds

![rw-book-cover](https://imageio.forbes.com/blogs-images/thumbnails/blog_6091/pt_6091_12_o.jpg?format=jpg&height=900&width=1600&fit=bounds)

## Metadata
- Author: [[Paul Teich]]
- Full Title: Public Cloud Giants Turn Their Attention To Private Clouds
- Category: #articles
- Document Tags: [[ifttt]] [[twitter]] 
- Summary: Major public cloud providers are growing fast and now push private-cloud offerings to capture enterprise workloads. Each company takes a different approach, from turnkey appliances to container or OpenStack-based stacks. The goal is to keep customers tied to their cloud ecosystems during digital transformation.
- URL: https://www.forbes.com/sites/paulteich/2018/08/27/public-cloud-giants-turn-their-attention-to-private-clouds/

## Full Document
Public cloud revenue is up across the big six cloud giants. Alibaba, Amazon, Baidu, Google, Microsoft and Tencent all had solid double-digit to spectacular triple-digit revenue growth from Q2 2017 to Q2 2018. Tencent almost tripled its public cloud revenue year-over-year\*, while [Alibaba](https://www.forbes.com/companies/alibaba/) , [Google](https://www.forbes.com/companies/google/) and [Microsoft](https://www.forbes.com/companies/microsoft/) all roughly doubled their public cloud revenue. [Baidu](https://www.forbes.com/companies/baidu/) reported a 64% increase and [Amazon](https://www.forbes.com/companies/amazon/) was up about 50%. Meanwhile, enterprise stalwart IBM reported its cloud revenue up 18%, with Oracle estimated to be in similar shape. (Huawei doesn’t report its cloud revenues.)

![Ma Huateng, chairman and chief executive officer of Tencent Holdings Ltd. in March 2018. Tencent is... [+] one of the big six cloud giants along with Alibaba, Amazon, Baidu, Google and Microsoft. Photographer: Anthony Kwan/Bloomberg](https://specials-images.forbesimg.com/dam/imageserve/42205353/960x0.jpg?fit=scale)
Ma Huateng, chairman and chief executive officer of Tencent Holdings Ltd. in March 2018. Tencent is... [+] one of the big six cloud giants along with Alibaba, Amazon, Baidu, Google and Microsoft. Photographer: Anthony Kwan/Bloomberg

How can public cloud giants sustain their growth? Part of the answer appears to be hijacking core enterprise applications away from VMware during digital transformation using private cloud offerings. [But the public cloud giants are pursuing wildly different private cloud strategies.](https://twitter.com/intent/tweet?url=http%3A%2F%2Fwww.forbes.com%2Fsites%2Fpaulteich%2F2018%2F08%2F27%2Fpublic-cloud-giants-turn-their-attention-to-private-clouds%2F&text=Public%20cloud%20giants%20are%20pursuing%20private%20cloud%20with%20wildly%20different%20strategies.)

**Private Cloud Strategies & Products**

All the cloud giants except Amazon now have private cloud strategies and products in place:

*Alibaba Cloud Apsara Stack Enterprise* 

Alibaba Cloud introduced Apsara Stack Enterprise V3.0 a few weeks ago (V1.0 shipped in 2015). Alibaba says that Apsara Stack is a “full-stack” on prem private cloud solution for mid- to large-sized businesses. Alibaba says that its Apsara Stack is based on the same underlying proprietary cloud native hyperscale architecture as Alibaba Cloud; it labels Apsara Stack as an “extension” of its public cloud. Alibaba says that Apsara can scale to connect millions of servers. Alibaba initially focused Apsara Stack on IaaS and big data and has recently focused on financial applications. It is not very clear how Alibaba deploys Apsara Stack at customer sites, but it looks like a professional services style engagement with Alibaba.

*Amazon Web Services (AWS)*

AWS suggests assembling a bag of parts (its modus operandi), starting with its Virtual Private Cloud (VPC) service as a base. Then add a Hardware Virtual Private Network (VPN) connection between AWS and a private data center. At this point, AWS suggests combining VPC with VMware Cloud on AWS, which will enable VMware’s vSphere Hypervisor (ESXi), Virtual SAN (vSAN) and its NSX network virtualization platform. You’ll need a cloud services architect and some other talented IT folks to help you assemble the parts and connect it to your existing virtualized on prem infrastructure.

But rolling your own infrastructure to migrate VMs between private and cloud infrastructure really isn’t a modern private cloud, even though the “Virtual Private Cloud” label says the right words.

*Baidu Cloud ABC-STACK*

A large part of Baidu’s most recent earnings call was dedicated to enabling artificial intelligence. Baidu’s hybrid cloud platform is ABC-STACK (AI, Big Data, Cloud Computing), which supports Baidu’s PaddlePaddle and other major AI development frameworks. A rack-sized, all-in-one, 64-GPU “ABC server” is the on prem hardware delivery unit for the private cloud component of ABC-STACK. Up to 1,000 ABC servers can be clustered together. Baidu targets ABC-STACK at large organizations with huge data lakes and matching AI budgets.

*Google Kubernetes Engine (GKE) On-Prem*

Google is also making big bets in AI and in container-based microservices. A few weeks ago, Google announced at its Cloud Next ’18 conference that Google Kubernetes Engine (GKE) On-Prem is in alpha availability, with beta availability coming later this year. GKE On-Prem will be Google’s private cloud software solution. Google promises “a quick and simple install and upgrade experience that’s validated and tested by Google,” but target customers will want to invest in refactoring their applications into containerized microservices. If you are unsure what that means or how much budget that takes, you’ll want to pass on GKE ON-Prem, at least for the next year or two.

*Huawei FusionCloud Private Cloud Solution*

Huawei Cloud is a key public cloud partner of China Telecom, Deutsche Telekom, Orange and Telefonica. It has launched public cloud services for its telecom partners in China, Europe and Latin America. Huawei’s FusionCloud Private Cloud Solution is based on Huawei’s FusionSphere OpenStack distribution using the KVM virtualization engine. Huawei has hardened its commercial OpenStack release for enterprise-grade maintenance, security and reliability. But [OpenStack deployment is still complex](https://www.forbes.com/sites/tiriasresearch/2016/04/25/private-cloud-openstack-coa/).

*IBM Cloud Private*

IBM Cloud Private for data is a Kubernetes-based container platform. It is in the same class as Google’s solution – for customers who make the investment to architect their application using microservices. IBM considers enterprise AI its key competitive advantage and wants to enable analytics and artificial intelligence in a hybrid cloud usage model. IBM says its Cloud Garage Service will help enterprise IT shops modernize development and deployment practices for IBM Cloud Private.

For contrast, IBM Cloud for SAP is intended to do the opposite: migrate local legacy SAP applications into SAP Cloud Platform private edition running on IBM Cloud.

*Microsoft Azure Stack*

Microsoft redesigned its Azure public cloud code to implement its [Azure Stack](https://www.forbes.com/sites/tiriasresearch/2016/10/03/microsoft-azure-stack-moving-on-private-cloud-at-ignite/) private cloud. Azure Stack is a subset of Azure designed to run on the smallest set of hardware – four dual-socket Xeon servers (scaling to fill each rack) plus a fifth management server. Azure and Azure Stack use the same development and management tools for strict consistency across private and public Azure Cloud deployments. Azure Stack is a combined hardware and software solution delivered in half- and full-rack solutions by [several server OEMs](https://azure.microsoft.com/en-us/overview/azure-stack/partners/) (Avanade, Cisco Systems, Dell EMC, Hewlett Packard Enterprise, Huawei, Lenovo and Terra).

Microsoft targets Azure Stack at edge of network and disconnected solutions, as well as cloud applications that meet specific regulatory requirements.

*Oracle Cloud at Customer*

Oracle Cloud at Customer is fully managed by Oracle. Oracle links Oracle Cloud and Oracle Cloud at Customer via SaaS, PaaS and IaaS integration. Oracle Private Cloud Appliance (PCA) is a scalable hardware IaaS platform with two to 25 dual-socket Intel Xeon compute nodes per rack. Oracle is focused on migrating customers’ VMware vSphere virtual machines to its PCA.

Oracle Cloud at Customer appears to be a turnkey VM “lift-and-shift” solution, unlike AWS’s offering, for customers trying to avoid the complexity of assembling a virtualized hybrid environment themselves.

*Tencent Cloud TStack Solution*

Tencent Cloud’s TStack Solution is based on OpenStack. TStack Solution supports the KVM and QEMU hypervisors, VMware’s ESXi bare metal hypervisor and Docker containers. Tencent says that its TStack Solution is a loosely coupled architecture, designed for independent deployment and has integrated cloud management capabilities. Like Huawei, Tencent is trying to simplify OpenStack deployment.

--

*\* Unless noted as reported by the company, revenue growth estimates are based on Canalys Worldwide cloud infrastructure services market Q2 2018.*

--

This topic is explored further in *[Digital Transformation Is A Private Cloud Affair](https://www.forbes.com/sites/paulteich/2018/08/28/digital-transformation-is-a-private-cloud-affair/)*.

This link added on 8/3/2018.

--

*The author and entities with which the author is affiliated may, from time to time, engage in business transactions involving the companies and/or the products mentioned in this post. The author has not made an investment in any company mentioned in this post. The views expressed in this post are solely those of the author and do not represent the views or opinions of any entity with which the author may be affiliated.*
