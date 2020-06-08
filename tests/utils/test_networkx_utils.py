import pytest
import networkx
from networkx.algorithms.isomorphism import is_isomorphic
from src.utils.networkx_utils import (
    get_node_subgraph,
    get_edge_subgraph,
    get_edges,
    get_nodes,
    yield_edges,
    yield_nodes,
    yield_edges_with_nodes,
    is_dict_subset,
)


def test_get_node_subgraph():
    edges = [
        ("A", "B", {"type": 1, "size": "big"}),
        ("A", "B", {"type": 2, "size": "small"}),
        ("B", "C", {"type": 1, "size": "big"}),
    ]
    nodes = [
        ("A", {"type": 1, "size": "big"}),
        ("B", {"type": 1, "size": "big"}),
        ("C", {"type": 1, "size": "small"}),
    ]
    graph = networkx.MultiGraph(edges)
    graph.add_nodes_from(nodes)
    graph.graph["graph_data"] = "graph_value"

    # subgraph by node
    subgraph = get_node_subgraph(graph, nodes=["A"])
    assert list(subgraph.edges(keys=True)) == [
        ("A", "B", 0),
        ("A", "B", 1),
    ]
    assert list(subgraph.nodes(data=True)) == [
        ("A", {"type": 1, "size": "big"}),
        ("B", {"type": 1, "size": "big"}),
    ]
    assert subgraph.graph["graph_data"] == "graph_value"

    # subgraph by node data
    subgraph = get_node_subgraph(graph, node_data={"type": 1, "size": "small"})
    assert list(subgraph.edges(keys=True)) == [
        ("B", "C", 0),
    ]


def test_get_edge_subgraph():
    edges = [
        ("A", "B", {"type": 1, "size": "big"}),
        ("A", "B", {"type": 2, "size": "small"}),
        ("B", "C", {"type": 1, "size": "big"}),
    ]
    nodes = [
        ("A", {"type": 1, "size": "big"}),
        ("B", {"type": 1, "size": "big"}),
        ("C", {"type": 1, "size": "small"}),
    ]
    graph = networkx.MultiGraph(edges)
    graph.add_nodes_from(nodes)
    graph.graph["graph_data"] = "graph_value"

    # subgraph by edge
    subgraph = get_edge_subgraph(graph, edges=[("A", "B")])
    assert list(subgraph.edges(keys=True)) == [
        ("A", "B", 0),
        ("A", "B", 1),
    ]
    assert list(subgraph.nodes(data=True)) == [
        ("A", {"type": 1, "size": "big"}),
        ("B", {"type": 1, "size": "big"}),
    ]
    assert subgraph.graph["graph_data"] == "graph_value"

    # subgraph by edge data
    assert list(
        get_edge_subgraph(graph, edge_data={"type": 2, "size": "small"}).edges(
            keys=True
        )
    ) == [("A", "B", 1),]


def test_get_edges():
    edges = [
        ("A", "B", {"type": 1, "size": "big"}),
        ("A", "B", {"type": 2, "size": "small"}),
        ("B", "C", {"type": 1, "size": "big"}),
    ]
    graph = networkx.MultiGraph(edges)

    # single edge, by edge
    assert list(get_edges(graph, edges=[("B", "C")])) == [("B", "C", 0)]

    # single edge, by data
    assert list(get_edges(graph, edge_data={"type": 2, "size": "small"})) == [
        ("A", "B", 1)
    ]

    # single edge, by node and data
    assert list(
        get_edges(graph, edges=[("A", "B")], edge_data={"type": 2, "size": "small"})
    ) == [("A", "B", 1)]

    # multiple edges, by edges
    assert list(get_edges(graph, edges=[("A", "B"), ("B", "C")])) == [
        ("A", "B", 0),
        ("A", "B", 1),
        ("B", "C", 0),
    ]

    # multiple edges, by data
    assert list(get_edges(graph, edge_data={"type": 1})) == [
        ("A", "B", 0),
        ("B", "C", 0),
    ]

    # multiple edges, by node and data
    assert list(
        get_edges(graph, edges=[("A", "B"), ("B", "C")], edge_data={"type": 1})
    ) == [("A", "B", 0), ("B", "C", 0)]

    # multiple edges by edge, filtering out by data
    assert list(
        get_edges(graph, edges=[("A", "B")], edge_data={"type": 1, "size": "big"})
    ) == [("A", "B", 0)]

    # multiple edges by data, filtering out by node
    assert list(get_edges(graph, edges=[("A", "B")], edge_data={"type": 1})) == [
        ("A", "B", 0)
    ]

    # all nodes with given data
    assert list(get_edges(graph, edge_data={"type": 1})) == [
        ("A", "B", 0),
        ("B", "C", 0),
    ]

    # no nodes
    assert list(get_edges(graph, edge_data={"type": 3})) == []
    assert list(get_edges(graph, edges=[("X", "Y")])) == []
    assert list(get_edges(graph, edges=[("A", "B")], edge_data={"type": None})) == []


def test_get_nodes():
    nodes = [
        ("A", {"type": 1, "size": "big"}),
        ("B", {"type": 1, "size": "big"}),
        ("C", {"type": 1, "size": "small"}),
        ("D", {"type": 2, "size": "huge"}),
    ]
    graph = networkx.MultiGraph()
    graph.add_nodes_from(nodes)

    # single node, by node
    assert list(get_nodes(graph, nodes=["A"])) == ["A"]

    # single node, by data
    assert list(get_nodes(graph, node_data={"type": 2, "size": "huge"})) == ["D"]

    # single node, by node and data
    assert list(
        get_nodes(graph, nodes=["A"], node_data={"type": 1, "size": "big"})
    ) == ["A"]

    # multiple nodes, by node
    assert list(get_nodes(graph, nodes=["A", "B"])) == ["A", "B"]

    # multiple nodes, by data
    assert list(get_nodes(graph, node_data={"type": 1, "size": "big"})) == ["A", "B"]

    # multiple nodes, by node and data
    assert list(
        get_nodes(graph, nodes=["A", "B"], node_data={"type": 1, "size": "big"})
    ) == ["A", "B"]

    # multiple nodes by node, filtering out by data
    assert list(
        get_nodes(graph, nodes=["A", "C"], node_data={"type": 1, "size": "big"})
    ) == ["A"]

    # multiple nodes by data, filtering out by node
    assert list(get_nodes(graph, nodes=["A"], node_data={"type": 1})) == ["A"]

    # all nodes with given data
    assert list(get_nodes(graph, node_data={"type": 1})) == ["A", "B", "C"]
    assert list(get_nodes(graph, node_data={"type": 2})) == ["D"]

    # no nodes
    assert list(get_nodes(graph, node_data={"type": 3})) == []
    assert list(get_nodes(graph, nodes=["X"])) == []
    assert (
        list(get_nodes(graph, nodes=["A", "B", "C", "D"], node_data={"type": None}))
        == []
    )


def test_yield_edges():
    edges = [("A", "B"), ("B", "C"), ("D", "E"), ("D", "E")]
    graph = networkx.MultiGraph(edges)

    # single edge
    assert list(yield_edges(graph, [("A", "B")])) == [("A", "B", 0)]

    # repeated single edge
    assert list(yield_edges(graph, [("D", "E")])) == [("D", "E", 0), ("D", "E", 1)]

    # multiple edges
    assert list(yield_edges(graph, [("A", "B"), ("B", "C")])) == [
        ("A", "B", 0),
        ("B", "C", 0),
    ]

    # all missing edges
    assert list(yield_edges(graph, [("X", "Y")])) == []

    # some missing edges
    assert list(yield_edges(graph, [("A", "B"), ("X", "Y")])) == [("A", "B", 0)]


def test_yield_nodes():
    edges = [("A", "B"), ("B", "C"), ("D", "E")]
    graph = networkx.MultiGraph(edges)

    # single node
    assert list(yield_nodes(graph, ["A"])) == ["A"]

    # multiple nodes
    assert list(yield_nodes(graph, ["A", "B"])) == ["A", "B"]

    # all missing nodes
    assert list(yield_nodes(graph, ["X"])) == []

    # some missing nodes, some present
    assert list(yield_nodes(graph, ["A", "X"])) == ["A"]


def test_yield_edges_with_nodes():
    edges = [("A", "B"), ("B", "C"), ("D", "E")]
    graph = networkx.MultiGraph(edges)

    # single node, single edge
    assert list(yield_edges_with_nodes(graph, ["D"])) == [("D", "E", 0)]

    # single node, multiple edges
    assert list(yield_edges_with_nodes(graph, ["B"])) == [("A", "B", 0), ("B", "C", 0)]

    # multiple node, single edge
    assert list(yield_edges_with_nodes(graph, ["D", "E"])) == [("D", "E", 0)]

    # multiple node, multiple edge
    assert list(yield_edges_with_nodes(graph, ["A", "D"])) == [
        ("A", "B", 0),
        ("D", "E", 0),
    ]

    # all missing edges
    assert list(yield_edges_with_nodes(graph, ["X", "Y"])) == []

    # some missing edges
    assert list(yield_edges_with_nodes(graph, ["D", "X"])) == [("D", "E", 0)]

    # all edges
    assert list(yield_edges_with_nodes(graph, ["A", "B", "C", "D", "E"])) == [
        ("A", "B", 0),
        ("B", "C", 0),
        ("D", "E", 0),
    ]


def test_is_dict_subset():
    assert is_dict_subset(dict(), dict())  # empty, empty
    assert is_dict_subset(dict(), {"A": 1})  # empty, non-empty
    assert is_dict_subset({"A": 1}, {"A": 1})  # exact match, single
    assert is_dict_subset({"A": 1, "B": 2}, {"A": 1, "B": 2})  # exact match, multiple
    assert is_dict_subset({"A": 1}, {"A": 1, "B": 2})  # subset single
    assert is_dict_subset({"A": 1, "B": 2}, {"A": 1, "B": 2, "C": 3})  # subset multiple

    assert not is_dict_subset({"A": 1}, dict())  # non-empty,
    assert not is_dict_subset({"A": 1}, {"B": 2})  # disjoint
    assert not is_dict_subset({"A": 1,}, {"A": 2})  # larger set wrong value
    assert not is_dict_subset(
        {"A": 1, "B": 2}, {"A": 1, "B": 1}
    )  # larger set wrong value multiple
    assert not is_dict_subset({"A": 1, "B": 2}, {"A": 1})  # larger set missing element
