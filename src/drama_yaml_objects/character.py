from src.drama_yaml_objects.generic_play_object import GenericPlayObject


class Character(GenericPlayObject):
    def __init__(self, name, play=str(), data=None):
        self.name = name
        self.play = play
        self.data = dict() if data is None else data
        super().__init__(self.data)

    def __eq__(self, other):
        try:
            return (self.play, self.name) == (other.play, other.name)
        except AttributeError:
            return False

    def __hash__(self):
        return hash((self.play, self.name))

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.name)}, {self.data})"

    def __str__(self):
        return self.name
