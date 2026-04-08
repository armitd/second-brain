# Software-defined vehicle Research Report 2021: Architecture Trends and Industry Panorama

![rw-book-cover](https://ml.globenewswire.com/Resource/Download/3e0b82c2-02d7-44c8-b22f-561e0f321f39)

## Metadata
- Author: [[Reportlinker]]
- Full Title: Software-defined vehicle Research Report 2021: Architecture Trends and Industry Panorama
- Category: #articles
- Document Tags: [[automotive]] 
- Summary: Car makers are shifting from hardware sales to software-driven business models that bundle IP, solutions, and services. OEMs are building internal software teams and partner ecosystems to develop operating systems, middleware, and apps for features like HMI and autonomous driving. Over time the industry will decouple hardware and software, concentrate power in a few large software providers, and monetize vehicles through continuous software services.
- URL: https://www.globenewswire.com/news-release/2021/08/11/2278893/0/en/Software-defined-vehicle-Research-Report-2021-Architecture-Trends-and-Industry-Panorama.html

## Full Document
New York, Aug. 11, 2021 (GLOBE NEWSWIRE) -- Reportlinker.com announces the release of the report "Software-defined vehicle Research Report 2021: Architecture Trends and Industry Panorama" - [https://www.reportlinker.com/p06128353/?utm\_source=GNW](https://www.globenewswire.com/Tracker?data=GGOG9VP80qqWHmKzSqFKCDz49pbCOlLkE9DywQhBjA0jMkioj0iKT88PRJ2ecU1lRg295KMK4y3Fbf8bwREC05vUnk9OnT5MOKTfHxcAvVVl3xCHu-l6rjmor0tO16W59bBvhHqs_R2drnhYWgT8pUbDxLPot7xiKuAknoB4WvqbPNsCEVayoksj5k8CdtnK)   

;  

(3) The application middleware and development framework, including functional software, SOA, etc.;  

(4) The application software layer, including smart cockpit HMI, ADAS/AD algorithms, connectivity algorithms, cloud platforms, etc.

**The business model of smart car software is in the form of "IP + solutions + services". Tier 1 software suppliers charge in following modes:** (1) One-time R&D expenses and software packages, such as ADAS/AD algorithm packages; (2) Software licensing fees per car, royalties (by a certain proportion of car shipments and unit price); (3) One-time R&D expenses and license packages per car.

Take the software IP licensing fees as an example. Regardless of the highly complex AD software, we estimate that the software IP licensing fees for a single car is at least RMB2,000-3,000. As the functions of smart cars become more complex, the software IP licensing fees per car will continue to rise.

At the same time, OEMs are also vigorously expanding their internal software R&D teams to reduce the cost of software outsourcing. In the next step, OEMs‘ software R&D will still focus on software that can directly create value for consumers, such as cockpit HMI, autonomous driving, etc. Of course, OEMs can also cooperate with independent software vendors in R&D through the decoupling of software and hardware, like BMW and ArcherMind Technology team up, and ThunderSoft and Human Horizons collaborate. However, for general software (such as surround view splicing, voice, DMS) and common platform-based software (such as OS kernels, virtual machines, HD maps, cloud platforms, etc.), OEMs still give priority to outsourcing.

In general, as software becomes more and more complex, the life cycle value (ASP) of software for a single car may be as high as tens of thousands of yuan, which makes software a main part of the vehicle BOM cost.

With the continuous evolution of software-defined vehicles, the business model of the entire automotive industry has changed accordingly, from new car manufacturing and marketing model which lasts for a long time to a larger-scale software × ownership model. Automakers will charge customers for software license and OTA updates to complete the closed-loop business model.

For example, Tesla has boosted the price of its FSD (Full Self-Driving) Beta launched at the end of 2020 by US$2,000 to US$10,000, and it will further raise the price of the package for L3/L4 autonomous driving to US$14,000. Tesla is trying to offer customers a way to subscribe and pay a monthly fee instead of US$10,000 up-front for their premium driver assistance features in order to expand the potential subscriber base.

On July 16, 2021, Tesla started offering a monthly subscription for its FSD package for US$199 per month in the United States. Tesla owners can cancel their monthly FSD subscription at any time. Customers who previously bought Tesla’s Enhanced Autopilot package (EAP) can subscribe to FSD for a lower price of US$99 a month but may require the HW3.0 upgrade. In other words, only Teslas that have the FSD computer hardware 3.0 (HW3) or above plus either Basic or Enhanced Autopilot configurations are eligible to subscribe to FSD; other owners can purchase a hardware upgrade for US$1,500 to make their vehicles FSD-ready.

Once Tesla fulfills the transformation of its business model, all existing Tesla owners may become subscribers of the FSD package. Assuming 10 million Tesla owners subscribe to the FSD package with a monthly price of US$100, a subscription fee of US$12 billion will be incurred each year and Tesla’s software gross margin will be as high as 70-80%. The software revenue from existing car owners is expected to be very stable and lucrative, posing a solid moat for Tesla.  

A Trilogy of Software-defined Vehicle Transformation of OEMs

**In the short term, the system kernel and middle layer are the key R&D directions. In the long run, SOA will bring about changes in business models. To complete the software-defined vehicle transformation, OEMs must at least achieve:**

1. Vehicle EEA upgrade. The hardware architecture develops from distributed ECU to centralized domains, and further upgrades to centralized + regional controllers. As for the communication architecture, the automotive network backbone is upgraded from LIN/CAN bus to Ethernet;

2. Linux, QNX and other RTOS only provide kernels. On this basis, OEMs realize hardware abstraction, form a middle layer operating system that supports application development, define developer interaction logic, and build application layers, namely the so-called self-developed operating systems of OEMs, similar to Tesla.OS, VW.OS, Daimler MB.OS, BMW-OS and Toyota Arene. At the same time, more and more OEMs have followed suit, such as SAIC Z-One SOA, Lixiang Li-OS and Volvo Cars.OS. The ultimate goal of OEMs is to open up vehicle programming to all enterprises by simplifying the development of vehicle software and increasing the frequency of updates, so as to master the ecological resources of developers;

3. With further making use of the huge number of users to build a developer ecosystem, the profit engine of automakers has transferred from "hardware manufacturing" to "software development". For example, Tesla continues to boost the price of FSD software while continuously reducing the price of vehicle hardware in order to promote the rapid development of the automobile company dominated by software revenue.

In the short term, most OEMs are still in the stage of upgrading their hardware architecture. At present, only Tesla and Volkswagen have completed the development, construction and large-scale applications of customized OS kernels. The decoupling of automotive hardware and software is also in the early stages of development. Now, OEMs have focused on basic software (system kernels, AP Autosar, middle layers, etc.).

From a long-term perspective, SOA (Service-Oriented Architecture) will reconstruct the automotive ecology. The automotive industry is likely to replicate the software model of "basic hardware, middle-level operating systems and upper-level applications" for PCs and smartphones. Meanwhile, smart car middleware giants will emerge. Upper-level APP developers need not pay attention to the underlying hardware architecture, but should focus on application development instead.

By building operating systems and SOA platforms by themselves or with suppliers, automakers have introduced a large number of algorithm suppliers, ecological partners, etc. to form a developer ecosystem. In the future, automakers can provide users with software services covering the full life cycle. Under this background, OEMs have laid out SOA software architecture development. In the next 2-3 years, SOA mass production will reach its peak, and consumers will enjoy richer smart driving experience.

The automotive SOA software platform is similar to Apple iOS and Google Android in the smart phone field. It is not only a generalized software architecture, but also an ecological platform for developers. In the smart phone field, Apple iOS and Google Android basically monopolize developer resources, each of them holds more than 20 million developer resources worldwide. Likewise, the automotive SOA software platform may gradually head toward an oligopolistic market.

At the same time, the powerful ecosystem of Apple and Android developers has become one of the fatal technologies in the context of the Sino-US trade war. Especially after the US government placed Huawei on its Entity List, Google stopped offering Google Mobile Services to Huawei, which affected the operation of Huawei’s mobile phones. In this case, Huawei had to launch HMS services and HarmonyOS. The underlying automotive software platform will also threaten the safety of the industrial strategy, and it has become a national strategy. It is urgent to build a standardized platform for automotive basic software.

Under the guidance of the Ministry of Industry and Information Technology of China, Neusoft Reach and China Association of Automobile Manufacturers have jointly planned and initiated China Automotive Basic Software Ecological Committee (AUTOSEMO). With more than 20 member units, AUTOSEMO will share experience and innovation, build open standardized software architectures, interface specifications and application frameworks, develop China’s automotive basic software industry ecosystem with independent intellectual property rights, as well as promote China’s automotive industry to accelerate the intelligent transformation.

On July 22, 2020, AUTOSEMO was established in Shanghai, with founding members including FAW, SAIC, GAC, NIO, Geely, Great Wall, Changan, Beiqi Foton, Dongfeng, FAW Jiefang, Xpeng, Neusoft Reach, Jingwei Hirain, NASN, VMAX, Horizon Robotics, Zhito, Wanxiang Qianchao, REFIRE and China Automotive Innovation. The first rotating chairman was assumed by Neusoft Reach.

The mission of AUTOSEMO is to forge basic software architecture standards and interface specifications dominated by local enterprises with independent intellectual property rights, share knowledge and achievements, as well as establish an industrial ecology, in response to the development needs of intelligent connected vehicles and autonomous driving technology in the future. Harboring the concept of independence, development, and innovation, it has created an automotive software ecosystem communication platform for the industry. It released the first China Automotive Basic Software Development White Paper 1.0 in November 2020, and the first Automotive SOA Software Architecture Technical Specifications 1.0 in June 2021 to accelerate the development of China’s automobile industry towards intelligence.

For smart cars with new EEA, AP AUTOSAR and middleware OS will be the focus of many Tier1 suppliers

Automakers are committed to defining more unified middleware communications and services to reduce development costs and system complexity. Operating software (OS) and middleware are the underlying software components that promote the separation of software and hardware. Even if automakers choose to develop their own operating systems, they will also rely on standard middleware products provided by suppliers. In particular, the architecture of the basic software platform is extremely important, because it can greatly improve the development efficiency of software for the application layer.

Automotive electronic software standards mainly include AUTOSAR, OSEK/VDX, etc. Among them, AUTOSAR has been developing for more than ten years, and has formed a complex technical system and extensive development ecology, as the mainstream of vehicle control operating systems.

AUTOSAR includes Classic and Adaptive platforms, designed for safety control and autonomous driving respectively. The Classic AUTOSAR platform, based on the OSEK/VDX standard, defines the technical specifications of vehicle control operating systems. With an operating system based on the POSIX standard, the Adaptive AUTOSAR platform can provide standardized platform interfaces and application services for operating systems that support the POSIX standard and diverse applications.

At present, the world-renowned AUTOSAR solution vendors include ETAS (Bosch), EB (Continental), Mentor Graphics (Siemens), Wind River (TPG Capital), and Vector, KPIT (a US-based company began in India as a joint venture) and so on.

In China, overseas suppliers, including EB, ETAS, VECTOR, etc., dominate the development tool chain and basic software under the Classic AUTOSAR standard, followed by domestic suppliers like Neusoft Reach, Huawei, Jingwei Hirain, etc. In terms of Adaptive AUTOSAR, suppliers are still in their infancy. Continental EB cooperates with Volkswagen to apply AP AUTOSAR and SOA platforms to ID series battery-electric vehicles of the Volkswagen MEB platform.

Previously, China’s automotive basic software architecture standards and industrial ecology were relatively backward. Following the trend of automotive intelligent transformation and upgrading, domestic vendors have focused on AP AUTOSAR and launched corresponding middleware and tool chain products to seize market opportunities.

In November 2020, Neusoft Reach fully upgraded NeuSAR, an AUTOSAR-based system platform developed by itself for next-generation automotive communication and computing architectures, to the version 3.0, featuring ASIL-D functional safety, information security function expansion, high-performance SOA protocol stacks, virtual verification solutions, full support for SOA, application dynamic deployment, vehicle-cloud collaboration solutions and the like.

Neusoft Reach’s basic software product NeuSAR builds a horizontal software platform that can realize effective decoupling of software and hardware. It converts the core functions and algorithms of Neusoft Reach’s products into SOA services and provides them to application developers through standardized interfaces so as to support flexible application development modes.

In addition, the vehicle-cloud integrated system built by Neusoft Reach connects the in-vehicle SOA services with the cloud through the vehicle-cloud collaboration middleware, and combines the cloud service platform with big data and CP/SP aggregation capabilities to enable the intelligent application scenarios of vehicle-cloud collaboration vertically.

NeuSAR, developed by Neusoft Reach independently, is compatible with the latest version of the AUTOSAR standard. It not only supports traditional ECU development, but also provides a wealth of basic software, middleware and development tools for software development based on domain controllers and new EEA. NeuSAR is widely used in domain control systems such as autonomous driving, intelligent cockpits, chassis power, and body control under the next-generation architecture.

Strategies of OEMs, traditional Tier1 suppliers, and software vendors to cope with the trend of SOA and layered decoupling

Under the SOA software framework, OEMs, Tier1 suppliers, and other authorized developers will step in the application software development ecology.

**There are three modes for OEMs to transform toward software:**

1. While expanding the internal R&D teams, OEMs establish strategic alliances with software companies. OEMs promote the construction of software ecology, while the Tier1 software suppliers are responsible for execution; for example, GAC R&D Center, Neusoft Reach, ThunderSoft, etc. have erected a joint innovation center;

2. OEMs set up software subsidiaries to lay out full stack technology, gradually conduct independent R&D of software, algorithms, chips and other full technology stacks, bypass the traditional Tier1 suppliers to a certain extent, and co-develop subsystems with the former Tier2 software suppliers; CARIAD (Car.Software), a subsidiary of Volkswagen, SAIC Z-One, and Changan Auto Software Technology Co., Ltd. are the examples herein;

3. OEMs erect software R&D divisions to directly cooperate with core technology vendors by all ways like investment so as to be as independent as possible. They mainly boast in-house R&D capabilities in one or more fields with strategic differences, and outsource some common software. For example, start-ups NIO, Xpeng, etc., which are smaller and more flexible and need not be comprehensive, focus on the development of core application software for smart cockpits and autonomous driving and have formed their own big R&D teams.

In the past automotive supply chain, powerful Tier1 suppliers generally provided software and hardware integrated "black boxes", so it is extremely difficult to decouple software from hardware. However, Tesla has broken through the business model of Tier1 suppliers. In the future, automotive electronics and auto parts will be tagged "white labels" like traditional machinery and body parts in the past. The hardware differentiation is getting smaller and the profits are becoming more and more transparent. It is possible that hardware will be sold to automakers at cost, while software will become the soul of vehicles and the new profit engine for OEMs. The differentiation and profitability of vehicles will shift to technology and related software stacks.

**Under the trend of SOA and hierarchical decoupling, Tier1 suppliers or software suppliers have the following coping strategies:**

1. For traditional Tier1 suppliers, it is a general trend that some system function development rights are taken back by OEMs. Therefore, they need transform and seek new ways urgently to avoid becoming hardware foundries. Traditional Tier1 giants are well aware of the fact that full-stack capabilities of software and hardware are the key to seizing the future overwhelming market share. More and more Tier1 suppliers, represented by Bosch, Huawei, Desay SV, etc., are committed to creating full-stack technical capabilities covering "hardware + underlying software + middleware + application software algorithms + system integration", so that they can not only provide customers with hardware and software separately, but also offer software and hardware integration solutions.

2. While further strengthening the autonomy and independent software development capabilities, OEMs have begun to seek direct cooperation with software suppliers. For example, OEMs will first seek to take back cockpit HMI system functions to themselves, but directly purchase UI/UX design tools, voice recognition modules, sound effect modules, face recognition modules and other application software from software suppliers, thus bypassing traditional Tier1 suppliers to accomplish independent development. For software suppliers, the more software IP portfolios they can provide, the higher the value per car they can secure. At the same time, software suppliers are also seeking to dabble in hardware design and manufacturing (such as domain controllers, TBOX, etc.) controlled by traditional Tier1 suppliers in order to provide diversified solutions.

In general, software-defined vehicles are currently in varying forms. According to the objective development law of the software industry, the software-defined vehicle industry will show several characteristics in the long run as below:

1. The entry barriers of automotive software will continue to elevate, with higher and higher concentration. The development barriers of automotive software will threaten small and medium-sized vendors who may feel difficult to survive. Whoever can achieve rapid iteration and scale effects may thrive and grab a relatively high market share; for example, Kanzi, the UI design software of ThunderSoft, has occupied 80% of the domestic market share.

2. Automotive software will feature capital intensiveness, and needs more and more capital. External financing will be conducted in the hundreds of millions of dollars. In the end, there will be several large software suppliers in each segment of automotive software with the overwhelming market share.  

Read the full report: [https://www.reportlinker.com/p06128353/?utm\_source=GNW](https://www.globenewswire.com/Tracker?data=GGOG9VP80qqWHmKzSqFKCDz49pbCOlLkE9DywQhBjA0jMkioj0iKT88PRJ2ecU1lRg295KMK4y3Fbf8bwREC0yKRU4oAQPhUsd5TMvJ9wsApdvlX1fZh8v_09jIf60K22K1eACS2rusAiGEo__nlPBb5YvhaUVak6SC_RMO-Mpjr_caBEYvvuD2Ca6NWS1Sq)

ReportLinker is an award-winning market research solution. Reportlinker finds and organizes the latest industry data so you get all the market research you need - instantly, in one place.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

##### Contact Data

```
            Clare: clare@reportlinker.com
US: (339)-368-6001
Intl: +1 339-368-6001
            
```

[Contact](https://www.globenewswire.com/news-release/2021/08/11/2278893/0/en/Software-defined-vehicle-Research-Report-2021-Architecture-Trends-and-Industry-Panorama.html#)
