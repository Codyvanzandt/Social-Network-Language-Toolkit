from multidict import MultiDict
from src.sdl_tools.field import Field


class Section:
    def __init__(self, enolib_section, divisions=tuple()):
        self._enolib_section = enolib_section
        self.key = self.get_key()
        self.divisions = self.get_divisions(divisions)
        self.data = self.get_data()

    def __str__(self):
        return f"<{self.__class__.__name__}({repr(self.key)})>"

    def __repr__(self):
        return f"<{self.__class__.__name__}({repr(self.key)}: {repr(self.values)})>"

    def get_key(self):
        return self._enolib_section.string_key()

    def get_divisions(self, divisions):
        return divisions if self.key == "edges" else divisions + (self.key,)

    def get_data(self):
        section_data = list()
        for element in self._enolib_section.elements():
            if element.yields_field():
                section_data.append(Field(element.to_field()))
            elif element.yields_section():
                section_data.append(
                    Section(element.to_section(), divisions=self.divisions)
                )
            else:
                raise ValueError(
                    f"Element {element.string_key()} must be a Field (e.g., 'string : YAML value') or a section (e.g., `# string`)."
                )
        return section_data

    def to_dict(self):
        is_edges_section = self.key == "edges"
        section_dict = MultiDict()
        for element in self.data:
            section_dict.extend(element.to_dict())
        return (
            {self.key: section_dict}
            if is_edges_section
            else {self.key: dict(section_dict)}
        )
