from src.social_network import SocialNetwork
from src.edge_notations.character_mapping_notation import CharacterMappingNotation
from pprint import pprint
import toml
import networkx

f = """
[play]
title = "Some Title"
author = "Some Author"

[characters]
Isabella = { gender = "female", archetype = "innamorati" }
Flavio = { gender = "male", archetype = "innamorati" }
Pantalone = { gender = "male", archetype = "vecchi" }

[network]
weighted = true
directed = true

[edges.act1.scene1]
Isabella.Pantalone = {type = "hit", weight = 1}
Isabella.Flavio = {type = "kissed", weight = 4}
Flavio.Pantalone = {type = "hit", weight = 3}

[edges.act2.scene1]
Isabella.Pantalone = {type = "hit", weight = 1}
Isabella.Flavio = {type = "kissed", weight = 4}
Flavio.Pantalone = {type = "hit", weight = 3}
"""

s = SocialNetwork(f)
pprint(list(s.get_edge_list()))
