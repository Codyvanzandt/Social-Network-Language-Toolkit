# Social Network Language and Toolkit
The Social Network Lanaguage (SNL) is an expressive, intuitive, and aesthetically pleasing markup langugage built to make manual social network transcription as painless as possible.

The SNL-Toolkit combines two Python-language tools for working with SNL documents: the converter and the writer. The converter turns SNL documents into networkx graphs and vice-versa; the writer provides a way to create SNL documents using Python.

# The State of the Project

Both the Social Network Language and its Toolkit are currently under active development.
They both are changing rapidly, and as such, are not yet publicly available.

## The State of the Language 

The language currently supports all of its core features (nodes and edge transcription, arbitrary metadata transcription, temporal markers), although the exact expression of those features is still subject to change.

Further work is neccessary on name-handling, e.g., ensuring that "Tom Jones", "Tom-Jones", and "Tom_Jones" are all valid expressions.

## The State of the Converter

The converter correctly converts SDL documents to networkx graphs insofar as the nodes, edges, and arbitrary metadata are correctly converted. 

The converter does not currently convert networkx graphs to SDL documents.

## The State of the Writer

Design and development for the writer are not yet under way.

# Installing the Social Network Language Toolkit

The Toolkit is currently unavailable for installation. It will soon be pip-installable in an experimental form.

# Using the Social Network Langauge and Toolkit

## The Language

Languages guides will not be written until the langauge is finalized. Below is a example of an SNL document written in the current form of the language:

```
# play
title : An Exceedingly Brief Love Story
author : Author MacAuthor

# node definitions
Isabella : {gender : female, archetype : lover}
Flavio : {gender : male, archetype : lover}
Pantalone : {gender : male, archetype : old man }

# edge definitions
kissed : {type : kissed}
hit : {type : hit}
spoke : {type: conversation}

# edges
@ act1
Isabella -spoke- Flavio
Isabella -spoke- Pantalone
@ act2
Isabella -kissed- Flavio
Pantalone -hit- Flavio
@ act3
Isabella -spoke- Pantalone
Flavio -spoke- Pantalone
Flavio -kissed- Isabella
```

## The Toolkit

Guides for the toolkit will not be written until the toolkit's API is finalized.


