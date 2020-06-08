import yaml
from src.sdl_tools.mapped_edge_serializer import serialize_mapped_edges, valid_yaml
from src.sdl_tools.enter_exit_edge_serializer import serialize_enter_exit_edges
from collections import ChainMap


def serialize_sdl(sdl_document):
    return {
        "play": serialize_section(sdl_document, "play"),
        "characters": serialize_section(sdl_document, "characters"),
        "edges": serialize_edges_section(sdl_document),
        "divisions": serialize_division_structure(sdl_document),
    }


def serialize_section(sdl_document, section_name):
    section = sdl_document.section(section_name)
    section_data = dict()
    for element in section.elements():
        field_key, field_value = get_field_key_value(element)
        section_data[field_key] = field_value
    return section_data


def get_field_key_value(sdl_element):
    if hasattr(sdl_element, "yields_field") and sdl_element.yields_field():
        sdl_field = sdl_element.to_field()
        sdl_key = sdl_field.string_key()
        sdl_value = sdl_field.required_value(valid_yaml)
        return sdl_key, sdl_value
    else:
        raise ValueError(f"{str(sdl_element)} must be of the format `key : value`")


def serialize_edges_section(sdl_document):
    edge_section = sdl_document.section("edges")
    return _serialize_edge_section(edge_section)


def _serialize_edge_section(edge_section):
    try:
        return list(serialize_mapped_edges(edge_section))
    except:
        try:
            return list(
                serialize_enter_exit_edges(
                    element.string_key() for element in edge_section.elements()
                )
            )
        except:
            return {
                subsection.string_key(): _serialize_edge_section(subsection)
                for subsection in (
                    subsection.to_section() for subsection in edge_section.elements()
                )
            }


def serialize_division_structure(sdl_document):
    edge_section = sdl_document.section("edges")
    return _get_section_structure(edge_section)


def _get_section_structure(section):
    subsections = list(_get_subsections(section))
    if len(subsections) == 0:
        return {section.string_key(): None}
    else:
        return {
            section.string_key(): dict(
                ChainMap(
                    *(_get_section_structure(subsection) for subsection in subsections)
                )
            )
        }


def _get_subsections(section):
    is_section = (
        lambda element: hasattr(element, "yields_section") and element.yields_section()
    )
    for element in section.elements():
        if is_section(element):
            yield element.to_section()
