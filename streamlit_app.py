import requests
import pandas as pd 
from API_KEY import api_key
import streamlit as st 

base_url = 'https://financialmodelingprep.com/api/v3'

st.header('Fall 2023 SIF Stock Screener')
symbol = st.sidebar.text_input('Ticker:',value='UIS')
financial_data = st.sidebar.selectbox('Financial Data Type',options=('income-statement', 'balance-sheet-statement', 'cash-flow-statement', 'income-statement-growth', 'balance-sheet-statement-growth', 'cash-flow-statement-growth', 'ratios-ttm', 'ratios', 'financial-growth', 'quote', 'rating', 'enterprise-values', 'key-metrics-ttm', 'key-metrics', 'historical-rating', 'discounted-cash-flow', 'historical-discounted-cash-flow-statement', 'historical-price-full', 'Historical Price smaller intervals'))

if financial_data == 'Historical Price smaller intervals':
    interval = st.sidebar.selectbox('Interval', options=('1min','5min','15min','30min','1hour','4hour'))
    financial_data = 'historical-chart/'+interval

transpose = st.sidebar.selectbox('Transpose', options=('Yes',"No"))
url = f'{base_url}/{financial_data}/{symbol}?apikey={api_key}'
response = requests.get(url)
data = response.json()

if transpose == 'Yes':
    df = pd.DataFrame(data).T
else:
   df = pd.DataFrame(data)
st.write(df)

