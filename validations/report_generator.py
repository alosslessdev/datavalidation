import json


def generate_json_report(results):

    with open("reports/validation_report.json", "w") as file:
        json.dump(results, file, indent=4)

    return "reports/validation_report.json"
