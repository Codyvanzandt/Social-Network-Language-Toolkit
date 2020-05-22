import yaml
from functools import partial
from src.drama_yaml_objects.play import Play
from src.drama_yaml_objects.network import Network
from src.drama_yaml_objects.character import Character
from src.drama_yaml_objects.character_collection import CharacterCollection


class SocialNetworkConfiguration:
    def __init__(self, data, yaml_loader="full"):
        self.yaml_loader = self._get_yaml_loader(yaml_loader)
        self.data = self._get_drama_yaml_data(data)
        self.play = self._get_play_data()
        self.network = self._get_network_data()
        self.characters = self._get_character_data()

    def _get_yaml_loader(self, yaml_loader):
        key_to_loader = {
            "base": partial(yaml.load, Loader=yaml.BaseLoader),
            "safe": partial(yaml.load, Loader=yaml.SafeLoader),
            "full": partial(yaml.load, Loader=yaml.FullLoader),
            "unsafe": partial(yaml.load, Loader=yaml.UnsafeLoader),
        }
        try:
            return key_to_loader[yaml_loader]
        except KeyError:
            raise SocialNetworkArgumentError(
                parameter="yaml_loader",
                value=yaml_loader,
                possible_values=key_to_loader.keys(),
            )

    def _get_drama_yaml_data(self, drama_yaml_data):
        try:
            return self.yaml_loader(drama_yaml_data) or dict()
        except AttributeError:
            possible_values = ["a string or an open text/yaml file object"]
            raise SocialNetworkArgumentError("data", drama_yaml_data, possible_values)

    def _get_play_data(self):
        return Play(self.data.get("play", None))

    def _get_network_data(self):
        return Network(self.data.get("network", None))

    def _get_character_data(self):
        return CharacterCollection(self._yield_individual_characters())

    def _yield_individual_characters(self):
        all_character_data = self.data.get("characters", dict())
        for character_name, character_datum in all_character_data.items():
            if "play" not in character_datum:
                character_datum["play"] = getattr(
                    self, "play", Play(data={"title": str()})
                )
            yield Character(name=character_name, data=character_datum)


class SocialNetworkArgumentError(Exception):
    def __init__(self, parameter, value, possible_values):
        possible_values = ", ".join(f"`{value}`" for value in possible_values)
        self.message = f"`{value}` is an invalid option for `{parameter}` argument. Valid arguments include {possible_values}"

    def __str__(self):
        return self.message
