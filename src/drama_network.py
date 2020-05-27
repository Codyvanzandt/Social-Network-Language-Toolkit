from src.sdl_tools import load_sdl_string, load_sdl_file
from src.converters.edge_list_converter import convert_to_edge_list
from src.converters.networkx_converter import convert_to_networkx
from pprint import pformat


class DramaNetwork:
    def __init__(self, data):
        self.data = self._load_sdl_data(data)

    def to_edge_list(self, play_data=False, division_data=False):
        return list(
            convert_to_edge_list(self, play_data=play_data, division_data=division_data)
        )

    def to_networkx(self):
        return convert_to_networkx(self)

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
