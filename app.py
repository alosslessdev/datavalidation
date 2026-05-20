import streamlit as st
import pandas as pd

from pages.dashboard import show_dashboard
from pages.dataset_analysis import show_analysis
from pages.failed_expectations import show_failed_expectations
from pages.reports_page import show_reports

st.set_page_config(
    page_title="Data Quality Dashboard",
    layout="wide"
)

st.title("Data Quality Dashboard")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV",
    type=["csv"]
)

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Dataset Analysis",
        "Failed Expectations",
        "Reports"
    ]
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.session_state["df"] = df

    if menu == "Dashboard":
        show_dashboard(df)

    elif menu == "Dataset Analysis":
        show_analysis(df)

    elif menu == "Failed Expectations":
        show_failed_expectations(df)

    elif menu == "Reports":
        show_reports()

else:
    st.info("Upload a CSV file to continue.")