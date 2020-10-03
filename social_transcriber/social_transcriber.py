from social_transcriber.parser import parser
from social_transcriber.transformers import TreeToDict, DictToGraph, GraphToSTL


class SocialTranscriber:
    def to_graph(self, data, directed=True):
        raw_stl = self.load_stl(data)
        stl_tree = parser.parse(raw_stl)
        stl_dict = TreeToDict().transform(stl_tree)
        return DictToGraph().transform(stl_dict, directed=directed)

    def to_string(self, graph):
        return GraphToSTL().transform(graph)

    def load_stl(self, stl_data):
        try:
            with open(stl_data, "r") as data_file:
                loaded_data = data_file.read()
        except (OSError, FileNotFoundError):
            try:
                loaded_data = stl_data.read()
            except AttributeError:
                loaded_data = stl_data
        return loaded_data


st = SocialTranscriber()

graph = st.to_graph("examples/fake_play")

print(st.to_string(graph))
