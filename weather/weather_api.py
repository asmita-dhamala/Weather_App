# weather/weather_api.py
import requests


API_KEY = 'd94774135c0fbebd9a08647b46b30fc9'

# API_KEY = 'https://api.openweathermap.org/data/2.5/weather?q=Kathmandu&appid=d94774135c0fbebd9a08647b46b30fc9'  # Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    url = f'{BASE_URL}?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None
