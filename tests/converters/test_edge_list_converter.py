import pytest
from src.converters.edge_list_converter import (
    convert_to_edge_list,
    _yield_edges,
)


def test_convert_to_edge_list(fake_drama_network):
    # Case: no play data, no division data
    computed_eges = list(convert_to_edge_list(fake_drama_network))
    expected_edges = list(get_raw_edges(fake_drama_network))
    assert computed_eges == expected_edges

    # Case: play data, no division data
    computed_edges_with_play = convert_to_edge_list(fake_drama_network, play_data=True)
    play_data = {"play": fake_drama_network.data["play"]}
    for expected_edge, computed_edge in zip(expected_edges, computed_edges_with_play):
        e_s, e_t, e_d = expected_edge  # expected source, expected target, expected data
        c_s, c_t, c_d = computed_edge  # computed source, computed target, computed data

        # expected data has play data attached
        e_d = dict(**e_d, **play_data)

        assert e_s == c_s
        assert e_t == c_t
        assert e_d == c_d

    # Case: play data and division data
    computed_edges_with_both = convert_to_edge_list(
        fake_drama_network, play_data=True, division_data=True
    )
    for expected_edge, computed_edge in zip(expected_edges, computed_edges_with_play):
        e_s, e_t, e_d = expected_edge  # expected source, expected target, expected data
        c_s, c_t, c_d = computed_edge  # computed source, computed target, computed data

        # expected data has play data attached
        e_d = dict(**e_d, **play_data)

        assert e_s == c_s
        assert e_t == c_t
        assert e_d == c_d


def test__yield_edges(fake_drama_network):
    # Case: no play data, no division data
    raw_edges = list(get_raw_edges(fake_drama_network))
    computed_edges = _yield_edges(raw_edges, play_data=dict(), division_data=tuple())
    expected_edges = raw_edges
    assert list(computed_edges) == expected_edges

    # Case: play data, no division data
    play_data = fake_drama_network.data["play"]
    computed_edges_with_play = _yield_edges(
        raw_edges, play_data=play_data, division_data=False
    )
    expected_edges = [(s, t, dict(**d, **{"play": play_data})) for s, t, d in raw_edges]
    assert list(computed_edges_with_play) == expected_edges

    # Case: play data and division data
    division_data = ("act1", "scene1")
    computed_edges_with_both = _yield_edges(
        raw_edges, play_data=play_data, division_data=division_data
    )
    expected_edges = [
        (s, t, dict(**d, **{"play": play_data}, **{"divisions": division_data}))
        for s, t, d in raw_edges
    ]
    assert list(computed_edges_with_both) == expected_edges


def get_raw_edges(network):
    for act, act_data in network.data["edges"].items():
        for scene, scene_data in act_data.items():
            for edge in scene_data:
                yield edge
