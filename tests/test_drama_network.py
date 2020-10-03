import pytest
from src.drama_network import DramaNetwork
from src.dnl_tools.dnl_to_graph import dnl_doc_to_graph
from src.utils.networkx_utils import get_subgraph, new_graph_from_edges
from src.utils.edge_utils import combine_all_edges, edges_equal, combine_edges
from networkx.algorithms.isomorphism import is_isomorphic
from functools import partial

drama_is_isomorphic = partial(
    is_isomorphic, node_match=lambda a, b: a == b, edge_match=lambda a, b: a == b
)


def test_getitem(fake_drama_network):
    for key in fake_drama_network.doc.data.keys():
        assert fake_drama_network[key] == fake_drama_network.doc.data[key]


def test_to_graph(fake_drama_network):
    assert drama_is_isomorphic(
        fake_drama_network.to_graph(directed=True),
        dnl_doc_to_graph(fake_drama_network.doc, directed=True),
    )

    assert drama_is_isomorphic(
        fake_drama_network.to_graph(directed=False),
        dnl_doc_to_graph(fake_drama_network.doc, directed=False),
    )


def test_to_subgraph(fake_drama_network):
    assert drama_is_isomorphic(
        fake_drama_network.to_subgraph(
            directed=True,
            divisions="act1",
            characters="Isabella",
            edges=("Isabella", "Flavio"),
            character_data={"archetype": "innamorati"},
            edge_data={"type": "kissed"},
        ),
        get_subgraph(
            fake_drama_network.to_graph(directed=True),
            divisions=("act1",),
            nodes=("Isabella",),
            edges=[
                ("Isabella", "Flavio"),
            ],
            node_data={"archetype": "innamorati"},
            edge_data={"type": "kissed"},
        ),
    )


def test_to_combined_graph(fake_drama_network):
    old_graph = fake_drama_network.to_graph()
    expected_edges = combine_all_edges(
        old_graph.edges(data=True), edges_equal, combine_edges
    )
    expected_graph = new_graph_from_edges(old_graph, expected_edges)
    assert drama_is_isomorphic(fake_drama_network.to_combined_graph(), expected_graph)


def test_to_string(fake_drama_network):
    assert fake_drama_network.to_string() == fake_drama_network.doc.to_string()


def test_to_file(fake_drama_network, tmp_path):
    tmp_file = tmp_path / "test_dnl"
    fake_drama_network.to_file(tmp_file.absolute())
    with open(tmp_file.absolute(), "r") as test_dnl_file:
        assert test_dnl_file.read() == fake_drama_network.to_string()
