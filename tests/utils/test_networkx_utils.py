import pytest
import networkx
from networkx.algorithms.isomorphism import is_isomorphic
from src.drama_network import DramaNetwork
from src.utils.networkx_utils import (
    get_subgraph,
    get_node_subgraph,
    get_edge_subgraph,
    get_division_subgraph,
    get_edges_by_division,
    get_edges,
    get_nodes,
    yield_edges,
    yield_nodes,
    yield_edges_with_nodes,
)


def test_get_subgraph():
    edges = [
        ("A", "B", {"type": 1, "size": "big", "divisions": ("act1", "scene1")}),
        ("A", "B", {"type": 2, "size": "small", "divisions": ("act1", "scene2")}),
        ("B", "C", {"type": 1, "size": "big", "divisions": ("act2", "scene1")}),
    ]
    nodes = [
        ("A", {"type": 1, "size": "big"}),
        ("B", {"type": 1, "size": "big"}),
        ("C", {"type": 1, "size": "small"}),
    ]
    graph = networkx.MultiGraph(edges)
    graph.add_nodes_from(nodes)

    # get_subgraph is isomorphic to get_node_subgraph when using only nodes/node_data

    assert is_isomorphic(
        get_subgraph(graph, nodes=["A", "B"]),
        get_node_subgraph(graph, nodes=["A", "B"]),
    )

    assert is_isomorphic(
        get_subgraph(graph, node_data={"type": 1, "size": "big"}),
        get_node_subgraph(graph, node_data={"type": 1, "size": "big"}),
    )

    assert is_isomorphic(
        get_subgraph(graph, nodes=["A", "C"], node_data={"type": 1,}),
        get_node_subgraph(graph, nodes=["A", "C"], node_data={"type": 1,}),
    )

    # get_subgraph is isomorphic to get_edge_subgraph when using only edges/edge_data

    assert is_isomorphic(
        get_subgraph(graph, edges=[("A", "B")]),
        get_edge_subgraph(graph, edges=[("A", "B")]),
    )

    assert is_isomorphic(
        get_subgraph(graph, edge_data={"type": 1, "size": "big"}),
        get_edge_subgraph(graph, edge_data={"type": 1, "size": "big"}),
    )

    assert is_isomorphic(
        get_subgraph(graph, edges=[("A", "B"), ("B", "C")], edge_data={"type": 1,}),
        get_edge_subgraph(
            graph, edges=[("A", "B"), ("B", "C")], edge_data={"type": 1,}
        ),
    )

    # get_subgraph is isomorphic to intersection( get_node_subgraph, get_edge_subgraph ) when using both node and edge data
    assert is_isomorphic(
        get_subgraph(graph, nodes=["A", "B", "C"], edges=[("B", "C")]),
        networkx.MultiGraph([("B", "C", 0)]),
    )

    assert is_isomorphic(
        get_subgraph(
            graph, nodes=["A", "B", "C"], edge_data={"type": 1, "size": "big"}
        ),
        networkx.MultiGraph([("A", "B", 0), ("B", "C", 0)]),
    )

    assert is_isomorphic(
        get_subgraph(graph, node_data={"type": 1}, edges=[("B", "C")]),
        networkx.MultiGraph([("B", "C", 0)]),
    )

    assert is_isomorphic(
        get_subgraph(graph, node_data={"size": "small"}, edge_data={"size": "big"}),
        networkx.MultiGraph([("B", "C", 0)]),
    )

    # get_subgraph is isomorphic to intersection( get_node_subgraph, get_edge_subgraph, get_division_subgraph ) when using node, edge, and division data
    assert is_isomorphic(
        get_subgraph(
            graph, divisions=["act2"], nodes=["A", "B", "C"], edges=[("B", "C")]
        ),
        networkx.MultiGraph([("B", "C", 0)]),
    )

    assert is_isomorphic(
        get_subgraph(
            graph,
            divisions=["scene1"],
            nodes=["A", "B", "C"],
            edge_data={"type": 1, "size": "big"},
        ),
        networkx.MultiGraph([("A", "B", 0), ("B", "C", 0)]),
    )

    assert is_isomorphic(
        get_subgraph(
            graph, divisions=["act2.scene1"], node_data={"type": 1}, edges=[("B", "C")]
        ),
        networkx.MultiGraph([("B", "C", 0)]),
    )

    assert is_isomorphic(
        get_subgraph(
            graph,
            divisions=["act2.scene1"],
            node_data={"size": "small"},
            edge_data={"size": "big"},
        ),
        networkx.MultiGraph([("B", "C", 0)]),
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


def test_get_division_subgraph():
    test_sdl = """
    # edges
    ## act1
    ### scene1
    A.B : {}
    ### scene2
    B.C : {}
    ## act2
    ### scene1
    C.D : {}
    ### scene2
    D.E : {}
    ### scene3
    E.F : {}
    """
    graph = DramaNetwork(test_sdl)._graph
    assert is_isomorphic(get_division_subgraph(graph, divisions=None), graph)

    assert is_isomorphic(
        get_division_subgraph(graph, divisions=["act1.scene1"]),
        networkx.MultiGraph([("A", "B")]),
    )

    assert is_isomorphic(
        get_division_subgraph(graph, divisions=["act1"]),
        networkx.MultiGraph([("A", "B"), ("B", "C")]),
    )

    assert is_isomorphic(
        get_division_subgraph(graph, divisions=["scene1"]),
        networkx.MultiGraph([("A", "B"), ("C", "D")]),
    )

    assert is_isomorphic(
        get_division_subgraph(graph, divisions=["nonexistent_scene"]),
        networkx.MultiGraph(),
    )


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


def test_get_edges_by_division():
    test_sdl = """
    # edges
    ## act1
    ### scene1
    A.B : {}
    ### scene2
    B.C : {}
    ## act2
    ### scene1
    C.D : {}
    ### scene2
    D.E : {}
    ### scene3
    E.F : {}
    """
    graph = DramaNetwork(test_sdl)._graph

    # entire acts
    assert list(get_edges_by_division(graph, ["act1"])) == [
        ("A", "B", 0),
        ("B", "C", 0),
    ]
    assert list(get_edges_by_division(graph, ["act2"])) == [
        ("C", "D", 0),
        ("D", "E", 0),
        ("E", "F", 0),
    ]

    # specific fully-qualified scenes
    assert list(get_edges_by_division(graph, ["act1.scene1"])) == [
        ("A", "B", 0),
    ]
    assert list(get_edges_by_division(graph, ["act1.scene2"])) == [
        ("B", "C", 0),
    ]
    assert list(get_edges_by_division(graph, ["act2.scene1"])) == [
        ("C", "D", 0),
    ]
    assert list(get_edges_by_division(graph, ["act2.scene2"])) == [
        ("D", "E", 0),
    ]
    assert list(get_edges_by_division(graph, ["act2.scene3"])) == [
        ("E", "F", 0),
    ]

    # divisions that aren't fully qualified return everything that matches
    assert list(get_edges_by_division(graph, ["scene3"])) == [
        ("E", "F", 0),
    ]

    assert list(get_edges_by_division(graph, ["scene1"])) == [
        ("A", "B", 0),
        ("C", "D", 0),
    ]
