import pytest
import yaml
from functools import partial
from src.social_network.social_network_configuration import (
    SocialNetworkConfiguration,
    SocialNetworkArgumentError,
)
from src.drama_yaml_objects.play import Play
from src.drama_yaml_objects.network import Network
from src.drama_yaml_objects.character import Character
from src.drama_yaml_objects.character_collection import CharacterCollection


# FUNCTIONAL TESTS


# UNIT TESTS


def test_initialization(social_network_configuration):
    default_configuration = social_network_configuration()
    assert isinstance(default_configuration, SocialNetworkConfiguration)


def test_get_yaml_loader(social_network_configuration):
    default_configuration = social_network_configuration()
    default_loader = default_configuration.yaml_loader
    assert default_loader.func == yaml.load
    assert default_loader.keywords == {"Loader": yaml.FullLoader}

    base_config = social_network_configuration(yaml_loader="base")
    base_loader = base_config.yaml_loader
    assert base_loader.func == yaml.load
    assert base_loader.keywords == {"Loader": yaml.BaseLoader}

    safe_config = social_network_configuration(yaml_loader="safe")
    safe_loader = safe_config.yaml_loader
    assert safe_loader.func == yaml.load
    assert safe_loader.keywords == {"Loader": yaml.SafeLoader}

    full_config = social_network_configuration(yaml_loader="full")
    full_loader = full_config.yaml_loader
    assert full_loader.func == yaml.load
    assert full_loader.keywords == {"Loader": yaml.FullLoader}

    unsafe_config = social_network_configuration(yaml_loader="unsafe")
    unsafe_loader = unsafe_config.yaml_loader
    assert unsafe_loader.func == yaml.load
    assert unsafe_loader.keywords == {"Loader": yaml.UnsafeLoader}

    with pytest.raises(SocialNetworkArgumentError) as arg_error:
        bad_loader = "arbitrary_bad_loader"
        bad_config = social_network_configuration(yaml_loader=bad_loader)
    assert f"`{bad_loader}` is an invalid option for `yaml_loader` argument." in str(
        arg_error.value
    )


def test_get_yaml_data(social_network_configuration, valid_drama_yaml):
    valid_string_config = social_network_configuration(data=valid_drama_yaml)
    assert isinstance(valid_string_config.data, dict)

    with open("examples/fake_play.yaml", "r") as yaml_file:
        valid_file_config = social_network_configuration(data=yaml_file)
    assert isinstance(valid_file_config.data, dict)

    with pytest.raises(SocialNetworkArgumentError) as arg_error:
        bad_data = None
        bad_string_config = social_network_configuration(data=bad_data)
    assert f"`{bad_data}` is an invalid option for `data` argument." in str(
        arg_error.value
    )


def test_get_play_data(social_network_configuration):
    default_play_config = social_network_configuration()
    assert isinstance(default_play_config.play, Play)

    play_title = "Some Title"
    play_author = "Some Author"
    play_yaml = f"""
    play:
      title: {play_title}
      author: {play_author}
    """
    populated_play_config = social_network_configuration(data=play_yaml)
    assert populated_play_config.play.title == play_title
    assert populated_play_config.play.author == play_author


def test_get_network_data(social_network_configuration):
    default_network_config = social_network_configuration()
    assert isinstance(default_network_config.network, Network)

    network_yaml = """
    network:
      weighted: true
      directed: true
    """
    populated_network_config = social_network_configuration(data=network_yaml)
    assert populated_network_config.network.weighted == True
    assert populated_network_config.network.directed == True


def test_get_character_data(social_network_configuration):
    default_character_config = social_network_configuration()
    assert isinstance(default_character_config.characters, CharacterCollection)
    assert len(default_character_config.characters) == 0

    character_yaml = """
    characters:
      Alice:
        occupation: engineer
        height:
          value: 65
          unit: inches
      Bob:
        occupation: doctor
    """
    populated_character_config = social_network_configuration(data=character_yaml)
    assert isinstance(populated_character_config.characters, CharacterCollection)
    assert isinstance(populated_character_config.characters.Alice, Character)
    assert populated_character_config.characters.Alice.name == "Alice"
    assert populated_character_config.characters.Alice.occupation == "engineer"
    assert populated_character_config.characters.Alice.height.value == 65
