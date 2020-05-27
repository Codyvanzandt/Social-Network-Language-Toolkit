import networkx
from src.converters.edge_list_converter import convert_to_edge_list

def convert_to_networkx(social_network):
    graph = _get_empty_graph(social_network)
    _add_play_data(social_network, graph)
    _add_character_data(social_network, graph)
    _add_edge_data(social_network, graph)
    return graph

def _get_empty_graph(social_network):
    network_data = social_network.data.get("network", dict())
    directed = network_data.get("directed", False)
    if directed == True:
        return networkx.MultiDiGraph()
    elif directed == False:
        return networkx.MultiGraph()
    else:
        raise ValueError(
            "The value network.directed must be either `true` or `false`"
        )

def _add_play_data(social_network, graph):
    play_data = social_network.data.get("play", dict())
    for play_data_key, play_data_value in play_data.items():
        graph.graph[play_data_key] = play_data_value

def _add_character_data(social_network, graph ):
    character_data = social_network.data.get("characters", dict())
    for character_name, character_data in character_data.items():
        graph.add_node(character_name, **character_data)

def _add_edge_data(social_network, graph):
    edges = convert_to_edge_list(social_network)
    graph.add_edges_from(edges)