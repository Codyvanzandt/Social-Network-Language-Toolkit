import pytest
import networkx
from networkx.algorithms.isomorphism import is_isomorphic
from src.utils.networkx_utils import get_subgraph_by_nodes


def test_get_subgraph_by_nodes():
    test_edge_list = [("A", "B", {}), ("B", "C", {}), ("C", "A", {}), ("D", "E", {})]
    test_graph = networkx.MultiGraph(test_edge_list)

    # subgraph of zero nodes == empty graph
    assert is_isomorphic(get_subgraph_by_nodes(test_graph, []), networkx.MultiGraph())

    # subgraph of absent nodes == empty graph
    assert is_isomorphic(
        get_subgraph_by_nodes(test_graph, ["X", "Y", "Z"]), networkx.MultiGraph()
    )

    # subgraph of all nodes == original graph
    assert is_isomorphic(
        get_subgraph_by_nodes(test_graph, ["A", "B", "C", "D", "E"]), test_graph
    )

    # subgraph of one source node with only one target node
    assert is_isomorphic(
        get_subgraph_by_nodes(test_graph, ["D"]), networkx.MultiGraph([("D", "E", {})]),
    )

    # subgraph of one source node with multiple target nodes
    assert is_isomorphic(
        get_subgraph_by_nodes(test_graph, ["A"]),
        networkx.MultiGraph([("A", "B", {}), ("C", "A", {})]),
    )

    # subgraph of multiple source nodes, some absent
    assert is_isomorphic(
        get_subgraph_by_nodes(test_graph, ["A", "Q"]),
        networkx.MultiGraph([("A", "B", {}), ("C", "A", {})]),
    )

    # subgraph of multiple source nodes, no shared target nodes
    assert is_isomorphic(
        get_subgraph_by_nodes(test_graph, ["A", "D"]),
        networkx.MultiGraph([("A", "B", {}), ("C", "A", {}), ("D", "E", {})]),
    )

    # subgraph of multiple source nodes, shared target nodes
    assert is_isomorphic(
        get_subgraph_by_nodes(test_graph, ["A", "B"]),
        networkx.MultiGraph([("A", "B", {}), ("C", "A", {}), ("B", "C", {})]),
    )
