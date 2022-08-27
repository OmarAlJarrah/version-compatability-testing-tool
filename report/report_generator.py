import templates


def normalize_data(data):
    encoding = 'utf-8'
    return data if data is None else data.decode(encoding)


def generate_report(output, errors):
    output = normalize_data(output)
    errors = normalize_data(errors)
    report_data = templates.default_report_template.format(output, errors)
    return report_data
