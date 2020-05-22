from src.social_network.social_network import SocialNetwork
from src.edge_notations.character_mapping_notation import CharacterMappingNotation
from pprint import pprint

s = SocialNetwork("examples/fake_play.yaml")
pprint(s.data["edges"])
e = CharacterMappingNotation(s.data["edges"])
pprint(e.edges)
