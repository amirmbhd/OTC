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
medications = {"GERD": [(1, 'Omeprazole'), (2, 'Esomeprazole'), (3, 'Famotidine'), (4, 'Calcium Carbonate'), (5, 'Magnesium Hydroxide')],
               "Allergies": [(1, 'Allegra 12 Hour (Fexofenadine)'), (2, 'Allegra 24 Hour (Fexofenadine)'), (3, "Buckley's Jack and Jill Children's Formula (Diphenhydramine HCI / Phenylephrine HCI)"), (4, "Children's Allegra (Fexofenadine)"), (5, 'Chlor-Trimeton (Chlorpheniramine Maleate)'), (6, 'Claritin (Loratadine)View Product'), (7, 'Claritin Syrup (Loratadine)'), (8, 'Dristan Long Lasting Menthol Spray (Oxymetazoline)'), (9, 'Dristan Long Lasting Nasal Mist (Oxymetazoline)'), (10, 'Otrivin (Xylometazoline Hydrochloride)'), (11, 'Reactine (Cetirizine) 5 mg'), (12, 'Zyrtec (Cetrizine)'), (13, 'Benadryl')],
               "Pain Control": [(1, 'drug A'), (2, 'drug B'), (3, 'drug C')],
               "Constipation": [(1, 'Psyllium'), (2, 'Polycarbophil'), (3, 'Methylcellulose'), (4, 'Bisacodyl'), (5, 'Senna'), (6, 'Polyethylene glycol'), (7, 'Docusate'), (8, 'Magnesium citrate'), (9, 'Mineral oil'), (10, 'Glycerin suppositories'), (11, 'Saline enemas')]}

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

    # Initially, assume the patient is eligible for all medications
    eligible_meds = [med[0] for med in medications[selection]]


    for index, row in OTC_df.iterrows():
        question = row['Question']
        option1 = row['Option 1']
        option2 = row['Option 2']
    
        user_response = st.radio(question, options=[option1, option2])
        
        if user_response == option1:
            options = str(row['options'])
    
            # If the options column says "NONE", the patient is not eligible for any medication
            if options == 'NONE':
                eligible_meds = []
                st.markdown("Based on your responses, you are not eligible for over the counter medications. Please consult a healthcare provider.")
                break
            else:
                # Check if options can be split, indicating multiple eligible medications
                if ',' in options:
                    options = list(map(int, options.split(',')))  # Split and convert string numbers to int
                    eligible_meds = list(set(eligible_meds) & set(options))  # Intersection of eligible_meds and options
                else:
                    # If options cannot be split, it is a single number
                    options = [int(options)]  # Convert the single number to int and put it in a list
                    eligible_meds = list(set(eligible_meds) & set(options))  # Intersection of eligible_meds and options
    





    # Display eligible medications
    if eligible_meds:
        st.markdown(f"Eligible medications for {selection}:")
        for med in medications[selection]:
            if med[0] in eligible_meds:  # Check if the medication is in the eligible list
                st.markdown(med[1])  # Only display the drug name
