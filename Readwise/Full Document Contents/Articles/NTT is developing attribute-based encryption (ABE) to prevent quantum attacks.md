# NTT is developing attribute-based encryption (ABE) to prevent quantum attacks

![rw-book-cover](https://venturebeat.com/wp-content/uploads/2022/01/GettyImages-1195673151-e1643167574400.jpg?w=1024?w=1200&strip=all)

## Metadata
- Author: [[Kolawole Samuel Adebayo]]
- Full Title: NTT is developing attribute-based encryption (ABE) to prevent quantum attacks
- Category: #articles
- Summary: NTT is developing attribute-based encryption (ABE) to guard data against quantum attacks. ABE lets owners set fine-grained access to sensitive data in data lakes and smart-city systems. NTT is testing post-quantum ABE with prototypes, a UTS pilot, and ongoing research before commercial rollout.
- URL: https://venturebeat.com/security/ntt-is-developing-attribute-based-encryption-abe-to-prevent-quantum-attacks/

## Full Document
![Concept of quantum computing with high speed binary numbers code.](https://venturebeat.com/wp-content/uploads/2022/01/GettyImages-1195673151-e1643167574400.jpg?w=750)Image Credit: Getty Images
*Join our daily and weekly newsletters for the latest updates and exclusive content on industry-leading AI coverage. [Learn More](https://venturebeat.com/newsletters/?utm_source=VBsite&utm_medium=desktopNav)*

Accelerated by COVID-19, the [digital economy](https://venturebeat.com/datadecisionmakers/how-digital-experiences-are-fueling-the-new-digital-economy/) is booming in incredible ways: more organizations are embracing digital transformation, migrating workloads to the cloud, exploring artificial intelligence (AI)-powered solutions for real-time business insights, and much more.

But there’s bad news, too: a soaring increase in the number of touchpoints across mobile and web interfaces has broadened the [attack surface](https://venturebeat.com/security/how-external-attack-surface-management-lets-you-see-your-org-through-an-attackers-eyes/), causing a sharp rise in data breaches that threaten both businesses and individuals. At the current rate of growth, damage from cyberattacks will amount to about $10.5 trillion annually by 2025 — a 300% increase from 2015 — according to [estimates by Cybersecurity Ventures](https://cybersecurityventures.com/cybercrime-damage-costs-10-trillion-by-2025/).

But enterprises are now rising up to fight in the never-sleeping, always-on cybersecurity war zone with new technologies like [confidential computing](https://venturebeat.com/security/confidential-computing-provides-revolutionary-data-encryption-uc-berkeley-professor-says/) and [quantum computing](https://venturebeat.com/ai/quantum-computing-faces-the-ghosts-of-its-past-present-and-future/). While quantum computing will unlock powerful analytic and AI-processing capabilities, it also opens the door to serious security vulnerabilities, due to the ability of these super-computers to [decrypt public-key algorithms](https://venturebeat.com/security/quantum-risk-cryptography/) in the very near future. This would give cybercriminals and nation-states the ability to openly decrypt information protected by public-key algorithms — not just in the future, but also retrospectively — by collecting encrypted data today to decrypt when quantum computers finally reach maturity.

Although [researchers](https://www.mckinsey.com/business-functions/mckinsey-digital/our-insights/when-and-how-to-prepare-for-post-quantum-cryptography) estimate quantum computers could do that as soon as 2030, with the Biden administration’s [CHIPS and Science Act](https://science.house.gov/chipsandscienceact) being approved — and setting aside $52 billion in subsidies to support semiconductor manufacturers, as well as $200 billion to aid research in AI, robotics and quantum computing — this development could happen even sooner.

While the cybersecurity dynamics point to significant potentials in an evolving market, the risks will be increasingly heightened in a post-quantum world. Currently-available commercial solutions do not fully meet customer demands for automation, pricing, services and other capabilities — which is why [NTT](https://services.global.ntt/), a global telecommunications and IT service and consulting company headquartered in Tokyo, is now pushing for the commercialization of attribute-based encryption (ABE).

#### Quantum computing’s full potential hasn’t been explored yet

ABE was introduced in a [2005 paper](https://ntt-research.com/ntt-research-distinguished-scientist-brent-waters-ucla-professor-amit-sahai-win-iacr-test-of-time-award/) co-authored by NTT Research’s cryptography and information security (CIS) lab director, Brent Waters, Ph.D., and is now approaching commercialization, according to a blog post published today by NTT.

On the heels of this development, NTT is currently conducting a proof-of-concept (POC) information-sharing platform using ABE with the University of Technology, Sydney (UTS). “As part of a broader technology [partnership with UTS](https://group.ntt/en/newsrelease/2021/11/30/211130a.html), this initial platform will focus on internal UTS applications,” NTT noted in its official statement.

“Compared to the prevailing coarse-grained access model of public-key encryption, where giving out a secret key essentially amounts to giving access to all the encrypted data, ABE is a more finely tuned approach that grants prescribed access of encrypted data to someone with a set of matching traits. The checking of those attributes happens mathematically, ‘inside the crypto,’ which shifts attention away from servers or software engineering towards policies and the encryption itself,” NTT further stated.

In addition to exploring the commercialization of ABE, NTT Research has also begun primary research into post-quantum ABE schemes. To show the growing maturity of this encryption scheme, NTT Research recently held a 14-day ABE hackathon, where five NTT global teams gathered in Sunnyvale, California, to build potential implementations of the technology.

During the just-concluded [NTT R&D Forum](https://www.rd.ntt/e/forum/2022/index.html), Waters noted that there is a fundamental difference between what quantum computers can potentially do and what quantum computers can do at the moment.

#### Use cases for attribute-based encryption

There are several real-life use cases for ABE in the business world and across the board, but especially in addressing the challenge of [data lakes](https://venturebeat.com/2022/03/10/what-is-a-data-lake-definition-benefits-architecture-and-best-practices/). Many companies today are swimming in large volumes of data lakes, so much that they find it difficult to effectively categorize their data. Apart from the huge difficulties with deriving accurate analytics from their datasets, another problem persists: much of the data is highly sensitive — like salary data in HR records and customer information. But ABE offers a solution in such scenarios by enabling companies to make data available to employees who need access to it, while protecting such sensitive information.

“We can control access rights at the data layer,” said Kei Karasawa, Ph.D., NTT research vice president of strategy, who added that the same process could be used in protecting smart city applications. “Governments may collect all kinds of information to fuel smart city applications — including transportation and supply chain data, images of peoples’ faces and more. That kind of information should be protected at the data layer,” he noted.

#### On the road to commercializing attribute-based encryption

NTT has continuously worked on the ABE model for a while. A relatively recent [paper](https://eprint.iacr.org/2020/1386) on ABE — which shows the first collusion-resistant, post-quantum, decentralized, multi-authority (MA-ABE) scheme — was co-authored by Waters and CIS lab scientists Pratish Datta and Ilan Komargodski and presented at [EuroCrypt 2021](https://eurocrypt.iacr.org/2021/). “It was proved under the ‘learning with errors (LWE)’ assumption, which has become a pillar in post-quantum security. The scheme also supports access policies captured by disjunctive normal form (DNF) formulas, which are useful in automated theorem proving,” NTT said in its official statement.

So far, NTT’s research team has implemented a prototype of the scheme, but not yet the full MA-ABE. Led by Takashi Goto, the team claims it’s conducting tests for decryption correctness and performance. To be deployed commercially, however, Goto said it would need to undergo further adaptation.“

Although practical [quantum attacks](https://venturebeat.com/security/shield-your-data-from-a-quantum-attack-the-path-to-pqc-migration/amp/) do not constitute an imminent threat, NTT customers can rest assured that some of the world’s top cryptographers are exploring post-quantum ABE solutions and that NTT will provide migration paths down the road,” Goto noted.

**VB Daily**

Stay in the know! Get the latest news in your inbox daily

By subscribing, you agree to VentureBeat's [Terms of Service.](https://venturebeat.com/terms-of-service/)

 #### The AI Impact Tour Dates

 Join leaders in enterprise AI for networking, insights, and engaging conversations at the upcoming stops of our AI Impact Tour. See if we're coming to your area!
