import toml


class SocialNetwork:
    def __init__(self, data):
        self.data = self._load_toml_data(data)

    def get_edge_list(self):
        return CharacterMappingNotation(
            self["edges"], self["characters"]
        ).get_edge_list()

    def get(self, key, default=None):
        try:
            return self.data[key]
        except KeyError:
            return default

    def _load_toml_data(self, data):
        try:
            return toml.load(data)
        except (OSError, FileNotFoundError):
            return toml.loads(data)

    def __getitem__(self, key):
        try:
            return self.data[key]
        except KeyError:
            valid_keys = ", ".join(self.data.keys())
            raise KeyError(
                f"{self.__class__.__name__} has no key `{key}`. Valid keys: {valid_keys}"
            )

    def __repr__(self):
        title = self.get("play", dict()).get("title", str())
        return f"{self.__class__.__name__}({title})"
