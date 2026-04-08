# How To Use NotebookLM As A Research Tool

![rw-book-cover](https://miro.medium.com/v2/resize:fit:1200/1*Jh6XXMnVeIeQTlT72ZBlow.png)

## Metadata
- Author: [[Steven Johnson]]
- Full Title: How To Use NotebookLM As A Research Tool
- Category: #articles
- Summary: NotebookLM helps you organize and search your research by letting you add documents, quotes, and web clippings as sources. You can import notes from tools like Google Play Reader, ReadWise, and Google Keep to build a smart, searchable notebook. It also lets you take notes, ask questions, and turn your ideas into new sources for deeper study.
- URL: https://stevenberlinjohnson.com/how-to-use-notebooklm-as-a-research-tool-6ad5c3a227cc

## Full Document
#### For the first time, it is possible to work with an AI that is grounded in all the important quotes from your reading history.

[**02.23.25:** I’ve updated this document to reflect all the new features we have introduced at [NotebookLM](http://notebooklm.google.com) since I originally wrote this piece.]

NotebookLM excels at workflows that involve synthesizing information dispersed across multiple documents, which makes it a valuable tool for students, scholars, journalists, analysts, and many other “knowledge worker” professions. If your research material involves any of our standard source formats, like PDFs, Google Docs, Web URLS, and more) you can **create a notebook for the project you’re working on, and immediately add the relevant documents as sources**. Within seconds, NotebookLM becomes a virtual research assistant, capable of answering questions or tracking down references based entirely on the source materials you’ve supplied.

But of course, many research projects revolved around information stored in books. If your project happens to involve public domain books, you should be able to find PDF or HTML-based versions that can be loaded into Notebook at sites like [Project Gutenberg](https://www.gutenberg.org/). (NotebookLM does not currently support the ePub format.) But if your research involves rights-protected books or e-books, the best way to use NotebookLM is to **capture the most important quotes from the books you read, and save them in a Google Doc**. The ideal formatting for a quote collection includes information about the author and title of the book (and other relevant metadata, like page number) in every paragraph in the file, like so:

*“The scientist Stuart Kauffman has a suggestive name for the set of all those first-order combinations: ‘the adjacent possible.’ The phrase captures both the limits and the creative potential of change and innovation.” (Steven Johnson, Where Good Ideas Comes From, pg. 45.)*

Once you have a collection of quotations formatted this way, you can import them as a source, and not only ask NotebookLM factual questions about them, but also questions like: “Who are the main authors who discuss ant colonies?” or “What was the name of that book about politics in Ancient Greece?”

![](https://miro.medium.com/v2/resize:fit:1400/1*Jh6XXMnVeIeQTlT72ZBlow.png)
As always with NotebookLM, the chat responses come with inline citations, allowing you to jump directly to the underlying passages that the model used to formulate its answers. Unlike earlier bibliographic tools, you don’t need rigid data formats with NotebookLM. You could put the author name at the beginning of the paragraph, or just mention the title at the end after a dash — NotebookLM is smart enough generally to figure out what you intended. But it is helpful to include whatever metadata you want in each paragraph of your quotation collection. If you have full bibiographic information included in each quote, you’ll also be able to ask Notebook to generate a biblography for the works cited in the previous response just be asking for that in a followup question.

**Capturing Quotes from Books Using the Google Play Reader**If you read books using the [Google Play e-reader](https://play.google.com/store/books?hl=en&gl=US), you can highlight text in the books as you read and automatically export the quotations to a Google Doc. (You may want to slightly edit those docs so they are formatted properly for NotebookLM, with metadata in each paragraph.)

To export highlights to Google docs, select the three dots in the upper right-hand corner while reading an e-book. Make sure “Save annotations to Google Drive is turned on.”

![](https://miro.medium.com/v2/resize:fit:1400/1*r6qu9XZ3lC_MctU6U3hVzg.png)
Once you highlight passages in a book, or add your own annotations, those notes will be captured to a new doc in a folder called “Play Books Notes” in your Drive. There will be one doc for each book that contains highlights. They will each have a name like **Notes from “Great Expectations.”**

You can then open a notebook, and import each book’s notes doc as a source.

**Capturing Quotes from Other e-Book Readers Using ReadWise**For other e-book readers, you can use the app [ReadWise](http://readwise.io) to curate your quotation collections and easily export them to a Google Doc as well. ReadWise automatically formats its quote collections so that they are optimized for NotebookLM.

1. Select the “Export” option on your Readwise dashboard.
2. Choose NotebookLM to export your highlights
3. Choose the “configure” option for Google Docs exporting. You’ll see the following screen:

![](https://miro.medium.com/v2/resize:fit:1400/1*wLA0lHUGF4HhqyBCS3hpEw.png)
If you choose “send to a single Doc in my Drive,” your highlights will be sent to a single doc in one continuous stream. (If they are more than roughly 200,000 words, they will be automatically split up into multiple docs.) This is the most efficient way to load your quotations into NotebookLM, because you can incorporate quotes from dozens of separate books into a single source. (Currently the free version NotebookLM limits you to 50 sources per notebook, though NotebookLM Plus allows you to store up to 300 sources)

However, if you are working on a project that only involves quotes from a small number of books, you can uncheck the option to “send to a single Doc” and ReadWise will create a new doc for each book that you have highlights for.

Once you have exported from ReadWise, you can open up NotebookLM. Choose “add sources,” and import the docs Readwise created from your Drive.

Note: Because Readwise formats each quote with the author and title information, **it doesn’t really matter from NotebookLM’s perspective whether you export all your highlights as a single file or not**. You can still ask questions like, “What did Wright argue about collective intelligence in the book *Non-Zero*?” and NotebookLM will be able to pull out information related to that specific book or author. But it can also be helpful to have each source be associated with a single book if you want to consult the sources directly.

Because I happen to have hundreds of books (and thousands of quotes) in my ReadWise collection, I choose to bulk export my quotes, which allows me to maintain a single notebook with my entire reading history loaded as sources. I have also added to this collection the full text of half of the books that I’ve written, so that slowly over time this Notebook is becoming a repository for all the important ideas I’ve written and all the ideas I’ve published. I call it the “Everything” notebook. Here are a few examples of the kinds of questions I can ask in this notebook:

![](https://miro.medium.com/v2/resize:fit:1400/1*7x2vzC_UPRYm3d8IEyzMXw.png)
![](https://miro.medium.com/v2/resize:fit:1400/1*46maEW9kymxoRgEwF7ZCVQ.png)
(I like how NotebookLM used the word “emerge” in the opening to the second response — a subtle nod to my book Emergence which had a long discussion of ant colonies. Very clever!)

**Adding Quotes from the Web using Google Keep**You can also use quote collections made up of text passages you’ve curated from the Web. Google Keep allows you to select text on any page and “Save to Keep” — capturing the text and the URL of the web page to your Keep account. (You can do Web clippings with Keep in several different ways. On desktop, there is a Chrome extension that you install. On mobile — both iOS and Android — if you install the Keep app, it gives you a share sheet that you can access from a mobile browser to collect web clippings.) Keep allows you to select your clippings and export them as a group to Docs, which can then be brought into NotebookLM as a source. So for instance an analyst researching information about a new financial services company could visit a dozen web sites that contain news articles about the company, selecting quotes and saving them to Keep as they read. When they’re done with that research, they go to their main Keep page, and select all the clippings that are relevant to their project. Then they click on the three dots in the upper right corner and choose “Copy to Google Docs.”

![](https://miro.medium.com/v2/resize:fit:1400/1*edC0qre2ON71uoO7FDSVMA.png)
That creates a new file in their Drive called “Google Keep Document” which they retitle something like “Financial company research.” Then they import that doc into NotebookLM, alongside any other sources they are using for the project. (ReadWise also offers web clipping tools that can output your quotes to Docs.)

**Organizing Your Ideas and Exploring Your Research**NotebookLM also offers extensive tools to help you organize and brainstorm ideas once you’ve collected a set of sources and quotations to use in your project. One productive workflow is to use NotebookLM to quickly capture interesting ideas as you read and ask questions, saving anything that piques your interest as a note. You can also compose your own notes just by hitting “Add note” in the right-hand Studio panel. One of my favorite working modes is to write and think with the chat and note panel open, but the source panel collapsed. I jot down ideas in the open note, but also bounce back to the chat to ask questions, brainstorm, or track down specific quotes or details from the sources.

![](https://miro.medium.com/v2/resize:fit:1400/1*kydZUdAk2fMMMGjnKraRCQ.png)
When you’ve compiled a set of notes for a project — whether saved responses from chat, or your own writing—you can then easily transform them into other formats, or store them as sources so that they can influence the chat responses. Just click on the three dots at the top of the Notes section of the Studio Panel, and choose “Convert all notes to source.”

![](https://miro.medium.com/v2/resize:fit:1400/1*S8hAYdVuV0r0qUChm8uzew.png)
After a few seconds, you’ll see a new source in the Source Panel called “All notes” with today’s date. If you unselect all your other sources and just select that “All notes” source, all the answers in chat will be grounded exclusively in that specific source.

![](https://miro.medium.com/v2/resize:fit:1400/1*HzZTtmAaTC1fCbRJiFlIZg.png)
Source selection is a very powerful feature in NotebookLM for a number of reasons, but in this case, it allows you to ask the model to transform or analyze your notes in almost any way you can imagine. Here’s one example where I asked Notebook to generate a quiz to review the material that I’d curated in my notes:

![](https://miro.medium.com/v2/resize:fit:1400/1*jZ8jf0bsvHLg54YWlMoyqw.png)
Hopefully these tips will be enough to get you started using NotebookLM as a research tool. If you’d like to learn more, or share your own experiences, we have [a lively NotebookLM Discord community](https://discord.com/invite/Az2N7BwV7r) with extensive discussion of use-cases, new feature ideas, and much more.
