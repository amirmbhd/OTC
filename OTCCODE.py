import streamlit as st
import pandas as pd
from PIL import Image

#OTC_df = pd.read_excel("otc.xlsx")



def load_images(image_name):
    img = Image.open(image_name)
    return st.image(img, width=700)

c_image = 'Baner.png'
load_images(c_image)

disease_options = ["", "GERD", "Allergies","Pain Control", "Constipation"]


st.title("Patient Over The Counter Recommendation Program")

st.markdown(
    "Welcome to the OTC Recommendation Program! This program will tell you which OTC medications you are eligible for based on your answers to some survey questions.  **Select the disease state in the sidebar to get started.**"
)

st.sidebar.markdown("**Please select the disease state that you would like to get recommendation on?**")
selection = st.sidebar.selectbox("Disease State:",disease_options)

                                 
