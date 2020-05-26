from src.sdl_tools import load_sdl_string, load_sdl_file


class SocialNetwork:
    def __init__(self, data):
        self.data = self._load_sdl_data(data)

    def _load_sdl_data(self, data):
        try:
            return load_sdl_file(data)
        except (OSError, FileNotFoundError):
            return load_sdl_string(data)

    def __repr__(self):
        title = self.data.get("play", dict()).get("title", str())
        return f"{self.__class__.__name__}({title})"
