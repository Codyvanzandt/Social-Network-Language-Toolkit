import pytest
from src.converters.sdl_file_converter import convert_to_file
from src.drama_network import DramaNetwork
from unittest.mock import patch


def test_convert_to_file(tmp_path, fake_drama_network):
    temp_sdl_file = tmp_path / "test.sdl"
    temp_sdl_file_path = temp_sdl_file.absolute()
    convert_to_file(fake_drama_network, temp_sdl_file_path)
    assert (
        DramaNetwork(temp_sdl_file_path, directed=True).to_sdl_string()
        == fake_drama_network.to_sdl_string()
    )
