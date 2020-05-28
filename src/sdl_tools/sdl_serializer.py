import yaml
from src.sdl_tools.mapped_edge_serializer import serialize_mapped_edges, valid_yaml
from src.sdl_tools.enter_exit_edge_serializer import serialize_enter_exit_edges


def serialize_sdl(sdl_document):
    return {
        "play": serialize_section(sdl_document, "play"),
        "characters": serialize_section(sdl_document, "characters"),
        "edges": serialize_edges_section(sdl_document),
    }


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


def serialize_edges_section(sdl_document):
    edge_section = sdl_document.section("edges")
    return _serialize_edge_section(edge_section)


def _serialize_edge_section(edge_section):
    try:
        return list(serialize_mapped_edges(edge_section))
    except:
        try:
            return list(serialize_enter_exit_edges(edge_section.elements()))
        except:
            return {
                subsection.string_key(): _serialize_edge_section(subsection)
                for subsection in (
                    subsection.to_section() for subsection in edge_section.elements()
                )
            }
