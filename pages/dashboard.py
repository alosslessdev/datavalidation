import streamlit as st
import pandas as pd

from validations.gx_validator import validate_dataset


def show_dashboard(df):

    st.header("Dashboard")

    total_rows = len(df)
    total_columns = len(df.columns)

    validation_results = validate_dataset(df)

    total_expectations = len(validation_results)

    successful = sum(r["success"] for r in validation_results)

    quality_score = round(
        (successful / total_expectations) * 100,
        2
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", total_rows)
    col2.metric("Columns", total_columns)
    col3.metric("Quality Score", f"{quality_score}%")

    st.subheader("Validation Results")

    results_df = pd.DataFrame(validation_results)

    st.dataframe(results_df)
