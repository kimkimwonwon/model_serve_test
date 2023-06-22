import streamlit as st
from st_files_connection import FilesConnection

def get_data(stock_name, start_date, end_date):

    '''
    params:
        stock_name : 종목명
        start_date : 시작일
        end_date : 종료일


    '''
    conn = st.experimental_connection('s3', type=FilesConnection)
    name = conn.read("s3://mykafkastockbucket/batch/kospi_name_code.csv", input_format="csv")
    df = conn.read("s3://mykafkastockbucket/batch/kospiTop200_daily_1year.csv", input_format="csv")
    code = name[name['name'] == stock_name]['code'].values[0]
    final_df = df[df['code'] == code]


    return final_df