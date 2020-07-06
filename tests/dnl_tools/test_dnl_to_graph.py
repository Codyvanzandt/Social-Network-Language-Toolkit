import pytest
import networkx
from src.dnl_tools.dnl_to_graph import (
    dnl_doc_to_graph,
    get_empty_graph,
    add_edges_section_to_graph,
    add_characters_section_to_graph,
    add_sections_to_graph,
)


def test_dnl_doc_to_graph():
    pass


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


def test_add_edges_section_to_graph():
    pass


def test_add_characters_section_to_graph():
    pass


def test_add_sections_to_graph():
    pass
