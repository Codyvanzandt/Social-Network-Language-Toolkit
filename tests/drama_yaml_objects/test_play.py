import pytest
from src.drama_yaml_objects.play import Play

# FUNCTIONAL TESTS


# UNIT TESTS


def test_initialization(play):
    default_play = play()
    assert isinstance(default_play, Play)
