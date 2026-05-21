import streamlit as st
import os

st.set_page_config(page_title="Reports", layout="wide")

st.header("Reports")

json_path = "reports/validation_report.json"

if os.path.exists(json_path):
    with open(json_path, "rb") as file:
        st.download_button(
            label="Download JSON Report",
            data=file,
            file_name="validation_report.json",
            mime="application/json"
        )
else:
    st.warning("No reports generated yet.")
