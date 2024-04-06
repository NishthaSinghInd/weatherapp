from django.shortcuts import render
import requests
import datetime 
from django.http import JsonResponse

# Function to fetch weather data from API
def get_weather_data(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=6a8c2720970c1dd78fb680438474bc0d'
    params = {'units': 'metric'}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST['cityName']
    else: 
        city='indore'

    # Fetch weather data
    weather_data = get_weather_data(city)

    if weather_data:
        description = weather_data['weather'][0]['description']
        icon = weather_data['weather'][0]['icon']
        temp = weather_data['main']['temp']
        day = datetime.datetime.today()
        return render(request, 'result.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city': city})
    else:
        error_message = f"Failed to fetch weather data for {city}. Please try again later."
        return render(request, 'result.html', {'error_message': error_message})


def page(request):
    return render(request, 'index.html')
