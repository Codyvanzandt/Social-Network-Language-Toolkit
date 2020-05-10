# Getting Started with DramaYAML and SocialDrama

## Table of Contents
[Getting Started with DramaYAML](#getting-started-with-dramayaml)
[Getting Started with SocialDrama](#getting-started-with-socialdrama)

## Getting Started with DramaYAML

### The Simplest Example

Getting started with DramaYAML is simple. You can start with a tiny portion of the syntax and add more as necessary.

To begin, we will represent a network with three edges: Alice-Bob, Bob-Charlie, and Charlie-Alice.

```yaml
edges:
  Alice: Bob
  Bob: Charlie
  Charlie: Alice
```

It is necessary to include the `edges:` marker and indent each edge underneath that marker with a fixed number of spaces. Any number of spaces will work as long as you are consistent. Tabs are prohibited.

Since we did not specify if the edges are weighted or directed, they are assumed to be unweighted and undirected. Let's see how we can change that.

### Adding Edge Weights and Edge Directions

We can configure our network to be weighted and directed by indenting `weighted:` and `directed:` markers underneath a `network:` marker.

If `directed:` is set to `true`, all edges are assumed to be directed. 
This means, for example, that the edge `Alice: Bob` creates an edge from Alice to Bob, but not from Bob to Alice.

If `weighted:` is set to `true`, all edges are assumed to have a default weight of `1`. 
We can also specify weights on a per-edge basis by indenting `weight:` markers underneath particular edges.

In the following example, all edges are directed and the Alice-Bob edge has a weight of `2`. 
The Bob-Charlie and Charlie-Alice edges are, by default, assumed to have a weight of `1`.

```yaml
network:
  weighted: true
  directed: true

edges:
  Alice: Bob
    weight: 2
  Bob: Charlie
  Charlie: Alice
```






