import pytest
from src.converters.string_converter import (
    convert_edges_list_to_string,
    convert_edges_data_to_string,
    convert_edges_section_to_string,
    convert_section_data_to_string,
    convert_section_name_to_string,
    convert_section_to_string,
    convert_to_string,
)


def test_convert_to_string(fake_drama_network):
    expected_string = (
        convert_section_to_string(fake_drama_network, "play")
        + convert_section_to_string(fake_drama_network, "characters")
        + convert_edges_section_to_string(fake_drama_network)
    )
    assert convert_to_string(fake_drama_network) == expected_string


def test_convert_section_to_string(fake_drama_network):
    character_section_name = "characters"
    character_section_data = fake_drama_network._data.get(
        character_section_name, dict()
    )
    actual_string = convert_section_to_string(
        fake_drama_network, character_section_name
    )
    expected_string = (
        convert_section_name_to_string(character_section_name)
        + convert_section_data_to_string(character_section_data)
        + "\n\n"
    )
    assert actual_string == expected_string


def test_convert_section_name_to_string():
    assert convert_section_name_to_string("section") == "# section\n"
    assert convert_section_name_to_string("section", section_level=2) == "## section\n"
    assert convert_section_name_to_string("section", section_level=3) == "### section\n"


def test_convert_section_data_to_string():
    assert (
        convert_section_data_to_string({"string_key": "value"}) == "string_key : value"
    )
    assert convert_section_data_to_string({"bool_key": True}) == f"bool_key : true"
    assert convert_section_data_to_string({"int_key": 42}) == f"int_key : 42"
    assert convert_section_data_to_string({"float_key": 42.0}) == f"float_key : 42.0"
    assert (
        convert_section_data_to_string({"array_key": [42, 42, 42]})
        == f"array_key : [42, 42, 42]"
    )
    assert (
        convert_section_data_to_string({"dict_key": {"key": "value"}})
        == "dict_key : {key: value}"
    )


def test_convert_edges_section_to_string(fake_drama_network):
    edges_data = fake_drama_network._data["edges"]
    expected_string = convert_section_name_to_string(
        "edges"
    ) + convert_edges_data_to_string(edges_data)
    assert convert_edges_section_to_string(fake_drama_network) == expected_string


def test_convert_edges_data_to_string():
    nested_edges_data = {
        "act1": {"scene1": [("A", "B", dict())]},
        "act2": [("C", "D", dict())],
    }
    expected_string = """## act1
### scene1
A.B : {}
## act2
C.D : {}"""
    assert convert_edges_data_to_string(nested_edges_data) == expected_string


def test_convert_edges_list_to_string():
    edges = [("A", "B", {"data0": "value0", "data1": "value1"}), ("B", "C", dict())]
    expected_string = "\n".join(["A.B : {data0: value0, data1: value1}", "B.C : {}"])
    actual_string = convert_edges_list_to_string(edges)
    assert actual_string == expected_string
