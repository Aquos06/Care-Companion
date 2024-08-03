import copy
import requests
import streamlit as st
from brave import Brave
from bs4 import BeautifulSoup
from utils.inference.service import AI71Inference
from utils.database.graph import Neo4Graph
from utils.const import BRAVE_API_KEY

def web_search(query):
    brave = Brave(api_key=BRAVE_API_KEY)
    num_results = 1
    search_result = brave.search(q=query, count=num_results)
    web_search = search_result.web_results
    
    search_results_list = []
    for i in web_search:
        result_list = []
        response = requests.get(i['url'])
        st.session_state.links.append(str(i['url']))
        if response.status_code != 200:
            continue
    
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('p')
        for i in articles:
            result_list.append(i.text)
            
        search_results_list.append("\n".join(result_list))
    
    return search_results_list

def get_patient_name():
    graph = Neo4Graph()
    cypher = ["MATCH (p:Patient) RETURN p.full_name"]
    names = graph.read_transaction(queries=cypher)
    full_name = [name['p.full_name'] for name in names[0]]
    return full_name

def format_user_query():
    graph = Neo4Graph()
    user_query  = copy.deepcopy(st.session_state.message_history)
    last_user_query:str = user_query[-1]

    for name in st.session_state.patient_name:
        if str(name).lower() in last_user_query['content'].lower():
            cypher = [f"MATCH (p:Patient {{full_name: '{name}'}})-[r]->(related) RETURN p,r,related"]
            patient_record = graph.read_transaction(queries=cypher)
            user_query[-1]["content"] = f"""
                                        Patient Record: {patient_record}
                                        {last_user_query['content']}
                                        """
            return [user_query[-1]]
        
    search_result = web_search(query=str(last_user_query['content']))
    user_query[-1]['content'] = f"""
            {search_result}
            {last_user_query['content']}
    """
    return [user_query[-1]]
        
def format_response():
    if st.session_state.links:
        links = "\n".join(st.session_state.links)
        return f"""
                \nLinks:
                    {links}
                """

def chatbot_ui():
    if "patient_name" not in st.session_state:
        st.session_state.patient_name = get_patient_name()
    if "message_history" not in st.session_state:
        st.session_state.message_history = []
    if "links" not in st.session_state:
        st.session_state.links = []

    LLM = AI71Inference()
    
    for chat in st.session_state.message_history:
        with st.chat_message(chat['role']):
            st.markdown(chat['content'])
    
    if query:= st.chat_input("Say something"):
        st.session_state.message_history.append({"role":"user","content":str(query)})

        with st.chat_message("user"):
            st.markdown(query)
        
        with st.chat_message("assistant"):
            response = st.write_stream(LLM.inference(history=format_user_query(),links=format_response()))
        st.session_state.links = []
        st.session_state.message_history.append({"role":"assistant","content": response})
