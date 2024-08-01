import streamlit as st
import pandas as pd

from utils.const import DOCTOR

def doctor_list_ui():
    df = pd.DataFrame(DOCTOR)
    
    st.title("Doctor Information")
    st.data_editor(df)