import streamlit as st

from type.page import PageType
from page.admin.chatbot import chatbot_ui
from page.admin.analyze import analyze_ui
from page.user.create_new import create_new_member_ui
from page.user.register import register_ui
from page.user.doctor_list import doctor_list_ui
from page.user.patient_chatbot import chatbot_patient_ui

if "mode" not in st.session_state:
    st.session_state.mode = PageType.NULL

def admin():
    if st.button("Admin"):
        st.session_state.mode = PageType.ADMIN
        st.rerun()

def patient():
    if st.button("Patient"):
        st.session_state.mode = PageType.PATIENT
        st.rerun()
        
def go_back():
    st.session_state.mode = PageType.NULL
        
def dashboard():
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Admin"):
            st.session_state.mode = PageType.ADMIN
    with col2:
        if st.button("Patient"):
            st.session_state.mode = PageType.PATIENT
            
admin_page = st.Page(admin, title="Admin", icon=":material/login:")
patient_page = st.Page(patient, title="Patient", icon=":material/logout:")
dashboard_page = st.Page(dashboard, title="Dashboard", icon=":material/login:")

chatbot_page = st.Page(chatbot_ui, title="Chatbot")
analyze_page = st.Page(analyze_ui, title="Anaylze Patient")

register_page = st.Page(create_new_member_ui, title="Register New Member")
schedule_page = st.Page(register_ui, title="Register Schedule")
doctor_page = st.Page(doctor_list_ui, title="Doctor List")
patient_chatbot_page = st.Page(chatbot_patient_ui, title="Chatbot")

goback_page = st.Page(go_back, title="Back to menu")

if st.session_state.mode == PageType.NULL:
    pg=st.navigation([dashboard_page])
elif st.session_state.mode == PageType.ADMIN:
    pg = st.navigation({
        "Dashboard": [chatbot_page, analyze_page],
        "Navigation": [goback_page]
        })
elif st.session_state.mode == PageType.PATIENT:
    pg = st.navigation({
        "Dashboard": [register_page, schedule_page, doctor_page, patient_chatbot_page],
        "Navigation": [goback_page]})
else:
    pg=st.navigation([dashboard_page])
    
pg.run()