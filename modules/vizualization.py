import streamlit as st
from st_files_connection import FilesConnection
import plotly.express as px
import pandas as pd     

def get_data(stock_name, start_date, end_date):

    '''
    params:
        stock_name : 종목명
        start_date : 시작일
        end_date : 종료일


    '''
    conn = st.experimental_connection('s3', type= FilesConnection)
    df = conn.read("s3://mykafkastockbucket/batch/dailymergedAll.csv", input_format = "csv")
    final_df = df[df['name'] == stock_name]
    final_df['date'] = final_df['date'].astype(str)
    final_df['date'] = pd.to_datetime(final_df['date']).dt.date

    final_df = final_df[(final_df['date'] >= start_date) & (final_df['date'] <= end_date)]
    final_df['date'] = pd.to_datetime(final_df['date'], format='%Y%m%d').dt.strftime('%Y-%m-%d')
    
    
    return final_df



def get_predicted_data(stock_name, start_date, end_date):

    '''
    params:
        stock_name : 종목명
        start_date : 시작일
        end_date : 종료일
    '''
    
    conn = st.experimental_connection('s3', type= FilesConnection)
    df = conn.read("s3://mykafkastockbucket/batch/320.csv", input_format = "csv")
    final_df = df[df['name'] == stock_name]
    final_df['date'] = final_df['date'].astype(str)
    final_df['date'] = pd.to_datetime(final_df['date']).dt.date

    final_df = final_df[(final_df['date'] >= start_date) & (final_df['date'] <= end_date)]
    final_df['date'] = pd.to_datetime(final_df['date'], format='%Y%m%d').dt.strftime('%Y-%m-%d')
    
    
    return final_df

# def get_minutes_data(stock_name, start_date, end_date):
    
#     '''
#     params:
#         stock_name : 종목명
#         start_date : 시작일
#         end_date : 종료일


#     '''
#     conn = st.experimental_connection('s3', type= FilesConnection)
#     name = conn.read("s3://mykafkastockbucket/batch/kospi_name_code_cp949.csv", input_format = "csv")
#     df = conn.read("s3://mykafkastockbucket/batch/kospiTop200_daily_1year.csv", input_format = "csv")
#     code = name[name['종목명'] == stock_name]['종목코드']
#     code =  'A'+str(code).zfill(6)
#     final_df = df[df['name'] == stock_name]

#     return final_df


def draw_chart(df):
    chart = px.line(df, x = 'date' , y = 'close', title = str(st.session_state.stock_name)+ ' 일자별 주가 그래프' ,
    width = 1000, height = 400 , template = 'plotly_dark')
    chart.update_xaxes(title='날짜')
    chart.update_yaxes(title='주가')
    return chart


def draw_chart_predict(df):
    
    chart = px.line(df, x = 'date' , y = 'close', title = str(st.session_state.stock_name)+ ' 일자별 주가 그래프' ,
    width = 1000, height = 400 , template = 'plotly_dark')
    
    # Add traces for 'pred1' and 'pred2'
    chart.add_scatter(x=df['date'], y=df['NBEATS'], mode='lines', name='NBEATS', line=dict(color='red'))
    chart.add_scatter(x=df['date'], y=df['NHITS'], mode='lines', name='NHITS', line=dict(color='green'))
 
    # Add titles    
    chart.update_xaxes(title='날짜')
    chart.update_yaxes(title='주가')
    
    return chart