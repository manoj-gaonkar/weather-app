from django.shortcuts import render
import requests

def home(request):
    if request.method == "POST":
        city = request.POST.get('city')
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=7d52319e84228356ec16d3b335a712b5&units=metric'
        r = requests.get(url.format(city)).json()
        weather_data = {
            'temp': round(r['main']['temp']),
            'desc': r['weather'][0]['description']
        }
        print(r)
        context = {
            'weather_data': weather_data, 

        }


        return render(request, 'weather/weather.html',context)
    else:
        return render(request, 'weather/weather.html')

def description(request):
    return render(request, 'weatherdesc.html')