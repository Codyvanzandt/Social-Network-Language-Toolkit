import pytest
from src.drama_toml_objects.network import Network

# FUNCTIONAL TESTS


# UNIT TESTS


def test_initialization(network):
    default_network = network()
    assert isinstance(default_network, Network)
    assert default_network.weighted == False
    assert default_network.directed == False

    data_dict = {"directed": True, "weighted": True}
    directed_weighted_network = network(data_dict)
    assert directed_weighted_network.weighted == True
    assert directed_weighted_network.directed == True
