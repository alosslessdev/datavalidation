import streamlit as st
import pandas as pd

from utils.charts import show_null_chart


def show_analysis(df):

    st.header("Dataset Analysis")

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
