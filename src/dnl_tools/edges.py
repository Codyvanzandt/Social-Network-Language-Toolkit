from multidict import MultiDict
from src.dnl_tools.field import Field
from src.dnl_tools.section import Section


class MappedEdges:
    def __init__(self, edges_section):
        self.edges_section = edges_section
        self.edges = list(self.get_edge_list(self.edges_section))

    def get_edge_list(self, edges_section):
        for element in edges_section.data:
            if isinstance(element, Field):
                yield self.convert_to_edge(element, edges_section.divisions)
            elif isinstance(element, Section):
                yield from self.get_edge_list(element)
            else:
                raise ValueError(
                    f"Element {repr(element)} must be a Field (e.g., 'string : YAML value') or a section (e.g., `# string`)."
                )

    def convert_to_edge(self, field, divisions):
        source, target = self.get_source_target(field)
        data = self.get_edge_data(field, divisions)
        return source, target, data

    @staticmethod
    def get_source_target(field):
        try:
            source_character, target_character = field.key.split(".")
            return source_character, target_character
        except ValueError:
            raise ValueError(
                f"Edge {repr(field.key)} must be of the form `character1.character2`"
            )

    def get_edge_data(self, field, divisions):
        return {
            k: v
            for d in (field.data, {"divisions": list(divisions)})
            for k, v in d.items()
        }


class MovementEdges:
    def __init__(self, edges_section):
        self.edges_section = edges_section
        self.edges = list(self.get_edge_list(self.edges_section))
