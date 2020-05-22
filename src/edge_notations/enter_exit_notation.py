import re
from collections import defaultdict
from itertools import combinations, permutations, product, chain

class EnterExitNotation:
    def __init__(self, edge_data, directed ):
        self.directed = directed
        self.on_stage = set()
        self.edges = self.get_edges(edge_data)

    def get_edges(self, edge_data):
        all_edges = list()
        for edge_group in edge_data:
            entering, exiting = self.create_enter_exit_sets(edge_group)
            self.handle_entrances_and_exits(entering, exiting)
            all_edges.append( self.get_new_edges(entering) )
        return list( chain.from_iterable(all_edges) )

    def get_new_edges(self, entering):
        if self.directed:
            on_stage_with_entering = chain( product(self.on_stage, entering), product(entering, self.on_stage) )
            entering_with_entering = permutations(entering, 2)
        else:
            on_stage_with_entering = product(self.on_stage, entering)
            entering_with_entering = combinations(entering, 2)
        return chain( on_stage_with_entering, entering_with_entering )

    def handle_entrances_and_exits(self, entering_characters, exiting_characters):
        for exiting_character in exiting_characters:
            self.on_stage.discard(exiting_character)
        for entering_character in entering_characters:
            self.on_stage.add(entering_character)

    @staticmethod
    def create_enter_exit_sets(character_group):
        pattern = re.compile(r"(\+|-)(\w+)")
        enter_exit = defaultdict(set)
        for character in character_group:
            direction, character = pattern.match(character).groups()
            enter_exit[direction].add(character)
        return enter_exit["+"], enter_exit["-"]
