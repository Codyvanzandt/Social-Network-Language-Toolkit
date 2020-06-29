import pytest
from itertools import product, combinations, chain
from src.dnl_tools.enter_exit_edge_serializer import (
    generate_edges,
    parse_entry_or_exit,
    parse_entries_and_exits,
    get_entrants_and_exiters,
    serialize_enter_exit_edges,
)


@pytest.mark.parametrize(
    "edges_data,expected_edges",
    [
        (["A+"], list()),
        (["A+,B+"], [("A", "B")]),
        (["A+,B+,C+"], [("A", "B"), ("A", "C"), ("B", "C")]),
        (["A+,B+,C+", "C-"], [("A", "B"), ("A", "C"), ("B", "C"), ("A", "B")]),
        (
            ["A+,B+,C+", "EXEUNT", "D+,E+"],
            [("A", "B"), ("A", "C"), ("B", "C"), ("D", "E")],
        ),
        (["A+", "B+", "C+"], [("A", "B"), ("A", "C"), ("B", "C")]),
    ],
)
def test_serialize_enter_exit_edges(edges_data, expected_edges):
    for edge, expected_edge in zip(
        serialize_enter_exit_edges(edges_data), expected_edges
    ):
        assert set(edge[:2]) == set(expected_edge)


@pytest.mark.parametrize(
    "entries_and_exits, entrants, exiters",
    [
        (list(), set(), set()),
        ([("+", "A")], {"A"}, set()),
        ([("-", "A")], set(), {"A"}),
        ([("+", "A"), ("-", "B")], {"A"}, {"B"}),
        ([("+", "A"), ("+", "B"), ("+", "A"), ("+", "B")], {"A", "B"}, set()),
        ([("+", "A"), ("+", "B"), ("-", "A"), ("-", "B")], {"A", "B"}, {"A", "B"}),
    ],
)
def test_get_entrants_and_exiters(entries_and_exits, entrants, exiters):
    assert get_entrants_and_exiters(entries_and_exits) == (entrants, exiters)


def test_get_entrants_and_exiters_raises():
    with pytest.raises(
        ValueError, match=r"Entry-Exit record '.*' must be formatted as .*"
    ):
        get_entrants_and_exiters(["A$"])


@pytest.mark.parametrize(
    "entries_and_exits", ["A+", "A+,", "A+,B+,", "A+, B+," " A+, B+, "]
)
def test_parse_entries_and_exits(entries_and_exits):
    expected_result = [
        parse_entry_or_exit(entry_exit)
        for entry_exit in entries_and_exits.split(",")
        if entry_exit and not entry_exit.isspace()
    ]
    assert list(parse_entries_and_exits(entries_and_exits)) == expected_result


@pytest.mark.parametrize(
    "entry_or_exit", ["A+", "A-", "'A B C'-", "EXEUNT"],
)
def test_parse_entry_or_exit(entry_or_exit):
    if entry_or_exit == "EXEUNT":
        assert parse_entry_or_exit(entry_or_exit) == ("-", "EXEUNT")
    else:
        assert parse_entry_or_exit(entry_or_exit) == (
            entry_or_exit[-1],
            entry_or_exit[:-1],
        )


def test_parse_entry_or_exit_raises():
    with pytest.raises(
        ValueError, match=r"Entry-Exit record .* must be formatted as .*",
    ):
        parse_entry_or_exit("A")


@pytest.mark.parametrize(
    "onstage, entrants",
    [
        (tuple(), tuple()),
        (("A", "B", "C"), tuple()),
        (tuple(), ("A", "B", "C")),
        (("A", "B", "C"), ("D", "E", "F")),
    ],
)
def test_generate_edges(onstage, entrants):
    expected_edges = chain(combinations(entrants, 2), product(entrants, onstage))
    expected_edges_with_data = (
        (source, target, dict()) for source, target in expected_edges
    )
    assert list(generate_edges(onstage, entrants)) == list(expected_edges_with_data)
