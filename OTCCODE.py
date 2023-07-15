import streamlit as st
import pandas as pd
from PIL import Image

def load_images(image_name):
    img = Image.open(image_name)
    return st.image(img, width=700)

c_image = 'Baner.png'
load_images(c_image)

disease_states = {
    "GERD": {1:'Omeprazole', 2:'Esomeprazole', 3:'Famotidine', 4:'Calcium Carbonate', 5:'Magnesium Hydroxide'},
    "Allergies": {1:'Allegra 12 Hour (Fexofenadine)', 2:'Allegra 24 Hour (Fexofenadine)', 
                  3:"Buckley's Jack and Jill Children's Formula (Diphenhydramine HCI / Phenylephrine HCI)",
                  4:"Children's Allegra (Fexofenadine)", 5:'Chlor-Trimeton (Chlorpheniramine Maleate)',
                  6:'Claritin (Loratadine)', 7:'Claritin Syrup (Loratadine)',
                  8:'Dristan Long Lasting Menthol Spray (Oxymetazoline)', 
                  9:'Dristan Long Lasting Nasal Mist (Oxymetazoline)',
                  10:'Otrivin (Xylometazoline Hydrochloride)', 11:'Reactine (Cetirizine) 5 mg', 12:'Zyrtec (Cetrizine)', 13:'Benadryl'},
    "Pain Control": {1:'drug A', 2:'drug B', 3:'drug C'},
    "Constipation": {1:'Psyllium', 2:'Polycarbophil', 3:'Methylcellulose', 4:'Bisacodyl', 5:'Senna', 6:'Polyethylene glycol',
                     7:'Docusate', 8:'Magnesium citrate', 9:'Mineral oil', 10:'Glycerin suppositories', 11:'Saline enemas'}
}

st.title("Patient Over The Counter Recommendation Program")

st.markdown(
    "Welcome to the OTC Recommendation Program! This program will tell you which OTC medications you are eligible for based on your answers to some survey questions.  **Select the disease state in the sidebar to get started.**"
)

st.sidebar.markdown("**Please select the disease state that you would like to get recommendation on?**")
selection = st.sidebar.selectbox("Disease State:", list(disease_states.keys()))

if selection == "Allergies":
    st.sidebar.text("Allergic rhinitis usually arises from a trigger in the environment and resolves over time in the absence of the trigger. Common symptoms include watery eyes, sneezing, runny nose, headache, and rash. Over-the-counter medications can help with these symptoms, but if they are persistent or become worse, medical attention is recommended.")

if selection:
    sheet = pd.read_excel("OTCRecommendations.xlsx", sheet_name = selection)
    
    # Strip leading or trailing spaces from column names
    sheet.columns = sheet.columns.str.strip()

    eligible_medications = set(disease_states[selection].keys())
    age = None

    for i in range(len(sheet)):
        question = sheet.loc[i, "Question"]
        option1 = sheet.loc[i, "Option 1"]
        option2 = sheet.loc[i, "Option 2"]
        options = str(sheet.loc[i, "options"])  # Cast to string to avoid errors in case the value is not a string
        
        if question == "Please enter your age:":
            age = st.number_input(question)
            continue

        if question == "Age condition":
            # Replace "Age" in option1 with the `age` variable
            option1 = option1.replace("Age", str(age))
            # Evaluate the condition in "Option 1" with the age
            if eval(option1):
                if options.lower() == "none":
                    st.write("Based on your responses you are not eligible for over the counter medications. Please consult a healthcare provider.")
                    eligible_medications = set()
                    break
                else:
                    option_numbers = list(map(int, options.split(',')))
                    eligible_medications.intersection_update(option_numbers)
            continue

        
  
        response = st.radio(question, options = [option1, option2], index=1)  # index=1 to set "Option 2" as default
        
        if response == option1:
            if options.lower() == "none":
                st.write("Based on your responses you are not eligible for over the counter medications. Please consult a healthcare provider.")
                eligible_medications = set()
                break
            else:
                option_numbers = list(map(int, options.split(',')))
                eligible_medications.intersection_update(option_numbers)
            
    if eligible_medications:
        st.write("Based on your responses, you are eligible for the following medications:")
        for num in eligible_medications:
            st.write(disease_states[selection][num])
