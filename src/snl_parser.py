from lark import Lark, Transformer
from collections import ChainMap


class TreeToDict(Transformer):
    def space(self, children):
        return " "

    def SIGNED_NUMBER(self, children):
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

    def edge(self, children):
        num_children = len(children)
        if num_children == 3:
            return tuple(children) + (dict(),)
        elif num_children == 4:
            return tuple(children)
        else:
            raise ValueError(f"edge {children} improperly formatted")

    def edge_mark(self, children):
        return "-" + "".join(children) + "-"

    def section(self, children):
        section_name, *section_data = children
        if section_name == "edges":
            return {section_name: tuple(section_data)}
        else:
            return {section_name: dict(section_data)}

    def document(self, children):
        return dict(ChainMap(*children))


snl_parser = Lark(
    r"""
    ?value: dict
      | list
      | pair
      | SIGNED_NUMBER
      | name
      | true
      | false

    space : (" " | /\t/)+
    name : CNAME (space CNAME)*
    true : "true"
    false : "false"

    list : "[" [value ("," value)*] "]"
    dict : "{" [pair ("," pair)*] "}"
    pair : name ":" value

    edge : name edge_mark name [":" value]
    edge_mark : "-" name? "-"

    section : "#" name ( pair* | edge*)
    document: section*

    %import common.CNAME
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS

    """,
    start="document",
)

doc = r"""# play
title : Some Title
author : Some Author

# node definitions
Isabella : {gender : female, archetype : innamorati}
Flavio : {gender : male, archetype : innamorati}
Pantalone : {gender : male, archetype : vecchi }

# edge definitions
kissed : {type : kissed}
hit : {type : hit}

# edges
Isabella -- Flavio : { type : kissed }
Isabella -kissed- Flavio : {weight : 1}
Flavio -hit- Pantalone
"""

tree = snl_parser.parse(doc)
print(TreeToDict().transform(tree))
