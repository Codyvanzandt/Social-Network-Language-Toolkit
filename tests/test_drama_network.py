import pytest
from pprint import pformat
from src.drama_network import DramaNetwork


def test_init(fake_drama_network):
    assert fake_drama_network


def test_repr(fake_drama_network):
    expected_repr = "DramaNetwork(a title)"
    assert repr(fake_drama_network) == expected_repr


def test_str(fake_drama_network):
    expected_str = f"DramaNetwork({pformat(fake_drama_network.data)})"
    assert str(fake_drama_network) == expected_str


def test__load_sdl_data(
    fake_drama_network, fake_play_data, fake_play_file, fake_play_string
):
    assert fake_drama_network._load_sdl_data(fake_play_file) == fake_play_data
    assert fake_drama_network._load_sdl_data(fake_play_string) == fake_play_data


def test_to_string(fake_drama_network):
    pass


def test_to_file(fake_drama_network):
    pass


def test_to_edge_list(fake_drama_network):
    pass


def test_to_networkx(fake_drama_network):
    pass
