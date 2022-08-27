from datetime import datetime
from templates import default_report_file_name_template


def generate_report_file_name(version: str):
    return default_report_file_name_template\
        .format(version, str(datetime.now()).replace(" ", "_"))


def write_report(report_data: str, version: str):
    report_file_name = generate_report_file_name(version)

    with open(report_file_name, 'w') as report_file:
        report_file.write(report_data)
