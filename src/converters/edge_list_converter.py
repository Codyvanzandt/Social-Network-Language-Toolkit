import itertools


def convert_to_edge_list(social_network, play_data=False, division_data=False):
    edge_list = social_network.data.get("edges", tuple())
    play_data = social_network.data.get("play", dict()) if play_data == True else dict()
    include_divison_data = division_data
    division_data = tuple()
    return _convert_to_edge_list(
        edge_list, play_data, division_data, include_divison_data
    )


def _convert_to_edge_list(edge_list, play_data, division_data, include_divison_data):
    try:
        yield from _yield_edges(
            edge_list, play_data, division_data, include_divison_data
        )
    except ValueError:
        yield from itertools.chain.from_iterable(
            _convert_to_edge_list(
                new_edge_list,
                play_data,
                division_data + (new_division,),
                include_divison_data,
            )
            for new_division, new_edge_list in edge_list.items()
        )


def _yield_edges(edge_list, play_data, division_data, include_divison_data):
    for source_character, target_character, edge_data in edge_list:
        if play_data:
            final_play_data = {"play": play_data}
            edge_data = {**edge_data, **final_play_data}
        if include_divison_data:
            final_division_data = {"divisions": division_data}
            edge_data = {**edge_data, **final_division_data}
        yield (source_character, target_character, edge_data)
