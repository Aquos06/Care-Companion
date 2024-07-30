import streamlit as st

from type.page import PageType
from page.admin.chatbot import chatbot_ui
from page.admin.analyze import analyze_ui
from page.admin.drugs import drugs_list_ui
from page.user.create_new import create_new_member_ui

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
drugs_page = st.Page(drugs_list_ui, title="Drugs List")

register_page = st.Page(create_new_member_ui, title="Register Schedule")
goback_page = st.Page(go_back, title="Back to menu")

if st.session_state.mode == PageType.NULL:
    pg=st.navigation([dashboard_page])
elif st.session_state.mode == PageType.ADMIN:
    pg = st.navigation({
        "Dashboard": [chatbot_page, analyze_page,drugs_page],
        "Navigation": [goback_page]
        })
elif st.session_state.mode == PageType.PATIENT:
    pg = st.navigation({
        "Dashboard": [register_page],
        "Navigation": [goback_page]})
else:
    pg=st.navigation([dashboard_page])
    
pg.run()