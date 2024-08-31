import requests
from django.conf import settings

class WeatherData:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    API_KEY = settings.WEATHER_API_KEY
    
    @staticmethod
    def get_weather_data(city):
        params = {
            "q": city,
            "appid": WeatherData.API_KEY,
            "units": "metric"
        }
        response = requests.get(WeatherData.BASE_URL, params=params)
        if response.status_code == 200:
            return response.json()
        return None