import itertools

def convert_to_edge_list(social_network):
    edge_list = social_network.data.get("edges", tuple())
    return _convert_to_edge_list(edge_list)

def _convert_to_edge_list(edge_list):
    try:
        yield from _yield_edges(edge_list)
    except ValueError:
        yield from itertools.chain.from_iterable(
            _convert_to_edge_list(new_edge_list)
            for new_edge_list in edge_list.values()
        )

def _yield_edges(edge_list):
    for source_character, target_character, edge_data in edge_list:
            yield (source_character, target_character, edge_data)