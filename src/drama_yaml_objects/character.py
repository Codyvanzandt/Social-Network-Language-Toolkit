from src.drama_yaml_objects.generic_play_object import GenericPlayObject


class Character(GenericPlayObject):
    def __init__(self, name, data=None):
        self.name = name
        self.data = dict() if data is None else data
        super().__init__(self.data)

    def __eq__(self, other):
        are_plays_equal = getattr(self, "play", str()) == getattr(other, "play", str())
        are_names_equal = getattr(self, "name", str()) == getattr(other, "name", str())
        return are_plays_equal and are_names_equal

    def __hash__(self):
        play = getattr(self, "play", str())
        name = getattr(self, "name", str())
        return hash((play, name))

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.name)}, {self.data})"

    def __str__(self):
        return self.name
