import enolib
from multidict import MultiDict
from src.dnl_tools.section import Section
from src.dnl_tools.edges import MappedEdges


class DNLDocument:
    def __init__(self, data):
        self._input_data = data if data is not None else str()
        self._loaded_data = self.load_data()
        self._parsed_data = self.parse_data()
        self._intermediate_data = self.serialize_to_itermediate_data()
        self.data = self.to_dict()

    def to_string(self):
        return "\n\n".join((datum.to_string() for datum in self._intermediate_data))

    def to_dict(self):
        data_dict = dict()
        for element in self._intermediate_data:
            if element.key == "edges":
                data_dict["edges"] = MappedEdges(element).edges
            else:
                data_dict.update(dict(element.to_dict()))
        return data_dict

    def serialize_to_itermediate_data(self):
        serialized_data = list()
        for element in self._parsed_data.elements():
            if element.yields_section():
                serialized_data.append(Section(element.to_section()))
            else:
                raise ValueError(
                    f"Top level element {element.string_key()} must be a section. Try reformatting it as: # {element.string_key()}"
                )
        return serialized_data

    def parse_data(self):
        return enolib.parse(self._loaded_data)

    def load_data(self):
        try:
            loaded_data = self.load_from_file_path(self._input_data)
        except (OSError, FileNotFoundError):
            try:
                loaded_data = self._input_data.read()
            except AttributeError:
                loaded_data = self._input_data
        return loaded_data

    @staticmethod
    def load_from_file_path(data):
        with open(data, "r") as data_file:
            return data_file.read()
