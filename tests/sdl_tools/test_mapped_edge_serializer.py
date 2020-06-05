import pytest
from src.sdl_tools.mapped_edge_serializer import (
    serialize_edge_key,
    serialize_mapped_edges,
)


def test_serialize_mapped_edges(section):
    edge_data = [
        (r"A.B : {}", "A", "B", {}),
        (r"A.B : {type : hit, weight : 1}", "A", "B", {"type": "hit", "weight": 1}),
    ]
    doc = section("edges", edge_data)
    edges_section = doc.section("edges")
    expected_edges = [(source, target, data) for _, source, target, data in edge_data]
    assert list(serialize_mapped_edges(edges_section)) == expected_edges


def test_serialize_edge_key():
    assert serialize_edge_key("A.B") == ("A", "B")
    assert serialize_edge_key("Mr A.Mr B") == ("Mr A", "Mr B")
    with pytest.raises(
        ValueError, match=r"Edge `.*` must be of the form `character1.character2`"
    ):
        serialize_edge_key("AB")
