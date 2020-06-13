import yaml
from src.utils.networkx_utils import get_edges_underneath_divisions


def convert_to_string(social_network):
    return (
        convert_section_to_string(social_network, "play")
        + convert_section_to_string(social_network, "characters")
        + convert_edges_section_to_string(social_network)
    )


def convert_section_to_string(social_network, section_name):
    section_data = social_network._data.get(section_name, dict())
    return (
        convert_section_name_to_string(section_name)
        + convert_section_data_to_string(section_data)
        + "\n\n"
    )


def convert_section_name_to_string(section_name, section_level=1):
    return f"{'#'*section_level} {section_name}\n"


def convert_section_data_to_string(section_data):
    return "\n".join(
        f"{data_key} : {convert_yaml_data_to_string(yaml_data)}"
        for data_key, yaml_data in section_data.items()
    )


def convert_yaml_data_to_string(yaml_data):
    return (
        yaml.dump(yaml_data, default_flow_style=True)
        .replace("...\n", "")
        .replace("\n", "")
    )


def convert_edges_section_to_string(social_network):
    edges_data = social_network._data.get("edges", dict())
    # edges_data = get_edges_underneath_divisions(social_network._graph)
    return convert_section_name_to_string("edges") + convert_edges_data_to_string(
        edges_data
    )


def prepare_edge_data_for_stringification(edges_data):
    filtered_edges_data = filter_edges_data(edges_data, ("divisions", "play"))
    return group_edges(filtered_edges_data)


def filter_edges_data(edges_data, exclude=tuple()):
    return edges_data


def group_edges(edges_data):
    return edges_data


def convert_edges_data_to_string(edges_data, section_level=1):
    try:
        return convert_edges_list_to_string(edges_data)
    except ValueError:
        return "\n".join(
            convert_section_name_to_string(sub_section, section_level + 1)
            + convert_edges_data_to_string(sub_section_data, section_level + 1)
            for sub_section, sub_section_data in edges_data.items()
        )


def convert_edges_list_to_string(edges_list):
    return "\n".join(
        f"{source_character}.{target_character} : {convert_yaml_data_to_string(edge_data)}"
        for source_character, target_character, edge_data in edges_list
    )
