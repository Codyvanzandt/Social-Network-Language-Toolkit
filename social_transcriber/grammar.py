grammar = r"""
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
"""
