from src.sdl_tools.sdl_document import SDLDocument

a = SDLDocument("examples/fake_play")
b = SDLDocument(a.to_string())

print(b.to_string())
