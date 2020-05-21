class GenericPlayObject:
    def __init__(self, data_dict=None):
        self.data_dict = dict() if data_dict is None else data_dict
        for name, value in self.data_dict.items():
            if isinstance(value, dict):
                self.__dict__[name] = GenericPlayObject(value)
            else:
                self.__dict__[name] = value

    def __repr__(self):
        return f"{self.__class__.__name__}(data_dict={self.data_dict})"
