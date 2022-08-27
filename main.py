import api.run
from config import config_reader


def main():
    configuration = config_reader.read_config_dict()
    api.run.run(config_dict=configuration)
