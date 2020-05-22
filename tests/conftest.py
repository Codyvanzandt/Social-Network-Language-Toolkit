import pytest
from src.social_network.social_network import SocialNetwork
from src.social_network.social_network_configuration import SocialNetworkConfiguration
from src.drama_yaml_objects.play import Play
from src.drama_yaml_objects.network import Network
from src.drama_yaml_objects.character import Character
from src.drama_yaml_objects.generic_play_object import GenericPlayObject
from src.drama_yaml_objects.character_collection import CharacterCollection

# FIXTURE CONSTANTS


@pytest.fixture
def valid_drama_yaml():
    with open("examples/fake_play.yaml", "r") as fake_play:
        return fake_play.read()


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
    def _character(name=str(), play=str(), data=dict(), *args, **kwargs):
        return Character(name=name, play=play, data=data, *args, **kwargs)

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
