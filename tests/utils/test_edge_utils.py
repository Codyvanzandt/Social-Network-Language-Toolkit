import pytest
from src.utils.edge_utils import walk_nested_edges
from pprint import pprint


def test_walk_nested_edges(fake_play_data):
    edge_data = fake_play_data["edges"]
    pprint(walk_nested_edges(edge_data))
