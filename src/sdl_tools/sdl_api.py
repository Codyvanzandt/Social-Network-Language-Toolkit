from src.sdl_tools.sdl_parser import parse_sdl_file, parse_sdl_string
from src.sdl_tools.sdl_serializer import serialize_sdl


def load_sdl_string(data):
    sdl_document = parse_sdl_string(data)
    return serialize_sdl(sdl_document)


def load_sdl_file(data):
    sdl_document = parse_sdl_file(data)
    return serialize_sdl(sdl_document)
