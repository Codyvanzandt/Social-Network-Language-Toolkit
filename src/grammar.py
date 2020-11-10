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

edge : ( (name edge_mark name [":" value]) | time_mark )
edge_mark : "-" name? "-"
time_mark : "@" time_value
time_value : /[A-Za-z0-9:_]+/

section : "#" name ( pair* | edge*)
document: section*

%import common.CNAME
%import common.SIGNED_NUMBER
%import common.WS
%ignore WS
"""
