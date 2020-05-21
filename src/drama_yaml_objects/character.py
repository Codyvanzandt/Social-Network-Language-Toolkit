from src.drama_yaml_objects.generic_play_object import GenericPlayObject


class Character(GenericPlayObject):
    def __init__(self, name, data_dict):
        self.name = name
        self._data_dict = data_dict
        super().__init__(data_dict)

    def __eq__(self, other):
        if other is self:
            return True
        elif type(self) == type(other):
            return self._data_dict == other._data_dict and self.name == other.name
        return False
