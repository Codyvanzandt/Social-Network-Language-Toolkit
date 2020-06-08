import pytest
from src.drama_network import DramaNetwork
from src.utils.edge_utils import get_edges_by_division


def test_get_edges_by_division():
    test_sdl = """
    # edges
    ## act1
    ### scene1
    A.B : {}
    ### scene2
    B.C : {}
    ## act2
    ### scene1
    C.D : {}
    ### scene2
    D.E : {}
    ### scene3
    E.F : {}
    """
    test_network = DramaNetwork(test_sdl)

    # entire acts
    assert list( get_edges_by_division(test_network,"act1") ) == [("A", "B", {}), ("B", "C", {})]
    assert list( get_edges_by_division(test_network,"act2") ) == [("C", "D", {}), ("D", "E", {}), ("E", "F", {})]

    # specific fully-qualified scenes
    assert list( get_edges_by_division(test_network,"act1.scene1") ) == [("A", "B", {}),]
    assert list( get_edges_by_division(test_network,"act1.scene2") ) == [("B", "C", {}),]
    assert list( get_edges_by_division(test_network,"act2.scene1") ) == [("C", "D", {}),]
    assert list( get_edges_by_division(test_network,"act2.scene2") ) == [("D", "E", {}),]
    assert list( get_edges_by_division(test_network,"act2.scene3") ) == [("E", "F", {}),]

    # non-qualified but unambiguous scenes
    assert list( get_edges_by_division(test_network,"scene3") ) == [("E", "F", {}),]

    # non-qualified but ambiguous scenes
    with pytest.raises(ValueError):
        list( get_edges_by_division(test_network,"scene1") )

    with pytest.raises(ValueError):
        list( get_edges_by_division(test_network,"scene2") )

    # missing scenes
    with pytest.raises(ValueError):
        list( get_edges_by_division(test_network,"missing scene") 

