import requests

API_KEY = "b3cd27a767f9224903108f9b96c44e94"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name : ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']

    print(weather)
    print(temperature)
else:
    print("An Error occured") 
