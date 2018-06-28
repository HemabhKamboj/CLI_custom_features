import requests
from pprint import pprint

def run(title):
    url = 'http://www.omdbapi.com/?t={}&apikey=2bf615e8'.format(title)
    res = requests.get(url)
    data = res.json()
    pprint(data)

def run_movieapi():
    title = input('Enter movie title: ' )
    run(title)