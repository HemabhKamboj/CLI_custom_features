import requests

def run (res):
    data = res.json()
    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]
    url ='http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=b4bacbe2dc824431289800439f1ec3df&units=metric'.format(latitude, longitude)

    res1 = requests.get(url)
    data = res1.json()
    wind_speed = data['wind']['speed']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']

    print('Temperature :{} degree celsius'.format(temp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Description :{}'.format(description))

def run_openweatherapi():
    res = requests.get('https://ipinfo.io/')
    run (res)