grammar = r"""
// "value" supports nested data types inside each other (e.g., a list can contain dicts)
?value: dict
      | list
      | pair
      | SIGNED_NUMBER
      | name
      | true
      | false

// constants
name : /[\w ,]+/
true : "true"
false : "false"

// data structures
list : "[" [value ("," value)*] "]"
dict : "{" [pair ("," pair)*] "}"
pair : name ":" value

// markers
edge : ( (name edge_mark name [":" value]) | time_mark )
edge_mark : "-" name? "-"
time_mark : "@" time_value
time_value : /[A-Za-z0-9:_]+/

// sections
section : "#" name ( pair* | edge*)
document: section*

%import common.CNAME
%import common.SIGNED_NUMBER
%import common.WS
%ignore WS
"""
