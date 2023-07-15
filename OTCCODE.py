import pandas as pd
import streamlit as st

# Define your dictionary
disease_state_dict = {
    'GERD': ['Omeprazole', 'Esomeprazole', 'Famotidine', 'Calcium Carbonate', 'Magnesium Hydroxide'],
    'Allergies': ['Allegra 12 Hour (Fexofenadine)', 'Allegra 24 Hour (Fexofenadine)', "Buckley's Jack and Jill Children's Formula (Diphenhydramine HCI / Phenylephrine HCI)", "Children's Allegra (Fexofenadine)", 'Chlor-Trimeton (Chlorpheniramine Maleate)', 'Claritin (Loratadine)View Product', 'Claritin Syrup (Loratadine)', 'Dristan Long Lasting Menthol Spray (Oxymetazoline)', 'Dristan Long Lasting Nasal Mist (Oxymetazoline)', 'Otrivin (Xylometazoline Hydrochloride)', 'Reactine (Cetirizine) 5 mg', 'Zyrtec (Cetrizine)', 'Benadryl'],
    'Pain Control': ['drug A', 'drug B', 'drug C'],
    'Constipation': ['Psyllium', 'Polycarbophil', 'Methylcellulose', 'Bisacodyl', 'Senna', 'Polyethylene glycol', 'Docusate', 'Magnesium citrate', 'Mineral oil', 'Glycerin suppositories', 'Saline enemas']
}

# Display the selection box
disease_state = st.sidebar.selectbox("Disease State", [" ", "GERD", "Allergies", "Pain Control", "Constipation"])
age = st.sidebar.selectbox("Age", list(range(1,101)))

if disease_state == "Allergies":
    st.sidebar.write("Allergic rhinitis usually arises from a trigger in the environment and resolves over time in the absence of the trigger. Common symptoms include watery eyes, sneezing, runny nose, headache, and rash. Over-the-counter medications can help with these symptoms, but if they are persistent or become worse, medical attention is recommended.")

if disease_state != " ":

    df = pd.read_excel(disease_state + ".xlsx") # assuming filename is same as disease_state
    df.columns = df.columns.str.strip() # stripping any leading or trailing spaces from column names

    eligible_medications = set(range(1, len(disease_state_dict[disease_state])+1)) # initially all meds are eligible

    for index, row in df.iterrows():
        question = row['Question']
        option1 = row['Option 1']
        option2 = row['Option 2']
        options = row['Options']

        if question == "Please enter your age:":
            continue # Skip age entry question

        if question == "Age condition":
            option1 = option1.replace("Age", str(age))
            if eval(option1):
                if options.lower() == "none":
                    st.write("Based on your responses you are not eligible for over the counter medications. Please consult a healthcare provider.")
                    eligible_medications = set()
                    break
                else:
                    option_numbers = list(map(int, options.split(',')))
                    eligible_medications.intersection_update(option_numbers)
            continue # Skip to next question

        selected_option = st.radio(question, [option1, option2], index=1)

        if selected_option == option1:
            if options.lower() == "none":
                st.write("Based on your responses you are not eligible for over the counter medications. Please consult a healthcare provider.")
                eligible_medications = set()
                break
            else:
                option_numbers = list(map(int, options.split(',')))
                eligible_medications.intersection_update(option_numbers)

    if eligible_medications:
        meds = [disease_state_dict[disease_state][i-1] for i in eligible_medications]
        st.write(f"Based on your responses, you are eligible for the following medications: {', '.join(meds)}")
