import requests
import datetime
from django.shortcuts import render


# Create your views here.
def index(request):
    url = "https://samples.openweathermap.org/data/2.5/weather?q=Kathmandu,NP&appid=db7ecc652d36495208b6e49bf523d634"
    city = "Kathmandu, NP"
    r = requests.get(url.format(city)).json()
    #To get current date of the location
    currentDT = datetime.datetime.now()
    celTemp =int(r['main']['temp'] - 273.15)
    #cconverison of kelvin ot degree celcius

    city_weather = {
        'city': city,
        'temperature': celTemp,
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
        'day': currentDT.strftime("%A"),
        'date': currentDT.strftime("%B %d, %Y"),
        'time': currentDT.strftime("%I:%M %p"),

    }
    context = {
        'city_weather': city_weather
    }
    print(city_weather)
    return render(request, "weather/weather.html", context)
