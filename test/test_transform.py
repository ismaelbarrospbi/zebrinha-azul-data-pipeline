import pytest
from transform import transform_weather_data

@pytest.fixture
def sample_weather_data():
    return {
        'temperature': 20,
        'humidity': 70,
        'wind_speed': 10
    }

def test_transform_weather_data(sample_weather_data):
    # Teste de transformação dos dados de clima
    transformed_data = transform_weather_data(sample_weather_data)
    assert 'formatted_temperature' in transformed_data
    assert 'formatted_humidity' in transformed_data
    assert 'formatted_wind_speed' in transformed_data
    assert isinstance(transformed_data['formatted_temperature'], str)
    assert isinstance(transformed_data['formatted_humidity'], str)
    assert isinstance(transformed_data['formatted_wind_speed'], str)
