class CharacterMappingNotation:
    def __init__(self, edge_data, characters):
        self.edge_data = edge_data
        self.characters = characters

    def get_edge_list(self):
        for act_name, act_data in self.edge_data.items():
            for scene_name, scene_data in act_data.items():
                for souce_character_name, target_character_data in scene_data.items():
                    for (
                        taget_character_name,
                        edge_data,
                    ) in target_character_data.items():
                        edge_data.update({"act": act_name, "scene": scene_name})
                        yield (souce_character_name, taget_character_name, edge_data)
