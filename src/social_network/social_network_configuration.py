import toml
from functools import partial
from src.drama_toml_objects.play import Play
from src.drama_toml_objects.network import Network
from src.drama_toml_objects.character import Character
from src.drama_toml_objects.character_collection import CharacterCollection


class SocialNetworkConfiguration:
    def __init__(self, data):
        self.data = self._load_drama_toml(data)
        self.play = self._get_play_data()
        self.network = self._get_network_data()
        self.characters = self._get_character_data()

    def _load_drama_toml(self, data):
        try:
            return toml.load(data)
        except FileNotFoundError:
            return toml.loads(data)

    def _get_play_data(self):
        return Play(self.data.get("play", None))

    def _get_network_data(self):
        return Network(self.data.get("network", None))

    def _get_character_data(self):
        return CharacterCollection(self._yield_individual_characters())

    def _yield_individual_characters(self):
        all_character_data = dict(self.data.get("characters", dict()))
        for character_name, character_datum in all_character_data.items():
            if "play" not in character_datum:
                character_datum["play"] = getattr(
                    self, "play", Play(data={"title": str()})
                )
            yield Character(name=character_name, data=character_datum)
