# How Intel is securing patient data through its pandemic response initiative

![rw-book-cover](https://venturebeat.com/wp-content/uploads/2021/09/GettyImages-1208499003-e1631641886627.jpg?w=1024?w=1200&strip=all)

## Metadata
- Author: [[Peter Wayner]]
- Full Title: How Intel is securing patient data through its pandemic response initiative
- Category: #articles
- Summary: Intel launched a $50 million Pandemic Response Technology Initiative to protect patient data using secure hardware and blockchain.  
Projects include privacy-preserving clinical trial matching and contact tracing built on Intel SGX trusted enclaves.  
The goal is to let organizations analyze distributed health data without exposing sensitive records or algorithm IP.
- URL: https://venturebeat.com/business/how-intel-is-securing-patient-data-through-its-pandemic-response-initiative/

## Full Document
![An Intel logo seen displayed on a smartphone.](https://venturebeat.com/wp-content/uploads/2021/09/GettyImages-1208499003-e1631641886627.jpg?w=750)An Intel logo on a smartphone. Image Credit: Mateusz Slodkowski/SOPA Images/LightRocket via Getty Images
*Join our daily and weekly newsletters for the latest updates and exclusive content on industry-leading AI coverage. [Learn More](https://venturebeat.com/newsletters/?utm_source=VBsite&utm_medium=desktopNav)*

Health care data is some of the most sensitive and heavily regulated information around. But fighting diseases, especially the current COVID-19 pandemic, requires being able to gather data quickly and analyze it thoroughly. So when Intel started looking for alignment in its work with blockchain technology and secure computing, it created the [Pandemic Response Technology Initiative](https://www.intel.com/content/www/us/en/corporate-responsibility/covid-19-response.html) (PRTI), a $50 million effort to fight the disease with the best the chip manufacturer can offer.

The PRTI began about a year ago, and Intel has attracted more than 200 projects that build upon the chipmaker’s secure technology. The projects themselves have been startlingly diverse and ranged from hardware to software. One was directed at bringing education online. Another helped turn regular hospital beds in Houston into virtual ICU stations. The Dyson company, famous for building vacuums, flipped the model around to create ventilators driven by Intel’s FPGA arrays.

That was last year. Now the latest projects are turning into products. In August, [Intel and ConsenSys Health announced](https://www.intc.com/news-events/press-releases/detail/1489/intel-consensys-health-advance-pandemic-research) that they were working together, with ConsenSys releasing a privacy-preserving [blockchain](https://venturebeat.com/2021/02/04/the-blockchain-based-virtual-world-that-can-help-usher-in-the-metaverse/) for simplifying the way medical trial researchers find test subjects. The tool allows people to volunteer to test new drugs and procedures without circulating their medical history widely. Patient matching can be more done more effectively and without leaking personal medical data.

Another firm, Leidos, is using the same foundations to work with the Centers for Disease Control and Prevention (CDC) on a [contact-tracing app](https://venturebeat.com/2020/04/13/what-privacy-preserving-coronavirus-tracing-apps-need-to-succeed/). If someone contracts COVID-19 (or another disease), they can connect with the people in their recent past and warn them.

One of the foundations for this is the improved hardware security, a.k.a. Intel Software Guard Extensions (Intel SGX), that’s now found on the latest 3rd Gen Intel Xeon Scalable platform. The platform expands what work can be done in this trusted corner because it offers more protected memory.

We sat down with Chris Gough, Intel’s GM of health and life sciences, to discuss how the technology is shifting the way people work with sensitive data.

*This interview has been edited for clarity and brevity.*

**VentureBeat: Tell me how the pandemic is connected to secure computing and the guts of the Intel processors?**

**Chris Gough:** Confidential computing is a really important focus, a big focus area for Intel. It’s in the class of privacy-preserving technology or privacy-preserving capabilities. Health care is, of course, really important, especially now. And it’s a regulated industry. There’s a need to protect personal information or personal health information, as it’s used.

But most importantly, in my view, there’s a lot of need and use cases in health care where data is distributed or data is federated across multiple different organizations. If you look at the contract tracing case, there’s lots of health care provider organizations, there’s the government organization, and there are the individual citizens. How can you access and analyze that data that’s distributed all over the place and still protect the security and privacy of the data itself?

**VentureBeat: There are some mathematical techniques that can be limited. How can you use hardware built into Intel chips?**

**Gough:** When you’re moving the compute to be near the data in a pretty protective environment, called a trusted execution environment, this is really the foundation of confidence. These trusted execution environments are a segment of memory completely enforced by the underlying hardware of our latest CPU. Only approved datasets and only approved applications can run inside that environment or enclave. The application developer or algorithm developer never sees the raw data, and the owner or steward of that raw data never sees the algorithm or application. Only the derived results are sent back.

**VentureBeat: This is a natural fit for the health care world, right?**

**Gough:** There’s a lot of use cases in both the health care provider side, as well as the regulatory side and really throughout the life sciences, where these organizations want to operate on these combined datasets that are very personal. A lot of those use cases or applications never get off the ground because of all the governance and regulatory issues with keeping the data protected. It’s hard to be comfortable letting others access it while still meeting those requirements.

**VentureBeat: But the pandemic is forcing people and companies to be more agile. They’re using technology to find ways around the roadblocks. That’s what brought Leidos together with the PRTI, right?**

**Gough:** We worked with Leidos on a couple of different projects. Both were blockchain-based, and this particular one is part of the Microbe Trace project, which was part of our Pandemic Response Technology Initiative.

This blockchain platform basically was intended to be a really flexible platform for contact tracing — both at the regional and state level, with abilities for sharing the data across geographic boundaries. And also all the way up to the national level to try and make it easier to coordinate when an outbreak happens and make sure that the important information can cross jurisdictional boundaries. It is based on our secure compute technology at the core of the Xeon scalable platform.

**VentureBeat: So the personal information is protected, but just enough information is available to track down an outbreak. You’re also announcing how ConsenSys is using the secure foundations to help find and match people during drug development. You need to comb through the medical records of many potential test subjects, but that means getting access to [those records].**

**Gough:** The ConsenSys project for the clinical trial matching does use the Intel SGX capability. It was released as a production capability in our previous processors, but the size of the enclave we supported increased dramatically with this latest generation. For these kinds of Big Data or AI or analysis use cases that are very data-hungry, they need that larger and larger memory size.

**VentureBeat: This could be a big cost-saver for the drug industry, right?**

**Gough:** Many, many clinical trials don’t meet their enrollment deadlines, or timelines. A third of the time is spent in patient recruitment, and it’s expensive. The industry spends billions on this. So by using this platform, they will have a central place where companies that are pulling together clinical trials or are looking or wanting to enroll patients can submit some data. Then the patients can submit their data and get matched up using AI-based algorithmic methods. There need to be assurances that the privacy of the data is maintained.

**VentureBeat: I’m just reminded of [Seymour Cray](https://en.wikipedia.org/wiki/Seymour_Cray), who didn’t put in a cache when he was designing the Cray because the datasets were so large.** 

**Gough:** Yes, exactly. With our latest CPU generation, we can support up to 1 terabyte-sized enclaves. I’m sure there’s use cases that need more than that, but so far, I haven’t encountered any that wanted it yet. The datasets are growing bigger and bigger, and the need to analyze them is growing.

**VentureBeat: Some of the new projects in the PRTI are using blockchains. When I think of some of the most public examples, like Bitcoin, the identities may be kept secret through encryption, but the main details of the transactions are very public. How are you balancing that with these medical use cases?**

**Gough:** The SGX capability can supplement a lot of blockchain, but it’s not integrated directly into them. The metadata in most of these health care use cases is stored on-chain, but some of the big data analysis happens off-chain. If you look at ConsenSys Health’s compute platform, some things happen or are stored on the blockchain. Some of the heavier analysis with larger data sizes happens off-chain with our confidential computing SGX capability.

I’ll just give a little bit of detail there. Basically, the CPU with the SGX capability sets up and enforces this memory partition in which only the approved datasets and applications can run. Then there’s an attestation step, where the application or the dataset … is tested, verified, and signed. The applications are verified and signed by the data providers. Only this approved code runs inside this trusted execution environment.

**VentureBeat: So how does this work with contact tracing? What’s put on the blockchain first for the contact tracing? Is it like every time Person X meets Person Y, both X and Y are entered onto the blockchain? Or is it a little more complicated?**

**Gough:** The platform is flexible, but it would be basically the same or very similar information to what’s collected manually by contact tracers today. So personal information about the citizen, their testing status, if they’re positive, who they came in contact with and where they live, where they came into contact with us. So you can share that information across different states or jurisdictions to more effectively figure out who needs to be notified.

**VentureBeat: And is there anything else we didn’t get to?**

**Gough:** Actually, one other thing I’ll mention is there’s actually two important parts to security and privacy. The one I’ve mentioned so far is more obvious, which is protecting the privacy of the [health data](https://venturebeat.com/2021/02/01/ai-in-health-care-creates-unique-data-challenges/). The one that’s a little more nuanced is actually protecting the intellectual property of the algorithm. So a lot of these algorithm developers or AI companies are putting millions of dollars of R&D into these AI algorithms. And there is a very real concern about IP protection.

**VentureBeat: Usually to get a patent, you need to have some kind of advancement, and you have to be able to write claims that describe it. But really a lot of what comes out of an AI is a bunch of weights, some thresholds, and some things that may or may not be very easily protectable by law. But if you can keep them secret, then you don’t need to worry about the law.**

**Gough:** You know, if their algorithm is compromised and taken by someone, the entire value disappears for some of these companies. And so it’s not only protecting the data for the patients, which is very important. But it’s also protecting the intellectual property of these algorithms.

**VB Daily**

Stay in the know! Get the latest news in your inbox daily

By subscribing, you agree to VentureBeat's [Terms of Service.](https://venturebeat.com/terms-of-service/)
