from time import time
import streamlit as st
import plotly.express as px 
from st_files_connection import FilesConnection
from modules.vizualization import *
from modules.st_initial import *
import datetime
import time

st.set_page_config(layout="wide")
# 화면분할
# session_state 초기화
initialize()

main_page, source_code , modeling  =  st.tabs(['Main Page' , 'Source_Code' , 'Modeling'])

#  ---------   --------- 

main_page.title("YBIGTA 2023-1 Conference 😎")

st.sidebar.title("Market Early 📈")
st.sidebar.text_input(label="Search Stock", value="AAPL🍎",key="stock_name")
search_button = st.sidebar.button('Search')
start_date = st.sidebar.date_input("Start Date", value=datetime.date(2021, 1, 1))
end_date = st.sidebar.date_input("End Date", value=datetime.date(2021, 1, 31))
st.sidebar.radio("Day or Minutes", ["Day", "Minutes"],key='day_or_minutes')

predict_start = st.sidebar.button('Predict Start')

# UI_sidebar

with main_page:
    main1, main2 = st.columns([0.6,0.4])


# ------------------


if search_button:
    df =  get_data(st.session_state.stock_name, start_date, end_date)
    #st.table(df)
    chart = draw_chart(df)
    main_page.plotly_chart(chart)
    main_page.write(df.tail())

# elif search_button and st.session_state.day_or_minutes == "Minutes": 
#     df =  get_minutes_data(st.session_state.stock_name, start_date, end_date)


# ------------------



if predict_start :

    with st.spinner('Wait for it...'):
        time.sleep(3)
    main1.success('Done!')


    # 모델링 
    # chart = px.line()
    # main1.st.plotlychart()
    main1.metric("hi" , " hello 117% " , "your stock is in danger" )
    main2.metric("hellow !!!  " , " hello 117% " , "your stock is in danger", delta_color ="inverse")


with source_code:
    code_col1 ,code_col2 = st.columns([0.7,0.3])
    code_col1.title("Source Code 📃")
    code_col1.image('imgs/gitlogo.png')
    link = '[Model GitHub Link](https://github.com/kimkimwonwon/model_serve_test)'
    code_col1.markdown(link, unsafe_allow_html=True)






with modeling:
    #modeling.title("Model Architecture 🤖")
    modeling_col1, modeling_col2 = st.columns([0.6,0.4])
    modeling_col1.title("Data Pipeline")
    modeling_col1.image('imgs/DataPipeline.png')
    modeling_col2.title("Model Architecture")
    modeling_col2.image('imgs/NeuralForecast.png')


# get module from : modules vizualization.py  - > st.write(hi())


# conn = st.experimental_connection('s3', type=FilesConnection)
# csv = conn.read("s3://mykafkastockbucket/topics/stock-tutorial/test/simple.csv", input_format="csv")
# st.write(csv)