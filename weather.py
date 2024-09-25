import requests
import json
city = input("Enter a city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e0d2559fc52f1229efca72b93176606d"

response = requests.get(url)
python_json=json.loads(response.text)
if python_json['cod'] == '404':
    print("please enter valid city name")
else:
    main=python_json['main']
    weather=python_json['weather'][0]
    print(f"the temp of {city} is {round(main['temp']-273,2)} degree centigrade")
    print("the more information given is below")
    print(f"Humidity->{main['humidity']}%")
    print(f"Description-> {weather['description']}")
    print(f"Max Temp-> {round(main['temp_max']-273,2)} degree centigrade")
    print(f"Min Temp-> {round(main['temp_min']-273,2)} degree centigrade")
    
 
    
    