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

def get_patient_hypotesis(patient_name, patient_id, patient_complaint):
    cypher_patient = [f""" 
            MATCH (p:Patient {{id: '{patient_id}'}})-[r]-(related)
            WHERE NOT type(r) = 'HAS_MEDICAL_HISTORY'
            RETURN p, r, related
              """]
    cypher_record = [f"""
            MATCH (p:Patient {{patient_id: "{patient_id}", full_name: "{patient_name}"}})-[r:HAS_MEDICAL_HISTORY]->(mh:MedicalHistory)
            RETURN p, r, mh
            ORDER BY r.date ASC
                     """]
    
    graph = Neo4Graph()
    AI71 = AI71Inference()
    record_patient = graph.read_transaction(queries=cypher_patient)
    st.session_state.patient_information = record_patient
    patient_medical = graph.read_transaction(queries=cypher_record)
    patient_medical = patient_medical[:-1]
    st.session_state.patient_medical_history = patient_medical
    
    messages = [{"role":"system","content":"You are an AI assistant designed to help doctor to diagnoze patient's diesease from the patient's information and past medical history. Always focus in the patient complaint"},
                {"role":"user", "content": f"""Using the patient information and patient complaint, Diagnosed patient's.
                                               Patient Information: {record_patient} {patient_medical}
                                               Patient Complaint: {patient_complaint}"""}]
    patient_diagnose = AI71.make_suggestion(history=messages)
    return patient_diagnose

def get_patient_medicines(patient_diseases):
    messages = [{"role": "system","content": "You are an AI assistant designed to help doctor to decide patient's medicines according to its information and current dieases"},
                {"role": "user","content": f"""Given a patient's dieases and patient's information. Give me a list of medicines and the rules for using the medicines.
                                               Patient Information: {st.session_state.patient_information}
                                               Patient Past Medical Record: {st.session_state.patient_medical_history}
                                               Patient Dieases: {patient_diseases}"""}]
    
    AI71 = AI71Inference()
    medicine_list = AI71.make_suggestion(history=messages)
    return medicine_list

def save_medical_history():
    cypher = [
        f"""
            CREATE(mh:MedicalHistory {{
                diseases: "{st.session_state.patient_diseases}",
                symptoms: "{st.session_state.patient_complaint}",
                medicine: "{st.session_state.patient_medicine_list}",
                patient_id: "{st.session_state.patient_id}"
            }})
        """,
        f"""
            MATCH (p: Patient {{patient_id: "{st.session_state.patient_id}"}}),
            (mh:MedicalHistory {{patient_id: "{st.session_state.patient_id}"}})
            CREATE (p)-[:HAS_MEDICAL_HISTORY]->(mh)
        """
    ]
    graph = Neo4Graph()
    graph.execute_query(queries=cypher)
    

def analyze_ui():
    if "patient_information" not in st.session_state:
        st.session_state.patient_information = ""
    if "patient_medical_history" not in st.session_state:
        st.session_state.patient_medical_history = ""
    if "patient_summary" not in st.session_state:
        st.session_state.patient_summary = "Patient Summary Loading..."
    if "patient_diagnose" not in st.session_state:
        st.session_state.patient_diagnose = "Analyze Dieases Loading..."
    if "patient_medicine_list" not in st.session_state:
        st.session_state.patient_medicine_list = "Medicine List Suggestion Loading..."
    if "patient_name" not in st.session_state:
        st.session_state.patient_name=""
    if "patient_id" not in st.session_state:
        st.session_state.patient_id=""
    if "patient_complaint" not in st.session_state:
        st.session_state.patient_complaint = ""
    if "patient_diseases" not in st.session_state:
        st.session_state.patient_diseases = ""
        
    patient_name = st.text_input("Patient Name")
    patient_id = st.text_input("Patient Id")
    if patient_name and patient_id and (st.session_state.patient_summary == "Patient Summary Loading..." or st.session_state.patient_name != patient_name or st.session_state.patient_id != patient_id):
        st.session_state.patient_name = patient_name
        st.session_state.patient_id = patient_id
        patient_summary = get_patient_summary(patient_name=patient_name, patient_id=patient_id)
        st.session_state.patient_summary = patient_summary
        st.markdown(f"Patient Information Summary")
        st.markdown(patient_summary)
    else:
        st.markdown(f"{st.session_state.patient_summary}")
    
    patient_complaint = st.text_input("Type the patient's complaint")
    if patient_complaint  and patient_id and (st.session_state.patient_diagnose == "Analyze Dieases Loading..." or st.session_state.patient_complaint != patient_complaint):
        st.session_state.patient_complaint = patient_complaint
        patient_diagnose = get_patient_hypotesis(patient_name=patient_name, patient_id=patient_id, patient_complaint=patient_complaint)
        st.session_state.patient_diagnose = patient_diagnose
        st.markdown(f"Patient Diagnose")
        st.markdown(f"{patient_diagnose}")
    else:
        st.markdown(st.session_state.patient_diagnose)
        
    patient_diseases = st.text_input("Type Final Diseases")
    if patient_diseases and (st.session_state.patient_medicine_list == "Medicine List Suggestion Loading..." or st.session_state.patient_diseases != patient_diseases) :
        st.session_state.patient_diseases = patient_diseases
        medicine_list = get_patient_medicines(patient_diseases=patient_diseases)
        st.session_state.patient_medicine_list = medicine_list
        st.markdown("Medicine Suggestion List")
        st.markdown(medicine_list)
    else:
        st.markdown(st.session_state.patient_medicine_list)
        
    if st.button("Save"):
        save_medical_history()