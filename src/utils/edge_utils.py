import itertools
import copy
from pprint import pprint


def combine_all_edges(edges, equal_func, combine_func):
    new_edges = list()
    for old_edge in edges:
        for i, new_edge in enumerate(new_edges):
            if equal_func(old_edge, new_edge):
                new_edges[i] = combine_func(old_edge, new_edge)
                break
        else:
            new_edges.append(copy.deepcopy(old_edge))
    return new_edges


def edges_equal(e1, e2):
    s1, t1, d1 = e1
    s2, t2, d2 = e2
    same_source = s1 == s2
    same_target = t1 == t2
    same_type = d1.get("type", None) == d2.get("type", None)
    same_divisions = d1.get("divisions", tuple()) == d2.get("divisions", tuple())
    return same_source and same_target and same_type and same_divisions


def combine_edges(e1, e2):
    s1, t1, d1 = e1
    _, _, d2 = e2
    weight_data = {"weight": d1.get("weight", 1) + d2.get("weight", 1)}
    combined_data = {k: v for d in (d1, d2, weight_data) for k, v in d.items()}
    return s1, t1, combined_data
