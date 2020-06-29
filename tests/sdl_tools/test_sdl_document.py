import pytest
from src.dnl_tools.dnl_document import DNLDocument
from src.dnl_tools.edges import MappedEdges
from pprint import pprint


def test_load_data(fake_play_file, fake_play_string):
    str_doc = DNLDocument(fake_play_string)
    assert str_doc._loaded_data == fake_play_string

    file_path_doc = DNLDocument(fake_play_file.absolute())
    assert file_path_doc._loaded_data == fake_play_string

    file_doc = DNLDocument(fake_play_file)
    assert file_doc._loaded_data == fake_play_string


def test_parse_data(fake_play_string):
    str_doc = DNLDocument(fake_play_string)
    assert str_doc._parsed_data


def test_serialize_data(fake_play_string, fake_play_data):
    str_doc = DNLDocument(fake_play_string)
