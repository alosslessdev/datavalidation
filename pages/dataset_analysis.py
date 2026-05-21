import streamlit as st
import pandas as pd

from utils.charts import show_null_chart

st.set_page_config(page_title="Dataset Analysis", layout="wide")

st.header("Dataset Analysis")

if "df" not in st.session_state:
    st.warning("No dataset loaded. Go to the main page and upload a CSV file.")
    st.stop()

df = st.session_state["df"]

st.subheader("Dataset Preview")

st.dataframe(df.head())

st.subheader("Missing Values")

nulls = df.isnull().sum()

null_df = pd.DataFrame({
    "Column": nulls.index,
    "Nulls": nulls.values
})

st.dataframe(null_df)

show_null_chart(null_df)
