import pytest
from src.sdl_tools.sdl_api import load_sdl_string, load_sdl_file


def test_load_sdl_string(fake_play_string, fake_play_data):
    assert load_sdl_string(fake_play_string) == fake_play_data


def test_load_sdl_file(fake_play_string, fake_play_data, tmp_path):
    temp_sdl_file = tmp_path / "temp.sdl"
    temp_sdl_file.write_text(fake_play_string)
    assert load_sdl_file(temp_sdl_file) == fake_play_data
