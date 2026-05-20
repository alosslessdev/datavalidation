import streamlit as st
import plotly.express as px


def show_null_chart(df):

    fig = px.bar(
        df,
        x="Column",
        y="Nulls",
        title="Missing Values by Column"
    )

    st.plotly_chart(fig, use_container_width=True)
