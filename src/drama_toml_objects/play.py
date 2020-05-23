from src.drama_toml_objects.generic_play_object import GenericPlayObject


class Play(GenericPlayObject):
    def __init__(self, data=None):
        self.data = data
        super().__init__(self.data)
