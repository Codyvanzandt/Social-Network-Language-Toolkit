# Social Drama
## A (Work-in-Progress) Tool for Literary Network Analysis

Notes:
1. You're working in the minimal branch. The original branch was a series of costly mistakes.
2. You've decided that "#sections" are a good idea, but "##subsections" aren't. Section names are arbitrary, with a few exceptions (node/edge definitions).
3. You've decided to let people define their own edge definitions in the "#edge definitions" section.
4. You've decided to let folks load in edge and node definitions from other files.
5. You've decided to let folks define when an edge happened with "@act1, scene1" syntax
6. You've decided to go ahead and implement node aliases.

Here's an example...

<pre>
# play
author : Some Author
title : Some Title

# node definitions
Alice : {type: 1, size:4, alias: A}
Bob : {type : 2, size:3, alias: B}
Charlie : {type : 3, size: 2, alias: C}

# edge definitions
- : {directedness: undirected}
-> : {directedness: directed}

# edges
@ act1, scene1
A->B
A,B -> C
A-C
</pre>
