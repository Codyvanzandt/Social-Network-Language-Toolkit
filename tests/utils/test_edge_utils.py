import pytest
from pprint import pprint

EDGE_DATA = {
    "act1": {
        "scene1": [
            ("A", "B", {"type": 1}),
            ("B", "C", {"type": 1}),
            ("C", "D", {"type": 1}),
        ],
        "scene2": [("D", "E", {"type": 1})],
    }
}
