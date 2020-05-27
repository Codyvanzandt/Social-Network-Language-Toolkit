from src.converters.string_converter import convert_to_string

def convert_to_file(social_network, file_path):
    with open(file_path, "w") as output_file:
        output_file.write( convert_to_string(social_network) )