from src.sdl_tools import load_sdl_file, parse_sdl_file
from pprint import pprint
import toml
import yaml

pprint(load_sdl_file("examples/fake_play"))

# #
# doc = parse_sdl_file("examples/fake_play")
# play = doc.section('play').elements()[0]
# print(play)
# print(dir(play))
