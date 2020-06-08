import networkx


def get_subgraph_by_nodes(graph, nodes):
    return graph.edge_subgraph(_yield_edges_with_nodes(graph, nodes)).copy()


def _yield_edges_with_nodes(graph, nodes):
    nodes_set = set(nodes)
    for s, t, k in graph.edges(keys=True):
        if s in nodes_set or t in nodes_set:
            yield (s, t, k)
