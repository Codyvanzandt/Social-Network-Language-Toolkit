import pytest
import copy
from src.drama_yaml_objects.character import Character

# FUNCTIONAL TESTS


# UNIT TESTS


def test_initialization(character):
    default_character = character()
    assert isinstance(default_character, Character)

    data_dict = {"occupation": "engineer"}
    alice_character = character("Alice", data=data_dict)
    assert alice_character.name == "Alice"
    assert alice_character.occupation == "engineer"


def test_equal(character):
    alice0 = character(name="Alice", play="Play0")
    alice1 = character(name="Alice", play="Play1")

    assert alice0 == alice0
    assert copy.deepcopy(alice0) == alice0

    assert alice0 != alice1
    assert alice0 != character("Bob", play="Play0")
    assert alice0 != "Something that definitely isn't a Character"


def test_repr(character):
    data_dict = {"occupation": "engineer"}
    alice_character = character("Alice", data=data_dict)
    assert repr(alice_character) == f"Character('Alice', {data_dict})"
