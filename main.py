from src.drama_network import DramaNetwork
from src.converters.edge_list_converter import convert_to_edge_list
from src.converters.networkx_converter import convert_to_networkx
from pprint import pprint
import toml
import yaml

dn = DramaNetwork("examples/fake_play")
for edge in dn.to_edge_list(play_data=True, division_data=True):
    pprint(edge)
