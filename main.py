from src.drama_network import DramaNetwork
from src.sdl_tools.sdl_serializer import serialize_divisions
from src.sdl_tools.sdl_parser import parse_sdl_file
from pprint import pprint

doc = parse_sdl_file("examples/fake_play")
pprint(serialize_divisions(doc))
