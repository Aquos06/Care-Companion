import streamlit as st
import numpy as np
import pandas as pd

@st.dialog("New Drugs")
def import_new_drugs():
    drug_name = st.text_input("Drugs name")
    drug_schedule = st.text_input("Drugs Schedule")
    drug_exception = st.text_input("Drugs Exception (you cannot consume this drugs if you have ... alergies)")
    drug_composition = st.text_input("Drugs Composition")
    
    if st.button("Submit"):
        #TODO crud DB and KG
        st.rerun()

def drugs_list_ui():
    #TODO: change df to get from the DB
    st.subheader("Drug Table")
    
    col1,col2 = st.columns([3,1],vertical_alignment="bottom", gap="large")
    
    with col1:
        search = st.text_input("Search")
        #TODO search bar
    
    with col2:
        import_drug = st.button("Import new drugs")
        if import_drug:
            import_new_drugs()
    
    df = pd.DataFrame(np.random.randn(50,5), columns=("col %d" % i for i in range(5)))
    st.dataframe(df,width=1000, height=500)