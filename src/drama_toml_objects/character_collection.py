class CharacterCollection:
    def __init__(self, character_iterable=tuple()):
        self.character_mapping = {
            character.name: character for character in character_iterable
        }
        for character_name, character_obj in self.character_mapping.items():
            setattr(self, character_name, character_obj)

    def __getitem__(self, character_name):
        return self.character_mapping[character_name]

    def __setitem__(self, character_name, character_obj):
        self.character_mapping[character_name] = character_obj
        setattr(self, character_name, character_obj)

    def __delitem__(self, character_name):
        self.character_mapping.pop(character_name, None)
        if hasattr(self, character_name):
            delattr(self, character_name)

    def __iter__(self):
        yield from self.character_mapping.values()

    def __len__(self):
        return len(self.character_mapping)

    def __contains__(self, character_name):
        return self.character_mapping[character_name]

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) is type(other):
            return dict.__eq__(self.character_mapping, other.character_mapping)
        return False

    def __repr__(self):
        characters = ", ".join(repr(char) for char in self.values())
        return f"{self.__class__.__name__}( ({characters}) )"

    def keys(self):
        return self.character_mapping.keys()

    def values(self):
        return self.character_mapping.values()

    def items(self):
        return self.character_mapping.items()

    def get(self, character_name, default):
        return self.character_mapping.get(character_name, default)
