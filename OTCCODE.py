import streamlit as st
import pandas as pd
from PIL import Image

# ... rest of your code ...

eligible_medications = set(disease_states[selection].keys())
age = None
is_eligible = True  # add this line

for i in range(len(sheet)):
    question = sheet.loc[i, "Question"]
    option1 = sheet.loc[i, "Option 1"]
    option2 = sheet.loc[i, "Option 2"]
    options = str(sheet.loc[i, "options"])  # Cast to string to avoid errors in case the value is not a string

    if question == "Please enter your age:":
        age = st.selectbox(question, list(range(1,101)))
    elif question == "Age condition":
        option1 = option1.replace("Age", str(age))
        if eval(option1):
            if options.lower() == "none":
                is_eligible = False  # change this line
                eligible_medications = set()
                break
            else:
                option_numbers = list(map(int, options.split(',')))
                eligible_medications.intersection_update(option_numbers)
    else:
        response = st.radio(question, options = [option1, option2], index=1)  # index=1 to set "Option 2" as default
        if response == option1:
            if options.lower() == "none":
                is_eligible = False  # change this line
                eligible_medications = set()
                break
            else:
                option_numbers = list(map(int, options.split(',')))
                eligible_medications.intersection_update(option_numbers)

# this block of code outside the loop:
if eligible_medications:
    st.write("Based on your responses, you are eligible for the following medications:")
    for num in eligible_medications:
        st.write(disease_states[selection][num])
elif not is_eligible:  # check if the user is not eligible
    st.write("Based on your responses you are not eligible for over the counter medications. Please consult a healthcare provider or contact your local pharmacy.")
