import streamlit as st
from st_files_connection import FilesConnection

st.title("Hello World")


conn = st.experimental_connection('s3', type=FilesConnection)

csv = conn.read("s3://mykafkastockbucket/topics/stock-tutorial/test/simple.csv", input_format="csv")




st.write(csv)