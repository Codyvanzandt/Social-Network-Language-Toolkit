import yaml
from functools import partial
from src.drama_yaml_objects.play import Play
from src.drama_yaml_objects.network import Network
from src.drama_yaml_objects.character import Character
from src.drama_yaml_objects.character_collection import CharacterCollection


class SocialNetworkConfiguration:
    def __init__(self, data, yaml_loader_key="full"):
        self.yaml_loader = self._get_yaml_loader(yaml_loader_key)
        self.data = self._get_drama_yaml_data(data)
        self.play = self._get_play_data()
        self.network = self._get_network_data()
        self.characters = self._get_character_data()

    def _get_yaml_loader(self, yaml_loader_key):
        key_to_loader = {
            "base": partial(yaml.load, Loader=yaml.BaseLoader),
            "safe": partial(yaml.load, Loader=yaml.SafeLoader),
            "full": partial(yaml.load, Loader=yaml.FullLoader),
            "unsafe": partial(yaml.load, Loader=yaml.UnsafeLoader),
        }
        try:
            return key_to_loader[yaml_loader_key]
        except KeyError:
            raise SocialNetworkArgumentError(
                parameter="yaml_loader",
                value=yaml_loader_key,
                possible_values=key_to_loader.keys(),
            )

    def _get_drama_yaml_data(self, drama_yaml_data):
        try:
            return self.yaml_loader(drama_yaml_data) or dict()
        except AttributeError:
            possible_values = ["a string or an open text/yaml file object"]
            raise SocialNetworkArgumentError("data", drama_yaml_data, possible_values)

    def _get_play_data(self):
        possible_play_variable_names = ["play", "Play"]
        for play_name in possible_play_variable_names:
            if play_name in self.data:
                return Play(self.data[play_name])
        else:
            return Play()

    def _get_network_data(self):
        possible_play_network_names = ["network", "Network"]
        for network_name in possible_play_network_names:
            if network_name in self.data:
                return Network(self.data[network_name])
        else:
            return Network()

    def _get_character_data(self):
        possible_character_variable_names = ["characters", "Characters"]
        for character_name in possible_character_variable_names:
            if character_name in self.data:
                return CharacterCollection(
                    Character(char_name, char_data)
                    for char_name, char_data in self.data[character_name].items()
                )
            else:
                return CharacterCollection()


class SocialNetworkArgumentError(Exception):
    def __init__(self, parameter, value, possible_values):
        possible_values = ", ".join(f"`{value}`" for value in possible_values)
        self.message = f"`{value}` is an invalid option for `{parameter}` argument. Valid arguments include {possible_values}"

    def __str__(self):
        return self.message
