import enolib

def parse_sdl_file(data):
    try:
        return enolib.parse(data.read(), source=data.name)
    except AttributeError:
        with open(data, "r") as sdl_file:
            return enolib.parse(sdl_file.read(), source=sdl_file.name)


def parse_sdl_string(data):
    return enolib.parse(data)