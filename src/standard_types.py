from typing import TypeVar, Hashable, Mapping, Any, Tuple, Iterable, Union

T = TypeVar("T")

Node = Hashable
Edge = Tuple[Node, Node, Mapping[Hashable, Any]]
EdgeList = Iterable[Edge]
EdgeSection = Union[EdgeList, Mapping[Hashable, "EdgeSection"]]
