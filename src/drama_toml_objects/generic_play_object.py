class GenericPlayObject:
    def __init__(self, data=None):
        self.data = dict() if data is None else data
        for name, value in self.data.items():
            if isinstance(value, dict):
                self.__dict__[name] = GenericPlayObject(value)
            else:
                self.__dict__[name] = value

    def __repr__(self):
        return f"{self.__class__.__name__}(data={self.data})"


# TODO: raise helpful exception when user passes a key in data_dict that cannot be used as an attribute name
