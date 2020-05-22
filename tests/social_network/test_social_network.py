import pytest
import yaml
from src.social_network.social_network import SocialNetwork
from src.drama_yaml_objects.character import Character

TEST_DRAMA_YAML = """
play:
  author: AUTHOR
  title: TITLE
  multi:
    level:
      data: DATA

network:
  directed: true
  weighted: true

characters:
  Alice:
    key: ALICE_VALUE
    multi:
      level:
        data: ALICE_DATA
  Bob:
    key: BOB_VALUE
"""

TEST_NETWORK = SocialNetwork(TEST_DRAMA_YAML)

# FUNCTIONAL TESTS


def test_yaml_loader():
    assert TEST_NETWORK.yaml_loader(TEST_DRAMA_YAML) == yaml.load(
        TEST_DRAMA_YAML, Loader=yaml.FullLoader
    )


def test_data():
    assert isinstance(TEST_NETWORK.data, dict)
    assert TEST_NETWORK.data["play"]["author"] == "AUTHOR"


def test_play():
    assert TEST_NETWORK.play.author == "AUTHOR"
    assert TEST_NETWORK.play.title == "TITLE"
    assert TEST_NETWORK.play.multi.level.data == "DATA"


def test_network():
    assert TEST_NETWORK.network.directed == True
    assert TEST_NETWORK.network.weighted == True


def test_characters():
    assert [character.name for character in TEST_NETWORK.characters] == ["Alice", "Bob"]

    assert isinstance(TEST_NETWORK.characters.Alice, Character)
    assert TEST_NETWORK.characters.Alice.name == "Alice"
    assert TEST_NETWORK.characters.Alice.key == "ALICE_VALUE"
    assert TEST_NETWORK.characters.Alice.multi.level.data == "ALICE_DATA"

    assert isinstance(TEST_NETWORK.characters.Bob, Character)
    assert TEST_NETWORK.characters.Bob.name == "Bob"
    assert TEST_NETWORK.characters.Bob.key == "BOB_VALUE"


# UNIT TESTS


def test_initialization(social_network):
    empty_network = social_network()
    assert isinstance(empty_network, SocialNetwork)
