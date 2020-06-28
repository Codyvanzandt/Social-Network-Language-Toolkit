import networkx

def sdl_doc_to_graph(sdl_doc, directed=False, multigraph=True):
    new_graph = get_empty_graph(directed, multigraph)
    add_sections_to_graph(sdl_doc, new_graph, exclude=("characters", "edges"))
    add_character_section_to_graph(sdl_doc, new_graph)
    add_edges_section_to_graph(sdl_doc, new_graph)
    return new_graph

def get_empty_graph(directed, multigraph):
    if directed and multigraph:
        return networkx.MultiDiGraph()
    elif directed and not multigraph:
        return networkx.DiGraph()
    elif not directed and multigraph:
        return networkx.MultiGraph()
    elif not directed and not multigraph:
        return networkx.Graph()
    else:
        raise ValueError(f"""Parameters 'directed' and 'multigraph' must be of type bool.
type(directed) == {type(directed)}, type(multigraph) == {type(multigraph)}""")

def add_edges_section_to_graph(sdl_doc, graph):
    pass

def add_character_section_to_graph(sdl_doc, graph):
    character_dict = sdl_doc.data.get("characters", dict())
    for character_name, character_data in character_dict.items():
        graph.add_node(character_name, **character_data)

def add_sections_to_graph(sdl_doc, graph, exclude=tuple()):
    excluded_section_keys = set(exclude)
    for section_key, section_data in sdl_doc.data.items():
        if section_key not in excluded_section_keys:
            graph.graph[section_key] = section_data