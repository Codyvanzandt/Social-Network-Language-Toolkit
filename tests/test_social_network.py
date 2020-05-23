import pytest
from src.social_network import SocialNetwork

# FUNCTIONAL TESTS

TEST_NETWORK = SocialNetwork("examples/fake_play.toml")


def test_play():
    assert isinstance(TEST_NETWORK.data, dict)
    assert TEST_NETWORK.data["play"]["author"] == "Some Author"
    assert TEST_NETWORK.data["play"]["title"] == "Some Title"


def test_network():
    assert TEST_NETWORK["network"]["directed"] == True
    assert TEST_NETWORK["network"]["weighted"] == True


def test_characters():
    assert [character for character in TEST_NETWORK["characters"].keys()] == [
        "Isabella",
        "Flavio",
        "Pantalone",
    ]

    assert TEST_NETWORK["characters"]["Isabella"]["gender"] == "female"
    assert TEST_NETWORK["characters"]["Isabella"]["archetype"] == "innamorati"

    assert TEST_NETWORK["characters"]["Pantalone"]["gender"] == "male"
    assert TEST_NETWORK["characters"]["Pantalone"]["archetype"] == "vecchi"


# UNIT TESTS


def test_initialization(social_network):
    empty_network = social_network("examples/fake_play.toml")
    assert isinstance(empty_network, SocialNetwork)
