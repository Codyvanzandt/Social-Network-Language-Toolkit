import yaml
from pprint import pprint

with open("examples/fake_play.yaml", "r") as fake_play_file:
    fake_play = yaml.load(fake_play_file, Loader=yaml.FullLoader)

pprint(fake_play)
