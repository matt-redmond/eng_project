from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import os
from selenium import webdriver
import sqlite3
from sqlite3 import Error

conn = None
try:
    conn = sqlite3.connect('elf.db')
except Error as e:
    print(e)

cursor = conn.cursor()

   
#Consumer price index
cursor.execute("DROP TABLE Consumer_Price_Index")
df2 = pd.read_csv('https://www.econdb.com/api/series/CPIUS/?format=csv',index_col='Date', parse_dates=['Date'])
df2.to_sql(name='Consumer_Price_Index', con=conn)
#Unemployment
cursor.execute("DROP TABLE Unemployment")
df3 = pd.read_csv('https://www.econdb.com/api/series/URATEUS/?format=csv',index_col='Date', parse_dates=['Date'])
df3.to_sql(name='Unemployment', con=conn)
#Retail Trade
cursor.execute("DROP TABLE Retail_Trade")
df4 = pd.read_csv('https://www.econdb.com/api/series/RETAUS/?format=csv', index_col='Date', parse_dates=['Date'])
df4.to_sql(name='Retail_Trade', con=conn)
#Housing
cursor.execute("DROP TABLE Housing_Price")
df5 = pd.read_csv('https://www.econdb.com/api/series/HOUUS/?format=csv',index_col='Date', parse_dates=['Date'])
df5.to_sql(name='Housing_Price', con=conn)
#hourly wage manufacturing
cursor.execute("DROP TABLE Hourly_Wage_Manuf")
df6 = pd.read_csv('https://www.econdb.com/api/series/WAGEMANUS/?format=csv',index_col='Date', parse_dates=['Date'])
df6.to_sql(name='Hourly_Wage_Manuf', con=conn)
#interest rates
cursor.execute("DROP TABLE Interest_Rates")
df7 = pd.read_csv('https://www.econdb.com/api/series/POLIRUS/?format=csv',index_col='Date', parse_dates=['Date'])
df7.to_sql(name='Interest_Rates', con=conn)
#sentiment index
cursor.execute("DROP TABLE Sentiment_Index")
df8 = pd.read_csv('https://www.econdb.com/api/series/SENTUS/?format=csv',index_col='Date', parse_dates=['Date'])
df8.to_sql(name='Sentiment_Index', con=conn)
#stock exchange index
cursor.execute("DROP TABLE Stock_Exchange")
df9 = pd.read_csv('https://www.econdb.com/api/series/SEIUS/?format=csv',index_col='Date', parse_dates=['Date'])
df9.to_sql(name='Stock_Exchange', con=conn)
#change in inventories
cursor.execute("DROP TABLE Inventory_Change")
df10 = pd.read_csv('https://www.econdb.com/api/series/CIUS/?format=csv',index_col='Date', parse_dates=['Date'])
df10.to_sql(name='Inventory_Change', con=conn)
#money supply
cursor.execute("DROP TABLE Money_Supply")
df11 = pd.read_csv('https://www.econdb.com/api/series/M3US/?format=csv',index_col='Date', parse_dates=['Date'])
df11.to_sql(name='Money_Supply', con=conn)
#electricity production
cursor.execute("DROP TABLE Elect_Prod")
df12 = pd.read_csv('https://www.econdb.com/api/series/ELEUS/?format=csv',index_col='Date', parse_dates=['Date'])
df12.to_sql(name='Elect_Prod', con=conn)
#oil production
cursor.execute("DROP TABLE Oil_Prod")
df13 = pd.read_csv('https://www.econdb.com/api/series/OILPRODUS/?format=csv',index_col='Date', parse_dates=['Date'])
df13.to_sql(name='Oil_Prod', con=conn)
#industrial production
cursor.execute("DROP TABLE Industrial_Production")
df14=pd.read_csv('https://www.econdb.com/api/series/IPUS/?format=csv',index_col='Date', parse_dates=['Date'])
df14.to_sql(name='Industrial_Production', con=conn)
#real gross domestic product
cursor.execute("DROP TABLE Real_GDP")
df15=pd.read_csv('https://www.econdb.com/api/series/RGDPUS/?format=csv',index_col='Date', parse_dates=['Date'])
df15.to_sql(name='Real_GDP', con=conn)
#Producer price Index
cursor.execute("DROP TABLE Producer_Price_Index")
df16=pd.read_csv('https://www.econdb.com/api/series/PPIUS/?format=csv',index_col='Date', parse_dates=['Date'])
df16.to_sql(name='Producer_Price_Index', con=conn)
#Government Debt
cursor.execute("DROP TABLE Govt_Debt")
df17=pd.read_csv('https://www.econdb.com/api/series/GDEBTUS/?format=csv',index_col='Date', parse_dates=['Date'])
df17.to_sql(name='Govt_Debt', con=conn)
#Export Goods
cursor.execute("DROP TABLE Export_Goods_Services")
df18=pd.read_csv('https://www.econdb.com/api/series/EXPUS/?format=csv',index_col='Date', parse_dates=['Date'])
df18.to_sql(name='Export_Goods_Services', con=conn)
#Import Goods
cursor.execute("DROP TABLE Import_Goods_Services")
df19=pd.read_csv('https://www.econdb.com/api/series/IMPUS/?format=csv',index_col='Date', parse_dates=['Date'])
df19.to_sql(name='Import_Goods_Services', con=conn)
#Job Vacancy Rate
cursor.execute("DROP TABLE Job_Vacancy_Rate")
df20=pd.read_csv('https://www.econdb.com/api/series/JVRUS/?format=csv',index_col='Date', parse_dates=['Date'])
df20.to_sql(name='Job_Vacancy_Rate', con=conn)
#General Govt Total Expenditure
cursor.execute("DROP TABLE Gen_Govt_Tot_Expenditure")
df21=pd.read_csv('https://www.econdb.com/api/series/GSPEUS/?format=csv',index_col='Date', parse_dates=['Date'])
df21.to_sql(name='Gen_Govt_Tot_Expenditure', con=conn)
#Gasoline Demand
cursor.execute("DROP TABLE Gasoline_Demand")
df23=pd.read_csv('https://www.econdb.com/api/series/GASODEMUS/?format=csv',index_col='Date', parse_dates=['Date'])
df23.to_sql(name='Gasoline_Demand', con=conn)
#Oil Demand
cursor.execute("DROP TABLE Oil_Demand")
df24=pd.read_csv('https://www.econdb.com/api/series/OILDEMUS/?format=csv',index_col='Date', parse_dates=['Date'])
df24.to_sql(name='Oil_Demand', con=conn)
#Gas Demand
cursor.execute("DROP TABLE Gas_Demand")
df25=pd.read_csv('https://www.econdb.com/api/series/GASDEMUS/?format=csv',index_col='Date', parse_dates=['Date'])
df25.to_sql(name='Gas_Demand', con=conn)
#COVID
cursor.execute("DROP TABLE COVID")
df26=pd.read_csv('https://api.covidactnow.org/v2/country/US.timeseries.csv?apiKey=9ea206e96d044285aeea6455fe2144cb')
df26.to_sql(name='COVID', con=conn)

cursor.execute("INSERT INTO TIME_UPDATED SELECT datetime('now')")

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()
