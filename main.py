import streamlit as st

from type.page import PageType
from page.admin.chatbot import chatbot_ui
from page.admin.analyze import analyze_ui
from page.user.create_new import create_new_member_ui
from page.user.register import register_ui
from page.user.doctor_list import doctor_list_ui
from page.user.patient_chatbot import chatbot_patient_ui
from page.admin.patient_list import patient_list_ui
from utils.auth.login import login

if "mode" not in st.session_state:
    st.session_state.mode = PageType.NULL
if "user_email" not in st.session_state:
    st.session_state.user_email = ""

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
            st.session_state.mode = PageType.LOGIN
            
def login_page_ui():
    email = st.text_input("Email")
    password = st.text_input("Password",type="password")
    col1,col2 = st.columns(2)
    
    with col1:
        if st.button("register new member"):
            st.session_state.mode = PageType.REGISTER
            st.rerun()
            
    with col2:
        if st.button("login"):
            if login(email=email,password=password):
                st.session_state.mode = PageType.PATIENT
                st.session_state.user_email = email
                st.rerun()
            else:
                st.toast("Your Password or user name is wrong")
            
admin_page = st.Page(admin, title="Admin", icon=":material/login:")
patient_page = st.Page(patient, title="Patient", icon=":material/logout:")
dashboard_page = st.Page(dashboard, title="Dashboard", icon=":material/login:")
login_page = st.Page(login_page_ui, title="Login")

chatbot_page = st.Page(chatbot_ui, title="Chatbot")
analyze_page = st.Page(analyze_ui, title="Anaylze Patient")
patient_list_page = st.Page(patient_list_ui, title="Patient List")

register_page = st.Page(create_new_member_ui, title="Register New Member")
schedule_page = st.Page(register_ui, title="Register Schedule")
doctor_page = st.Page(doctor_list_ui, title="Doctor List")
patient_chatbot_page = st.Page(chatbot_patient_ui, title="Chatbot")

goback_page = st.Page(go_back, title="Back to menu")

if st.session_state.mode == PageType.NULL:
    pg=st.navigation([dashboard_page])
elif st.session_state.mode == PageType.ADMIN:
    pg = st.navigation({
        "Dashboard": [chatbot_page, analyze_page,patient_list_page],
        "Navigation": [goback_page]
        })
elif st.session_state.mode == PageType.PATIENT:
    pg = st.navigation({
        "Dashboard": [schedule_page, doctor_page, patient_chatbot_page],
        "Navigation": [goback_page]})
elif st.session_state.mode == PageType.REGISTER:
    pg = st.navigation([register_page,goback_page])
elif st.session_state.mode == PageType.LOGIN:
    pg = st.navigation([login_page,goback_page])
else:
    pg=st.navigation([dashboard_page])
    
pg.run()