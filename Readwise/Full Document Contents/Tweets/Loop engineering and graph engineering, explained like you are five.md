# Loop engineering and graph engineering, explained like you are five

![rw-book-cover](https://pbs.twimg.com/profile_images/2054664188417413120/DZKz0Tqn.jpg)

## Metadata
- Author: [[Yarchi]]
- Full Title: Loop engineering and graph engineering, explained like you are five
- Category: #tweets
- Summary: A loop is one worker doing tasks one by one, while a graph is many workers in a line, each doing a part and saving progress. Use loops for small, quick jobs and graphs for bigger, repeatable projects with clear steps. Graphs help find errors, save work, and run parts at the same time, making big jobs easier to manage.
- URL: https://twitter.com/undefinedKi/status/2081400172806894047/?rw_tt_thread=True

## Full Document
Loop engineering and graph engineering, explained like you are five. Everyone throws the words around, almost nobody defines them

A loop is one worker with a to-do list. It picks a task, does it, looks at what happened, picks the next one. Everything it knows lives in one conversation. When that conversation fills up, things start falling out of it.

A graph is an assembly line. Each station does one job. Between stations the work gets saved to disk. If station four fails, you rerun station four, not the whole line.

Three questions decide which one you need:

1. Will you do this a hundred more times? If not, use the loop. Building the line costs more than doing the work by hand
2. Can a script tell you the output is correct? If only your taste can judge it, the checkpoints are decoration
3. Do you know the steps yet? If not, the loop will find a path you would never have drawn

The loop is not dead, it got demoted. Every station on the line still has a worker running a loop inside it.

Bookmark this 

![Image](https://pbs.twimg.com/media/HOKebRUXgAApjHK.jpg?name=orig)

![](https://pbs.twimg.com/profile_images/2054664188417413120/DZKz0Tqn.jpg)

[Yarchi](https://twitter.com/undefinedKi)
[@undefinedKi](https://twitter.com/undefinedKi)

![Graph Engineering: an Agent That Reviews Its Own Work. The Anthropic Method (Full Guide)](https://pbs.twimg.com/media/HOA-17dXMAEBHCV.jpg)

Your agent is not dumb. It is shaped wrong. 

Short tasks work. You ask for a function, you get a function. Then you point the same agent at something real, a refactor across forty files, a migration, a research job that runs for an hour, and it drifts. It forgets a decision it made twenty minutes ago. It fixes one file and breaks another. You restart it, and it starts from zero. 

The instinct is to blame the model. Usually the model is fine. The shape of the work is wrong. 

### Loops and graphs

Most agents are loops. The model thinks, calls a tool, reads the result, thinks again, and repeats until it decides it is done. Control lives inside the model. You see the input and the output, and almost nothing in between. When it fails at minute forty, you do not know which minute it went wrong. 

A graph moves control outside the model. You define the steps, what connects to what, and where state lives. The model still does the thinking, but inside nodes you drew. Some nodes do not use a model at all: a script, a compiler, a test suite. 

Four things change when you do this. You can see where it failed, because failure happens at a named node. You can resume, because state sits on disk instead of in a context window. You can run independent branches at the same time. And you can make the boring parts deterministic instead of paying a model to guess. 

### This is not theory

[Posted Jul 25, 2026 at 12:23PM](https://twitter.com/undefinedKi/status/2080992300893675775)
