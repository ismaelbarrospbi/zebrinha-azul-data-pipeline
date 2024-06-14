-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS zebrinha_azul;

-- Uso do banco de dados
USE zebrinha_azul;

-- Tabela para dados de clima
CREATE TABLE IF NOT EXISTS weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    temperature DECIMAL(5, 2),
    humidity DECIMAL(5, 2),
    wind_speed DECIMAL(5, 2),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabela para dados de tráfego
CREATE TABLE IF NOT EXISTS traffic_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    origin VARCHAR(255),
    destination VARCHAR(255),
    distance DECIMAL(10, 2),
    duration INT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Exemplo de inserção de dados de clima
--INSERT INTO weather_data (temperature, humidity, wind_speed)
--VALUES
    --(25.5, 65.2, 12.3),
    --(22.8, 70.5, 10.1);

-- Exemplo de inserção de dados de tráfego
--INSERT INTO traffic_data (origin, destination, distance, duration)
--VALUES
    --('Origem A', 'Destino B', 30.5, 45),
    --('Origem C', 'Destino D', 15.2, 20);
