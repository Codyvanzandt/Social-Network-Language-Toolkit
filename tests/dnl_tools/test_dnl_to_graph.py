import pytest
import networkx
from src.dnl_tools.dnl_to_graph import (
    dnl_doc_to_graph,
    get_empty_graph,
    add_edges_section_to_graph,
    add_characters_section_to_graph,
    add_sections_to_graph,
)

CHARACTER_DNL = """# characters
Alice : { age : Alice-age, occupation : Alice-occupation }
Bob : { age : Bob-age, occupation : Bob-occupation }
"""

EDGE_DNL = """# edges
Alice.Bob : {type : 1}
Alice.Bob : {type : 2}
"""

OTHER_DNL = """# custom-section
key : {nested : {value : 1}}
"""


def test_dnl_doc_to_graph(dnl_doc_factory, fake_play_string):
    doc = dnl_doc_factory(fake_play_string)
    graph = dnl_doc_to_graph(doc, directed=True)
    assert dict(graph.nodes(data=True)) == doc.data["characters"]
    assert graph.graph == {"play": doc.data["play"]}

    expected_edges = doc.data["edges"]
    actual_edges = list(graph.edges(data=True))
    assert len(expected_edges) == len(actual_edges)
    for i, edge in enumerate(expected_edges):
        assert edge in actual_edges


def test_get_empty_graph():
    assert isinstance(
        get_empty_graph(directed=True, multigraph=True), networkx.MultiDiGraph
    )
    assert isinstance(
        get_empty_graph(directed=True, multigraph=False), networkx.DiGraph
    )
    assert isinstance(
        get_empty_graph(directed=False, multigraph=True), networkx.MultiGraph
    )
    assert isinstance(get_empty_graph(directed=False, multigraph=False), networkx.Graph)

    with pytest.raises(ValueError):
        get_empty_graph(directed="bad input", multigraph=True)


def test_add_edges_section_to_graph(dnl_doc_factory):
    doc = dnl_doc_factory(EDGE_DNL)
    graph = get_empty_graph(directed=False, multigraph=True)
    add_edges_section_to_graph(doc, graph)
    assert list(graph.edges(data=True)) == doc.data["edges"]


def test_add_characters_section_to_graph(dnl_doc_factory):
    doc = dnl_doc_factory(CHARACTER_DNL)
    graph = get_empty_graph(directed=False, multigraph=False)
    add_characters_section_to_graph(doc, graph)
    assert dict(graph.nodes(data=True)) == doc.data["characters"]


def test_add_sections_to_graph(dnl_doc_factory):
    doc = dnl_doc_factory(CHARACTER_DNL + EDGE_DNL + OTHER_DNL)
    graph = get_empty_graph(directed=False, multigraph=True)
    add_sections_to_graph(doc, graph, exclude=("characters", "edges"))
    assert graph.graph == {"custom-section": doc.data["custom-section"]}
