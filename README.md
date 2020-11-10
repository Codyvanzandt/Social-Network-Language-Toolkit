# Social Network Language and Toolkit
The Social Network Lanaguage (SNL) is an expressive, intuitive, and aesthetically pleasing markup langugage built to make manual social network transcription as painless as possible.

The SNL-Toolkit combines two Python-language tools for working with SNL documents: the Converter and the Writer. The Converter turns SNL documents into networkx graphs and vice-versa; the Writer provides a way to create SNL documents using Python.

# The State of the Project

Both the Social Network Language and its Toolkit are currently under active development.
They both are changing rapidly, and as such, are not yet suitable for anything other than experimentation.

# Installing the Social Network Language Toolkit

The Social Network Language Toolkit is installable through pip:

```
pip install snltoolkit
```

# Using the Social Network Langauge and Toolkit

## The Language

Comprehensive guides will not be written until the langauge is finalized. Below is a example of an SNL document written in the current form of the language:

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

Comprehensive guides for the toolkit will not be written until the API is finalized.

Below is a basic example that uses the Converter to convert an SDL document to a networkx graph:

```python
import snltoolkit

snl_converter = snltoolkit.Converter()

resulting_networkx_graph = snl_converter.to_graph("path/to/a/snl/document")
```

