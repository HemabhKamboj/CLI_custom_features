import requests
from pprint import pprint

city = input('Enter city: ' )
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=2b515c3a84b41916eaabe59d6b012b62&units=metric'.format(city)
res = requests.get(url)
data = res.json()
temp = data['main']['temp']
pprint(temp)
pprint(data)