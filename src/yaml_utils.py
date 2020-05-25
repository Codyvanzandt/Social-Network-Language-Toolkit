import yaml

def parse_yaml(yaml_data):
    

def load_yaml(string_or_file):
    try:
        with open(string_or_file, "r") as yaml_file:
            return yaml.load(string_or_file)
    except (OSError, FileNotFoundError):
        return yaml.load(string_or_file)