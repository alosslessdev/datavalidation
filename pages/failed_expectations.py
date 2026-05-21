import streamlit as st
import pandas as pd

from validations.gx_validator import validate_dataset

st.set_page_config(page_title="Failed Expectations", layout="wide")

st.header("Failed Expectations")

if "df" not in st.session_state:
    st.warning("No dataset loaded. Go to the main page and upload a CSV file.")
    st.stop()

df = st.session_state["df"]

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
