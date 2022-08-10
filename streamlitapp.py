import pandas as pd
import streamlit as st
import sqlite3
from sqlite3 import Error
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

conn = None
try:
    conn = sqlite3.connect('elf.db')
except Error as e:
    print(e)
    

st.title = ('Lumber Prices and Other Economic Metrics')

st.header('''
Lumber Prices and Other Economic Metrics
''')

def load_data():
    data = pd.read_sql_query("SELECT * FROM ELF_COMBO",conn)
    lowercase = lambda x: str(x).lower()
    data['Date'] = pd.to_datetime(data['Date']).dt.date
    return data

data = load_data()

data = data.set_index('Date')

#https://stackoverflow.com/questions/26414913/normalize-columns-of-a-dataframe
data3=(data-data.min())/(data.max()-data.min())

data3.reset_index(inplace=True)
data3 = data3.rename(columns = {'index':'Date'})
data3['Date'] = pd.to_datetime(data3['Date']).dt.date


#fig = px.line(data, x=data.index,y="Unemployment",title="US Unemployment")

#st.plotly_chart(fig, use_container_width=True)

cola, colb = st.columns(2)

with cola:
    dstart = st.date_input("Enter Start Date")
with colb:
    dend = st.date_input("Enter End Date")

#https://stackoverflow.com/questions/29370057/select-dataframe-rows-between-two-dates
mask = (data3["Date"] > dstart) & (data3["Date"] <=dend)

data2 = data3.loc[mask]

fig2 = go.Figure()

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.checkbox('Lumber Prices', value=True):
        fig2.add_trace(go.Scatter(x=data2["Date"], y=data2["Lumber_Price"],
                    mode='lines',
                    name='Lumber Prices'))
                    
    if st.checkbox('Interest Rates'):
        fig2.add_trace(go.Scatter(x=data2["Date"], y=data2["Interest_Rates"],
                    mode='lines',
                    name='Interest Rates'))

    if st.checkbox('Housing Price'):
        fig2.add_trace(go.Scatter(x=data2["Date"], y=data2["Housing_Price"],
                    mode='lines',
                    name='Housing Price'))
                    
    if st.checkbox('Covid Cases'):
        fig2.add_trace(go.Scatter(x=data2["Date"], y=data2["cases"],
                    mode='lines',
                    name='Covid Cases'))

    if st.checkbox('Covid Deaths'):
        fig2.add_trace(go.Scatter(x=data2["Date"], y=data2["deaths"],
                    mode='lines',
                    name='Covid Deaths'))
                    
with col2:
    if st.checkbox('CPI'):
        fig2.add_trace(go.Scatter(x=data2["Date"], y=data2["Consumer_Price_Index"],
                    mode='lines',
                    name='CPI'))
                    
    if st.checkbox('PPI'):
        fig2.add_trace(go.Scatter(x=data2["Date"], y=data2["Producer_Price_Index"],
                    mode='lines',
                    name='Producer Price Index'))
               
    if st.checkbox('Sentiment Index'):
        fig2.add_trace(go.Scatter(x=data2["Date"], y=data2["Sentiment_Index"],
                    mode='lines',
                    name='Sentiment Index'))
                                   
    if st.checkbox('Govt Debt'):
        fig2.add_trace(go.Scatter(x=data2["Date"], y=data2["Govt_Debt"],
                    mode='lines',
                    name='Govt Debt'))
                    
    if st.checkbox('Money Supply'):
        fig2.add_trace(go.Scatter(x=data2["Date"], y=data2["Money_Supply"],
                    mode='lines',
                    name='Money Supply'))
                    
with col3:
    if st.checkbox('Elect Prod'):
        fig2.add_trace(go.Scatter(x=data2["Date"], y=data2["Elect_Prod"],
                    mode='lines',
                    name='Electrical Production'))
                    
    if st.checkbox('Oil Prod'):
        fig2.add_trace(go.Scatter(x=data2["Date"], y=data2["Oil_Prod"],
                    mode='lines',
                    name='Oil Prod'))
                    
    if st.checkbox('Ind Prod'):
        fig2.add_trace(go.Scatter(x=data2["Date"], y=data2["Industrial_Production"],
                    mode='lines',
                    name='Industrial Production'))
                    
    if st.checkbox('Wages Manuf'):
        fig2.add_trace(go.Scatter(x=data2["Date"], y=data2["Hourly_Wage_Manuf"],
                    mode='lines',
                    name='Hourly Wage Manuf'))
                    
    if st.checkbox('Job Vacancy Rate'):
        fig2.add_trace(go.Scatter(x=data2["Date"], y=data2["Job_Vacancy_Rate"],
                    mode='lines',
                    name='Job Vacancy Rate'))
                                      
with col4:
    if st.checkbox('Gas Demand'):
        fig2.add_trace(go.Scatter(x=data2["Date"], y=data2["Gas_Demand"],
                    mode='lines',
                    name='Gas Demand'))
                    
    if st.checkbox('Oil Demand'):
        fig2.add_trace(go.Scatter(x=data2["Date"], y=data2["Oil_Demand"],
                    mode='lines',
                    name='Oil Demand'))
                    
    if st.checkbox('Gasoline Demand'):
        fig2.add_trace(go.Scatter(x=data2["Date"], y=data2["Gasoline_Demand"],
                    mode='lines',
                    name='Gasoline Demand'))
                    
    if st.checkbox('Retail Trade'):
        fig2.add_trace(go.Scatter(x=data2["Date"], y=data2["Retail_Trade"],
                    mode='lines',
                    name='Retail Trade'))
                    
    if st.checkbox('Stock Exchange'):
        fig2.add_trace(go.Scatter(x=data2["Date"], y=data2["Stock_Exchange"],
                    mode='lines',
                    name='Stock Exchange'))
                    
st.plotly_chart(fig2, use_container_width=False)

st.write(data)
