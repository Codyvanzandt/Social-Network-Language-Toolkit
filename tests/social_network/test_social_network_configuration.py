import pytest
import toml
from functools import partial
from src.social_network.social_network_configuration import SocialNetworkConfiguration
from src.drama_toml_objects.play import Play
from src.drama_toml_objects.network import Network
from src.drama_toml_objects.character import Character
from src.drama_toml_objects.character_collection import CharacterCollection


# FUNCTIONAL TESTS


# UNIT TESTS


def test_initialization(social_network_configuration):
    default_configuration = social_network_configuration()
    assert isinstance(default_configuration, SocialNetworkConfiguration)


def test_get_play_data(social_network_configuration):
    default_network_config = social_network_configuration("examples/fake_play.toml")
    assert isinstance(default_network_config.play, Play)
    assert default_network_config.play.title == "Some Title"
    assert default_network_config.play.author == "Some Author"


def test_get_network_data(social_network_configuration):
    default_network_config = social_network_configuration("examples/fake_play.toml")
    assert isinstance(default_network_config.network, Network)
    assert default_network_config.network.weighted == True
    assert default_network_config.network.directed == True


def test_get_character_data(social_network_configuration):
    default_network_config = social_network_configuration("examples/fake_play.toml")
    assert isinstance(default_network_config.characters, CharacterCollection)
    assert isinstance(default_network_config.characters.Isabella, Character)
    assert default_network_config.characters.Isabella.name == "Isabella"
    assert default_network_config.characters.Isabella.gender == "female"
    assert default_network_config.characters.Isabella.archetype == "innamorati"
