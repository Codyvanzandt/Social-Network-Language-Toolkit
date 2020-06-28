import pytest
from src.drama_network import DramaNetwork
import src.converters.converters as converters

# Initializing


def test_multiple_initializations(fake_play_string, fake_play_file):
    assert (
        (from_string := DramaNetwork(fake_play_string))._data
        == (from_file := DramaNetwork(fake_play_file))._data
        == (from_string_2 := DramaNetwork(from_string.to_string()))._data
    )

    print(converters.networkx_to_drama_network(from_string._graph)._data)
    print()
    print(from_string_2._data)
    assert (
        converters.networkx_to_drama_network(from_string._graph)._data
        == from_string_2._data
    )
