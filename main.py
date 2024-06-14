import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Chaves das APIs
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
TRAFFIC_API_KEY = os.getenv("TRAFFIC_API_KEY")

# URLs das APIs
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q=London&appid={WEATHER_API_KEY}&units=metric"
traffic_url = f"https://maps.googleapis.com/maps/api/directions/json?origin=place_id:ChIJ685WIFYViEgRHlHvBbiD5nE&destination=place_id:ChIJdd4hrwug2EcRmSrV3Vo6llI&key={TRAFFIC_API_KEY}"

def extract_weather_data():
    print("Iniciando extração de dados de clima...")
    response = requests.get(weather_url)
    if response.status_code == 200:
        data = response.json()
        weather_df = pd.json_normalize(data)
        print("Extração de dados de clima concluída com sucesso.")
        return weather_df, data
    else:
        raise Exception(f"Falha na extração de dados de clima: {response.status_code}")

def extract_traffic_data():
    print("Iniciando extração de dados de trânsito...")
    response = requests.get(traffic_url)
    if response.status_code == 200:
        data = response.json()
        print("Estrutura dos dados de trânsito:", data)
        traffic_df = pd.json_normalize(data['routes'])
        print("Extração de dados de trânsito concluída com sucesso.")
        return traffic_df, data
    else:
        raise Exception(f"Falha na extração de dados de trânsito: {response.status_code}")

def transform_weather_data(weather_df):
    print("Iniciando transformação de dados de clima...")
    weather_df['timestamp'] = datetime.now()
    weather_df = weather_df[['name', 'weather', 'main.temp', 'main.humidity', 'wind.speed', 'timestamp']]
    weather_df.columns = ['city', 'weather', 'temperature', 'humidity', 'wind_speed', 'timestamp']
    weather_df['weather'] = weather_df['weather'].apply(lambda x: x[0]['description'] if isinstance(x, list) and len(x) > 0 else None)
    print("Transformação de dados de clima concluída com sucesso.")
    return weather_df

def transform_traffic_data(traffic_df):
    print("Iniciando transformação de dados de trânsito...")
    if not traffic_df.empty:
        traffic_df['timestamp'] = datetime.now()
        traffic_df = traffic_df[['summary', 'legs', 'timestamp']]
        traffic_df = traffic_df.explode('legs')  # Expandir a lista 'legs'
        traffic_df['duration'] = traffic_df['legs'].apply(lambda x: x['duration']['text'] if isinstance(x, dict) else None)
        traffic_df = traffic_df[['summary', 'duration', 'timestamp']]
        traffic_df.columns = ['route_summary', 'duration', 'timestamp']
    else:
        traffic_df = pd.DataFrame(columns=['route_summary', 'duration', 'timestamp'])
    print("Transformação de dados de trânsito concluída com sucesso.")
    return traffic_df

if __name__ == "__main__":
    try:
        # Extração
        weather_data, raw_weather_data = extract_weather_data()
        traffic_data, raw_traffic_data = extract_traffic_data()
        
        # Salvar os dados brutos em arquivos CSV
        raw_weather_df = pd.json_normalize(raw_weather_data)
        raw_weather_df.to_csv('raw_weather_data.csv', index=False)
        raw_traffic_df = pd.json_normalize(raw_traffic_data['routes'])
        raw_traffic_df.to_csv('raw_traffic_data.csv', index=False)

        # Transformação
        transformed_weather_data = transform_weather_data(weather_data)
        transformed_traffic_data = transform_traffic_data(traffic_data)
        
        # Salvar os dados transformados em arquivos CSV
        transformed_weather_data.to_csv('transformed_weather_data.csv', index=False)
        transformed_traffic_data.to_csv('transformed_traffic_data.csv', index=False)
        
        print("Extração e transformação concluídas com sucesso.")
    except Exception as e:
        print(f"Erro: {e}")
