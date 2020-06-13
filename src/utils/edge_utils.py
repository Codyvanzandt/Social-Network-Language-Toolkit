def walk_nested_edges(edge_data, func=None):
    func = lambda x: x if func is None else func
    if isinstance(edge_data, list):
        return func(edge_data)
    elif isinstance(edge_data, dict):
        return {
            section_key : walk_nested_edges(section_value)
            for section_key, section_value in edge_data.items()
        }