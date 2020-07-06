import networkx
from src.utils.edge_utils import combine_all_edges, edges_equal, combine_edges


def dnl_doc_to_graph(dnl_doc, directed=False):
    new_graph = get_empty_graph(directed=directed, multigraph=True)
    add_sections_to_graph(dnl_doc, new_graph, exclude=("characters", "edges"))
    add_characters_section_to_graph(dnl_doc, new_graph)
    add_edges_section_to_graph(dnl_doc, new_graph)
    return new_graph


def get_empty_graph(directed, multigraph):
    if directed == True and multigraph == True:
        return networkx.MultiDiGraph()
    elif directed == True and multigraph == False:
        return networkx.DiGraph()
    elif directed == False and multigraph == True:
        return networkx.MultiGraph()
    elif directed == False and multigraph == False:
        return networkx.Graph()
    else:
        raise ValueError(
            f"""Parameters 'directed' and 'multigraph' must be of type bool.
type(directed) == {type(directed)}, type(multigraph) == {type(multigraph)}"""
        )


def add_edges_section_to_graph(dnl_doc, graph):
    edges = dnl_doc.data.get("edges", tuple())
    graph.add_edges_from(edges)


def add_characters_section_to_graph(dnl_doc, graph):
    character_dict = dnl_doc.data.get("characters", dict())
    for character_name, character_data in character_dict.items():
        graph.add_node(character_name, **character_data)


def add_sections_to_graph(dnl_doc, graph, exclude=tuple()):
    excluded_section_keys = set(exclude)
    for section_key, section_data in dnl_doc.data.items():
        if section_key not in excluded_section_keys:
            graph.graph[section_key] = section_data
