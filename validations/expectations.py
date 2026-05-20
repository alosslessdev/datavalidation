def get_expectations():

    expectations = [
        {
            "column": "Age",
            "type": "not_null"
        },
        {
            "column": "Fare",
            "type": "positive"
        },
        {
            "column": "Survived",
            "type": "binary"
        }
    ]

    return expectations
