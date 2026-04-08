# Government Security Classifications Policy

![rw-book-cover](https://en.wikipedia.org/static/apple-touch/wikipedia.png)

## Metadata
- Author: [[wikipedia.org]]
- Full Title: Government Security Classifications Policy
- Category: #articles
- Summary: The Government Security Classifications Policy (GSCP) is a system for classifying sensitive government data in the United Kingdom.
- URL: https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy

## Full Document
The **Government Security Classifications Policy** (GSCP) is a system for classifying [sensitive government data](https://en.wikipedia.org/wiki/Classified_information_in_the_United_Kingdom) in the [United Kingdom](https://en.wikipedia.org/wiki/United_Kingdom).

#### GPMS

Historically, the [Government Protective Marking Scheme](https://en.wikipedia.org/wiki/Government_Protective_Marking_Scheme) was used by government bodies in the UK; it divides data into UNCLASSIFIED, PROTECT, RESTRICTED, CONFIDENTIAL, SECRET and TOP SECRET. This system was designed for paper-based records; it is not easily adapted to modern government work and is not widely understood.[[1]](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_note-1)

#### Current classifications

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Government_Security_Classifications_Policy.png/440px-Government_Security_Classifications_Policy.png)](https://en.wikipedia.org/wiki/File:Government_Security_Classifications_Policy.png)The criteria for classifications are being adjusted to, so there is not always a perfect map from layer to layer.
The GSCP uses three levels of classification: OFFICIAL, SECRET and TOP SECRET.[[2]](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_note-HMG_Sec_Class-2) This is simpler than the old model and there is no direct relationship between the old and new classifications. "Unclassified" is deliberately omitted from the new model. Government bodies are not expected to automatically remark existing data, so there may be cases where organisations working under the new system still handle some data marked according to the old system.

Information Asset Owners continue to be responsible for information. The new policy does not specify particular IT security requirements – IT systems should be built and used in accordance with existing guidance from [CESG](https://en.wikipedia.org/wiki/Communications-Electronics_Security_Group).[[3]](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_note-3)

Everybody who works with government – including contractors and suppliers – is responsible for protecting information they work with, regardless of whether it has a protective marking.

Aggregation does not automatically trigger an increase in protective marking. For instance, a database with thousands of records which are individually OFFICIAL should not be relabeled as a SECRET database. Instead, information owners are expected to make decisions about [controls](https://en.wikipedia.org/wiki/Security_controls) based on a [risk assessment](https://en.wikipedia.org/wiki/Risk_assessment), and should consider what the aggregated information is, [who needs to access](https://en.wikipedia.org/wiki/Need_to_know) it, and how.

##### OFFICIAL

OFFICIAL includes most public-sector data, including a wide range of information on day-to-day government business. It is not subject to any special risks. Personal data would usually be OFFICIAL.[[4]](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_note-4) The data should be protected by [controls](https://en.wikipedia.org/wiki/Security_control) based on commercial best practice instead of expensive, difficult specialist technology and bureaucracy. There is no requirement to mark every document as "OFFICIAL" – it is understood that this is the default for government documents.[[5]](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_note-HMG_Work_Off-5)

Organisations may add "descriptors" to highlight particular types of official data, for instance commercially sensitive information about contracts, or diplomatic data which should not be seen by locally hired embassy staff. These descriptors do not automatically require special controls. "OFFICIAL" will usually include the kinds of data that were previously UNCLASSIFIED, RESTRICTED, or CONFIDENTIAL; but this may vary.

The threat model for OFFICIAL data is similar to typical large private-sector organisations; it anticipates that individual hackers, pressure groups, criminals, and investigative journalists might attempt to get information. The threat model does not guarantee protection against very persistent and skilled attacks, for instance by organised crime groups or by foreign governments; these are possible, but normal controls would make them more difficult, and much stronger controls would be disproportionate. People with routine access to OFFICIAL information should be subject to [BPSS](https://en.wikipedia.org/wiki/BPSS) screening.

OFFICIAL may include data which is subject to separate regulatory requirements, such as the [Data Protection Act](https://en.wikipedia.org/wiki/Data_Protection_Act_1998) (personal data) or [PCI DSS](https://en.wikipedia.org/wiki/PCI_DSS) (card payments).

###### OFFICIAL-SENSITIVE

OFFICIAL-SENSITIVE is an additional caveat for OFFICIAL data where it is particularly important to enforce [need to know](https://en.wikipedia.org/wiki/Need_to_know) rules. OFFICIAL-SENSITIVE documents should be marked, but they are not necessarily tracked.

It is not a classification.[[6]](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_note-6) ‘Sensitive’ is a handling caveat for a small subset of information marked OFFICIAL that require special handling by staff.

##### SECRET

"Very sensitive information", which might (for example) seriously harm national defence or crime investigations. Data should only be marked as SECRET if the Senior Information Risk Owner (which is a board level position in an organisation) agrees that it is high-impact *and* that the data must be protected against very capable attackers. Although some specialist technology might be used to protect the data, there is still strong emphasis on reuse of commercial security tools.

SECRET is a big step up from OFFICIAL; government bodies are warned against being overcautious and applying much stricter rules when OFFICIAL would be sufficient.

People with routine access to SECRET information should usually have [SC clearance](https://en.wikipedia.org/wiki/SC_clearance). SECRET data may often be exempt from [FOIA](https://en.wikipedia.org/wiki/Freedom_of_Information_Act_2000) disclosure.

##### TOP SECRET

Data with exceptionally high impact levels; compromise would have very serious impacts – for instance, many deaths. This requires an extremely high level of protection, and controls are expected to be similar to those used on existing "Top Secret" data, including CESG-approved products. Very little risk can be tolerated in TOP SECRET, although no activity is completely risk-free.[[7]](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_note-7)

People with routine access to TOP SECRET information should usually have [DV clearance](https://en.wikipedia.org/wiki/DV_clearance). TOP SECRET information is assumed to be exempt from [FOIA](https://en.wikipedia.org/wiki/Freedom_of_Information_Act_2000) disclosure. Disclosure of such information is assumed to be above the threshold for [Official Secrets Act](https://en.wikipedia.org/wiki/Official_Secrets_Act) prosecution.[[8]](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_note-8)

##### Special handling instructions

Special handling instructions are additional markings which used in conjunction with a classification marking to indicate the nature or source of its content, limit access to designated groups, and / or to signify the need for enhanced handling measures. In addition to a paragraph near the start of the document special handling instructions include Descriptors, Codewords, Prefixes and national caveats.[[2]](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_note-HMG_Sec_Class-2)

###### Descriptors

A DESCRIPTOR is used with the security classification to identify certain categories of sensitive information and indicates the need for common sense precautions to limit access. The normal descriptors are 'COMMERCIAL’, 'LOCSEN’ and 'PERSONAL’.[[2]](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_note-HMG_Sec_Class-2)

###### Codewords

A Codeword is a single word expressed in CAPITAL letters that follows the security classification to providing security cover for a particular asset or event. They are usually only applied to SECRET and TOP SECRET assets.[[2]](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_note-HMG_Sec_Class-2)

###### Prefixes and national caveats

The UK prefix is added to the security classification of all assets sent to foreign governments or international organisations. This prefix designates the UK as the originating country and that the British Government should be consulted before any possible disclosure.[[2]](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_note-HMG_Sec_Class-2)

National caveats follow the security classification. Unless explicitly named, information bearing a national caveat is not sent to foreign governments, overseas contractors, international organisations or released to any foreign nationals.[[2]](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_note-HMG_Sec_Class-2) Example

‘TOP SECRET – UK / US EYES ONLY’
With the exception of British Embassies and Diplomatic Missions or Service units or establishments, assets bearing the UK EYES ONLY national caveat are not sent overseas.[[2]](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_note-HMG_Sec_Class-2)

#### New approach to handling classified information

As per the previous GPMS model, the choice of classification relates only to the data's confidentiality. Unlike the old model it replaces however, the GSCP does not consider the consequence of a compromise as the primary factor, but instead is based on the capability and motivation of potential threat actors (attackers) and the acceptability of that risk to the business.

Where a capable and motivated attacker such as a Foreign Intelligence Service, or Serious and Organised Crime are considered to be in scope of the data to be classified, the business must implicitly accept this risk to classify the data as OFFICIAL. If they do not or cannot accept this risk they must at least initially consider the data to be SECRET, though it may be reduced to OFFICIAL or increased to TOP SECRET later when the consequences of a compromise are also considered.

The implication of this approach and the binary nature of determining if a risk from capable and motivated attackers is acceptable or not, means that data cannot easily progress through the GSCP in a linear fashion as it did through GPMS.

This is a complexity often lost on Information Asset Owners previously used to the strictly hierarchical tiered rising structure of GPMS (e.g. UNCLASSIFIED, PROTECT, RESTRICTED, CONFIDENTIAL, SECRET, TOP SECRET).

By contrast GSCP data starts either with an OFFICIAL **OR** SECRET classification depending on the nature of threat and its acceptability to the business, and thereafter moves up or down accordingly based on consequence of compromise.

OFFICIAL data may therefore rise to TOP SECRET, but cannot be SECRET unless the risk previously accepted for a capable attacker is revised.

SECRET data may be reduced to OFFICIAL where no serious consequences can be identified from a potential breach, or SECRET can also rise to TOP SECRET if serious consequences could arise.

Impact levels also consider integrity and availability, but CESG's system of Business Impact Levels (BIL) is under review too and in most practical contexts have now fallen into disuse.

It is therefore no longer strictly the case that the greater the consequences if the data confidentiality were to be compromised, the higher the classification, since data with a high impact (including material which could result in threat to life) may still be classified as OFFICIAL if the relevant business owner believes it is not necessary to protect this from an attacker who has the capabilities of a Foreign Intelligence Service or Serious and Organised Crime.

Conversely some data with much lower consequences (for example ongoing Police investigations into a criminal group, or intelligence information relating to possible prosecutions) but where the business will not accept compromise from such an attacker could be classified as SECRET.

Guidance issued in April 2014 at the implementation of the GSCP and still available on Gov.UK sources [[9]](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_note-9) suggested that UK Government information systems would continue to be accredited much as before, normally using CESG [Information Assurance Standard 1 & 2](https://en.wikipedia.org/wiki/Information_Assurance_Standard_1_%26_2). This has however been progressively discarded through GDS and NCSC blog statements since May 2014 and the IS1 & 2 standard itself is no longer maintained or mandated. Accreditation has also been largely replaced by alternative models of assurance aligned to various commercial practices.

The NAO report "Protecting Information across Government" (Sep 2016) was somewhat critical of the move to this model and the adoption of GSCP overall [[10]](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_note-10)

Existing published guidance continues to suggest that storage media which hold UK government data should still be destroyed or purged according to [HMG IA Policy No. 5](https://en.wikipedia.org/wiki/HMG_IA_Policy_No._5), however terminology in this guidance and other material has not been updated fully to reflect the changes from GPMS protective markings to GSCP classifications and as such its value is now arguably somewhat reduced as a published standard.

Higher classifications still tend to require stricter [personnel vetting](https://en.wikipedia.org/wiki/Security_vetting_in_the_United_Kingdom).

#### History

The Government Security Classifications Policy was completed and published in December 2012; additional guidance and supporting processes were developed over time. The policy came into effect on 2 April 2014. [Government procurement](https://en.wikipedia.org/wiki/Government_procurement_in_the_United_Kingdom) procedures took account of the new policy from 21 October 2023 so that new security requirements could be taken into account in contracts let from that date.[[11]](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_note-11)

#### See also

* [Security Policy Framework](https://en.wikipedia.org/wiki/Security_Policy_Framework)
* [Information Assurance Standard 1 & 2](https://en.wikipedia.org/wiki/Information_Assurance_Standard_1_%26_2)
* [Cabinet Office](https://en.wikipedia.org/wiki/Cabinet_Office)
* [List X site](https://en.wikipedia.org/wiki/List_X_site)
* [Compartmentalization (information security)](https://en.wikipedia.org/wiki/Compartmentalization_(information_security))
* [Security vetting in the United Kingdom](https://en.wikipedia.org/wiki/Security_vetting_in_the_United_Kingdom)

#### References

1. **[^](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_ref-1)** An Introduction to Government Security Classifications. Page 1. Cabinet Office, April 2013
2. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_ref-HMG_Sec_Class_2-0) [***b***](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_ref-HMG_Sec_Class_2-1) [***c***](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_ref-HMG_Sec_Class_2-2) [***d***](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_ref-HMG_Sec_Class_2-3) [***e***](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_ref-HMG_Sec_Class_2-4) [***f***](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_ref-HMG_Sec_Class_2-5) [***g***](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_ref-HMG_Sec_Class_2-6) [*Government Security Classifications*](https://web.archive.org/web/20170830013656/https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/251480/Government-Security-Classifications-April-2014.pdf) (PDF) (Version 1.0 – October 2013 ed.). HMG Cabinet Office. April 2014. Archived from [the original](https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/251480/Government-Security-Classifications-April-2014.pdf) (PDF) on August 30, 2017. Retrieved September 10, 2014.
3. **[^](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_ref-3)** Government Security Classifications FAQ Sheet 2: Managing Information Risk at OFFICIAL. Cabinet Office, April 2013
4. **[^](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_ref-4)** An Introduction to Government Security Classifications, Cabinet Office, April 2013
5. **[^](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_ref-HMG_Work_Off_5-0)** [*Government Security Classifications FAQ Sheet 1: Working with OFFICIAL Information*](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/251475/FAQ1-Working-with-Official-Information-v1.2-Apr-2013.pdf) (PDF). HMG Cabinet Office. April 2013.Government Security Classifications FAQ Sheet 1: Working with OFFICIAL Information. Cabinet Office, April 2013
6. **[^](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_ref-6)** ["'OFFICIAL-SENSITIVE' data and IT"](https://www.gov.uk/guidance/official-sensitive-data-and-it). *GOV.UK*. Retrieved 2023-08-24.
7. **[^](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_ref-7)** Government Security Classifications: Security Controls Framework. Cabinet Office, April 2013
8. **[^](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_ref-8)** Government Security Classifications: Security Controls Framework, page 19. Cabinet Office, April 2013
9. **[^](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_ref-9)** ["Government Security Classifications"](https://www.gov.uk/government/publications/government-security-classifications). 17 July 2023.
10. **[^](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_ref-10)** ["Protecting information across government – National Audit Office (NAO) Report"](https://www.nao.org.uk/report/protecting-information-across-government/). 14 September 2016.
11. **[^](https://en.wikipedia.org/wiki/Government_Security_Classifications_Policy#cite_ref-11)** Cabinet Office, [Procurement Policy Note – Implementing the New Classifications Policy](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/252385/PPN_0913_-_Implementing_the_New_Classifications_Policy.pdf), Information Note 9/13, published 21 October 2013, accessed 24 March 2023

#### External links

* [Government Security Classifications on the Cabinet Office website](https://www.gov.uk/government/publications/government-security-classifications)
* [Government Security Classifications video](https://www.youtube.com/watch?v=_s9AuJdei64)
* [Ministry of Defence Industry Security Notice 2014/1](https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/282902/isn_2014_01_gov_security_class_scheme.pdf)
* [PSN Community Briefing](https://web.archive.org/web/20140903105102/https://www.publicservicesnetwork.service.gov.uk/article/2074/PSN-publishes-community-briefing-on-new-Government-Security-Classification-Policy)
* [Cybermatters blog post on the scheme](http://cybermatters.info/2014/04/01/uk-government-security-classification-scheme/)
