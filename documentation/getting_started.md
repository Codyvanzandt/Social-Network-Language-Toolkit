# Getting Started with DramaYAML

This section contains two different tutorials on DramaYAML, each assuming a different level of familiarity with YAML, the markup language on which DramaYAML is built.

If you are comfortable with YAML and would like a quick but complete overview of DramaYAML's features, check out the [Annotated Example](#annotated-example).

If you not comfortable with YAML, check out the [DramaYAML Tutorial](#dramayaml-tutorial) to learn both YAML and DramaYAML from the ground up.

In either case, you may also wish to check out the [*A Midsummer Night's Dream* example](#a-midsummer-night's-dream-example) to see what a real, full-length play looks like in DramaYAML. 

## Table of Contents
- [Annotated Example](#annotated-example)
- [DramaYAML Tutorial](#dramayaml-tutorial)
  - [Introducing YAML Syntax](#introducing-yaml-syntax)
  - [Adding Play Data](#adding-play-data)
  - [Adding Character Data](#adding-character-data)
  - [Adding Character Aliases](#adding-character-aliases)
  - [Adding Edge Data](#adding-edge-data)
- [A Midsummer Night's Dream Example](#a-midsummer-night's-dream-example)
  
## Annotated Example

```yaml
# Specify play data underneath the `play` key. 
# There are no required keys, although `title` and `author` are recommended.
play:
  title: A Very Good Play                   # You can use unquoted, single-quoted, or double-quoted strings
  author: "Alex Arthur"                    
  arbitrary_string: 'Dumbledore'
  arbitrary_boolean: true                   # Booleans
  arbitrary_int: 42                         # Integers
  arbitrary_float: 3.14                     # Floating-point number
  arbitrary_array: [Porthos, Athos, Aramis] # Arrays


# Specify network data underneath the `network` key.
# There are no required keys, although `weighted` and `directed` are recommended.
# If you do not include the `weighted` key, then the network is assumed to be unweighted.
# If you do not include `directed` key, then the network is assumed to be undirected.
network:
  weighted: true                   
  directed: true


# Specify character data underneath the `characters` key.
# There are no required keys, although `alias` is recommended.
characters:
  Alice: 
    occupation: engineer
    protagonist: true
    alias: A  # For convenience, you can assign and use an alias in place of a character name.
  Bob:                      
    occupation: carpenter       
    protagonist: false
    alias: B
  Charlie:                 
    occupation: doctor
    protagonist: true
    alias: C


# Specify edges underneath the `edges` key.
# There are a number edge notations, each with its own tradeoff between explicitness and labor intensiveness.

# Character Mapping Notation is the most explicit and most labor-intensive notation.
edges: 
    Alice:      
      Bob: 1        # Alice-Bob, weight=1 
      Charlie: 1    # Alice-Charlie, weight=1
    Charlie:
      Bob: 1        # Charlie-Bob, weight=1


# Character Array Notation is moderately explicit and moderately labor-intensive.
# It creates an edge between every pair of characters in an array.
# In a undirected network, this creates an edge between every combination of two characters.
# In a directed network, this creates an edge between every permutation of two characters.
# In a weighted network, each edge will be given a weight of 1.
# Note: you must prefix each new array with a `-` (dash).
edges:
  - [Alice, Bob, Charlie] # In an undirected network, this creates three edges: 
                          # Alice-Bob, Alice-Charlie, Bob-Charlie.
                          # In a directed network, this creates six edges:
                          # Alice-Bob, Bob-Alice, Alice-Charlie, Charlie-Alice, Bob-Charlie, Charlie-Bob.  


# Enter-Exit Notation is the least explicit and least labor-intensive notation.
# In each scene, you specify who has exited and entered from the previous scene.
# An edge is created between every pair of characters who remain.
# In a undirected network, this creates an edge between every combination of two characters.
# In a directed network, this creates an edge between every permutation of two characters.
# In a weighted network, each edge will be given a weight of 1.

edges:
  - [+Alice, +Bob,]     # Alice and Bob enter. Undirected edges: Alice-Bob
  - [-Bob, +Charlie]    # Bob exits, Charlie enters. Undirected edges: Alice-Charlie
  - [+Bob]              # Bob enters. Undirected edges: Alice-Bob, Alice-Charlie, Bob-Charlie


# Using Character Aliases
# You can use character aliases with any edge notation.
# For example, if we assume Alice is alised to `A`, Bob to `B`, and Charlie to `C`, we can take this...

edges: 
  Alice:
    Bob: 1
    Charlie: 2
  Charlie:
    Bob: 3

# ...and rewrite it as this:

edges:
    A:             
      B: 1        
      C: 2
    C:
      B: 3 
      
# You can also divide up edges into Acts and Scenes.
# Your acts and scenes can be named anything you like, although `Act1`, `Scene1`, etc. is a useful convention.
edges:
  Act1: 
    Scene1:
      Alice:
        Bob: 1
        Charlie: 2
    Scene2:
      Charlie:
        Bob: 3

# You can add as many act and scene sub-divisions as you like.
edges:
    Act1:
      Scene1:
        SubScene1:
          SubSubScene1:
            Alice:
              Bob: 1
              Charlie: 2
          SubSubScene2:
            Charlie:
              Bob: 3
```

## DramaYAML Tutorial

### Introducing YAML Syntax

### Adding Play Data

We can add play metadata underneath the `play:` marker. 
We can use any markers we wish, although it is recommended that we include `title` and `author` markers.

```yaml
play:
  title: A Very Good Play
  author: Alex Author
  any_piece_of_data_you_like: isn't that nifty? 

network:
  weighted: true
  directed: true

edges:
  Alice: Bob
    weight: 2
  Bob: Charlie
  Charlie: Alice
```

### Adding Character Data

We can add arbitrary character metadata underneath a `characters:` marker.

```yaml
play:
  title: A Very Good Play
  author: Alex Author
  any_piece_of_data_you_like: isn't that nifty? 

characters:
  Alice:
    occupation: engineer
    major_character: true
  Bob:
    occupation: teacher
    major_character: false
  Charlie:
    occupation: carpenter
    major_character: true

network:
  weighted: true
  directed: true

edges:
  Alice: Bob
    weight: 2
  Bob: Charlie
  Charlie: Alice
```

### Adding Character Aliases

We can speed up the process of transcribing our social network by assigning short aliases to each of our characters.

To assign the alias `A` to Alice, we add `&A` in front of Alice's name underneath the `characters:` marker.

Transforming this:

```yaml
characters:
  Alice:
    occupation: engineer
    major_character: true
```

Into this:

```yaml
characters:
  &A Alice:
    occupation: engineer
    major_character: true
```

We can now use Alice's alias anywhere we might have used "Alice" by prefixing her alias with an `*` (asterix).

In this example, we'll also go ahead and assign the aliases `B` and `C` to Bob and Charlie, respectively.

```yaml
play:
  title: A Very Good Play
  author: Alex Author
  any_piece_of_data_you_like: isn't that nifty? 

characters:
  &A Alice:
    occupation: engineer
    major_character: true
  &B Bob:
    occupation: teacher
    major_character: false
  &C Charlie:
    occupation: carpenter
    major_character: true

network:
  weighted: true
  directed: true

edges:
  *A: *B
    weight: 2
  *B: *C
  *C: *A
```

### Adding Edge Data

In our first example, we will add three undirected, unweighted edges: Alice-Bob, Bob-Charlie, and Charlie-Alice.

```yaml
edges:
  Alice: Bob
  Bob: Charlie
  Charlie: Alice
```

It is necessary to include the `edges:` marker and indent each edge underneath that marker with a fixed number of spaces. Any number of spaces will work as long as you are consistent. Tabs are prohibited.

Since we did not specify if the edges are weighted or directed, they are assumed to be unweighted and undirected. Let's see how we can change that.

We can configure our network to be weighted and directed by indenting `weighted:` and `directed:` markers underneath a `network:` marker.

If `directed:` is set to `true`, all edges are assumed to be directed. 
This means, for example, that the edge `Alice: Bob` creates an edge from Alice to Bob, but not from Bob to Alice.

If `weighted:` is set to `true`, all edges are assumed to have a default weight of `1`. 
We can also specify weights on a per-edge basis by indenting `weight:` markers underneath particular edges.

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

In this example, all edges are directed and the Alice-Bob edge has a weight of `2`. 
The Bob-Charlie and Charlie-Alice edges are, by default, assumed to have a weight of `1`.


## A Midsummer Night's Dream Example