import pytest
from pprint import pformat
from src.drama_network import DramaNetwork
from src.converters.string_converter import convert_to_string
from src.converters.edge_list_converter import convert_to_edge_list
from src.converters.sdl_file_converter import convert_to_file
from src.converters.networkx_converter import convert_to_networkx
from src.utils.networkx_utils import get_subgraph, get_divisions
from networkx.algorithms.isomorphism import is_isomorphic


def test_init(fake_drama_network, fake_play_data):
    assert fake_drama_network
    assert fake_drama_network._data == fake_play_data
    assert is_isomorphic(
        fake_drama_network._graph,
        convert_to_networkx(
            fake_drama_network, directed=False, play_data=True, division_data=True
        ),
    )


def test_iter(fake_drama_network):
    assert list(iter(fake_drama_network)) == list(iter(fake_drama_network._graph))


def test_contains(fake_drama_network):
    assert ("Isabella" in fake_drama_network) == (
        "Isabella" in fake_drama_network._graph
    )
    assert ("Missing Character" in fake_drama_network) == (
        "Missing Character" in fake_drama_network._graph
    )


def test_len(fake_drama_network):
    assert len(fake_drama_network) == len(fake_drama_network._graph)


def test_get_item(fake_drama_network):
    assert (fake_drama_network["Isabella"]) == (fake_drama_network._graph["Isabella"])

    with pytest.raises(KeyError):
        fake_drama_network["Missing Character"]

    with pytest.raises(KeyError):
        fake_drama_network._graph["Missing Character"]


def test_get_attr(fake_drama_network):
    assert (
        fake_drama_network.neighbors.__self__
        is fake_drama_network._graph.neighbors.__self__
    )


def test_str(fake_drama_network):
    expected_str = "DramaNetwork(a title)"
    assert str(fake_drama_network) == expected_str


def test_play(fake_drama_network):
    assert fake_drama_network.play() == fake_drama_network._graph.graph


def test_characters(fake_drama_network):
    assert fake_drama_network.characters(
        data=True, default=None
    ) == fake_drama_network._graph.nodes(data=True, default=None)
    assert fake_drama_network.characters(
        data=False, default=False
    ) == fake_drama_network._graph.nodes(data=False, default=None)


def test_divisions(fake_drama_network):
    assert fake_drama_network.divisions() == get_divisions(fake_drama_network._graph)

    expected_level_two_divisions = [
        division
        for division in get_divisions(fake_drama_network._graph)
        if len(division.split(".")) == 2
    ]
    assert fake_drama_network.divisions(level=2) == expected_level_two_divisions


def test_edges(fake_drama_network):
    assert list(fake_drama_network.edges()) == list(fake_drama_network._graph.edges())
    assert list(fake_drama_network.edges(nbunch="Isabella")) == list(
        fake_drama_network._graph.edges(nbunch="Isabella")
    )
    assert list(fake_drama_network.edges(nbunch="Isabella", data="archetype")) == list(
        fake_drama_network._graph.edges(nbunch="Isabella", data="archetype")
    )
    assert list(
        fake_drama_network.edges(nbunch="Isabella", data="missing data", default=1)
    ) == list(
        fake_drama_network._graph.edges(
            nbunch="Isabella", data="missing data", default=1
        )
    )


def test_subnetwork(fake_drama_network):
    assert is_isomorphic(
        fake_drama_network.subnetwork()._graph, get_subgraph(fake_drama_network._graph)
    )

    assert is_isomorphic(
        fake_drama_network.subnetwork(characters="Isabella")._graph,
        get_subgraph(fake_drama_network._graph, nodes=["Isabella"]),
    )

    assert is_isomorphic(
        fake_drama_network.subnetwork(
            characters="Isabella", divisions="act1.scene1"
        )._graph,
        get_subgraph(
            fake_drama_network._graph, divisions=["act1.scene1"], nodes=["Isabella"]
        ),
    )

    assert is_isomorphic(
        fake_drama_network.subnetwork(
            characters="Isabella", divisions="act1.scene1", edges=("Isabella", "Flavio")
        )._graph,
        get_subgraph(
            fake_drama_network._graph,
            divisions=["act1.scene1"],
            nodes=["Isabella"],
            edges=[("Isabella", "Flavio")],
        ),
    )

    assert is_isomorphic(
        fake_drama_network.subnetwork(
            characters="Isabella",
            divisions="act1.scene1",
            edges=("Isabella", "Flavio"),
            edge_data={"type": "kissed"},
        )._graph,
        get_subgraph(
            fake_drama_network._graph,
            divisions=["act1.scene1"],
            nodes=["Isabella"],
            edges=[("Isabella", "Flavio")],
            edge_data={"type": "kissed"},
        ),
    )


def test_to_sdl_string(fake_drama_network):
    assert fake_drama_network.to_sdl_string() == convert_to_string(fake_drama_network)


def test_to_file(fake_drama_network, tmp_path):
    from_to_file = tmp_path / "from_file.sdl"
    from_convert_to_file = tmp_path / "from_convert_to_file.sdl"
    fake_drama_network.to_file(path=from_to_file)
    convert_to_file(fake_drama_network, from_convert_to_file)
    assert (
        DramaNetwork(from_to_file.absolute())._data
        == DramaNetwork(from_convert_to_file.absolute())._data
    )


def test__load_sdl_data(
    fake_drama_network, fake_play_data, fake_play_file, fake_play_string
):
    assert (
        fake_drama_network._load_sdl_data(fake_play_file)["play"]
        == fake_play_data["play"]
    )
    assert (
        fake_drama_network._load_sdl_data(fake_play_file)["characters"]
        == fake_play_data["characters"]
    )
    assert (
        fake_drama_network._load_sdl_data(fake_play_file)["edges"]
        == fake_play_data["edges"]
    )
    assert (
        fake_drama_network._load_sdl_data(fake_play_string)["play"]
        == fake_play_data["play"]
    )
    assert (
        fake_drama_network._load_sdl_data(fake_play_string)["characters"]
        == fake_play_data["characters"]
    )
    assert (
        fake_drama_network._load_sdl_data(fake_play_string)["edges"]
        == fake_play_data["edges"]
    )
