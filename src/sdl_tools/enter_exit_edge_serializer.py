def serialize_enter_exit_edges(edges_section):
    return list( parse_records(edges_section))

def parse_records(edges_section):
    for record in edges_section.split("\n"):
        yield parse_record(record)

def parse_record(record):
    for entry_or_exit in record.split(","):
        yield parse_entry_or_exit( entry_or_exit.strip() )

def parse_entry_or_exit(entry_or_exit):
    entry_exit, character = entry_or_exit[0], entry_exit[1:]
    if entry_exit not in ("+", "-"):
        raise ValueError( f"Entry-Exit record {entry_or_exit} must be formatted as a '+' or '-' followed by a single character name." )
    return entry_exit, character
