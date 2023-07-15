import streamlit as st
import pandas as pd
from PIL import Image

OTC_df = pd.read_excel("OTCRecommendations.xlsx")

GERD = ['Drug 1',	'Drug 2',	'Drug 3',	'Drug 4',	'Drug 5',	'Drug 6',	'Drug 7',	'Drug 8',	'Drug 9',	'Drug 10',	'Drug 11',	'Drug 12']
Allergies = ['Allegra 12 Hour (Fexofenadine)',	'Allegra 24 Hour (Fexofenadine)', 'Buckleys Jack Jill Childrens Formula (Diphenhydramine HCI / Phenylephrine HCI)',	'Childrens Allegra (Fexofenadine)',	'Chlor-Trimeton (Chlorpheniramine Maleate)',	'Claritin (Loratadine)View Product',	'Claritin Syrup (Loratadine)',	'Dristan Long Lasting Menthol Spray (Oxymetazoline)',	'Dristan Long Lasting Nasal Mist (Oxymetazoline)',	'Otrivin (Xylometazoline Hydrochloride)',	'Reactine (Cetirizine) 5 mg',	'Zyrtec (Cetrizine)']	
Pain_Control = ['Drug 1',	'Drug 2',	'Drug 3',	'Drug 4',	'Drug 5',	'Drug 6',	'Drug 7',	'Drug 8',	'Drug 9',	'Drug 10',	'Drug 11',	'Drug 12']
Constipation = ['Psyllium',	'Polycarbophil',	'Methylcellulose',	'Bisacodyl',	'Senna',	'Polyethylene glycol',	'Docusate',	'Magnesium citrate',	'Mineral oil',	'Glycerin suppositories',	'Saline enemas']

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

                                 
