import streamlit as st
import pandas as pd
from PIL import Image

#OTC_df = pd.read_excel("otc.xlsx")


st.title("Patient Over The Counter Recommendation Program")

st.markdown(
    "Welcome to the OTC Recommendation Program! This program will tell you which OTC medications you are eligible for based on your answers to some survey questions.  **Select the disease state in the sidebar to get started.**"
)


def load_images(image_name):
    img = Image.open(image_name)
    return st.image(img, width=800)

c_image = 'diab.png'
load_images(c_image)
