import pytest
import networkx
from src.converters.networkx_converter import (
    convert_to_networkx,
    _get_empty_graph,
    _add_play_data,
    _add_character_data,
)
from pprint import pprint


def test_convert_to_networkx(fake_drama_network):
    # undirected
    resulting_graph = convert_to_networkx(fake_drama_network, directed=False)
    for source, target, edge_data in fake_drama_network.to_edge_list():
        assert resulting_graph.has_edge(source, target)
        assert resulting_graph.has_edge(target, source)
        assert resulting_graph.get_edge_data(
            source, target
        ) == resulting_graph.get_edge_data(target, source)
        assert edge_data in resulting_graph.get_edge_data(source, target).values()


def test__get_empty_graph():
    assert isinstance(_get_empty_graph(directed=True), networkx.MultiDiGraph)
    assert isinstance(_get_empty_graph(directed=False), networkx.MultiGraph)
    with pytest.raises(
        ValueError, match="The value for `directed` must be one of.*",
    ):
        _get_empty_graph(directed="bad value")


def test__add_play_data(fake_drama_network):
    empty_graph = _get_empty_graph(directed=False)
    _add_play_data(fake_drama_network, empty_graph)
    for play_data_key, play_data_value in fake_drama_network.data["play"].items():
        assert empty_graph.graph[play_data_key] == play_data_value


def test__add_character_data(fake_drama_network):
    empty_graph = _get_empty_graph(directed=False)
    _add_character_data(fake_drama_network, empty_graph)
    for character_name, character_data in fake_drama_network.data["characters"].items():
        assert character_name in empty_graph.nodes
        for char_data_key, char_data_value in character_data.items():
            assert empty_graph.nodes[character_name][char_data_key] == char_data_value
