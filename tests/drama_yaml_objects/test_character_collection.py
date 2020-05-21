from src.drama_yaml_objects.character_collection import CharacterCollection
import copy


def test_character_collection(character_collection, character):
    # __init__
    empty_character_collection = character_collection()
    assert len(empty_character_collection) == 0

    alice = character("Alice", data_dict={"occupation": "engineer"})
    doctor_alice = character("Alice", data_dict={"occupation": "doctor"})

    # __getitem__, getattr,
    populated_character_collection = character_collection([alice])
    assert populated_character_collection.character_mapping["Alice"] is alice
    assert populated_character_collection.Alice is alice
    assert populated_character_collection.Alice.occupation == "engineer"

    # __setitem__, setattr
    populated_character_collection["Alice"] = doctor_alice
    assert populated_character_collection["Alice"] is doctor_alice
    assert populated_character_collection.Alice is doctor_alice

    # __iter__
    for char in populated_character_collection:
        assert char.name in populated_character_collection.character_mapping

    # __len__
    assert len(populated_character_collection) == 1

    # __contains__
    assert "Alice" in populated_character_collection

    # __eq__
    assert (
        copy.deepcopy(populated_character_collection) == populated_character_collection
    )
    assert populated_character_collection == populated_character_collection
    assert populated_character_collection != "Definitely not a character collection"

    # __delitem__, get
    del populated_character_collection["Alice"]
    assert populated_character_collection.get("Alice", None) is None
    assert hasattr(populated_character_collection, "Alice") == False

    # keys, values, items
    assert set(populated_character_collection.keys()) == set(
        populated_character_collection.character_mapping.keys()
    )
    assert set(populated_character_collection.values()) == set(
        populated_character_collection.character_mapping.values()
    )
    assert set(populated_character_collection.items()) == set(
        populated_character_collection.character_mapping.items()
    )
