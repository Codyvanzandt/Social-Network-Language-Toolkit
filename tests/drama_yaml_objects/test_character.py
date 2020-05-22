import pytest
import copy
from src.drama_yaml_objects.character import Character

# FUNCTIONAL TESTS


# UNIT TESTS


def test_initialization(character):
    default_character = character()
    assert isinstance(default_character, Character)

    data_dict = {"occupation": "engineer"}
    alice_character = character("Alice", data_dict)
    assert alice_character.name == "Alice"
    assert alice_character.occupation == "engineer"


def test_equal(character):
    data_dict = {"occupation": "engineer"}
    alice_character = character("Alice", data_dict)
    assert alice_character == alice_character

    assert copy.deepcopy(alice_character) == alice_character

    assert alice_character != character("Bob", data_dict)

    assert alice_character != "Something that definitely isn't a Character"


def test_repr(character):
    data_dict = {"occupation": "engineer"}
    alice_character = character("Alice", data_dict)
    assert repr(alice_character) == f"Character('Alice')"
