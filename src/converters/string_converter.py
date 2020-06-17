import yaml
from src.utils.networkx_utils import get_edges_underneath_divisions


def convert_to_string(social_network):
    return (
        convert_play_section_to_string(social_network)
        + convert_characters_section_to_string(social_network)
        + convert_edges_section_to_string(social_network)
    )


def convert_play_section_to_string(social_network):
    return (
        convert_section_name_to_string("play")
        + convert_section_data_to_string(social_network._graph.graph)
        + "\n\n"
    )


def convert_characters_section_to_string(social_network):
    character_data = dict(social_network.nodes(data=True))
    return (
        convert_section_name_to_string("characters")
        + convert_section_data_to_string(character_data)
        + "\n\n"
    )


def convert_edges_section_to_string(social_network):
    edges_data = get_edges_underneath_divisions(social_network._graph)
    return convert_section_name_to_string("edges") + convert_edges_data_to_string(
        edges_data
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
        for (
            source_character,
            target_character,
            edge_data,
        ) in prepare_edge_data_for_stringification(edges_list)
    )


def prepare_edge_data_for_stringification(edges_list):
    return sorted(
        filter_edges_list(edges_list, ("divisions", "play")),
        key=lambda edge: (edge[0], edge[1]),
    )


def filter_edges_list(edges_list, exclude=tuple()):
    for s, t, data in edges_list:
        yield s, t, {k: v for k, v in data.items() if k not in exclude}
