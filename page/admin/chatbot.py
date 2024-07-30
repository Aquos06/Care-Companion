import streamlit as st
from utils.inference.service import AI71Inference

def chatbot_ui():
    if "message_history" not in st.session_state:
        st.session_state.message_history = []

    LLM = AI71Inference()
    
    for chat in st.session_state.message_history:
        with st.chat_message(chat['role']):
            st.markdown(chat['content'])
    
    

    if query:= st.chat_input("Say something"):
        st.session_state.message_history.append({"role":"user","content":str(query)})

        with st.chat_message("user"):
            st.markdown(query)
        
        with st.chat_message("assistant"):
            response = st.write_stream(LLM.inference(history=st.session_state.message_history))
            
        st.session_state.message_history.append({"role":"assistant","content": response})
