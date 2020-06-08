import pytest
from pprint import pformat
from src.drama_network import DramaNetwork
from src.converters.string_converter import convert_to_string
from src.converters.edge_list_converter import convert_to_edge_list
from src.converters.sdl_file_converter import convert_to_file
from src.converters.networkx_converter import convert_to_networkx
from networkx.algorithms.isomorphism import is_isomorphic


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
    assert (
        fake_drama_network._load_sdl_data(fake_play_file)["play"]
        == fake_play_data["play"]
    )
    assert (
        fake_drama_network._load_sdl_data(fake_play_file)["characters"]
        == fake_play_data["characters"]
    )
    assert (
        fake_drama_network._load_sdl_data(fake_play_file)["edges"]
        == fake_play_data["edges"]
    )
    assert (
        fake_drama_network._load_sdl_data(fake_play_string)["play"]
        == fake_play_data["play"]
    )
    assert (
        fake_drama_network._load_sdl_data(fake_play_string)["characters"]
        == fake_play_data["characters"]
    )
    assert (
        fake_drama_network._load_sdl_data(fake_play_string)["edges"]
        == fake_play_data["edges"]
    )


def test_to_string(fake_drama_network):
    assert fake_drama_network.to_string() == convert_to_string(fake_drama_network)


def test_to_file(fake_drama_network, tmp_path):
    from_to_file = tmp_path / "from_file.sdl"
    from_convert_to_file = tmp_path / "from_convert_to_file.sdl"
    fake_drama_network.to_file(path=from_to_file)
    convert_to_file(fake_drama_network, from_convert_to_file)
    assert (
        DramaNetwork(from_to_file.absolute()).data
        == DramaNetwork(from_convert_to_file.absolute()).data
    )


def test_to_edge_list(fake_drama_network):
    assert fake_drama_network.to_edge_list() == list(
        convert_to_edge_list(fake_drama_network)
    )


def test_to_networkx(fake_drama_network):
    def data_equivalent(a, b):
        assert a == b
        return True

    assert is_isomorphic(
        fake_drama_network.to_networkx(directed=True),
        convert_to_networkx(fake_drama_network, directed=True),
        node_match=data_equivalent,
        edge_match=data_equivalent,
    )
