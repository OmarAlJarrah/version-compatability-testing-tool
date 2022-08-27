import subprocess


def execute(command: str):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, errors = process.communicate()
    return output, errors
