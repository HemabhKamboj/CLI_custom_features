from selenium import webdriver
import wikipediaapi
import requests


def run_wiki():

    wiki_wiki = wikipediaapi.Wikipedia('en')
    item = input("\n Enter the Topic : ")
    
    page = wiki_wiki.page(item)
    print("Page - Exists: %s" % page.exists())
    if(page.exists()==False):
        print("No page found")
    else:
        print("Title: %s" % page.title)
        print("Summary: %s" % page.summary[0:60])
        input("press any key to open url")
        url = page.fullurl
        driver = webdriver.Chrome()
        driver.get(url)
        print(url)
        
        print(page.canonicalurl)
      