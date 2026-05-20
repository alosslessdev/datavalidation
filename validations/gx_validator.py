import pandas as pd

from validations.expectations import get_expectations


def validate_dataset(df):

    expectations = get_expectations()

    results = []

    for exp in expectations:

        column = exp["column"]
        exp_type = exp["type"]

        if exp_type == "not_null":

            failed = int(df[column].isnull().sum())

            results.append({
                "column": column,
                "expectation": "Not Null",
                "failed": failed,
                "success": failed == 0
            })

        elif exp_type == "positive":

            failed = int((df[column] < 0).sum())

            results.append({
                "column": column,
                "expectation": "Positive Values",
                "failed": failed,
                "success": failed == 0
            })

        elif exp_type == "binary":

            failed = int((~df[column].isin([0, 1])).sum())

            results.append({
                "column": column,
                "expectation": "Binary Values",
                "failed": failed,
                "success": failed == 0
            })

    return results
