import pytest
import enolib
from src.sdl_tools.sdl_parser import parse_sdl_string, parse_sdl_file


def test_parse_sdl_string(fake_play_string):
    assert parse_sdl_string(fake_play_string)


def test_parse_sdl_file(fake_play_string, tmp_path):
    temp_sdl_file = tmp_path / "temp.sdl"
    temp_sdl_file.write_text(fake_play_string)
    assert parse_sdl_file(temp_sdl_file)


def test_parse_sdl_file_name(fake_play_string, tmp_path):
    temp_sdl_file = tmp_path / "temp.sdl"
    temp_sdl_file.write_text(fake_play_string)
    assert parse_sdl_file(temp_sdl_file.absolute())
