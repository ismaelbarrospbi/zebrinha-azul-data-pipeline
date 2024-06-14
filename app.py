import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Variáveis de conexão com o banco de dados
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

# String de conexão
connection_string = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Criar a engine de conexão
engine = create_engine(connection_string)

# Função para carregar dados do banco de dados
def load_data(table_name):
    query = f"SELECT * FROM {table_name}"
    data = pd.read_sql(query, con=engine)
    return data

# Carregar dados
weather_data = load_data('weather_data')
traffic_data = load_data('traffic_data')

# Criar visualizações
st.title('Zebrinha Azul Data Visualization')
st.header('Weather Data')
st.dataframe(weather_data)

st.header('Traffic Data')
st.dataframe(traffic_data)

# Visualizações adicionais
st.line_chart(weather_data[['temperature', 'timestamp']].set_index('timestamp'))
st.bar_chart(traffic_data[['route_summary', 'duration']].set_index('route_summary'))
