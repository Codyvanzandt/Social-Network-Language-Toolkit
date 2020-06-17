import itertools


def walk_nested_edges(edge_data, func=None):
    func = func if func is not None else lambda x: x
    if isinstance(edge_data, list):
        return func(edge_data)
    elif isinstance(edge_data, dict):
        return {
            section_key: walk_nested_edges(section_value, func=func)
            for section_key, section_value in edge_data.items()
        }


def flatten_nested_edges(edge_data):
    if isinstance(edge_data, list):
        return edge_data
    else:
        return list(
            itertools.chain.from_iterable(
                flatten_nested_edges(subsection) for _, subsection in edge_data.items()
            )
        )
