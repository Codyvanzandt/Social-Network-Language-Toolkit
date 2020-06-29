from functools import partial
import yaml
import pytest


class Field:
    def __init__(self, enolib_field, yaml_loader="default"):
        self._yaml_loader = self.get_yaml_loader(yaml_loader)
        self._enolib_field = enolib_field
        self.key = self.get_key()
        self.data = self.get_data()

    def __eq__(self, other):
        try:
            return (self.key == other.key) and (self.data == other.data)
        except AttributeError:
            return False

    def __repr__(self):
        return f"<{self.__class__.__name__}({repr(self.key)}: {repr(self.data)})>"

    def to_dict(self):
        return {self.key: self.data}

    def to_string(self, **kwargs):
        return f"{self.key} : {self.data}"

    @staticmethod
    def get_yaml_loader(yaml_loader_str):
        return {"default": partial(yaml.load, Loader=yaml.FullLoader)}[yaml_loader_str]

    def get_key(self):
        return self._enolib_field.string_key()

    def get_data(self):
        return self._enolib_field.required_value(self._yaml_loader)
