# Social Drama
## A (Work-in-Progress) Tool for Literary Network Analysis

Notes:
1. You're working in the minimal branch. The original branch was a series of costly mistakes.
2. You've decided that "#sections" are a good idea, but "##subsections" aren't.
3. You've decided to let people define their own edge definitions in the "#edge definitions" section.
4. You've decided to let folks load in edge and node definitions from other files.
5. You've decided to let folks define when an edge happened with "@act1, scene1" syntax

Here's an example...

<pre>
# play
author : Some Author
title : Some Title

# node definitions
A : {type: 1, size:4}
B : {type : 2, size:3}
C : {type : 3, size: 2}

# edge definitions
- : {directedness: undirected}
-> : {directedness: directed}

# edges
A->B
A,B -> C
A-C
</pre>
