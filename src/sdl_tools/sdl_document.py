import enolib
from multidict import MultiDict
from src.sdl_tools.field import Field
from src.sdl_tools.section import Section
from src.sdl_tools.edges import MappedEdges


class SDLDocument:
    def __init__(self, data):
        self._data = data if data is not None else str()
        self._loaded_data = self.load_data()
        self._parsed_data = self.parse_data()
        self._intermediate_data = self.serialize_to_itermediate_data()
        self.data = self.serialize_to_dict()

    def serialize_to_dict(self):
        data_dict = dict()
        for element in self._intermediate_data:
            if element.key == "edges":
                extra_edge_data = self._get_extra_edge_data()
                data_dict["edges"] = MappedEdges(element, **extra_edge_data).edges
            else:
                data_dict.update(dict(element.to_dict()))
        return data_dict

    def _get_extra_edge_data(self):
        play_title = self._get_play_title()
        if play_title:
            return {"play": play_title}
        else:
            return dict()

    def _get_play_title(self):
        play_data = next(
            (
                element.to_dict()
                for element in self._intermediate_data
                if element.key == "play"
            ),
            dict(),
        )
        return play_data.get("play", dict()).get("title", None)

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
            loaded_data = self.load_file_path_data(self._data)
        except (OSError, FileNotFoundError):
            try:
                loaded_data = self._data.read()
            except AttributeError:
                loaded_data = self._data
        return loaded_data

    @staticmethod
    def load_file_path_data(data):
        with open(data, "r") as data_file:
            return data_file.read()
