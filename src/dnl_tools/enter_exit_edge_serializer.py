from itertools import combinations, product, chain
from ordered_set import OrderedSet

EXEUNT = "EXEUNT"


def serialize_enter_exit_edges(edges_data):
    on_stage, entrants, exiters = OrderedSet(), OrderedSet(), OrderedSet()
    for enter_exit_record in edges_data:
        parsed_entries_and_exits = parse_entries_and_exits(enter_exit_record)
        # Add all entrants and exiters
        entrants, exiters = get_entrants_and_exiters(parsed_entries_and_exits)

        # EXEUNT -> Everyone on stage is now an exiter
        if EXEUNT in exiters:
            exiters.update(on_stage)

        # Remove all exiters from stage
        on_stage = on_stage - exiters

        yield from generate_edges(on_stage, entrants)

        # Move the entrants on stage, clear the entrants and exiters to prepare for the next scene
        on_stage.update(entrants)
        entrants, exiters = OrderedSet(), OrderedSet()


def parse_entries_and_exits(entries_and_exits):
    for entry_or_exit in entries_and_exits.split(","):
        if entry_or_exit and not entry_or_exit.isspace():
            yield parse_entry_or_exit(entry_or_exit)


def get_entrants_and_exiters(parsed_entries_and_exits):
    entrants = OrderedSet()
    exiters = OrderedSet()
    for entry_or_exit, character in parsed_entries_and_exits:
        if entry_or_exit == "+":
            entrants.add(character)
        elif entry_or_exit == "-":
            exiters.add(character)
        else:
            raise ValueError(
                f"Entry-Exit record '{entry_or_exit}{character}' must be formatted as a '+' or '-' followed by a single character name."
            )
    return entrants, exiters


def parse_entry_or_exit(entry_or_exit):
    stripped_entry_or_exit = entry_or_exit.strip()
    if stripped_entry_or_exit == EXEUNT:
        return "-", EXEUNT
    else:
        entry_exit, character = stripped_entry_or_exit[-1], stripped_entry_or_exit[:-1]
        if entry_exit not in ("+", "-"):
            raise ValueError(
                f"Entry-Exit record {entry_or_exit} must be formatted as a '+' or '-' followed by a single character name."
            )
        return entry_exit, character


def generate_edges(on_stage, entrants):
    entrants_with_each_other = combinations(entrants, 2)
    entrants_with_on_stage = product(entrants, on_stage)
    for source_character, target_character in chain(
        entrants_with_each_other, entrants_with_on_stage
    ):
        yield (source_character, target_character, dict())
