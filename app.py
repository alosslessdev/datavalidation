import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Data Quality Dashboard",
    layout="wide"
)

st.title("Data Quality Dashboard")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.session_state["df"] = df
    st.success(f"Loaded dataset with {len(df)} rows and {len(df.columns)} columns.")
    st.info("Use the sidebar to navigate between pages.")

else:
    st.info("Upload a CSV file to begin.")
