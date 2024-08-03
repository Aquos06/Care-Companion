import streamlit as st
from utils.inference.service import AI71Inference
from utils.database.graph import Neo4Graph
from utils.const import DOCTOR

def doctor_to_str():
    formatted_doctors = []
    for doctor in DOCTOR:
        doctor_str = (
            f"Doctor Name: {doctor['name']}, Specialization: {doctor['specialization']}, "
        )
        # Append the formatted string to the list
        formatted_doctors.append(doctor_str)

    # Join all formatted doctor strings with a newline separator
    string = "\n".join(formatted_doctors)
    return string


def chatbot_patient_ui():
    LLM = AI71Inference()
    graph = Neo4Graph()
    
    col1, col2 = st.columns(2)
    with col1:
        patient_id = st.text_input("Patient ID")
    with col2:
        patient_name = st.text_input("Patient Full Name")    
    
    if patient_id and patient_name:
        cypher = [f"""
        MATCH (p:Patient {{patient_id: "{patient_id}", full_name: "{patient_name}"}})-[r]->(related)
        RETURN p, r, related
            """]
        patients_information = graph.read_transaction(queries=cypher)

        if "message_history_patient" not in st.session_state:
            st.session_state.message_history_patient = [
                {"role": "system",
                 "content": f"""You are a AI Medical Assistant. Given the patient's information, You need to answer user's query using you own knowledge and you always need to consider patient's informations.
                                Patient Information: {patients_information}
                                Furthermore, below is a list of doctor and its information. Always use this information if user ask suggestion or ask question about doctor."""},
            ]
        
        for index,chat in enumerate(st.session_state.message_history_patient):
            if index > 2:
                with st.chat_message(chat['role']):
                    st.markdown(chat['content'])
                
        if query:=st.chat_input("Say Something"):
            st.session_state.message_history_patient.append({"role":"user", "content":str(query)})
            
            with st.chat_message("user"):
                st.markdown(query)
            with st.chat_message("assistant"):
                response = st.markdown(LLM.patient_inference(history=st.session_state.message_history_patient))
                
            st.session_state.message_history_patient.append({"role":"assistant", "content":response})