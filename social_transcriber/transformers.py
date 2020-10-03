from networkx import MultiDiGraph, MultiGraph
from lark import Transformer
from collections import ChainMap

NODES_KEY = "nodes"
EDGES_KEY = "edges"
EDGE_DEF_KEY = "edge definitions"

NEWLINE = "\n"


class GraphToSTL:
    def transform(self, graph):
        return (
            self.write_sections(graph)
            + self.write_nodes(graph)
            + self.write_edges(graph)
        )

    def write_edges(self, graph):
        return f"""# {EDGES_KEY}
{NEWLINE.join(f'{source} -- {target}{self.format_edge_data(data)}' for source, target, data in graph.edges(data=True) )}

"""

    def format_edge_data(self, datum):
        return f": {datum}" if datum else ""

    def write_nodes(self, graph):
        return f"""# {NODES_KEY}
{NEWLINE.join(f'{node} : {node_data}' for node, node_data in graph.nodes(data=True))}

"""

    def write_sections(self, graph):
        sections = (
            f"""# {section_title}
{NEWLINE.join( f"{key} : {value}" for key, value in section_data.items()) }
"""
            for section_title, section_data in graph.graph.items()
        )
        return "\n".join(sections) + "\n"


class DictToGraph:
    def transform(self, dictionary, directed=True):
        graph = self.get_empty_graph(directed=directed)
        graph.add_edges_from(self.get_edge_data(dictionary))
        graph.add_nodes_from(self.get_node_data(dictionary))
        graph.graph.update(dictionary)
        return graph

    def get_edge_data(self, dictionary):
        edge_def_data = dictionary.get(EDGE_DEF_KEY, dict())
        edge_data = dictionary.pop(EDGES_KEY, tuple())
        for source, edge_marker, target, data in edge_data:
            pre_defined_data = edge_def_data.get(edge_marker, dict())
            final_data = {**pre_defined_data, **data}
            yield (source, target, final_data)

    def get_node_data(self, dictionary):
        return dictionary.pop(NODES_KEY, dict()).items()

    @staticmethod
    def get_empty_graph(directed=True):
        return MultiDiGraph() if directed else MultiGraph()


class TreeToDict(Transformer):
    def space(self, children):
        return " "

    def SIGNED_NUMBER(self, children):
        (n,) = children
        return float(n)

    def name(self, children):
        return "".join(children)

    def true(self, children):
        return True

    def false(self, children):
        return False

    def list(self, children):
        return list(children)

    def dict(self, children):
        return dict(children)

    def pair(self, children):
        return tuple(children)

    def edge(self, children):
        num_children = len(children)
        if num_children == 3:
            return tuple(children) + (dict(),)
        elif num_children == 4:
            return tuple(children)
        else:
            raise ValueError(f"edge {children} improperly formatted")

    def edge_mark(self, children):
        return "".join(children)

    def section(self, children):
        section_name, *section_data = children
        if section_name == "edges":
            return {section_name: tuple(section_data)}
        else:
            return {section_name: dict(section_data)}

    def document(self, children):
        return dict(ChainMap(*children))
