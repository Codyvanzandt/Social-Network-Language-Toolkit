from src.sdl_tools.sdl_api import load_sdl_string, load_sdl_file
from src.converters.edge_list_converter import convert_to_edge_list
from src.converters.networkx_converter import convert_to_networkx
from src.converters.string_converter import convert_to_string
from src.converters.sdl_file_converter import convert_to_file
from src.utils.networkx_utils import get_subgraph
from src.utils.drama_network_utils import get_subgraph_data
from pprint import pformat
import copy


class DramaNetwork:
    def __init__(self, data=None, directed=False):
        self._data = self._load_sdl_data(data) if data else dict()
        self._graph = convert_to_networkx(
            self, directed=directed, play_data=True, division_data=True
        )

    def __getattr__(self, name):
        try:
            return self._data[name]
        except IndexError:
            return getattr(self._graph, name)
        
    def get(self, name, default=None):
        return self._data.get(name, default=default)

    def to_edge_list(self, play_data=False, division_data=False):
        return list(
            convert_to_edge_list(self, play_data=play_data, division_data=division_data)
        )

    def subgraph(
        self,
        division=None,
        characters=None,
        edges=None,
        character_data=None,
        edge_data=None,
    ):
        subgraph = get_subgraph(
            self._graph,
            division=division,
            nodes=characters,
            edges=edges,
            node_data=character_data,
            edge_data=edge_data,
        )
        subgraph_data = get_subgraph_data(self, subgraph)
        subgraph_drama_network = DramaNetwork()
        subgraph_drama_network._graph = subgraph
        subgraph_drama_network._data = subgraph_data
        return subgraph_drama_network

    def to_string(self):
        return convert_to_string(self)

    def to_file(self, path):
        return convert_to_file(self, path)

    def _load_sdl_data(self, data):
        try:
            return load_sdl_file(data)
        except (OSError, FileNotFoundError):
            return load_sdl_string(data)

    def __str__(self):
        return f"{self.__class__.__name__}({pformat(self._data)})"

    def __repr__(self):
        title = self._data.get("play", dict()).get("title", str())
        return f"{self.__class__.__name__}({title})"
