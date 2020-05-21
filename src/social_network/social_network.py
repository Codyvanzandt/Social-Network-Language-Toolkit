import yaml
from src.social_network.social_network_configuration import SocialNetworkConfiguration


class SocialNetwork:
    def __init__(self, data, *args, **kwargs):
        self._social_network_config = SocialNetworkConfiguration(data, *args, **kwargs)
        self.yaml_loader = self._social_network_config.yaml_loader
        self.yaml_data = self._social_network_config.data
        self.play = self._social_network_config.play
        self.network = self._social_network_config.network
        self.characters = self._social_network_config.characters
