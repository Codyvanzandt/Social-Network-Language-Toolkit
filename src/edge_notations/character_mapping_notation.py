from itertools import chain


class CharacterMappingNotation2:
    def __init__(self, edge_data):
        self.edges = self.get_edges(edge_data)


class CharacterMappingNotation:
    def __init__(self, edge_data):
        self.edges = self.get_edges(edge_data)

    def get_edges(self, edge_data):
        if self.is_character_data(edge_data):
            return list(
                chain.from_iterable(
                    self.generate_edge_list(edge_data_item)
                    for edge_data_item in edge_data.items()
                )
            )
        else:
            return {
                outer_key: self.get_edges(inner_data)
                for outer_key, inner_data in edge_data.items()
            }

    def generate_edge_list(self, source_and_target_data):
        source_character, target_data = source_and_target_data
        for target_data in target_data:
            yield self.get_edge_data(source_character, target_data)

    def get_edge_data(self, source_character, target_edge_data):
        if isinstance(target_edge_data, str):
            return self.get_simple_edge_data(source_character, target_edge_data)
        elif isinstance(target_edge_data, dict):
            return self.get_complex_edge_data(source_character, target_edge_data)

    @staticmethod
    def get_simple_edge_data(source_character, target_edge_data):
        target_character_name = target_edge_data
        edge_data = dict()
        return (source_character, target_character_name, edge_data)

    @staticmethod
    def get_complex_edge_data(source_character, target_edge_data):
        target_data_items = iter(target_edge_data.items())
        (target_character_name, edge_weight), edge_data = (
            next(target_data_items),
            dict(target_data_items),
        )
        if edge_weight is not None:
            edge_data["weight"] = edge_weight
        return (source_character, target_character_name, edge_data)

    @staticmethod
    def is_character_data(data):
        for key, value in data.items():
            if not isinstance(key, str) or not isinstance(value, list):
                return False
        return True
