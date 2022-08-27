from report.report_generator import generate_report
from report.report_writer import write_report


def handle(output, errors, version):
    report_data = generate_report(output, errors)
    write_report(report_data, version)
