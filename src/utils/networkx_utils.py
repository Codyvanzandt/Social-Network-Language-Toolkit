import networkx
from src.utils.general_utils import (
    is_subarray,
    is_dict_subset,
    nested_dict_get,
    nested_dict_set,
)

# SUBGRAPH API


def get_subgraph(
    graph, divisions=None, nodes=None, edges=None, node_data=None, edge_data=None
):
    node_subgraph = get_node_subgraph(graph, nodes=nodes, node_data=node_data)
    edge_subgraph = get_edge_subgraph(graph, edges=edges, edge_data=edge_data)
    division_subgraph = get_division_subgraph(graph, divisions=divisions)
    intersecting_edges = (
        edge
        for edge in graph.edges(keys=True)
        if node_subgraph.has_edge(*edge)
        and edge_subgraph.has_edge(*edge)
        and division_subgraph.has_edge(*edge)
    )
    return graph.edge_subgraph(intersecting_edges).copy()


def get_node_subgraph(graph, nodes=None, node_data=None):
    """
    Given:
        nodes - an iterable of nodes
        node_data - a dict of node data
    Return:
        A shallow-copy subgraph with the given nodes.
        If node_data is specified, only nodes with matching data will be included. 
    """
    subgraph_nodes = get_nodes(graph, nodes=nodes, node_data=node_data)
    subgraph_edges = yield_edges_with_nodes(graph, subgraph_nodes)
    return graph.edge_subgraph(subgraph_edges).copy()


def get_edge_subgraph(graph, edges=None, edge_data=None):
    """
    Given:
        edges - an iterable of (source, target)
        edge_data - a dict of edge data
    Return:
        A shallow-copy subgraph with the given edges.
        If edge_data is specified, only edges with matching data will be included. 
    """
    subgraph_edges = get_edges(graph, edges=edges, edge_data=edge_data)
    return graph.edge_subgraph(subgraph_edges).copy()


def get_division_subgraph(graph, divisions):
    """
    Given:
        division - a division like "act1" or a nested division like "act1.scene1"
    Return:
        A shallow-copy subgraph with edges from the given division.
    """
    subgraph_edges = get_edges_by_division(graph, divisions=divisions)
    return graph.edge_subgraph(subgraph_edges).copy()


# DIVISION API


def get_divisions(graph):
    divisions = set()
    for s, t, division_data in graph.edges(data="divisions", default=dict()):
        nested_division = str()
        for division in division_data:
            nested_division = (
                division
                if nested_division == str()
                else f"{nested_division}.{division}"
            )
            divisions.add(nested_division)
    return tuple(sorted(divisions))


def get_empty_division_structure(graph):
    division_structure = dict()
    for _, _, edge_data in graph.edges(data=True):
        edge_divisions = edge_data.get("divisions", tuple())
        nested_dict_set(division_structure, edge_divisions, dict())
    return division_structure


# EDGES API


def get_edges_underneath_divisions(graph):
    division_structure = get_empty_division_structure(graph)
    for s, t, edge_data in graph.edges(data=True):
        edge_divisions = edge_data.get("divisions", tuple())
        current_edges = nested_dict_get(division_structure, edge_divisions)
        if current_edges == dict():
            nested_dict_set(division_structure, edge_divisions, [(s, t, edge_data)])
        else:
            nested_dict_set(
                division_structure, edge_divisions, current_edges + [(s, t, edge_data)]
            )
    return division_structure


def get_edges_by_division(graph, divisions):
    if divisions is None:
        yield from graph.edges(keys=True)
    else:
        target_divisions = {tuple(division.split(".")) for division in divisions}
        for source, target, key, edge_data in graph.edges(keys=True, data=True):
            edge_division = edge_data.get("divisions", tuple())
            if any(
                is_subarray(target_division, edge_division)
                for target_division in target_divisions
            ):
                yield (source, target, key)


def yield_edges_with_nodes(graph, nodes):
    nodes_set = set(nodes)
    for s, t, k in graph.edges(keys=True):
        if s in nodes_set or t in nodes_set:
            yield (s, t, k)


def get_edges(graph, edges=None, edge_data=None):
    target_edges = edges if edges else graph.edges()
    if not edge_data:
        yield from yield_edges(graph, target_edges)
    else:
        for s, t, k in yield_edges(graph, target_edges):
            data = graph[s][t][k]
            if is_dict_subset(edge_data, data):
                yield (s, t, k)


def yield_edges(graph, edges):
    edges_set = set(edges)
    for s, t, k in graph.edges(keys=True):
        if (s, t) in edges_set:
            yield (s, t, k)


# NODES API


def get_nodes(graph, nodes=None, node_data=None):
    target_nodes = nodes if nodes else graph.nodes()
    if not node_data:
        yield from yield_nodes(graph, target_nodes)
    else:
        for node in yield_nodes(graph, target_nodes):
            data = graph.nodes[node]
            if is_dict_subset(node_data, data):
                yield node


def yield_nodes(graph, nodes):
    node_set = set(nodes)
    for node in graph.nodes():
        if node in node_set:
            yield node
