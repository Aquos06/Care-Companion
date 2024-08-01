import streamlit as st
from utils.database.graph import Neo4Graph
from utils.inference.service import AI71Inference

def get_patient_summary(patient_name, patient_id):
    cypher=[f"""
            MATCH (p:Patient {{patient_id: "{patient_id}", full_name: "{patient_name}"}})-[r]->(related)
            RETURN p, r, related
            """]
    
    graph = Neo4Graph()
    AI71 = AI71Inference()
    
    record = graph.read_transaction(queries=cypher)
    messages = [{"role":"system","content":"You are an AI assistant designed to summarize patient information for the doctors. You need to highlight the important information for the doctors. Only Highlight infromation about medical"},
                {"role":"user","content":f"""Based on the Node Object below, summarize the patient's information for the doctor. Do not give any email, phone number, or addres information. ONLY HIGHLIGHT INFORMATION ABOUT MEDICAL
                                             Node object is {record}"""}]
    patient_summary = AI71.make_suggestion(history=messages)
    return patient_summary

def analyze_ui():
    if "patient_name" not in st.session_state:
        st.session_state.patient_name= ""
    if "patient_complaint" not in st.session_state:
        st.session_state.patient_complaint = ""
    if "patient_drugs" not in st.session_state:
        st.session_state.patient_drugs = ""
    if "patient_diseases" not in st.session_state:
        st.session_state.patient_diseases = ""
        
    patient_name = st.text_input("Patient Name")
    patient_id = st.text_input("Patient Id")
    if patient_name and patient_id:
        st.session_state.patient_name = patient_name
        patient_summary = get_patient_summary(patient_name=patient_name, patient_id=patient_id)
        st.markdown(patient_summary)
    else:
        st.markdown(f"Patient Summary Loading...")
    
    patient_complaint = st.text_input("Type the patient's complaint")
    if patient_complaint:
        st.markdown("Analyze Dieases Loading...")
        st.session_state.patient_complaint = patient_complaint
        
    patient_diseases = st.text_input("Type Final Diseases")
    if patient_diseases:
        st.session_state.patient_diseases = patient_diseases
    
    patient_drugs = st.text_input("Type Patient Drugs")
    if patient_drugs:
        st.session_state.patient_drugs = patient_drugs
        
    export_drugs_document = st.button("Export Report")