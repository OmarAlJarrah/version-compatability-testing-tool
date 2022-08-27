from api.run import run_testing
from config import config_reader


def main():
    configuration = config_reader.read_config_dict()
    run_testing(config_dict=configuration)


if __name__ == "__main__":
    main()
