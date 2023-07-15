import streamlit as st
import pandas as pd
from PIL import Image

def load_images(image_name):
    img = Image.open(image_name)
    return st.image(img, width=700)

c_image = 'Baner.png'
load_images(c_image)

disease_options = ["", "GERD", "Allergies","Pain Control", "Constipation"]

# Predefine a dictionary with all medications per disease state
medications = {"GERD": ['Drug 1', 'Drug 2', 'Drug 3', 'Drug 4', 'Drug 5', 'Drug 6', 'Drug 7', 'Drug 8', 'Drug 9', 'Drug 10', 'Drug 11', 'Drug 12'],
               "Allergies": ['Allegra 12 Hour (Fexofenadine)', 'Allegra 24 Hour (Fexofenadine)', 'Buckleys Jack Jill Childrens Formula (Diphenhydramine HCI / Phenylephrine HCI)', 'Childrens Allegra (Fexofenadine)', 'Chlor-Trimeton (Chlorpheniramine Maleate)', 'Claritin (Loratadine)View Product', 'Claritin Syrup (Loratadine)', 'Dristan Long Lasting Menthol Spray (Oxymetazoline)', 'Dristan Long Lasting Nasal Mist (Oxymetazoline)', 'Otrivin (Xylometazoline Hydrochloride)', 'Reactine (Cetirizine) 5 mg', 'Zyrtec (Cetrizine)'],
               "Pain Control": ['Drug 1', 'Drug 2', 'Drug 3', 'Drug 4', 'Drug 5', 'Drug 6', 'Drug 7', 'Drug 8', 'Drug 9', 'Drug 10', 'Drug 11', 'Drug 12'],
               "Constipation": ['Psyllium', 'Polycarbophil', 'Methylcellulose', 'Bisacodyl', 'Senna', 'Polyethylene glycol', 'Docusate', 'Magnesium citrate', 'Mineral oil', 'Glycerin suppositories', 'Saline enemas']}

st.title("Patient Over The Counter Recommendation Program")

st.markdown(
    "Welcome to the OTC Recommendation Program! This program will tell you which OTC medications you are eligible for based on your answers to some survey questions.  **Select the disease state in the sidebar to get started.**"
)

st.sidebar.markdown("**Please select the disease state that you would like to get recommendation on?**")
selection = st.sidebar.selectbox("Disease State:", disease_options)

if selection == "Allergies":
    st.sidebar.markdown("""
    Allergic rhinitis usually arises from a trigger in the environment and resolves over time in the absence of the trigger.
    Common symptoms include watery eyes, sneezing, runny nose, headache, and rash. Over-the-counter medications can help with these symptoms, 
    but if they are persistent or become worse, medical attention is recommended.
    """)

if selection:
    OTC_df = pd.read_excel("OTCRecommendations.xlsx", sheet_name = selection)

    # Strip leading and trailing whitespaces from column names
    OTC_df.columns = OTC_df.columns.str.strip()

    flag = 0
    for index, row in OTC_df.iterrows():
        question = row['Question']
        option1 = row['Option 1']
        option2 = row['Option 2']
        
        user_response = st.radio(question, options=[option1, option2])
        if user_response == option2:
            flag += 1

    if flag == len(OTC_df):
        st.markdown(f"All medications suitable for {selection}:")
        for med in medications[selection]:
            st.markdown(med)
