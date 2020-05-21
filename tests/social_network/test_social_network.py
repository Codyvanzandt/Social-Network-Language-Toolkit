import pytest
from src.social_network.social_network import SocialNetwork

# FUNCTIONAL TESTS


def test_play_data():
    pass


# UNIT TESTS


def test_initialization(social_network):
    empty_network = social_network()
    assert isinstance(empty_network, SocialNetwork)
