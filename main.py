from src.social_network import SocialNetwork
from pprint import pprint
import toml
import yaml

with open("examples/fake_play.yaml","r") as fake_play:
    pprint(yaml.load( fake_play, Loader=yaml.FullLoader))