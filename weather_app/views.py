from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.cache import cache
from .functions import WeatherData
# Create your views here.


class WeatherView(APIView):
    def get(self, request, city):
        cached_data = cache.get(city)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)
        else:
            weather_data = WeatherData.get_weather_data(city)
            if weather_data:
                cache.set(city, weather_data, timeout=3600)
                return Response(weather_data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)   