# Why your organization needs a software bill of materials

![rw-book-cover](https://venturebeat.com/wp-content/uploads/2022/01/GettyImages-1146418045.jpg?w=1024?w=1200&strip=all)

## Metadata
- Author: [[Bren Briggs]]
- Full Title: Why your organization needs a software bill of materials
- Category: #articles
- Summary: Join our daily and weekly newsletters for the latest updates and exclusive content on industry-leading AI coverage. Learn More The recent Log4j vulnerability has exposed systemic problems in how businesses, and the community at large, audit their software.
- URL: https://venturebeat.com/business/why-your-organization-needs-a-software-bill-of-materials/

## Full Document
![](https://venturebeat.com/wp-content/uploads/2022/01/GettyImages-1146418045.jpg?w=750)Image Credit: metamorworks/Getty Images
*Join our daily and weekly newsletters for the latest updates and exclusive content on industry-leading AI coverage. [Learn More](https://venturebeat.com/newsletters/?utm_source=VBsite&utm_medium=desktopNav)*

The recent [Log4j vulnerability](https://blogs.apache.org/foundation/entry/apache-log4j-cves) has exposed systemic problems in how businesses, and the community at large, audit their software.

Early indications show the Log4j vulnerability was [being weaponized](https://venturebeat.com/2021/12/20/log4j-vulnerabilities-malware-strains-multiply-major-attack-disclosed/) and exploited [days before the news broke about its existence](https://twitter.com/eastdakota/status/1469800951351427073?s=21). Organizations needed to take action immediately to find all instances of the vulnerability in linked libraries, but most had no clear overview of where such instances existed in their systems. Google’s [own research](https://security.googleblog.com/2021/12/understanding-impact-of-apache-log4j.html) showed that more than 8% of all packages on Maven Central have a vulnerable version of Log4j in their dependencies, but of that group only a fifth declared it directly. This means that around 28,000 packages on Maven Central are affected by these bugs while never directly declaring or using Log4j.

Finding all instances of vulnerable dependencies and confirming patch levels can be a daunting task, even for software you completely control and develop in house. Identifying it in your vendors can be even more difficult. Oftentimes, these vendors have just as murky an idea of their own dependencies.

Like any other IT assets such as servers, laptops, or installed applications, having an accurate inventory of your software and dependencies (both direct and transitive) is an essential, and arguably the most fundamental, security control you can apply. Businesses cannot secure what they are not aware of. How do companies begin to take control of the growing complexity of dependencies? By auditing and automating dependency graphs, beginning with direct dependencies and expanding to the transitive ones, often referred to as a [software bill of materials](https://venturebeat.com/2021/09/09/spdx-is-now-official-data-standard-for-software-bill-of-materials/) (SBOM).

While there is nuance to the discussion about what an SBOM should be and contain, for the purposes of this article, we will simply refer informally to an SBOM as a manifest of all components and libraries packaged with an application, along with their licenses. This includes tools and linked libraries. If you are delivering a Docker image, it should also include the list of all installed packages.

#### Getting serious about your software supply chain

Unfortunately, the ecosystem for generating these maps of dependencies often suffers from a lack of sufficient tooling. While the tools available for analyzing dependencies for vulnerabilities are rapidly evolving and improving, the domain is still in its relative infancy. Snyk, Anchore, and other tools provide amazing visibility into your application’s dependencies, but few languages provide native tooling to generate comprehensive visual maps. As an example, let’s look at an older language (Java) and a newer language (Go) that has had the benefit of time and experience to develop a modern package ecosystem.

In Java, developers may use tools like [jdeps](https://wiki.openjdk.java.net/display/JDK8/Java+Dependency+Analysis+Tool) (introduced in JDK 8) or [Maven Dependency Analyzer](https://maven.apache.org/plugins/maven-dependency-plugin/index.html), while Golang, despite its modernity, struggled early on to work out its own dependency management story and instead allowed tools like [Dep](https://github.com/golang/dep) (deprecated and archived) to fill in the gaps before ultimately settling on its [own module system](https://go.dev/ref/mod). In both cases, direct dependencies are usually easy to enumerate, but a full and comprehensive list of direct and transitive dependencies can be challenging to generate without additional tooling.

For open source maintainers, Google has started a very useful project called [Open Source Insights](https://deps.dev/) for auditing projects hosted on NPM, PyPI, or Github, or similar locations. There is already a significant amount of work and research being applied in this area, but it is clear that more needs to be done.

While it is critical that applications themselves are audited for dependencies and vulnerabilities, that is only the beginning of the story. Just as an asset inventory or vulnerability report can only tell you what exists, an SBOM is only a manifest of packages and dependencies. These dependencies must be audited for their relative health beyond what vulnerabilities might be flagged. For instance, a dependency might not meet the [qualifications](https://cve.mitre.org/compatible/guidelines.html) to be reported to National Institute of Standards and Technology (NIST) and may not have a Common Vulnerabilities Exposure (CVE) assigned for whatever reason, be it an issue with [abandonware](https://en.wikipedia.org/wiki/Abandonware) or a fully internal product that is relatively unscrutinized. Other reasons it may not be reported include ownership or maintenance of the library having transferred to a bad actor, bad actors intentionally modifying releases, outdated and vulnerable packages in the Docker container running the app, and/or hosts running old kernels with known, critical CVEs.

Security leaders in the organization are responsible for studying and thinking deeply about software supply chain issues that could affect their products or business, and this all starts by gathering an accurate inventory of the dependencies in the SBOM.

#### Generating an SBOM

Generating an SBOM can be a technical challenge in its own right, but remember that organizations are made of people and processes. Understanding and evangelizing the need for such work is of critical importance to get buy-in. As mentioned above, security leaders in organizations should start by building an inventory of all their in-house software, containers, and third-party vendor packages or applications. Once the first level of inventory is complete, the next step is to determine direct dependencies and finally transitive dependencies. This process should look and feel very similar to any other detection process, such as event logging or asset inventory.

When evangelizing an SBOM to your organization, consider the following benefits:

1. A complete, up-to-date, and accurate inventory of your software dependencies dramatically reduces time to remediation when vulnerabilities in packages such as Log4j are discovered.
2. A manifest generated during the CI/CD process also provides instantaneous feedback about new dependencies and can prevent new, vulnerable components from being included in your software by enforcing policies at build time.
3. It is often said that what is measured improves. Keeping tabs on your dependencies encourages hygiene by stripping unnecessary dependencies and removing old ones.
4. It encourages uniformity in software versioning, saving both time and money for engineering and security teams.
5. Per the White House, it will soon become a [compliance requirement](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/) for many organizations.

As the complexity of our software stacks continues to increase and supply chains become increasingly tempting and viable targets for attackers, techniques and tools such as dependency management and SBOMs must become essential parts of our overall security strategy. And security leaders carry the responsibility of communicating these benefits of these tools to their organizations.

*Bren Briggs is VP of DevOps and Cybersecurity at [Hypergiant](https://hypergiant.com/).*

**VB Daily**

Stay in the know! Get the latest news in your inbox daily

By subscribing, you agree to VentureBeat's [Terms of Service.](https://venturebeat.com/terms-of-service/)
