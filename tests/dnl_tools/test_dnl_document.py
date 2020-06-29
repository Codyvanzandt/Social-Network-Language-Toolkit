import pytest
from src.dnl_tools.dnl_document import DNLDocument


def test_to_string(fake_play_file, fake_play_string):
    assert (
        DNLDocument(fake_play_file.absolute()).to_string().strip()
        == fake_play_string.strip()
    )


def test_to_dict():
    pass


def test_serialize_intermediate_data():
    pass


def test_parse_data():
    pass


def test_load_data():
    pass


def test_load_from_file_path():
    pass
