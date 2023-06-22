import streamlit as st

session_state_keys = [ 'stock_name' ] 

def initialize():

    for key in session_state_keys:
        if key not in st.session_state:
            st.session_state[key] = ''

