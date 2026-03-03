"""
TT_Sprint05_Project package.
Started: 2026-03-02T22:52:51Z
"""

__version__ = "0.1.0"
import pandas as pd
import plotly.express as px
import streamlit as st

st.header(" Sprint 05 - Projeto")

car_data = pd.read_csv("vehicles_us.csv")

hist_button = st.button("Criar Histograma")
if hist_button:
    st.write("Criando um histograma")

    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox("Criar Gráfico de Dispersão")
if build_scatter:
    st.write("Criando um Gráfico de Dispersão")

    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
