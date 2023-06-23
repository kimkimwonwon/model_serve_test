from time import time
import streamlit as st
import plotly.express as px 
from st_files_connection import FilesConnection
from modules.vizualization import *
from modules.st_initial import *
import datetime
import time
import requests
import json
import numpy as np



def count_outliers(lst):
    mean = np.mean(lst)
    std = np.std(lst)
    
    lower_bound = mean - 2 * std
    upper_bound = mean + 2 * std
    
    outliers = [x for x in lst if x < lower_bound or x > upper_bound]
    num_outliers = len(outliers)
    
    return num_outliers

def standard_scale(lst):
    # 리스트를 numpy 배열로 변환
    arr = np.array(lst)
    
    # 평균과 표준 편차 계산
    mean = np.mean(arr)
    std = np.std(arr)
    
    # 표준화 수식 적용
    scaled_arr = (arr - mean) / std
    
    # 표준화된 배열 반환
    return scaled_arr.tolist()



st.set_page_config(layout="wide")
# 화면분할
# session_state 초기화
initialize()

st.image('imgs/market_early_logo.png', width = 100 )

main_page ,Modeling  ,  Role ,source_code =  st.tabs(['🌟 Main Page 🌟' , '🤖 Modeling 🤖',  'R&R', 'Source_Code'])

#  ---------   --------- 

main_page.title("YBIGTA 2023-1 Conference 😎")

st.sidebar.title("Market Early 📈")
st.sidebar.text_input(label="Search Stock", value="AAPL🍎",key="stock_name")
search_button = st.sidebar.button('Search')
start_date = st.sidebar.date_input("Start Date", value=datetime.date(2022, 5, 20))
end_date = st.sidebar.date_input("End Date", value=datetime.date(2023, 5, 20))
st.sidebar.radio("Day or Minutes", ["Day", "Minutes"],key='day_or_minutes')

predict_start = st.sidebar.button('Predict Start 🔍')

# UI_sidebar

with main_page:
    main1, main2 = st.columns([0.6,0.4])


# ------------------


if search_button:
    df =  get_data(st.session_state.stock_name, start_date, end_date)
    st.session_state.df  = df 
    #st.table(df)
    chart = draw_chart(df)
    main_page.plotly_chart(chart)
    main_page.write(df.tail())

# elif search_button and st.session_state.day_or_minutes == "Minutes": 
#     df =  get_minutes_data(st.session_state.stock_name, start_date, end_date)


# ------------------



if predict_start :
    if st.  session_state.stock_name != '':
        with st.spinner('Wait for it...'):
            time.sleep(3)
        
        main_page.header('Reconstruction Error Outlier of autoencoder')

        df =  get_data(st.session_state.stock_name, start_date, end_date)

        column_names = ['open', 'high', 'low', 'close', 'vol', 'value', 'agg_price', 'foreign_rate', 'agency_buy', 'agency_netbuy']
        tmp_df = df[column_names]
        tail_df = tmp_df[-15:]

        time_series = []
        for _, row in tail_df.iterrows():
            time_series.append({
                "high": row['high'],
                "open": row['open'],
                "low": row['low'],
                "close": row['close'],
                "vol": row['vol'],
                "value": row['value'],
                "agg_price": row['agg_price'],
                "foreign_rate": row['foreign_rate'],
                "agency_buy": row['agency_buy'],
                "agency_netbuy": row['agency_netbuy']
            })

        sample_json = {
            "time_series" : time_series,
            # "stock_name" : "삼성전자"
        }

        


        # AutoEncoder 
        URL =  'http://localhost:8080/2015-03-31/functions/function/invocations'
        response = requests.post(url= URL, json= sample_json)
        body = response.json()['body']
        prediction = json.loads(body)['prediction']

        num_outlier = count_outliers(prediction)
        scaled_prediction = standard_scale(prediction)

        scaled_prediction_df = pd.DataFrame({'value': scaled_prediction})
        fig = px.histogram(scaled_prediction_df, x='value', nbins=20)

        fig.update_layout(
            title="Standardized Reconstruction Error Histogram",
            xaxis_title="Value",
            yaxis_title="Frequency",
            bargap=0.1
        )

        main_page.plotly_chart(fig)

        

        if num_outlier > 3: 
            main1.metric(f"Reconstruction Error Outlier : {num_outlier}" , "⛈️" , "your stock is in danger" ,delta_color ="inverse")
        if num_outlier <= 3: 
            main1.metric(f"Reconstruction Error Outlier {num_outlier}" , "☀️" , "your stock is in safe" )

        main_page.success('Done!')
    else:
        main_page.error('Please Search Stock First!')



with source_code:
    code_col1 ,code_col2 = st.columns([0.7,0.3])
    code_col1.title("Source Code 📃")
    code_col1.image('imgs/gitlogo.png')
    link = '[Model GitHub Link](https://github.com/kimkimwonwon/model_serve_test)'
    code_col1.markdown(link, unsafe_allow_html=True)



with Modeling:
    #modeling.title("Model Architecture 🤖")
    modeling_col1, modeling_col2 = st.columns([1,1])
    modeling_col1.title("Data Pipeline")
    modeling_col1.image('imgs/DataPipeline.png')
    modeling_col2.title("Model Architecture")
    modeling_col2.image('imgs/NeuralForecast.png')


with Role:
    Role.title("Role 🤝")
    Role.image('imgs/randr.png')
    
    

