from java.gradle.command_builder import build_command
from cli_utils.command_executor import execute
from handlers import report_handler


def handle(config_data: dict):
    path = config_data['project_path']
    for version in config_data['versions']:
        command = build_command(jdk_version=version, project_path=path)
        output, errors = execute(command)
        report_handler.handle(output=output, errors=errors, version=version)
