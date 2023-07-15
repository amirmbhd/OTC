import streamlit as st
import pandas as pd
from PIL import Image

# ... rest of your code ...

eligible_medications = set(disease_states[selection].keys())
age = None
is_eligible = True  # add this line

for i in range(len(sheet)):
    # ... rest of your code inside the loop ...

    if question == "Age condition":
        # ... rest of your code in this condition ...
        if eval(option1):
            if options.lower() == "none":
                # st.write("Based on your responses you are not eligible for over the counter medications. Please consult a healthcare provider.")
                is_eligible = False  # change this line
                eligible_medications = set()
                break
            else:
                # ... rest of your code in this condition ...

    response = st.radio(question, options = [option1, option2], index=1)  # index=1 to set "Option 2" as default

    if response == option1:
        if options.lower() == "none":
            # st.write("Based on your responses you are not eligible for over the counter medications. Please consult a healthcare provider or contact your local pharmacy.")
            is_eligible = False  # change this line
            eligible_medications = set()
            break
        else:
            # ... rest of your code in this condition ...

# this block of code outside the loop:
if eligible_medications:
    st.write("Based on your responses, you are eligible for the following medications:")
    for num in eligible_medications:
        st.write(disease_states[selection][num])
elif not is_eligible:  # check if the user is not eligible
    st.write("Based on your responses you are not eligible for over the counter medications. Please consult a healthcare provider or contact your local pharmacy.")
