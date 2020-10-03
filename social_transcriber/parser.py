from lark import Lark
from social_transcriber.grammar import grammar

parser = Lark(grammar, start="document")
