import enolib
from enolib.elements.section import Section
from enolib.elements.field import Field
import yaml
from collections import defaultdict


def load_sdl_string(data):
    sdl_document = parse_sdl_string(data)
    return serialize_sdl(sdl_document)


def load_sdl_file(data):
    sdl_document = parse_sdl_file(data)
    return serialize_sdl(sdl_document)


def parse_sdl_file(data):
    try:
        return enolib.parse(data.read(), source=data.name)
    except AttributeError:
        with open(data, "r") as sdl_file:
            return enolib.parse(sdl_file.read(), source=sdl_file.name)


def parse_sdl_string(data):
    return enolib.parse(data)


def serialize_sdl(sdl_document):
    return {
        "play": serialize_section(sdl_document, "play"),
        "characters": serialize_section(sdl_document, "characters"),
        "network": serialize_section(sdl_document, "network"),
        "edges": serialize_edge_section(sdl_document),
    }


def serialize_edge_section(sdl_document):
    edge_section = sdl_document.section("edges")
    return _serialize_edge_section(edge_section)
    

def _serialize_edge_section(edge_section):
    try:
        return list( serialize_edges(edge_section) )
    except:
        return {
            subsection.string_key() : _serialize_edge_section(subsection)
            for subsection in ( subsection.to_section() for subsection in edge_section.elements() )
        }


def serialize_edges(edges_section):
    for edge in edges_section.elements():
        edge = edge.to_field()
        source_character, target_character = parse_edge_key(edge.string_key())
        edge_data = edge.required_value(valid_yaml)
        yield (source_character, target_character, edge_data)


def serialize_section(sdl_document, section_name):
    section = sdl_document.section(section_name)
    section_data = dict()
    for element in section.elements():
        field_key, field_value = get_field_key_value(element)
        section_data[field_key] = field_value
    return section_data


def get_field_key_value(sdl_element):
    if sdl_element.yields_field():
        sdl_field = sdl_element.to_field()
        sdl_key = sdl_field.string_key()
        sdl_value = sdl_field.required_value(valid_yaml)
        return sdl_key, sdl_value
    else:
        raise ValueError(f"{str(sdl_element)} must be of the format `key : value`")


def valid_yaml(value):
    return yaml.load(value, Loader=yaml.FullLoader)


def parse_edge_key(value):
    try:
        source_character, target_character = value.split(".")
        return source_character, target_character
    except ValueError:
        raise ValueError(f"Edge `{value}` must be of the form `character1.character2`")
