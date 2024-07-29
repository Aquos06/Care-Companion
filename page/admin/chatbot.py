import streamlit as st

if "message_history" not in st.session_state:
    st.session_state.message_history = []
if "is_user" not in st.session_state:
    st.session_state.is_user = True

def chatbot_ui():
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