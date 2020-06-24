import networkx


def convert_to_networkx(social_network, directed, play_data=False, division_data=False):
    graph = _get_empty_graph(directed)
    _add_play_data(social_network, graph)
    _add_character_data(social_network, graph)
    _add_edge_data(social_network, graph, play_data, division_data)
    return graph


def _get_empty_graph(directed):
    if directed == True:
        return networkx.MultiDiGraph()
    elif directed == False:
        return networkx.MultiGraph()
    else:
        raise ValueError("The value for `directed` must be one of: (True, False)")


def _add_play_data(social_network, graph):
    play_data = social_network._data.get("play", dict())
    for play_data_key, play_data_value in play_data.items():
        graph.graph[play_data_key] = play_data_value


def _add_character_data(social_network, graph):
    character_data = social_network._data.get("characters", dict())
    for character_name, character_data in character_data.items():
        graph.add_node(character_name, **character_data)


def _add_edge_data(social_network, graph, play_data, division_data):
    edges = social_network._doc.data.get("edges", list())
    graph.add_edges_from(edges)
