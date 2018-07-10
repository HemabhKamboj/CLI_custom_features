from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def run_hackathon():
    browser = webdriver.Chrome()
    browser.get('https://www.hackerearth.com/challenges/')
    res = browser.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(res , 'lxml')
    box = soup.find('div',{'class':'upcoming challenge-list'})
    tiles = box.find_all('div',{'class': 'challenge-card-modern'})

    for i,item in enumerate(tiles,1):
        name = item.find('span',{'class':'challenge-list-title challenge-card-wrapper'}).text.strip()
        start = item.find('div',{'class':'date'}).text.strip()
        typ = item.find('div',{'class':'challenge-type'}).text.strip()
        print ( "{}.{}  \n  {}\n  {}\n".format(i, name, typ,start))
    browser.close()