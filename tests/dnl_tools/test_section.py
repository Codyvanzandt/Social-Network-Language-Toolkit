import pytest
import enolib
from src.dnl_tools.section import Section
from src.dnl_tools.field import Field

FAKE_SECTION_STRING = """# edges
key : {nested : { value : 1 } }
"""
FAKE_SECTION = Section(enolib.parse(FAKE_SECTION_STRING).section("edges"))

BAD_SECTION_STRING = "bad_data"

FAKE_FIELD_STRING = """key : {nested : { value : 1 } }
"""
FAKE_FIELD = Field(enolib.parse(FAKE_FIELD_STRING).elements()[0].to_field())


def test_repr():
    assert (
        repr(FAKE_SECTION)
        == f"<{FAKE_SECTION.__class__.__name__}({repr(FAKE_SECTION.key)}: {repr(FAKE_SECTION.data)})>"
    )


def test_get_key():
    assert FAKE_SECTION.get_key() == "edges"


def test_get_divisions():
    assert FAKE_SECTION.get_divisions(divisions=tuple()) == tuple()
    assert FAKE_SECTION.get_divisions(divisions=("containing_section",)) == (
        "containing_section",
    )


def test_get_data():
    assert FAKE_SECTION.get_data() == [FAKE_FIELD]


def test_to_string():
    assert (
        FAKE_SECTION.to_string()
        == """# edges
key : {'nested': {'value': 1}}"""
    )


def test_to_dict():
    assert FAKE_SECTION.to_dict() == {"edges": {"key": {"nested": {"value": 1}}}}


def test_bad_input():
    with pytest.raises(ValueError):
        bad_section = Section(enolib.parse(BAD_SECTION_STRING))
