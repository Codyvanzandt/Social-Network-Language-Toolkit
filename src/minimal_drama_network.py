from src.sdl_tools.sdl_document import SDLDocument
from src.sdl_tools.sdl_to_graph import sdl_doc_to_graph
from src.utils.general_utils import convert_to_container
from src.utils.edge_utils import combine_all_edges, edges_equal, combine_edges
from src.utils.networkx_utils import get_subgraph, new_graph_from_edges, get_divisions


class DramaNetwork:
    def __init__(self, data):
        self._doc = SDLDocument(data)
        self.data = self._doc.data

    def __getitem__(self, key):
        return self.data[key]

    def to_graph(self, directed=False):
        return sdl_doc_to_graph(self._doc, directed=directed)

    def to_subgraph(
        self,
        directed=False,
        divisions=None,
        characters=None,
        edges=None,
        character_data=None,
        edge_data=None,
    ):
        divisions = convert_to_container(divisions)
        characters = convert_to_container(characters)
        edges = convert_to_container(edges, nested=True)

        subgraph = get_subgraph(
            self.to_graph(directed=directed),
            divisions=divisions,
            nodes=characters,
            edges=edges,
            node_data=character_data,
            edge_data=edge_data,
        )
        return subgraph

    def to_reduced_graph(self, directed=False, equal_func=None, combine_func=None):
        old_graph = self.to_graph(directed=directed)
        equal_func = equal_func if equal_func is not None else edges_equal
        combine_func = combine_func if combine_func is not None else combine_edges
        new_edges = combine_all_edges(old_graph.edges(data=True), equal_func, combine_func)
        return new_graph_from_edges(old_graph, new_edges)