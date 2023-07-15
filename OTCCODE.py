import streamlit as st
import pandas as pd
from PIL import Image

def load_images(image_name):
    img = Image.open(image_name)
    return st.image(img, width=700)

c_image = 'Baner.png'
load_images(c_image)

disease_states = { ... }  # Disease states dictionary

st.title("OTCRec: An Efficient Approach to Community Pharmacy Counseling")

st.markdown( ... )  # Your initial markdown text

st.sidebar.markdown("**Please select the disease state that you would like to get recommendation on?**")
options = [""] + list(disease_states.keys())
selection = st.sidebar.selectbox("Disease State:", options)

# Your sidebar descriptions for different disease states...

if selection:
    sheet = pd.read_excel("OTCRecommendations.xlsx", sheet_name = selection)
    sheet.columns = sheet.columns.str.strip()
    eligible_medications = set(disease_states[selection].keys())
    age = None
    ineligible = False  # Initialize the flag to False

    for i in range(len(sheet)):
        question = sheet.loc[i, "Question"]
        option1 = sheet.loc[i, "Option 1"]
        option2 = sheet.loc[i, "Option 2"]
        options = str(sheet.loc[i, "options"])
        
        if question == "Please enter your age:":
            age = st.selectbox(question, list(range(1,101)))
            continue

        if question == "Age condition":
            option1 = option1.replace("Age", str(age))
            if eval(option1):
                if options.lower() == "none":
                    ineligible = True
                    eligible_medications = set()
                    break
                else:
                    option_numbers = list(map(int, options.split(',')))
                    eligible_medications.intersection_update(option_numbers)
            continue

        response = st.radio(question, options = [option1, option2], index=1)
        
        if response == option1:
            if options.lower() == "none":
                ineligible = True
                eligible_medications = set()
                break
            else:
                option_numbers = list(map(int, options.split(',')))
                eligible_medications.intersection_update(option_numbers)

    if eligible_medications:
        st.write("Based on your responses, you are eligible for the following medications:")
        for num in eligible_medications:
            st.write(disease_states[selection][num])
    elif ineligible:  # Check the flag
        st.write("Based on your responses you are not eligible for over the counter medications. Please consult a healthcare provider or contact your local pharmacy.")
