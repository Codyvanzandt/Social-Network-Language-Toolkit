import pytest
import networkx
from src.converters.networkx_converter import SDLToNXConverter
from pprint import pprint


def test_convert_to_networkx(fake_sdl_document):
    # undirected
    resulting_graph = SDLToNXConverter(fake_sdl_document).to_networkx(
        directed=False, embed_play=False
    )
    for source, target, edge_data in fake_sdl_document.data["edges"]:
        assert resulting_graph.has_edge(source, target)
        assert resulting_graph.has_edge(target, source)
        assert resulting_graph.get_edge_data(
            source, target
        ) == resulting_graph.get_edge_data(target, source)
        assert edge_data in resulting_graph.get_edge_data(source, target).values()


def test__get_empty_graph():
    assert isinstance(
        SDLToNXConverter.get_empty_graph(directed=True), networkx.MultiDiGraph
    )
    assert isinstance(
        SDLToNXConverter.get_empty_graph(directed=False), networkx.MultiGraph
    )
    with pytest.raises(
        ValueError, match="The value for `directed` must be one of.*",
    ):
        SDLToNXConverter.get_empty_graph(directed="bad value")


def test__add_play_data(fake_sdl_document):
    empty_graph = SDLToNXConverter.get_empty_graph(directed=False)
    SDLToNXConverter.add_play_data(
        empty_graph, fake_sdl_document.data.get("play", dict())
    )
    for play_data_key, play_data_value in fake_sdl_document.data["play"].items():
        assert empty_graph.graph[play_data_key] == play_data_value


def test__add_character_data(fake_sdl_document):
    empty_graph = SDLToNXConverter.get_empty_graph(directed=False)
    SDLToNXConverter.add_character_data(
        empty_graph, fake_sdl_document.data["characters"]
    )
    for character_name, character_data in fake_sdl_document.data["characters"].items():
        assert character_name in empty_graph.nodes
        for char_data_key, char_data_value in character_data.items():
            assert empty_graph.nodes[character_name][char_data_key] == char_data_value
