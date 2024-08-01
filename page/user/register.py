import streamlit as st

from type.page import PageType
from utils.database.graph import Neo4Graph
from utils.inference.service import AI71Inference
from utils.const import DOCTOR

def make_suggestion(symptoms):
    AI71 = AI71Inference()
    prompt = [{
                "role":"system",
                "content": f"""You are an AI assistant designed to choose which doctor suits the best according to the patient's systomps."""},
              {
                "role": "user",
                "content": f"""
                    Please choose the suitable doctor according to the symptomps, and give the reason.
                    Doctor List: {DOCTOR}
                    Symtomps: {symptoms}
                """
              }]
    suggestion = AI71.make_suggestion(history=prompt)
    return suggestion

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
    if "suggestion" not in st.session_state:
        st.session_state.suggestion = ""
    
    full_name = st.text_input("Full Name")
    patient_id = st.text_input("Patient Id")
    symptoms = st.text_area("Symptomps")
    
    if symptoms and st.session_state.suggestion == "":
        suggestion = make_suggestion(symptoms=symptoms)
        st.session_state.suggestion = suggestion
        st.markdown(suggestion)
    elif st.session_state.suggestion != "":
        st.markdown(st.session_state.suggestion)
    else:
        st.markdown("Loading suggestion...")
    #TODO: give doctor suggestion
    
    doctor_list = (doc["name"] for doc in DOCTOR)
    pick_doctor = st.selectbox("Select Doctor",doctor_list)
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