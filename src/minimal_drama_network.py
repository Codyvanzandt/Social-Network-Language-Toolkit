from src.sdl_tools.sdl_document import SDLDocument


class DramaNetwork:
    def __init__(self, data):
        self._doc = SDLDocument(data)
        self.data = self._doc.data

    def __getitem__(self, key):
        return self.data[key]

    def to_graph(
        self, directed=False, multigraph=True, equal_func=None, combine_func=None
    ):
        pass

    def to_subgraph(
        self,
        divisions=None,
        characters=None,
        edges=None,
        character_data=None,
        edge_data=None,
    ):
        pass
