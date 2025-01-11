from django.shortcuts import render
from .weather_api import get_weather


def weather_view(request):
    if request.method == "POST":
        city = request.POST.get("city")
        weather_data = get_weather(city)
        
        if weather_data:
            context = {
                'city': city,
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'humidity': weather_data['main']['humidity'],
                'wind_speed': weather_data['wind']['speed'],
                'weather_icon': weather_data['weather'][0]['icon'],
            }
        else:
            context = {'error': 'City not found or invalid.'}
    else:
        context = {}

    return render(request, 'weather.html', context)


