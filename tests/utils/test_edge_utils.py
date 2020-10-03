import pytest
from src.utils.edge_utils import combine_all_edges, edges_equal, combine_edges

EDGES = [
    ("A", "B", {"type": 1, "divisions": (1, 2)}),
    ("A", "B", {"type": 1, "divisions": (1, 2)}),
    ("A", "C", {"type": 1, "divisions": (1, 2)}),
    ("A", "B", {"type": 2, "divisions": (1, 2)}),
    ("A", "B", {"type": 1, "divisions": (3, 4)}),
    ("A", "B", {}),
]


def test_combine_all_edges():
    expected_edges = [
        (
            "A",
            "B",
            {"weight": 2, "type": 1, "divisions": (1, 2)},
        ),
    ] + EDGES[2::]
    assert combine_all_edges(EDGES, edges_equal, combine_edges) == expected_edges


def test_edges_equal():
    assert edges_equal(EDGES[0], EDGES[1])
    assert not edges_equal(EDGES[0], EDGES[2])
    assert not edges_equal(EDGES[0], EDGES[3])
    assert not edges_equal(EDGES[0], EDGES[4])


def test_combine_edges():
    assert combine_edges(EDGES[0], EDGES[1]) == (
        "A",
        "B",
        {"weight": 2, "type": 1, "divisions": (1, 2)},
    )
    assert combine_edges(EDGES[5], EDGES[5]) == (
        "A",
        "B",
        {"weight": 2, "type": None, "divisions": tuple()},
    )
