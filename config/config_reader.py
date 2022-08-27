import json
from config.cli_options_reader import get_config_file_path


def read_config_dict():
    config_file_path = get_config_file_path()
    with open(config_file_path, 'r') as config_file:
        json_config = json.load(config_file)

    return json_config
