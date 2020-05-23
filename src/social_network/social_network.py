import toml
from src.social_network.social_network_configuration import SocialNetworkConfiguration


class SocialNetwork:
    def __init__(self, data, *args, **kwargs):
        self._social_network_config = SocialNetworkConfiguration(data, *args, **kwargs)
        self.data = self._social_network_config.data
        self.play = self._social_network_config.play
        self.network = self._social_network_config.network
        self.characters = self._social_network_config.characters

    def __repr__(self):
        title = getattr(self.play, "title", str())
        formatted_title = title if title == str() else f"title={repr(title)}"
        return f"{self.__class__.__name__}({formatted_title})"
