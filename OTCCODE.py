import streamlit as st
import pandas as pd

OTC_df = pd.read_excel("vaccines3.xlsx")


st.title("Patient Over The Counter Recommendation Program")

st.markdown(
    "Welcome to the OTC Recommendation Program! This program will tell you which OTC medications you are eligible for based on your answers to some survey question.  **Select the disease state in the sidebar to get started.**"
)

