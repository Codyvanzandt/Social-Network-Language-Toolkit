import abc
from multidict import MultiDict
from src.sdl_tools.sdl_document import SDLDocument
from src.utils.networkx_utils import get_edges_underneath_divisions


class AbstractSDLConverter(metaclass=abc.ABCMeta):
    def __init__(self, obj):
        self.obj = obj

    def to_sdl_doc(self):
        return SDLDocument(self.to_sdl_string())

    def to_sdl_string(self):
        play_string = self.single_section_to_string(self.get_play_dict())
        character_string = self.single_section_to_string(self.get_character_dict())
        edges_string = self.edges_data_to_string(self.get_edges_dict())
        return "\n\n".join((play_string, character_string, edges_string))

    @abc.abstractmethod
    def get_play_dict(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_character_dict(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_edges_dict(self):
        raise NotImplementedError()

    @staticmethod
    def single_section_to_string(obj):
        section_data = (
            f"# {section_key}\n"
            + "\n".join((f"{k} : {v}" for k, v in section_data.items()))
            for section_key, section_data in obj.items()
        )
        return "\n".join(section_data)

    def edges_data_to_string(self, obj, level=1):
        if isinstance(obj, list):
            edge_strings = (f"{s}.{t} : {d}" for s, t, d in obj)
            return "\n".join(edge_strings)
        elif isinstance(obj, (dict, MultiDict)):
            subsection_strings = (
                f"{'#'*level} {subsection_key}\n"
                + self.edges_data_to_string(subsection_data, level=level + 1)
                for subsection_key, subsection_data in obj.items()
            )
            return "\n".join(subsection_strings)
        else:
            raise ValueError(
                f"{self.obj} can only contain list, dict, or multidict structures, except inside the data-dict of individuald edges."
            )


class NetworkxToSDLConverter(AbstractSDLConverter):
    def get_play_dict(self):
        return {"play": self.obj.graph}

    def get_character_dict(self):
        return {"characters": self.obj.nodes()}

    def get_edges_dict(self):
        edges = get_edges_underneath_divisions(self.obj)
        return {"edges": edges}
