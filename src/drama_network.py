from src.sdl_tools.sdl_api import load_sdl_string, load_sdl_file
from src.converters.edge_list_converter import convert_to_edge_list
from src.converters.networkx_converter import convert_to_networkx
from src.converters.string_converter import convert_to_string
from src.converters.sdl_file_converter import convert_to_file
from pprint import pformat


class DramaNetwork:
    def __init__(self, data):
        self.data = self._load_sdl_data(data)

    def to_edge_list(self, play_data=False, division_data=False):
        return list(
            convert_to_edge_list(self, play_data=play_data, division_data=division_data)
        )

    def to_networkx(self, play_data=False, division_data=False):
        return convert_to_networkx(
            self, play_data=play_data, division_data=division_data
        )

    def to_string(self):
        return convert_to_string(self)

    def to_file(self, path):
        return convert_to_file(self, path)

    def _load_sdl_data(self, data):
        try:
            return load_sdl_file(data)
        except (OSError, FileNotFoundError):
            return load_sdl_string(data)

    def __str__(self):
        return f"{self.__class__.__name__}({pformat(self.data)})"

    def __repr__(self):
        title = self.data.get("play", dict()).get("title", str())
        return f"{self.__class__.__name__}({title})"
