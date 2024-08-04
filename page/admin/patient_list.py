import streamlit as st
import pandas as pd
from utils.database.graph import Neo4Graph


def patient_list_ui():
    graph = Neo4Graph()
    query = ["""
    MATCH (p:Patient)
    RETURN p.patient_id AS patient_id, p.full_name AS full_name
    """]
    record = graph.read_transaction(queries=query)
    print(record)
    df = pd.DataFrame(record[0])
    
    st.title("Patient Information")
    st.data_editor(df)