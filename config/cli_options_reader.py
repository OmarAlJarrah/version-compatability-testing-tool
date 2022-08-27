import sys
import getopt
from config.cli_available_options import options, long_options, default_config_file_path


def get_long_option(argument):
    for index in range(len(options)):
        is_valid_option = argument == options[index] \
                              or argument == long_options[index]

        if is_valid_option:
            return long_options[index][2::]


def get_config_file_path():
    argument_list = sys.argv[1:]
    path = default_config_file_path

    try:
        arguments, values = getopt.getopt(argument_list, options, long_options)
        for current_argument, current_value in arguments:
            argument = get_long_option(current_argument)
            if argument is None:
                continue
            path = argument

    except getopt.error as err:
        print(str(err))

    return path


# Options are:
# lang, dependency_manager, project_path
# Note: versions should be read from a json file
