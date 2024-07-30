import datetime
import streamlit as st
from type.page import PageType

def register_ui():
    full_name = st.text_input("Full Name")
    birthday = st.date_input("Birth date", datetime.date(2000,9,18))
    symptoms = st.text_area("Symptomps")
    #TODO: give doctor suggestion
    
    pick_doctor = st.selectbox("Select Doctor",("hansen","h"))
    date = st.date_input("Date")
    time = st.time_input("Time")
    if st.button("Save"):
        st.session_state.mode = PageType.NULL