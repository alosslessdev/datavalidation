import streamlit as st
import pandas as pd

from validations.gx_validator import validate_dataset


def show_failed_expectations(df):

    st.header("Failed Expectations")

    results = validate_dataset(df)

    failed = [
        r for r in results
        if not r["success"]
    ]

    if failed:

        failed_df = pd.DataFrame(failed)

        st.dataframe(failed_df)

    else:
        st.success("No failed expectations found.")
