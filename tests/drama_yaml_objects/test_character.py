import pytest
import copy
from src.drama_toml_objects.character import Character

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
    alice = character(name="Alice")
    bob = character(name="Bob")

    assert alice == alice
    assert copy.deepcopy(alice) == alice

    assert alice != bob
    assert alice != "Something that definitely isn't a Character"


def test_repr(character):
    data_dict = {"occupation": "engineer"}
    alice_character = character("Alice", data=data_dict)
    assert repr(alice_character) == f"Character('Alice', {data_dict})"
