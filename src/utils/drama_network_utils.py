import copy


def get_subgraph_data(drama_network, subgraph):
    old_data = copy.deepcopy(drama_network._data)
    return {
        "play": get_subgraph_play_data(old_data),
        "characters": get_subgraph_character_data(old_data, subgraph),
        "edges": get_subgraph_edges_data(subgraph),
    }


def get_subgraph_play_data(data):
    new_play_data = data.get("play", dict())
    new_play_data["subgraph"] = True
    return new_play_data


def get_subgraph_character_data(data, subgraph):
    new_character_data = data.get("characters", dict())
    return {
        character: character_data
        for character, character_data in new_character_data.items()
        if character in subgraph.nodes()
    }


def get_subgraph_edges_data(subgraph):
    return [(s, t, d) for s, t, d in subgraph.edges(data=True)]
