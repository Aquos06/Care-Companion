import streamlit as st

if "patient_name" not in st.session_state:
    st.session_state.patient_name= ""
if "patient_complaint" not in st.session_state:
    st.session_state.patient_complaint = ""
if "patient_drugs" not in st.session_state:
    st.session_state.patient_drugs = ""



def analyze_ui():
    patient_name = st.text_input("Patient Name")
    if patient_name:
        st.session_state.patient_name = patient_name
        st.markdown("**Patients Summary**")
        st.text(f"patient name is {patient_name}")
    
    patient_complaint = st.text_input("Type the patient's complaint")
    if patient_complaint:
        st.session_state.patient_complaint = patient_complaint
        
    patient_drugs = st.text_input("Type Patient Drugs")
    if patient_drugs:
        st.session_state.patient_drugs = patient_drugs
    
    export_drugs_document = st.button("Export Report")