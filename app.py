from time import time
import streamlit as st
import plotly.express as px 
from st_files_connection import FilesConnection
from modules.vizualization import *
from modules.st_initial import *
import datetime


st.set_page_config(layout="wide")
# 화면분할
main1, main2 = st.columns([0.6,0.4])

# session_state 초기화
initialize()




#  ---------   --------- 

st.title("YBIGTA 2023-1 Conference😎")

st.sidebar.title("Market Early 📈")

st.sidebar.text_input(label="Search Stock", value="AAPL🍎",key="stock_name")

start_date = st.sidebar.date_input("Start Date", value=datetime.date(2021, 1, 1))

end_date = st.sidebar.date_input("End Date", value=datetime.date(2021, 1, 31))

day_or_minutes = st.sidebar.radio("Day or Minutes", ["Day", "Minutes"])


st.sidebar.markdown(day_or_minutes)


predict_start = st.sidebar.button('Predict Start')


df =  get_data(st.session_state.stock_name, start_date, end_date)





if predict_start :
    st.balloons()
    chart = px.line()
    main1.st.plotlychart()




# get module from : modules vizualization.py  - > st.write(hi())

st.write(st.session_state.stock_name)



conn = st.experimental_connection('s3', type=FilesConnection)
csv = conn.read("s3://mykafkastockbucket/topics/stock-tutorial/test/simple.csv", input_format="csv")




st.write(csv)