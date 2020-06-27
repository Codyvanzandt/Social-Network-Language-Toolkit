import networkx
import abc


class AbstractNetworkxConverter(metaclass=abc.ABCMeta):
    def __init__(self, obj):
        self.obj = obj

    def to_networkx(self, directed=False, embed_play=False):
        new_graph = self.get_empty_graph(directed=directed)

        play_data = self.get_play_data()
        character_data = self.get_character_data()
        edge_data = self.get_edge_data(embed_play=embed_play)

        self.add_play_data(new_graph, play_data)
        self.add_character_data(new_graph, character_data)
        self.add_edge_data(new_graph, edge_data)
        return new_graph

    @staticmethod
    def get_empty_graph(directed):
        if directed == True:
            return networkx.MultiDiGraph()
        elif directed == False:
            return networkx.MultiGraph()
        else:
            raise ValueError("The value for `directed` must be one of: (True, False)")

    @staticmethod
    def add_play_data(graph, play_data):
        for play_data_key, play_data_value in play_data.items():
            graph.graph[play_data_key] = play_data_value

    @staticmethod
    def add_character_data(graph, character_data):
        for character_name, character_data in character_data.items():
            graph.add_node(character_name, **character_data)

    @staticmethod
    def add_edge_data(graph, edge_data):
        graph.add_edges_from(edge_data)

    @abc.abstractmethod
    def get_play_data(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_character_data(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_edge_data(self, embed_play=False):
        raise NotImplementedError()


class SDLConverter(AbstractNetworkxConverter):
    def get_play_data(self):
        return self.obj.data.get("play", dict())

    def get_character_data(self):
        return self.obj.data.get("characters", dict())

    def get_edge_data(self, embed_play=False):
        if not embed_play:
            yield from self.obj.data.get("edges", list())
        else:
            play_data = self.get_play_data()
            for source, target, data in self.obj.data.get("edges", list()):
                new_data = {k: v for d in (data, play_data) for k, v in d.items()}
                yield (source, target, new_data)


class DramaNetworkConverter(SDLConverter):
    def __init__(self, obj):
        self.obj = obj._doc
