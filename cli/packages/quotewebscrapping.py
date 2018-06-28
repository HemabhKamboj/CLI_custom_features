import requests
from bs4 import BeautifulSoup

def run(resource):
    soup = BeautifulSoup(resource.text, 'lxml')

    quote = soup.find('img',{'class':'p-qotd'}) 
    print(quote['alt'])

def run_quotewebscrapping():
    resource = requests.get('https://www.brainyquote.com/quotes_of_the_day.html')
    run (resource)