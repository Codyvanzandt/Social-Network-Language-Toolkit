import itertools


def walk_nested_edges(edge_section, func=None):
    func = func if func is not None else lambda x: x
    if isinstance(edge_section, list):
        return func(edge_section)
    elif isinstance(edge_section, dict):
        return {
            section_key: walk_nested_edges(section_value, func=func)
            for section_key, section_value in edge_section.items()
        }


def flatten_nested_edges(edge_section):
    if isinstance(edge_section, list):
        return edge_section
    else:
        return list(
            itertools.chain.from_iterable(
                flatten_nested_edges(subsection)
                for _, subsection in edge_section.items()
            )
        )
