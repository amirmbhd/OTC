import streamlit as st
import pandas as pd
from PIL import Image

def load_images(image_name):
    img = Image.open(image_name)
    return st.image(img, width=700)

c_image = 'Baner.png'
load_images(c_image)

disease_states = {
    "GERD": {1:'Prilosec (omeprazole)', 2:'Nexium (esomeprazole)', 3:'Pepcid (famotidine)', 4:'Tums (calcium carbonate)', 5:'Milk of Magnesia (magnesium hydroxide)'},
    "Allergies": {1:'Allegra 12 Hour (Fexofenadine)', 2:'Allegra 24 Hour (Fexofenadine)', 
                  3:"Buckley's Jack and Jill Children's Formula (Diphenhydramine HCI / Phenylephrine HCI)",
                  4:"Children's Allegra (Fexofenadine)", 5:'Chlor-Trimeton (Chlorpheniramine Maleate)',
                  6:'Claritin (Loratadine)', 7:'Claritin Syrup (Loratadine)',
                  8:'Dristan Long Lasting Menthol Spray (Oxymetazoline)', 
                  9:'Dristan Long Lasting Nasal Mist (Oxymetazoline)',
                  10:'Otrivin (Xylometazoline Hydrochloride)', 11:'Reactine (Cetirizine) 5 mg', 12:'Zyrtec (Cetrizine)', 13:'Benadryl'},
    "Pain Control": {1:'Tylenol (acetaminophen)', 2:'Advil, Motrin (ibuprofen)', 
                  3:"Aleve (naproxen)",
                  4:"Aspirin", 5:'Lidoderm (topical lidocaine)',
                  6:'Icy Hot (menthol + methyl salicylate)', 7:'Topical capsaicin',
                  8:'"Excedrin, Goodys Powder (acetaminophen + aspirin + caffeine)"', 
                  9:'Orajel (benzocaine oral topical)',
                  10: 'Biofreeze (menthol) , 11:'Antacids(Tums)'},
    "Constipation": {1:'Psyllium', 2:'Polycarbophil', 3:'Methylcellulose', 4:'Bisacodyl', 5:'Senna', 6:'Polyethylene glycol',
                     7:'Docusate', 8:'Magnesium citrate', 9:'Mineral oil', 10:'Glycerin suppositories', 11:'Saline enemas'}
}

st.title("Patient Over The Counter Recommendation Program")

st.markdown(
    "Welcome to the OTC Recommendation Program! This program will tell you which OTC medications you are eligible for based on your answers to some survey questions.  **Select the disease state in the sidebar to get started.**"
)

st.sidebar.markdown("**Please select the disease state that you would like to get recommendation on?**")
options = [""] + list(disease_states.keys())
selection = st.sidebar.selectbox("Disease State:", options)

if selection == "Allergies":
    st.sidebar.markdown("""
    Allergic rhinitis usually arises from a trigger in the environment and resolves over time in the absence of the trigger.
    Common symptoms include watery eyes, sneezing, runny nose, headache, and rash. Over-the-counter medications can help with these symptoms, 
    but if they are persistent or become worse, medical attention is recommended.
    """)
if selection == "GERD":
    st.sidebar.markdown("""
    GERD, or gastroesophageal reflux disease, is when stomach acid flows back into the esophagus, causing symptoms like heartburn and difficulty swallowing. 
    Over-the-counter medications such as antacids or acid reducers can help provide relief. If symptoms persist or worsen, it is recommended to seek medical attention for a proper diagnosis and potentially stronger medications. 
    Consulting with a healthcare professional is important for personalized guidance and treatment options.        
    """)
if selection == "Pain Control":
    st.sidebar.markdown("""
    Pain management often involves the use of over-the-counter (OTC) medications to alleviate symptoms. OTC pain relievers such as acetaminophen (Tylenol) or nonsteroidal anti-inflammatory drugs (NSAIDs) like ibuprofen (Advil) or naproxen (Aleve) can be effective in reducing mild to moderate pain. 
    These medications can help with headaches, muscle aches, menstrual cramps, and minor injuries. However, it's important to carefully follow the instructions, recommended dosage, and duration of use provided on the packaging. 
    If pain persists or becomes severe, it is advisable to consult with a healthcare professional for a proper diagnosis and guidance on the most appropriate treatment options. Remember, OTC pain medications may not be suitable for everyone, so it's essential to seek medical advice to ensure safe and effective pain management.            
    """)
if selection == "Constipation":
    st.sidebar.markdown("""
    Constipation is a common condition that affects the digestive system - patients have difficulty passing stool or are unable to have regular bowel movements. 
    Luckily, there are several products that are available over the counter to treat this condition. Each type of medication can provide relief for patients, and there are many different formulation options as well. 
    It should be noted that these over-the-counter options are only meant to treat short-term constipation. Some cases of constipation may require prescription medication or further medical attention                        
    """)

if selection:
    sheet = pd.read_excel("OTCRecommendations.xlsx", sheet_name = selection)
    sheet.columns = sheet.columns.str.strip()
    eligible_medications = set(disease_states[selection].keys())
    age = None

    for i in range(len(sheet)):
        question = sheet.loc[i, "Question"]
        option1 = sheet.loc[i, "Option 1"]
        option2 = sheet.loc[i, "Option 2"]
        options = str(sheet.loc[i, "options"])  # Cast to string to avoid errors in case the value is not a string
        
        if question == "Please enter your age:":
            age = st.selectbox(question, list(range(1,101)))
            continue

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
    else:
        st.write("There are no OTC recommendations based on your responses.")
