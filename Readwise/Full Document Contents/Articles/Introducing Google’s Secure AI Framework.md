# Introducing Google’s Secure AI Framework

![rw-book-cover](https://blog.google/static/blogv2/images/google-1000x1000.png)

## Metadata
- Author: [[Phil Venables]]
- Full Title: Introducing Google’s Secure AI Framework
- Category: #articles
- Summary: Google has introduced the Secure AI Framework (SAIF) to establish security standards for safe AI development and deployment. This framework aims to protect AI systems from various risks, ensuring they are secure-by-default. Google plans to collaborate with industry partners and share insights to promote responsible AI practices.
- URL: https://blog.google/technology/safety-security/introducing-googles-secure-ai-framework/

## Full Document
The potential of AI, especially generative AI, is immense. However, in the pursuit of progress within these new frontiers of innovation, there needs to be clear industry security standards for building and deploying this technology in a responsible manner. That’s why today we are excited to introduce the Secure AI Framework (SAIF), a conceptual framework for secure AI systems.

* For a summary of SAIF, click [here](https://services.google.com/fh/files/blogs/google_secure_ai_framework_summary.pdf).
* For examples of how practitioners can implement SAIF, click [here](https://services.google.com/fh/files/blogs/google_secure_ai_framework_approach.pdf).

#### Why we’re introducing SAIF now

SAIF is inspired by the security best practices — like reviewing, testing and controlling the supply chain — that we’ve applied to software development, while incorporating our understanding of [security mega-trends](https://cloud.google.com/blog/products/identity-security/8-megatrends-drive-cloud-adoption-and-improve-security-for-all) and risks specific to AI systems.

A framework across the public and private sectors is essential for making sure that responsible actors safeguard the technology that supports AI advancements, so that when AI models are implemented, they’re secure-by-default. Today marks an important first step.

Over the years at Google, we’ve embraced an [open](https://blog.google/technology/safety-security/shared-success-in-building-a-safer-open-source-community/) and [collaborative approach](https://www.whitehouse.gov/briefing-room/statements-releases/2021/08/25/fact-sheet-biden-administration-and-private-sector-leaders-announce-ambitious-initiatives-to-bolster-the-nations-cybersecurity/) to cybersecurity. This includes combining frontline intelligence, expertise, and innovation with a commitment to share threat information with others to help respond to — and prevent — cyber attacks. Building on that approach, SAIF is designed to help mitigate risks specific to AI systems like [stealing the model](https://arxiv.org/abs/2004.15015), [data poisoning of the training data](https://arxiv.org/abs/2302.10149), injecting malicious inputs through [prompt injection](https://arxiv.org/abs/2302.12173), and [extracting confidential information](https://arxiv.org/abs/2012.07805) in the training data. As AI capabilities become increasingly integrated into products across the world, adhering to a [bold and responsible](https://www.ft.com/content/8be1a975-e5e0-417d-af51-78af17ef4b79) framework will be even more critical.

And with that, let’s take a look at SAIF and its six core elements:

**1. Expand strong security foundations to the AI ecosystem**

This includes leveraging secure-by-default infrastructure protections and expertise [built over the last two decades](https://services.google.com/fh/files/misc/google-cloud-security-foundations-guide.pdf) to protect AI systems, applications and users. At the same time, develop organizational expertise to keep pace with advances in AI and start to scale and adapt infrastructure protections in the context of AI and evolving threat models. For example, injection techniques like [SQL injection](https://www.techrepublic.com/article/mandiant-malware-proliferating/#:~:text=According%20to%20the%20Mandiant%20report,compared%20to%2012%25%20in%202021.) have existed for some time, and organizations can adapt mitigations, such as input sanitization and limiting, to help better defend against [prompt injection style attacks](https://arxiv.org/abs/2302.12173).

**2. Extend detection and response to bring AI into an organization’s threat universe**

Timeliness is critical in detecting and responding to AI-related cyber incidents, and extending threat intelligence and other capabilities to an organization improves both. For organizations, this includes monitoring inputs and outputs of generative AI systems to detect anomalies and using [threat intelligence](https://cloud.google.com/blog/products/identity-security/rsa-introducing-ai-powered-insights-threat-intelligence) to anticipate attacks. This effort typically requires collaboration with trust and safety, threat intelligence, and counter abuse teams.

**3. Automate defenses to keep pace with existing and new threats**

The latest AI innovations can improve the scale and speed of response efforts to security incidents. Adversaries [will likely use AI to scale their impact](https://www.mandiant.com/resources/podcasts/how-adversaries-are-leveraging-ai), so it is important to [use AI and its current and emerging capabilities](https://cloud.google.com/blog/products/identity-security/rsa-google-cloud-security-ai-workbench-generative-ai) to stay nimble and cost effective in protecting against them.

**4. Harmonize platform level controls to ensure consistent security across the organization**

Consistency across control frameworks can support AI risk mitigation and scale protections across different platforms and tools to ensure that the best protections are available to all AI applications in a scalable and cost efficient manner. At Google, this includes extending secure-by-default protections to AI platforms like [Vertex AI](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-launches-vertex-ai-unified-platform-for-mlops) and [Security AI Workbench](https://cloud.google.com/blog/products/identity-security/rsa-google-cloud-security-ai-workbench-generative-ai), and building controls and protections into the software development lifecycle. Capabilities that address general use cases, like [Perspective API](https://perspectiveapi.com/), can help the entire organization benefit from state of the art protections.

**5. Adapt controls to adjust mitigations and create faster feedback loops for AI deployment**

Constant testing of implementations through continuous learning can ensure detection and protection capabilities address the changing threat environment. This includes techniques like reinforcement learning based on incidents and user feedback and involves steps such as updating training data sets, fine-tuning models to respond strategically to attacks and allowing the software that is used to build models to embed further security in context (e.g. detecting anomalous behavior). Organizations can also conduct regular [red team](https://blog.google/technology/safety-security/meet-the-team-responsible-for-hacking-google/) exercises to improve safety assurance for AI-powered products and capabilities.

**6. Contextualize AI system risks in surrounding business processes**

Lastly, conducting end-to-end risk assessments related to how organizations will deploy AI can help inform decisions. This includes an assessment of the end-to-end business risk, such as data lineage, validation and operational behavior monitoring for certain types of applications. In addition, organizations should construct automated checks to validate AI performance.

#### Why we support a secure AI community for everyone

We’ve long advocated for, and often developed, industry frameworks to raise the security bar and reduce overall risk. We’ve collaborated with others to launch the [Supply-chain Levels for Software Artifacts (SLSA) framework](https://slsa.dev/) to improve software supply chain integrity, and our pioneering work on our [BeyondCorp](https://cloud.google.com/beyondcorp/) access model led to the [zero trust principles](https://cloud.google.com/blog/topics/developers-practitioners/zero-trust-and-beyondcorp-google-cloud) which are industry standard today. What we learned from these and other efforts is that to succeed in the long term, you have to build a community to support and advance the work. That’s why we’re excited to announce the first steps in our journey to build a SAIF community for everyone.

#### How Google is putting SAIF into action

We’re already taking five steps to support and advance a framework that works for all.

1. **Fostering industry support for SAIF** with the announcement of key partners and contributors in the coming months and continued industry engagement to help develop the [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) and [ISO/IEC 42001 AI Management System Standard](https://www.iso.org/standard/81230.html) (the industry's first AI certification standard). These standards rely heavily on the security tenets in the NIST [Cybersecurity Framework](https://www.nist.gov/cyberframework/updating-nist-cybersecurity-framework-journey-csf-20) and [ISO/IEC 27001 Security Management System](https://www.iso.org/standard/27001) — which Google will be participating in to ensure planned updates are applicable to emerging technology like AI — and are consistent with SAIF elements.
2. **Working directly with organizations, including customers and governments** to help them understand how to assess AI security risks and mitigate them. This includes conducting workshops with practitioners and continuing to publish best practices for deploying AI systems securely.
3. **Sharing insights from Google’s leading threat intelligence teams** like [Mandiant](https://www.mandiant.com/) and [TAG](https://blog.google/threat-analysis-group/) on cyber activity involving AI systems. To learn more about some of the ways Google practitioners are leveraging generative AI to identify threats faster, eliminate toil, and better solve for security talent gaps, [see here](https://www.mandiant.com/resources/blog/mandiant-leveraging-ai).
4. **Expanding our bug hunters programs** (including our [Vulnerability Rewards Program](https://bughunters.google.com/about/rules/6625378258649088/google-and-alphabet-vulnerability-reward-program-vrp-rules)) to reward and incentivize research around AI safety and security.
5. **Continuing to deliver secure AI offerings** with [partners like GitLab](https://about.gitlab.com/press/releases/2023-05-02-gitLab-and-google-cloud-partner-to-expand-ai-assisted-capabilities.html) and [Cohesity](https://www.crn.com/news/storage/cohesity-google-cloud-team-up-for-vertex-ai-data-protection), and further develop new capabilities to help customers build secure systems. That includes our [commitment to the open source community](https://blog.google/technology/safety-security/shared-success-in-building-a-safer-open-source-community/) and we will soon publish several open source tools to help put SAIF elements into practice for AI security.

As we advance SAIF, we’ll continue to share research and explore methods that help to utilize AI in a secure way. We’re committed to working with governments, industry and academia to share insights and achieve common goals to ensure that this profoundly helpful technology works for everyone, and that we as a society get it right.
