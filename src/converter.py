from src.parser import Parser
from src.transformers import TreeToDict, EdgesToAugmentedEdges, DictToGraph, GraphToString


class Converter:
    def to_graph(self, data, directed=True):
        raw_stl = self.load_snl(data)
        stl_tree = Parser.parse(raw_stl)
        stl_dict = EdgesToAugmentedEdges().transform(TreeToDict().transform(stl_tree))
        return DictToGraph().transform(stl_dict, directed=directed)

    def to_string(self, graph):
        return GraphToString().transform(graph)

    def load_snl(self, data):
        try:
            with open(data, "r") as data_file:
                loaded_data = data_file.read()
        except (OSError, FileNotFoundError):
            try:
                loaded_data = data.read()
            except AttributeError:
                loaded_data = data
        return loaded_data
