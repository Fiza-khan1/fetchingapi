from django.shortcuts import render
import urllib.request  
from django.http import JsonResponse
import json
import requests

def home(request):
    if request.method=='POST':
        city=request.POST.get('city','True')
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial&appid=00cef32dcaf01cc7d447c2bf1a7f452c').read()  
        list_of_data = json.loads(source)  
        context = {  
            'city': city,  
            "country_code": str(list_of_data['sys']['country']),  
            "coordinate": str(list_of_data['coord']['lon']) + ' '  
                            + str(list_of_data['coord']['lat']),  
            "temp": str(list_of_data['main']['temp']) + 'k',  
            "pressure": str(list_of_data['main']['pressure']),  
            "humidity": str(list_of_data['main']['humidity']),  
        }  

    else:  
        context = {}  
    return render(request,'index.html',context)



    
