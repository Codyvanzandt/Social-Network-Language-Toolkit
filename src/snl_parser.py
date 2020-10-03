from lark import Lark, Transformer
from pprint import pprint


class TreeToDict(Transformer):
    def number(self, children):
        (n,) = children
        return float(n)
    def true(self, children):
        return True
    def false(self, children):
        return False
    def space(self, children):
        return " "
    def CNAME(self, children):
        return str(children)
    def edge(self, children):
        return "-".join(children)
    def words(self, children):
        return "".join(children)
    def dict(self, children):
        return dict(children)
    def pair(self, children):
        return tuple(children)
    def dict_pair(self, children):
        return tuple(children)
    def section_symbol(self, children):
        return "#"
    def section_marker(self, children):
        return "".join(children)
    def section_header(self, children):
        return " ".join(children)
    # def section(self, children):
    #     section_name, *section_data = children
    #     return {section_name : dict(section_data)}
    # def document(self, children):
        

snl_parser = Lark(r"""
    ?value: map
      | number
      | name
      | true
      | false

    number : SIGNED_NUMBER
    name : CNAME (space+ CNAME)*
    true : "true"
    false : "false"

    space: " "
    doublespace : "  "
    newline : /\n/

    document: section*
    section : name newline doublespace
    map : name space? ":" space? value newline?

    %import common.CNAME
    %import common.SIGNED_NUMBER

    """, start='document')

doc = r"""play
  title : Some Title
  author : Some Author

characters
  Isabella
    gender : female
    archetype : innamorati
  Flavio 
    gender : male
    archetype : innamorati 
  Pantalone
    gender : male
    archetype : vecchi

edges
  act1
    scene1
      Isabella-Pantalone
        weight : 1
        type : hit
      Isabella-Flavio
        weight : 2
        type : kissed 
      Flavio-Pantalone
        weight : 3
        type : hit  
    scene1
      Isabella-Pantalone
        weight : 1
        type : hit
      Isabella-Flavio
        weight : 2
        type : kissed 
      Flavio-Pantalone
        weight : 3
        type : hit
"""
print(repr(doc))

tree = snl_parser.parse(doc)
print(tree.pretty())
# pprint( TreeToDict().transform(tree) )