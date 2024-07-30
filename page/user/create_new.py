import datetime
import streamlit as st
from type.page import PageType

def create_new_member_ui():
    full_name = st.text_input("Full Name")
    birtday = st.date_input("Birth Date", datetime.date(2000,9,18))
    gender = st.selectbox("Gender",('Men','Women'))
    Address = st.text_input("Address")
    phone_number = st.text_input("Phone Number")
    email_addr = st.text_input("Email Address")
    medical_history = st.text_area("Medical History")
    current_medications = st.text_area("Current Medication")
    family_medical_history = st.text_area("Family Medical History")
    
    if st.button("Save"):
        st.session_state.mode = PageType.NULL