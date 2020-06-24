import pytest
import enolib
from src.drama_network import DramaNetwork

# Drama Network
@pytest.fixture
def fake_drama_network(fake_play_string):
    return DramaNetwork(fake_play_string, directed=True)


# DOCUMENT SECTIONS
@pytest.fixture
def section():
    def _section(section_name, field_data):
        formatted_fields = "\n".join(field for field, *_ in field_data)
        section_string = f"""
        # {section_name}
        {formatted_fields}
        """
        return enolib.parse(section_string)

    return _section


# PLAY STRING, PLAY FILE, PLAY DATA, and PLAY DOCUMENT


@pytest.fixture
def fake_play_string():
    return """
# play
title : a title
author : an author
boolean : true
integer : 42
float : 42.0
array : [42, 42, 42]
nested : {nested: nested}

# characters
Flavio : {archetype: innamorati, gender: male}
Isabella : {archetype: innamorati, gender: female}
Pantalone : {archetype: vecchi, gender: male}

# edges
## act1
### scene1
Isabella.Flavio : {type: kissed, weight: 1}
Isabella.Flavio : {type: kissed, weight: 3}
Flavio.Isabella : {type: kissed, weight: 5}
Isabella.Flavio : {type: hit, weight: 7}

### scene2
Isabella.Pantalone : {type: hit, weight: 1}
Isabella.Flavio : {}

## act2
### scene1
Pantalone.Flavio : {}
Flavio.Pantalone : {type: hit, weight: 1}
"""


@pytest.fixture
def fake_play_data():
    return {
        "play": {
            "title": "a title",
            "author": "an author",
            "boolean": True,
            "integer": 42,
            "float": 42.0,
            "array": [42, 42, 42],
            "nested": {"nested": "nested"},
        },
        "characters": {
            "Flavio": {"archetype": "innamorati", "gender": "male",},
            "Isabella": {"archetype": "innamorati", "gender": "female"},
            "Pantalone": {"archetype": "vecchi", "gender": "male"},
        },
        "edges": {
            "act1": {
                "scene1": [
                    ("Isabella", "Flavio", {"type": "kissed", "weight": 1,},),
                    ("Isabella", "Flavio", {"type": "kissed", "weight": 3,},),
                    ("Flavio", "Isabella", {"type": "kissed", "weight": 5,},),
                    ("Isabella", "Flavio", {"type": "hit", "weight": 7,},),
                ],
                "scene2": [
                    ("Isabella", "Pantalone", {"type": "hit", "weight": 1,},),
                    ("Isabella", "Flavio", {},),
                ],
            },
            "act2": {
                "scene1": [
                    ("Pantalone", "Flavio", {},),
                    ("Flavio", "Pantalone", {"type": "hit", "weight": 1,},),
                ]
            },
        },
    }


@pytest.fixture
def fake_play_data_with_edge_data():
    return {
        "play": {
            "title": "a title",
            "author": "an author",
            "boolean": True,
            "integer": 42,
            "float": 42.0,
            "array": [42, 42, 42],
            "nested": {"nested": "nested"},
        },
        "characters": {
            "Flavio": {"archetype": "innamorati", "gender": "male",},
            "Isabella": {"archetype": "innamorati", "gender": "female"},
            "Pantalone": {"archetype": "vecchi", "gender": "male"},
        },
        "edges": [
            (
                "Isabella",
                "Flavio",
                {
                    "type": "kissed",
                    "weight": 1,
                    "divisions": ("act1", "scene1"),
                    "play": "a title",
                },
            ),
            (
                "Isabella",
                "Flavio",
                {
                    "type": "kissed",
                    "weight": 3,
                    "divisions": ("act1", "scene1"),
                    "play": "a title",
                },
            ),
            (
                "Flavio",
                "Isabella",
                {
                    "type": "kissed",
                    "weight": 5,
                    "divisions": ("act1", "scene1"),
                    "play": "a title",
                },
            ),
            (
                "Isabella",
                "Flavio",
                {
                    "type": "hit",
                    "weight": 7,
                    "divisions": ("act1", "scene1"),
                    "play": "a title",
                },
            ),
            (
                "Isabella",
                "Pantalone",
                {
                    "type": "hit",
                    "weight": 1,
                    "divisions": ("act1", "scene2"),
                    "play": "a title",
                },
            ),
            (
                "Isabella",
                "Flavio",
                {"divisions": ("act1", "scene2"), "play": "a title"},
            ),
            (
                "Pantalone",
                "Flavio",
                {"divisions": ("act2", "scene1"), "play": "a title"},
            ),
            (
                "Flavio",
                "Pantalone",
                {
                    "type": "hit",
                    "weight": 1,
                    "divisions": ("act2", "scene1"),
                    "play": "a title",
                },
            ),
        ],
    }


@pytest.fixture
def fake_play_file(fake_play_string, tmp_path):
    fake_file = tmp_path / "fake_file.sdl"
    fake_file.write_text(fake_play_string)
    return fake_file


@pytest.fixture
def fake_play_sdl_doc(fake_play_string):
    return enolib.parse(fake_play_string)
