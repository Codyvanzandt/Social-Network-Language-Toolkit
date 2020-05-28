import yaml


def serialize_mapped_edges(edges_section):
    for edge in edges_section.elements():
        edge = edge.to_field()
        source_character, target_character = serialize_edge_key(edge.string_key())
        edge_data = edge.required_value(valid_yaml)
        yield (source_character, target_character, edge_data)


def serialize_edge_key(value):
    try:
        source_character, target_character = value.split(".")
        return source_character, target_character
    except ValueError:
        raise ValueError(f"Edge `{value}` must be of the form `character1.character2`")


def valid_yaml(value):
    return yaml.load(value, Loader=yaml.FullLoader)
