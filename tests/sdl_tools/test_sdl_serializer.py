import pytest
import enolib
import yaml
from src.sdl_tools.sdl_serializer import (
    get_field_key_value,
    serialize_section,
    serialize_edges_section,
    serialize_sdl,
    serialize_divisions,
    _get_subsections,
    _get_subsections_from,
)
from src.sdl_tools.mapped_edge_serializer import serialize_mapped_edges
from src.sdl_tools.enter_exit_edge_serializer import serialize_enter_exit_edges
from src.sdl_tools.sdl_parser import parse_sdl_string
from pprint import pprint


def test_serialize_sdl(fake_play_sdl_doc):
    serialized_doc = serialize_sdl(fake_play_sdl_doc)
    assert serialized_doc["play"] == serialize_section(fake_play_sdl_doc, "play")
    assert serialized_doc["characters"] == serialize_section(
        fake_play_sdl_doc, "characters"
    )
    assert serialized_doc["edges"] == serialize_edges_section(fake_play_sdl_doc)
    assert serialized_doc["divisions"] == serialize_divisions(fake_play_sdl_doc)


def test__serialize_edge_section_mapped():
    mapped_edges_text = """
    # edges
    A.B : {}
    B.C : {}
    """
    mapped_edges_doc = parse_sdl_string(mapped_edges_text)
    mapped_edges_section = mapped_edges_doc.section("edges")
    assert serialize_edges_section(mapped_edges_doc) == list(
        serialize_mapped_edges(mapped_edges_section)
    )


def test__serialize_edge_section_enter_exit():
    enter_exit_text = """
    # edges
    A+, B+, C+
    A-, B-, D+, E+
    """
    enter_exit_doc = parse_sdl_string(enter_exit_text)
    edges_section = enter_exit_doc.section("edges")
    edges_data = [edge.string_key() for edge in edges_section.elements()]
    assert serialize_edges_section(enter_exit_doc) == list(
        serialize_enter_exit_edges(edges_data)
    )


def test__serialize_edge_section_nested():
    nested_text = """
    # edges
    ## act1
    A.B : {}
    B.C : {}
    """
    nested_edges_doc = parse_sdl_string(nested_text)
    nested_edges_section = nested_edges_doc.section("edges").section("act1")
    expected_serialization = {
        "act1": list(serialize_mapped_edges(nested_edges_section))
    }
    assert serialize_edges_section(nested_edges_doc) == expected_serialization


def test_serialize_section(fake_play_sdl_doc, fake_play_data):
    sections = ("play", "characters")
    for section in sections:
        assert serialize_section(fake_play_sdl_doc, section) == fake_play_data[section]


def test_get_field_key_value(section):
    section_name = "section_name"
    field_key_value_triples = [
        ("key0:value0", "key0", "value0"),
        ("key 0 : value 0", "key 0", "value 0"),
        ("key0 : {inner_key : inner_value}", "key0", "{inner_key : inner_value}"),
    ]
    doc = section(section_name, field_key_value_triples)
    for i, field in enumerate(doc.section("section").elements()):
        expected_key = field_key_value_triples[i][1]
        expected_value = yaml.load(
            field_key_value_triples[i][2], Loader=yaml.FullLoader
        )
        assert get_field_key_value(field) == (expected_key, expected_value)


def test_get_field_key_value_raises():
    with pytest.raises(ValueError, match=".* must be of the format `key : value`"):
        get_field_key_value(parse_sdl_string("# section"))


def test_serialize_divisions():
    doc = """
    # edges
    ## section
    ### subsection0
    #### subsubsection0
    ### subsection1
    #### subsubsection1
    """
    expected_structure = {
        "section",
        "section.subsection0",
        "section.subsection1",
        "section.subsection0.subsubsection0",
        "section.subsection1.subsubsection1",
    }
    assert serialize_divisions(parse_sdl_string(doc)) == expected_structure


def test__get_subsections():
    sections = """
    # section
    ## subsection0
    ### subsubsection0
    ## subsection1
    ### subsubsection1
    """
    section = parse_sdl_string(sections).section("section")
    sections = _get_subsections(section)
    expected_structure = {
        "section",
        "section.subsection0",
        "section.subsection1",
        "section.subsection0.subsubsection0",
        "section.subsection1.subsubsection1",
    }
    assert sections == expected_structure


def test__get_subsections_from():
    some_subsections = """
    # section
    ## subsection0
    ## subsection1
    """
    section = parse_sdl_string(some_subsections).section("section")
    subsections = _get_subsections_from(section)
    subsection_strings = [subsection.string_key() for subsection in subsections]
    assert subsection_strings == ["subsection0", "subsection1"]

    no_subsections = """
    # section
    """
    section = parse_sdl_string(no_subsections).section("section")
    subsections = _get_subsections_from(section)
    subsection_strings = [subsection.string_key() for subsection in subsections]
    assert subsection_strings == list()
