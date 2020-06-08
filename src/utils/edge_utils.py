import networkx


def get_edges_by_division(drama_network, division, play_data=False):
    target_division = tuple(division.split("."))
    for source, target, edge_data in drama_network.to_edge_list(
        play_data=play_data, division_data=True
    ):
        edge_division = edge_data.get("divisions", tuple())
        if is_subarray(target_division, edge_division):
            yield (source, target, edge_data)


def is_subarray(a, b):
    """
    Given: sequences containing strings, a and b
    Return: boolean, a is a subarray of b
    """
    a_pointer, b_pointer = 0, 0
    len_a, len_b = len(a), len(b)
    while a_pointer < len_a and b_pointer < len_b:
        if a[a_pointer] == b[b_pointer]:
            a_pointer += 1
            b_pointer += 1
            if a_pointer == len_a:
                return True
        else:
            a_pointer = 0
            b_pointer += 1
    return False
