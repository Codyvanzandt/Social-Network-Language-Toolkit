from src.dnl_tools.dnl_document import DNLDocument
from src.dnl_tools.dnl_to_graph import dnl_doc_to_graph
from src.utils.general_utils import convert_to_container
from src.utils.edge_utils import combine_all_edges, edges_equal, combine_edges
from src.utils.networkx_utils import get_subgraph, new_graph_from_edges


class DramaNetwork:
    def __init__(self, data):
        self.doc = DNLDocument(data)

    def __getitem__(self, key):
        return self.doc.data[key]

    def to_graph(self, directed=False):
        return dnl_doc_to_graph(self.doc, directed=directed)

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

    def to_combined_graph(self, directed=False, equal_func=None, combine_func=None):
        old_graph = self.to_graph(directed=directed)
        equal_func = equal_func if equal_func is not None else edges_equal
        combine_func = combine_func if combine_func is not None else combine_edges
        new_edges = combine_all_edges(
            old_graph.edges(data=True), equal_func, combine_func
        )
        return new_graph_from_edges(old_graph, new_edges)

    def to_string(self):
        return self.doc.to_string()

    def to_file(self, file_path):
        with open(file_path, "w") as output_file:
            output_file.write(self.to_string())
