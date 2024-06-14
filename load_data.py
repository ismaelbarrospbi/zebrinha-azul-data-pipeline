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

# Carregar os dados transformados
weather_data = pd.read_csv('transformed_weather_data.csv')
traffic_data = pd.read_csv('transformed_traffic_data.csv')

# Carregar os dados no banco de dados
weather_data.to_sql('weather_data', con=engine, if_exists='replace', index=False)
traffic_data.to_sql('traffic_data', con=engine, if_exists='replace', index=False)

print("Dados carregados no banco de dados com sucesso.")
