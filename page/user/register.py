import datetime
import streamlit as st
from type.page import PageType
from utils.database.graph import Neo4Graph

def make_new_medical_history(full_name, patient_id, symptoms, date, time):
    cypher = [
        f"""
            CREATE (fmh:MedicalHistory {{
                symptoms: "{symptoms}",
                dieases: "",
                drugs: "",
                date: date("{date.isoformat()}")
            }})
        """,
        f"""
            MATCH(p:Patient {{full_name: "{full_name}", patient_id: "{patient_id}"}}),
            (fmh:MedicalHistory {{symptoms: "{symptoms}", date: date("{date.isoformat()}")}})
            CREATE (p)-[:HAS_MEDICAL_HISTORY]->(fmh)
        """
    ]
    
    graph = Neo4Graph()
    graph.execute_query(cypher)

def register_ui():
    full_name = st.text_input("Full Name")
    patient_id = st.text_input("Patient Id")
    symptoms = st.text_area("Symptomps")
    #TODO: give doctor suggestion
    
    pick_doctor = st.selectbox("Select Doctor",("hansen","h"))
    date = st.date_input("Date")
    time = st.time_input("Time")
    if st.button("Save"):
        make_new_medical_history(
            full_name=full_name.lower(),
            patient_id=patient_id,
            symptoms=symptoms,
            date=date,
            time=time
        )
        st.session_state.mode = PageType.NULL
        st.rerun()