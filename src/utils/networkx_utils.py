import networkx


def get_node_subgraph(graph, nodes=None, node_data=None):
    """
    Given:
        nodes - an iterable of nodes
        node_data - a dict of node data
    Return:
        A shallow-copy subgraph with the given nodes.
        If node_data is specified, only nodes with matching data will be included. 
    """
    subgraph_nodes = list(get_nodes(graph, nodes=nodes, node_data=node_data))
    subgraph_edges = list(yield_edges_with_nodes(graph, subgraph_nodes))
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


def get_edges(graph, edges=None, edge_data=None):
    target_edges = edges if edges else graph.edges()
    if not edge_data:
        yield from yield_edges(graph, target_edges)
    else:
        for s, t, k in yield_edges(graph, target_edges):
            data = graph[s][t][k]
            if is_dict_subset(edge_data, data):
                yield (s, t, k)


def get_nodes(graph, nodes=None, node_data=None):
    target_nodes = nodes if nodes else graph.nodes()
    if not node_data:
        yield from yield_nodes(graph, target_nodes)
    else:
        for node in yield_nodes(graph, target_nodes):
            data = graph.nodes[node]
            if is_dict_subset(node_data, data):
                yield node


def yield_edges(graph, edges):
    edges_set = set(edges)
    for s, t, k in graph.edges(keys=True):
        if (s, t) in edges_set:
            yield (s, t, k)


def yield_nodes(graph, nodes):
    node_set = set(nodes)
    for node in graph.nodes():
        if node in node_set:
            yield node


def yield_edges_with_nodes(graph, nodes):
    nodes_set = set(nodes)
    for s, t, k in graph.edges(keys=True):
        if s in nodes_set or t in nodes_set:
            yield (s, t, k)


def is_dict_subset(smaller, larger):
    return all(
        larger.get(smaller_key, None) == smaller_val
        for smaller_key, smaller_val in smaller.items()
    )
