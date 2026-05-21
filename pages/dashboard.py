import streamlit as st
import pandas as pd

from validations.gx_validator import validate_dataset

st.set_page_config(page_title="Dashboard", layout="wide")

st.header("Dashboard")

if "df" not in st.session_state:
    st.warning("No dataset loaded. Go to the main page and upload a CSV file.")
    st.stop()

df = st.session_state["df"]

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
