import src.converters.drama_network_converter
import src.converters.networkx_converter
import src.converters.sdl_converter
import src.drama_network

# Converting to DramaNetwork


def networkx_to_drama_network(graph):
    return src.converters.drama_network_converter.NXToDramaNetwork(
        graph
    ).to_drama_network()


def sdl_doc_to_drama_network(sdl_doc):
    return src.drama_network.DramaNetwork(sdl_doc.to_string())


# Converting to Networkx


def sdl_doc_to_networkx(sdl_doc, directed=False, embed_play=True):
    return src.converters.networkx_converter.SDLToNXConverter(sdl_doc).to_networkx(
        directed=directed, embed_play=embed_play
    )


def drama_network_to_networkx(drama_network, directed=False, embed_play=True):
    return src.converters.networkx_converter.DramaNetworkToNXConverter(
        drama_network
    ).to_networkx(directed=directed, embed_play=embed_play)


# Converting to SDL Document


def drama_network_to_sdl_doc(drama_network):
    return drama_network._doc


def networkx_to_sdl_doc(graph):
    return src.converters.sdl_converter.NetworkxToSDLConverter(graph).to_sdl_doc()
