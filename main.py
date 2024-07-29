import streamlit as st
from type.page import PageType
# from page.chatbot import chatbot

if "mode" not in st.session_state:
    st.session_state.mode = PageType.NULL
if "message_history" not in st.session_state:
    st.session_state.message_history = []
if "is_user" not in st.session_state:
    st.session_state.is_user = True

def login():
    if st.button("Admin"):
        st.session_state.mode = PageType.ADMIN
        st.rerun()

def logout():
    if st.button("Patient"):
        st.session_state.mode = PageType.PATIENT
        st.rerun()
        
def dashboard():
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Admin"):
            st.session_state.mode = PageType.ADMIN
    with col2:
        if st.button("Patient"):
            st.session_state.mode = PageType.PATIENT
            
def chatbot():
    query = st.chat_input("Say something")

    if query:
        if st.session_state.is_user:
            st.session_state.message_history.append({"role":"user","content":str(query)})
            st.session_state.is_user = False
        else:
            st.session_state.message_history.append({"role":"system", "content": str(query)})
            st.session_state.is_user = True
            
        for chat in st.session_state.message_history:
            if chat["role"] == "user":
                st.chat_message("user").write(chat['content'])    
            else:
                st.chat_message("bot").write(chat['content']) 
                
        print(st.session_state.message_history)
                
                    
admin_page = st.Page(login, title="Admin", icon=":material/login:")
patient_page = st.Page(logout, title="Patient", icon=":material/logout:")
dashboard_page = st.Page(dashboard, title="Dashboard", icon=":material/login:")

chatbot_page = st.Page(chatbot, title="Chatbot")

# dashboard = st.Page(
#     "main.py", title="Dashboard", icon=":material/dashboard:", default=True
# )
# bugs = st.Page("main.py", title="Bug reports", icon=":material/bug_report:")
# alerts = st.Page(
#     "main.py", title="System alerts", icon=":material/notification_important:"
# )

# search = st.Page("main.py", title="Search", icon=":material/search:")
# history = st.Page("main.py", title="History", icon=":material/history:")

if st.session_state.mode == PageType.NULL:
    pg=st.navigation([dashboard_page])
elif st.session_state.mode == PageType.ADMIN:
    pg = st.navigation([chatbot_page, patient_page])
elif st.session_state.mode == PageType.PATIENT:
    pg = st.navigation([admin_page, patient_page])
else:
    pg=st.navigation([dashboard_page])
    

pg.run()