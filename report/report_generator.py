from report.templates import default_report_template


def normalize_data(data):
    encoding = 'utf-8'
    return "None" if data is None else data.decode(encoding)


def generate_report(output, errors):
    output = normalize_data(output)
    errors = normalize_data(errors)
    report_data = default_report_template.format(output, errors)
    return report_data
