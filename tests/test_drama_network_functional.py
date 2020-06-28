import pytest
from src.drama_network import DramaNetwork
import src.converters.converters as converters
from pprint import pprint

# Initializing


def test_multiple_initializations(fake_play_string, fake_play_file):
    assert (
        (from_string := DramaNetwork(fake_play_string))._data
        == (from_file := DramaNetwork(fake_play_file))._data
        == (from_string_2 := DramaNetwork(from_string.to_string()))._data
    )
