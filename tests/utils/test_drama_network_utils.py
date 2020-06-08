import pytest
from src.drama_network import DramaNetwork
from src.utils.drama_network_utils import get_edges_by_division, is_subarray


def test_is_subarray():
    assert is_subarray([1], [1])  # exactly equal
    assert is_subarray([1, 2], [1, 2])  # exactly equal, multiple
    assert is_subarray([1], [1, 2])  # left
    assert is_subarray([1, 2], [1, 2, 3])  # left, multiple
    assert is_subarray([1], [2, 1])  # right
    assert is_subarray([1, 0], [2, 1, 0])  # right, multiple
    assert is_subarray([1], [3, 1, 2])  # middle
    assert is_subarray([1, 0], [2, 1, 0, -1])  # middle, multiple

    assert not is_subarray([], [])  # empty empty
    assert not is_subarray([], [1])  # empty, nonempty
    assert not is_subarray([1], [])  # nonempty, empty
    assert not is_subarray([1], [2])  # not present single
    assert not is_subarray([1, 2], [1, 3])  # not present multiple
    assert not is_subarray([1, 2], [1, 0, 2])  # present, but not sequential
    assert not is_subarray([1, 2], [2, 1])  # present, but reversed


def test_get_edges_by_division():
    test_sdl = """
    # edges
    ## act1
    ### scene1
    A.B : {}
    ### scene2
    B.C : {}
    ## act2
    ### scene1
    C.D : {}
    ### scene2
    D.E : {}
    ### scene3
    E.F : {}
    """
    test_network = DramaNetwork(test_sdl)

    # entire acts
    assert list(get_edges_by_division(test_network, "act1")) == [
        ("A", "B", {"divisions": ("act1", "scene1")}),
        ("B", "C", {"divisions": ("act1", "scene2")}),
    ]
    assert list(get_edges_by_division(test_network, "act2")) == [
        ("C", "D", {"divisions": ("act2", "scene1")}),
        ("D", "E", {"divisions": ("act2", "scene2")}),
        ("E", "F", {"divisions": ("act2", "scene3")}),
    ]

    # specific fully-qualified scenes
    assert list(get_edges_by_division(test_network, "act1.scene1")) == [
        ("A", "B", {"divisions": ("act1", "scene1")}),
    ]
    assert list(get_edges_by_division(test_network, "act1.scene2")) == [
        ("B", "C", {"divisions": ("act1", "scene2")}),
    ]
    assert list(get_edges_by_division(test_network, "act2.scene1")) == [
        ("C", "D", {"divisions": ("act2", "scene1")}),
    ]
    assert list(get_edges_by_division(test_network, "act2.scene2")) == [
        ("D", "E", {"divisions": ("act2", "scene2")}),
    ]
    assert list(get_edges_by_division(test_network, "act2.scene3")) == [
        ("E", "F", {"divisions": ("act2", "scene3")}),
    ]

    # divisions that aren't fully qualified return everything that matches
    assert list(get_edges_by_division(test_network, "scene3")) == [
        ("E", "F", {"divisions": ("act2", "scene3")}),
    ]

    assert list(get_edges_by_division(test_network, "scene1")) == [
        ("A", "B", {"divisions": ("act1", "scene1")}),
        ("C", "D", {"divisions": ("act2", "scene1")}),
    ]
