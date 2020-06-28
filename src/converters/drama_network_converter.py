from src.converters.sdl_converter import NetworkxToSDLConverter
import src.drama_network
from networkx.classes.function import is_directed


class NXToDramaNetwork:
    def __init__(self, obj):
        self.obj = obj

    def to_drama_network(self):
        directed = is_directed(self.obj)
        sdl = NetworkxToSDLConverter(self.obj).to_sdl_doc()
        return src.drama_network.DramaNetwork(sdl.to_string(), directed=directed)
