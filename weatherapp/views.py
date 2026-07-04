from django.shortcuts import render
import requests
import datetime

def home(request):
    # Get city from form, default to 'Mingora'
    city = request.POST.get('city', 'Mingora')
    
    # API configuration
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': '6fed475361281eb2377e12aceb8c018e',
        'units': 'metric'
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:
            context = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temp': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'day': datetime.date.today(),
            }
        else:
            context = {'error': 'City not found. Please check the spelling!'}
            
    except Exception as e:
        context = {'error': 'Connection failed. Please check your internet.'}

    return render(request, 'weatherapp/index.html', context)