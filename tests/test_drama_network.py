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


def test_str(fake_drama_network):
    expected_str = "DramaNetwork(a title)"
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
        DramaNetwork(from_to_file.absolute())._data
        == DramaNetwork(from_convert_to_file.absolute())._data
    )
