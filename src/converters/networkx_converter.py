import networkx

class NetworkxConverter:

    def __init__(self, social_network):
        self.social_network = social_network

    def convert(self):
        graph = self.get_empty_graph()
        graph.add_character_data()
        return graph

    def add_character_data(self, graph):
        for character_name, character_data in self.social_network.data.get("characters", dict()).items():
            graph.add_node(character_name, **character_data)

    def add_edge_data(self,graph):
        pass

    def get_empty_graph(self):
        directed = self.social_network_data.get("network", dict()).get("directed", False)
        play_data = self.get_play_data()
        if directed == True:
            return networkx.MultiDiGraph(**play_data)
        elif directed == False:
            return networkx.MultiGraph(**play_data)
        else:
            raise ValueError("The value network.directed must be either `true` or `false`")

    def get_play_data(self):
        return self.social_network.data.get("play", dict())