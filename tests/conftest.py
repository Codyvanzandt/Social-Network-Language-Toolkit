import pytest
import toml
from src.social_network import SocialNetwork

# FIXTURE CONSTANTS


@pytest.fixture
def valid_drama_toml():
    return toml.load("examples/fake_play.toml")


# FIXTURE FACTORIES


@pytest.fixture
def social_network():
    def _social_network(data=str(), *args, **kwargs):
        return SocialNetwork(data, *args, **kwargs)

    return _social_network
