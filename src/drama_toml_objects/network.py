from src.drama_toml_objects.generic_play_object import GenericPlayObject


class Network(GenericPlayObject):
    def __init__(self, data=None):
        self.weighted = False
        self.directed = False
        super().__init__(data)
