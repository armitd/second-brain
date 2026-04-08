# Conway's law

![rw-book-cover](https://en.wikipedia.org/static/apple-touch/wikipedia.png)

## Metadata
- Author: [[wikipedia.org]]
- Full Title: Conway's law
- Category: #articles
- Summary: Conway's Law, named after computer programmer Melvin Conway, states that organizations design systems that mirror their own communication structure. This is based on the idea that for a product to function effectively, the authors and designers of its components must communicate with each other. Therefore, the technical structure of a system reflects the social boundaries of the organizations that produced it. The law is primarily applied in the field of software architecture but can be applied to most technical fields. Various interpretations exist regarding the causality and desirability of the phenomenon described by Conway's Law.
- URL: https://en.wikipedia.org/wiki/Conway%27s_law

## Full Document
**Conway's law** is an [adage](https://en.wikipedia.org/wiki/Adage) that states organizations design systems that mirror their own communication structure. It is named after the [computer programmer](https://en.wikipedia.org/wiki/Programmer) [Melvin Conway](https://en.wikipedia.org/wiki/Melvin_Conway), who introduced the idea in 1967.[[1]](https://en.wikipedia.org/wiki/Conway's_law#cite_note-1) His original wording was:

> Any organization that designs a system (defined broadly) will produce a design whose structure is a copy of the organization's communication structure.[[2]](https://en.wikipedia.org/wiki/Conway's_law#cite_note-Conway-2)[[3]](https://en.wikipedia.org/wiki/Conway's_law#cite_note-3)
> 
> — Melvin E. Conway

The law is based on the reasoning that in order for a product to function, the authors and designers of its component parts must communicate with each other in order to ensure compatibility between the components. Therefore, the technical structure of a system will reflect the social boundaries of the organizations that produced it, across which communication is more difficult. In colloquial terms, it means complex products end up "shaped like" the organizational structure they are designed in or designed for. The law is applied primarily in the field of software architecture, though Conway directed it more broadly and its assumptions and conclusions apply to most technical fields.

#### Variations

[Eric S. Raymond](https://en.wikipedia.org/wiki/Eric_S._Raymond), an open-source advocate, restated Conway's law in *The New Hacker's Dictionary*, a reference work based on the [Jargon File](https://en.wikipedia.org/wiki/Jargon_File). The organization of the software and the organization of the software team will be [congruent](https://en.wiktionary.org/wiki/congruence), he said. Summarizing an example in Conway's paper, Raymond wrote:

> If you have four groups working on a compiler, you'll get a 4-pass compiler.[[4]](https://en.wikipedia.org/wiki/Conway's_law#cite_note-Raymond1996-4)[[5]](https://en.wikipedia.org/wiki/Conway's_law#cite_note-JargonFile-5)
> 
> 

Raymond further presents *Tom Cheatham's amendment* of Conway's Law, stated as:

> If a group of N persons implements a COBOL compiler, there will be N−1 passes. Someone in the group has to be the manager.[[4]](https://en.wikipedia.org/wiki/Conway's_law#cite_note-Raymond1996-4)
> 
> 

[Yourdon](https://en.wikipedia.org/wiki/Edward_Yourdon) and [Constantine](https://en.wikipedia.org/wiki/Larry_Constantine), in their 1979 book on [Structured Design](https://en.wikipedia.org/wiki/Structured_Design), gave a more strongly stated variation of Conway's Law:

> The structure of any system designed by an organization is [isomorphic](https://en.wikipedia.org/wiki/Isomorphism) to the structure of the organization.[[6]](https://en.wikipedia.org/wiki/Conway's_law#cite_note-Yourdon1979-6)
> 
> 

[James O. Coplien](https://en.wikipedia.org/wiki/James_O._Coplien) and [Neil B. Harrison](https://en.wikipedia.org/w/index.php?title=Neil_B._Harrison&action=edit&redlink=1) stated in a 2004 book concerned with organizational patterns of [Agile software development](https://en.wikipedia.org/wiki/Agile_software_development):

> If the parts of an organization (e.g., teams, departments, or subdivisions) do not closely reflect the essential parts of the product, or if the relationships between organizations do not reflect the relationships between product parts, then the project will be in trouble ... Therefore: Make sure the organization is compatible with the product architecture.[[7]](https://en.wikipedia.org/wiki/Conway's_law#cite_note-7)
> 
> 

More recent commentators have noted a corollary - for software projects with a long lifetime of code reuse, such as [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows), the structure of the code mirrors not only the communication structure of the organization which created the most recent release, but also the communication structures of every *previous* team which worked on that code.[[8]](https://en.wikipedia.org/wiki/Conway's_law#cite_note-:0-8)

#### Interpretations

The law is, in a strict sense, only about correspondence; it does *not* state that communication structure is the cause of system structure, merely describes the connection. Different commentators have taken various positions on the direction of causality; that technical design causes the organization to restructure to fit,[[9]](https://en.wikipedia.org/wiki/Conway's_law#cite_note-9) that the organizational structure dictates the technical design,[[10]](https://en.wikipedia.org/wiki/Conway's_law#cite_note-10) or both.[[11]](https://en.wikipedia.org/wiki/Conway's_law#cite_note-11)[[12]](https://en.wikipedia.org/wiki/Conway's_law#cite_note-12)[[13]](https://en.wikipedia.org/wiki/Conway's_law#cite_note-ColferBaldwin-13) Conway's law was intended originally as a sociological observation, but many other interpretations are possible. The *New Hacker's Dictionary* entry uses it in a primarily humorous context,[[14]](https://en.wikipedia.org/wiki/Conway's_law#cite_note-14) while participants at the 1968 *National Symposium on [Modular Programming](https://en.wikipedia.org/wiki/Modular_programming)* considered it sufficiently serious and universal to dub it 'Conway's Law'.[[6]](https://en.wikipedia.org/wiki/Conway's_law#cite_note-Yourdon1979-6) Opinions also vary on the desirability of the phenomenon; some say that the mirroring pattern is a helpful feature of such systems, while other interpretations say it's an undesirable result of organizational bias. Middle positions describe it as a necessary feature of compromise, undesirable in the abstract but necessary to handle human limitations.[[8]](https://en.wikipedia.org/wiki/Conway's_law#cite_note-:0-8)

#### Supporting evidence

An example of the impact of Conway's Law can be found in the design of some organization websites. Nigel Bevan stated in a 1997 paper, regarding [usability](https://en.wikipedia.org/wiki/Usability) issues in websites: "Organizations often produce web sites with a content and structure which mirrors the internal concerns of the organization rather than the needs of the users of the site."[[15]](https://en.wikipedia.org/wiki/Conway's_law#cite_note-Bevan1997-15)

Evidence in support of Conway's law has been published by a team of [Massachusetts Institute of Technology](https://en.wikipedia.org/wiki/Massachusetts_Institute_of_Technology) (MIT) and [Harvard Business School](https://en.wikipedia.org/wiki/Harvard_Business_School) researchers who, using "the mirroring hypothesis" as an equivalent term for Conway's law, found "strong evidence to support the mirroring hypothesis", and that the "product developed by the loosely-coupled organization is significantly more modular than the product from the tightly-coupled organization". The authors highlight the impact of "organizational design decisions on the technical structure of the artifacts that these organizations subsequently develop".[[16]](https://en.wikipedia.org/wiki/Conway's_law#cite_note-MacCormack2011-16)

Additional and likewise supportive case studies of Conway's law have been conducted by Nagappan, Murphy and Basili at the [University of Maryland](https://en.wikipedia.org/wiki/University_of_Maryland) in collaboration with [Microsoft](https://en.wikipedia.org/wiki/Microsoft),[[17]](https://en.wikipedia.org/wiki/Conway's_law#cite_note-Nagappan2008-17) and by Syeed and Hammouda at [Tampere University of Technology](https://en.wikipedia.org/wiki/Tampere_University_of_Technology) in Finland.[[18]](https://en.wikipedia.org/wiki/Conway's_law#cite_note-18)

#### See also

* [Cognitive dimensions of notations](https://en.wikipedia.org/wiki/Cognitive_dimensions_of_notations)
* [Deutsch limit](https://en.wikipedia.org/wiki/Deutsch_limit)
* [Organizational theory](https://en.wikipedia.org/wiki/Organizational_theory)
* [Good Regulator](https://en.wikipedia.org/wiki/Good_Regulator)

#### References

1. **[^](https://en.wikipedia.org/wiki/Conway's_law#cite_ref-1)** Conway, Melvin. ["Conway's Law"](http://www.melconway.com/Home/Conways_Law.html). *Mel Conway's Home Page*. [Archived](https://web.archive.org/web/20190929004831/http://www.melconway.com/Home/Conways_Law.html) from the original on 2019-09-29. Retrieved 2019-09-29.
2. **[^](https://en.wikipedia.org/wiki/Conway's_law#cite_ref-Conway_2-0)** Conway, Melvin E. (April 1968). ["How do Committees Invent?"](http://www.melconway.com/Home/Committees_Paper.html). *[Datamation](https://en.wikipedia.org/wiki/Datamation)*. **14** (5): 28–31. [Archived](https://web.archive.org/web/20191010021833/http://www.melconway.com/Home/Committees_Paper.html) from the original on 2019-10-10. Retrieved 2019-10-10. […] organizations which design systems […] are constrained to produce designs which are copies of the communication structures of these organizations.
3. **[^](https://en.wikipedia.org/wiki/Conway's_law#cite_ref-3)** Conway, Melvin (1968). ["How do committees invent"](http://www.melconway.com/Home/pdf/committees.pdf) (PDF). *Datamation*: 28–31.
4. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Conway's_law#cite_ref-Raymond1996_4-0) [***b***](https://en.wikipedia.org/wiki/Conway's_law#cite_ref-Raymond1996_4-1) Raymond, Eric S. (October 1996). [*The New Hacker's Dictionary*](https://books.google.com/books?id=g80P_4v4QbIC) (3rd ed.). Cambridge, Massachusetts: MIT Press. p. 124. [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier)) [978-0-262-68092-9](https://en.wikipedia.org/wiki/Special:BookSources/978-0-262-68092-9). Conway's Law: prov. The rule […] originally stated as "If you have four groups working on a compiler, you'll get a 4-pass compiler". […] Tom Cheatham's amendment of Conway's Law: "If a group of N persons implements a COBOL compiler, there will be N-1 passes. Someone in the group has to be the manager."
5. **[^](https://en.wikipedia.org/wiki/Conway's_law#cite_ref-JargonFile_5-0)** Eric S. Raymond. ["Conway's Law"](http://catb.org/~esr/jargon/html/C/Conways-Law.html). *The Jargon File, version 4.4.8*. [Archived](https://web.archive.org/web/20120326195139/http://catb.org/~esr/jargon/html/C/Conways-Law.html) from the original on 2012-03-26. Retrieved 2012-03-26.
6. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Conway's_law#cite_ref-Yourdon1979_6-0) [***b***](https://en.wikipedia.org/wiki/Conway's_law#cite_ref-Yourdon1979_6-1) Yourdon, Edward; Constantine, Larry L. (1979). [*Structured Design: Fundamentals of a Discipline of Computer Program and Systems Design*](https://books.google.com/books?id=zMQmAAAAMAAJ) (2nd ed.). Englewood Cliffs, N.J.: Prentice Hall. [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier)) [0138544719](https://en.wikipedia.org/wiki/Special:BookSources/0138544719). [OCLC](https://en.wikipedia.org/wiki/OCLC_(identifier)) [4503223](https://www.worldcat.org/oclc/4503223). Conway's Law: The structure of a system reflects the structure of the organization that built it. Conway's Law has been stated even more strongly: The structure of any system designed by an organization is isomorphic to the structure of the organization.
7. **[^](https://en.wikipedia.org/wiki/Conway's_law#cite_ref-7)** Coplien and Harrison (July 2004). *Organizational Patterns of Agile Software Development*. [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier)) [978-0-13-146740-8](https://en.wikipedia.org/wiki/Special:BookSources/978-0-13-146740-8).
8. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Conway's_law#cite_ref-:0_8-0) [***b***](https://en.wikipedia.org/wiki/Conway's_law#cite_ref-:0_8-1) Muratori, Casey, [*The Only Unbreakable Law*](https://www.youtube.com/watch?v=5IUj1EZwpJY), retrieved 2022-03-21
9. **[^](https://en.wikipedia.org/wiki/Conway's_law#cite_ref-9)** Chandler, A. D. (1977). The Visible Hand: The Managerial Revolution in American Business. Harvard University Press, Cambridge, MA.
10. **[^](https://en.wikipedia.org/wiki/Conway's_law#cite_ref-10)** Henderson, R. M., & Clark, K. B. (1990). Architectural innovation: The reconfiguration of existing product technologies and the failure of established firms. Administrative science quarterly, 9-30.
11. **[^](https://en.wikipedia.org/wiki/Conway's_law#cite_ref-11)** Baldwin, C. Y., & Clark, K. B. (2000). Design rules: The power of modularity (Vol. 1). Chapter 7. MIT press. (Chapters 1 and 14 are counted as a descriptive industry study.)
12. **[^](https://en.wikipedia.org/wiki/Conway's_law#cite_ref-12)** Fixson, S. K., & Park, J. K. (2008). The power of integrality: Linkages between product architecture, innovation, and industry structure. Research Policy, 37(8), 1296-1316.
13. **[^](https://en.wikipedia.org/wiki/Conway's_law#cite_ref-ColferBaldwin_13-0)** "The Mirroring Hypothesis: Theory, Evidence and Exceptions", Lyra J. Colfer, Carliss Y. Baldwin <https://www.hbs.edu/ris/Publication%20Files/16-124_7ae90679-0ce6-4d72-9e9d-828872c7af49.pdf>
14. **[^](https://en.wikipedia.org/wiki/Conway's_law#cite_ref-14)** Raymond1996
15. **[^](https://en.wikipedia.org/wiki/Conway's_law#cite_ref-Bevan1997_15-0)** Bevan, Nigel (November 1997). ["Usability issues in website design"](https://experiencelab.typepad.com/files/usability-issues-in-website-design-1.pdf) (PDF). *Design of Computing Systems: Social and Ergonomic Considerations*. Proceedings of the Seventh International Conference on Human-Computer Interaction (HCI International '97). Vol. 2. San Francisco, California, USA: Elsevier. pp. 803–806.
16. **[^](https://en.wikipedia.org/wiki/Conway's_law#cite_ref-MacCormack2011_16-0)** MacCormack, Alan; Rusnak, John; Baldwin, Carliss Y. (2011). ["Exploring the Duality between Product and Organizational Architectures: A Test of the Mirroring Hypothesis"](https://dash.harvard.edu/bitstream/handle/1/34403525/maccormack%2Cbaldwin%2Crusnak_exploring-the-duality.pdf) (PDF). *SSRN Working Paper Series*. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.2139/ssrn.1104745](https://doi.org/10.2139%2Fssrn.1104745). [ISSN](https://en.wikipedia.org/wiki/ISSN_(identifier)) [1556-5068](https://www.worldcat.org/issn/1556-5068). We find strong evidence to support the mirroring hypothesis. In all of the pairs we examine, the product developed by the loosely-coupled organization is significantly more modular than the product from the tightly-coupled organization. […] Our results have significant managerial implications, in highlighting the impact of organizational design decisions on the technical structure of the artifacts that these organizations subsequently develop.
17. **[^](https://en.wikipedia.org/wiki/Conway's_law#cite_ref-Nagappan2008_17-0)** Nagappan, Nachiappan; Murphy, Brendan; Basili, Victor (2008). "The influence of organizational structure on software quality". *Proceedings of the 13th International Conference on Software Engineering - ICSE '08*. New York, New York, USA: ACM Press: 521. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1145/1368088.1368160](https://doi.org/10.1145%2F1368088.1368160). [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier)) [9781605580791](https://en.wikipedia.org/wiki/Special:BookSources/9781605580791). [S2CID](https://en.wikipedia.org/wiki/S2CID_(identifier)) [5048618](https://api.semanticscholar.org/CorpusID:5048618).
18. **[^](https://en.wikipedia.org/wiki/Conway's_law#cite_ref-18)** Syeed, M. M. Mahbubul; Hammouda, Imed (2013). "Socio-technical Congruence in OSS Projects: Exploring Conway's Law in FreeBSD". *Open Source Software: Quality Verification*. IFIP Advances in Information and Communication Technology. Vol. 404. pp. 109–126. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/978-3-642-38928-3\_8](https://doi.org/10.1007%2F978-3-642-38928-3_8). [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier)) [978-3-642-38927-6](https://en.wikipedia.org/wiki/Special:BookSources/978-3-642-38927-6).

#### Further reading

* Alan MacCormack, John Rusnak & Carliss Baldwin, 2012, "Exploring the Duality between Product and Organizational Architectures: A Test of the 'Mirroring' Hypothesis," *Research Policy* **41**:1309–1324 [earlier Harvard Business School Working Paper 08-039], see [[1]](http://www.hbs.edu/faculty/Publication%20Files/Research%20Policy%2041%20(2012)%201309–%201324_c5c2350e-013c-4065-a2f9-d95eb32177d5.pdf), accessed 9 March 2015.
* Lise Hvatum & Allan Kelly, Eds., "What do I think about Conway's Law now? Conclusions of a EuroPLoP 2005 Focus Group," European Conference on Pattern Languages of Programs, Kloster Irsee, Germany, January 16, 2006, see [[2]](http://www.allankelly.net/static/presentations/EuroPLoP2005/ConwaysLawFocusGroup.pdf), addressed 9 March 2015.
* Lyra Colfer & Carliss Baldwin. "The Mirroring Hypothesis: Theory, Evidence and Exceptions." Harvard Business School Working Paper, No. 16-124, April 2016. (Revised May 2016.) See [[3]](http://www.hbs.edu/faculty/Publication%20Files/16-124_7ae90679-0ce6-4d72-9e9d-828872c7af49.pdf), accessed 2 August 2016.
