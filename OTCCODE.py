import streamlit as st
import pandas as pd
from PIL import Image

#OTC_df = pd.read_excel("otc.xlsx")



def load_images(image_name):
    img = Image.open(image_name)
    return st.image(img, width=700)

c_image = 'Baner.png'
load_images(c_image)



st.title("Patient Over The Counter Recommendation Program")

st.markdown(
    "Welcome to the OTC Recommendation Program! This program will tell you which OTC medications you are eligible for based on your answers to some survey questions.  **Select the disease state in the sidebar to get started.**"
)

st.sidebar.radio(
            "Do you want to check if you have completed the series for {vaccine_key}?",
            ["No", "Yes","GERD", "ALLERGIES"],
            index=0,
            )
