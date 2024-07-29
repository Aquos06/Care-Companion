import streamlit as st

def chatbot():
    if "message_history" not in st.session_state:
        st.session_state.message_history = []
        
    def chat_input_send():
        st.session_state.message_history.append(query)
    
    query = st.chat_input("Say something",on_submit=chat_input_send)

    chat_container = st.empty()
    for chat in st.session_state.message_history:
        print(chat)
        chat_container.chat_message("user").write(chat)    