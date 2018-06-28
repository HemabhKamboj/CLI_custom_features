import requests
from pprint import pprint

def run (res):
    data = res.json()
    country = data['country']
    url = 'https://newsapi.org/v2/top-headlines?''country={}&''apiKey=29cc4d194a15470db46f37d7f30a5178'.format(country)
    response = requests.get(url)
    pprint (response.json())

def run_newsapi():
    res = requests.get('https://ipinfo.io/')
    run(res)