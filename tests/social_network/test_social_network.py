import pytest
from src.social_network.social_network import SocialNetwork
from src.drama_toml_objects.character import Character

# FUNCTIONAL TESTS

TEST_NETWORK = SocialNetwork("examples/fake_play.toml")


def test_data():
    assert isinstance(TEST_NETWORK.data, dict)
    assert TEST_NETWORK.data["play"]["author"] == "Some Author"
    assert TEST_NETWORK.data["play"]["title"] == "Some Title"


def test_play():
    assert TEST_NETWORK.play.author == "Some Author"
    assert TEST_NETWORK.play.title == "Some Title"


def test_network():
    assert TEST_NETWORK.network.directed == True
    assert TEST_NETWORK.network.weighted == True


def test_characters():
    assert [character.name for character in TEST_NETWORK.characters] == [
        "Isabella",
        "Flavio",
        "Pantalone",
    ]

    assert isinstance(TEST_NETWORK.characters.Isabella, Character)
    assert TEST_NETWORK.characters.Isabella.name == "Isabella"
    assert TEST_NETWORK.characters.Isabella.gender == "female"
    assert TEST_NETWORK.characters.Isabella.archetype == "innamorati"

    assert isinstance(TEST_NETWORK.characters.Pantalone, Character)
    assert TEST_NETWORK.characters.Pantalone.name == "Pantalone"
    assert TEST_NETWORK.characters.Pantalone.gender == "male"
    assert TEST_NETWORK.characters.Pantalone.archetype == "vecchi"


# UNIT TESTS


def test_initialization(social_network):
    empty_network = social_network()
    assert isinstance(empty_network, SocialNetwork)
