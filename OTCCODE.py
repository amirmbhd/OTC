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
                  8:'Excedrin, Goodys Powder (acetaminophen + aspirin + caffeine)', 
                  9:'Orajel (benzocaine oral topical)',
                  10: "Biofreeze (menthol)", 11: "Tums (antacids)", 12: "Pepto Bismol (Bismuth Subsalicylate)"},
    "Constipation": {1:'Metamucil (psyllium)', 2:'FiberCon, Fiber Lax (polycarbophil)', 3:'Citrucel (methylcellulose)', 4:'Dulcolax (bisacodyl)', 5:'Senokot (senna)', 6:'MiraLax (polyethylene glycol)',
                     7:'Colace (docusate)', 8:'Citroma (magnesium citrate)', 9:'Kondremul (mineral oil)', 10:'Glycerin suppositories', 11:'Saline enemas'}
}

# ... rest of your code ...

eligible_medications = set(disease_states[selection].keys())
age = None
is_eligible = True  # add this line

for i in range(len(sheet)):
    # ... rest of your code inside the loop ...

# this block of code outside the loop:
if eligible_medications:
    st.write("Based on your responses, you are eligible for the following medications:")
    for num in eligible_medications:
        st.write(disease_states[selection][num])
elif not is_eligible:  # check if the user is not eligible
    st.write("Based on your responses you are not eligible for over the counter medications. Please consult a healthcare provider or contact your local pharmacy.")
