from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

#request to make a request to api

import requests
#import decouple so that we can pull values from env
from decouple import config
  
def index(request):
    if request.method == 'POST':
       
        city = request.POST['city']
        
        r = requests.get('http://dataservice.accuweather.com/forecasts/v1/daily/5day/'+city+'?apikey='+config("API_KEY"))
        data=r.json()
        print(data)
        # converting JSON data to a dictionary
        final=data["DailyForecasts"][:3]
        print(type(final))
        
        # data for variable list_of_data
        # data = {z
        #     "country_code": str(list_of_data['sys']['country']),
        #     "coordinate": str(list_of_data['coord']['lon']) + ' '
        #                 + str(list_of_data['coord']['lat']),
        #     "temp": str(list_of_data['main']['temp']) + 'k',
        #     "pressure": str(list_of_data['main']['pressure']),
        #     "humidity": str(list_of_data['main']['humidity']),
        # }
        
    else:
        final =[]
    return render(request, "main/index.html", {"data":final})