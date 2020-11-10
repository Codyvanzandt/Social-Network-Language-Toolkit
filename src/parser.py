from lark import Lark
from src.grammar import grammar

Parser = Lark(grammar, start="document")
