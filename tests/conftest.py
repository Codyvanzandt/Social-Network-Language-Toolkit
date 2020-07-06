import pytest
import enolib
from src.drama_network import DramaNetwork
from src.dnl_tools.dnl_document import DNLDocument


@pytest.fixture
def fake_drama_network(fake_play_string):
    return DramaNetwork(fake_play_string, directed=True)


@pytest.fixture
def dnl_doc_factory():
    def make_dnl_doc(data):
        return DNLDocument(data)

    return make_dnl_doc


# PLAY STRING, PLAY FILE, PLAY DATA, and PLAY DOCUMENT


@pytest.fixture
def fake_play_file(fake_play_string, tmp_path):
    fake_file = tmp_path / "fake_file.dnl"
    fake_file.write_text(fake_play_string)
    return fake_file


@pytest.fixture
def fake_play_string():
    return """
# play
title : a title
author : an author
boolean : True
integer : 42
float : 42.0
array : [42, 42, 42]
nested : {'nested': 'nested'}

# characters
Flavio : {'archetype': 'innamorati', 'gender': 'male'}
Isabella : {'archetype': 'innamorati', 'gender': 'female'}
Pantalone : {'archetype': 'vecchi', 'gender': 'male'}

# edges
## act1
### scene1
Isabella.Flavio : {'type': 'kissed', 'weight': 1}
Isabella.Flavio : {'type': 'kissed', 'weight': 3}
Flavio.Isabella : {'type': 'kissed', 'weight': 5}
Isabella.Flavio : {'type': 'hit', 'weight': 7}
### scene2
Isabella.Pantalone : {'type': 'hit', 'weight': 1}
Isabella.Flavio : {}
## act2
### scene1
Pantalone.Flavio : {}
Flavio.Pantalone : {'type': 'hit', 'weight': 1}
"""


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
                {"type": "kissed", "weight": 1, "divisions": ["act1", "scene1"],},
            ),
            (
                "Isabella",
                "Flavio",
                {"type": "kissed", "weight": 3, "divisions": ["act1", "scene1"],},
            ),
            (
                "Flavio",
                "Isabella",
                {"type": "kissed", "weight": 5, "divisions": ["act1", "scene1"],},
            ),
            (
                "Isabella",
                "Flavio",
                {"type": "hit", "weight": 7, "divisions": ["act1", "scene1"],},
            ),
            (
                "Isabella",
                "Pantalone",
                {"type": "hit", "weight": 1, "divisions": ["act1", "scene2"],},
            ),
            ("Isabella", "Flavio", {"divisions": ["act1", "scene2"],},),
            ("Pantalone", "Flavio", {"divisions": ["act2", "scene1"],},),
            (
                "Flavio",
                "Pantalone",
                {"type": "hit", "weight": 1, "divisions": ["act2", "scene1"],},
            ),
        ],
    }
