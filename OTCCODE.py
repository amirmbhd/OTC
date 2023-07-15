import streamlit as st
import pandas as pd
from PIL import Image

def load_images(image_name):
    img = Image.open(image_name)
    return st.image(img, width=700)

c_image = 'Baner.png'
load_images(c_image)

disease_states = {
    "GERD": ['Omeprazole', 'Esomeprazole', 'Famotidine', 'Calcium Carbonate', 'Magnesium Hydroxide'],
    "Allergies": ['Allegra 12 Hour (Fexofenadine)', 'Allegra 24 Hour (Fexofenadine)', 
                  'Buckleys Jack Jill Childrens Formula (Diphenhydramine HCI / Phenylephrine HCI)',
                  'Childrens Allegra (Fexofenadine)', 'Chlor-Trimeton (Chlorpheniramine Maleate)',
                  'Claritin (Loratadine)View Product', 'Claritin Syrup (Loratadine)',
                  'Dristan Long Lasting Menthol Spray (Oxymetazoline)', 'Dristan Long Lasting Nasal Mist (Oxymetazoline)',
                  'Otrivin (Xylometazoline Hydrochloride)', 'Reactine (Cetirizine) 5 mg', 'Zyrtec (Cetrizine)', 'Benadryl'],
    "Pain Control": ['drug A', 'drug B', 'drug C'],
    "Constipation": ['Psyllium', 'Polycarbophil', 'Methylcellulose', 'Bisacodyl', 'Senna', 'Polyethylene glycol',
                     'Docusate', 'Magnesium citrate', 'Mineral oil', 'Glycerin suppositories', 'Saline enemas']
}

st.title("Patient Over The Counter Recommendation Program")
st.markdown(
    "Welcome to the OTC Recommendation Program! This program will tell you which OTC medications you are eligible for based on your answers to some survey questions.  **Select the disease state in the sidebar to get started.**"
)

st.sidebar.markdown("**Please select the disease state that you would like to get recommendation on?**")
disease_options = ["", "GERD", "Allergies","Pain Control", "Constipation"]
selection = st.sidebar.selectbox("Disease State:",disease_options)

if selection:
    OTC_df = pd.read_excel("OTCRecommendations.xlsx", sheet_name=selection, header=0)

    # initial eligible medications list contains all medications
    eligible_meds = [i+1 for i in range(len(disease_states[selection]))]  

    for index, row in OTC_df.iterrows():
        question = row['Question']
        option1 = row['Option 1']
        option2 = row['Option 2']
        user_response = st.radio(question, options=[option1, option2])
        
        if user_response == option1:
            options = str(row['options'])
            if options == 'NONE':
                eligible_meds = []
                st.markdown("Based on your responses, you are not eligible for over the counter medications. Please consult a healthcare provider.")
                break
            else:
                if ',' in options:
                    options = list(map(int, options.split(',')))
                    eligible_meds = list(set(eligible_meds) & set(options))
                else:
                    options = [int(options)]
                    eligible_meds = list(set(eligible_meds) & set(options))
    
    # Displaying the eligible medications to the user
    if eligible_meds:
        meds_names = [disease_states[selection][i-1] for i in eligible_meds]
        st.markdown("**Based on your responses, you may find the following medications useful:**")
        for med in meds_names:
            st.markdown("- " + med)
    else:
        st.markdown("**Based on your responses, there are no recommended over the counter medications. Please consult a healthcare provider.**")
