import requests
from bs4 import BeautifulSoup

resource = requests.get('https://www.brainyquote.com/quotes_of_the_day.html')
soup = BeautifulSoup(resource.text, 'lxml')

quote = soup.find('img',{'class':'p-qotd'})
print(quote['alt'])