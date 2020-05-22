from src.social_network.social_network import SocialNetwork
from src.edge_notations.character_mapping_notation import CharacterMappingNotation
from src.edge_notations.enter_exit_notation import EnterExitNotation
from pprint import pprint

s = SocialNetwork("examples/fake_play.yaml")
e = EnterExitNotation(s.data["edges"], directed=False)
pprint(e.edges)
