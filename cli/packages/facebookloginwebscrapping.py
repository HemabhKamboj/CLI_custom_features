from selenium import webdriver
from getpass import getpass

def send_details(usr,pwd, browser):
    usr_nm = browser.find_element_by_id('email')
    pass_nm = browser.find_element_by_id('pass')
    login_btn =browser.find_element_by_id('u_0_2')
    usr_nm.send_keys(usr)
    pass_nm.send_keys(pwd)
    login_btn.submit()
    choice = input("Enter anything to exit: ")

def facebook():
    usr = input("Enter  username:")
    pwd = getpass("password: ")
    browser = webdriver.Chrome()
    browser.get('https://www.facebook.com/')
    send_details(usr,pwd,browser)
    try:
        browser.close()
    except:
        return
      