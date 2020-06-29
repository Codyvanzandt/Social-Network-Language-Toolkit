from src.dnl_tools.field import Field
import enolib

FAKE_FIELD_STRING = """key : {nested : { value : 1 } }
"""
FAKE_FIELD = Field(enolib.parse(FAKE_FIELD_STRING).elements()[0].to_field())


def test_field_key():
    assert FAKE_FIELD.get_key() == "key"


def test_field_data():
    assert FAKE_FIELD.get_data() == {"nested": {"value": 1}}


def test_to_string():
    assert FAKE_FIELD.to_string() == "key : {'nested': {'value': 1}}"


def test_to_dict():
    assert FAKE_FIELD.to_dict() == {"key": {"nested": {"value": 1}}}


def test_repr():
    assert repr(FAKE_FIELD) == "<Field('key': {'nested': {'value': 1}})>"
