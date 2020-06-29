import pytest
import enolib
from src.dnl_tools.dnl_document import DNLDocument


def test_bad_input():
    with pytest.raises(ValueError):
        DNLDocument("bad data")


def test_to_string(fake_play_file, fake_play_string):
    assert (
        DNLDocument(fake_play_file.absolute()).to_string().strip()
        == fake_play_string.strip()
    )


def test_to_dict(fake_play_file, fake_play_data_with_edge_data):
    assert DNLDocument(fake_play_file).data == fake_play_data_with_edge_data


def test_parse_data(fake_play_file):
    doc = DNLDocument(fake_play_file)
    for e1, e2 in zip(
        doc._parsed_data.elements(), enolib.parse(doc._loaded_data).elements()
    ):
        section1 = e1.to_section()
        section2 = e2.to_section()
        assert section1.string_key() == section2.string_key()


def test_load_data(fake_play_file, fake_play_string, fake_play_data_with_edge_data):
    assert (
        DNLDocument(fake_play_file).data
        == DNLDocument(fake_play_file.absolute()).data
        == DNLDocument(fake_play_string).data
    )


def test_load_from_file_path(fake_play_file, fake_play_string):
    assert (
        DNLDocument.load_from_file_path(fake_play_file.absolute()) == fake_play_string
    )
