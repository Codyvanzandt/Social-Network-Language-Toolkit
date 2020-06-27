def convert_to_file(social_network, file_path):
    with open(file_path, "w") as output_file:
        output_file.write(social_network._doc.to_string())
