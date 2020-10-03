from lark import Lark, Transformer
from collections import ChainMap


class TreeToDict(Transformer):
    def space(self, children):
        return " "
    def number(self, children):
        (n,) = children
        return float(n)
    def name(self, children):
        return "".join(children)
    def true(self, children):
        return True
    def false(self, children):
        return False
    def list(self, children):
        return list(children)
    def dict(self, children):
        return dict(children)
    def pair(self, children):
        return tuple(children)
    def directed_edge(self, children):
        return "".join( ("-",) + tuple(children) + (">",) )
    def undirected_edge(self, children):
        return "".join( ("-",) + tuple(children) + ("-",) )
    def edge(self, children):
        num_children = len(children)
        if num_children == 3:
            return tuple(children) + (dict(),)
        elif num_children == 4:
            return tuple(children)
        else:
            raise ValueError(f"edge {children} improperly formatted")
    def section(self, children):
        section_name, *section_data = children
        if section_name == "edges":
            return { section_name : tuple(section_data) }
        else:
            return { section_name : dict(section_data) }
    def document(self, children):
        return dict(ChainMap(*children))

        
        

snl_parser = Lark(r"""
    ?value: dict
      | list
      | pair
      | number
      | name
      | true
      | false

    space : (" " | /\t/)+

    number : SIGNED_NUMBER
    name : CNAME (space CNAME)*
    true : "true"
    false : "false"

    list : "[" [value ("," value)*] "]"
    dict : "{" [pair ("," pair)*] "}"
    pair : name ":" value

    edge : name (directed_edge | undirected_edge) name [":" value]
    directed_edge : "-" name? ">"
    undirected_edge : "-" name? "-"

    document: section*
    section : "#" name ( pair* | edge*)

    %import common.CNAME
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS

    """, start='document')

doc = r"""# play
title : Some Title
author : Some Author

# node definitions
Isabella : {gender : female, archetype : innamorati}
Flavio : {gender : male, archetype : innamorati}
Pantalone : {gender : male, archetype : vecchi }

# edge definitions
KISSED : {type : kissed}
HIT : {type : hit}


# edges
Isabella -> Flavio : { type : kissed }
Isabella -- Pantalone : { type : hit }
Isabella -KISSED> Flavio
Flavio -HIT- Pantalone
"""

tree = snl_parser.parse(doc)
print( TreeToDict().transform(tree) )