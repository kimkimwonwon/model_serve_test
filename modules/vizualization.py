import streamlit as st
from st_files_connection import FilesConnection
import plotly.express as px

def get_data(stock_name, start_date, end_date):

    '''
    params:
        stock_name : 종목명
        start_date : 시작일
        end_date : 종료일


    '''
    conn = st.experimental_connection('s3', type= FilesConnection)
    name = conn.read("s3://mykafkastockbucket/batch/kospi_name_code_cp949.csv", input_format = "csv")
    df = conn.read("s3://mykafkastockbucket/batch/kospiTop200_daily_1year.csv", input_format = "csv")
    code = name[name['종목명'] == stock_name]['종목코드']
    code =  'A'+str(code).zfill(6)
    final_df = df[df['name'] == stock_name]
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
    chart = px.line(df, x = df.index , y = 'close', title = st.session_state.stock_name, width = 800, 
    height = 400 , template = 'plotly_dark')
    return chart