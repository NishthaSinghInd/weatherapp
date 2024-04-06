from django.shortcuts import render
import requests
import datetime 

# Create your views here.
def home(request):
    if 'cityName' in requests.POST:
        city = request.POST['cityName']
    else:
        city = 'indore'
    


    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=6a8c2720970c1dd78fb680438474bc0d'
    PARAMS = {'units':'metric'}
    data =request.get(url,PARAMS).json()
    description =data['weather'][0]['description']
    icon=data['weather'][0]['icon']
    temp=data['main']['temp']
    day = datetime.data.today()
    return render(request,'index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city})
   
def page(req):
    return render(req,'index.html')