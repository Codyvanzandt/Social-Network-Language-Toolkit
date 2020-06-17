import pytest
from src.utils.edge_utils import walk_nested_edges, flatten_nested_edges
from pprint import pprint

EDGE_DATA = {
    "act1": {
        "scene1": [
            ("A", "B", {"type": 1}),
            ("B", "C", {"type": 1}),
            ("C", "D", {"type": 1}),
        ],
        "scene2": [("D", "E", {"type": 1})],
    }
}


def test_walk_nested_edges():

    assert walk_nested_edges(EDGE_DATA, lambda x: x) == EDGE_DATA

    empty_edge_data = {
        "act1": {
            "scene1": [("A", "B", {}), ("B", "C", {}), ("C", "D", {})],
            "scene2": [("D", "E", {})],
        }
    }

    def remove_data(edge_list):
        return [(s, t, {}) for s, t, _ in edge_list]

    assert walk_nested_edges(EDGE_DATA, remove_data) == empty_edge_data


def test_flatten_nested_edges():
    expected_edges = [
        ("A", "B", {"type": 1}),
        ("B", "C", {"type": 1}),
        ("C", "D", {"type": 1}),
        ("D", "E", {"type": 1}),
    ]
    assert flatten_nested_edges(EDGE_DATA) == expected_edges
