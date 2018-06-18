import requests
from pprint import pprint

res = requests.get('https://ipinfo.io/')
data = res.json()
print(data)
country = data['country']
url = 'https://newsapi.org/v2/top-headlines?''country={}&''apiKey=29cc4d194a15470db46f37d7f30a5178'.format(country)
response = requests.get(url)
pprint (response.json())
