-- Criar banco de dados
CREATE DATABASE IF NOT EXISTS zebrinha_azul;

-- Usar o banco de dados criado
USE zebrinha_azul;

-- Criar tabela de dados de clima
CREATE TABLE IF NOT EXISTS weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(100),
    weather VARCHAR(255),
    temperature FLOAT,
    timestamp DATETIME
);

-- Criar tabela de dados de trânsito
CREATE TABLE IF NOT EXISTS traffic_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    summary VARCHAR(255),
    legs JSON,
    timestamp DATETIME
);
