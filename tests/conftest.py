import pytest
import toml
from src.social_network.social_network import SocialNetwork
from src.social_network.social_network_configuration import SocialNetworkConfiguration
from src.drama_toml_objects.play import Play
from src.drama_toml_objects.network import Network
from src.drama_toml_objects.character import Character
from src.drama_toml_objects.generic_play_object import GenericPlayObject
from src.drama_toml_objects.character_collection import CharacterCollection

# FIXTURE CONSTANTS


@pytest.fixture
def valid_drama_toml():
    return toml.load("examples/fake_play.toml")


# FIXTURE FACTORIES


@pytest.fixture
def generic_play_object():
    def _generic_play_object(data=None):
        return GenericPlayObject(data)

    return _generic_play_object


@pytest.fixture
def play():
    def _play(title=str(), data=None, *args, **kwargs):
        return Play(data=data, *args, **kwargs)

    return _play


@pytest.fixture
def network():
    def _network(*args, **kwargs):
        return Network(*args, **kwargs)

    return _network


@pytest.fixture
def character():
    def _character(name=str(), data=dict(), *args, **kwargs):
        return Character(name=name, data=data, *args, **kwargs)

    return _character


@pytest.fixture
def character_collection():
    def _character_collection(character_iterable=list(), *args, **kwargs):
        return CharacterCollection(character_iterable, *args, **kwargs)

    return _character_collection


@pytest.fixture
def social_network():
    def _social_network(data=str(), *args, **kwargs):
        return SocialNetwork(data, *args, **kwargs)

    return _social_network


@pytest.fixture
def social_network_configuration():
    def _social_network_configuration(data=str(), *args, **kwargs):
        return SocialNetworkConfiguration(data, *args, **kwargs)

    return _social_network_configuration
