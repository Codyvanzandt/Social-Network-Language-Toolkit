from src.social_network.social_network import SocialNetwork
from pprint import pprint
import toml
import networkx

s = SocialNetwork("examples/fake_play.toml")
pprint(s.data)
