from src.utils.general_utils import (
    is_dict_subset,
    is_subarray,
    is_container,
    convert_to_container,
)


def test_convert_to_container():
    assert convert_to_container(None, nested=True) is None
    assert convert_to_container(None, nested=False) is None
    assert convert_to_container("A", nested=True) == ("A",)
    assert convert_to_container("A", nested=False) == ("A",)
    assert convert_to_container("A", nested=True) == ("A",)
    assert convert_to_container("A", nested=False) == ("A",)
    assert convert_to_container(("A",), nested=True) == (("A",),)
    assert convert_to_container(("A",), nested=False) == ("A",)


def test_is_container():
    assert not is_container("A")
    assert is_container(("A",))


def test_is_subarray():
    assert is_subarray([1], [1])  # exactly equal
    assert is_subarray([1, 2], [1, 2])  # exactly equal, multiple
    assert is_subarray([1], [1, 2])  # left
    assert is_subarray([1, 2], [1, 2, 3])  # left, multiple
    assert is_subarray([1], [2, 1])  # right
    assert is_subarray([1, 0], [2, 1, 0])  # right, multiple
    assert is_subarray([1], [3, 1, 2])  # middle
    assert is_subarray([1, 0], [2, 1, 0, -1])  # middle, multiple

    assert not is_subarray([], [])  # empty empty
    assert not is_subarray([], [1])  # empty, nonempty
    assert not is_subarray([1], [])  # nonempty, empty
    assert not is_subarray([1], [2])  # not present single
    assert not is_subarray([1, 2], [1, 3])  # not present multiple
    assert not is_subarray([1, 2], [1, 0, 2])  # present, but not sequential
    assert not is_subarray([1, 2], [2, 1])  # present, but reversed


def test_is_dict_subset():
    assert is_dict_subset(dict(), dict())  # empty, empty
    assert is_dict_subset(dict(), {"A": 1})  # empty, non-empty
    assert is_dict_subset({"A": 1}, {"A": 1})  # exact match, single
    assert is_dict_subset({"A": 1, "B": 2}, {"A": 1, "B": 2})  # exact match, multiple
    assert is_dict_subset({"A": 1}, {"A": 1, "B": 2})  # subset single
    assert is_dict_subset({"A": 1, "B": 2}, {"A": 1, "B": 2, "C": 3})  # subset multiple

    assert not is_dict_subset({"A": 1}, dict())  # non-empty,
    assert not is_dict_subset({"A": 1}, {"B": 2})  # disjoint
    assert not is_dict_subset({"A": 1,}, {"A": 2})  # larger set wrong value
    assert not is_dict_subset(
        {"A": 1, "B": 2}, {"A": 1, "B": 1}
    )  # larger set wrong value multiple
    assert not is_dict_subset({"A": 1, "B": 2}, {"A": 1})  # larger set missing element
