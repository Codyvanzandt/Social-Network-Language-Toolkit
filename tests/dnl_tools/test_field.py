from src.dnl_tools.field import Field
import enolib


def make_field(enolib_str):
    return Field(enolib.parse(enolib_str).elements()[0].to_field())


FAKE_FIELD_STRING = """key : {nested : { value : 1 } }
"""
OTHER_FAKE_FIELD_STRING = """key : {nested : { value : 2 } }
"""

FAKE_FIELD = make_field(FAKE_FIELD_STRING)
OTHER_FAKE_FIELD = make_field(OTHER_FAKE_FIELD_STRING)


def test_eq():
    assert FAKE_FIELD == FAKE_FIELD
    assert FAKE_FIELD != OTHER_FAKE_FIELD


def test_field_key():
    assert FAKE_FIELD.get_key() == "key"


def test_field_data():
    assert FAKE_FIELD.get_data() == {"nested": {"value": 1}}


def test_to_string():
    assert FAKE_FIELD.to_string() == "key : {'nested': {'value': 1}}"


def test_to_dict():
    assert FAKE_FIELD.to_dict() == {"key": {"nested": {"value": 1}}}


def test_repr():
    assert (
        repr(FAKE_FIELD)
        == f"<{FAKE_FIELD.__class__.__name__}({repr(FAKE_FIELD.key)}: {repr(FAKE_FIELD.data)})>"
    )
