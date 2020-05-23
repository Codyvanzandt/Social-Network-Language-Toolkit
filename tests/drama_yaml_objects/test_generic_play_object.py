import pytest
from src.drama_toml_objects.generic_play_object import GenericPlayObject

# UNIT TESTS


def test_initialization(generic_play_object):
    empty_generic_object = generic_play_object()
    assert isinstance(empty_generic_object, GenericPlayObject)


def test_basic_data_storage(generic_play_object):
    test_data = {"a": 1, "b": {"c": 2, "d": 3}}
    non_empty_generic_object = generic_play_object(test_data)
    assert non_empty_generic_object.a == 1
    assert non_empty_generic_object.b.c == 2
    assert non_empty_generic_object.b.d == 3


def test_repr(generic_play_object):
    assert repr(generic_play_object()) == r"GenericPlayObject(data={})"
