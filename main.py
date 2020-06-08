from src.drama_network import DramaNetwork
from src.converters.edge_list_converter import convert_to_edge_list
from src.converters.networkx_converter import convert_to_networkx
from src.converters.string_converter import convert_to_string
from src.sdl_tools.enter_exit_edge_serializer import serialize_enter_exit_edges
from pprint import pprint
from src.sdl_tools.sdl_parser import parse_sdl_file
from src.sdl_tools.sdl_serializer import serialize_edges_section
import toml
import yaml

dn = DramaNetwork("examples/fake_play")

act1 = dn.to_networkx_subgraph(directed=False, division="act1", nodes=["Isabella"], edge_data={"type":"kissed"})
pprint(list(act1.edges(data=True)))
