from django.shortcuts import render,redirect, HttpResponseRedirect, reverse
import requests
from django.contrib import messages
# for getting current location of the user
import geocoder
from geopy.geocoders import Nominatim


def index(request):
    return render(request,'weather/index.html')


def home(request):
    g = geocoder.ip('me')
    geolocator = Nominatim(user_agent='http')
    location = geolocator.reverse(g.latlng)
    address = location.raw['address']
    main = address.get('city') 
    if address.get('city'):
        main = address.get('city') 
    elif address.get('state'):
        main = address.get('state')


    if request.method == "POST":
        city = request.POST.get('city')
        print(len(city),main)
        if(city== ""):
            new_city=main
        else:
            new_city = city
        print(new_city)
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=7d52319e84228356ec16d3b335a712b5&units=metric'
        r = requests.get(url.format(new_city)).json()
        print(r['cod'])
        if r['cod'] != 200:
            print("inside cod")
            return render(request, 'weather/weather.html',{'messages' : f"No results found"})
        print('outside cod')
        weather_data = {
            'temp': round(r['main']['temp']),
            'desc': r['weather'][0]['description'],
            'city': r['name']
        }
        context = {
            'weather_data': weather_data, 
        }
    else:
        context ={
            'weather_data':{
                
            }
        }
    return render(request,'weather/weather.html',context)
            

    
    

def description(request):
    return redirect(request, 'weatherdesc.html')