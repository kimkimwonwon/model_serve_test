import streamlit as st
from st_files_connection import FilesConnection
from modules.vizualization import *

st.set_page_config(layout="wide")

if 'stock_name' not in st.session_state:
    st.session_state['user_name'] = ''

st.title("Market Early 😎")

st.sidebar.title("Market Early 📈")



st.sidebar.text_input(label="Search Stock", value="AAPL🍎",key="stock_name")


# get module from : modules vizualization.py  - > st.write(hi())

st.write(st.session_state.stock_name)





conn = st.experimental_connection('s3', type=FilesConnection)
csv = conn.read("s3://mykafkastockbucket/topics/stock-tutorial/test/simple.csv", input_format="csv")







st.write(csv)