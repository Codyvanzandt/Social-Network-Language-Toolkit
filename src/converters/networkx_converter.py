import networkx
from src.converters.edge_list_converter import convert_to_edge_list


def convert_to_networkx(social_network, directed, multigraph, play_data=False, division_data=False):
    graph = _get_empty_graph(social_network, directed, multigraph)
    _add_play_data(social_network, graph)
    _add_character_data(social_network, graph)
    _add_edge_data(social_network, graph, play_data, division_data)
    return graph


def _get_empty_graph(social_network, directed, multigraph):
    if directed and multigraph:
        return networkx.MultiDiGraph()
    elif directed and not multigraph:
        return networkx.DiGraph()
    elif not directed and multigraph:
        return networkx.MultiGraph()
    elif not directed and not multigraph:
        return networkx.Graph()
    else:
        raise ValueError("The values for `directed` and `multigraph` must be one of: (true, false) ")


def _add_play_data(social_network, graph):
    play_data = social_network.data.get("play", dict())
    for play_data_key, play_data_value in play_data.items():
        graph.graph[play_data_key] = play_data_value


def _add_character_data(social_network, graph):
    character_data = social_network.data.get("characters", dict())
    for character_name, character_data in character_data.items():
        graph.add_node(character_name, **character_data)


def _add_edge_data(social_network, graph, play_data, division_data):
    edges = convert_to_edge_list(social_network, play_data, division_data)
    if isinstance(graph, ( networkx.MultiGraph, networkx.MultiDiGraph ) ):
        graph.add_edges_from(edges)
    else:
        _add_nonmulti_edge_data(graph, edges)

def _add_nonmulti_edge_data(graph, edges):
    for source, target, edge_data in edges:
        if graph.has_edge(source, target):
            old_weight = graph.get_edge_data(source, target).get("weight", 1)
            incoming_weight = edge_data.get("weight", 1)
            graph[source][target]["weight"] = old_weight + incoming_weight
        else:
            graph.add_edge(source, target, **edge_data)